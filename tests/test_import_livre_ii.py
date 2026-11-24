"""Contrats de l'import du chapitre 1 du II, sans modifier ses sources."""

from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

from lecture_support import Document, compact
from test_fenetres_github import load_generator
from test_securite_documents import assert_passive


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "livre_2_le_vertige_des_vies_oubliees.md"
ASSETS = "assets/fenetres-livre-2/"


class ImportLivreIITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_bytes().decode("utf-8")
        cls.document = Document(cls.source)

    def test_un_seul_chapitre_1_et_neuf_sections_sans_chapitre_2(self):
        chapters = re.findall(r"^## Chapitre\s+(\d+)\b[^\n]*", self.source, re.M)
        self.assertEqual(chapters, ["1"])
        self.assertEqual(
            re.findall(r"^###\s+([IVX]+)[. —–:]", self.source, re.M),
            ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        )
        self.assertNotRegex(self.source, r"(?im)^#+\s*(?:\*\*)?Chapitre\s+2\b")
        self.assertEqual(len(re.findall(
            r"(?im)^#+\s*(?:\*\*)?Chapitre\s+1\b", self.source)), 1)

    def test_fenetre_de_revelation_conserve_toutes_les_donnees_en_html(self):
        windows = [window for window in self.document.windows
                   if window.attrs.get("data-window-id") == "L2-C1-F01"]
        self.assertEqual(len(windows), 1)
        transcripts = list(windows[0].descendants("details"))
        self.assertEqual(len(transcripts), 1)
        text = compact(transcripts[0].text())
        for pattern in (r"\bHasol Shun\b", r"\bArcaniste Astral\b",
                        r"(?i)(?:rang|rareté)\s*:\s*Astrale?\b",
                        r"(?i)niveau\s*:\s*1\b",
                        r"(?i)coût[^.!?]{0,65}\b25\b",
                        r"(?i)cercles[^.!?]{0,30}\b2\b"):
            with self.subTest(donnee=pattern):
                self.assertRegex(text, pattern)

    def test_sourire_force_d_iseria_et_question_de_hasol_conserves(self):
        text = compact(self.document.root.text()).lower()
        self.assertRegex(text, r"sourire[^.!?]{0,120}forcé|forc[ée][^.!?]{0,120}sourire")
        self.assertRegex(text, r"maman\s*[,?…—–-]?\s*tout va bien\s*\?")
        self.assertIn("iseria", text)

    def test_samia_est_plus_jeune_de_trois_ans_et_entre_a_seize_ans(self):
        section = re.search(r"^### VI\.[\s\S]*?(?=^### VII\.)", self.source, re.M)
        self.assertIsNotNone(section)
        text = compact(section.group()).lower()
        self.assertIn("samia", text)
        self.assertRegex(text, r"(?:trois|3) ans (?:de moins|plus jeune)|cadette de (?:trois|3) ans")
        self.assertRegex(text, r"académie[^.!?]{0,100}(?:seize|16) ans")

    def test_manuscrit_sans_contenu_actif_ni_ressource_distante(self):
        assert_passive(self, self.source)
        self.assertNotRegex(self.source, r"!\[[^\]]*\]\(\s*(?:https?:|//|data:)")

    def test_premiere_conversation_elric_concerne_les_raids_de_portails(self):
        section = re.search(r"^### V\.[\s\S]*?(?=^### VI\.)", self.source, re.M)
        self.assertIsNotNone(section)
        text = compact(section.group())
        self.assertNotIn("dragons", text.lower())
        passages = (
            "Vous avez déjà pris part à des raids de portails ?",
            "Plus d'une fois.",
            "Dangereux. Beaucoup plus que tu ne l'imagines.",
            "Vous pourriez m'y emmener un jour ?",
            "Nous ne nous connaissons que depuis cinq minutes et tu veux déjà participer à un raid ?",
        )
        position = 0
        for passage in passages:
            with self.subTest(passage=passage):
                found = text.find(passage, position)
                self.assertGreaterEqual(found, position)
                position = found + len(passage)

    def test_derives_svg_locaux_identiques_et_generation_idempotente(self):
        generator = load_generator()
        generated, images = generator.produire(self.source)
        generated = generated.replace("assets/fenetres/", ASSETS)
        self.assertEqual(generated, self.source)
        self.assertTrue(images, "La fenêtre doit produire ses SVG bureau et mobile")
        references = [node.attrs[key]
                      for node in self.document.root.descendants()
                      for key in ("src", "srcset") if key in node.attrs]
        expected = {ASSETS + name for name in images}
        self.assertEqual(set(references), expected)
        self.assertEqual(len(references), len(expected))
        self.assertIn("L2-C1-F01.svg", images)
        self.assertIn("L2-C1-F01-mobile.svg", images)
        for name, svg in images.items():
            with self.subTest(image=name):
                self.assertEqual((ROOT / ASSETS / name).read_bytes(), svg.encode("utf-8"))
                assert_passive(self, svg)
                tree = ET.fromstring(svg)
                self.assertEqual(tree.tag, "{http://www.w3.org/2000/svg}svg")
                for node in tree.iter():
                    self.assertNotIn(node.tag.rsplit("}", 1)[-1].lower(),
                                     {"foreignobject", "image", "script"})
        regenerated, repeated_images = generator.produire(generated)
        self.assertEqual(regenerated.replace("assets/fenetres/", ASSETS), generated)
        self.assertEqual(repeated_images, images)


if __name__ == "__main__":
    unittest.main()
