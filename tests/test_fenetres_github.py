"""Contrats hors réseau de la présentation GitHub, indépendants du filtre distant."""

from collections import Counter
from contextlib import redirect_stderr
import importlib.util
import io
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

from lecture_support import Document, compact, digest, historical_prefix, manifest, before_approved_rune_corrections
import test_lecture as lecture_tests
from test_lecture import REFERENCE


ROOT = Path(__file__).resolve().parents[1]
BASELINE_SHA256 = "aef0ae36950a34bb3bf7cfb1dce08f31c3a282528226fe5ad045e3da8d3d8f23"
SVG_NS = "{http://www.w3.org/2000/svg}"


def read_exact(path):
    return path.read_bytes().decode("utf-8")


def load_generator():
    spec = importlib.util.spec_from_file_location("generer_fenetres", ROOT / "scripts/generer_fenetres.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GitHubFenetreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = read_exact(ROOT / "livre_1_l_ascension_d_une_legende_oubliee.md")
        cls.document = Document(cls.source)

    def test_picture_mobile_et_image_de_secours_avec_transcription_integrale(self):
        allowed_images = []
        allowed_sources = []
        for window in self.document.windows:
            identifier = window.attrs["data-window-id"]
            with self.subTest(fenetre=identifier):
                pictures = list(window.descendants("picture"))
                self.assertEqual(len(pictures), 1)
                picture = pictures[0]
                self.assertIs(picture.parent, window)
                self.assertEqual(picture.classes, {"lit-window__github-picture"})
                self.assertEqual([node.tag for node in picture.children], ["source", "img"])
                mobile, desktop = picture.children
                self.assertEqual(re.sub(r"\s", "", mobile.attrs.get("media", "")), "(max-width:600px)")
                self.assertEqual(mobile.attrs.get("srcset"), f"assets/fenetres/{identifier}-mobile.svg")
                self.assertEqual(desktop.attrs.get("src"), f"assets/fenetres/{identifier}.svg")
                self.assertTrue(desktop.attrs.get("alt", "").strip())
                allowed_images.append(desktop)
                allowed_sources.append(mobile)
                details = list(window.descendants("details"))
                self.assertEqual(len(details), 1)
                self.assertIs(details[0].parent, window)
                self.assertEqual(details[0].classes, {"lit-window__transcript"})
                self.assertNotIn("open", details[0].attrs)
                self.assertEqual([node.tag for node in window.children], ["picture", "details"])
                summaries = list(details[0].descendants("summary"))
                self.assertEqual(len(summaries), 1)
                summary = summaries[0]
                self.assertIs(details[0].children[0], summary)
                self.assertEqual(summary.classes, {"lit-window__transcript-toggle"})
                self.assertEqual(compact("".join(part for part in summary.content if isinstance(part, str))),
                                 "Version textuelle de la fenêtre")
                self.assertEqual(compact(details[0].text()), compact(window.text()))
                self.assertEqual(len(list(details[0].descendants("svg"))), 1)
        # Aucun assouplissement pour une illustration narrative ou une autre image.
        self.assertEqual(list(self.document.root.descendants("img")), allowed_images)
        self.assertEqual(list(self.document.root.descendants("source")), allowed_sources)
        self.assertNotRegex(self.document.outside_windows(), r"!\[[^\]]*\]\(")

    def test_restauration_source_avant_wrappers_octet_identique_et_idempotente(self):
        generator = load_generator()
        restored = generator.extraire_source_fenetres(self.source)
        historical = generator.extraire_source_fenetres(before_approved_rune_corrections(self.source))
        self.assertEqual(digest(historical_prefix(historical, REFERENCE)), BASELINE_SHA256)
        self.assertEqual(generator.extraire_source_fenetres(restored), restored)
        self.assertEqual(Document(restored).outside_segments(), self.document.outside_segments())

    def test_restauration_source_historique_sans_wrapper_inchangee(self):
        source = 'avant\r\n<div class="system-window" data-window-id="001"><p>Mana 1 200 &amp; 6★</p></div>\r\naprès'
        self.assertEqual(load_generator().extraire_source_fenetres(source), source)

    def test_extraction_mixte_restaure_aussi_ancienne_fenetre_sans_identifiant(self):
        generator = load_generator()
        modern = '<div class="system-window lit-window" data-window-id="A"><p>Mana 1 200 &amp; 6★</p></div>'
        legacy = '<div class="system-window lit-window"><p>Ancienne rune +15</p></div>'
        wrapped, _ = generator.produire(modern)
        mixed = "Avant\r\n" + legacy + "\r\nEntre\r\n" + wrapped + "\r\nAprès"
        expected = "Avant\r\n" + legacy + "\r\nEntre\r\n" + modern + "\r\nAprès"
        self.assertEqual(generator.extraire_source_fenetres(mixed), expected)
        self.assertEqual(generator.extraire_source_fenetres(expected), expected)
        # Lire une source historique ne lui impose pas les contraintes du build d'assets.
        with self.assertRaises(ValueError):
            generator.produire(mixed)

    def test_dependances_markdown_et_pillow_conservent_les_versions_approuvees(self):
        requirements = {line.split("#", 1)[0].strip()
                        for line in read_exact(ROOT / "requirements-lecture.txt").splitlines()}
        self.assertIn("Markdown==3.10.2", requirements)
        self.assertIn("Pillow==12.1.1", requirements)

    def test_svg_desktop_mobile_inventaire_dimensions_securite_et_texte_affiche(self):
        expected = {f"{window.attrs['data-window-id']}{suffix}.svg"
                    for window in self.document.windows for suffix in ("", "-mobile")}
        directory = ROOT / "assets/fenetres"
        self.assertEqual({path.name for path in directory.glob("*.svg")}, expected)
        for window in self.document.windows:
            for suffix in ("", "-mobile"):
                name = f"{window.attrs['data-window-id']}{suffix}.svg"
                with self.subTest(svg=name):
                    source = read_exact(directory / name)
                    self.assertNotRegex(source, r"(?i)<!DOCTYPE|<!ENTITY|<\?xml-stylesheet")
                    svg = ET.fromstring(source)
                    self.assertEqual(svg.tag, SVG_NS + "svg")
                    for dimension in ("width", "height"):
                        value = svg.attrib[dimension]
                        self.assertRegex(value, r"^\d+(?:\.\d+)?(?:px)?$")
                        self.assertGreater(float(value.removesuffix("px")), 0)
                    viewbox = [float(value) for value in re.split(r"[\s,]+", svg.attrib["viewBox"].strip())]
                    self.assertEqual(len(viewbox), 4)
                    self.assertGreater(viewbox[2], 0)
                    self.assertGreater(viewbox[3], 0)
                    for node in svg.iter():
                        tag = node.tag.split("}")[-1].lower()
                        self.assertIn(tag, {"svg", "g", "rect", "path", "circle", "text", "tspan", "title", "desc"},
                                      "Primitive SVG non approuvée : contrat passif fermé")
                        for key, value in node.attrib.items():
                            key = key.split("}")[-1].lower()
                            self.assertFalse(key.startswith("on"), key)
                            if key == "href":
                                self.assertTrue(value.startswith("#"), value)
                            self.assertNotRegex(value, r"(?i)(?:https?:|javascript:|data:|file:|@import)")
                            for target in re.findall(r"url\(\s*['\"]?([^)'\"]+)", value, re.I):
                                self.assertTrue(target.startswith("#"), target)
                        if tag == "style":
                            self.assertNotRegex(node.text or "", r"(?i)@import|@font-face|url\(")
                    # Seuls text/tspan sont une preuve d'affichage, jamais title/metadata/commentaire.
                    texts = [node for node in svg.iter(SVG_NS + "text")]
                    self.assertTrue(texts)
                    shown = " ".join("".join(node.itertext()) for node in texts)
                    normalize = lambda text: re.sub(r"\s+", "", text)
                    self.assertEqual(normalize(shown), normalize(window.text()))
                    for node in texts:
                        self.assertNotIn(node.attrib.get("display", ""), {"none"})
                        self.assertNotIn(node.attrib.get("visibility", ""), {"hidden", "collapse"})
                        self.assertNotEqual(node.attrib.get("opacity"), "0")
                    colors = Counter(value.lower() for node in svg.iter() for value in node.attrib.values())
                    for color in ("#ffffff", "#242424", "#d1ab61", "#a17b35", "#d8bf8f"):
                        self.assertGreater(colors[color], 0, color)


class GenerateurFenetreCliTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="fenêtres CLI & ", dir="/tmp/opencode")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        scripts = self.directory / "scripts"
        scripts.mkdir()
        self.script = scripts / "generer_fenetres.py"
        # La CLI déduit sa racine de __file__ : une copie isole toutes ses écritures.
        shutil.copyfile(ROOT / "scripts/generer_fenetres.py", self.script)
        self.manuscript = self.directory / "livre_1_l_ascension_d_une_legende_oubliee.md"
        self.original = ('# Chapitre 1 — Test\n\nAvant & intact.\n\n'
                         '<div class="system-window lit-window" data-window-id="essai-001" data-window-type="system">\n'
                         '<div class="system-header lit-window__header"><svg aria-hidden="true" focusable="false" '
                         'viewBox="0 0 24 24"><path d="M1 1h2"/></svg>État &amp; rune</div>\n'
                         '<p>Mana naturel 1 200 ; <span class="rune-bonus">+30 %</span> ; '
                         'rare (bleue), 6★, <span class="upgrade-badge">+15</span>.</p>\n'
                         '<table><tr><th>Valeur</th><th>Bonus</th></tr><tr><td>2 150</td><td>+60</td></tr></table>\n'
                         '</div>\n\nAprès, inchangé.\n')
        self.manuscript.write_text(self.original, encoding="utf-8")
        self.assets = self.directory / "assets/fenetres"

    def cli(self, *args):
        return subprocess.run([sys.executable, str(self.script), *args],
                              cwd=self.directory, capture_output=True, text=True,
                              encoding="utf-8", timeout=30)

    def snapshot(self):
        return {path.relative_to(self.directory).as_posix(): (path.read_bytes(), path.stat().st_mtime_ns)
                for path in self.directory.rglob("*") if path.is_file()}

    def assert_success(self, process):
        self.assertEqual(process.returncode, 0, process.stderr)

    def test_aide_et_arguments_invalides_sans_ecriture(self):
        before = self.snapshot()
        process = self.cli("--help")
        self.assert_success(process)
        for option in ("--check", "--help"):
            self.assertIn(option, process.stdout)
        self.assertEqual(self.cli("--option-inconnue").returncode, 2)
        self.assertEqual(self.snapshot(), before)

    def test_generation_deterministe_idempotente_et_check_strictement_sans_ecriture(self):
        before = self.snapshot()
        self.assertEqual(self.cli("--check").returncode, 1)
        self.assertEqual(self.snapshot(), before)
        self.assert_success(self.cli())
        generated = self.snapshot()
        self.assertEqual({path.name for path in self.assets.glob("*.svg")},
                         {"essai-001.svg", "essai-001-mobile.svg"})
        self.assertEqual(load_generator().extraire_source_fenetres(read_exact(self.manuscript)), self.original)
        self.assert_success(self.cli())
        self.assertEqual(self.snapshot(), generated)
        self.assert_success(self.cli("--check"))
        self.assertEqual(self.snapshot(), generated)
        # Repartir de la même source produit les mêmes octets, même sans assets préexistants.
        self.manuscript.write_text(self.original, encoding="utf-8")
        shutil.rmtree(self.assets)
        self.assert_success(self.cli())
        self.assertEqual({path: content for path, (content, _) in self.snapshot().items()},
                         {path: content for path, (content, _) in generated.items()})

    def test_check_detecte_svg_manquant_perime_et_enveloppe_absente_sans_reparer(self):
        for state in ("manquant", "périmé", "enveloppe absente"):
            with self.subTest(etat=state):
                self.assert_success(self.cli())
                if state == "manquant":
                    (self.assets / "essai-001-mobile.svg").unlink()
                elif state == "périmé":
                    (self.assets / "essai-001.svg").write_text("périmé", encoding="utf-8")
                else:
                    self.manuscript.write_text(self.original, encoding="utf-8")
                before = self.snapshot()
                process = self.cli("--check")
                self.assertEqual(process.returncode, 1, process.stderr)
                self.assertEqual(self.snapshot(), before)
                self.assert_success(self.cli())
                self.assert_success(self.cli("--check"))

    def test_ajout_decouvert_et_controle_comme_les_fenetres_historiques(self):
        self.original = self.original.replace("essai-001", "001")
        self.manuscript.write_text(self.original, encoding="utf-8")
        self.assert_success(self.cli())
        historical = read_exact(self.manuscript)
        addition = self.original.replace("Chapitre 1", "Chapitre 2").replace('data-window-id="001"', 'data-window-id="ajout-unique"')
        self.manuscript.write_text(historical + "\n---\n\n" + addition, encoding="utf-8")
        before = self.snapshot()
        self.assertEqual(self.cli("--check").returncode, 1)
        self.assertEqual(self.snapshot(), before)
        self.assert_success(self.cli())
        source = read_exact(self.manuscript)
        self.assertTrue(source.startswith(historical))
        check = GitHubFenetreTests()
        check.source, check.document = source, Document(source)
        structure = lecture_tests.ConservationManuscritTests()
        structure.document = check.document

        def validate():
            with patch(__name__ + ".ROOT", self.directory):
                check.test_picture_mobile_et_image_de_secours_avec_transcription_integrale()
                check.test_svg_desktop_mobile_inventaire_dimensions_securite_et_texte_affiche()

        validate()
        structure.test_chaque_fenetre_modernisee_a_un_header_et_svg_decoratif_local()
        with patch.dict(REFERENCE, manifest(self.original), clear=True):
            structure.test_identifiants_fenetres_uniques_types_non_vides_et_couverture_racines()
        added = check.document.windows[-1]
        for attribute in ("data-window-id", "data-window-type"):
            with self.subTest(attribut=attribute):
                saved = added.attrs[attribute]
                added.attrs[attribute] = ""
                try:
                    with patch.dict(REFERENCE, manifest(self.original), clear=True):
                        with self.assertRaises(AssertionError):
                            structure.test_identifiants_fenetres_uniques_types_non_vides_et_couverture_racines()
                finally:
                    added.attrs[attribute] = saved
        for suffix in ("", "-mobile"):
            asset = self.assets / f"ajout-unique{suffix}.svg"
            original = asset.read_bytes()
            with self.subTest(svg=asset.name):
                svg = ET.fromstring(original)
                next(node for node in svg.iter(SVG_NS + "text") if node.text == "150").text = "151"
                asset.write_bytes(ET.tostring(svg, encoding="utf-8"))
                self.assertNotEqual(asset.read_bytes(), original)
                with self.assertRaises(AssertionError):
                    validate()
                asset.write_bytes(original)
        asset = self.assets / "ajout-unique.svg"
        original = asset.read_bytes()
        for tag in ("a", "script", "foreignObject", "image", "animateTransform", "filter", "feImage"):
            with self.subTest(primitive_hostile=tag):
                svg = ET.fromstring(original)
                ET.SubElement(svg, SVG_NS + tag)
                asset.write_bytes(ET.tostring(svg, encoding="utf-8"))
                with self.assertRaises(AssertionError):
                    validate()
                asset.write_bytes(original)
        picture = next(added.descendants("picture"))
        picture.children[1].attrs["src"] = "assets/fenetres/essai-001.svg"
        with self.assertRaises(AssertionError):
            validate()

    def test_entrees_invalides_code_2_sans_ecriture_ni_traceback(self):
        invalid_sources = {
            "absent": None,
            "vide": " \n",
            "aucune fenêtre": "# Texte sans fenêtre\n",
            "identifiant absent": self.original.replace(' data-window-id="essai-001"', ""),
            "identifiant non sûr": self.original.replace("essai-001", "../ailleurs"),
            "identifiant dupliqué": self.original + self.original,
            "racine non fermée": self.original.replace("</div>\n\nAprès", "\n\nAprès"),
        }
        for state, source in invalid_sources.items():
            for arguments in ((), ("--check",)):
                with self.subTest(etat=state, arguments=arguments):
                    if source is None:
                        self.manuscript.unlink(missing_ok=True)
                    else:
                        self.manuscript.write_text(source, encoding="utf-8")
                    before = self.snapshot()
                    process = self.cli(*arguments)
                    self.assertEqual(process.returncode, 2, process.stderr)
                    self.assertIn("Erreur", process.stderr)
                    self.assertNotIn("Traceback", process.stderr)
                    self.assertEqual(self.snapshot(), before)

    def test_svg_obsolete_refuse_sans_suppression_automatique(self):
        self.assert_success(self.cli())
        (self.assets / "obsolete.svg").write_text("à examiner explicitement", encoding="utf-8")
        before = self.snapshot()
        for arguments in ((), ("--check",)):
            with self.subTest(arguments=arguments):
                process = self.cli(*arguments)
                self.assertEqual(process.returncode, 2, process.stderr)
                self.assertIn("obsolete.svg", process.stderr)
                self.assertNotIn("Traceback", process.stderr)
                self.assertEqual(self.snapshot(), before)

    def test_identifiants_distincts_mais_noms_svg_en_collision_refuses_avant_ecriture(self):
        source = self.original.replace("essai-001", "A")
        source += self.original.replace("essai-001", "A-mobile")
        self.manuscript.write_text(source, encoding="utf-8")
        before = self.snapshot()
        for arguments in ((), ("--check",)):
            with self.subTest(arguments=arguments):
                process = self.cli(*arguments)
                self.assertEqual(process.returncode, 2, process.stderr)
                self.assertIn("A-mobile.svg", process.stderr)
                self.assertNotIn("Traceback", process.stderr)
                self.assertEqual(self.snapshot(), before)

    def test_echec_remplacement_atomique_du_manuscrit_preserve_source_et_nettoie_temporaire(self):
        self.assert_success(self.cli())
        self.manuscript.write_text(self.original, encoding="utf-8")
        before = self.snapshot()
        generator = load_generator()
        replacements = []

        def interrupted_replace(temporary, target):
            temporary, target = Path(temporary), Path(target)
            replacements.append(target)
            self.assertEqual(target, self.manuscript)
            self.assertEqual(temporary.parent, target.parent)
            self.assertNotEqual(temporary, target)
            self.assertTrue(temporary.is_file())
            self.assertEqual(generator.extraire_source_fenetres(read_exact(temporary)), self.original)
            self.assertEqual(read_exact(target), self.original)
            raise OSError("Interruption simulée avant remplacement")

        errors = io.StringIO()
        with patch.object(generator, "ROOT", self.directory), \
                patch.object(generator.os, "replace", side_effect=interrupted_replace), \
                redirect_stderr(errors):
            self.assertEqual(generator.main([]), 2)
        self.assertEqual(replacements, [self.manuscript])
        self.assertIn("Interruption simulée", errors.getvalue())
        self.assertNotIn("Traceback", errors.getvalue())
        self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()
