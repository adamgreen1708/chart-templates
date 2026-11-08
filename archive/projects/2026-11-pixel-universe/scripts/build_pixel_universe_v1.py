"""Generate deterministic 16x16 Pixel Universe icon and two mosaic SVG exports.

Run from repository root:
    python archive/projects/2026-11-pixel-universe/scripts/build_pixel_universe_v1.py

Only standard-library dependencies. Source colour fields join to the existing
published 24-character superhero seed, never invented measurement data.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / "archive/projects/2026-11-pixel-universe"
SEED = ROOT / "archive/projects/2026-11-superhero-colour-code/data/character_palette_seed.csv"
CODES = PROJECT / "data/pixel_universe_art_v1.csv"
BUILDER = ROOT / "site/assets/js/pixel-art-builder.js"
OUT = PROJECT / "output/v1"

ORDER = (
    "Superman", "Batman (Bruce Wayne)", "Wonder Woman (Diana)",
    "The Flash (Barry Allen)", "Spider-Man (Peter Parker)", "Wolverine (Logan)",
    "The Joker", "Riddler (Edward Nygma)", "Lex Luthor",
    "Green Goblin (Norman Osborn)", "Magneto (Max Eisenhardt)",
    "Venom (Eddie Brock)"
)


def records(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def studio_palette():
    code = BUILDER.read_text(encoding="utf-8")
    area = code.split("  const colours = [", 1)[1].split("  ];", 1)[0]
    named = re.findall(r'\{ name: "([^"]+)", hex: "(#[0-9a-f]{6})" \}', area)
    assert len(named) == 16, "Requires merged PR #197 palette"
    return {name.lower(): (i, hx) for i, (name, hx) in enumerate(named)}


def validate():
    seed = {x["character"]: x for x in records(SEED)}
    sprites = records(CODES)
    assert len(sprites) == 12
    assert tuple(x["character"] for x in sprites) == ORDER
    pal = studio_palette()
    synonyms = {"grey": "slate"}
    for idx, sprite in enumerate(sprites):
        source = seed[sprite["character"]]
        assert source["role"] == ("Hero" if idx < 6 else "Villain")
        assert re.fullmatch(r"[0-9a-f]{256}", sprite["pixel_code"])
        assert sprite["slug"] and sprite["artistic_note"]
        for c in [source["dominant_colour"], source["second_major_colour"],
                  *source["accent_colours"].split(";")]:
            if c:
                name = synonyms.get(c, c)
                assert name in pal, (sprite["character"], c)
                assert format(pal[name][0], "x") in sprite["pixel_code"], (
                    "Artwork omits source-labelled costume colour", sprite["character"], c
                )
    return sprites, pal


def cell_rectangles(code, colours, start_x, start_y, step):
    shapes = []
    for i, digit in enumerate(code):
        idx = int(digit, 16)
        if idx == 0:
            continue
        px = start_x + (i % 16) * step
        py = start_y + (i // 16) * step
        shapes.append(f'<rect x="{px}" y="{py}" width="{step}" height="{step}" fill="{colours[idx]}"/>')
    return shapes


def icon_svg(row, colours):
    name = row["character"].replace("&", "&amp;")
    return "\n".join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400" role="img" aria-label="{name} original 16 by 16 pixel portrait">',
        '<rect width="400" height="400" fill="#F3F4F6"/>',
        '<rect x="40" y="40" width="320" height="320" fill="#ffffff"/>',
        '<g shape-rendering="crispEdges">',
        *cell_rectangles(row["pixel_code"], colours, 40, 40, 20),
        '</g>', '</svg>', ''
    ])


def mosaic_svg(title, entries, colours):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200" role="img" aria-label="Pixel Universe: {title.lower()} colour-portrait mosaic">',
        '<rect width="1200" height="1200" fill="#F3F4F6"/>',
        '<text x="87" y="108" font-family="Space Grotesk, sans-serif" font-size="53" font-weight="700" fill="#111111">PIXEL UNIVERSE</text>',
        f'<text x="87" y="172" font-family="IBM Plex Sans, sans-serif" font-size="34" fill="#454545">{title}</text>',
        '<g shape-rendering="crispEdges">'
    ]
    for j, row in enumerate(entries):
        tx, ty = 87 + (j % 3) * 332, 250 + (j // 3) * 366
        lines.append(f'<rect x="{tx}" y="{ty}" width="300" height="300" fill="#ffffff"/>')
        lines.extend(cell_rectangles(row["pixel_code"], colours, tx+6, ty+6, 18))
    lines.append('</g>')
    for j, row in enumerate(entries):
        tx, ty = 87 + (j % 3) * 332, 250 + (j // 3) * 366
        label = re.sub(r" \([^)]*\)", "", row["character"])
        if label == "The Joker":
            label = "Joker"
        lines.append(f'<text x="{tx}" y="{ty+338}" font-family="IBM Plex Sans, sans-serif" font-size="30" fill="#111111">{label}</text>')
    lines.extend([
        '<line x1="87" y1="1080" x2="1113" y2="1080" stroke="#CDD0D3" stroke-width="2"/>',
        '<text x="87" y="1125" font-family="IBM Plex Sans, sans-serif" font-size="22" fill="#555555">Original pixel portraits from qualitative costume colours</text>',
        '</svg>', ''
    ])
    return "\n".join(lines)


def main():
    sprites, pal = validate()
    indexed = [None] * 16
    for _, (i, color) in pal.items():
        indexed[i] = color
    assert all(indexed)
    (OUT / "icons").mkdir(parents=True, exist_ok=True)
    for row in sprites:
        (OUT / "icons" / (row["slug"]+".svg")).write_text(icon_svg(row,indexed),encoding="utf-8")
    (OUT / "hero_mosaic.svg").write_text(mosaic_svg("The heroes",sprites[:6],indexed),encoding="utf-8")
    (OUT / "villain_mosaic.svg").write_text(mosaic_svg("The villains",sprites[6:],indexed),encoding="utf-8")
    print("Generated 12 editable icon previews and 2 square mosaics from source-backed codes")


if __name__ == "__main__":
    main()
