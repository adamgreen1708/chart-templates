import csv
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent


# -------------------------
# DATA LOADING
# -------------------------
def load_wide_data(csv_path, x_col, y_col):
    x_vals, y_vals = [], []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            x_vals.append(row[x_col])
            y_vals.append(float(row[y_col]))

    return x_vals, y_vals


# -------------------------
# RENDER
# -------------------------
def main():
    print("RUNNING LINKEDIN RENDER")

    from chart_config import CHART_CONFIG
    cfg = CHART_CONFIG

    data_path = REPO_ROOT / cfg["data_file"]

    x, y = load_wide_data(
        data_path,
        cfg["x_col"],
        cfg["y_col"]
    )

    # -------------------------
    # FIGURE (LINKEDIN STYLE)
    # -------------------------
    fig, ax = plt.subplots(
        figsize=(
            cfg.get("fig_width", 8),
            cfg.get("fig_height", 10),
        )
    )

    fig.patch.set_facecolor("#F3F4F6")
    ax.set_facecolor("#F3F4F6")

    # -------------------------
    # DOT PLOT (DEFAULT)
    # -------------------------
    positions = list(range(len(x)))
    ax.scatter(y, positions, s=60)

    ax.set_yticks(positions)
    ax.set_yticklabels(x)
    ax.invert_yaxis()

    # -------------------------
    # GRID + AXIS
    # -------------------------
    ax.grid(axis="x", color="#D9D9D9", linewidth=0.8)

    ax.tick_params(
        axis="both",
        labelsize=cfg.get("tick_label_fontsize", 12),
        length=0
    )

    # remove spines
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    ax.spines["bottom"].set_color("#B0B0B0")

    # -------------------------
    # TITLE + SUBTITLE
    # -------------------------
    fig.text(
        0.12,
        0.93,
        cfg.get("title", ""),
        fontsize=cfg.get("title_fontsize", 24),
        fontweight="bold",
        ha="left"
    )

    fig.text(
        0.12,
        0.885,
        cfg.get("subtitle", ""),
        fontsize=cfg.get("subtitle_fontsize", 15),
        ha="left"
    )

    # -------------------------
    # FOOTER
    # -------------------------
    fig.text(
        0.12,
        0.06,
        cfg.get("footer_left", ""),
        fontsize=cfg.get("footer_fontsize", 10),
        ha="left"
    )

    fig.text(
        0.95,
        0.06,
        cfg.get("source_text", ""),
        fontsize=cfg.get("footer_fontsize", 10),
        ha="right"
    )

    # -------------------------
    # LAYOUT
    # -------------------------
    fig.subplots_adjust(
        top=0.78,
        bottom=0.16,
        left=0.12,
        right=0.95
    )

    # -------------------------
    # SAVE
    # -------------------------
    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    base = Path(cfg["data_file"]).stem
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    fig.savefig(REPO_ROOT / f"output/{base}.png", dpi=300)
    fig.savefig(REPO_ROOT / f"output/{base}_{ts}.png", dpi=300)

    plt.close(fig)

    print("Chart saved successfully")


if __name__ == "__main__":
    main()