import csv
import os
import sys
from collections import defaultdict
from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_538 import apply_538_template  # noqa: E402
from chart_utils import add_reference_line, highlight_point, add_end_label  # noqa: E402
from chart_config import CHART_CONFIG  # noqa: E402


def _coerce_value(value):
    try:
        num = float(value)
        if num.is_integer():
            return int(num)
        return num
    except ValueError:
        return value


def load_wide_data(csv_path, x_col, y_col):
    x_vals, y_vals = [], []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x_vals.append(_coerce_value(row[x_col]))
            y_val = _coerce_value(row[y_col])
            if not isinstance(y_val, (int, float)):
                raise ValueError(f"Non-numeric y value: {row[y_col]}")
            y_vals.append(y_val)

    return {"Main": {"x": x_vals, "y": y_vals}}


def load_long_data(csv_path, x_col, series_col, value_col):
    grouped = defaultdict(lambda: {"x": [], "y": []})

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            grouped[row[series_col]]["x"].append(_coerce_value(row[x_col]))
            y_val = _coerce_value(row[value_col])
            if not isinstance(y_val, (int, float)):
                raise ValueError(f"Non-numeric value: {row[value_col]}")
            grouped[row[series_col]]["y"].append(y_val)

    return dict(grouped)


def get_series_style(series_name, index, config):
    style_cfg = config.get("series_style", {})
    palette = style_cfg.get("palette", ["#1F8FA8"])

    style = {
        "color": palette[index % len(palette)],
        "linewidth": style_cfg.get("default_linewidth", 3),
        "bar_width": style_cfg.get("default_bar_width", 0.7),
        "marker_size": style_cfg.get("default_marker_size", 55),
    }

    style.update(config.get("series_overrides", {}).get(series_name, {}))
    return style


def sort_single_series(series_data, descending=True):
    if len(series_data) != 1:
        return series_data

    name = next(iter(series_data))
    values = series_data[name]

    pairs = list(zip(values["x"], values["y"]))
    pairs.sort(key=lambda t: t[1], reverse=descending)

    return {
        name: {
            "x": [p[0] for p in pairs],
            "y": [p[1] for p in pairs],
        }
    }


def format_value(val):
    if isinstance(val, float):
        return f"{val:.1f}".rstrip("0").rstrip(".")
    return str(val)


def render_line(ax, series_data, config):
    for i, (name, values) in enumerate(series_data.items()):
        style = get_series_style(name, i, config)

        ax.plot(values["x"], values["y"], color=style["color"], linewidth=style["linewidth"])

        if config.get("auto_end_labels", True) and values["x"]:
            latest_val = values["y"][-1]

            add_end_label(
                ax,
                x=values["x"][-1],
                y=latest_val,
                label=format_value(latest_val),
                color=style["color"],
                dx=0.15,
            )


def render_scatter(ax, series_data, config):
    for i, (name, values) in enumerate(series_data.items()):
        style = get_series_style(name, i, config)

        ax.scatter(values["x"], values["y"], color=style["color"], s=style["marker_size"])

        if config.get("auto_end_labels", True) and values["x"]:
            latest_val = values["y"][-1]

            add_end_label(
                ax,
                x=values["x"][-1],
                y=latest_val,
                label=format_value(latest_val),
                color=style["color"],
                dx=0.15,
            )


def render_bar(ax, series_data, config):
    name = next(iter(series_data))
    values = series_data[name]
    style = get_series_style(name, 0, config)

    positions = list(range(len(values["x"])))

    ax.bar(positions, values["y"], color=style["color"], width=style["bar_width"])
    ax.set_xticks(positions)
    ax.set_xticklabels(values["x"])


def render_dot(ax, series_data, config):
    name = next(iter(series_data))
    values = series_data[name]
    style = get_series_style(name, 0, config)

    positions = list(range(len(values["x"]))

    ax.scatter(values["y"], positions, color=style["color"], s=style["marker_size"])
    ax.set_yticks(positions)
    ax.set_yticklabels(values["x"])
    ax.invert_yaxis()


def add_annotations(ax, config):
    for ref in config.get("reference_lines", []):
        add_reference_line(ax, **ref)

    for pt in config.get("highlight_points", []):
        highlight_point(ax, **pt)

    for lbl in config.get("end_labels", []):
        add_end_label(ax, **lbl)


def main():
    print("RUNNING CLEAN 538 RENDER")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    cfg = CHART_CONFIG
    data_path = REPO_ROOT / cfg.get("data_file", "data/test_chart.csv")

    if cfg.get("data_format") == "long":
        data = load_long_data(data_path, cfg["x_col"], cfg["series_col"], cfg["value_col"])
    else:
        data = load_wide_data(data_path, cfg["x_col"], cfg["y_col"])

    if cfg.get("chart_type") in {"bar", "dot"}:
        data = sort_single_series(data, cfg.get("sort_descending", True))

    fig, ax = plt.subplots(figsize=(12, 8.5))

    chart_type = cfg.get("chart_type", "line")

    if chart_type == "line":
        render_line(ax, data, cfg)
    elif chart_type == "scatter":
        render_scatter(ax, data, cfg)
    elif chart_type == "bar":
        render_bar(ax, data, cfg)
    elif chart_type == "dot":
        render_dot(ax, data, cfg)
    else:
        raise ValueError("Invalid chart type")

    add_annotations(ax, cfg)

    apply_538_template(
        ax,
        fig,
        title=cfg.get("title", ""),
        subtitle=cfg.get("subtitle", ""),
        source_text=cfg.get("source_text", ""),
        footer_left=cfg.get("footer_left", ""),
        vertical_gridlines=cfg.get("vertical_gridlines", False),
    )

    base_name = Path(cfg["data_file"]).stem
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    latest = REPO_ROOT / "output" / f"{base_name}.png"
    versioned = REPO_ROOT / "output" / f"{base_name}_{timestamp}.png"

    fig.savefig(latest, dpi=300)
    fig.savefig(versioned, dpi=300)
    plt.close(fig)

    print(f"Saved: {latest}")
    print(f"Saved: {versioned}")


if __name__ == "__main__":
    main()