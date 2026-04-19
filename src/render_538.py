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


def main():
    print("RUNNING CONFIG-DRIVEN 538 RENDER")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    # Plot all series
    for s in CHART_CONFIG["series"]:
        ax.plot(
            s["x"],
            s["y"],
            color=s.get("color", "#1F8FA8"),
            linewidth=s.get("linewidth", 3),
            label=s.get("name", ""),
        )

    # Reference lines
    for r in CHART_CONFIG.get("reference_lines", []):
        add_reference_line(
            ax,
            y=r["y"],
            label=r.get("label"),
            color=r.get("color", "#999999"),
            linestyle=r.get("linestyle", "--"),
            linewidth=r.get("linewidth", 1.5),
            label_x=r.get("label_x", "left"),
            label_offset=r.get("label_offset", 0.0),
        )

    # Highlight points
    for p in CHART_CONFIG.get("highlight_points", []):
        highlight_point(
            ax,
            x=p["x"],
            y=p["y"],
            label=p.get("label"),
            color=p.get("color", "#000000"),
            size=p.get("size", 45),
            dx=p.get("dx", 0),
            dy=p.get("dy", 0),
            ha=p.get("ha", "left"),
        )

    # End labels
    for e in CHART_CONFIG.get("end_labels", []):
        add_end_label(
            ax,
            x=e["x"],
            y=e["y"],
            label=e["label"],
            color=e.get("color", "#111111"),
            dx=e.get("dx", 0.2),
        )

    # Extend x-axis if requested
    all_x = []
    for s in CHART_CONFIG["series"]:
        all_x.extend(s["x"])
    ax.set_xlim(min(all_x), max(all_x) + CHART_CONFIG.get("xlim_right_pad", 0.0))

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