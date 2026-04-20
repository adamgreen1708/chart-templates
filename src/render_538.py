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
    x_vals = []
    y_vals = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x_vals.append(_coerce_value(row[x_col]))
            y_val = _coerce_value(row[y_col])

            if not isinstance(y_val, (int, float)):
                raise ValueError(f"Non-numeric y value found: {row[y_col]}")

            y_vals.append(y_val)

    return {"Main": {"x": x_vals, "y": y_vals}}


def load_long_data(csv_path, x_col, series_col, value_col):
    grouped = defaultdict(lambda: {"x": [], "y": []})

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            series_name = row[series_col]
            x_val = _coerce_value(row[x_col])
            y_val = _coerce_value(row[value_col])

            if not isinstance(y_val, (int, float)):
                raise ValueError(f"Non-numeric value found: {row[value_col]}")

            grouped[series_name]["x"].append(x_val)
            grouped[series_name]["y"].append(y_val)

    return dict(grouped)


def get_series_style(series_name, index, config):
    style_cfg = config.get("series_style", {})
    default_color = style_cfg.get("default_color", "#1F8FA8")
    default_linewidth = style_cfg.get("default_linewidth", 3)
    default_bar_width = style_cfg.get("default_bar_width", 0.7)
    default_marker_size = style_cfg.get("default_marker_size", 55)
    palette = style_cfg.get("palette", [default_color])

    style = {
        "color": palette[index % len(palette)] if palette else default_color,
        "linewidth": default_linewidth,
        "bar_width": default_bar_width,
        "marker_size": default_marker_size,
    }

    override = config.get("series_overrides", {}).get(series_name, {})
    style.update(override)
    return style


def sort_single_series_for_rank_chart(series_data, descending=True):
    if len(series_data) != 1:
        return series_data

    series_name = next(iter(series_data))
    values = series_data[series_name]

    pairs = list(zip(values["x"], values["y"]))
    pairs.sort(key=lambda t: t[1], reverse=descending)

    sorted_x = [p[0] for p in pairs]
    sorted_y = [p[1] for p in pairs]

    return {series_name: {"x": sorted_x, "y": sorted_y}}


def is_all_numeric(values):
    return all(isinstance(v, (int, float)) for v in values)


def render_line(ax, series_data, config):
    all_numeric_x = []

    for idx, (series_name, values) in enumerate(series_data.items()):
        style = get_series_style(series_name, idx, config)

        ax.plot(
            values["x"],
            values["y"],
            color=style["color"],
            linewidth=style["linewidth"],
            label=series_name,
        )

        numeric_x = [v for v in values["x"] if isinstance(v, (int, float))]
        all_numeric_x.extend(numeric_x)

        if config.get("auto_end_labels", False) and values["x"] and values["latest_val = values["y"][-1]

# format nicely (int vs float)
if isinstance(latest_val, float):
    label_text = f"{latest_val:.1f}".rstrip("0").rstrip(".")
else:
    label_text = str(latest_val)

add_end_label(
    ax,
    x=values["x"][-1],
    y=latest_val,
    label=label_text,
    color=style["color"],
    dx=0.15,
)

    if all_numeric_x:
        ax.set_xlim(
            min(all_numeric_x),
            max(all_numeric_x) + config.get("xlim_right_pad", 0.0),
        )


def render_scatter(ax, series_data, config):
    all_numeric_x = []

    for idx, (series_name, values) in enumerate(series_data.items()):
        style = get_series_style(series_name, idx, config)

        ax.scatter(
            values["x"],
            values["y"],
            color=style["color"],
            s=style["marker_size"],
            label=series_name,
            zorder=4,
        )

        numeric_x = [v for v in values["x"] if isinstance(v, (int, float))]
        all_numeric_x.extend(numeric_x)

        if config.get("auto_end_labels", False) and values["x"] and values["y"]:
            add_end_label(
                ax,
                x=values["x"][-1],
                y=values["y"][-1],
                label=series_name if len(series_data) > 1 else "Latest",
                color=style["color"],
                dx=0.15,
            )

    if all_numeric_x:
        ax.set_xlim(
            min(all_numeric_x),
            max(all_numeric_x) + config.get("xlim_right_pad", 0.0),
        )


def render_bar(ax, series_data, config):
    series_name = next(iter(series_data))
    values = series_data[series_name]
    style = get_series_style(series_name, 0, config)

    x_vals = values["x"]
    y_vals = values["y"]

    if is_all_numeric(x_vals):
        ax.bar(
            x_vals,
            y_vals,
            color=style["color"],
            width=style["bar_width"],
        )
        ax.set_xlim(
            min(x_vals) - style["bar_width"],
            max(x_vals) + style["bar_width"] + config.get("xlim_right_pad", 0.0),
        )
    else:
        positions = list(range(len(x_vals)))
        ax.bar(
            positions,
            y_vals,
            color=style["color"],
            width=style["bar_width"],
        )
        ax.set_xticks(positions)
        ax.set_xticklabels(x_vals)


def render_dot(ax, series_data, config):
    series_name = next(iter(series_data))
    values = series_data[series_name]
    style = get_series_style(series_name, 0, config)

    x_vals = values["x"]
    y_vals = values["y"]

    positions = list(range(len(x_vals)))

    ax.scatter(
        y_vals,
        positions,
        color=style["color"],
        s=style["marker_size"],
        zorder=4,
    )

    ax.set_yticks(positions)
    ax.set_yticklabels(x_vals)
    ax.invert_yaxis()

    max_y = max(y_vals) if y_vals else 0
    ax.set_xlim(0, max_y + config.get("xlim_right_pad", 0.0))

    if config.get("auto_end_labels", False):
        for pos, y_val in zip(positions, y_vals):
            ax.text(
                y_val + 0.1,
                pos,
                f"{y_val:g}",
                fontsize=10,
                color=style["color"],
                ha="left",
                va="center",
            )


def add_annotations(ax, config):
    for ref in config.get("reference_lines", []):
        add_reference_line(
            ax,
            y=ref["y"],
            label=ref.get("label"),
            color=ref.get("color", "#999999"),
            linestyle=ref.get("linestyle", "--"),
            linewidth=ref.get("linewidth", 1.5),
            label_x=ref.get("label_x", "left"),
            label_offset=ref.get("label_offset", 0.0),
        )

    for point in config.get("highlight_points", []):
        highlight_point(
            ax,
            x=point["x"],
            y=point["y"],
            label=point.get("label"),
            color=point.get("color", "#000000"),
            size=point.get("size", 45),
            dx=point.get("dx", 0),
            dy=point.get("dy", 0),
            ha=point.get("ha", "left"),
        )

    for label in config.get("end_labels", []):
        add_end_label(
            ax,
            x=label["x"],
            y=label["y"],
            label=label["label"],
            color=label.get("color", "#111111"),
            dx=label.get("dx", 0.2),
        )


def main():
    print("RUNNING GENERIC 538 RENDER V1.2")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    data_path = REPO_ROOT / CHART_CONFIG.get("data_file", "data/test_chart.csv")
    data_format = CHART_CONFIG.get("data_format", "wide")
    chart_type = CHART_CONFIG.get("chart_type", "line")
    sort_desc = CHART_CONFIG.get("sort_descending", True)

    if data_format == "long":
        series_data = load_long_data(
            data_path,
            CHART_CONFIG.get("x_col", "x"),
            CHART_CONFIG.get("series_col", "series"),
            CHART_CONFIG.get("value_col", "value"),
        )
    else:
        series_data = load_wide_data(
            data_path,
            CHART_CONFIG.get("x_col", "x"),
            CHART_CONFIG.get("y_col", "y"),
        )

    if chart_type in {"bar", "dot"}:
        series_data = sort_single_series_for_rank_chart(
            series_data,
            descending=sort_desc,
        )

    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    if chart_type == "line":
        render_line(ax, series_data, CHART_CONFIG)
    elif chart_type == "scatter":
        render_scatter(ax, series_data, CHART_CONFIG)
    elif chart_type == "bar":
        render_bar(ax, series_data, CHART_CONFIG)
    elif chart_type == "dot":
        render_dot(ax, series_data, CHART_CONFIG)
    else:
        raise ValueError(
            f"Unsupported chart_type: {chart_type}. "
            "Use one of: line, bar, scatter, dot."
        )

    add_annotations(ax, CHART_CONFIG)

    apply_538_template(
        ax,
        fig,
        title=CHART_CONFIG.get("title", ""),
        subtitle=CHART_CONFIG.get("subtitle", ""),
        source_text=CHART_CONFIG.get("source_text", "Source: data"),
        footer_left=CHART_CONFIG.get("footer_left", "Adam Green | coffeetableviz"),
        vertical_gridlines=CHART_CONFIG.get("vertical_gridlines", False),
    )

    data_file = CHART_CONFIG.get("data_file", "data/test_chart.csv")
    base_name = Path(data_file).stem

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    latest_path = REPO_ROOT / "output" / f"{base_name}.png"
    versioned_path = REPO_ROOT / "output" / f"{base_name}_{timestamp}.png"

    fig.savefig(latest_path, dpi=300)
    fig.savefig(versioned_path, dpi=300)
    plt.close(fig)

    print(f"Saved latest chart to {latest_path}")
    print(f"Saved versioned chart to {versioned_path}")


if __name__ == "__main__":
    main()