"""Tests for the complete draft Pixel Universe v1 icon dataset and mosaics."""
import importlib.util
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/"archive/projects/2026-11-pixel-universe"
SOURCE=ROOT/"archive/projects/2026-11-superhero-colour-code/data/character_palette_seed.csv"


def load(path):
    with path.open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))


def build_module():
    path=PROJECT/"scripts/build_pixel_universe_v1.py"
    spec=importlib.util.spec_from_file_location("pixel_universe_v1",path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_all_twelve_codes_are_16x16_and_unique():
    art=load(PROJECT/"data/pixel_universe_art_v1.csv")
    assert len(art)==12
    assert len({x["character"] for x in art})==12
    assert len({x["pixel_code"] for x in art})==12
    assert all(len(x["pixel_code"])==256 for x in art)
    assert all(set(x["pixel_code"]) <= set("0123456789abcdef") for x in art)


def test_exact_published_source_colours_present():
    mod=build_module()
    art,palette=mod.validate()
    seed={x["character"]:x for x in load(SOURCE)}
    for row in art:
        old=seed[row["character"]]
        for colour in (old["dominant_colour"],old["second_major_colour"]):
            if colour:
                index=palette.get(colour,palette.get({"grey":"slate"}.get(colour,"")))[0]
                assert format(index,"x") in row["pixel_code"]


def test_prototypes_unchanged():
    existing={x["character"]:x["pixel_code"] for x in load(PROJECT/"data/pixel_universe_prototypes.csv")}
    art={x["character"]:x["pixel_code"] for x in load(PROJECT/"data/pixel_universe_art_v1.csv")}
    assert set(existing)=={"Superman","The Joker"}
    assert all(art[k]==v for k,v in existing.items())


def test_committed_mosaics_are_reproducible():
    mod=build_module()
    art,palette=mod.validate()
    cols=[None]*16
    for _,(idx,value) in palette.items(): cols[idx]=value
    for side,subset,label in (("hero",art[:6],"The heroes"),("villain",art[6:],"The villains")):
        expected=mod.mosaic_svg(label,subset,cols)
        committed=(PROJECT/"output/v1"/(side+"_mosaic.svg")).read_text(encoding="utf-8")
        assert committed==expected
