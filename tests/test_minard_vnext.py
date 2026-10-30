"""Minard migration: original troop widths and geography remain data-led."""
import csv
from pathlib import Path
import sys, importlib.util
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from editorial_minard import load_validate_minard
BASE=ROOT/"archive/projects/2026-10-icons-of-data"
REVIEW=BASE/"review/config_minard_vnext.py"


def troop_rows():
    with (BASE/"data/minard_troops.csv").open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))


def config():
    module_spec=importlib.util.spec_from_file_location("minard_review",REVIEW)
    module=importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module.CHART_CONFIG


def test_original_historical_data_and_labels_are_kept():
    groups,cities,temp=load_validate_minard(ROOT,config(),troop_rows())
    assert sum(len(v) for v in groups.values())==51
    assert (len(cities),len(temp))==(20,9)
    assert [int(groups[(g,"A")][0]["survivors"]) for g in (1,2,3)]==[340000,60000,22000]
    assert int(groups[(1,"R")][-1]["survivors"])==4000
    assert min(int(x["temp"]) for x in temp)==-30
    assert sum(not x["date"] for x in temp)==1


def test_unverified_values_fail_closed():
    rows=troop_rows()
    rows[0]["survivors"]="340001"
    with pytest.raises(ValueError,match="don't match"):
        load_validate_minard(ROOT,config(),rows)
    with pytest.raises(ValueError,match="51 troop"):
        load_validate_minard(ROOT,config(),troop_rows()[:-1])


def test_new_house_config_is_review_only():
    cfg=config()
    assert cfg["render_profile"]=="social_square"
    assert cfg["chart_type"]=="minard_campaign"
    assert cfg["data_file"]=="archive/projects/2026-10-icons-of-data/data/minard_troops.csv"
    assert cfg["output_file"]=="output/minard_vnext_preview.png"
