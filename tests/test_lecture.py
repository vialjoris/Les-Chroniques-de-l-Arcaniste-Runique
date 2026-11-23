"""Régressions éditoriales et lecteur : python3 -m unittest discover -s tests -v."""

import base64
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

from lecture_support import ROOT_CLASSES, Document, compact, digest, historical_prefix, manifest, semantic_classes, table_cells


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = json.loads((Path(__file__).parent / "fixtures/roman_avant.json").read_text(encoding="utf-8"))
SCRIPT = ROOT / "scripts/generer_lecture.py"


def read_exact(path):
    return Path(path).read_bytes().decode("utf-8")


class AnalyseurTests(unittest.TestCase):
    def test_plages_racines_avec_div_imbrique_commentaire_et_attribut_cite(self):
        window = '<div class="system-window" title="a > b"><div class="system-header">Titre</div><!-- </div> -->fin<div><span>6★ +15 30 %</span></div></div>'
        source = "avant\r\n" + window + "\r\naprès"
        document = Document(source)
        self.assertEqual(document.outside_segments(), ["avant\r\n", "\r\naprès"])
        node = document.windows[0]
        self.assertEqual(source[node.start:node.end], window)
        self.assertIn("fin", node.text())

    def test_normalisation_limitee_aux_espaces_entites_et_decors_de_header(self):
        before = '<div class="system-window"><div class="system-header">✦ Titre ◆ ✓</div><p>★LÉGENDAIRE★ 6★ +15 30 % &amp; 1 200 ✦</p></div>'
        after = '<div class="system-window"><div class="system-header"><svg aria-hidden="true"><title>Décor ignoré</title></svg>Titre</div>\n<p>★LÉGENDAIRE★ 6★ +15 30 % &#38; 1\n200 ✦</p></div>'
        text = lambda source: compact(Document(source).windows[0].text())
        self.assertEqual(text(before), text(after))
        for token in ("6★", "+15", "30 %", "1 200", "✦</p>"):
            with self.subTest(token=token):
                self.assertNotEqual(text(before), text(before.replace(token, "")))
        self.assertNotEqual(text(before), text(before.replace("1 200", "1200")))

    def test_deplacement_de_texte_entre_segments_est_detecte(self):
        window = '<div class="system-window">texte</div>'
        before, after = Document("a" + window + "bc"), Document("ab" + window + "c")
        self.assertEqual(before.outside_windows(), after.outside_windows())
        self.assertNotEqual(before.outside_segments(), after.outside_segments())

    def test_seul_le_summary_de_transcription_est_ignore_pas_les_donnees(self):
        source = '<div class="system-window"><details><summary class="lit-window__transcript-toggle">Interface</summary><summary>CANON 6★</summary><p class="lit-window__transcript-toggle">Mana 1 200</p></details></div>'
        self.assertEqual(Document(source).windows[0].text(), "CANON 6★Mana 1 200")


class AjoutsChapitresTests(unittest.TestCase):
    def setUp(self):
        self.original = ('# Chapitre 1 — Historique\r\nAvant.\r\n'
                         '<div class="system-window" data-window-id="001">Mana 1 200</div>'
                         '\r\nToute la fin historique, même son dernier octet.\r\n')
        self.reference = manifest(self.original)
        self.addition = ('\n---\n\n# Chapitre 2 — Ajout\nTexte nouveau.\n'
                         '<div class="system-window" data-window-id="nouvelle">Mana 2 150</div>\n'
                         '\n---\n\n# Chapitre 3 — Autre ajout\nFin nouvelle.\n')

    def assert_conserved(self, source):
        historical = historical_prefix(source, self.reference)
        check = ConservationManuscritTests()
        check.document = Document(source)
        check.historical = Document(historical)
        check.actual = manifest(historical)
        with patch.dict(REFERENCE, self.reference, clear=True):
            check.test_segments_narratifs_octet_identiques_a_leur_position()
            check.test_fenetres_ordonnees_et_integralite_du_texte_conservees()
            check.test_chapitres_et_repartition_des_fenetres_inchanges()
            check.test_classes_compatibles_et_associations_bonus_texte_valeurs()
            check.test_tables_conservent_lignes_cellules_et_valeurs_associees()
        self.assertEqual(historical.encode("utf-8"), self.original.encode("utf-8"))

    def test_baseline_seule_et_plusieurs_chapitres_ajoutes_acceptes(self):
        self.assert_conserved(self.original)
        self.assert_conserved(self.original + self.addition)

    def test_nouveau_chapitre_avec_ancre_dediee_accepte_sans_perte_octets(self):
        addition = self.addition.replace('# Chapitre 2', '<span id="chapitre-2"></span>\n\n# Chapitre 2')
        self.assert_conserved(self.original + addition)
        with self.assertRaises(ValueError):
            historical_prefix(self.original[:-1] + addition.lstrip("\n"), self.reference)

    def test_texte_arbitraire_autour_ancre_et_numero_incoherent_refuses(self):
        anchor = '<span id="chapitre-2"></span>\n\n'
        for prefix in ("Texte interdit.\n" + anchor,
                       anchor + "Texte interdit.\n",
                       '<span id="chapitre-3"></span>\n\n'):
            with self.subTest(prefix=prefix):
                addition = self.addition.replace("# Chapitre 2", prefix + "# Chapitre 2")
                with self.assertRaises(ValueError):
                    historical_prefix(self.original + addition, self.reference)

    def test_alterations_du_prefixe_et_de_toute_sa_fin_refusees(self):
        variants = {
            "début": self.original.replace("Avant.", "Après."),
            "fenêtre": self.original.replace("1 200", "1 201"),
            "dernier segment": self.original.replace("Toute la fin", "Une autre fin"),
            "dernier caractère narratif": self.original.replace("octet.", "octet!"),
            "dernier octet": self.original[:-1],
            "derniers espaces": self.original.rstrip(),
            "fin entièrement supprimée": self.original[:self.original.index("</div>") + len("</div>")],
        }
        for name, source in variants.items():
            with self.subTest(alteration=name):
                with self.assertRaises((ValueError, AssertionError)):
                    self.assert_conserved(source + self.addition.lstrip("\n"))

    def test_ajout_hors_nouveau_chapitre_ne_devient_pas_une_fin_historique_toleree(self):
        for suffix in ("Narration ajoutée à la fin historique.\n", "\n# Chapitre 1 — Doublon\n"):
            with self.subTest(suffix=suffix):
                with self.assertRaises(ValueError):
                    historical_prefix(self.original + suffix, self.reference)


class ConservationManuscritTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = read_exact(ROOT / "roman.md")
        cls.document = Document(cls.source)
        cls.historical = Document(historical_prefix(cls.source, REFERENCE))
        cls.actual = manifest(cls.historical.source)

    def test_segments_narratifs_octet_identiques_a_leur_position(self):
        packed = base64.b64decode(REFERENCE["outside_segments_sha256_base64"], validate=True)
        expected_count = len(REFERENCE["window_text_sha256"]) + 1
        self.assertEqual(len(packed), expected_count * 32)
        segments = self.historical.outside_segments()
        self.assertEqual(len(segments), expected_count)
        for index, segment in enumerate(segments):
            with self.subTest(segment=index):
                self.assertEqual(digest(segment), packed[index * 32:(index + 1) * 32].hex())

    def test_fenetres_ordonnees_et_integralite_du_texte_conservees(self):
        self.assertEqual(len(self.historical.windows), len(REFERENCE["window_text_sha256"]))
        for index, expected in enumerate(REFERENCE["window_text_sha256"]):
            with self.subTest(fenetre=index + 1):
                self.assertEqual(digest(compact(self.document.windows[index].text())), expected)

    def test_chapitres_et_repartition_des_fenetres_inchanges(self):
        self.assertEqual(self.actual["chapters"], REFERENCE["chapters"])
        self.assertEqual(self.actual["chapter_window_counts"], REFERENCE["chapter_window_counts"])

    def test_classes_compatibles_et_associations_bonus_texte_valeurs(self):
        self.assertEqual(self.actual["bonus_associations_sha256"], REFERENCE["bonus_associations_sha256"])
        classes = [semantic_classes(window) for window in self.historical.windows]
        if self.actual["window_classes_sha256"] != REFERENCE["window_classes_sha256"]:
            # Seules les exceptions de présentation explicitement arbitrées sont admises.
            for allowance in REFERENCE.get("presentation_allowances", []):
                index = allowance["window"] - 1
                badge_class = allowance["class"]
                self.assertIn(badge_class, {"passive-badge"})
                window = self.document.windows[index]
                self.assertEqual(digest(compact(window.text())), REFERENCE["window_text_sha256"][index])
                badges = [node for node in window.descendants() if badge_class in node.classes]
                self.assertEqual(len(badges), 1)
                self.assertEqual(compact(badges[0].text()), allowance["text"])
                self.assertIn(allowance["context"], compact(window.text()))
                del classes[index][badge_class]
        self.assertEqual(digest(json.dumps(classes, sort_keys=True)), REFERENCE["window_classes_sha256"])

    def test_tables_conservent_lignes_cellules_et_valeurs_associees(self):
        self.assertEqual(len(table_cells(self.historical)), REFERENCE["table_count"])
        self.assertEqual(self.actual["tables_sha256"], REFERENCE["tables_sha256"])

    def test_identifiants_fenetres_uniques_types_non_vides_et_couverture_racines(self):
        ids = [window.attrs.get("data-window-id", "").strip() for window in self.document.windows]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))
        historical_ids = ids[:len(REFERENCE["window_text_sha256"])]
        self.assertEqual(set(historical_ids), {f"{number:03d}" for number in range(1, len(historical_ids) + 1)})
        for index, original_id in enumerate(REFERENCE.get("window_ids_before", [])):
            if original_id and re.fullmatch(r"\d{3}", original_id):
                with self.subTest(identifiant_historique=original_id):
                    self.assertEqual(ids[index], original_id)
        for window in self.document.windows:
            with self.subTest(fenetre=window.attrs.get("data-window-id")):
                self.assertTrue(window.attrs.get("data-window-type", "").strip())
                self.assertTrue(window.classes & ROOT_CLASSES)
        modernized = [node for node in self.document.root.descendants() if "lit-window" in node.classes]
        self.assertEqual(modernized, self.document.windows)

    def test_chaque_fenetre_modernisee_a_un_header_et_svg_decoratif_local(self):
        for index, window in enumerate(self.document.windows, 1):
            with self.subTest(fenetre=index):
                self.assertIn("lit-window", window.classes)
                headers = [node for node in window.descendants() if "system-header" in node.classes]
                self.assertEqual(len(headers), 1)
                icons = list(headers[0].descendants("svg"))
                self.assertGreaterEqual(len(icons), 1)
                for svg in window.descendants("svg"):
                    self.assertEqual(svg.attrs.get("aria-hidden"), "true")
                    self.assertEqual(svg.attrs.get("focusable"), "false")
                    self.assertRegex(svg.attrs.get("viewbox", ""), r"^\s*-?[\d.]+[ ,]+-?[\d.]+[ ,]+[\d.]+[ ,]+[\d.]+\s*$")
                for node in window.descendants():
                    self.assertNotIn(node.tag, {"script", "iframe", "object", "embed", "image", "foreignobject"})
                    for key, value in node.attrs.items():
                        self.assertFalse(key.startswith("on"), key)
                        if key in {"src", "srcset"}:
                            # Seule l'exception GitHub contrôlée exhaustivement ci-dessous est admise.
                            identifier = window.attrs["data-window-id"]
                            expected = {"img": ("src", f"assets/fenetres/{identifier}.svg"),
                                        "source": ("srcset", f"assets/fenetres/{identifier}-mobile.svg")}
                            self.assertEqual((key, value), expected.get(node.tag), value)
                        if key in {"href", "xlink:href"}:
                            self.assertTrue(value.startswith("#"), value)
                # La baseline ne contient aucun autre pictogramme : aucun ajout implicite à la whitelist.
                self.assertFalse(any(0x1F000 <= ord(c) <= 0x1FAFF or ord(c) in {0xFE0F, 0x20E3} for c in window.text()))
                self.assertFalse(any(c in headers[0].text() for c in "✦◆✓"))


class StyleTests(unittest.TestCase):
    def test_palette_structure_bonus_et_modes_hors_ligne(self):
        css = re.sub(r"/\*.*?\*/", "", read_exact(ROOT / "style.css"), flags=re.S)
        rules = []
        for match in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
            declarations = dict((key.strip().lower(), value.strip().lower()) for key, value in
                                re.findall(r"([\w-]+)\s*:\s*([^;]+)", match[2]))
            rules.append((match[1].strip(), declarations))

        def values(selector, prop):
            return [declarations[prop] for selectors, declarations in rules
                    if selector in [part.strip() for part in selectors.split(",")] and prop in declarations]

        self.assertIn("#ffffff", values(".lit-window", "background"))
        self.assertIn("#242424", values(".lit-window", "color"))
        self.assertIn("#a17b35", values(".system-header", "color"))
        self.assertTrue(any("#d1ab61" in value for value in values(".lit-window", "border")))
        self.assertTrue(any("#d8bf8f" in value for value in values(".system-header", "border-bottom")))
        runic, temporary = values(".rune-bonus", "color"), values(".temporary-bonus", "color")
        self.assertTrue(runic)
        self.assertTrue(temporary)
        self.assertNotEqual(runic[-1], temporary[-1])
        self.assertRegex(css, r"@media\s+[^{}]*\(\s*max-width\s*:")
        self.assertRegex(css, r"@media\s+print\b")
        self.assertNotRegex(css, r"(?i)@import|https?://|url\(\s*['\"]?//")


class GenerateurTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="lecture tests ")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.source = self.directory / "roman essai.md"
        self.css = self.directory / "style & couleurs.css"
        self.output = self.directory / "lecture essai.html"
        self.source.write_text('# Roman & **titre**\n\n# Chapitre 1 — **Premier**\n\nTexte *important* & clair.\n\n| Valeur | Bonus |\n|---|---|\n| 1 200 | +15 % |\n\n<div class="system-window lit-window"><div class="system-header"><svg aria-hidden="true" focusable="false" viewBox="0 0 24 24"><path d="M1 1h2"/></svg>État &amp; rune</div><table><tr><td>6★</td><td><span class="upgrade-badge">+3</span></td></tr></table></div>\n\n# Chapitre 2 — Suite\n', encoding="utf-8")
        self.css.write_text("body { color: #242424; }", encoding="utf-8")

    def cli(self, *extra, source=None, output=None):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--input", str(source or self.source),
             "--output", str(output or self.output), "--css", str(self.css), *extra],
            cwd=self.directory, capture_output=True, text=True, encoding="utf-8", timeout=30,
        )

    def assert_success(self, process):
        self.assertEqual(process.returncode, 0, process.stderr)

    def test_aide_documente_options_et_codes_sans_generation(self):
        process = self.cli("--help")
        self.assert_success(process)
        for option in ("--input", "--output", "--css", "--check", "--help"):
            self.assertIn(option, process.stdout)
        self.assertIn("Codes de sortie", process.stdout)
        self.assertFalse(self.output.exists())

    def test_arguments_invalides_retournent_2(self):
        self.assertEqual(self.cli("--option-inconnue").returncode, 2)

    def test_erreurs_entree_absente_vide_ou_css_absent_sont_explicites(self):
        for state in ("absent", "vide", "css absent"):
            with self.subTest(etat=state):
                source = self.source
                if state == "absent":
                    source = self.directory / "inexistant.md"
                elif state == "vide":
                    source = self.directory / "vide.md"
                    source.write_text(" \n", encoding="utf-8")
                else:
                    self.css.unlink()
                process = self.cli(source=source)
                self.assertEqual(process.returncode, 1)
                self.assertIn("Erreur", process.stderr)
                self.assertNotIn("Traceback", process.stderr)
                self.assertFalse(self.output.exists())

    def test_sortie_ne_peut_ecraser_source_ni_css(self):
        for protected in (self.source, self.css):
            with self.subTest(fichier=protected.name):
                before = protected.read_bytes()
                process = self.cli(output=protected)
                self.assertEqual(process.returncode, 1)
                self.assertEqual(protected.read_bytes(), before)

    def test_collisions_liens_physiques_ne_modifient_pas_source_ni_css(self):
        for index, protected in enumerate((self.source, self.css)):
            with self.subTest(fichier=protected.name):
                alias = self.directory / f"lien physique {index}.html"
                try:
                    os.link(protected, alias)
                except (OSError, NotImplementedError) as error:
                    self.skipTest(f"Liens physiques indisponibles : {error}")
                before = protected.read_bytes()
                process = self.cli(output=alias)
                self.assertEqual(process.returncode, 1, process.stderr)
                self.assertEqual(protected.read_bytes(), before)
                self.assertEqual(alias.read_bytes(), before)

    def test_generation_deterministe_et_check_necrit_pas(self):
        before = self.source.read_bytes(), self.css.read_bytes()
        missing = self.cli("--check")
        self.assertEqual(missing.returncode, 1)
        self.assertFalse(self.output.exists())
        self.assert_success(self.cli())
        initial = self.output.read_bytes()
        self.assert_success(self.cli())
        self.assertEqual(self.output.read_bytes(), initial)
        self.assert_success(self.cli("--check"))
        self.output.write_bytes(b"derive perime")
        self.assertEqual(self.cli("--check").returncode, 1)
        self.assertEqual(self.output.read_bytes(), b"derive perime")
        self.assert_success(self.cli())
        self.assertEqual(self.output.read_bytes(), initial)
        self.assertEqual((self.source.read_bytes(), self.css.read_bytes()), before)

    def test_html_francais_offline_tables_svg_spans_markdown_et_css_chemin_espaces(self):
        self.assert_success(self.cli())
        document = Document(read_exact(self.output))
        nodes = list(document.root.descendants())
        self.assertEqual(next(node for node in nodes if node.tag == "html").attrs["lang"], "fr")
        self.assertTrue(any(node.tag == "meta" and node.attrs.get("charset", "").lower() == "utf-8" for node in nodes))
        self.assertTrue(any(node.tag == "meta" and node.attrs.get("name") == "viewport" and "width=device-width" in node.attrs.get("content", "") for node in nodes))
        links = [node for node in nodes if node.tag == "link" and node.attrs.get("rel") == "stylesheet"]
        self.assertEqual(len(links), 1)
        url = urlsplit(links[0].attrs["href"])
        self.assertEqual(url.scheme, "")
        self.assertEqual(url.netloc, "")
        self.assertEqual((self.output.parent / unquote(url.path)).resolve(), self.css.resolve())
        self.assertEqual(len(list(document.root.descendants("table"))), 2)
        self.assertEqual(len(list(document.root.descendants("svg"))), 1)
        self.assertEqual([node.text() for node in nodes if "upgrade-badge" in node.classes], ["+3"])
        self.assertIn("Roman & titre", compact(document.root.text()))
        self.assertIn("Texte important & clair.", compact(document.root.text()))
        self.assertNotIn("**", document.root.text())
        self.assertNotIn("*important*", document.root.text())
        self.assertFalse(any(node.tag == "script" for node in nodes))
        navigation = next(document.root.descendants("nav"))
        self.assertEqual([compact(node.text()) for node in navigation.descendants("a")],
                         ["Chapitre 1 — Premier", "Chapitre 2 — Suite"])
        csp = [node.attrs["content"] for node in nodes if node.tag == "meta" and node.attrs.get("http-equiv", "").lower() == "content-security-policy"]
        self.assertEqual(len(csp), 1)
        self.assertIn("default-src 'none'", csp[0])
        for node in nodes:
            for attr in ("src", "href", "xlink:href"):
                if attr in node.attrs:
                    resource = urlsplit(node.attrs[attr])
                    self.assertEqual((resource.scheme, resource.netloc), ("", ""))

    def test_chapitres_du_manuscrit_sommaire_resolu_et_fenetres_conservees(self):
        self.assert_success(self.cli(source=ROOT / "roman.md"))
        document = Document(read_exact(self.output))
        nodes = list(document.root.descendants())
        chapters = [node for node in nodes if node.tag in {"h1", "h2"} and compact(node.text()).startswith("Chapitre ")]
        source_text = read_exact(ROOT / "roman.md")
        expected_chapters = manifest(source_text)["chapters"]
        self.assertEqual([compact(node.text()) for node in chapters], expected_chapters)
        ids = [node.attrs["id"] for node in nodes if "id" in node.attrs]
        self.assertEqual(len(ids), len(set(ids)))
        navs = list(document.root.descendants("nav"))
        self.assertEqual(len(navs), 1)
        links = list(navs[0].descendants("a"))
        epilogues = [node for node in nodes if node.tag in {"h1", "h2"}
                     and compact(node.text()).startswith("Épilogue")]
        expected_navigation = expected_chapters + [compact(node.text()) for node in epilogues]
        self.assertEqual([compact(node.text()) for node in links], expected_navigation)
        self.assertEqual([node.attrs["href"] for node in links],
                         ["#" + node.attrs["id"] for node in [*chapters, *epilogues]])
        for node in document.root.descendants("a"):
            href = node.attrs.get("href", "")
            if href.startswith("#"):
                self.assertIn(href[1:], ids)
        source = Document(source_text)
        self.assertEqual(len(document.windows), len(source.windows))
        self.assertEqual([compact(node.text()) for node in document.windows], [compact(node.text()) for node in source.windows])
        self.assertEqual(table_cells(document), table_cells(source))
        self.assertEqual(len(list(document.root.descendants("svg"))), len(list(source.root.descendants("svg"))))
        self.assertFalse(any(node.tag in {"img", "picture", "source", "details", "summary"} for node in nodes))
        self.assertFalse(any("**" in node.text() for node in nodes if node.tag in {"h1", "h2", "h3"}))

    def test_derive_du_projet_est_regenere_a_l_identique(self):
        process = subprocess.run(
            [sys.executable, str(SCRIPT), "--check"], cwd=self.directory,
            capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        self.assert_success(process)


if __name__ == "__main__":
    unittest.main()
