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
FICHE_ORVEN = '''  <div class="system-header lit-window__header">RUNE AMÉLIORÉE</div>
  <h3>Rune Énergie</h3>
  <p>Grade actuel : <span class="lit-badge lit-badge--rune-uncommon">Peu commun (Vert)</span></p>
  <p>Grade natif : <span class="lit-badge lit-badge--rune-common">Commun (Blanc)</span></p>
  <p>Rang : 1★</p>
  <p>Amélioration : <span class="upgrade-badge">+3</span></p>
  <hr>
  <p>Caractéristique principale : <span class="rune-bonus">Résistance +4 %</span></p>
  <p>Caractéristique secondaire : <strong><span class="rune-bonus">Vitesse +1</span></strong></p>'''
DESCRIPTION_LAME = (
    "Renforce la compréhension des techniques d'escrime.",
    "Facilite leur assimilation et améliore la précision ainsi que les automatismes "
    "associés au maniement de la lame.",
)
CORRECTIONS_SEPT_RUNES = (
    (
        "Et progressivement, les suivants.\n\nUn jour,",
        "Et progressivement, les suivants.\n\n"
        "Avec sept cercles, elle portait déjà sept runes, choisies avec Orven et Ray : "
        "quatre Fatal, dont celle offerte par son père, deux Gardien, dont son autre cadeau, "
        "et une Énergie.\n\nUn jour,",
    ),
    (
        "Elle commença immédiatement à imaginer les ensembles qu'elle pourrait porter.",
        "Ce huitième emplacement lui permettrait de compléter son ensemble Énergie.",
    ),
    (
        "— Évidemment !\n\nÀ son retour à l'Académie,",
        "— Évidemment !\n\n— Ce soir, je vais devoir aller voir Orven.\n\n"
        "— Attends, ne sois pas trop pressée. L'Académie te réserve une surprise. Tu verras."
        "\n\nÀ son retour à l'Académie,",
    ),
    (
        "Puis son regard descendit vers les deux runes qu'elle portait déjà.",
        "Puis son regard descendit vers les deux runes de son père, parmi les sept qu'elle portait.",
    ),
    (
        "Ce soir-là, Hasol équipa ses huit nouvelles runes.",
        "Ce soir-là, Hasol retira aussi les cinq autres runes et les rangea à part, "
        "puis équipa ses huit nouvelles runes.",
    ),
)
CORRECTIONS_RESERVE_IMMEDIATE = (
    (
        "et une Énergie.\n\nUn jour,",
        "et une Énergie.\n\nAvec eux, elle avait aussi préparé une seconde Énergie, "
        "gardée en réserve pour équiper son prochain emplacement dès l'obtention "
        "d'un nouveau cercle.\n\nUn jour,",
    ),
    (
        "Hasol s'immobilisa.\n\nElle ouvrit son statut.",
        "Hasol s'immobilisa.\n\nElle sortit aussitôt la seconde Énergie préparée "
        "avec Orven et Ray et l'équipa dans le nouvel emplacement.\n\nElle ouvrit son statut.",
    ),
    ("Huit runes possibles.", "Huit runes équipées."),
    (
        "Ce huitième emplacement lui permettrait de compléter son ensemble Énergie.",
        "Quatre Fatal, deux Gardien et deux Énergie : ses huit emplacements étaient "
        "occupés, et la paire Énergie était désormais active. Ses ensembles s'équilibraient.",
    ),
    (
        "— Ce soir, je vais devoir aller voir Orven.",
        "— Ce soir, je vais devoir aller voir Orven pour améliorer mes runes "
        "et préparer les prochains ensembles.",
    ),
    (
        "Puis son regard descendit vers les deux runes de son père, parmi les sept qu'elle portait.",
        "Puis son regard descendit vers les deux runes de son père, parmi les huit qu'elle portait.",
    ),
    (
        "Ce soir-là, Hasol retira aussi les cinq autres runes et les rangea à part, "
        "puis équipa ses huit nouvelles runes.",
        "Ce soir-là, Hasol retira aussi les six autres runes et les rangea à part, "
        "puis équipa ses huit nouvelles runes.",
    ),
)
CHAMPS_HUITIEME_CERCLE = (
    "  <p>Cercles de mana : 7 → 8</p>\n"
    "  <p>Emplacements runiques : 8</p>\n"
)


def sans_sommaire_et_ancres(source):
    """Inverse uniquement l'ajout exact de navigation demandé par l'auteur."""
    titres = re.findall(r"^## (Chapitre (\d+) — [^\n]+)$", source, re.M)
    if [numero for _, numero in titres] != ["1", "2"]:
        raise ValueError("Deux chapitres existants attendus")
    sommaire = "## Sommaire\n\n" + "".join(
        f"{numero}. [{titre}](#chapitre-{numero})\n" for titre, numero in titres
    ) + "\n"
    introduction = (
        "# Les Chroniques de l’Arcaniste Runique\n\n"
        "*Livre II — Le Vertige des vies oubliées*\n\n"
    )
    if source.count("## Sommaire") != 1 or not source.startswith(
            introduction + sommaire + "---\n\n"):
        raise ValueError("Sommaire exact attendu après le titre du livre")
    if re.findall(r'<span id="chapitre-[^"]*"></span>', source) != [
            f'<span id="chapitre-{numero}"></span>' for _, numero in titres]:
        raise ValueError("Ancres de chapitres uniques attendues dans l'ordre")
    source = source.replace(sommaire, "", 1)
    for titre, numero in titres:
        ancre = f'<span id="chapitre-{numero}"></span>\n\n'
        if source.count(ancre + "## " + titre + "\n") != 1:
            raise ValueError("Ancre attendue immédiatement devant son titre")
        source = source.replace(ancre + "## " + titre + "\n", "## " + titre + "\n", 1)
    return source


class ImportLivreIITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_bytes().decode("utf-8")
        cls.document = Document(cls.source)
        cls.sans_navigation = sans_sommaire_et_ancres(cls.source)
        cls.chapitre_1, cls.chapitre_2 = re.split(
            r"\n---\n\n(?=## Chapitre 2\b)", cls.sans_navigation, maxsplit=1)

    def test_sommaire_et_ancres_uniques_correspondent_aux_seuls_titres_existants(self):
        titres = re.findall(r"^## (Chapitre (\d+) — [^\n]+)$", self.source, re.M)
        liens = re.findall(r"^(\d+)\. \[([^\n]+)\]\(#chapitre-(\d+)\)$",
                           self.source, re.M)
        self.assertEqual(liens, [(numero, titre, numero) for titre, numero in titres])
        self.assertEqual(self.source.count(
            "## Sommaire\n"), 1)
        self.assertEqual(re.findall(r"\(#chapitre-[^)]+\)", self.source),
                         [f"(#chapitre-{numero})" for _, numero in titres])
        self.assertNotIn('<span id="chapitre-', self.sans_navigation)

    def test_retrait_navigation_refuse_les_alterations_et_ne_masque_pas_la_narration(self):
        for avant, apres in (
            ("(#chapitre-1)", "(#chapitre-3)"),
            ("1. [Chapitre 1", "1. [Autre titre"),
            ('<span id="chapitre-1"></span>', '<span id="chapitre-2"></span>'),
            ('<span id="chapitre-1"></span>',
             '<span id="chapitre-1"></span>\n\n<span id="chapitre-1"></span>'),
            ('<span id="chapitre-2"></span>\n\n', ''),
            ('<span id="chapitre-1"></span>\n\n',
             '<span id="chapitre-1"></span>\n\nTexte ajouté\n\n'),
            ("---\n\n", "Texte ajouté\n\n---\n\n"),
            ("(#chapitre-2)\n", "(#chapitre-2)\n3. [Futur](#chapitre-3)\n"),
        ):
            with self.subTest(alteration=apres), self.assertRaises(ValueError):
                sans_sommaire_et_ancres(self.source.replace(avant, apres, 1))
        for texte in ("Une délicieuse odeur", "## Chapitre 2 — Les prodiges"):
            with self.subTest(texte=texte):
                modifie = self.source.replace(texte, texte + " ALTÉRÉ", 1)
                if texte.startswith("##"):
                    with self.assertRaises(ValueError):
                        sans_sommaire_et_ancres(modifie)
                else:
                    self.assertEqual(sans_sommaire_et_ancres(modifie),
                                     self.sans_navigation.replace(texte, texte + " ALTÉRÉ", 1))
                    chapitre_1 = re.split(r"\n---\n\n(?=## Chapitre 2\b)",
                                          sans_sommaire_et_ancres(modifie), maxsplit=1)[0]
                    self.assertNotEqual(hashlib.sha256(chapitre_1.encode("utf-8")).hexdigest(),
                                        "eed12b51da5554ef3671b7a035104451c6d746c9738b3d1acac6087a9ab9ea8b")

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
        # DEC-172 : une seule identification narrative et la fiche complète de F01.
        avant = "L'artisan récupéra une rune blanche de faible valeur."
        apres = "L'artisan récupéra une rune Énergie commune (blanche), 1★, +0, de faible valeur."
        self.assertEqual(original.count(avant), 1)
        self.assertEqual(generated.count(apres), 1)
        original = original.replace(avant, apres, 1)
        ouverture = ('<div class="rune-window green-grade lit-window" '
                     'data-window-id="L2-C2-F01" data-window-type="amelioration">\n')
        fiche = ouverture + FICHE_ORVEN + "\n</div>"
        self.assertEqual(generated.count(fiche), 1)
        generated = generated.replace(fiche, "Vitesse.", 1)
        # Seul l'ajout exact dans F02 est inversé, jamais les descriptions ailleurs.
        ouverture_lame = ('<div class="system-window lit-window" '
                          'data-window-id="L2-C2-F02" data-window-type="competence">\n')
        notification_lame = (
            '  <div class="system-header lit-window__header">Nouvelle compétence passive acquise.</div>\n'
            '  <p>Lame runique.</p>\n'
        )
        description_lame = "".join(f"  <p>{texte}</p>\n" for texte in DESCRIPTION_LAME)
        fiche_lame = ouverture_lame + notification_lame + description_lame + "</div>"
        self.assertEqual(generated.count(fiche_lame), 1)
        generated = generated.replace(
            fiche_lame, ouverture_lame + notification_lame + "</div>", 1)
        # DEC-175/176 : inversion limitée à la réserve immédiate et aux deux champs F03.
        ouverture_cercle = ('<div class="system-window lit-window" '
                            'data-window-id="L2-C2-F03" data-window-type="croissance">\n')
        notification_cercle = (
            '  <div class="system-header lit-window__header">Croissance runique — Seuil atteint.</div>\n'
            '  <p>Un cercle de mana supplémentaire a été obtenu.</p>\n'
        )
        fiche_cercle = ouverture_cercle + notification_cercle + CHAMPS_HUITIEME_CERCLE + "</div>"
        self.assertEqual(generated.count(fiche_cercle), 1)
        generated = generated.replace(
            fiche_cercle, ouverture_cercle + notification_cercle + "</div>", 1)
        for avant, apres in CORRECTIONS_RESERVE_IMMEDIATE:
            with self.subTest(reserve=apres):
                self.assertEqual(generated.count(apres), 1)
                generated = generated.replace(apres, avant, 1)
        # DEC-174 : inversion exacte des cinq seuls raccords, sans exclure la section IV.
        for avant, apres in CORRECTIONS_SEPT_RUNES:
            with self.subTest(correction=avant):
                self.assertEqual(original.count(avant), 1)
                self.assertEqual(generated.count(apres), 1)
                generated = generated.replace(apres, avant, 1)

        def texte_utile(source):
            # Seuls le balisage de présentation et les espaces de mise en page diffèrent.
            return compact(re.sub(r"[*#]", "", Document(source).root.text()))

        self.assertEqual(texte_utile(generated), texte_utile(original))

    def test_sept_puis_huit_runes_reserve_immediate_surprise_et_retrait_des_six_autres(self):
        section = re.search(r"^### IV\.[\s\S]*?(?=^### V\.)", self.chapitre_2, re.M).group()
        avant_bureau, au_bureau = section.split("Dans le bureau de ce dernier,", 1)
        passages = (
            "Avec sept cercles, elle portait déjà sept runes, choisies avec Orven et Ray : "
            "quatre Fatal, dont celle offerte par son père, deux Gardien, dont son autre cadeau, "
            "et une Énergie.",
            CORRECTIONS_RESERVE_IMMEDIATE[0][1].split("\n\n")[1],
            "Une notification apparut.",
            "Cercles de mana : 7 → 8",
            "Emplacements runiques : 8",
            CORRECTIONS_RESERVE_IMMEDIATE[1][1],
            "— Monsieur Arowell ! J'ai huit cercles !",
            "Huit runes équipées.",
            CORRECTIONS_RESERVE_IMMEDIATE[3][1],
            "— Je crois savoir à quoi tu penses.",
            "— À quoi ?",
            "— Aux runes.",
            CORRECTIONS_RESERVE_IMMEDIATE[4][1],
            "— Attends, ne sois pas trop pressée. L'Académie te réserve une surprise. Tu verras.",
        )
        position = 0
        for passage in passages:
            with self.subTest(passage=passage):
                trouve = avant_bureau.find(passage, position)
                self.assertGreaterEqual(trouve, position)
                position = trouve + len(passage)
        self.assertNotIn("Vol de vie", avant_bureau)
        self.assertNotIn("Iseria", avant_bureau)
        self.assertNotIn("L2-ORV-R001", avant_bureau)
        self.assertNotRegex(avant_bureau, r"sept (?:sur huit|runes sur huit)|7/8|huitième rune manquante")
        composition = CORRECTIONS_SEPT_RUNES[0][1].split("\n\n")[1]
        self.assertNotRegex(composition, r"★|[0-9]|rare|légendaire|affixe|principale|secondaire")
        reserve = CORRECTIONS_RESERVE_IMMEDIATE[0][1].split("\n\n")[1]
        self.assertNotRegex(reserve, r"★|[0-9]|rare|légendaire|affixe|principale|secondaire")
        self.assertNotRegex(CORRECTIONS_RESERVE_IMMEDIATE[3][1], r"%|PV|Mana|Attaque")
        self.assertIn(CORRECTIONS_RESERVE_IMMEDIATE[5][1], au_bureau)
        rangement = "Hasol installa soigneusement les deux pierres dans des compartiments séparés."
        retrait = CORRECTIONS_RESERVE_IMMEDIATE[6][1]
        self.assertLess(au_bureau.index(rangement), au_bureau.index(retrait))
        self.assertIn("Deux ensembles Vol de vie complets.", au_bureau)
        self.assertNotIn("les cinq autres runes", au_bureau)
        self.assertNotRegex(retrait, r"vend|rééquip|3★")

    def test_popup_huitieme_cercle_avant_apres_sans_confondre_capacite_et_equipement(self):
        window = next(w for w in self.document.windows
                      if w.attrs.get("data-window-id") == "L2-C2-F03")
        self.assertEqual(window.classes, {"system-window", "lit-window"})
        self.assertEqual(window.attrs["data-window-type"], "croissance")
        text = compact(list(window.descendants("details"))[0].text())
        fragments = ("Croissance runique — Seuil atteint.",
                     "Un cercle de mana supplémentaire a été obtenu.",
                     "Cercles de mana : 7 → 8", "Emplacements runiques : 8")
        for fragment in fragments:
            self.assertIn(fragment, text)
        self.assertNotRegex(text, r"équip|rareté|rang|bonus|%")
        for suffixe in (".svg", "-mobile.svg"):
            tree = ET.parse(ROOT / ASSETS / ("L2-C2-F03" + suffixe))
            svg_text = compact(" ".join(
                "".join(n.itertext()) for n in tree.iter() if n.tag.endswith("}text")))
            for fragment in fragments:
                self.assertIn(fragment, svg_text)

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
            "Caractéristique secondaire : Vitesse +1", "Nouvelle compétence passive acquise. Lame runique.",
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

    def test_fiche_orven_complete_une_seule_secondaire_vitesse_en_gras(self):
        window = next(w for w in self.document.windows
                      if w.attrs.get("data-window-id") == "L2-C2-F01")
        self.assertIn("rune-window", window.classes)
        self.assertIn("green-grade", window.classes)
        self.assertEqual(window.attrs["data-window-type"], "amelioration")
        transcript = list(window.descendants("details"))
        self.assertEqual(len(transcript), 1)
        text = compact(transcript[0].text())
        for fragment in ("RUNE AMÉLIORÉE", "Rune Énergie",
                         "Grade actuel : Peu commun (Vert)", "Grade natif : Commun (Blanc)",
                         "Rang : 1★", "Amélioration : +3",
                         "Caractéristique principale : Résistance +4 %",
                         "Caractéristique secondaire : Vitesse +1"):
            self.assertIn(fragment, text)
        self.assertEqual(text.count("Caractéristique secondaire :"), 1)
        self.assertEqual([compact(n.text()) for n in window.descendants("span")
                          if "rune-bonus" in n.classes], ["Résistance +4 %", "Vitesse +1"])
        self.assertEqual([compact(n.text()) for n in window.descendants("strong")], ["Vitesse +1"])
        self.assertNotIn("ensemble", text.lower())
        self.assertNotIn("temporaire", text.lower())
        for suffixe in (".svg", "-mobile.svg"):
            tree = ET.parse(ROOT / ASSETS / ("L2-C2-F01" + suffixe))
            nodes = [n for n in tree.iter() if n.tag.endswith("}text")]
            svg_text = compact(" ".join("".join(n.itertext()) for n in nodes))
            for fragment in ("Rune Énergie", "Peu commun (Vert)", "Commun (Blanc)",
                             "1★", "+3", "Résistance +4 %", "Vitesse +1"):
                self.assertIn(fragment, svg_text)
            for valeur in ("Vitesse", "+1"):
                emphase = [n for n in nodes if n.text == valeur]
                self.assertEqual(len(emphase), 1)
                self.assertEqual(emphase[0].get("font-weight"), "700")
                self.assertEqual(emphase[0].get("fill"), "#175b9b")

    def test_lame_runique_passive_et_description_exacte_en_html_et_svg(self):
        window = next(w for w in self.document.windows
                      if w.attrs.get("data-window-id") == "L2-C2-F02")
        self.assertEqual(window.attrs["data-window-type"], "competence")
        transcripts = list(window.descendants("details"))
        self.assertEqual(len(transcripts), 1)
        self.assertEqual([compact(n.text()) for n in transcripts[0].descendants("p")],
                         ["Lame runique.", *DESCRIPTION_LAME])
        fragments = ("Nouvelle compétence passive acquise.", "Lame runique.",
                     *DESCRIPTION_LAME)
        for suffixe in (".svg", "-mobile.svg"):
            with self.subTest(variante=suffixe):
                tree = ET.parse(ROOT / ASSETS / ("L2-C2-F02" + suffixe))
                svg_text = compact(" ".join(
                    "".join(n.itertext()) for n in tree.iter() if n.tag.endswith("}text")))
                for fragment in fragments:
                    self.assertIn(fragment, svg_text)
        self.assertIn(fragments[0], compact(transcripts[0].text()))

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
