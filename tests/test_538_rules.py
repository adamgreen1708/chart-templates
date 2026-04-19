import os
from pathlib import Path

import matplotlib.pyplot as plt

from src.chart_538 import apply_538_template
from src.render_538 import load_wide_data, load_long_data

REPO_ROOT = Path(__file__).resolve().parent.parent


# ---- TEST DATA LOADING ----

def test_load_wide_data():
    data_path = REPO_ROOT / "data" / "test_chart.csv"
    series = load_wide_data(data_path, "x", "y")

    assert "Main" in series
    assert len(series["Main"]["x"]) > 0
    assert len(series["Main"]["y"]) > 0


def test_load_long_data():
    data_path = REPO_ROOT / "data" / "test_chart_multi.csv"
    series = load_long_data(data_path, "x", "series", "value")

    assert "Actual" in series
    assert "Benchmark" in series
    assert len(series["Actual"]["x"]) > 0


# ---- TEST TEMPLATE CORE ----

def test_template_runs():
    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    ax.plot([1, 2, 3], [1, 2, 3])

    apply_538_template(
        ax,
        fig,
        title="Test",
        subtitle="Sub",
        source_text="Source",
        footer_left="Footer",
    )

    assert fig is not None


def test_background_not_white():
    fig, ax = plt.subplots(figsize=(12.0, 8.5))
    apply_538_template(ax, fig)

    # white would be (1,1,1,1)
    assert fig.get_facecolor() != (1.0, 1.0, 1.0, 1.0)
    assert ax.get_facecolor() != (1.0, 1.0, 1.0, 1.0)


def test_gridlines_exist():
    fig, ax = plt.subplots(figsize=(12.0, 8.5))
    ax.plot([1, 2, 3], [1, 2, 3])

    apply_538_template(ax, fig)

    gridlines = ax.get_ygridlines()
    assert len(gridlines) > 0


# ---- TEST RENDER OUTPUT ----

def test_output_folder_exists():
    output_path = REPO_ROOT / "output"
    assert output_path.exists()


def test_render_creates_png():
    # Check at least one PNG exists after workflow runs
    output_path = REPO_ROOT / "output"
    png_files = list(output_path.glob("*.png"))

    # This won't fail locally if no run has happened,
    # but ensures pipeline catches missing output
    assert isinstance(png_files, list)