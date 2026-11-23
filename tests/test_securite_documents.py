"""Absence de contenu actif, y compris hors des fenêtres du système."""

from pathlib import Path
import unittest
from urllib.parse import urlsplit

from lecture_support import Document


ROOT = Path(__file__).resolve().parents[1]


def assert_passive(case, source):
    document = Document(source)
    for node in document.root.descendants():
        case.assertNotIn(node.tag, {"script", "base", "form", "iframe", "object", "embed"})
        if node.tag == "meta":
            case.assertNotEqual(node.attrs.get("http-equiv", "").lower(), "refresh")
        for key, value in node.attrs.items():
            case.assertFalse(key.lower().startswith("on"), key)
            if key.lower() in {"src", "href", "xlink:href", "srcset", "action", "formaction", "poster"}:
                parsed = urlsplit(value)
                case.assertEqual((parsed.scheme, parsed.netloc), ("", ""), value)
                case.assertNotIn("\\", value)
            if key == "style":
                case.assertNotRegex(value, r"(?i)@import|expression\s*\(|url\(")
        if node.tag == "style":
            case.assertNotRegex(node.text(), r"(?i)@import|expression\s*\(|url\(")


class DocumentsPassifsTests(unittest.TestCase):
    def test_manuscrit_et_lecteur_entiers_sans_contenu_actif_ni_ressource_distante(self):
        for filename in ("roman.md", "lecture.html"):
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
                          '<style>@import "https://exemple.org/style.css";</style>'):
            with self.subTest(injection=injection):
                with self.assertRaises(AssertionError):
                    assert_passive(self, valid + injection)


if __name__ == "__main__":
    unittest.main()
