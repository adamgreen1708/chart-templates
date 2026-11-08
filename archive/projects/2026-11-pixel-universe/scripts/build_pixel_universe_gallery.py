"""Build Pixel Universe Jekyll gallery data and source-faithful SVG artwork.

Run from repo root:
  python archive/projects/2026-11-pixel-universe/scripts/build_pixel_universe_gallery.py
  python archive/projects/2026-11-pixel-universe/scripts/build_pixel_universe_gallery.py --check

The archived 12 exact 16x16 pixel codes and the published 24-character
superhero seed are canonical. Artist-added pixels are NOT measured costume areas.
No dependency except the Python standard library.
"""
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / "archive/projects/2026-11-pixel-universe"
PUBLISHED = ROOT / "archive/projects/2026-11-superhero-colour-code"
STUDIO = ROOT / "site/assets/js/pixel-art-builder.js"
OUT = ROOT / "site/assets/pixel-universe"
YAML = ROOT / "site/_data/pixel_universe.yml"


def rows(path):
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def short_name(name):
    label = re.sub(r" \([^)]*\)", "", name)
    return "Joker" if label == "The Joker" else label


def palette():
    js = STUDIO.read_text(encoding="utf-8")
    body = js.split("  const colours = [", 1)[1].split("  ];", 1)[0]
    entries = re.findall(r'\{ name: "([^"]+)", hex: "(#[0-9a-f]{6})" \}', body)
    assert len(entries) == 16
    return {name.lower(): (index, hexcode) for index, (name, hexcode) in enumerate(entries)}


def hue_to_ink(colour, inks):
    return inks["slate" if colour == "grey" else colour]


def build_records():
    source = {r["character"]: r for r in rows(PUBLISHED / "data/character_palette_seed.csv")}
    audit = {r["character"]: r for r in rows(PUBLISHED / "data/publication_source_review_2026-11-08.csv")}
    art = rows(PROJECT / "data/pixel_universe_art_v1.csv")
    protos = {r["character"]: r for r in rows(PROJECT / "data/pixel_universe_prototypes.csv")}
    assert len(art) == 12 and len(source) == 24 and len(audit) == 24
    assert set(protos) == {"Superman", "The Joker"}
    inks = palette()
    expected = {"Hero": 6, "Villain": 6}
    counts = {"Hero": 0, "Villain": 0}
    result = []
    for a in art:
        s = source[a["character"]]
        review = audit[a["character"]]
        assert review["coded_dominant_hue"] == s["dominant_colour"]
        assert a["character"] not in {r["character"] for r in result}
        if a["character"] in protos:
            assert a["pixel_code"] == protos[a["character"]]["pixel_code"]
        assert re.fullmatch(r"[0-9a-f]{256}", a["pixel_code"])
        assert re.fullmatch(r"[a-z0-9-]+", a["slug"])
        assert s["role"] in counts
        counts[s["role"]] += 1
        assert s["role"] == ("Hero" if len(result) < 6 else "Villain")
        names = [s["dominant_colour"], s["second_major_colour"]]
        accent = [c.strip() for c in s["accent_colours"].split(";") if c.strip()]
        for name in names + accent:
            assert name in inks or (name == "grey" and "slate" in inks)
            index, _ = hue_to_ink(name, inks)
            assert format(index, "x") in a["pixel_code"]
        result.append({
            "character": a["character"],
            "name": short_name(a["character"]),
            "slug": a["slug"],
            "publisher": s["publisher"],
            "role": s["role"],
            "costume_version": s["costume_version"],
            "main_colour": names[0],
            "main_hex": hue_to_ink(names[0], inks)[1],
            "supporting_colour": names[1],
            "supporting_hex": hue_to_ink(names[1], inks)[1],
            "code": a["pixel_code"],
            "design_note": a["artistic_note"],
            "source_url": review["source_url"],
            "source_risk": review["risk_level"],
            "preview": "/assets/pixel-universe/icons/" + a["slug"] + ".svg",
            "accents": [{"name": c, "hex": hue_to_ink(c, inks)[1]} for c in accent],
        })
    assert counts == expected
    return result, inks


def yaml_text(records):
    fields = (
        "character", "name", "slug", "publisher", "role", "costume_version",
        "main_colour", "main_hex", "supporting_colour", "supporting_hex",
        "code", "design_note", "source_url", "source_risk", "preview"
    )
    chunks = []
    for row in records:
        chunk = ["- character: " + json.dumps(row["character"], ensure_ascii=False)]
        chunk.extend("  " + name + ": " + json.dumps(row[name], ensure_ascii=False) for name in fields[1:])
        chunk.append("  accents: " + json.dumps(row["accents"], ensure_ascii=False))
        chunks.append("\n".join(chunk))
    return "\n".join(chunks) + "\n"


def icon_svg(record, palette_by_index):
    name = escape(record["character"], {'"': "&quot;"})
    items = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400" role="img" aria-label="{name} original 16 by 16 pixel portrait">',
        '<rect width="400" height="400" fill="#F3F4F6"/>',
        '<rect x="40" y="40" width="320" height="320" fill="#ffffff"/>',
        '<g shape-rendering="crispEdges">',
    ]
    code = record["code"]
    for i, digit in enumerate(code):
        ink = int(digit, 16)
        if ink == 0:
            continue
        x, y = 40 + (i % 16) * 20, 40 + (i // 16) * 20
        items.append(f'<rect x="{x}" y="{y}" width="20" height="20" fill="{palette_by_index[ink]}"/>')
    items.extend(["</g>", "</svg>", ""])
    return "\n".join(items)


def mosaic_svg(title, group, colours):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200" role="img" aria-label="Pixel Universe: {title.lower()} colour-portrait mosaic">',
        '<rect width="1200" height="1200" fill="#F3F4F6"/>',
        '<text x="87" y="108" font-family="Space Grotesk, sans-serif" font-size="53" font-weight="700" fill="#111111">PIXEL UNIVERSE</text>',
        f'<text x="87" y="172" font-family="IBM Plex Sans, sans-serif" font-size="34" fill="#454545">{title}</text>',
        '<g shape-rendering="crispEdges">',
    ]
    for j, record in enumerate(group):
        tx, ty = 87+(j % 3)*332, 250+(j//3)*366
        lines.append(f'<rect x="{tx}" y="{ty}" width="300" height="300" fill="#ffffff"/>')
        for i, digit in enumerate(record["code"]):
            ink = int(digit, 16)
            if ink == 0:
                continue
            x, y = tx+6+(i%16)*18, ty+6+(i//16)*18
            lines.append(f'<rect x="{x}" y="{y}" width="18" height="18" fill="{colours[ink]}"/>')
    lines.append("</g>")
    for j, record in enumerate(group):
        tx, ty = 87+(j%3)*332, 250+(j//3)*366
        label = record["name"]
        lines.append(f'<text x="{tx}" y="{ty+338}" font-family="IBM Plex Sans, sans-serif" font-size="30" fill="#111111">{escape(label)}</text>')
    lines.extend([
        '<line x1="87" y1="1080" x2="1113" y2="1080" stroke="#CDD0D3" stroke-width="2"/>',
        '<text x="87" y="1125" font-family="IBM Plex Sans, sans-serif" font-size="22" fill="#555555">Original pixel portraits from qualitative costume colours</text>',
        "</svg>", ""
    ])
    return "\n".join(lines)


def outputs():
    records, ink_map = build_records()
    colours = [None] * 16
    for _, (i, colour) in ink_map.items():
        colours[i] = colour
    assert all(colours)
    created = {YAML: yaml_text(records)}
    for record in records:
        created[OUT / "icons" / (record["slug"] + ".svg")] = icon_svg(record, colours)
    for name, sublist, caption in (
        ("hero_mosaic.svg", records[:6], "The heroes"),
        ("villain_mosaic.svg", records[6:], "The villains"),
    ):
        approved = PROJECT / "output/v1" / name
        data = mosaic_svg(caption, sublist, colours)
        assert approved.read_text(encoding="utf-8") == data, "Approved V1 mosaic changed: " + name
        created[OUT / name] = data
    return created


def main():
    assets = outputs()
    check_only = sys.argv[1:] == ["--check"]
    assert sys.argv[1:] in ([], ["--check"]), "Usage: build_pixel_universe_gallery.py [--check]"
    for location, content in assets.items():
        if check_only:
            assert location.exists() and location.read_text(encoding="utf-8") == content, (
                "Generated asset missing/stale: " + str(location)
            )
        else:
            location.parent.mkdir(parents=True, exist_ok=True)
            location.write_text(content, encoding="utf-8")
    print(("Verified" if check_only else "Wrote"), len(assets), "source-driven Pixel Universe gallery assets")


if __name__ == "__main__":
    main()
