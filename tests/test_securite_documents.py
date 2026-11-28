"""Absence de contenu actif, y compris hors des fenêtres du système."""

from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

from lecture_support import Document


ROOT = Path(__file__).resolve().parents[1]


def assert_passive(case, source):
    def local_url(value):
        try:
            parsed = urlsplit(value.strip())
        except ValueError:
            case.fail(f"URL illisible : {value!r}")
        case.assertEqual((parsed.scheme, parsed.netloc), ("", ""), value)
        case.assertNotIn("\\", value)

    # Les images Markdown ne sont pas des balises pour HTMLParser.
    for target in re.findall(r'!\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)', source):
        local_url(target.strip("<>"))
    references = dict(re.findall(r'(?m)^\s*\[([^\]]+)\]:\s*<?([^\s>]+)>?', source))
    for label, identifier in re.findall(r'!\[([^\]]*)\]\[([^\]]*)\]', source):
        local_url(references.get(identifier or label, ""))
    document = Document(source)
    for node in document.root.descendants():
        case.assertNotIn(node.tag, {"script", "base", "form", "iframe", "object", "embed", "foreignobject", "image"})
        if node.tag == "meta":
            case.assertNotEqual(node.attrs.get("http-equiv", "").lower(), "refresh")
        for key, value in node.attrs.items():
            case.assertFalse(key.lower().startswith("on"), key)
            if key.lower() in {"src", "href", "xlink:href", "srcset", "action", "formaction", "poster"}:
                candidates = value.split(",") if key.lower() == "srcset" else [value]
                for candidate in candidates:
                    if key.lower() == "srcset":
                        tokens = candidate.split()
                        if not tokens:
                            continue
                        candidate = tokens[0]
                    local_url(candidate)
            if key == "style":
                case.assertNotRegex(value, r"(?i)@import|expression\s*\(|url\(")
        if node.tag == "style":
            case.assertNotRegex(node.text(), r"(?i)@import|expression\s*\(|url\(")


class DocumentsPassifsTests(unittest.TestCase):
    def test_manuscrit_et_lecteur_entiers_sans_contenu_actif_ni_ressource_distante(self):
        for filename in ("livre_1_l_ascension_d_une_legende_oubliee.md",
                         "livre_2_le_vertige_des_vies_oubliees.md", "lecture.html"):
            with self.subTest(document=filename):
                assert_passive(self, (ROOT / filename).read_text(encoding="utf-8"))

    def test_injections_hors_fenetres_refusees(self):
        valid = '<h1>Roman</h1><p>Texte conservé.</p><a href="#chapitre-1">Lecture</a>'
        assert_passive(self, valid)
        for injection in ('<meta http-equiv="refresh" content="0;url=https://exemple.org">',
                          '<base href="/ailleurs/">', '<form action="/envoi"></form>',
                          '<script>alert(1)</script>', '<p onclick="alert(1)">Texte</p>',
                          '<img src="https://exemple.org/image.svg">',
                          '<img src="//exemple.org/image.svg">',
                          '<img src="http://[">',
                          '<source srcset="local.svg 1x, https://exemple.org/image.svg 2x">',
                          '<source srcset="local.svg 600w, //exemple.org/image.svg 1200w">',
                          '![image](https://exemple.org/image.svg)',
                          '![image](<https://exemple.org/image.svg>)',
                          '![image][distant]\n[distant]: https://exemple.org/image.svg',
                          '<svg><foreignObject><p>Texte</p></foreignObject></svg>',
                          '<style>@import "https://exemple.org/style.css";</style>'):
            with self.subTest(injection=injection):
                with self.assertRaises(AssertionError):
                    assert_passive(self, valid + injection)

    def test_images_locales_et_srcset_multi_candidat_local_restent_acceptes(self):
        assert_passive(self, '<source srcset="local.svg 1x, local-mobile.svg 2x">'
                       '![image](assets/local.svg)\n![image][local]\n[local]: assets/local.svg')

    def test_document_simple_et_attributs_vides_ne_font_pas_crasher_le_controle(self):
        for source in ("", "Texte simple.", '<img src="">', '<source srcset="">',
                       '<source srcset=" , local.svg 1x, ">'):
            with self.subTest(source=source):
                assert_passive(self, source)

    def test_svg_derives_des_deux_livres_sont_passifs(self):
        for filename, directory in (("livre_1_l_ascension_d_une_legende_oubliee.md", "fenetres"),
                                    ("livre_2_le_vertige_des_vies_oubliees.md", "fenetres-livre-2")):
            document = Document((ROOT / filename).read_text(encoding="utf-8"))
            for window in document.windows:
                for suffix in ("", "-mobile"):
                    path = ROOT / "assets" / directory / (window.attrs["data-window-id"] + suffix + ".svg")
                    with self.subTest(svg=path.name):
                        assert_passive(self, path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
