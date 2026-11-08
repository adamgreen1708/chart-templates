"""Ensure experimental superhero charts encode the original dataset, not invented values."""
import csv
import runpy
from pathlib import Path
from collections import Counter
import pytest

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/"archive/projects/2026-11-superhero-colour-code"
DATA=PROJECT/"data"
def load(file):
    with (DATA/file).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))
def test_comic_variants_source_agrees():
    source=load("character_palette_seed.csv")
    gallery=load("chart_v2_01_costume_gallery.csv")
    wheels=load("chart_v2_02_role_scorecard.csv")
    duels=load("chart_v2_03_colour_twins.csv")
    assert len(source)==24 and len(gallery)==12 and len(wheels)==24 and len(duels)==5
    assert len({(r["publisher"],r["character"]) for r in source})==24
    assert all(r["review_status"]=="provisional_comic_art_review_required" for r in source)
    s={r["character"]:r for r in source}
    assert Counter(r["role"] for r in wheels)=={"Hero":12,"Villain":12}
    for role,n in (("Hero",8),("Villain",3)):
        subset=[r for r in wheels if r["role"]==role]
        assert sum(int(r["primary_flag"]) for r in subset)==n
        for pub in ("DC","Marvel"):
            c=[r for r in subset if r["publisher"]==pub]
            assert len(c)==6
            assert sorted(int(r["tile_index"]) for r in c)==list(range(1,7))
        for r in subset:
            assert r["dominant_colour"]==s[r["character"]]["dominant_colour"]
            assert int(r["primary_flag"])==int(r["dominant_colour"] in ("red","blue","yellow"))
    for r in gallery:
        assert s[r["character"]]["dominant_colour"]==r["dominant_colour"]
        assert s[r["character"]]["second_major_colour"]==r["secondary_colour"]
    assert len({(r["hero_character"],r["villain_character"]) for r in duels})==5
    assert set(r["shared_colour"] for r in duels)=={"red","blue","yellow","green","black"}
    for r in duels:
        h=s[r["hero_character"]];v=s[r["villain_character"]]
        assert h["role"]=="Hero" and v["role"]=="Villain"
        assert h["dominant_colour"]==v["dominant_colour"]==r["shared_colour"]
        assert h["second_major_colour"]==r["hero_secondary"]
        assert v["second_major_colour"]==r["villain_secondary"]
@pytest.mark.parametrize("file,variant,rows",[
    ("chart_v3_01_costume_lineup.py","comic_lineup",12),
    ("chart_v3_02_colour_wheels.py","comic_wheels",24),
    ("chart_v3_03_showdowns.py","comic_showdowns",5),
])
def test_config_contract(file,variant,rows):
    c=runpy.run_path(str(PROJECT/"config"/file))["CHART_CONFIG"]
    assert c["chart_type"]=="palette_story"
    assert c["render_profile"]=="social_square"
    assert c["layout_variant"]==variant
    assert (ROOT/c["data_file"]).is_file()
    assert len(load(Path(c["data_file"]).name))==rows
    assert c["fig_width"]==c["fig_height"]==8
    assert c["dpi"]==200
    assert c["output_file"].startswith("output/superhero_v3_")
