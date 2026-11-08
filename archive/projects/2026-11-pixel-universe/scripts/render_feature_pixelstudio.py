"""Render the Pixel Universe article feature from an actual Pixel Art Studio 16x16 code.

Source of truth: data/feature_pixelstudio_16x16.txt (256 hex characters).
Colour mapping: site/assets/js/pixel-art-builder.js; do not invent new paint inks.

Run from the repository root:
    python archive/projects/2026-11-pixel-universe/scripts/render_feature_pixelstudio.py
    python archive/projects/2026-11-pixel-universe/scripts/render_feature_pixelstudio.py --check

Each visible square is precisely 70x70 px on the same 76 px grid; there
are no non-square marks, unequal tiles, traced assets, or extra colours.
Blank Studio cells are the light-grey feature paper rather than painted
white cells. This is original editorial art, not the 12-character dataset.
"""
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / "archive/projects/2026-11-pixel-universe"
SOURCE = PROJECT / "data/feature_pixelstudio_16x16.txt"
PALETTE_SOURCE = ROOT / "site/assets/js/pixel-art-builder.js"
DEST = ROOT / "site/assets/pixel-universe/feature-pixel-identity.svg"

CANVAS = 1600
N = 16
ORIGIN = 192
STEP = 76
TILE = 70
PAPER = "#F3F4F6"
ALLOWED_INDICES = {0, 1, 4, 6}  # Studio White, Black, Slate, Red
ALT = (
    "An anonymous black and slate pixel mask built from equal-sized squares, "
    "with a few red accents and individual pixels scattered around all sides"
)


def studio_palette():
    source = PALETTE_SOURCE.read_text(encoding="utf-8")
    array = source.split("  const colours = [", 1)[1].split("  ];", 1)[0]
    entries = re.findall(r'\{ name: "([^"]+)", hex: "(#[0-9a-f]{6})" \}', array)
    assert len(entries) == 16, "Expected Pixel Art Studio 16-colour palette"
    assert entries[0][0] == "White"
    assert entries[1][0] == "Black"
    assert entries[4][0] == "Slate"
    assert entries[6][0] == "Red"
    return [colour for _, colour in entries]


def load_code():
    code = SOURCE.read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"[0-9a-f]{256}", code), "Must be one genuine 16x16 Studio code"
    assert {int(digit, 16) for digit in code} == ALLOWED_INDICES
    # Balanced detached particles near each edge of a 16x16 canvas.
    for points in (
        [(x, 0) for x in range(16)],
        [(x, 15) for x in range(16)],
        [(0, y) for y in range(16)],
        [(15, y) for y in range(16)],
    ):
        assert any(code[y * 16 + x] != "0" for x, y in points), "Missing halo on a side"
    assert 0 < code.count("6") <= 12, "Red accent should stay restrained"
    return code


def svg(code, palette):
    rows = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS}" height="{CANVAS}" '
        f'viewBox="0 0 {CANVAS} {CANVAS}" role="img" aria-label="{escape(ALT)}">',
        f'<rect width="{CANVAS}" height="{CANVAS}" fill="{PAPER}"/>',
        '<g shape-rendering="crispEdges">',
    ]
    for index, digit in enumerate(code):
        colour = int(digit, 16)
        if colour == 0:
            continue
        x = ORIGIN + (index % 16) * STEP
        y = ORIGIN + (index // 16) * STEP
        rows.append(
            f'<rect x="{x}" y="{y}" width="{TILE}" height="{TILE}" '
            f'fill="{palette[colour]}"/>'
        )
    rows.extend(["</g>", "</svg>", ""])
    return "\n".join(rows)


def main():
    assert sys.argv[1:] in ([], ["--check"]), "Usage: render_feature_pixelstudio.py [--check]"
    generated = svg(load_code(), studio_palette())
    if sys.argv[1:] == ["--check"]:
        assert DEST.exists() and DEST.read_text(encoding="utf-8") == generated, (
            "Pixel Studio feature is not source-identical; regenerate before publishing"
        )
        print("Verified exact 16x16 Studio code, uniform tile geometry, colour mapping and SVG")
    else:
        DEST.parent.mkdir(parents=True, exist_ok=True)
        DEST.write_text(generated, encoding="utf-8")
        print("Rendered", DEST)


if __name__ == "__main__":
    main()
