"""Outils de contrôle indépendants du générateur de lecture."""

from collections import Counter
import base64
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import zlib


ROOT_CLASSES = {"system-window", "character-sheet", "rune-window"}
HEADER_DECORATIONS = "✦◆✓"
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def digest(text):
    return sha256(text.encode("utf-8")).hexdigest()


def compact(text):
    return " ".join(text.split())


def visual_text(node):
    """Texte dessiné ; le complément de rareté reste contrôlé séparément en transcription."""
    if node.tag == "svg" or "lit-sr-only" in node.classes:
        return ""
    if node.tag == "summary" and "lit-window__transcript-toggle" in node.classes:
        return ""
    return "".join(visual_text(part) if isinstance(part, Node) else part for part in node.content)


class Node:
    def __init__(self, tag, attrs, parent=None):
        self.tag = tag
        self.attrs = dict(attrs)
        self.parent = parent
        self.children = []
        self.content = []
        self.start = self.end = None

    @property
    def classes(self):
        return set(self.attrs.get("class", "").split())

    def descendants(self, tag=None):
        for child in self.children:
            if tag is None or child.tag == tag:
                yield child
            yield from child.descendants(tag)

    def text(self, normalize_header=False):
        if self.tag == "svg":
            return ""
        if self.tag == "summary" and "lit-window__transcript-toggle" in self.classes:
            return ""
        header = normalize_header or "system-header" in self.classes
        pieces = []
        for part in self.content:
            if isinstance(part, Node):
                pieces.append(part.text(header))
            else:
                pieces.append(part.translate(str.maketrans("", "", HEADER_DECORATIONS)) if header else part)
        return "".join(pieces)


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.line_offsets = [0]
        for match in re.finditer("\n", source):
            self.line_offsets.append(match.end())
        self.root = Node("document", [])
        self.stack = [self.root]
        self.windows = []
        self.feed(source)
        self.close()
        if any(node.classes & ROOT_CLASSES for node in self.stack):
            raise ValueError("Fenêtre HTML non fermée")

    def source_offset(self):
        line, col = self.getpos()
        return self.line_offsets[line - 1] + col

    def handle_starttag(self, tag, attrs):
        parent = self.stack[-1]
        node = Node(tag, attrs, parent)
        node.start = self.source_offset()
        parent.children.append(node)
        parent.content.append(node)
        if node.classes & ROOT_CLASSES:
            if any(item.classes & ROOT_CLASSES for item in self.stack):
                raise ValueError("Fenêtre racine imbriquée")
            self.windows.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)
        else:
            node.end = node.start + len(self.get_starttag_text())

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.stack.pop().end = self.source_offset() + len(self.get_starttag_text())

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                node = self.stack[index]
                node.end = self.source.index(">", self.source_offset()) + 1
                del self.stack[index:]
                return

    def handle_data(self, data):
        self.stack[-1].content.append(data)

    def outside_windows(self):
        return "".join(self.outside_segments())

    def outside_segments(self):
        pieces, previous = [], 0
        for node in self.windows:
            if node.end is None:
                raise ValueError("Fenêtre HTML sans fermeture")
            pieces.append(self.source[previous:node.start])
            previous = node.end
        pieces.append(self.source[previous:])
        return pieces


def semantic_classes(node):
    counts = Counter()
    for item in [node, *node.descendants()]:
        counts.update(item.classes & {
            *ROOT_CLASSES, "system-header", "rune-bonus", "temporary-bonus",
            "upgrade-badge", "passive-badge", "legendary-text", "success-text",
        })
    return dict(sorted(counts.items()))


def manifest(source):
    document = Document(source)
    chapter_positions = list(re.finditer(r"^# Chapitre (\d+)\b", source, re.M))
    counts = {match[1]: 0 for match in chapter_positions}
    for window in document.windows:
        previous = [match for match in chapter_positions if match.start() < window.start]
        if not previous:
            raise ValueError("Fenêtre sans chapitre de rattachement")
        counts[previous[-1][1]] += 1
    return {
        "source_sha256": digest(source),
        "outside_windows_sha256": digest(document.outside_windows()),
        "outside_segments_sha256_base64": base64.b64encode(b"".join(
            bytes.fromhex(digest(segment)) for segment in document.outside_segments()
        )).decode("ascii"),
        "chapters": re.findall(r"^# (Chapitre \d+[^\n]*)$", source, re.M),
        "chapter_window_counts": counts,
        "table_count": len(table_cells(document)),
        "window_text_sha256": [digest(compact(node.text())) for node in document.windows],
        "window_ids_before": [node.attrs.get("data-window-id") for node in document.windows],
        "window_classes_sha256": digest(json.dumps(
            [semantic_classes(node) for node in document.windows], sort_keys=True,
        )),
        "bonus_associations_sha256": digest(json.dumps([
            [(sorted(node.classes & {"rune-bonus", "temporary-bonus", "success-text"}), compact(node.text()))
             for node in window.descendants()
             if node.classes & {"rune-bonus", "temporary-bonus", "success-text"}]
            for window in document.windows
        ], ensure_ascii=False)),
        "tables_sha256": digest(json.dumps(table_cells(document), ensure_ascii=False)),
    }


def historical_prefix(source, reference):
    """Retrouver la fin exacte de la baseline sans absorber ni rogner sa dernière narration."""
    source = before_approved_rune_corrections(source)
    source = without_added_contents(source, reference)
    source = before_approved_description_corrections(source)
    source = before_approved_oeil_corrections(source)
    document = Document(source)
    count = len(reference["window_text_sha256"])
    if len(document.windows) < count:
        raise ValueError("Fenêtres historiques manquantes")
    packed = base64.b64decode(reference["outside_segments_sha256_base64"], validate=True)
    if len(packed) != (count + 1) * 32:
        raise ValueError("Manifeste des segments historiques invalide")
    start = document.windows[count - 1].end
    stop = document.windows[count].start if len(document.windows) > count else len(source)
    checksum = sha256()
    for end in range(start, stop + 1):
        if checksum.digest() == packed[-32:]:
            suffix = source[end:]
            if suffix:
                chapter = re.match(
                    r'\s*(?:---\s*)?(?:<span id="chapitre-(?P<anchor>\d+)"></span>\s*)?'
                    r'# Chapitre (?P<number>\d+)\b', suffix,
                )
                if (not chapter
                        or int(chapter["number"]) <= max(map(int, reference["chapter_window_counts"]))
                        or (chapter["anchor"] is not None and chapter["anchor"] != chapter["number"])):
                    raise ValueError("Ajout hors d'un nouveau chapitre après la baseline")
            return source[:end]
        if end < stop:
            checksum.update(source[end].encode("utf-8"))
    raise ValueError("Dernier segment narratif historique altéré ou tronqué")


def before_approved_rune_corrections(source):
    """Inverser les deux journaux DEC-179 du I, sans exemption de contenu."""
    source = before_bubble_presentation(source)
    source = before_invisible_rune_ids_and_dec181(source)
    fixtures = Path(__file__).parent / "fixtures"
    stages = [json.loads((fixtures / name).read_text(encoding="utf-8")) for name in (
        "corrections_runes_livre1_dec179.json",
        "corrections_runes_livre1_dec179_complements.json",
    )]
    added = [identifier for stage in stages for identifier in stage["windows_added"]]
    # Les petits documents synthétiques et les sources déjà restaurées restent intacts.
    if not any(f'data-window-id="{identifier}"' in source for identifier in added):
        return source
    for stage in reversed(stages):
        if digest(source) != stage["result_sha256"]:
            raise ValueError("Source DEC-179 altérée avant inversion")
        for pair in reversed(stage["pairs"]):
            start, end = pair["after_start_char"], pair["after_end_char"]
            if source[start:end] != pair["after"]:
                raise ValueError(f"Bloc DEC-179 altéré ou déplacé : caractère {start}")
            source = source[:start] + pair["before"] + source[end:]
        if digest(source) != stage["baseline_sha256"]:
            raise ValueError("Baseline DEC-179 non restaurée exactement")
    return source


def historical_book_ii(source):
    """Isoler les 1–3 intacts ; seules les quatre entrées de sommaire sont retirées.

    Longueur issue de livre-II-avant.md, identique à HEAD avant intégration.
    L'empreinte existante du journal de bulles reste la preuve, sans nouvelle baseline.
    """
    boundary = re.search(r'\n---\n\n<span id="chapitre-4"></span>\n\n## Chapitre 4 — ', source)
    if boundary is None:
        return source
    prefix = source[:boundary.start()]
    for number in range(4, 8):
        title = re.search(rf'^## (Chapitre {number} — [^\n]+)$', source, re.M)
        if title is None:
            raise ValueError("Extension II incomplète")
        link = f'{number}. [{title[1]}](#chapitre-{number})\n'
        if prefix.count(link) != 1:
            raise ValueError("Entrée de sommaire ajoutée absente ou dupliquée")
        prefix = prefix.replace(link, '', 1)
    if len(prefix) != 250472:
        raise ValueError("Borne historique II altérée")
    stage = json.loads((Path(__file__).parent / "fixtures" /
                        "bulles_20261127_inverse.json").read_text(encoding="utf-8"))["2"]
    if digest(prefix) != stage["after_sha256"]:
        raise ValueError("Chapitres 1–3 ou sommaire historique II altérés")
    return prefix


def before_bubble_presentation(source, book=1):
    """Inversion fermée pour appliquer les anciennes preuves, jamais pour le rendu courant."""
    if "data-rarity=" not in source:
        return source
    stages = json.loads((Path(__file__).parent / "fixtures" /
                         "bulles_20261127_inverse.json").read_text(encoding="utf-8"))
    stage = stages[str(book)]
    if digest(source) != stage["after_sha256"]:
        raise ValueError("Présentation du 27 novembre altérée avant inversion")
    edits = json.loads(zlib.decompress(base64.b64decode(
        stage["reverse_edits_zlib_base64"], validate=True)).decode("utf-8"))
    if len(edits) != stage["replacement_count"]:
        raise ValueError("Journal inverse incomplet")
    last = len(source)
    for start, end, before in reversed(edits):
        if not 0 <= start <= end <= last:
            raise ValueError("Éditions inverses désordonnées")
        source = source[:start] + before + source[end:]
        last = start
    if digest(source) != stage["before_sha256"]:
        raise ValueError("Baseline avant bulles non restaurée exactement")
    return source


def before_invisible_rune_ids_and_dec181(source):
    """Restaurer les formes pré-DEC-181 avant d'appliquer les journaux historiques.

    Cette inversion est volontairement fermée : elle ne normalise que l'insécabilité,
    le déplacement des identifiants vers ``data-rune-id`` et les corrections métier
    explicitement autorisées sur le livre I.
    """
    source = before_bubble_presentation(source)
    source = source.replace("&nbsp;", " ")
    source = re.sub(
        r'<tr data-rune-id="([^"]+)"><th scope="row">',
        r'<tr><th scope="row">\1 · ', source,
    )
    source = re.sub(
        r'<h3 data-rune-id="([^"]+)">',
        r'<h3>\1 — ', source,
    )

    def restore_paragraph(match):
        identifier, body = match.groups()
        strong = re.match(r"<strong>([^<]+)</strong>(.*)", body, re.S)
        if strong:
            return f"<p><strong>{identifier} — {strong[1]}</strong>{strong[2]}</p>"
        return f"<p><strong>{identifier} :</strong> {body}</p>"

    source = re.sub(
        r'<p data-rune-id="([^"]+)">(.*?)</p>', restore_paragraph, source,
    )

    approved = (
        ("L’Éclaireuse", "La Ranger"),
        ("l’Éclaireuse", "la Ranger"),
        ("Éclaireuse", "Ranger"),
        ("Tempête runique", "Tempête arcanique"),
        (
            "  <p>Dégâts : <strong>120 % de la Puissance arcanique</strong>.</p>\n"
            "  <p>Mana récupéré : <strong>75 % des dégâts infligés</strong>, dans la limite de <strong>1 200 Mana</strong>.</p>\n"
            "  <p>Rayon : <strong>8 mètres</strong>.</p>\n"
            "  <p>Coût : <strong>100 Mana</strong>.</p>\n"
            "  <p>Temps de recharge : <strong>20 secondes</strong>.</p>",
            "  <p>Déploie une tempête de Vent imprégnée d&#x27;inscriptions runiques. Les ennemis atteints subissent des dégâts magiques déterminés par la Puissance arcanique effective du lanceur.</p>\n"
            "  <p>Le sort absorbe une partie du Mana disponible chez les cibles touchées et le transfère au lanceur, dans la limite de sa réserve maximale et de la capacité d&#x27;absorption de la compétence.</p>\n"
            "  <p>Temps de recharge</p>\n  <p>Oui</p>",
        ),
        (
            "Hasol sentit aussitôt du Mana affluer dans ses cercles, restitué en proportion des dégâts qu'elle venait d'infliger.",
            "Hasol sentit aussitôt quelque chose revenir vers elle.\n\nUn courant invisible.\n\nUne énergie qui ne provenait pas de ses propres réserves.\n\nLe Mana des démons.\n\nIl afflua dans ses cercles.",
        ),
        (
            "La compétence lui avait rendu du Mana, sans dépasser son plafond propre.",
            "Une partie de ce qu'elle venait de dépenser lui avait été restituée.",
        ),
    )
    for after, before in approved:
        source = source.replace(after, before)
    return source


# Corrections éditoriales DEC-104/106/107, déjà présentes avant l'import final.
# Les phrases exactes sont réversibles pour conserver les anciennes empreintes.
APPROVED_DESCRIPTIONS = (
    ("Son père leva les yeux du registre commercial qu’il consultait.",
     "Son père leva les yeux du registre commercial qu’il consultait. Quelques mèches brunes se soulevaient au-dessus de son front, adoucissant les traits nets de son visage. Il portait une veste sombre à col haut, bordée de fins galons dorés, dont il avait défait une attache pour lire à son aise."),
    ("Sa mère sourit.",
     "Sa mère sourit. Ses longs cheveux rose pâle glissèrent sur son épaule lorsqu’elle se pencha vers Hasol. Les broderies dorées de sa robe claire dessinaient de fines arabesques le long des manches ; la coupe elfique et le tombé impeccable du tissu lui donnaient cette élégance que sa fille lui avait toujours connue."),
    ("La clochette tinta. Une voix leur demanda d’attendre, puis un homme aux cheveux grisonnants sortit de l’arrière-boutique en s’essuyant les doigts. Il accueillit la mère de Hasol avec un sourire et contourna son comptoir.",
     "La clochette tinta. Une voix leur demanda d’attendre, puis un homme aux cheveux grisonnants sortit de l’arrière-boutique en s’essuyant les doigts. Une barbe encadrait son visage, et il releva les yeux derrière ses lunettes pour accueillir la mère de Hasol avec un sourire, avant de contourner son comptoir."),
    ("Ses cheveux sombres étaient soigneusement attachés, et sa silhouette élancée ne semblait nullement gênée par le poids de son équipement.",
     "Ses cheveux bruns, coupés court, encadraient son visage, et sa silhouette élancée ne semblait nullement gênée par le poids de son équipement."),
    ("Le soir, en rentrant chez elle, Hasol retrouva sa mère dans le petit salon.",
     "Le soir, en rentrant chez elle, Hasol retrouva sa mère dans le salon."),
    ("Le lendemain matin, Hasol descendit au petit salon familial avec son carnet sous le bras.",
     "Le lendemain matin, Hasol descendit au salon familial avec son carnet sous le bras."),
    ("Iseria se trouvait dans le petit salon lorsque Hasol rentra.",
     "Iseria se trouvait dans le salon lorsque Hasol rentra."),
    ("Elle savait seulement qu’elle se trouvait maintenant dans le petit salon.",
     "Elle savait seulement qu’elle se trouvait maintenant dans le salon."),
    ("Les regards qu’elle adressait parfois au fauteuil vide du petit salon.",
     "Les regards qu’elle adressait parfois au fauteuil vide du salon."),
    ("En rentrant, Hasol trouva Iseria dans le petit salon.",
     "En rentrant, Hasol trouva Iseria dans le salon."),
    ("Iseria se trouvait dans le petit salon.", "Iseria se trouvait dans le salon."),
)


def before_approved_description_corrections(source):
    end = re.search(r"^# Chapitre 13\b", source, re.M)
    prefix, suffix = (source[:end.start()], source[end.start():]) if end else (source, "")
    for before, after in APPROVED_DESCRIPTIONS:
        prefix = prefix.replace(after, before)
    return prefix + suffix


# DEC-168 : uniquement les deux paragraphes de 095 et la réplique d'Orven.
APPROVED_OEIL_CORRECTIONS = (
    ("  <p>Révèle le résultat final exact d'une rune à +15, à condition que l'hôte réalise personnellement les améliorations restantes.</p>\n"
     "  <p>Permet de connaître les caractéristiques secondaires obtenues, les renforcements qui leur seront attribués et leurs valeurs finales.</p>",
     "  <p>Révèle les caractéristiques secondaires qui seront découvertes lors de l'amélioration d'une rune. Leur nature est prédéterminée et reste identique quel que soit l'artisan.</p>\n"
     "  <p>Si l'hôte réalise personnellement les améliorations restantes jusqu'à +15 et atteint ce palier, révèle également les renforcements attribués et leurs valeurs finales exactes.</p>"),
    ("— Ta compétence décrit ce qui se produira lorsque tu réaliseras personnellement les améliorations. Si je le fais à ta place, nous risquons de ne pas tester la bonne chose.",
     "— La nature de la secondaire annoncée resterait la même si je l'améliorais. Mais les valeurs finales exactes que ton Œil révèle à +15 concernent tes propres améliorations. Commençons donc par vérifier ta prédiction entre tes mains."),
)


def before_approved_oeil_corrections(source):
    """Inverser les seuls textes exacts de DEC-168, dans le chapitre 10 uniquement."""
    chapter = re.search(r"^# Chapitre 10\b[^\n]*\n", source, re.M)
    if chapter is None:
        return source
    following = re.search(r"^# (?:Chapitre \d+\b|Épilogue\b)", source[chapter.end():], re.M)
    end = chapter.end() + following.start() if following else len(source)
    body = source[chapter.end():end]
    for before, after in APPROVED_OEIL_CORRECTIONS:
        if body.count(after) == 1:
            body = body.replace(after, before, 1)
    return source[:chapter.end()] + body + source[end:]


def without_added_contents(source, reference):
    """Exclure uniquement les liens du sommaire correspondant aux nouveaux titres."""
    first = re.search(r"^# Chapitre \d+\b", source, re.M)
    if first is None:
        return source
    last = max(map(int, reference["chapter_window_counts"]))
    prefix, body = source[:first.start()], source[first.start():]
    titles = re.findall(r"^# (Chapitre (\d+)[^\n]*)$", body, re.M)
    added = {f"{number}. [{title}](#chapitre-{number})"
             for title, number in titles if int(number) > last}
    epilogue = re.search(r"^# (Épilogue[^\n]*)$", body, re.M)
    if epilogue:
        for link in ("[Épilogue](#epilogue)", f"[{epilogue[1]}](#epilogue)",
                     f"- [{epilogue[1]}](#epilogue)"):
            prefix = prefix.replace("\n\n" + link + "\n", "\n")
    return "".join(line for line in prefix.splitlines(keepends=True)
                   if line.rstrip("\r\n") not in added) + body


def table_cells(document):
    return [
        [[(cell.tag, compact(cell.text())) for cell in row.children if cell.tag in {"th", "td"}]
         for row in table.descendants("tr")]
        for table in document.root.descendants("table")
    ]


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Calculer un manifeste depuis une baseline éditoriale explicitement choisie, sans modifier la fixture.",
    )
    parser.add_argument("--baseline", type=Path, required=True,
                        help="Source UTF-8 approuvée à analyser ; aucun chemin implicite.")
    args = parser.parse_args()
    print(json.dumps(manifest(args.baseline.read_bytes().decode("utf-8")), ensure_ascii=False, indent=2))
