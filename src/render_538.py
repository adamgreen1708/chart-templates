import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt

# Allow imports when running from repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_538 import apply_538_template  # noqa: E402


def main():
    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    # Simple placeholder data for first successful render
    x = [2019, 2020, 2021, 2022, 2023, 2024]
    y = [48, 52, 55, 61, 58, 64]

    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    ax.plot(x, y, linewidth=2)

    title = "Test chart for locked 538 template"
    subtitle = "This is a workflow check to confirm GitHub Actions can render and save a PNG."

    apply_538_template(
        ax,
        fig,
        title=title,
        subtitle=subtitle,
        vertical_gridlines=False,
    )

    output_path = REPO_ROOT / "output" / "test_chart.png"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved chart to {output_path}")


if __name__ == "__main__":
    main()