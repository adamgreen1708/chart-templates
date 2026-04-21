import csv
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_538 import apply_538_template
from chart_config import CHART_CONFIG


# =========================
# HELPERS
# =========================

def _coerce_value(value):
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except Exception:
        return value


def _safe_headers(reader):
    reader.fieldnames = [h.strip().replace("\ufeff", "") for h in reader.fieldnames]
    return reader


def _clean_row(row):
    return {k.strip(): v for k, v in row.items()}


def _fail_with_columns(reader, missing):
    raise ValueError(
        f"Column '{missing}' not found.\nAvailable columns: {', '.join(reader.fieldnames)}"
    )


def _get_color(d, default="#1F8FA8"):
    return d.get("color") or d.get("colour") or default


def _format_value(val, fmt=None):
    if fmt:
        try:
            if "{" in fmt:
                return fmt.format(val)
            return format(val, fmt)
        except Exception:
            pass

    if isinstance(val, float):
        return f"{val:.1f}".rstrip("0").rstrip(".")
    return str(val)


def _axis_formatter_from_fmt(fmt):
    if not fmt:
        return None

    def _formatter(val, pos):
        try:
            if "{" in fmt:
                return fmt.format(val)
            return format(val, fmt)
        except Exception:
            return _format_value(val)

    return FuncFormatter(_formatter)


# =========================
# DATA LOADING
# =========================

def _sort_series(data):
    sorted_data = {}
    for series_name, vals in data.items():
        pairs = list(zip(vals["x"], vals["y"]))
        pairs.sort(key=lambda t: t[0])
        sorted_data[series_name] = {
            "x": [p[0] for p in pairs],
            "y": [p[1] for p in pairs],
        }
    return sorted_data


def load_wide_data(csv_path, x_col, y_col):
    x_vals, y_vals = [], []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = _safe_headers(csv.DictReader(f))

        if x_col not in reader.fieldnames:
            _fail_with_columns(reader, x_col)
        if y_col not in reader.fieldnames:
            _fail_with_columns(reader, y_col)

        for row in reader:
            row = _clean_row(row)
            x_vals.append(_coerce_value(row[x_col]))
            y_vals.append(_coerce_value(row[y_col]))

    return {"Main": {"x": x_vals, "y": y_vals}}


def load_long_data(csv_path, x_col, series_col, value_col):
    grouped = defaultdict(lambda: {"x": [], "y": []})

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = _safe_headers(csv.DictReader(f))

        for col in [x_col, series_col, value_col]:
            if col not in reader.fieldnames:
                _fail_with_columns(reader, col)

        for row in reader:
            row = _clean_row(row)
            series_name = row[series_col]
            grouped[series_name]["x"].append(_coerce_value(row[x_col]))
            grouped[series_name]["y"].append(_coerce_value(row[value_col]))

    return _sort_series(dict(grouped))


# =========================
# VALIDATION
# =========================

def validate_chart_config(cfg, data):
    chart_type = cfg.get("chart_type")
    data_format = cfg.get("data_format")

    errors = []

    if chart_type not in {"line", "bar", "dot", "scatter"}:
        errors.append(f"Invalid chart_type: {chart_type}")

    if data_format not in {"long", "wide"}:
        errors.append(f"Invalid data_format: {data_format}")

    if chart_type == "line":
        if data_format != "long":
            errors.append("Line charts require data_format='long'")
        if not cfg.get("series_col"):
            errors.append("Line charts require 'series_col'")

    if chart_type == "bar":
        if data_format != "wide":
            errors.append("Bar charts require data_format='wide'")
        if cfg.get("series_col"):
            errors.append("Bar charts must not use 'series_col'")

    if chart_type == "dot":
        if data_format != "wide":
            errors.append("Dot charts require data_format='wide'")
        if not cfg.get("sort_descending"):
            errors.append("Dot charts require sort_descending=True")

    if chart_type == "scatter":
        for vals in data.values():
            if not all(isinstance(x, (int, float)) for x in vals["x"]):
                errors.append("Scatter requires numeric x")
            if not all(isinstance(y, (int, float)) for y in vals["y"]):
                errors.append("Scatter requires numeric y")

    y_axis_max = cfg.get("y_axis_max")
    if y_axis_max is not None:
        all_y = []
        for vals in data.values():
            all_y.extend(vals["y"])
        if all_y and max(all_y) > y_axis_max:
            errors.append("y_axis_max too low for data")

    if errors:
        raise ValueError("CHART CONFIG VALIDATION FAILED:\n- " + "\n- ".join(errors))


# =========================
# RENDERERS
# =========================

def render_line(ax, data, cfg):
    for vals in data.values():
        ax.plot(vals["x"], vals["y"], color="#1F8FA8")


def render_bar(ax, data, cfg):
    vals = next(iter(data.values()))
    x = list(range(len(vals["x"])))
    ax.bar(x, vals["y"], color="#1F8FA8")
    ax.set_xticks(x)
    ax.set_xticklabels(vals["x"])


def render_dot(ax, data, cfg):
    vals = next(iter(data.values()))
    pairs = list(zip(vals["x"], vals["y"]))
    pairs.sort(key=lambda t: t[1], reverse=True)

    labels = [p[0] for p in pairs]
    values = [p[1] for p in pairs]

    y_pos = list(range(len(labels)))
    ax.scatter(values, y_pos, color="#1F8FA8")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()


def render_scatter(ax, data, cfg):
    for vals in data.values():
        ax.scatter(vals["x"], vals["y"], color="#1F8FA8")


# =========================
# MAIN
# =========================

def main():
    print("RUNNING 538 RENDER FINAL")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    cfg = CHART_CONFIG

    data_path = REPO_ROOT / cfg["data_file"]

    if cfg["data_format"] == "long":
        data = load_long_data(
            data_path,
            cfg["x_col"],
            cfg["series_col"],
            cfg["value_col"],
        )
    else:
        data = load_wide_data(
            data_path,
            cfg["x_col"],
            cfg["y_col"],
        )

    # ✅ VALIDATION HERE
    validate_chart_config(cfg, data)

    fig, ax = plt.subplots(figsize=(12, 8.5))

    if cfg["chart_type"] == "line":
        render_line(ax, data, cfg)
    elif cfg["chart_type"] == "bar":
        render_bar(ax, data, cfg)
    elif cfg["chart_type"] == "dot":
        render_dot(ax, data, cfg)
    elif cfg["chart_type"] == "scatter":
        render_scatter(ax, data, cfg)

    apply_538_template(
        ax,
        fig,
        title=cfg.get("title", ""),
        subtitle=cfg.get("subtitle", ""),
        source_text=cfg.get("source_text", ""),
        footer_left=cfg.get("footer_left", ""),
        vertical_gridlines=True,
    )

    fig.savefig(REPO_ROOT / "output/chart.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    main()