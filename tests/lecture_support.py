"""Outils de contrôle indépendants du générateur de lecture."""

from collections import Counter
import base64
from hashlib import sha256
from html.parser import HTMLParser
import json
import re


ROOT_CLASSES = {"system-window", "character-sheet", "rune-window"}
HEADER_DECORATIONS = "✦◆✓"
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def digest(text):
    return sha256(text.encode("utf-8")).hexdigest()


def compact(text):
    return " ".join(text.split())


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
