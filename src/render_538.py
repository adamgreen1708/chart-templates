print("RUNNING NEW RENDER VERSION V2")
import os
import sys
from chart_utils import add_reference_line, highlight_point
from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

# Allow imports when running from repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_538 import apply_538_template  # noqa: E402


def main():
    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    x = [2019, 2020, 2021, 2022, 2023, 2024]
    y = [48, 52, 55, 61, 58, 64]

    fig, ax = plt.subplots(figsize=(12.0, 8.5))
    ax.plot(x, y, color="#1F8FA8", linewidth=3)
# ---- REFERENCE LINES (TEST) ----
add_reference_line(
    ax,
    y=50,
    label="Baseline",
    color="#999999"
)

# ---- HIGHLIGHT POINT (TEST) ----
highlight_point(
    ax,
    x=x[-1],
    y=y[-1],
    label="Latest",
    color="#C44E52"
)
    title = "Test chart for locked 538 template"
    subtitle = "This is a workflow check to confirm GitHub Actions can render and save a PNG."

    apply_538_template(
        ax,
        fig,
        title=title,
        subtitle=subtitle,
        vertical_gridlines=False,
    )

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    latest_path = REPO_ROOT / "output" / "test_chart.png"
    versioned_path = REPO_ROOT / "output" / f"test_chart_{timestamp}.png"

    fig.savefig(latest_path, dpi=300, bbox_inches="tight")
    fig.savefig(versioned_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved latest chart to {latest_path}")
    print(f"Saved versioned chart to {versioned_path}")


if __name__ == "__main__":
    main()