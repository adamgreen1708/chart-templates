"""Guard the publication-ready Superhero Colours package against mismatched data/assets."""
from pathlib import Path
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/"archive/projects/2026-11-superhero-colour-code"
SITE=ROOT/"site"
POST=SITE/"_posts/2026-11-08-who-wears-the-hero-colours.md"
SITE_IMGS=SITE/"assets/charts/superhero-colour-code"
NAMES=(
    "superhero_v3_01_comic_lineup.png",
    "superhero_v3_02_colour_wheels.png",
    "superhero_v3_03_showdowns.png",
)
PRIMARIES={"red","blue","yellow"}

def records(path):
    with path.open(encoding="utf-8",newline="") as fh:
        return list(csv.DictReader(fh))

def test_publication_ready_article_is_explicitly_qualitative():
    content=POST.read_text(encoding="utf-8")
    assert content.startswith("---\n")
    meta=content.split("---",2)[1]
    assert re.search(r"(?m)^published:\s*true$",meta)
    assert re.search(r"(?m)^category:\s*Culture$",meta)
    assert "layout: post" in meta
    assert "hero_image: /assets/charts/superhero-colour-code/superhero_v3_01_comic_lineup.png" in meta
    assert "<figure class=\"story-chart full-bleed\">" in content
    assert content.count("<figure class=\"story-chart full-bleed\">")==2
    assert "../output/" not in content
    assert "0 / 24" not in content # this is a research gate, not a claim about what readers see
    assert "curated, qualitative exploration" in content
    assert "not measured fabric areas" in content
    assert "Sinestro" in content
    assert "not every individual colour choice has been verified" in content.lower()
    assert "Tim Leong" in content

def test_published_png_assets_are_binary_identical_to_approved_archive():
    article=POST.read_text(encoding="utf-8")
    for name in NAMES:
        original=(PROJECT/"output"/name).read_bytes()
        site=(SITE_IMGS/name).read_bytes()
        assert hashlib.sha256(original).digest()==hashlib.sha256(site).digest(),name
        assert name in article

def test_all_24_characters_appear_under_wheels_in_same_order():
    blog=POST.read_text(encoding="utf-8")
    rs=records(PROJECT/"data/chart_v2_02_role_scorecard.csv")
    assert len(rs)==24
    all_lines=blog.splitlines()
    table_start=all_lines.index("| Role | DC character · main hue | Marvel character · main hue |")
    assert all_lines[table_start+1]=="|:--|:--|:--|"
    tab=all_lines[table_start+2:table_start+14]
    assert len(tab)==12
    for i,role in enumerate(("Hero","Villain")):
        dc=sorted((r for r in rs if r["role"]==role and r["publisher"]=="DC"),
                  key=lambda r:int(r["tile_index"]))
        marvel=sorted((r for r in rs if r["role"]==role and r["publisher"]=="Marvel"),
                      key=lambda r:int(r["tile_index"]))
        assert len(dc)==len(marvel)==6
        for index in range(6):
            def fmt(r):
                colour=r["dominant_colour"]
                if colour in PRIMARIES: colour=f"**{colour}**"
                return f'{r["display"]} · {colour}'
            expected=f"| {role} | {fmt(dc[index])} | {fmt(marvel[index])} |"
            assert tab[i*6+index]==expected

def test_source_risk_gate_is_explicit_not_falsely_approved():
    rs=records(PROJECT/"data/publication_source_review_2026-11-08.csv")
    assert len(rs)==24
    assert len({(r["publisher"],r["character"]) for r in rs})==24
    assert sum(r["risk_level"]=="high" for r in rs)==14
    assert all(r["validated_for_publication"]=="no" for r in rs)
    assert all(r["chosen_comic_art_pinned"]=="no" for r in rs)
    content=(PROJECT/"content/publication_readiness.md").read_text(encoding="utf-8")
    assert "qualitative publication route" in content.lower()
    assert "not independently verified" in content.lower()
