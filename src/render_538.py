import matplotlib.pyplot as plt
import os
from chart_538 import apply_538_template


def main():
    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 12, 18, 20]

    # Create figure
    fig, ax = plt.subplots(figsize=(12.0, 8.5))

    # Plot
    ax.plot(x, y)

    # Apply 538 styling
    apply_538_template(ax, fig)

    # Save output
    filepath = "output/test_chart.png"
    plt.savefig(filepath, dpi=300, bbox_inches="tight")

    print(f"Chart saved to {filepath}")


if __name__ == "__main__":
    main()