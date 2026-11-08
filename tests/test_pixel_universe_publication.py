"""Pixel Universe sequel: approve the exact feature art before publication.

This QA intentionally expects published:false while the review PR is open.
To publish, switch the status and the final test after explicit approval.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / "site/_posts/2026-11-08-pixel-universe-256-squares.md"
ART = ROOT / "site/assets/pixel-universe/feature-pixel-identity.svg"
GALLERY = ROOT / "site/resources/pixel-universe/index.html"
SOURCE = ROOT / "archive/projects/2026-11-pixel-universe/content/feature_art_review.md"


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
    assert "An anonymous blocky mask" in front
    assert "256-cell design code" in post


def test_feature_is_house_style_stencil_and_text_free():
    xml = ART.read_text(encoding="utf-8")
    assert 'width="1600" height="1600"' in xml
    assert 'fill="#F3F4F6"' in xml
    assert 'fill="#C44E52"' in xml
    assert "<text" not in xml and "<image" not in xml
    assert "<script" not in xml and "<foreignObject" not in xml
    assert "<use" not in xml and "http://" not in xml.replace(
        'xmlns="http://www.w3.org/2000/svg"', ""
    )
    tree = ET.fromstring(xml)
    assert tree.attrib["viewBox"] == "0 0 1600 1600"
    allowed = {"#F3F4F6", "#C44E52", "#161819", "#383A3B"}
    rectangles = list(tree.iter("{http://www.w3.org/2000/svg}rect"))
    assert len(rectangles) > 100
    assert {r.attrib.get("fill") for r in rectangles} <= allowed
    assert 1 <= sum(r.attrib.get("fill") == "#C44E52" for r in rectangles) <= 10


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
    assert "not yet an approved published asset" in note
