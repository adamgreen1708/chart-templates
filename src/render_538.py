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


def main():
    print("RUNNING 538 BIG UPDATE RENDER")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    x = [2019, 2020, 2021, 2022, 2023, 2024]
    y = [48, 52, 55, 61, 58, 64]

    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    ax.plot(x, y, color="#1F8FA8", linewidth=3)

    add_reference_line(
        ax,
        y=50,
        label="Baseline",
        color="#999999",
        label_x="left",
        label_offset=0.5,
    )

    highlight_point(
        ax,
        x=2022,
        y=61,
        label="Peak test point",
        color="#C44E52",
        dx=0.15,
        dy=1.0,
    )

    add_end_label(
        ax,
        x=x[-1],
        y=y[-1],
        label="Latest",
        color="#1F8FA8",
        dx=0.15,
    )

    ax.set_xlim(min(x), max(x) + 0.8)

    title = "Test chart for locked 538 template"
    subtitle = "Now using reusable footer text, reference lines, highlights and end labels."

    apply_538_template(
        ax,
        fig,
        title=title,
        subtitle=subtitle,
        source_text="Source: test data",
        footer_left="Adam Green | coffeetableviz",
        vertical_gridlines=False,
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