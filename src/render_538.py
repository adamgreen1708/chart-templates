from pathlib import Path

from chart_538 import (
    apply_538_template,
    create_538_figure,
    add_538_titles,
    plot_538_line,
    save_538_png,
)


def main() -> None:
    """Render a simple example line chart using the 538 template."""

    # Example generic data (not hardcoded to a specific domain)
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

    output_dir = Path(__file__).resolve().parent.parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "example_538.png"
    save_538_png(fig, str(output_path))

    print(f"Saved chart to {output_path}")


if __name__ == "__main__":
    main()
