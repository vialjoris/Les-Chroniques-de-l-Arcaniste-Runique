"""Invariants de la migration visuelle du 27 novembre, sans écriture ni réseau."""

import json
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

from lecture_support import Document, compact, digest, visual_text, before_bubble_presentation
from test_fenetres_github import load_generator
from test_securite_documents import assert_passive
from test_runes_livre_i import inventory_rows, rune_identifier, states_from_lore, validate_affixes
from test_import_livre_ii import lore_chapter_3_equipment, rune_record


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = json.loads((Path(__file__).parent / "fixtures" /
                        "fenetres_avant_bulles_20261127.json").read_text(encoding="utf-8"))
SVG_NS = "{http://www.w3.org/2000/svg}"
RARITIES = {
    "rune-common": ("Gardien", "commune", "common"),
    "rune-uncommon": ("Fatal", "peu commune", "uncommon"),
    "rune-rare": ("Vol de vie", "rare", "rare"),
    "rune-epic": ("Arcanique", "épique", "epic"),
    "rune-legendary": ("Énergie", "légendaire", "legendary"),
    "common": ("Marcheuse du voile", "commune", "common"),
    "rare": ("Gardien", "rare", "rare"),
    "legendary": ("Sage runique", "légendaire", "legendary"),
    "astral": ("Arcaniste Astral", "astrale", "astral"),
}
RUNE_GRADES = {
    "common": "commune (blanche)",
    "uncommon": "peu commune (verte)",
    "rare": "rare (bleue)",
    "epic": "épique (violette)",
    "legendary": "légendaire (orange)",
}


def rune_row_record(row):
    cells = [node for node in row.children if node.tag in {"td", "th"}]
    if len(cells) != 3:
        raise ValueError("Trois cellules attendues pour une fiche d'inventaire complète")
    bubbles = [node for node in cells[0].descendants() if "data-rarity" in node.attrs]
    if len(bubbles) != 1:
        raise ValueError("Une seule rune attendue dans cette ligne")
    bubble = bubbles[0]
    grade = RUNE_GRADES[bubble.attrs["data-rarity"]]
    stars = re.search(r"([1-6])★", cells[0].text())
    upgrade = re.search(r"\+(\d+)\b", cells[0].text())
    if not stars or not upgrade:
        raise ValueError("Étoiles et amélioration obligatoires")
    identity = f"{compact(bubble.text())} {grade}, {stars[1]}★"
    return identity, int(upgrade[1]), compact(cells[1].text()), compact(cells[2].text())


def contrast(first, second):
    def luminance(color):
        values = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
                  for value in values]
        return sum(value * weight for value, weight in zip(linear, (0.2126, 0.7152, 0.0722)))
    lighter, darker = sorted((luminance(first), luminance(second)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def css_rules(source):
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    rules = {}
    for selectors, body in re.findall(r"([^{}]+)\{([^{}]*)\}", source):
        values = dict(re.findall(r"([\w-]+)\s*:\s*([^;]+)", body))
        for selector in selectors.split(","):
            rules.setdefault(selector.strip(), {}).update(
                {key.strip(): value.strip().lower() for key, value in values.items()})
    return rules


def conservation_contract(source):
    document = Document(source)
    values = {
        "outside_segments": document.outside_segments(),
        "window_ids": [window.attrs["data-window-id"] for window in document.windows],
        "rune_ids": [[node.attrs["data-rune-id"] for node in window.descendants()
                      if "data-rune-id" in node.attrs] for window in document.windows],
        "numbers": [re.findall(r"[+−-]?\d+(?:[ \u00a0]\d{3})*(?:[,.]\d+)?|★+",
                               re.sub(r"Rareté : ★ LÉGENDAIRE ★", "", compact(window.text())))
                    for window in document.windows],
        "affixes": [re.findall(
            r"(?:PV|Attaque|Défense|Vitesse|Mana|PA|Précision|Résistance) \+\d[\d ]*(?: %)?",
            compact(window.text())) for window in document.windows],
        "bonus": [[(sorted(node.classes & {"rune-bonus", "temporary-bonus", "success-text"}),
                    compact(node.text())) for node in window.descendants()
                   if node.classes & {"rune-bonus", "temporary-bonus", "success-text"}
                   and re.search(r"\d", node.text())]
                  for window in document.windows],
    }
    return {key: digest(json.dumps(value, ensure_ascii=False)) for key, value in values.items()}


class ConservationBullesTests(unittest.TestCase):
    def test_inversion_bornee_retrouve_les_deux_baselines_sans_fichier_temporaire(self):
        for book, (name, reference) in enumerate(REFERENCE["books"].items(), 1):
            source = (ROOT / name).read_bytes().decode("utf-8")
            restored = before_bubble_presentation(source, book)
            with self.subTest(livre=name):
                self.assertEqual(digest(restored), reference["source_sha256"])
                self.assertEqual(before_bubble_presentation(restored, book), restored)
                self.assertEqual(Document(restored).outside_segments(), Document(source).outside_segments())
                for changed in (source.replace("Attaque +70", "Attaque +71", 1),
                                "Ajout non autorisé\n" + source,
                                source.replace('data-rarity="rare"', 'data-rarity="legendary"', 1)):
                    self.assertNotEqual(changed, source)
                    with self.assertRaises(ValueError):
                        before_bubble_presentation(changed, book)

    def test_octets_hors_fenetres_ordre_ids_et_donnees_chiffrees_preserves_dans_les_deux_livres(self):
        for name, expected in REFERENCE["books"].items():
            source = (ROOT / name).read_bytes().decode("utf-8")
            with self.subTest(livre=name):
                self.assertEqual(len(Document(source).windows), expected["window_count"])
                actual = conservation_contract(source)
                for key, checksum in actual.items():
                    with self.subTest(contrat=key):
                        self.assertEqual(checksum, expected[key])

    def test_contrat_detecte_les_pertes_et_permutations_sans_dependre_des_ids_operationnels(self):
        source = ('Prose\r\n<div class="rune-window" data-window-id="exemple">'
                  '<p data-rune-id="PIERRE-TEST">Fatal 6★ +15</p>'
                  '<p>Attaque +160 ; Vitesse +8 ; PV +25</p>'
                  '<span class="rune-bonus">+35 %</span></div>\r\nFin.')
        expected = conservation_contract(source)
        changes = {
            "outside_segments": ("Prose\r\n", "Prose\n"),
            "window_ids": ('data-window-id="exemple"', 'data-window-id="autre"'),
            "rune_ids": ('data-rune-id="PIERRE-TEST"', 'data-rune-id="AUTRE-PIERRE"'),
            "numbers": ("6★ +15", "5★ +15"),
            "affixes": ("Vitesse +8 ; PV +25", "PV +25 ; Vitesse +8"),
            "bonus": ('class="rune-bonus"', 'class="temporary-bonus"'),
        }
        for contract, (before, after) in changes.items():
            with self.subTest(contrat=contract):
                self.assertIn(before, source)
                self.assertNotEqual(conservation_contract(source.replace(before, after))[contract],
                                    expected[contract])
        self.assertEqual(conservation_contract(source.replace("<p>", "<p class=\"presentation\">")),
                         expected)


class BullesPresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.generator = load_generator()
        cls.rules = css_rules((ROOT / "style.css").read_text(encoding="utf-8"))

    def test_neuf_variantes_css_svg_contraste_texte_et_bordure_commune(self):
        palettes = {}
        for variant, (name, rarity, metadata) in RARITIES.items():
            with self.subTest(variante=variant):
                declarations = self.rules[".lit-badge--" + variant]
                foreground, background = declarations["color"], declarations["background"]
                self.assertGreaterEqual(contrast(foreground, background), 4.5)
                palettes[variant] = background
                if metadata == "common":
                    self.assertEqual(background, "#ffffff")
                    self.assertGreaterEqual(contrast(declarations["border-color"], background), 3)
                source = ('<div class="rune-window lit-window" data-window-id="essai-palette">'
                          '<div class="system-header">Palette de test</div><p>'
                          f'<span class="lit-badge lit-badge--{variant}" data-rarity="{metadata}">{name}</span>'
                          f'<span class="lit-sr-only"> ({rarity})</span>'
                          '</p><p>Principale : Attaque +70</p></div>')
                _, images = self.generator.produire(source)
                self.assertEqual(len(images), 2)
                for asset, content in images.items():
                    with self.subTest(svg=asset):
                        svg = ET.fromstring(content)
                        badge = next(node for node in svg.iter(SVG_NS + "text") if node.text == name)
                        self.assertEqual(badge.attrib["fill"].lower(), foreground)
                        rectangles = [node for node in svg.iter(SVG_NS + "rect")
                                      if node.attrib.get("fill", "").lower() == background]
                        self.assertTrue(rectangles)
                        self.assertGreaterEqual(contrast(badge.attrib["fill"], background), 4.5)
                        description = compact(" ".join(node.text or "" for node in svg.iter(SVG_NS + "desc")))
                        self.assertIn(f"{name} ({rarity})", description)
                        shown = compact(" ".join("".join(node.itertext()) for node in svg.iter(SVG_NS + "text")))
                        self.assertNotIn(f"({rarity})", shown)
                        self.assertIn("Attaque +70", shown)
        self.assertEqual(len({palettes[key] for key in palettes if key.startswith("rune-")}), 5)
        self.assertEqual(len({palettes[key] for key in palettes if not key.startswith("rune-")}), 4)
        self.assertEqual(palettes["astral"], palettes["rune-epic"])
        self.assertNotEqual(palettes["astral"], palettes["legendary"])

    def test_rarete_en_texte_reel_associee_a_chaque_bulle_sans_role_interactif(self):
        checked = 0
        for name in REFERENCE["books"]:
            document = Document((ROOT / name).read_bytes().decode("utf-8"))
            for window in document.windows:
                details = list(window.descendants("details"))
                self.assertEqual(len(details), 1)
                self.assertNotIn("open", details[0].attrs)
                for node in details[0].descendants():
                    if "lit-badge" not in node.classes:
                        continue
                    if window.attrs.get("data-window-type") == "competence" and "data-rarity" not in node.attrs:
                        # La rareté propre à une compétence n'est pas une classe de personnage.
                        continue
                    variants = [value.removeprefix("lit-badge--") for value in node.classes
                                if value.startswith("lit-badge--")]
                    self.assertEqual(len(variants), 1)
                    variant = variants[0]
                    self.assertIn(variant, RARITIES)
                    rarity, metadata = RARITIES[variant][1:]
                    with self.subTest(livre=name, fenetre=window.attrs["data-window-id"], bulle=node.text()):
                        self.assertEqual(node.attrs.get("data-rarity"), metadata)
                        self.assertNotIn("role", node.attrs)
                        self.assertNotIn("tabindex", node.attrs)
                        self.assertTrue(compact(node.text()))
                        self.assertNotRegex(node.text(), r"(?i)\b(?:commune?|rare|épique|légendaire)\b|[()]")
                        siblings = node.parent.children
                        index = siblings.index(node)
                        self.assertLess(index + 1, len(siblings), "La couleur/ARIA seuls ne sont pas un repli")
                        supplement = siblings[index + 1]
                        self.assertIn(rarity, compact(supplement.text()).lower())
                        self.assertNotIn("aria-hidden", supplement.attrs)
                        self.assertNotIn("hidden", supplement.attrs)
                    checked += 1
        self.assertGreater(checked, 100)

    def test_alternative_oriente_vers_transcription_et_svg_reste_passif_integral(self):
        for name in REFERENCE["books"]:
            source = (ROOT / name).read_bytes().decode("utf-8")
            document = Document(source)
            assert_passive(self, source)
            directory = ROOT / "assets" / ("fenetres-livre-2" if name.startswith("livre_2") else "fenetres")
            for window in document.windows:
                identifier = window.attrs["data-window-id"]
                with self.subTest(livre=name, fenetre=identifier):
                    image = next(window.descendants("img"))
                    self.assertIn("Version textuelle complète dans le volet suivant", image.attrs.get("alt", ""))
                    rune_ids = {node.attrs["data-rune-id"] for node in window.descendants()
                                if "data-rune-id" in node.attrs}
                    for node in window.descendants():
                        for key, value in node.attrs.items():
                            if key != "data-rune-id":
                                for rune_id in rune_ids:
                                    self.assertNotIn(rune_id, value)
                    for suffix in ("", "-mobile"):
                        content = (directory / f"{identifier}{suffix}.svg").read_text(encoding="utf-8")
                        self.assertNotRegex(content, r"(?i)<(?:script|foreignObject|image)\b|javascript:|@import|https?://(?!www.w3.org/2000/svg)")
                        svg = ET.fromstring(content)
                        shown = " ".join("".join(node.itertext()) for node in svg.iter(SVG_NS + "text"))
                        self.assertEqual(re.sub(r"\s+", "", shown), re.sub(r"\s+", "", visual_text(window)))
                        description = " ".join("".join(node.itertext()) for node in svg.iter(SVG_NS + "desc"))
                        self.assertEqual(compact(description), compact(window.text()))
                        for rune_id in rune_ids:
                            self.assertNotIn(rune_id, content)

    def test_iseria_ne_recoit_aucune_classe_astrale_dans_les_fenetres_ni_leurs_alternatives(self):
        for name in REFERENCE["books"]:
            source = (ROOT / name).read_bytes().decode("utf-8")
            for window in Document(source).windows:
                content = source[window.start:window.end]
                if "Iseria" not in content:
                    continue
                with self.subTest(livre=name, fenetre=window.attrs["data-window-id"]):
                    self.assertNotRegex(content, r'lit-badge--astral|Classe astrale|classe astrale')
                    self.assertNotRegex(content, r'(?i)Iseria.{0,100}(?:rang|classe|rareté)\s*:?\s*astral')

    def test_noms_raretes_etoiles_paliers_et_affixes_des_inventaires_restent_conformes_au_lore(self):
        lore = (ROOT / "lore/runes.md").read_text(encoding="utf-8")
        states = states_from_lore(lore)
        final_life_2 = lore_chapter_3_equipment(lore)
        checked = [0, 0]
        for name in REFERENCE["books"]:
            book_2 = name.startswith("livre_2")
            source = (ROOT / name).read_bytes().decode("utf-8")
            for window in Document(source).windows:
                rows = ([row for row in window.descendants("tr")
                         if len([cell for cell in row.children if cell.tag == "td"]) == 3]
                        if book_2 else inventory_rows(window))
                for row in rows:
                    identifier = rune_identifier(row)
                    if identifier is None:
                        # Les transitions réelles/projetées restent contrôlées par les tests historiques.
                        continue
                    with self.subTest(livre=name, fenetre=window.attrs["data-window-id"], rune=identifier):
                        identity, level, main, subs = rune_row_record(row)
                        validate_affixes(identity, level, main, subs)
                        if book_2:
                            self.assertEqual(rune_record(f"{identity}, +{level}", main, subs),
                                             final_life_2[identifier])
                        else:
                            self.assertEqual((identity, main, subs), states[identifier, level])
                    checked[int(book_2)] += 1
        self.assertGreater(checked[0], 100)
        self.assertEqual(checked[1], 32)

    def test_lecture_metier_des_bulles_refuse_les_mutations_meme_si_le_texte_de_rarete_est_change_aussi(self):
        source = ('<table><tr data-rune-id="EXEMPLE"><td>'
                  '<span class="lit-badge lit-badge--rune-rare" data-rarity="rare">Fatal</span>'
                  '<span class="lit-sr-only"> (rare (bleue))</span>, 6★, +15</td>'
                  '<td>Attaque +160</td><td>Vitesse +8 ; PV +25 ; Mana +20 ; PA +60</td></tr></table>')
        record = lambda value: rune_row_record(next(Document(value).root.descendants("tr")))
        expected = record(source)
        for before, after in ((">Fatal<", ">Gardien<"), ('data-rarity="rare"', 'data-rarity="legendary"'),
                              ("6★", "5★"), ("+15", "+14"), ("Attaque +160", "Attaque +161"),
                              ("Vitesse +8 ; PV +25", "PV +25 ; Vitesse +8")):
            with self.subTest(mutation=(before, after)):
                changed = source.replace(before, after)
                self.assertNotEqual(changed, source)
                self.assertNotEqual(record(changed), expected)

    def test_calcul_de_contraste_refuse_les_couleurs_trop_claires(self):
        self.assertAlmostEqual(contrast("#000000", "#ffffff"), 21)
        self.assertLess(contrast("#ffffff", "#edf7ef"), 4.5)
        self.assertGreaterEqual(contrast("#ffffff", "#22643b"), 4.5)

    def test_fenetre_simple_sans_id_reste_lisible_mais_enveloppe_github_sans_id_refusee(self):
        from scripts.generer_lecture import generer_html
        source = '# Exemple\n\n<div class="system-window lit-window"><p>Niveau : 1</p></div>'
        result = generer_html(source, "style.css")
        self.assertEqual(compact(Document(result).windows[0].text()), "Niveau : 1")
        identified = source.replace('class="system-window lit-window"',
                                    'class="system-window lit-window" data-window-id="exemple"')
        wrapped, _ = self.generator.produire(identified)
        malformed = wrapped.replace(' data-window-id="exemple"', "")
        with self.assertRaises(ValueError):
            generer_html(malformed, "style.css")

    def test_impression_affiche_les_raretes_et_evite_les_transcriptions_en_double(self):
        css = (ROOT / "style.css").read_text(encoding="utf-8")
        print_rules = {}
        for match in re.finditer(r"@media\s+print\s*\{", css):
            start, depth, end = match.end(), 1, match.end()
            while end < len(css) and depth:
                depth += (css[end] == "{") - (css[end] == "}")
                end += 1
            print_rules.update(css_rules(css[start:end - 1]))
        rarity = print_rules[".lit-window .lit-sr-only"]
        self.assertEqual(rarity["position"], "static")
        self.assertEqual(rarity["clip-path"], "none")
        self.assertEqual(rarity["overflow"], "visible")
        self.assertEqual((rarity["width"], rarity["height"]), ("auto", "auto"))
        self.assertNotEqual(rarity.get("display"), "none")
        self.assertEqual(print_rules[".lit-window__accessible-details"]["display"], "none")


if __name__ == "__main__":
    unittest.main()
