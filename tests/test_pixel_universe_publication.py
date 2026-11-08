"""Pixel Universe sequel: approve the exact feature art before publication.

This QA intentionally expects published:false while the review PR is open.
To publish, switch the status and the final test after explicit approval.
"""
from pathlib import Path
import importlib.util
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / "site/_posts/2026-11-08-pixel-universe-256-squares.md"
ART = ROOT / "site/assets/pixel-universe/feature-pixel-identity.svg"
GALLERY = ROOT / "site/resources/pixel-universe/index.html"
SOURCE = ROOT / "archive/projects/2026-11-pixel-universe/content/feature_art_review.md"
FEATURE_CODE = ROOT / "archive/projects/2026-11-pixel-universe/data/feature_pixelstudio_16x16.txt"
FEATURE_SCRIPT = ROOT / "archive/projects/2026-11-pixel-universe/scripts/render_feature_pixelstudio.py"


def test_unpublished_approval_gate_and_post_metadata():
    post = POST.read_text(encoding="utf-8")
    assert post.startswith("---\n")
    front = post.split("---", 2)[1]
    assert re.search(r"(?m)^published: false$", front)
    assert re.search(r"(?m)^category: Culture$", front)
    assert re.search(r"(?m)^layout: post$", front)
    assert re.search(r"(?m)^slug: pixel-universe-256-squares$", front)
    for key in ("card_image", "hero_image", "social_image"):
        assert re.search(
            rf"(?m)^{key}: /assets/pixel-universe/feature-pixel-identity.svg$", front
        )
    assert "An anonymous black and slate pixel mask built from equal-sized squares" in front
    assert "256-cell design code" in post


def test_feature_is_house_style_stencil_and_text_free():
    xml = ART.read_text(encoding="utf-8")
    assert 'width="1600" height="1600"' in xml
    assert 'fill="#F3F4F6"' in xml
    assert 'fill="#c34635"' in xml
    assert "<text" not in xml and "<image" not in xml
    assert "<script" not in xml and "<foreignObject" not in xml
    assert "<use" not in xml and "http://" not in xml.replace(
        'xmlns="http://www.w3.org/2000/svg"', ""
    )
    tree = ET.fromstring(xml)
    assert tree.attrib["viewBox"] == "0 0 1600 1600"
    # Every painted rectangle must come from ONE 16x16 Studio code and use
    # identical 70px square tiles and the precise Studio palette indices.
    spec = importlib.util.spec_from_file_location("pixel_universe_feature", FEATURE_SCRIPT)
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    code = renderer.load_code()
    palette = renderer.studio_palette()
    assert len(code) == 256
    assert re.fullmatch(r"[0-9a-f]{256}", FEATURE_CODE.read_text(encoding="utf-8").strip())
    assert xml == renderer.svg(code, palette), "SVG must match the 256 source cells"
    rectangles = list(tree.iter("{http://www.w3.org/2000/svg}rect"))
    assert rectangles[0].attrib == {"width": "1600", "height": "1600", "fill": "#F3F4F6"}
    pixels = rectangles[1:]
    assert len(pixels) == sum(digit != "0" for digit in code) == 95
    expected = []
    for i, digit in enumerate(code):
        if digit == "0":
            continue
        expected.append({
            "x": str(192 + (i % 16) * 76),
            "y": str(192 + (i // 16) * 76),
            "width": "70",
            "height": "70",
            "fill": palette[int(digit, 16)],
        })
    assert [rect.attrib for rect in pixels] == expected
    assert all(rect.attrib["width"] == rect.attrib["height"] == "70" for rect in pixels)
    assert len({(rect.attrib["width"], rect.attrib["height"]) for rect in pixels}) == 1
    assert {rect.attrib["fill"] for rect in pixels} == {"#111111", "#7b898f", "#c34635"}
    assert sum(rect.attrib["fill"] == "#c34635" for rect in pixels) == 8
    assert all(
        any(code[y*16+x] != "0" for (x,y) in side)
        for side in [
            [(x,0) for x in range(16)], [(x,15) for x in range(16)],
            [(0,y) for y in range(16)], [(15,y) for y in range(16)]
        ]
    )


def test_article_is_true_to_qualitative_source_and_links_work():
    post = POST.read_text(encoding="utf-8")
    for path in (
        "/assets/pixel-universe/hero_mosaic.svg",
        "/assets/pixel-universe/villain_mosaic.svg",
        "/stories/who-wears-the-hero-colours/",
        "/resources/8x8-pixel-art-builder/",
        "/resources/pixel-universe/",
    ):
        assert path in post
    assert "six heroes and six villains" in post
    assert "qualitative editorial classifications" in post
    assert "not measurements of costume area" in post
    assert "not a formal test" in post
    assert "no affiliation" in post or "not affiliated" in post
    assert POST.name == "2026-11-08-pixel-universe-256-squares.md"
    gallery = GALLERY.read_text(encoding="utf-8")
    assert "Read the Pixel Universe story" in gallery
    assert "/stories/pixel-universe-256-squares/" in gallery
    note = SOURCE.read_text(encoding="utf-8")
    assert "95 painted cells" in note
    assert "user approved" in note.lower()
    assert "individual pixels scattered around all sides" in post
