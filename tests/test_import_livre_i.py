"""Contrats de l'import final, sans régénération des sources ni des dérivés."""

from html import unescape
from pathlib import Path
import re
import unittest

from lecture_support import Document, compact, digest, manifest, historical_prefix


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = re.compile(r"^# Chapitre (\d+) — ([^\n]+)$", re.M)
CH13_BEFORE_XI = "2e1a64b9a19963e8eab5224a71edc27bd68af20c4e29907bd9a63437102f64dd"
BEFORE_IMPORT = {
    1: "b50dfb5a73edf17ca17d927cbd3c15295ba827c38df1b39377305db58c7f7e0d",
    2: "2e3897390deec79b664a6618ab42c44679c874afc4da2f795667eb5df93f7369",
    3: "bda84770ddd08d573162b8d6cb2244ea804267d2943a54c78a3a8c35de055ec0",
    4: "7331a08713fe51fac8ac1d1a6d501a97e90e368bd3e5a3ebb7c69c2905af0226",
    5: "17e3c57795e3d71ea99d462fab9e959ed096bf6c1cbea094b6485eeab4f11933",
    6: "360f32a49c9fd59834304456639c8ad5555458c97cc0ca704cd3814102bb4cd1",
    7: "df39f4bf23335a96940a5de0f82f4cbb16405fbe457833cf56979f2e91ca9f0e",
    8: "d3ca7d396f5d7f7d7fb1fed311f026aebfefe6d47a85e75d2a9d3ce69ed487ed",
    9: "db4cf7485df44bf613315d54005502c8331b4db65795d9a59bb40464b7874c09",
    10: "f1afcef0a4a2c9c056d7e7e11fa34f8663d422a77b9492b1e548f23b31e76162",
    11: "900a2058b5cc814e80dd31c04bc6d681a91d575670ec05be3febd1b4255f6cc0",
    12: "1a80238397895e5251bfab12397272dd045a72410a6630bf9d1dadec3ffab9f0",
}


def chapters(source):
    matches = list(CHAPTER.finditer(source))
    epilogue = re.search(r"^# Épilogue\b[^\n]*", source, re.M)
    return {int(match[1]): source[match.end():
            matches[index + 1].start() if index + 1 < len(matches)
            else epilogue.start() if epilogue else len(source)]
            for index, match in enumerate(matches)}


def readable(source):
    source = re.sub(r"<[^>]*>", " ", source)
    text = compact(unescape(source).replace("’", "'").replace("**", "").replace("*", ""))
    return text.replace("Pendant plusieurs minutes, ils réussirent à faire reculer le boss.",
                        "Pendant quelques secondes, ils réussirent à faire reculer le boss.").replace(
        "Il passa une main dans ses longs cheveux noirs, démêlant doucement une mèche coincée entre eux.",
        "Il passa une main dans les longs cheveux brun sombre d'Hasol, démêlant doucement une mèche coincée entre eux.").replace(
        "Son visage, habituellement si fermé depuis la disparition de sa famille, semblait soudain hésiter entre plusieurs émotions.",
        "Son visage, habituellement si fermé depuis la disparition d'une partie de sa famille, semblait soudain hésiter entre plusieurs émotions.").replace(
        "— Toi, tu attends vingt-quatre niveaux pour obtenir ton premier sort offensif et il te permet de voler celui des autres !",
        "— Toi, tu attends le niveau quarante pour obtenir ton premier sort offensif et il te permet de voler celui des autres !")


def source_chapter(archive, number, title):
    heading = re.compile(rf"^(?:#\s*)?(?:\*\*)?Chapitre {number} — {re.escape(title)}(?:\*\*)?\s*$", re.M)
    candidates = list(heading.finditer(archive))
    if not candidates:
        raise AssertionError(f"Source du chapitre {number} absente")
    # La dernière version complète, et non une proposition ou un commentaire.
    start = candidates[-1].end()
    end = re.search(rf"^(?:\*\*)?Fin du chapitre {number}\b[^\n]*$", archive[start:], re.M)
    if end is None:
        raise AssertionError(f"Fin de la source du chapitre {number} absente")
    return archive[start:start + end.start()]


def narrative_paragraphs(source):
    """Ancres longues : ne confondre ni petits libellés système ni narration."""
    for paragraph in re.split(r"\n\s*\n", source):
        text = readable(paragraph)
        if (len(text) >= 60 and not re.search(r"[\d|]", text)
                and not text.startswith(("#", "SYSTÈME", "Déploie ", "Le sort "))):
            yield text.replace("ma belle", "ma princesse").replace("Ma belle", "Ma princesse")


def assert_narrative_conserved(case, original, imported):
    destination = readable(Document(imported).root.text())
    cursor = 0
    anchors = list(narrative_paragraphs(original))
    case.assertGreater(len(anchors), 10, "Source narrative trop courte ou mauvaise version")
    for anchor in anchors:
        found = destination.find(anchor, cursor)
        case.assertNotEqual(found, -1, f"Paragraphe source absent, modifié ou déplacé : {anchor[:180]}")
        cursor = found + len(anchor)


class ImportLivreITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (ROOT / "livre_1_l_ascension_d_une_legende_oubliee.md").read_bytes().decode("utf-8")
        cls.parts = chapters(cls.source)
        cls.archive = (ROOT / "docs/new.txt").read_text(encoding="utf-8")

    def test_corps_des_chapitres_1_a_12_identiques_a_l_avant_import(self):
        for number, expected in BEFORE_IMPORT.items():
            with self.subTest(chapitre=number):
                self.assertIn(number, self.parts)
                self.assertEqual(digest(self.parts[number]), expected)

    def test_section_xi_13_conserve_la_source_narrative(self):
        start = self.archive.index("XI. La nuit où tout a changé")
        end = self.archive.index("Fin du chapitre 13", start)
        section = self.parts[13].split("## XI. La nuit où tout a changé", 1)
        self.assertEqual(len(section), 2)
        assert_narrative_conserved(self, self.archive[start:end], section[1])

    def test_seize_chapitres_uniques_suivis_d_un_epilogue_non_numerote(self):
        self.assertEqual([int(match[1]) for match in CHAPTER.finditer(self.source)], list(range(1, 17)))
        epilogues = list(re.finditer(r"^# Épilogue\b[^\n]*", self.source, re.M))
        self.assertEqual(len(epilogues), 1)
        self.assertGreater(epilogues[0].start(), list(CHAPTER.finditer(self.source))[-1].end())
        self.assertNotRegex(self.source, r"(?im)^#+\s*(?:\*\*)?Chapitre\s+17\b")

    def test_chapitre_13_sections_i_a_x_preservees_octet_pour_octet(self):
        start = re.search(r"^# Chapitre 13 —[^\n]*", self.source, re.M)
        self.assertIsNotNone(start)
        xi = re.search(r"^## XI\. La nuit où tout a changé\s*$", self.source[start.start():], re.M)
        self.assertIsNotNone(xi, "La nouvelle section XI doit suivre les dix sections validées")
        before = self.source[start.start():start.start() + xi.start()]
        before = re.sub(r"\s*---\s*$", "", before)
        before = re.sub(r"\n---\n\n\*\*Fin du chapitre 13[^\n]*\*\*\s*$", "", before)
        self.assertEqual(digest(before.rstrip()), CH13_BEFORE_XI)

    def test_dernieres_sources_14_15_16_conservent_les_paragraphes_narratifs_dans_l_ordre(self):
        for number, title in ((14, "Le centième boss"), (15, "Enfin, la magie"), (16, "Celle qui demeure")):
            with self.subTest(chapitre=number):
                self.assertIn(number, self.parts)
                original = source_chapter(self.archive, number, title) if number != 16 else self.archive[
                    self.archive.rindex('# **Chapitre 16 — Celle qui demeure**'):self.archive.index('## **FIN DU LIVRE I**', self.archive.rindex('# **Chapitre 16 — Celle qui demeure**'))]
                if number == 16:
                    original = original.split('## **Épilogue', 1)[0]
                assert_narrative_conserved(self, original, self.parts[number])

    def test_compteurs_distincts_et_progression_sans_doublon(self):
        for number in (13, 14, 15, 16):
            self.assertIn(number, self.parts)
        windows = {n: " ".join(compact(w.text()) for w in Document(self.parts[n]).windows)
                   for n in (13, 14, 15, 16)}
        self.assertRegex(windows[13], r"5\s*000")
        self.assertRegex(windows[13], r"(?i)aucune restriction de niveau")
        self.assertRegex(windows[14], r"100\s*/\s*100")
        self.assertRegex(windows[14], r"13\s*→\s*14")
        self.assertRegex(windows[15], r"14\s*→\s*15")
        self.assertRegex(windows[15], r"15\s*→\s*16")
        first = re.search(r"5\s*000", windows[15])
        second = re.search(r"10\s*000", windows[15])
        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        self.assertLess(first.start(), second.start())

    def test_equipement_13_puis_14_puis_16_et_ensembles(self):
        self.assertIn(14, self.parts)
        self.assertIn(15, self.parts)
        for number, required in ((14, ("Fatal", "Arcanique", "Vitesse", "Gardien")),
                                 (15, ("Fatal", "Arcanique", "Vitesse", "Gardien", "Énergie"))):
            windows = [compact(window.text()) for window in Document(self.parts[number]).windows]
            for ensemble in required:
                self.assertTrue(any(ensemble in text for text in windows), (number, ensemble))
        text = readable(self.parts[14])
        self.assertIn("treize", text)
        self.assertIn("quatorze", text)
        self.assertRegex(readable(self.parts[15]), r"16 runes équipées")

    def test_siphon_description_qualitative_sans_formule_chiffree(self):
        self.assertIn(15, self.parts)
        windows = Document(self.parts[15]).windows
        descriptions = [compact(w.text()) for w in windows
                        if "Siphon runique" in w.text() and "Vol de Mana" in w.text()]
        self.assertEqual(len(descriptions), 1)
        description = descriptions[0]
        for term in ("Vent", "Puissance arcanique", "Mana", "réserve maximale"):
            self.assertIn(term, description)
        self.assertNotRegex(description, r"\d+\s*(?:%|secondes?|Mana|mètres?)")

    def test_raccords_cibles_presents_sans_retablir_les_anciennes_ambiguities(self):
        dialogue = compact(self.parts[15])
        self.assertIn("— Toi, tu attends le niveau quarante pour obtenir ton premier sort offensif et il te permet de voler celui des autres !", dialogue)
        self.assertNotIn("tu attends vingt-quatre niveaux", dialogue)
        text = compact(self.parts[16]).replace("’", "'")
        self.assertIn("Pendant quelques secondes, ils réussirent à faire reculer le boss.", text)
        self.assertNotIn("Pendant plusieurs minutes, ils réussirent à faire reculer le boss.", text)
        self.assertIn("depuis la disparition d'une partie de sa famille", text)
        xi = compact(self.parts[13].split("## XI.", 1)[1]).replace("’", "'")
        self.assertIn("les longs cheveux brun sombre d'Hasol", xi)
        self.assertNotIn("ses longs cheveux noirs", xi)

    def test_epilogue_douze_gongs_une_cloche_et_surnom(self):
        self.assertIn(16, self.parts)
        chapter = self.parts[16]
        self.assertEqual(len(re.findall(r"\bDONG\b", chapter)), 12)
        self.assertEqual(len(re.findall(r"\bDING\b", chapter)), 1)
        epilogue = re.search(r"^# Épilogue\b[^\n]*", self.source, re.M)
        self.assertIsNotNone(epilogue)
        text = self.source[epilogue.end():]
        for term in ("Iseria", "Astrae", "Douze", "Un seul"):
            self.assertIn(term, text)
        self.assertIn("ma princesse", chapter.lower())
        self.assertIsNone(re.search(r"(?i)\bma belle\b(?!-sœur)", chapter),
                          "Le surnom de Zio doit être ma princesse, sans interdire belle-sœur")
        # « belle-sœur » reste légitime dans les relations familiales antérieures.


class ImportMutationTests(unittest.TestCase):
    def test_suppression_modification_et_inversion_des_paragraphes_detectees(self):
        first = "Hasol contemplait la capitale silencieuse, les maisons encore endormies et le jardin de son enfance. Elle retrouva le courage de regarder le monde sans détourner les yeux."
        second = "Zio lui tendit la main sans prononcer une parole. Elle reconnut ce geste familier et sentit sa peur refluer tandis que leurs compagnons attendaient au bas du grand escalier."
        paragraphs = [first, second] * 6
        original = "\n\n".join(paragraphs)
        assert_narrative_conserved(self, original, original)
        for changed in (original.replace(first, "", 1), original.replace("capitale", "forteresse", 1),
                        "\n\n".join([second, first, *paragraphs[2:]])):
            with self.subTest(mutation=changed[:40]):
                with self.assertRaises(AssertionError):
                    assert_narrative_conserved(self, original, changed)

    def test_liens_sommaire_ajoutes_seuls_exemptes_pas_texte_arbitraire(self):
        original = "## Sommaire\n1. [Chapitre 1 — Ancien](#chapitre-1)\n\n# Chapitre 1 — Ancien\n<div class=\"system-window\">Mana</div>\nFin.\n"
        reference = manifest(original)
        addition = "\n# Chapitre 2 — Nouveau\nSuite.\n"
        source = original.replace("\n\n# Chapitre 1", "\n2. [Chapitre 2 — Nouveau](#chapitre-2)\n\n# Chapitre 1") + addition
        self.assertEqual(historical_prefix(source, reference), original)
        corrupted = source.replace("Ancien](", "Altéré](", 1)
        self.assertNotEqual(digest(historical_prefix(corrupted, reference)), digest(original))


if __name__ == "__main__":
    unittest.main()
