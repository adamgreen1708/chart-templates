"""Pixel Universe gallery contract: source data, URLs and published art alignment.

Run: python -m pytest tests/test_pixel_universe_gallery.py -q
"""
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "archive/projects/2026-11-pixel-universe/scripts/build_pixel_universe_gallery.py"
PAGE = ROOT / "site/resources/pixel-universe/index.html"
INDEX = ROOT / "site/resources/index.html"
CSS = ROOT / "site/assets/css/pixel-universe.css"
BUILDER = ROOT / "site/assets/js/pixel-art-builder.js"


def generator():
    spec = importlib.util.spec_from_file_location("pixel_universe_gallery", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_gallery_has_twelve_source_joined_presets():
    module = generator()
    cards, _ = module.build_records()
    assert len(cards) == 12
    assert len({x["character"] for x in cards}) == 12
    assert len({x["slug"] for x in cards}) == 12
    assert [x["role"] for x in cards] == ["Hero"] * 6 + ["Villain"] * 6
    assert all(re.fullmatch("[0-9a-f]{256}", x["code"]) for x in cards)
    assert all(x["source_url"].startswith("https://") for x in cards)
    assert all(x["preview"].startswith("/assets/pixel-universe/icons/") for x in cards)


def test_site_assets_regenerate_without_changes():
    assets = generator().outputs()
    assert len(assets) == 15  # 12 icon previews, two mosaics and YAML data
    for path, text in assets.items():
        assert path.exists(), f"Missing committed generated file {path}"
        assert path.read_text(encoding="utf-8") == text, f"Stale art or YAML: {path}"


def test_approved_prototype_pixel_codes_are_preserved():
    module = generator()
    cards, _ = module.build_records()
    original = {r["character"]: r["pixel_code"] for r in module.rows(
        module.PROJECT / "data/pixel_universe_prototypes.csv"
    )}
    assert set(original) == {"Superman", "The Joker"}
    assert all(next(x["code"] for x in cards if x["character"] == name) == code
               for name, code in original.items())


def test_all_builder_links_are_real_and_url_safe():
    module = generator()
    cards, _ = module.build_records()
    studio_js = BUILDER.read_text(encoding="utf-8")
    assert "#size=16&art=" in studio_js
    assert "[0-9a-f]{256}" in studio_js
    for card in cards:
        fragment = "#size=16&art=" + card["code"]
        assert re.fullmatch(r"#size=16&art=[0-9a-f]{256}", fragment)
    template = PAGE.read_text(encoding="utf-8")
    assert 'href="{{ \'/resources/8x8-pixel-art-builder/\' | relative_url }}#size=16&amp;art={{ character.code }}"' in template
    assert template.count('Open &amp; remix') == 2
    assert "pixel_universe" in template
    assert "where: \"role\", \"Hero\"" in template
    assert "where: \"role\", \"Villain\"" in template


def test_mobile_gallery_has_safe_breakpoints_and_no_zoo_mutation():
    styles = CSS.read_text(encoding="utf-8")
    assert "max-width:580px" in styles
    assert "grid-template-columns:minmax(0,1fr)" in styles
    assert "max-width:700px" in styles
    assert "image-rendering:pixelated" in styles
    template = PAGE.read_text(encoding="utf-8")
    assert "hand-picked, qualitative study" in template
    assert "not fabric-area percentages" in template
    assert "no affiliation" in template
    assert "/stories/who-wears-the-hero-colours/" in template
    index = INDEX.read_text(encoding="utf-8")
    assert index.count("'/resources/pixel-universe/'") == 1
    assert "Fifteen paint colours" in index
