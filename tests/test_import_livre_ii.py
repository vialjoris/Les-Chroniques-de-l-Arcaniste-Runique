"""Contrats métier des trois chapitres validés du livre II."""

from collections import Counter
from pathlib import Path
import hashlib
import re
import unittest

from lecture_support import Document, compact
from test_fenetres_github import load_generator
from test_securite_documents import assert_passive


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "livre_2_le_vertige_des_vies_oubliees.md"
ASSETS = ROOT / "assets/fenetres-livre-2"
ROMANS = (
    ROOT / "livre_1_l_ascension_d_une_legende_oubliee.md",
    SOURCE,
)


def chapters(source):
    matches = list(re.finditer(r"^## Chapitre (\d+) — ([^\n]+)$", source, re.M))
    return {
        int(match[1]): source[match.start():matches[index + 1].start()
                              if index + 1 < len(matches) else len(source)]
        for index, match in enumerate(matches)
    }


def archive_chapter_2(archive):
    """Sélectionner la dernière transmission complète par ancres, jamais par lignes."""
    heading = re.compile(r"^# \*\*Chapitre 2 — Les prodiges de l'Académie\*\*$", re.M)
    ending = re.compile(r"^\*Fin du chapitre 2 — Les prodiges de l'Académie\*$", re.M)
    candidates = []
    for start in heading.finditer(archive):
        end = ending.search(archive, start.end())
        if end:
            block = archive[start.start():end.end()]
            if len(re.findall(r"^## \*\*[IVX]+\.", block, re.M)) == 12:
                candidates.append(block)
    if not candidates:
        raise ValueError("Transmission complète du chapitre 2 introuvable")
    return candidates[-1]


def rune_ids(document):
    return [node.attrs["data-rune-id"] for node in document.root.descendants()
            if "data-rune-id" in node.attrs]


def rune_identity(value):
    match = re.fullmatch(
        r"(.+?) (commune|peu commune|rare|épique|légendaire) \(([^)]+)\), (\d)★, (\+\d+)",
        compact(value),
    )
    if not match:
        raise ValueError(f"Identité runique illisible : {value!r}")
    return match.groups()


def rune_record(identity, main, secondaries):
    ensemble, rarity, color, stars, upgrade = rune_identity(identity)
    return {
        "ensemble": ensemble,
        "rareté": rarity,
        "couleur": color,
        "étoiles": stars,
        "amélioration": upgrade,
        "principale": compact(main),
        "secondaires": tuple(part.strip() for part in compact(secondaries).split(" ; ")),
    }


def chapter_3_equipment(source):
    document = Document(source)
    windows = [window for window in document.windows
               if window.attrs.get("data-window-id") == "L2-C3-F04"]
    if len(windows) != 1:
        raise ValueError(f"L2-C3-F04 attendue une fois, trouvée {len(windows)} fois")
    records = {}
    for row in windows[0].descendants("tr"):
        identifier = row.attrs.get("data-rune-id")
        if not identifier:
            continue
        cells = list(row.descendants("td"))
        if len(cells) != 3:
            raise ValueError(f"Fiche {identifier} : trois cellules attendues")
        if identifier in records:
            raise ValueError(f"Fiche dupliquée : {identifier}")
        records[identifier] = rune_record(*(cell.text() for cell in cells))
    return records


def lore_chapter_3_equipment(lore):
    heading = "### Livre II, vie 2 — équipement de 32 runes au chapitre 3 (DEC-183)"
    start = lore.index(heading)
    end_match = re.search(r"^## ", lore[start + len(heading):], re.M)
    end = len(lore) if end_match is None else start + len(heading) + end_match.start()
    records = {}
    for line in lore[start:end].splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 5 or not re.fullmatch(r"`L2-HAS-R\d+`", cells[0]):
            continue
        identifier = cells[0].strip("`")
        if identifier in records:
            raise ValueError(f"Fiche dupliquée dans le lore : {identifier}")
        records[identifier] = rune_record(
            f"{cells[1]}, {cells[2]}", cells[3], cells[4]
        )
    return records


def assert_unbreakable_values(case, source):
    for value in re.findall(r"(?:\d(?:[\d ]*\d)?)(?: %| (?=\d{3}\b))", source):
        case.fail(f"Valeur numérique sécable dans une fenêtre : {value!r}")


class ImportLivreIITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.document = Document(cls.source)
        cls.parts = chapters(cls.source)
        cls.windows = {window.attrs["data-window-id"]: window
                       for window in cls.document.windows}

    def test_sommaire_ancres_et_trois_chapitres_structures(self):
        titles = re.findall(r"^## (Chapitre (\d+) — [^\n]+)$", self.source, re.M)
        self.assertEqual([number for _, number in titles], ["1", "2", "3"])
        links = re.findall(r"^(\d+)\. \[([^\n]+)\]\(#chapitre-(\d+)\)$", self.source, re.M)
        self.assertEqual(links, [(number, title, number) for title, number in titles])
        self.assertEqual(re.findall(r'<span id="chapitre-(\d+)"></span>', self.source),
                         ["1", "2", "3"])
        expected = {1: 9, 2: 12, 3: 18}
        for number, count in expected.items():
            sections = re.findall(r"^### ([IVX]+)\.", self.parts[number], re.M)
            self.assertEqual(len(sections), count)
            self.assertEqual(len(sections), len(set(sections)))
        self.assertNotRegex(self.source, r"(?im)^#+\s*(?:\*\*)?Chapitre\s+4\b")

    def test_chapitre_1_valide_reste_identique_a_la_reference_preexistante(self):
        self.assertEqual(hashlib.sha256(self.parts[1].encode()).hexdigest(),
                         "999491e2506c8e92ac6f4b44f3e2676207b2eef175d85b636c82f8c366ec145a")

    def test_archive_chapitre_2_est_bornee_par_ancres_sans_absorber_les_appends(self):
        archive = (ROOT / "docs/new.txt").read_text(encoding="utf-8")
        block = archive_chapter_2(archive)
        self.assertTrue(block.startswith("# **Chapitre 2 — Les prodiges de l'Académie**"))
        self.assertTrue(block.endswith("*Fin du chapitre 2 — Les prodiges de l'Académie*"))
        self.assertEqual(len(re.findall(r"^## \*\*[IVX]+\.", block, re.M)), 12)
        self.assertNotIn("Chapitre 3 — Celle qui n'était pas dans les bois", block)
        self.assertNotIn("Passif amélioré", block,
                         "Les retouches postérieures ne doivent pas être absorbées dans l'archive")

    def test_chapitre_2_preserve_les_ancres_narratives_hors_retouches_autorisees(self):
        archive = archive_chapter_2((ROOT / "docs/new.txt").read_text(encoding="utf-8"))
        destination = compact(Document(load_generator().extraire_source_fenetres(
            self.parts[2])).root.text())
        retouched_topics = (
            "Samia", "Yoon", "Bénédiction", "Croissance", "Ranger", "rune", "Rune",
            "Orven", "cercle", "Cercle", "boss", "Boss", "gobelin", "portail", "Portail",
            "invulnérable", "compétence", "quarante-cinq pour cent", "vingt-cinq pour cent",
        )
        anchors = []
        for paragraph in re.split(r"\n\s*\n", archive):
            text = compact(re.sub(r"[*#]", "", Document(paragraph).root.text()))
            if len(text) >= 120 and not any(topic in text for topic in retouched_topics):
                anchors.append(text)
        self.assertGreaterEqual(len(anchors), 30)
        cursor = 0
        for anchor in anchors:
            found = destination.find(anchor, cursor)
            self.assertGreaterEqual(found, cursor, anchor[:160])
            cursor = found + len(anchor)

    def test_samia_classe_ciblee_par_livre_sans_effacer_zephyr_ni_le_futur(self):
        book_i = ROMANS[0].read_text(encoding="utf-8")
        system = (ROOT / "lore/systeme.md").read_text(encoding="utf-8")
        text_ii = compact(Document(self.parts[2]).root.text())
        self.assertIn("Samia Claire. Classe : Marcheuse du voile. Rang : Commun.", text_ii)
        self.assertIn("Marcheuse du voile commune, qui représente cinq points", text_ii)
        self.assertIn("Samia Claire : Éclaireuse, commune — 5 points", compact(Document(book_i).root.text()))
        self.assertIn("Zéphyr Claire", self.source)
        self.assertIn("La fille du Ranger, Samia", self.parts[2])
        self.assertIn("Exécutrice astrale de rang Astral", system)
        self.assertNotIn("Samia Claire. Classe : Ranger astral", text_ii)

    def test_quatre_pouvoirs_de_samia_et_limites_sont_presents(self):
        for name in ("Écho des Mondes", "Vision du Voile", "Flèche du Néant", "Pas du Voile"):
            self.assertIn(name, self.parts[2])
        for limit in ("zones qu'elle avait réellement explorées", "ni heure d'apparition ou d'ouverture",
                      "ne traverse donc pas les obstacles", "ni invisible ni immunisée"):
            self.assertIn(limit, self.parts[2])

    def test_yoon_progresse_jusqu_au_niveau_40_sans_anticiper_50_60(self):
        joined = self.parts[2] + self.parts[3]
        expected = ((10, "Sceau de lucidité"), (20, "Domaine des Entraves runiques"),
                    (30, "Marque runique"), (40, "Résonance runique"))
        for level, name in expected:
            self.assertRegex(joined, rf"(?s)Niveau {level} atteint.*?{re.escape(name)}")
        self.assertIn("Évolution de Résonance runique · Actif ciblé", self.parts[3])
        self.assertNotIn("Résonance supérieure", joined)
        self.assertNotIn("Tempête runique", joined)
        self.assertNotIn("Convergence runique", joined)
        system = (ROOT / "lore/systeme.md").read_text(encoding="utf-8")
        self.assertRegex(system, r"Tempête runique[^\n]*Niveau 50")
        self.assertRegex(system, r"Convergence runique[^\n]*Niveau 60")

    def test_vague_legendaire_et_chant_conservent_leurs_limites(self):
        text = compact(self.windows["L2-C2-F08"].text())
        for value in ("10 % des PV maximaux de Yoon toutes les cinq secondes",
                      "Coût : 5 Mana", "Portée : 10 mètres", "Incantation : 5 secondes",
                      "Aucun temps de recharge", "20 % de la Puissance arcanique de Yoon",
                      "plus faible pourcentage de PV actuels, Yoon comprise",
                      "5 % des PV maximaux de Yoon"):
            self.assertIn(value, text)

    def test_benediction_ne_revele_aucun_taux_exact_a_hasol(self):
        visible = compact(Document(self.parts[2]).root.text())
        self.assertEqual(visible.count("Passif amélioré"), 2)
        self.assertNotRegex(visible, r"(?:45|25|60|50)\s*%[^.]{0,80}(?:échec|résultat)")
        self.assertNotRegex(visible.lower(), r"(?:quarante-cinq|vingt-cinq|soixante|cinquante) pour cent")
        lore = (ROOT / "lore/systeme.md").read_text(encoding="utf-8")
        for rate in ("45 %", "25 %", "60 %", "50 %"):
            self.assertIn(rate, lore)

    def test_croissance_astrale_distingue_compteurs_et_conditions(self):
        text = compact(self.parts[1] + self.parts[2] + self.parts[3])
        self.assertIn("Boss de donjon et de portail achevés personnellement", text)
        self.assertIn("Démons éliminés personnellement dans les portails", text)
        self.assertIn("aucune condition de niveau", text)
        self.assertIn("hors portails", text)
        book_i = compact(Document(ROMANS[0].read_text(encoding="utf-8")).root.text())
        self.assertNotIn("Boss de donjon et de portail achevés personnellement", book_i)

    def test_chapitre_3_niveau_siphon_compteurs_et_equipement(self):
        siphon = compact(self.windows["L2-C3-F01"].text())
        for value in ("39 → 40", "120 % de la PA", "75 % des dégâts infligés", "8 mètres",
                      "100 Mana", "20 secondes", "1 200 Mana"):
            self.assertIn(value, siphon)
        growth = compact(self.windows["L2-C3-F03"].text())
        for value in ("10 000", "200", "90 000", "2", "30", "32"):
            self.assertIn(value, growth)
        equipment = compact(self.windows["L2-C3-F04"].text())
        self.assertIn("Niveau 40 · Runes équipées 32/32", equipment)
        self.assertIn("8 Vol de vie · 8 Arcanique · 8 Vitesse · 2 Énergie · 2 Gardien · 4 Fatal", equipment)
        self.assertIn("Bonus d'ensemble actifs : 9", equipment)

    def test_chapitre_3_alpha_deux_frappes_sans_chiffres_inventes_et_fin_exacte(self):
        alpha = self.parts[3][self.parts[3].index("Le loup alpha se tenait entre les arbres."):
                              self.parts[3].index("### XVII. Le courage de Ray")]
        self.assertIn("frappa une première fois", alpha)
        self.assertIn("une seconde frappe", alpha)
        self.assertIn("Deux coups d'épée", alpha)
        self.assertNotRegex(alpha, r"\b(?:PV|dégâts|niveau)\s*[:=]?\s*\d")
        self.assertEqual(len(re.findall(r"\bDONG\b", self.parts[3])), 12)
        self.assertEqual(len(re.findall(r"\bDING\b", self.parts[3])), 2)
        self.assertTrue(self.parts[3].rstrip().endswith(
            "*Fin du chapitre 3 — Celle qui n'était pas dans les bois.*"))

    def test_vingt_six_fenetres_et_cinquante_deux_svg_derives(self):
        ids = [window.attrs["data-window-id"] for window in self.document.windows]
        self.assertEqual(len(ids), 26)
        self.assertEqual(len(ids), len(set(ids)))
        files = {path.name for path in ASSETS.glob("*.svg")}
        expected = {identifier + suffix + ".svg" for identifier in ids for suffix in ("", "-mobile")}
        self.assertEqual(files, expected)
        self.assertEqual(len(files), 52)

    def test_generation_livre_ii_idempotente_et_derives_identiques(self):
        generated, images = load_generator().produire(self.source)
        self.assertEqual(generated.replace("assets/fenetres/", "assets/fenetres-livre-2/"), self.source)
        self.assertEqual(set(images), {path.name for path in ASSETS.glob("*.svg")})
        self.assertEqual(len(images), 52)
        for name, content in images.items():
            self.assertEqual((ASSETS / name).read_text(encoding="utf-8"), content)

    def test_manuscrit_passif(self):
        assert_passive(self, self.source)


class IdentifiantsRunesTests(unittest.TestCase):
    def setUp(self):
        self.sources = {path.name: path.read_text(encoding="utf-8") for path in ROMANS}
        self.documents = {name: Document(source) for name, source in self.sources.items()}
        self.lore = (ROOT / "lore/runes.md").read_text(encoding="utf-8")

    def test_decouverte_dynamique_et_associations_machine_lore(self):
        discovered = {identifier for document in self.documents.values()
                      for identifier in rune_ids(document)}
        self.assertGreater(len(discovered), 40)
        self.assertTrue(any(identifier.startswith("L2-") for identifier in discovered))
        self.assertTrue(any(not identifier.startswith("L2-") for identifier in discovered))
        for identifier in discovered:
            with self.subTest(rune=identifier):
                self.assertIn(identifier, self.lore)

    def test_ids_absents_du_visible_html_svg_et_lecteur(self):
        for name, document in self.documents.items():
            visible_manuscript = compact(document.root.text())
            for identifier in set(rune_ids(document)):
                self.assertNotIn(identifier, visible_manuscript, name)
            for window in document.windows:
                ids = rune_ids(Document(document.source[window.start:window.end]))
                visible = compact(window.text())
                for identifier in ids:
                    self.assertNotIn(identifier, visible, (name, window.attrs["data-window-id"]))
                    for suffix in ("", "-mobile"):
                        directory = "fenetres-livre-2" if name.startswith("livre_2") else "fenetres"
                        svg = (ROOT / "assets" / directory /
                               f"{window.attrs['data-window-id']}{suffix}.svg").read_text(encoding="utf-8")
                        self.assertNotIn(identifier, svg)
        reader = (ROOT / "lecture.html").read_text(encoding="utf-8")
        for identifier in set(rune_ids(self.documents[ROMANS[0].name])):
            self.assertNotIn(identifier, compact(Document(reader).root.text()))

    def test_mutations_suppression_permutation_et_reintroduction_visible_detectees(self):
        fixture = ('<table><tr data-rune-id="ALPHA-R001"><td>Fatal</td></tr>'
                   '<tr data-rune-id="ZX-LOT-77"><td>Gardien</td></tr></table>')

        def validate(source):
            document = Document(source)
            ids = rune_ids(document)
            self.assertEqual(ids, ["ALPHA-R001", "ZX-LOT-77"])
            visible = compact(document.root.text())
            self.assertTrue(all(identifier not in visible for identifier in ids))

        validate(fixture)
        mutations = (
            fixture.replace(' data-rune-id="ALPHA-R001"', "", 1),
            fixture.replace("ALPHA-R001", "TEMP").replace("ZX-LOT-77", "ALPHA-R001").replace("TEMP", "ZX-LOT-77"),
            fixture.replace("<td>Fatal</td>", "<td>ALPHA-R001 · Fatal</td>"),
        )
        for mutation in mutations:
            with self.subTest(mutation=mutation), self.assertRaises(AssertionError):
                validate(mutation)

    def test_32_fiches_vie_2_concordent_entierement_avec_le_referentiel_lore(self):
        window = next(w for w in self.documents[ROMANS[1].name].windows
                      if w.attrs["data-window-id"] == "L2-C3-F04")
        ids = rune_ids(Document(self.sources[ROMANS[1].name][window.start:window.end]))
        self.assertEqual(len(ids), 32)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(identifier.startswith("L2-HAS-") for identifier in ids))
        book_i_ids = set(rune_ids(self.documents[ROMANS[0].name]))
        self.assertTrue(book_i_ids.isdisjoint(ids))
        manuscript_records = chapter_3_equipment(self.sources[ROMANS[1].name])
        lore_records = lore_chapter_3_equipment(self.lore)
        self.assertEqual(list(manuscript_records), ids)
        self.assertEqual(manuscript_records, lore_records)
        for record in manuscript_records.values():
            self.assertEqual(record["amélioration"], "+15")
            self.assertEqual(len(record["secondaires"]), 4)
        start = self.lore.index("### Livre II, vie 2 — équipement de 32 runes")
        end = self.lore.index("## Livre II, chapitre 2 validé", start)
        section = self.lore[start:end]
        for phrase in ("Hasol Shun, équipée au chapitre 3 de la vie 2",
                        "8 Vol de vie / 8 Arcanique / 8 Vitesse / 2 Énergie / 2 Gardien / 4 Fatal",
                        "exemplaires matériels distincts"):
            self.assertIn(phrase, section)

    def test_mutations_des_fiches_vie_2_divergentes_du_lore_sont_refusees(self):
        window = next(w for w in self.documents[ROMANS[1].name].windows
                      if w.attrs["data-window-id"] == "L2-C3-F04")
        source = self.sources[ROMANS[1].name][window.start:window.end]
        expected = lore_chapter_3_equipment(self.lore)
        mutations = {
            "ensemble": ("Fatal rare (bleue), 6★", "Gardien rare (bleue), 6★"),
            "rareté/couleur": ("Fatal rare (bleue), 6★", "Fatal épique (violette), 6★"),
            "étoiles": ("Fatal rare (bleue), 6★", "Fatal rare (bleue), 5★"),
            "amélioration": ("6★, <span class=\"upgrade-badge\">+15</span></td>",
                              "6★, <span class=\"upgrade-badge\">+14</span></td>"),
            "principale": ("Attaque +160", "Attaque +161"),
            "secondaire": ("Vitesse +8 ; PV +25", "Vitesse +9 ; PV +25"),
        }
        for field, (before, after) in mutations.items():
            with self.subTest(champ=field):
                self.assertIn(before, source)
                changed = source.replace(before, after, 1)
                with self.assertRaises(AssertionError):
                    self.assertEqual(chapter_3_equipment(changed), expected)


class InsecabiliteTests(unittest.TestCase):
    def test_pourcentages_et_milliers_sont_insecables_dans_les_fenetres(self):
        for path in ROMANS:
            source = path.read_text(encoding="utf-8")
            for window in Document(source).windows:
                raw = source[window.start:window.end]
                with self.subTest(manuscrit=path.name, fenetre=window.attrs["data-window-id"]):
                    assert_unbreakable_values(self, raw)

    def test_mutations_espace_percent_et_millier_sont_refusees(self):
        valid = "<div><p>Attaque +63&nbsp;%</p><p>Mana 1&nbsp;200</p></div>"
        assert_unbreakable_values(self, valid)
        for changed in (valid.replace("63&nbsp;%", "63 %"),
                        valid.replace("1&nbsp;200", "1 200")):
            with self.subTest(source=changed), self.assertRaises(AssertionError):
                assert_unbreakable_values(self, changed)


if __name__ == "__main__":
    unittest.main()
