"""Pixel Universe sequel draft: editorial consistency and publishing safeguards."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"archive/projects/2026-11-pixel-universe/content"
DRAFT=(P/"editorial_draft.md").read_text(encoding="utf-8")
SOCIAL=(P/"social_copy.md").read_text(encoding="utf-8")
RELEASE=(P/"editorial_release_notes.md").read_text(encoding="utf-8")


def test_two_mosaics_exact_assets_and_attribution():
    assert "/assets/pixel-universe/hero_mosaic.svg" in DRAFT
    assert "/assets/pixel-universe/villain_mosaic.svg" in DRAFT
    assert DRAFT.count('<figure class="story-chart full-bleed">') == 2
    assert "qualitative editorial classifications" in DRAFT
    assert "not measurements of costume area" in DRAFT
    assert "not a formal test" in DRAFT


def test_links_consistent_with_gallery_and_original_story():
    assert "/stories/who-wears-the-hero-colours/" in DRAFT
    assert "/resources/pixel-universe/" in DRAFT
    assert "/resources/8x8-pixel-art-builder/" in DRAFT
    assert "/resources/pixel-universe/" in SOCIAL
    assert "six heroes and six villains" in DRAFT


def test_publication_gate_remains_explicit_and_unmerged():
    assert "not published" in RELEASE.lower()
    assert "approval" in RELEASE.lower()
    assert "feature-art review" in RELEASE.lower()
    assert "published: false" in RELEASE
    assert "#194" in RELEASE
