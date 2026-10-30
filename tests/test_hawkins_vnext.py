"""Pinned HadCRUT5 data and Hawkins chart-house migration checks."""
import csv,sys
from pathlib import Path
import importlib.util
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from editorial_hawkins import validate_hawkins_source

DATA=ROOT/"archive/projects/2026-10-icons-of-data/editions/07-hawkins/data/HadCRUT.5.2.0.0.analysis.summary_series.global.annual.snapshot_2026-10-19.csv"
CONFIG=ROOT/"archive/projects/2026-10-icons-of-data/editions/07-hawkins/config/review_02_hawkins_vnext.py"

def rows():
    with DATA.open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def test_pinned_complete_annual_data_and_confidence_intervals():
    spec=importlib.util.spec_from_file_location("hawkins_config",CONFIG)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cfg=module.CHART_CONFIG
    years,anomaly,lo,hi=validate_hawkins_source(ROOT,cfg,rows())
    assert (len(years),years[0],years[-1]) == (176,1850,2025)
    assert abs(anomaly[-1]-1.0732167)<1e-7
    assert all(lo<anomaly) and all(anomaly<hi)
    assert cfg["render_profile"]=="social_square"
    assert cfg["chart_type"]=="hawkins_stripes"
    assert cfg["output_file"].startswith("output/")

def test_missing_or_changed_data_fails():
    spec=importlib.util.spec_from_file_location("hawkins_config",CONFIG)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with pytest.raises(ValueError):
        validate_hawkins_source(ROOT,module.CHART_CONFIG,rows()[:-1])
    bad=rows()
    bad[0]["Anomaly (deg C)"]="NaN"
    with pytest.raises(ValueError):
        validate_hawkins_source(ROOT,module.CHART_CONFIG,bad)
