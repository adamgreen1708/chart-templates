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
    default_color = config["series_style"].get("default_color", "#1F8FA8")
    default_linewidth = config["series_style"].get("default_linewidth", 3)
    palette = config["series_style"].get("palette", [default_color])

    style = {
        "color": palette[index % len(palette)] if palette else default_color,
        "linewidth": default_linewidth,
    }

    override = config.get("series_overrides", {}).get(series_name, {})
    style.update(override)
    return style


def main():
    print("RUNNING STABLE 538 RENDER V1.1")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    data_path = REPO_ROOT / CHART_CONFIG["data_file"]
    data_format = CHART_CONFIG.get("data_format", "wide")

    if data_format == "long":
        series_data = load_long_data(
            data_path,
            CHART_CONFIG["x_col"],
            CHART_CONFIG["series_col"],
            CHART_CONFIG["value_col"],
        )
    else:
        series_data = load_wide_data(
            data_path,
            CHART_CONFIG["x_col"],
            CHART_CONFIG["y_col"],
        )

    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    all_numeric_x = []

    # Plot series
    for idx, (series_name, values) in enumerate(series_data.items()):
        style = get_series_style(series_name, idx, CHART_CONFIG)

        ax.plot(
            values["x"],
            values["y"],
            color=style["color"],
            linewidth=style["linewidth"],
            label=series_name,
        )

        numeric_x = [v for v in values["x"] if isinstance(v, (int, float))]
        all_numeric_x.extend(numeric_x)

        # Auto end labels
        if CHART_CONFIG.get("auto_end_labels", False) and values["x"] and values["y"]:
            add_end_label(
                ax,
                x=values["x"][-1],
                y=values["y"][-1],
                label=series_name if data_format == "long" else "Latest",
                color=style["color"],
                dx=0.15,
            )

    # X-axis padding for numeric x
    if all_numeric_x:
        ax.set_xlim(
            min(all_numeric_x),
            max(all_numeric_x) + CHART_CONFIG.get("xlim_right_pad", 0.0),
        )

    # Reference lines
    for ref in CHART_CONFIG.get("reference_lines", []):
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

    # Highlight points
    for point in CHART_CONFIG.get("highlight_points", []):
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

    # Manual end labels
    for label in CHART_CONFIG.get("end_labels", []):
        add_end_label(
            ax,
            x=label["x"],
            y=label["y"],
            label=label["label"],
            color=label.get("color", "#111111"),
            dx=label.get("dx", 0.2),
        )

    apply_538_template(
        ax,
        fig,
        title=CHART_CONFIG["title"],
        subtitle=CHART_CONFIG["subtitle"],
        source_text=CHART_CONFIG["source_text"],
        footer_left=CHART_CONFIG["footer_left"],
        vertical_gridlines=CHART_CONFIG.get("vertical_gridlines", False),
    )

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    latest_path = REPO_ROOT / "output" / "test_chart.png"
    versioned_path = REPO_ROOT / "output" / f"test_chart_{timestamp}.png"

    fig.savefig(latest_path, dpi=300)
    fig.savefig(versioned_path, dpi=300)
    plt.close(fig)

    print(f"Saved latest chart to {latest_path}")
    print(f"Saved versioned chart to {versioned_path}")


if __name__ == "__main__":
    main()
