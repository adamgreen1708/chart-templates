#!/usr/bin/env python3
"""Render a deterministic square card from a Blockbuster Quote edition."""

from __future__ import annotations

import argparse
import random
from datetime import date
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont


SIZE = 1600
PAPER = (241, 241, 241)      # site --paper: #f1f1f1
INK = (17, 17, 17)          # site --ink: #111111
MUTED = (100, 100, 100)     # site --muted: #646464
LINE = (207, 207, 207)      # site --line: #cfcfcf
ACCENT = (201, 69, 69)      # site --accent: #c94545
SKETCH_FILL = (227, 227, 227)

FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SERIF_ITALIC = "/usr/share/fonts/opentype/urw-base35/NimbusRoman-Italic.otf"


def read_front_matter(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"{path} has no YAML front matter")
    _, matter, _ = raw.split("---", 2)
    return yaml.safe_load(matter)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def fit_lines(draw: ImageDraw.ImageDraw, copy: str, face: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = copy.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=face)[2] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_megaphone(draw: ImageDraw.ImageDraw) -> None:
    """Draw one symbolic, monochrome, cross-hatched megaphone."""
    horn = [(1060, 455), (1425, 330), (1425, 775), (1060, 650)]
    draw.polygon(horn, fill=SKETCH_FILL, outline=INK, width=9)
    draw.rounded_rectangle((975, 490, 1085, 620), radius=18, fill=SKETCH_FILL, outline=INK, width=9)
    draw.polygon([(1040, 625), (1130, 650), (1085, 865), (995, 840)], fill=SKETCH_FILL, outline=INK)
    draw.line([(1040, 625), (1130, 650), (1085, 865), (995, 840), (1040, 625)], fill=INK, width=9)

    # Deliberately imperfect-looking hatch strokes, clipped by hand to the horn.
    hatch = [
        ((1090, 478), (1240, 410)), ((1082, 515), (1320, 405)),
        ((1075, 555), (1402, 401)), ((1078, 595), (1418, 438)),
        ((1100, 625), (1418, 478)), ((1160, 645), (1418, 530)),
        ((1220, 665), (1418, 578)), ((1280, 685), (1418, 625)),
        ((1340, 705), (1418, 672)),
    ]
    for start, end in hatch:
        draw.line([start, end], fill=INK, width=3)
    for offset in (0, 34, 68):
        draw.line([(1015 + offset // 4, 680 + offset), (1098 + offset // 4, 704 + offset)], fill=INK, width=3)

    # Sound marks belong to the same single symbolic sketch.
    draw.arc((1450, 430, 1535, 680), -67, 67, fill=INK, width=7)
    draw.arc((1470, 380, 1590, 730), -67, 67, fill=INK, width=5)


def render(data: dict, output: Path) -> None:
    image = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(image)

    # A fixed seed gives the paper a reproducible, lightly flecked surface.
    rng = random.Random(18091998)
    for _ in range(7200):
        x, y = rng.randrange(SIZE), rng.randrange(SIZE)
        shade = rng.choice(((224, 224, 224), (247, 247, 247), (233, 233, 233)))
        draw.point((x, y), fill=shade)

    run_date = data["date"]
    if isinstance(run_date, str):
        run_date = date.fromisoformat(run_date)
    display_date = run_date.strftime("%-d %B %Y").upper()

    margin = 112
    header_face = font(FONT_SANS_BOLD, 25)
    date_face = font(FONT_SANS, 25)
    film_face = font(FONT_SANS_BOLD, 42)
    quote_face = font(FONT_SERIF, 78)
    label_face = font(FONT_SANS_BOLD, 22)
    body_face = font(FONT_SANS, 33)
    kicker_face = font(FONT_SERIF_ITALIC, 31)

    draw.text((margin, 92), data["header"], font=header_face, fill=ACCENT)
    date_box = draw.textbbox((0, 0), display_date, font=date_face)
    draw.text((SIZE - margin - date_box[2], 92), display_date, font=date_face, fill=MUTED)
    draw.line((margin, 142, SIZE - margin, 142), fill=ACCENT, width=5)

    draw.text((margin, 184), data["film"], font=film_face, fill=INK)
    film_width = draw.textbbox((margin, 184), data["film"], font=film_face)[2]
    draw.text((film_width + 20, 196), str(data["film_year"]), font=date_face, fill=ACCENT)

    quote = f'“{data["quote"]}”'
    quote_lines = fit_lines(draw, quote, quote_face, 830)
    y = 330
    for line in quote_lines:
        draw.text((margin, y), line, font=quote_face, fill=INK)
        y += 104

    draw_megaphone(draw)

    draw.line((margin, 965, SIZE - margin, 965), fill=LINE, width=3)
    draw.text((margin, 1012), "WHY TODAY", font=label_face, fill=ACCENT)
    y = 1060
    for line in fit_lines(draw, data["why_today"], body_face, SIZE - 2 * margin):
        draw.text((margin, y), line, font=body_face, fill=INK)
        y += 50

    draw.line((margin, 1402, SIZE - margin, 1402), fill=INK, width=2)
    draw.text((margin, 1440), data["kicker"], font=kicker_face, fill=MUTED)

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, format="PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("edition", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    render(read_front_matter(args.edition), args.output)


if __name__ == "__main__":
    main()
