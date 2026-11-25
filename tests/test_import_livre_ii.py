"""Contrats des deux chapitres importés du II, sans modifier leurs sources."""

import hashlib
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
        cls.chapitre_1, cls.chapitre_2 = cls.source.split(
            "\n---\n\n## Chapitre 2", 1)
        cls.chapitre_2 = "## Chapitre 2" + cls.chapitre_2

    def test_deux_chapitres_neuf_et_douze_sections_sans_chapitre_3(self):
        chapters = re.findall(r"^## Chapitre\s+(\d+)\b[^\n]*", self.source, re.M)
        self.assertEqual(chapters, ["1", "2"])
        self.assertEqual(
            re.findall(r"^###\s+([IVX]+)[. —–:]", self.chapitre_1, re.M),
            ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        )
        self.assertEqual(
            re.findall(r"^###\s+([IVX]+)[. —–:]", self.chapitre_2, re.M),
            ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"],
        )
        self.assertNotRegex(self.source, r"(?im)^#+\s*(?:\*\*)?Chapitre\s+3\b")
        self.assertEqual(len(re.findall(
            r"(?im)^#+\s*(?:\*\*)?Chapitre\s+1\b", self.source)), 1)

    def test_chapitre_1_local_et_ses_retouches_a_relire_preserves_octet_par_octet(self):
        self.assertEqual(
            hashlib.sha256(self.chapitre_1.encode("utf-8")).hexdigest(),
            "eed12b51da5554ef3671b7a035104451c6d746c9738b3d1acac6087a9ab9ea8b",
        )

    def test_chapitre_2_conserve_integralement_la_derniere_transmission(self):
        lines = (ROOT / "docs/new.txt").read_text(encoding="utf-8").splitlines()
        original = "\n".join(lines[103068:108183])
        self.assertTrue(original.startswith("# **Chapitre 2 — Les prodiges de l'Académie**"))
        self.assertTrue(original.endswith("*Fin du chapitre 2 — Les prodiges de l'Académie*"))
        original = original.replace("Classe : Ranger.", "Classe : Ranger astral.")
        original = original.replace("Samia est une Ranger commune", "Samia est une Ranger astral commune")
        original = original.replace("Une Ranger commune venait", "Une Ranger astral commune venait")
        generated = load_generator().extraire_source_fenetres(self.chapitre_2)

        def texte_utile(source):
            # Seuls le balisage de présentation et les espaces de mise en page diffèrent.
            return compact(re.sub(r"[*#]", "", Document(source).root.text()))

        self.assertEqual(texte_utile(generated), texte_utile(original))

    def test_samia_ranger_astral_commun_sans_renommer_zephyr_ni_les_usages_generiques(self):
        text = compact(Document(load_generator().extraire_source_fenetres(self.chapitre_2)).root.text())
        self.assertIn("Samia Claire. Classe : Ranger astral. Rang : Commun. Cercles de mana : 2.", text)
        self.assertIn("— Samia Claire. Classe : Ranger astral.", text)
        self.assertIn("La fille du Ranger, Samia", text)
        self.assertIn("Le Ranger contempla la dague.", text)
        self.assertIn("La jeune Ranger", text)

    def test_vague_legendaire_et_benediction_gardent_leurs_chiffres_et_limites(self):
        text = compact(Document(load_generator().extraire_source_fenetres(self.chapitre_2)).root.text())
        for passage in (
            "Coût : 5 Mana.", "Portée : 10 mètres.", "Incantation : 5 secondes.",
            "Aucun temps de recharge.", "20 % de la Puissance arcanique de Yoon",
            "membre du groupe possédant le plus faible pourcentage de PV actuels",
            "5 % des PV maximaux de Yoon.", "— Le sort me soigne moi.",
            "quarante-cinq pour cent le risque relatif d'échec",
            "vingt-cinq pour cent la probabilité relative de ne pas obtenir le meilleur résultat possible",
            "elles ne garantissaient toujours pas la réussite des tentatives",
            "**soixante pour cent**", "**cinquante pour cent**",
        ):
            with self.subTest(passage=passage):
                self.assertIn(passage, text)

    def test_groupes_de_cinquante_points_et_retraite_a_vingt_quatre_et_cinquante_ans(self):
        for passage in (
            "**Total : cinquante points.**", "**50 points.**",
            "Samia est une Ranger astral commune, qui représente cinq points.",
            "Hasol avait vingt-quatre ans lorsque son mentor lui annonça qu'il prenait sa retraite.",
            "J'avais quarante-deux ans lorsque nous nous sommes rencontrés. Aujourd'hui, j'en ai cinquante.",
        ):
            with self.subTest(passage=passage):
                self.assertIn(passage, self.chapitre_2)

    def test_seuls_les_affichages_systeme_deviennent_fenetres(self):
        windows = Document(self.chapitre_2).windows
        self.assertEqual([w.attrs.get("data-window-id") for w in windows],
                         [f"L2-C2-F{i:02}" for i in range(1, 10)])
        text = [compact(list(w.descendants("details"))[0].text()) for w in windows]
        expected = (
            "Vitesse.", "Nouvelle compétence passive acquise. Lame runique.",
            "Croissance runique — Seuil atteint. Un cercle de mana supplémentaire a été obtenu.",
            "Niveau supérieur. Niveau 10 atteint.", "Infiltration runique.",
            "Infiltration runique activée. Durée : 30 secondes.",
            "Samia Claire. Classe : Ranger astral. Rang : Commun. Cercles de mana : 2.",
            "Coût : 5 Mana. Portée : 10 mètres. Incantation : 5 secondes.",
            "Croissance runique. Boss de donjon personnellement achevé : +1.",
        )
        for actual, fragment in zip(text, expected):
            self.assertIn(fragment, actual)
        self.assertIn("**Cartographie des portails.**", self.chapitre_2)
        self.assertIn("**Coup astral.**", self.chapitre_2)

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
        text = compact(Document(self.chapitre_1).root.text()).lower()
        self.assertRegex(text, r"sourire[^.!?]{0,120}forcé|forc[ée][^.!?]{0,120}sourire")
        self.assertRegex(text, r"maman\s*[,?…—–-]?\s*tout va bien\s*\?")
        self.assertIn("iseria", text)

    def test_samia_est_plus_jeune_de_trois_ans_et_entre_a_seize_ans(self):
        section = re.search(r"^### VI\.[\s\S]*?(?=^### VII\.)", self.chapitre_1, re.M)
        self.assertIsNotNone(section)
        text = compact(section.group()).lower()
        self.assertIn("samia", text)
        self.assertRegex(text, r"(?:trois|3) ans (?:de moins|plus jeune)|cadette de (?:trois|3) ans")
        self.assertRegex(text, r"académie[^.!?]{0,100}(?:seize|16) ans")

    def test_manuscrit_sans_contenu_actif_ni_ressource_distante(self):
        assert_passive(self, self.source)
        self.assertNotRegex(self.source, r"!\[[^\]]*\]\(\s*(?:https?:|//|data:)")

    def test_premiere_conversation_elric_concerne_les_raids_de_portails(self):
        section = re.search(r"^### V\.[\s\S]*?(?=^### VI\.)", self.chapitre_1, re.M)
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

    def test_trois_compteurs_de_croissance_distincts_expliques_aux_parents_et_elric(self):
        for numero, suivant in (("III", "IV"), ("VII", "VIII")):
            section = re.search(
                rf"^### {numero}\.[\s\S]*?(?=^### {suivant}\.)", self.chapitre_1, re.M)
            self.assertIsNotNone(section)
            text = compact(section.group()).lower()
            with self.subTest(section=numero):
                self.assertIn("mille", text)
                self.assertIn("cent boss", text)
                self.assertIn("cinq mille", text)
                self.assertIn("personnellement", text)
                self.assertIn("hors portails", text)
                self.assertIn("prérequis de niveau", text)
        self.assertIn(
            "Seul ce dernier imposait des prérequis de niveau aux créatures éliminées ; "
            "les boss de donjon et les démons de portails n'en avaient pas.", self.chapitre_1)
        self.assertIn(
            "Les démons des portails n'alimentaient pas le compteur des mille "
            "monstres ordinaires hors portails.", self.chapitre_1)

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
        self.assertEqual({p.name for p in (ROOT / ASSETS).glob("*.svg")}, set(images))
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
