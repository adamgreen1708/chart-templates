import csv
import os
import sys
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


def load_xy_data(csv_path, x_col, y_col):
    """
    Load two columns from a CSV file.
    Attempts numeric conversion where possible.
    """
    x_vals = []
    y_vals = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x_raw = row[x_col]
            y_raw = row[y_col]

            try:
                x_val = float(x_raw)
                if x_val.is_integer():
                    x_val = int(x_val)
            except ValueError:
                x_val = x_raw

            try:
                y_val = float(y_raw)
                if y_val.is_integer():
                    y_val = int(y_val)
            except ValueError as exc:
                raise ValueError(f"Non-numeric y value found: {y_raw}") from exc

            x_vals.append(x_val)
            y_vals.append(y_val)

    return x_vals, y_vals


def main():
    print("RUNNING CONFIG-DRIVEN 538 RENDER V1")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    data_path = REPO_ROOT / CHART_CONFIG["data_file"]
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    x_vals, y_vals = load_xy_data(data_path, x_col, y_col)

    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    # ---- PLOT SERIES ----
    for series in CHART_CONFIG["series"]:
        ax.plot(
            x_vals,
            y_vals,
            color=series.get("color", "#1F8FA8"),
            linewidth=series.get("linewidth", 3),
            label=series.get("name", "Series"),
        )

    # ---- AXIS RANGE ----
    if x_vals and isinstance(x_vals[0], (int, float)):
        ax.set_xlim(
            min(x_vals),
            max(x_vals) + CHART_CONFIG.get("xlim_right_pad", 0.0),
        )

    # ---- REFERENCE LINES ----
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

    # ---- HIGHLIGHT POINTS ----
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

    # ---- END LABELS ----
    for label in CHART_CONFIG.get("end_labels", []):
        add_end_label(
            ax,
            x=label["x"],
            y=label["y"],
            label=label["label"],
            color=label.get("color", "#111111"),
            dx=label.get("dx", 0.2),
        )

    # ---- APPLY TEMPLATE ----
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