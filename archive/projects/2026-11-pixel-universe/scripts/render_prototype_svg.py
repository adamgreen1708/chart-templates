"""Rebuild reviewed Pixel Universe prototype SVGs from the source-backed pixel CSV.

Run from repository root:
    python archive/projects/2026-11-pixel-universe/scripts/render_prototype_svg.py

Uses only stdlib. Produces source-faithful 400px square SVG previews with a
light-grey border and original one-character-per-pixel HEX codes.
"""
import csv
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / "archive/projects/2026-11-pixel-universe"
SEED = ROOT / "archive/projects/2026-11-superhero-colour-code/data/character_palette_seed.csv"
SRC = PROJECT / "data/pixel_universe_prototypes.csv"
BUILDER = ROOT / "site/assets/js/pixel-art-builder.js"
DEST = PROJECT / "output/prototypes"


def palette():
    js = BUILDER.read_text(encoding="utf-8")
    part = js.split("  const colours = [", 1)[1].split("  ];", 1)[0]
    entries = re.findall(r'\{ name: "([^"]+)", hex: "(#[0-9a-f]{6})" \}', part)
    assert len(entries) == 16, "Pixel Art Studio 16-slot palette required"
    return {name.lower(): (n, colour) for n, (name, colour) in enumerate(entries)}


def records(path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def svg_from_code(code, colours, label):
    assert re.fullmatch(r"[0-9a-f]{256}", code)
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" '
        'viewBox="0 0 400 400" role="img" aria-label="' + escape(label) + '">',
        '<rect width="400" height="400" fill="#F3F4F6"/>',
        '<rect x="40" y="40" width="320" height="320" fill="#ffffff"/>',
        '<g shape-rendering="crispEdges">',
    ]
    for idx, digit in enumerate(code):
        colour_index = int(digit, 16)
        if colour_index == 0:
            continue
        hexcode = colours[colour_index]
        x, y = idx % 16, idx // 16
        parts.append(
            f'<rect x="{40+x*20}" y="{40+y*20}" '
            f'width="20" height="20" fill="{hexcode}"/>'
        )
    parts.extend(["</g>", "</svg>", ""])
    return "\n".join(parts)


def main():
    pal = palette()
    colours = [None] * 16
    for _, (index, colour) in pal.items():
        colours[index] = colour
    assert all(colours)
    source = {row["character"]: row for row in records(SEED)}
    prototypes = records(SRC)
    assert len(prototypes) == 2
    assert set(p["character"] for p in prototypes) == {"Superman", "The Joker"}
    DEST.mkdir(parents=True, exist_ok=True)
    for p in prototypes:
        s = source[p["character"]]
        for a, b in [
            ("publisher", "publisher"),
            ("role", "role"),
            ("costume_version", "costume_version"),
            ("dominant_colour", "dominant_colour"),
            ("second_major_colour", "second_major_colour"),
            ("accent_colours", "accent_colours"),
        ]:
            assert p[a] == s[b], f"{p['character']} field mismatch: {a}"
        assert p["grid_size"] == "16"
        assert p["review_status"] == "creative_prototype_review_only"
        used = set(p["pixel_code"])
        for source_colour in [p["dominant_colour"], p["second_major_colour"], p["accent_colours"]]:
            if source_colour:
                assert format(pal[source_colour][0], "x") in used
        image = svg_from_code(p["pixel_code"], colours, p["character"] + " original 16 by 16 pixel art prototype")
        filename = p["slug"] + ".svg"
        (DEST / filename).write_text(image, encoding="utf-8")
        print("Created", DEST / filename)


if __name__ == "__main__":
    main()
