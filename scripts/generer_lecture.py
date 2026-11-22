#!/usr/bin/env python3
"""Génère le lecteur hors ligne à partir du seul manuscrit officiel."""

import argparse
from html import escape
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote


RACINE = Path(__file__).resolve().parent.parent


def generer_html(source: str, css_href: str) -> str:
    # Le HTML/SVG du manuscrit est une source locale de confiance, pas une saisie web.
    from markdown import Markdown
    from markdown.extensions import Extension
    from markdown.treeprocessors import Treeprocessor

    class StructureLecture(Treeprocessor):
        def run(self, root):
            self.titre = "Les Chroniques de l’Arcaniste Runique"
            self.chapitres = []
            enfants = list(root)
            if enfants and enfants[0].tag == "h1":
                self.titre = "".join(enfants[0].itertext())
                root.remove(enfants[0])

            # Le sommaire du dérivé est recalculé, sans modifier celui du manuscrit.
            for index, enfant in enumerate(enfants[:-1]):
                if (enfant.tag == "h2"
                        and "".join(enfant.itertext()).strip().casefold() == "sommaire"
                        and enfants[index + 1].tag == "ol"):
                    root.remove(enfant)
                    root.remove(enfants[index + 1])
                    break

            for element in root.iter():
                if element.tag == "h1":
                    texte = "".join(element.itertext())
                    chapitre = re.match(r"Chapitre\s+(\d+)\b", texte, re.IGNORECASE)
                    if chapitre:
                        identifiant = f"lecture-chapitre-{chapitre.group(1)}"
                        element.set("id", identifiant)
                        element.set("tabindex", "-1")
                        self.chapitres.append((identifiant, texte))
                if element.tag in {"h1", "h2", "h3", "h4", "h5"}:
                    element.tag = f"h{int(element.tag[1]) + 1}"

    structure = StructureLecture()

    class ExtensionLecture(Extension):
        def extendMarkdown(self, md):
            md.treeprocessors.register(structure, "structure_lecture", 5)

    moteur = Markdown(
        extensions=["tables", "fenced_code", "sane_lists", ExtensionLecture()],
        output_format="html",
    )
    contenu = moteur.convert(source)
    liens = "\n".join(
        f'      <li><a href="#{escape(identifiant, quote=True)}">{escape(titre)}</a></li>'
        for identifiant, titre in structure.chapitres
    )
    navigation = ""
    if liens:
        navigation = f'''<nav class="reader-nav" id="sommaire" aria-labelledby="sommaire-titre">
    <h2 id="sommaire-titre">Sommaire</h2>
    <ol>
{liens}
    </ol>
  </nav>
  '''
    titre = escape(structure.titre)
    return f'''<!doctype html>
<!-- Fichier dérivé de roman.md, généré par scripts/generer_lecture.py. Ne pas modifier à la main. -->
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Joris VIAL">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self' data:; base-uri 'none'; form-action 'none'">
  <title>{titre}</title>
  <link rel="stylesheet" href="{escape(css_href, quote=True)}">
</head>
<body class="reader-body">
  <a class="reader-skip-link" href="#contenu">Aller au texte du roman</a>
  <header class="reader-header">
    <h1>{titre}</h1>
    <p class="reader-author">Joris VIAL</p>
  </header>
  {navigation}<main class="reader-main" id="contenu" tabindex="-1">
{contenu}
  </main>
</body>
</html>
'''


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Générer lecture.html depuis roman.md (HTML/SVG local de confiance).",
        add_help=False,
        epilog=("Lecture hors ligne : conserver le HTML et style.css à leurs emplacements relatifs. "
                "Aucun téléchargement ni JavaScript. Codes de sortie : 0 succès, "
                "1 erreur ou dérivé périmé, 2 arguments invalides."),
    )
    parser.add_argument("-h", "--help", action="help", help="Afficher cette aide et quitter.")
    parser.add_argument("--input", type=Path, default=RACINE / "roman.md",
                        help="Manuscrit Markdown UTF-8 (défaut : roman.md du projet).")
    parser.add_argument("--output", type=Path, default=RACINE / "lecture.html",
                        help="Fichier HTML à produire (défaut : lecture.html du projet).")
    parser.add_argument("--css", type=Path, default=RACINE / "style.css",
                        help="Feuille locale liée, non copiée (défaut : style.css du projet).")
    parser.add_argument("--check", action="store_true",
                        help="Vérifier les octets du dérivé sans écrire ; code 1 si absent ou périmé.")
    args = parser.parse_args(argv)

    try:
        entree = args.input.resolve()
        sortie = args.output.resolve()
        css = args.css.resolve()
        if sortie in {entree, css}:
            raise ValueError("la sortie ne doit remplacer ni le manuscrit ni la feuille CSS")
        if not css.is_file():
            raise ValueError(f"feuille CSS absente ou non lisible : {args.css}")
        source = entree.read_text(encoding="utf-8")
        if not source.strip():
            raise ValueError("le manuscrit est vide")
        css_href = quote(Path(os.path.relpath(css, sortie.parent)).as_posix(), safe="/.")
        resultat = generer_html(source, css_href).encode("utf-8")
        if args.check:
            if not sortie.is_file() or sortie.read_bytes() != resultat:
                print(f"Lecteur absent ou périmé : {args.output}", file=sys.stderr)
                return 1
            print(f"Lecteur à jour : {args.output}")
        else:
            if sortie.exists() and (sortie.samefile(entree) or sortie.samefile(css)):
                raise ValueError("la sortie ne doit remplacer ni le manuscrit ni la feuille CSS")
            sortie.write_bytes(resultat)
            print(f"Lecteur généré : {args.output}")
    except ModuleNotFoundError as erreur:
        if erreur.name != "markdown":
            raise
        print("Erreur : dépendance Markdown absente. Installer : "
              "python3 -m pip install -r requirements-lecture.txt", file=sys.stderr)
        return 1
    except (OSError, UnicodeError, ValueError) as erreur:
        print(f"Erreur de génération : {erreur}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
