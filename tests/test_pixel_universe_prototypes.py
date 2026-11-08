"""Prototype QA: exact editable codes and source dataset parity."""
import csv
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"archive/projects/2026-11-pixel-universe"
S=ROOT/"archive/projects/2026-11-superhero-colour-code/data/character_palette_seed.csv"


def rows(path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def test_two_icons_have_exactly_256_hex_cells():
    data=rows(P/"data/pixel_universe_prototypes.csv")
    assert [x["character"] for x in data] == ["Superman","The Joker"]
    assert all(len(x["pixel_code"])==256 for x in data)
    assert all(set(x["pixel_code"]) <= set("0123456789abcdef") for x in data)
    assert all(x["grid_size"]=="16" for x in data)


def test_palette_roles_match_published_source():
    expected={x["character"]:x for x in rows(S)}
    data=rows(P/"data/pixel_universe_prototypes.csv")
    for x in data:
        old=expected[x["character"]]
        for col in ("publisher","role","costume_version","dominant_colour","second_major_colour","accent_colours"):
            assert x[col]==old[col]
        assert x["review_status"]=="creative_prototype_review_only"
        assert "fabric percentage" not in x["design_note"].lower()


def test_source_hue_codes_are_present():
    js=(ROOT/"site/assets/js/pixel-art-builder.js").read_text(encoding="utf-8")
    assert '"Purple", hex: "#6f42c1"' in js and '"Gold", hex: "#d4a017"' in js
    palette={"blue":"2","red":"6","yellow":"5","purple":"d","green":"3","orange":"7"}
    for x in rows(P/"data/pixel_universe_prototypes.csv"):
        for col in ("dominant_colour","second_major_colour","accent_colours"):
            if x[col]:
                assert palette[x[col]] in x["pixel_code"]


def test_svg_renderer_is_deterministic_and_matches_review_assets():
    src=P/"scripts/render_prototype_svg.py"
    spec=importlib.util.spec_from_file_location("pixel_universe_prototypes",src)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    names={name.lower():val for name,val in mod.palette().items()}
    cols=[None]*16
    for _,(i,c) in names.items(): cols[i]=c
    for row in rows(P/"data/pixel_universe_prototypes.csv"):
        regenerated=mod.svg_from_code(
            row["pixel_code"],cols,row["character"]+" original 16 by 16 pixel art prototype"
        )
        committed=(P/"output/prototypes"/(row["slug"]+".svg")).read_text(encoding="utf-8")
        assert regenerated==committed
