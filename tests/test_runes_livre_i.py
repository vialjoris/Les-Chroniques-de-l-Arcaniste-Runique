"""Contrats DEC-178/179/180 : données du lore et conservation, sans générateur."""

from collections import Counter
import json
from pathlib import Path
import re
import unittest

from lecture_support import Document, before_approved_rune_corrections, compact, digest


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).parent / "fixtures"
SOURCE = ROOT / "livre_1_l_ascension_d_une_legende_oubliee.md"
ADDED = {
    "C3-R01", "C4-R01", "C6-R01", "C6-R02", "C6-R03",
    "C7-R01", "C7-R02", "C7-R03", "C9-R01", "C10-R01",
    "C12-R01", "C12-R02", "C14-R01", "C15-R01", "C15-R02",
}
IDENTITY = re.compile(
    r"(?P<ensemble>Fatal|Gardien|Énergie|Arcanique|Vitesse) "
    r"(?P<grade>peu commune \(verte\)|commune \(blanche\)|rare \(bleue\)|"
    r"épique \(violette\)|légendaire \(orange\)), (?P<stars>[1-6])★")
ID = re.compile(r"\b(?:HAS|ORV|CLI|MAR|REC|GRI|YOO|ISE)-R\d{3}\b")


def states_from_lore(lore):
    """Lire les tables canoniques ; les journaux de correction ne fournissent aucun attendu."""
    states = {}
    for line in lore.splitlines():
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 5 or not ID.fullmatch(cells[0]):
            continue
        identifier, identity, level, main, subs = cells
        match = IDENTITY.fullmatch(identity)
        if match is None:
            # La table finale donne la qualité commune à toutes ses lignes dans son introduction.
            if identity not in {"Fatal", "Gardien", "Énergie", "Arcanique", "Vitesse"}:
                continue
            identity += " rare (bleue), 6★"
            level, main, subs = "+15", cells[2], cells[3]
        level = int(re.match(r"\+(\d+)\b", level)[1])
        key = (identifier, level)
        value = (identity, main, subs)
        if key in states and states[key] != value:
            raise ValueError(f"Deux fiches canoniques incompatibles : {key}")
        states[key] = value
    # Les cadeaux ont des fiches à puces, pas de table d'affixes à +6.
    states["HAS-R001", 6] = ("Fatal rare (bleue), 6★", "Attaque +70", "Vitesse +4 ; PV +25")
    states["HAS-R002", 6] = ("Gardien rare (bleue), 6★", "Défense +70", "PV +30 ; Mana +20")
    states["HAS-R003", 0] = ("Fatal rare (bleue), 3★", "Attaque +7", "Vitesse +2 ; PV +30")
    return states


def validate_affixes(identity, level, main, subs):
    match = IDENTITY.fullmatch(identity)
    if match is None or not 0 <= level <= 15:
        raise ValueError("Identité incomplète")
    grade = match["grade"]
    count = {"commune (blanche)": 0, "peu commune (verte)": 1,
             "rare (bleue)": 2, "épique (violette)": 3, "légendaire (orange)": 4}[grade]
    for milestone, threshold in ((3, 0), (6, 1), (9, 2), (12, 3)):
        if level >= milestone and count == threshold:
            count += 1
    values = [] if subs == "Aucune" else subs.split(" ; ")
    if len(values) != count:
        raise ValueError(f"Secondaires incompatibles : {identity} +{level}, {subs}")
    for value in (main, *values):
        if not re.fullmatch(r"(?:PV|Attaque|Défense|Vitesse|Mana|PA|Précision|Résistance) \+\d[\d ]*(?: %)?", value):
            raise ValueError(f"Affixe invalide : {value}")
        if value.startswith("PA ") and "%" in value:
            raise ValueError("PA % non admise")
    for value in values:
        if value.startswith(("PV ", "Défense ")) and "%" in value:
            raise ValueError("Secondaire en pourcentage non validée")


def inventory_rows(window):
    return [row for table in window.descendants("table") if "lit-window__inventory" in table.classes
            for row in table.descendants("tr") if any(cell.tag == "td" for cell in row.children)]


def assert_inventory(case, window, states):
    seen = set()
    for index, row in enumerate(inventory_rows(window)):
        cells = [compact(cell.text()) for cell in row.children if cell.tag in {"th", "td"}]
        case.assertEqual(len(cells), 3)
        if window.attrs["data-window-id"] == "019":
            key = (f"HAS-R{index + 3:03d}", 0)
            identity, main, subs = states[key]
            case.assertEqual(tuple(cells), (identity + ", +0", main, subs))
            validate_affixes(identity, 0, main, subs)
            continue
        identifier = ID.search(cells[0])
        if identifier:
            identifier = identifier[0]
            identity = IDENTITY.search(cells[0])
        else:
            heading = next(window.descendants("h3"))
            identifier = ID.search(heading.text())[0]
            identity = IDENTITY.search(compact(heading.text()))
        case.assertIsNotNone(identity, cells[0])
        level = re.search(r"\+(\d+)\b", cells[0])
        case.assertIsNotNone(level, cells[0])
        key = (identifier, int(level[1]))
        case.assertNotIn(key, seen)
        seen.add(key)
        case.assertIn(key, states)
        actual = (identity[0], cells[1], cells[2])
        case.assertEqual(actual, states[key], key)
        validate_affixes(actual[0], key[1], *actual[1:])


class RunesLivreITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_bytes().decode("utf-8")
        cls.document = Document(cls.source)
        cls.windows = {window.attrs["data-window-id"]: window for window in cls.document.windows}
        cls.before = before_approved_rune_corrections(cls.source)
        cls.lore = (ROOT / "lore/runes.md").read_text(encoding="utf-8")
        cls.characters = (ROOT / "lore/personnages.md").read_text(encoding="utf-8")
        cls.states = states_from_lore(cls.lore)

    def test_deux_journaux_figes_restaurent_les_138_fenetres_sans_changer_les_fixtures_historiques(self):
        expected = (
            ("corrections_runes_livre1_dec179.json", 126,
             "9d27a766bef9706867ebbf658ba4dd2ecfb46b885cbf6a4e5d850ad3ae0caa2b",
             "1e4221ee2755748a072534630d816a22c6b84f260e3bb500347b2d8c3d304912"),
            ("corrections_runes_livre1_dec179_complements.json", 11,
             "1e4221ee2755748a072534630d816a22c6b84f260e3bb500347b2d8c3d304912",
             "a26785c286e66efe96466aa355d08aba4a002a670c32d52491e261d47d257575"),
        )
        rebuilt = self.before
        for name, count, before, after in expected:
            stage = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
            self.assertEqual(len(stage["pairs"]), count)
            self.assertEqual((stage["baseline_sha256"], stage["result_sha256"]), (before, after))
            self.assertEqual(digest(rebuilt), before)
            last = len(rebuilt)
            for pair in reversed(stage["pairs"]):
                start, end = pair["before_start_char"], pair["before_end_char"]
                self.assertLessEqual(end, last)
                self.assertEqual(rebuilt[start:end], pair["before"])
                rebuilt = rebuilt[:start] + pair["after"] + rebuilt[end:]
                last = start
            self.assertEqual(digest(rebuilt), after)
        for name, checksum in (
            ("corrections_runes_livre1_dec179.json", "1e20c5b5454385ad414d40297b1b2a60b4db68e78dc4291299d24f1c81ad8796"),
            ("corrections_runes_livre1_dec179_complements.json", "cbcc5eb418d3fd65af4d59624d653394d03149cff14018226baa34e5a024cb51"),
        ):
            self.assertEqual(digest((FIXTURES / name).read_bytes().decode("utf-8")), checksum)
        self.assertEqual(rebuilt, self.source)
        self.assertEqual(len(Document(self.before).windows), 138)
        self.assertEqual(len(self.document.windows), 153)
        self.assertEqual(set(self.windows) - {w.attrs["data-window-id"] for w in Document(self.before).windows}, ADDED)
        self.assertEqual(len(list((ROOT / "assets/fenetres").glob("*.svg"))), 306)

    def test_toutes_les_lignes_d_inventaire_correspondent_aux_etats_canoniques(self):
        self.assertEqual(len(inventory_rows(self.windows["019"])), 8)
        checked = 0
        for identifier, window in self.windows.items():
            if inventory_rows(window):
                with self.subTest(fenetre=identifier):
                    assert_inventory(self, window, self.states)
                checked += len(inventory_rows(window))
        self.assertGreater(checked, 100)

    def test_paliers_et_affixes_du_referentiel_sont_valides_sans_recoloration(self):
        self.assertGreater(len(self.states), 60)
        identities = {}
        for (identifier, level), (identity, main, subs) in self.states.items():
            with self.subTest(rune=identifier, palier=level):
                validate_affixes(identity, level, main, subs)
                self.assertEqual(identities.setdefault(identifier, identity), identity)
        for identity, level, main, subs in (
            ("Énergie commune (blanche), 1★", 3, "PV +85", "Aucune"),
            ("Fatal rare (bleue), 6★", 6, "Attaque +70", "Vitesse +4"),
            ("Fatal rare (bleue), 6★", 15, "Attaque +160", "PV +25 ; Mana +20 ; CC +3 ; DCC +4"),
            ("Fatal rare (bleue), 6★", 6, "PA +30 %", "PV +20 ; Mana +10"),
            ("Fatal rare (bleue), 6★", 6, "Attaque +70", "PV +20 % ; Défense +3 %"),
        ):
            with self.subTest(invalide=(identity, level, main, subs)):
                with self.assertRaises(ValueError):
                    validate_affixes(identity, level, main, subs)

    def test_fiches_individuelles_et_etats_avant_apres_conformes_au_lore(self):
        mapping = {
            "003": [("HAS-R001", 6)], "005": [("HAS-R002", 6)],
            "020": [("HAS-R003", 0)],
            "090": [("ORV-R001", 0)], "033": [("ORV-R001", 1)], "034": [("ORV-R001", 3)],
            "091": [("CLI-R001", 0)], "035": [("CLI-R001", 0)],
            "036": [("CLI-R001", 1)], "037": [("CLI-R001", 2)],
            "C3-R01": [("MAR-R001", 0)], "C4-R01": [("CLI-R002", 0)],
            "C6-R01": [("REC-R001", 0)], "C6-R02": [("REC-R002", 0)],
            "C6-R03": [("REC-R003", 0)], "057": [("GRI-R001", 6)],
            "058": [("HAS-R011", 0), ("HAS-R012", 0)],
            "068": [("HAS-R009", 7)], "069": [("HAS-R009", 7)], "070": [("HAS-R009", 9)],
            "C9-R01": [("HAS-R010", 9)], "076": [("HAS-R013", 6), ("HAS-R014", 6)],
            "079": [("HAS-R009", 9), ("HAS-R010", 9), ("YOO-R001", 6), ("YOO-R002", 6)],
            "C10-R01": [("ORV-R002", 0)], "098": [("ORV-R002", 3)],
            "C14-R01": [("HAS-R027", 15)], "C15-R01": [("HAS-R028", 15)],
            "C15-R02": [("HAS-R029", 15)],
        }
        for window_id, keys in mapping.items():
            window = self.windows[window_id]
            # Séparer les paragraphes multi-runes évite de valider un affixe d'une voisine.
            paragraphs = [compact(node.text()) for node in window.descendants("p")]
            for key in keys:
                with self.subTest(fenetre=window_id, rune=key):
                    identity, main, subs = self.states[key]
                    text = compact(window.text())
                    self.assertIn(identity, text.replace(" — ", ", "))
                    self.assertIn(f"+{key[1]}", text)
                    self.assertIn(key[0], text)
                    candidates = [text] if len(keys) == 1 else [p for p in paragraphs if key[0] in p]
                    self.assertEqual(len(candidates), 1)
                    self.assertIn(main, candidates[0])
                    for affix in ([] if subs == "Aucune" else subs.split(" ; ")):
                        self.assertIn(affix, candidates[0])
                    if subs == "Aucune":
                        self.assertIn("Aucune", candidates[0])
                    validate_affixes(identity, key[1], main, subs)

    def test_nombre_de_secondaires_aux_paliers_inclut_le_plus_15_sans_cinquieme(self):
        samples = (
            ("commune (blanche)", ((0, 0), (1, 0), (2, 0), (3, 1), (6, 2), (9, 3), (15, 4))),
            ("peu commune (verte)", ((0, 1), (3, 1), (6, 2), (9, 3), (15, 4))),
            ("rare (bleue)", ((0, 2), (6, 2), (9, 3), (12, 4), (15, 4))),
            ("légendaire (orange)", ((0, 4), (9, 4), (15, 4))),
        )
        affixes = ["Vitesse +2", "Mana +10", "Attaque +3", "Défense +3", "PA +20"]
        for grade, milestones in samples:
            for level, count in milestones:
                with self.subTest(grade=grade, palier=level):
                    identity = f"Énergie {grade}, 2★"
                    subs = " ; ".join(affixes[:count]) if count else "Aucune"
                    validate_affixes(identity, level, "PV +70", subs)
                    too_many = " ; ".join(affixes[:count + 1])
                    with self.assertRaises(ValueError):
                        validate_affixes(identity, level, "PV +70", too_many)

    def test_fiches_historiques_et_transitions_conservent_les_affixes_connus(self):
        for identifier, key in (("002", ("HAS-R001", 6)), ("004", ("HAS-R002", 6))):
            identity, main, subs = self.states[key]
            text = compact(self.windows[identifier].text()).replace(" — ", ", ")
            self.assertIn(identity, text)
            self.assertIn("+6", text)
            self.assertIn(main, text)
            for affix in subs.split(" ; "):
                self.assertIn(affix, text)
        for identifier in ("006", "009", "016"):
            items = [compact(n.text()) for n in self.windows[identifier].descendants("p")]
            for ensemble, main, subs in (
                ("Fatal", "Attaque +70", "Vitesse +4, PV +25"),
                ("Gardien", "Défense +70", "PV +30, Mana +20"),
            ):
                matching = [item for item in items if item.startswith("Rune " + ensemble)]
                self.assertEqual(len(matching), 1)
                self.assertIn("bleue 6★ +6", matching[0])
                self.assertIn(main, matching[0])
                self.assertIn(subs, matching[0])
        success = compact(self.windows["021"].text())
        for term in ("Fatal rare (bleue), 3★ +3", "Attaque +7 → +22", "Vitesse +2 → +4", "PV +30"):
            self.assertIn(term, success)
        for identifier in ("034", "098"):
            badges = [n for n in self.windows[identifier].descendants()
                      if any(c.startswith("lit-badge--rune-") for c in n.classes)]
            self.assertTrue(badges)
            self.assertTrue(all("lit-badge--rune-common" in badge.classes for badge in badges))
        self.assertIn("PV +436", compact(self.windows["068"].text()))
        self.assertIn("PV +436", compact(self.windows["069"].text()))
        self.assertIn("AMÉLIORATION ÉCHOUÉE", compact(self.windows["069"].text()))
        self.assertIn("3★, +7 conservé", compact(self.windows["069"].text()))
        self.assertIn("PV +532", compact(self.windows["070"].text()))

    def test_occupations_identites_ensembles_et_transferts_sans_transformation_d_etoiles(self):
        expected = {
            "022": list(range(1, 11)), "059": [1, 2, 3, 4, 5, 6, 9, 10, 11, 12],
            "060": [1, 2, 3, 4, 5, 6, 9, 10, 11, 12],
            "062": [1, 2, 3, 4, 5, 6, 9, 10, 11, 12],
            "078": [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14],
            "087": [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14],
            "C14-F01": [1, *range(16, 27), 2],
            "C14-F09": [1, *range(16, 27), 2, 27],
            "C15-F10": [1, *range(16, 27), 2, 27, 28, 29],
        }
        for window_id, numbers in expected.items():
            with self.subTest(fenetre=window_id):
                rows = inventory_rows(self.windows[window_id])
                self.assertEqual([ID.search(row.text())[0] for row in rows],
                                 [f"HAS-R{n:03d}" for n in numbers])
                sets = Counter(IDENTITY.search(row.text())["ensemble"] for row in rows)
                self.assertEqual(sets["Fatal"], 4)
                self.assertIn(sets["Gardien"], {1, 2, 3, 4})
                self.assertIn(sets["Arcanique"], {0, 2, 4})
                if window_id.startswith("C"):
                    for row in rows:
                        self.assertIn("rare (bleue), 6★, +15", row.text())
                    self.assertEqual(sets["Vitesse"], 4)
        self.assertEqual(Counter(re.search(r", \+(\d+)\b", row.children[0].text())[1]
                                 for row in inventory_rows(self.windows["060"])), {"6": 6, "3": 4})
        yoon = compact(self.windows["079"].text())
        self.assertLess(yoon.index("HAS-R009"), yoon.index("Anciennes runes conservées"))
        self.assertGreater(yoon.index("YOO-R001"), yoon.index("non équipées"))
        for reference in (self.lore, self.characters):
            for term in ("HAS-R009/010", "YOO-R001/002", "11/11", "12/12", "14/14", "15/15", "16/16"):
                self.assertIn(term, reference)
            self.assertIn("ellipses", reference)
            self.assertIn("ne pas figer", reference.lower())
        self.assertIn("Propriétaire Hasol jusqu’au chapitre 9, puis **Yoon Notos**", self.lore)
        self.assertIn("HAS-R001/002 et HAS-R016 à 026", self.characters)
        self.assertIn("HAS-R003 à 015 ne deviennent pas 6★", self.characters)

    def test_statistiques_naturelles_et_classes_conservees_independamment_de_l_inverse(self):
        before_windows = {w.attrs["data-window-id"]: w for w in Document(self.before).windows}
        checked = 0
        for identifier, before in before_windows.items():
            old = [table for table in before.descendants("table") if "lit-window__stats" in table.classes]
            new = [table for table in self.windows[identifier].descendants("table") if "lit-window__stats" in table.classes]
            cells = lambda tables: [[[(cell.tag, compact(cell.text())) for cell in row.children
                                       if cell.tag in {"th", "td"}]
                                      for row in table.descendants("tr")] for table in tables]
            self.assertEqual(cells(old), cells(new), identifier)
            checked += len(old)
            old_class = [compact(n.text()) for n in before.descendants()
                         if n.classes & {"lit-badge--legendary", "lit-badge--rare", "lit-badge--common"}]
            new_class = [compact(n.text()) for n in self.windows[identifier].descendants()
                         if n.classes & {"lit-badge--legendary", "lit-badge--rare", "lit-badge--common"}]
            self.assertEqual(old_class, new_class, identifier)
        self.assertGreater(checked, 0)
        self.assertIn("Rareté légendaire", compact(self.windows["C14-F01"].text()))

    def test_projections_et_rune_temporelle_ne_deviennent_pas_des_etats_acquis(self):
        for identifier in ("C12-R01", "C12-R02"):
            text = compact(self.windows[identifier].text())
            self.assertIn("Projection conditionnelle +15 — NON ACQUISE", text)
            self.assertIn("réussite des tentatives non garantie", text)
        merchant = compact(self.windows["C12-R01"].text())
        self.assertIn("ordre des renforcements de Défense et de Mana indéterminé", merchant)
        self.assertIn("État réel conservé à +9 ; aucune tentative engagée", merchant)
        iseria = compact(self.windows["097"].text())
        for term in ("Légendaire — Orange", "★★★★", "+9", "PV +25 %", "+60", "+4", "+30", "+20"):
            self.assertIn(term, iseria)
        projection = compact(self.windows["099"].text())
        for term in ("État actuel : +9", "État final analysé : +15", "PV +43 %", "+140",
                     "Améliorations restantes effectuées personnellement par Hasol", "Non garantie"):
            self.assertIn(term, projection)
        for identifier in ("C16-F05", "C16-F06"):
            window = self.windows[identifier]
            text = compact(window.text()).lower()
            self.assertFalse(inventory_rows(window))
            self.assertNotRegex(text, r"[1-6]★|principale :|secondaires :")
        self.assertIn("identification partielle", self.characters)


class RunesLivreIMutationsTests(unittest.TestCase):
    def test_inverse_refuse_valeur_ordre_suppression_doublon_deplacement_et_prefixe(self):
        source = SOURCE.read_bytes().decode("utf-8")
        document = Document(source)
        windows = {w.attrs["data-window-id"]: w for w in document.windows}
        first, second = windows["C6-R02"], windows["C6-R01"]
        card = source[first.start:first.end]
        other = source[second.start:second.end]
        mutations = {
            "valeur": source.replace(card, card.replace("PV +40", "PV +41"), 1),
            "ordre": source.replace(card, "REMPLACEMENT", 1).replace(other, card, 1).replace("REMPLACEMENT", other, 1),
            "suppression": source[:first.start] + source[first.end:],
            "doublon": source[:first.end] + card + source[first.end:],
            "insertion préfixe": "Hasol était invincible.\n" + source,
            "narration hors journal": source.replace("Hasol", "Hésol", 1),
        }
        for label, changed in mutations.items():
            with self.subTest(mutation=label):
                self.assertNotEqual(changed, source)
                with self.assertRaises(ValueError):
                    before_approved_rune_corrections(changed)

    def test_contrat_d_inventaire_detecte_les_mutations_sans_utiliser_le_journal(self):
        source = SOURCE.read_bytes().decode("utf-8")
        states = states_from_lore((ROOT / "lore/runes.md").read_text(encoding="utf-8"))
        window = next(w for w in Document(source).windows if w.attrs["data-window-id"] == "C15-F10")
        card = source[window.start:window.end]
        assert_inventory(self, window, states)
        for old, new in (("PV +300", "PV +301"), ("6★, +15", "3★, +15"),
                         ("rare (bleue)", "légendaire (orange)"),
                         ("PV +300 ; Vitesse +8", "Vitesse +8 ; PV +300"),
                         ("PA +60 ; Résistance +6 %", "PA +60"),
                         ("HAS-R029", "HAS-R009")):
            with self.subTest(mutation=(old, new)):
                changed = card.replace(old, new)
                self.assertNotEqual(changed, card)
                with self.assertRaises((AssertionError, ValueError)):
                    assert_inventory(self, Document(changed).windows[0], states)


if __name__ == "__main__":
    unittest.main()
