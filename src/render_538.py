from pathlib import Path

import matplotlib.pyplot as plt

from chart_538 import apply_538_template, create_538_figure, add_538_titles, plot_538_line


def main() -> None:
    """Render a simple example line chart using the 538 template."""

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    x = [1, 2, 3, 4, 5]
    y = [10, 14, 13, 17, 20]

    fig, ax = create_538_figure()
    plot_538_line(ax, x, y)
    apply_538_template(ax, fig)

    add_538_titles(
        fig,
        title="Example 538-style chart",
        subtitle="Reusable matplotlib template with locked layout and styling",
    )

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")

    output_path = output_dir / "test_chart.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")

    print(f"Chart saved to {output_path}")


if __name__ == "__main__":
    main()
