"""Pixel Universe v1: guard legacy pixel links while extending palette 13 → 16.

Structural tests are intentionally dependency-free; browser/visual QA remains a
separate release gate. This suite does not claim costume-colour measurements.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BUILDER = (SITE / "assets/js/pixel-art-builder.js").read_text(encoding="utf-8")
GALLERY = (SITE / "assets/js/pixel-art-gallery.js").read_text(encoding="utf-8")
PAGE = (SITE / "resources/8x8-pixel-art-builder/index.html").read_text(encoding="utf-8")
ZOO_PAGE = (SITE / "resources/pixel-art-gallery/index.html").read_text(encoding="utf-8")
ZOO_INCLUDE = (SITE / "_includes/pixel-art-gallery.html").read_text(encoding="utf-8")
ZOO_DATA = (SITE / "_data/pixel_art_gallery.yml").read_text(encoding="utf-8")

LEGACY = (
    "#ffffff", "#111111", "#096ba6", "#06ad23", "#7b898f",
    "#e8c94f", "#c34635", "#fb8e31", "#ee3edc",
    "#8b5a3c", "#e8cf9a", "#87c9eb", "#296647",
)
ADDED = ("#6f42c1", "#d4a017", "#b8bdc3")
ALL = LEGACY + ADDED


def _builder_palette():
    # Read only the actual `colours` JS array, not unrelated colour use.
    segment = BUILDER.split("  const colours = [", 1)[1].split("  ];", 1)[0]
    return re.findall(r'\{ name: "([^"]+)", hex: "(#[0-9a-f]{6})" \}', segment)


def _gallery_palette():
    segment = GALLERY.split("  const palette = [", 1)[1].split("  ];", 1)[0]
    return re.findall(r'"(#[0-9a-f]{6})"', segment)


def _swatches():
    return [
        (int(index), colour)
        for index, colour in re.findall(
            r'data-colour="(\d+)" style="--swatch:(#[0-9a-f]{6})"', PAGE
        )
    ]


def test_palette_keeps_all_thirteen_legacy_indices():
    palette = _builder_palette()
    assert len(palette) == 16
    assert tuple(c for _, c in palette[:13]) == LEGACY
    assert palette[13:] == [
        ("Purple", "#6f42c1"), ("Gold", "#d4a017"), ("Silver", "#b8bdc3")
    ]
    assert _gallery_palette() == list(ALL)
    assert _swatches() == list(enumerate(ALL))[1:]
    assert len(_swatches()) == 15


def test_both_decoders_accept_hex_and_encoder_is_hex():
    assert "^[0-9a-f]+$" in BUILDER
    assert "[0-9a-f]{64}" in BUILDER and "[0-9a-f]{256}" in BUILDER
    assert "[0-9a-f]+" in GALLERY
    assert 'parseInt(value, 16)' in BUILDER
    assert BUILDER.count("parseInt(value, 16)") == 3
    assert 'value.toString(16)' in BUILDER
    assert 'parseInt(code[index], 16)' in GALLERY
    assert "parseInt(value, 13)" not in BUILDER
    assert "value.toString(13)" not in BUILDER
    assert "parseInt(code[index], 13)" not in GALLERY


def test_legacy_link_formats_and_local_storage_identifiers_unchanged():
    assert 'return dimension === 8 ? "#art=" + code : "#size=16&art=" + code;' in BUILDER
    assert 'coffeetableviz.pixel-art.v1' in BUILDER
    assert 'coffeetableviz.pixel-art.16.v1' in BUILDER
    for n in (64, 256):
        # Hex digits 0–c have the same numeric value and character as base 13.
        legacy = "0123456789abc" * (n // 13) + "0123456789abc"[:n % 13]
        assert len(legacy) == n
        assert "".join(format(int(c, 16), "x") for c in legacy) == legacy
        assert all(int(c, 16) < 13 for c in legacy)
        extended = ("def0123456789abc" * (n // 16))[:n]
        assert len(extended) == n
        assert "".join(format(int(c, 16), "x") for c in extended) == extended


def test_existing_zoo_codes_are_all_valid_legacy_codes():
    codes = re.findall(r'^  code: "([^"]+)"', ZOO_DATA, flags=re.MULTILINE)
    assert len(codes) >= 20
    assert all(len(code) in (64, 256) for code in codes)
    assert all(re.fullmatch(r"[0-9a-c]+", code) for code in codes)


def test_user_facing_counts_and_cache_versions_match():
    assert "Fifteen paint colours" in PAGE
    assert 'aria-label="Fifteen paint colours"' in PAGE
    assert "fifteen paint colours" in ZOO_PAGE
    assert "fifteen paint colours" in ZOO_INCLUDE
    assert PAGE.count("20261108-palette16") == 2
    assert ZOO_PAGE.count("20261108-palette16") == 1
