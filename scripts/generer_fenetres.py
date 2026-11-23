#!/usr/bin/env python3
"""Fenêtres SVG pour GitHub ; le HTML du manuscrit reste la source unique."""

import argparse
from dataclasses import dataclass, field
from functools import lru_cache
from html import escape
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import stat
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PICTURE_CLASS = "lit-window__github-picture"
TRANSCRIPT_CLASS = "lit-window__transcript"
TOGGLE_CLASS = "lit-window__transcript-toggle"
TOGGLE_TEXT = "Version textuelle de la fenêtre"
VOID = {"br", "hr", "img", "source", "wbr", "meta", "link", "input"}


@dataclass
class Fenetre:
    debut: int
    ouverture: int
    fermeture: int
    fin: int
    identifiant: str


class Reperes(HTMLParser):
    """Repère les racines sans réécrire leur HTML ni le Markdown environnant."""

    def __init__(self, source, verifier_identifiants=True):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.verifier_identifiants = verifier_identifiants
        self.lignes = [0] + [m.end() for m in re.finditer("\n", source)]
        self.profondeur = 0
        self.courante = None
        self.fenetres = []
        self.feed(source)
        if self.courante:
            raise ValueError("Fenêtre HTML non fermée")
        ids = [f.identifiant for f in self.fenetres]
        if verifier_identifiants and len(set(ids)) != len(ids):
            raise ValueError("Identifiants de fenêtres dupliqués")

    def position(self):
        ligne, colonne = self.getpos()
        return self.lignes[ligne - 1] + colonne

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag != "div":
            return
        if "lit-window" in attrs.get("class", "").split():
            if self.courante:
                raise ValueError("Racines de fenêtres imbriquées")
            identifiant = attrs.get("data-window-id", "")
            if self.verifier_identifiants and not re.fullmatch(r"[A-Za-z0-9_-]+", identifiant):
                raise ValueError("Identifiant de fenêtre absent ou non sûr")
            debut = self.position()
            self.courante = (debut, debut + len(self.get_starttag_text()), identifiant)
            self.profondeur = 0
        if self.courante:
            self.profondeur += 1

    def handle_endtag(self, tag):
        if tag == "div" and self.courante:
            self.profondeur -= 1
            if self.profondeur == 0:
                debut, ouverture, identifiant = self.courante
                fermeture = self.position()
                self.fenetres.append(Fenetre(debut, ouverture, fermeture,
                                              fermeture + len("</div>"), identifiant))
                self.courante = None


def extraire_source_fenetres(source: str) -> str:
    """Retire uniquement nos enveloppes GitHub, sans dépendance à Pillow.

    Entrée historique inchangée ; sortie et corps HTML conservés octet pour
    octet. Les enveloppes incomplètes provoquent une erreur plutôt qu'une perte.
    """
    if f'class="{PICTURE_CLASS}"' not in source:
        return source
    identifiants = set()
    for f in reversed(Reperes(source, verifier_identifiants=False).fenetres):
        corps = source[f.ouverture:f.fermeture]
        if f'class="{PICTURE_CLASS}"' not in corps:
            continue
        if not re.fullmatch(r"[A-Za-z0-9_-]+", f.identifiant) or f.identifiant in identifiants:
            raise ValueError("Identifiant de fenêtre enveloppée absent, dupliqué ou non sûr")
        identifiants.add(f.identifiant)
        motif = (r'\n  <picture class="' + PICTURE_CLASS + r'">.*?</picture>'
                 r'\n  <details class="' + TRANSCRIPT_CLASS + r'">'
                 r'\n    <summary class="' + TOGGLE_CLASS + r'">'
                 + re.escape(TOGGLE_TEXT) + r'</summary>')
        entete = re.match(motif, corps, flags=re.S)
        if not entete or not corps.endswith("  </details>\n"):
            raise ValueError(f"Enveloppe GitHub invalide : {f.identifiant}")
        original = corps[entete.end():-len("  </details>\n")]
        source = source[:f.ouverture] + original + source[f.fermeture:]
    return source


@dataclass
class Noeud:
    tag: str
    attrs: dict = field(default_factory=dict)
    enfants: list = field(default_factory=list)

    @property
    def classes(self):
        return self.attrs.get("class", "").split()


class Arbre(HTMLParser):
    def __init__(self, fragment):
        super().__init__(convert_charrefs=True)
        self.racine = Noeud("fragment")
        self.pile = [self.racine]
        self.feed(fragment)

    def handle_starttag(self, tag, attrs):
        noeud = Noeud(tag, dict(attrs))
        self.pile[-1].enfants.append(noeud)
        if tag not in VOID:
            self.pile.append(noeud)

    def handle_startendtag(self, tag, attrs):
        self.pile[-1].enfants.append(Noeud(tag, dict(attrs)))

    def handle_endtag(self, tag):
        if len(self.pile) > 1 and self.pile[-1].tag == tag:
            self.pile.pop()

    def handle_data(self, data):
        self.pile[-1].enfants.append(data)


def texte(noeud):
    if isinstance(noeud, str):
        return noeud
    if noeud.tag == "svg":
        return ""
    return "".join(texte(e) for e in noeud.enfants)


def normaliser(valeur):
    return " ".join(valeur.split())


# Charte explicite, distincte des règles et données du système.
BADGES = {
    "lit-badge--legendary": ("#795b22", "#fbf3dd", "#D1AB61"),
    "lit-badge--rare": ("#175b9b", "#edf4fc", "#b6cce5"),
    "lit-badge--common": ("#42474c", "#f2f3f4", "#c4c8cc"),
    "lit-badge--astral": ("#694493", "#f3edfb", "#cdb9e2"),
    "lit-badge--rune-common": ("#505050", "#FFFFFF", "#c8c8c8"),
    "lit-badge--rune-uncommon": ("#22643b", "#edf7ef", "#b3d3bd"),
    "lit-badge--rune-rare": ("#175b9b", "#edf4fc", "#b6cce5"),
    "lit-badge--rune-epic": ("#694493", "#f3edfb", "#cdb9e2"),
    "lit-badge--rune-legendary": ("#884717", "#fff1e4", "#dfbd98"),
    "upgrade-badge": ("#175b9b", "#edf4fc", "#b6cce5"),
    "passive-badge": ("#55504a", "#f5f2ed", "#d9d2c6"),
}


def fragments(noeud, couleur="#242424", gras=False):
    if isinstance(noeud, str):
        return [(noeud, couleur, gras, None)]
    if noeud.tag == "svg":
        return []
    classes = noeud.classes
    if any(c in classes for c in ("rune-bonus", "lit-window__runic-value")):
        couleur = "#175b9b"
    elif any(c in classes for c in ("temporary-bonus", "success-text")):
        couleur = "#22643b"
    elif "legendary-text" in classes:
        couleur = "#795b22"
    gras = gras or noeud.tag in {"strong", "h2", "h3", "th"}
    for classe in classes:
        if classe in BADGES:
            return [(normaliser(texte(noeud)), BADGES[classe][0], True, BADGES[classe])]
    resultat = []
    for enfant in noeud.enfants:
        resultat.extend(fragments(enfant, couleur, gras))
    return resultat


class Dessin:
    def __init__(self, largeur):
        # Import différé : le lecteur HTML ne dépend pas du générateur d'images.
        from PIL import ImageFont
        self.police = ImageFont.load_default
        self.largeur = largeur
        self.mobile = largeur <= 320
        self.marge = 20 if self.mobile else 28
        self.taille = 18
        self.y = self.marge
        self.elements = []
        self.contenu = []

    @lru_cache(maxsize=4096)
    def mesure(self, valeur, taille):
        # textLength reproduit ces métriques sans charger une police distante.
        return round(self.police(size=taille).getlength(valeur) * 1.08, 2)

    def ligne(self, y, x=None, largeur=None):
        x = self.marge if x is None else x
        largeur = self.largeur - 2 * self.marge if largeur is None else largeur
        self.elements.append(f'<path d="M{x} {y}h{largeur}" stroke="#D8BF8F"/>')

    def flux(self, morceaux, x=None, largeur=None, taille=None):
        x = self.marge if x is None else x
        largeur = self.largeur - 2 * self.marge if largeur is None else largeur
        taille = taille or self.taille
        curseur = x
        hauteur = taille * 1.65
        debut = self.y
        for valeur, couleur, gras, badge in morceaux:
            unites = [valeur] if badge else re.findall(r"\s+|\S+", valeur)
            for unite in unites:
                unite = re.sub(r"\s+", " ", unite)
                if not unite:
                    continue
                # Un badge trop long devient plusieurs badges lisibles, sans perte.
                if self.mesure(unite, taille) + (12 if badge else 0) > largeur:
                    bouts = []
                    courant = ""
                    # Garder les mots entiers dans les bulles quand c'est possible.
                    parties = re.findall(r"\S+\s*|\s+", unite) if " " in unite.strip() else list(unite)
                    parties = [fragment for partie in parties
                               for fragment in (list(partie) if self.mesure(partie, taille) > largeur - 12
                                                else [partie])]
                    for partie in parties:
                        if courant and self.mesure(courant + partie, taille) > largeur - 12:
                            bouts.append(courant)
                            courant = ""
                        courant += partie
                    bouts.append(courant)
                else:
                    bouts = [unite]
                for bout in bouts:
                    w = self.mesure(bout, taille)
                    total = w + (12 if badge else 0)
                    if curseur + total > x + largeur + 0.01 and curseur > x:
                        self.y += hauteur
                        curseur = x
                    if bout.isspace() and curseur == x:
                        self.contenu.append(bout)
                        continue
                    if badge:
                        self.elements.append(
                            f'<rect x="{curseur:.2f}" y="{self.y:.2f}" width="{total:.2f}" '
                            f'height="{taille + 9}" rx="{(taille + 9) / 2}" '
                            f'fill="{badge[1]}" stroke="{badge[2]}"/>')
                    tx = curseur + (6 if badge else 0)
                    self.elements.append(
                        f'<text x="{tx:.2f}" y="{self.y + taille + 1:.2f}" '
                        f'font-size="{taille}" font-weight="{700 if gras else 400}" '
                        f'fill="{couleur}" textLength="{w:.2f}" lengthAdjust="spacingAndGlyphs" '
                        f'xml:space="preserve">{escape(bout)}</text>')
                    self.contenu.append(bout)
                    curseur += total
        self.y = max(self.y, debut) + hauteur

    def icone(self, noeud):
        autorises = {"d", "cx", "cy", "r", "x", "y", "width", "height", "points", "rx"}
        primitives = []
        for enfant in noeud.enfants:
            if isinstance(enfant, Noeud) and enfant.tag in {"path", "circle", "rect", "polygon", "polyline"}:
                attrs = " ".join(f'{k}="{escape(v, quote=True)}"' for k, v in enfant.attrs.items()
                                 if k in autorises)
                primitives.append(f'<{enfant.tag} {attrs}/>')
        self.elements.append(
            f'<g transform="translate({self.marge} {self.y})" fill="none" stroke="#A17B35" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            + "".join(primitives) + '</g>')

    def bloc(self, noeud):
        if isinstance(noeud, str):
            if noeud.strip():
                self.flux(fragments(noeud))
            return
        if "lit-window__header" in noeud.classes:
            for enfant in noeud.enfants:
                if isinstance(enfant, Noeud) and enfant.tag == "svg":
                    self.icone(enfant)
            self.flux(fragments(noeud, "#A17B35", True), self.marge + 36,
                      self.largeur - 2 * self.marge - 36, 24)
            self.y += 10
            self.ligne(self.y)
            self.y += 18
        elif noeud.tag == "hr":
            self.y += 8
            self.ligne(self.y)
            self.y += 15
        elif noeud.tag == "tr":
            cellules = [e for e in noeud.enfants if isinstance(e, Noeud)]
            depart = self.y
            fins = []
            largeur = (self.largeur - 2 * self.marge) / max(1, len(cellules))
            for i, cellule in enumerate(cellules):
                if not self.mobile:
                    self.y = depart
                self.flux(fragments(cellule), self.marge if self.mobile else self.marge + i * largeur,
                          self.largeur - 2 * self.marge if self.mobile else largeur - 12)
                fins.append(self.y)
            self.y = max(fins, default=depart) + 8
            self.ligne(self.y)
            self.y += 12
        elif noeud.tag in {"p", "h2", "h3", "li"}:
            if noeud.tag in {"h2", "h3"}:
                self.y += 5
            self.flux(fragments(noeud), taille=20 if noeud.tag in {"h2", "h3"} else None)
            self.y += 8
        else:
            for enfant in noeud.enfants:
                self.bloc(enfant)

    def svg(self, arbre):
        self.bloc(arbre)
        attendu = normaliser(texte(arbre))
        if re.sub(r"\s", "", "".join(self.contenu)) != re.sub(r"\s", "", attendu):
            raise ValueError("Le dessin ne restitue pas tout le texte de la fenêtre")
        hauteur = round(self.y + self.marge)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.largeur}" height="{hauteur}" '
                f'viewBox="0 0 {self.largeur} {hauteur}" font-family="Arial, sans-serif">\n'
                f'<rect x="4" y="7" width="{self.largeur - 8}" height="{hauteur - 10}" rx="14" fill="#483615" opacity="0.08"/>\n'
                f'<rect x="1" y="1" width="{self.largeur - 6}" height="{hauteur - 7}" rx="14" fill="#FFFFFF" stroke="#D1AB61"/>\n'
                + "\n".join(self.elements) + "\n</svg>\n")


def produire(source):
    original = extraire_source_fenetres(source)
    fenetres = Reperes(original).fenetres
    if not fenetres:
        raise ValueError("Aucune fenêtre .lit-window trouvée")
    images = {}
    resultat = original
    for f in reversed(fenetres):
        corps = original[f.ouverture:f.fermeture]
        arbre = Arbre(corps).racine
        titre = next((normaliser(texte(e)) for e in arbre.enfants
                      if isinstance(e, Noeud) and "lit-window__header" in e.classes), "Système")
        for suffixe, largeur in (("", 680), ("-mobile", 320)):
            nom = f"{f.identifiant}{suffixe}.svg"
            if nom in images:
                raise ValueError(f"Collision de noms SVG : {nom}")
            images[nom] = Dessin(largeur).svg(arbre)
        enveloppe = (
            f'\n  <picture class="{PICTURE_CLASS}">\n'
            f'    <source media="(max-width: 600px)" srcset="assets/fenetres/{f.identifiant}-mobile.svg">\n'
            f'    <img src="assets/fenetres/{f.identifiant}.svg" alt="{escape("Fenêtre du système — " + titre, quote=True)}">\n'
            f'  </picture>\n  <details class="{TRANSCRIPT_CLASS}">\n'
            f'    <summary class="{TOGGLE_CLASS}">{TOGGLE_TEXT}</summary>'
            + corps + '  </details>\n')
        resultat = resultat[:f.ouverture] + enveloppe + resultat[f.fermeture:]
    if extraire_source_fenetres(resultat) != original:
        raise ValueError("La transformation a altéré la source")
    return resultat, images


def ecrire_atomique(chemin, contenu):
    """Remplace un fichier complet, sans tronquer sa version précédente."""
    mode = stat.S_IMODE(chemin.stat().st_mode) if chemin.exists() else 0o644
    temporaire = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=chemin.parent,
                                         prefix=f".{chemin.name}.", suffix=".tmp", delete=False) as flux:
            temporaire = Path(flux.name)
            flux.write(contenu)
            flux.flush()
            os.fsync(flux.fileno())
        temporaire.chmod(mode)
        os.replace(temporaire, chemin)
    finally:
        if temporaire is not None:
            temporaire.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="vérifie les enveloppes et SVG sans écrire ; code 1 si périmés, 2 si erreur")
    args = parser.parse_args(argv)
    try:
        manuscrit = ROOT / "livre_1_l_ascension_d_une_legende_oubliee.md"
        source = manuscrit.read_text(encoding="utf-8")
        resultat, images = produire(source)
        dossier = ROOT / "assets/fenetres"
        presents = {p.name for p in dossier.glob("*.svg")}
        obsoletes = presents - images.keys()
        if obsoletes:
            raise ValueError("SVG obsolètes à examiner et retirer explicitement : " + ", ".join(sorted(obsoletes)))
        perimes = [nom for nom, contenu in images.items()
                   if not (dossier / nom).exists()
                   or (dossier / nom).read_text(encoding="utf-8") != contenu]
        if args.check:
            if resultat != source or perimes:
                print(f"À régénérer : manuscrit={resultat != source}, SVG={len(perimes)}", file=sys.stderr)
                return 1
        else:
            dossier.mkdir(parents=True, exist_ok=True)
            for nom in perimes:
                ecrire_atomique(dossier / nom, images[nom])
            if resultat != source:
                ecrire_atomique(manuscrit, resultat)
        print(f"{len(images) // 2} fenêtres, {len(images)} SVG : " + ("à jour" if args.check else "générés"))
        return 0
    except (ValueError, OSError, ImportError) as erreur:
        print(f"Erreur : {erreur}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
