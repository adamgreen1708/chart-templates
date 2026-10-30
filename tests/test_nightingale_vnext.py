"""Nightingale migration: preserved monthly data, rates and shared profile."""
import csv
import sys
from pathlib import Path
import importlib.util

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from editorial_nightingale import validate_nightingale_rows

SOURCE = ROOT / "archive/projects/2026-10-icons-of-data/editions/04-nightingale/data/nightingale_24_months.csv"
CONFIG = ROOT / "archive/projects/2026-10-icons-of-data/editions/04-nightingale/config/review_02_nightingale_vnext.py"


def rows():
    with SOURCE.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_full_source_is_pinned_and_checked():
    sample = rows()
    dates = validate_nightingale_rows(sample)
    assert len(dates) == 24
    assert sum(int(r["Disease"]) for r in sample[:12]) == 11157
    assert sum(int(r["Disease"]) for r in sample[12:]) == 3319
    assert sample[9]["Date"] == "1855-01-01"
    assert float(sample[9]["Disease.rate"]) == 1022.8


def test_fails_on_rate_or_row_count_change():
    sample = rows()
    sample[9]["Disease.rate"] = "1000"
    with pytest.raises(ValueError, match="annualised"):
        validate_nightingale_rows(sample)
    with pytest.raises(ValueError, match="24 monthly"):
        validate_nightingale_rows(rows()[:-1])


def test_preview_is_real_config_and_is_not_site_published():
    spec = importlib.util.spec_from_file_location("nightingale_config", CONFIG)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    config = module.CHART_CONFIG
    assert config["render_profile"] == "social_square"
    assert config["chart_type"] == "nightingale_rates"
    assert ROOT.joinpath(config["data_file"]) == SOURCE
    assert config["output_file"].startswith("output/")
    assert not config["output_file"].startswith("site/")
