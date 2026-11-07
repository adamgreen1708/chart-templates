"""Contract tests for the real-data superhero palette editorial renderer."""
import csv
import runpy
import sys
from collections import Counter
from pathlib import Path
import pytest

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"archive/projects/2026-11-superhero-colour-code"
DATA=P/"data"
sys.path.insert(0,str(ROOT/"src"))
from editorial_schematics import EDITORIAL_TYPES

def read(name):
    with (DATA/name).open(encoding="utf-8-sig",newline="") as fh:
        return list(csv.DictReader(fh))

def test_dataset_and_palette_views():
    seed=read("character_palette_seed.csv")
    gallery=read("chart_v2_01_costume_gallery.csv")
    score=read("chart_v2_02_role_scorecard.csv")
    twins=read("chart_v2_03_colour_twins.csv")
    assert len(seed)==24 and len({(r["publisher"],r["character"]) for r in seed})==24
    assert len(gallery)==12 and len(score)==24 and len(twins)==5
    assert Counter(r["role"] for r in gallery)=={"Hero":6,"Villain":6}
    assert Counter(r["role"] for r in score)=={"Hero":12,"Villain":12}
    assert set((r["publisher"],r["character"]) for r in score)==set(
        (r["publisher"],r["character"]) for r in seed)
    assert all(r["review_status"]=="provisional_comic_art_review_required" for r in seed)
    byname={r["character"]:r for r in seed}
    for r in gallery:
        s=byname[r["character"]]
        assert s["dominant_colour"]==r["dominant_colour"]
        assert s["second_major_colour"]==r["secondary_colour"]
        assert r["dominant_hex"].startswith("#")
    for r in score:
        s=byname[r["character"]]
        assert s["dominant_colour"]==r["dominant_colour"]
        assert int(r["primary_flag"])==int(s["dominant_colour"] in ("red","blue","yellow"))
    assert sum(int(r["primary_flag"]) for r in score if r["role"]=="Hero")==8
    assert sum(int(r["primary_flag"]) for r in score if r["role"]=="Villain")==3
    for pub in ("DC","Marvel"):
        for role in ("Hero","Villain"):
            cohort=[r for r in score if r["publisher"]==pub and r["role"]==role]
            assert len(cohort)==6 and sorted(int(r["tile_index"]) for r in cohort)==list(range(1,7))
    for r in twins:
        h=byname[r["hero_character"]]
        v=byname[r["villain_character"]]
        assert h["role"]=="Hero" and v["role"]=="Villain"
        assert h["dominant_colour"]==v["dominant_colour"]==r["shared_colour"]
        assert h["second_major_colour"]==r["hero_secondary"]
        assert v["second_major_colour"]==r["villain_secondary"]
    assert set(r["shared_colour"] for r in twins)=={"red","blue","yellow","green","black"}

@pytest.mark.parametrize("file,variant,n",[
    ("chart_v2_01_costume_gallery.py","gallery",12),
    ("chart_v2_02_role_scorecard.py","scorecard",24),
    ("chart_v2_03_colour_twins.py","twins",5),
])
def test_renderer_contract(file,variant,n):
    assert "palette_story" in EDITORIAL_TYPES
    config=runpy.run_path(str(P/"config"/file))["CHART_CONFIG"]
    assert config["chart_type"]=="palette_story"
    assert config["layout_variant"]==variant
    assert config["render_profile"]=="social_square"
    assert (ROOT/config["data_file"]).exists()
    assert len(read(Path(config["data_file"]).name))==n
    assert config["dpi"]==200
    assert config["output_file"].startswith("output/superhero_v2_")
