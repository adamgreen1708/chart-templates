def add_reference_line(ax, y, label=None, color="#999999", linestyle="--", linewidth=1.5):
    """
    Add a horizontal reference line with optional label
    """
    ax.axhline(y, linestyle=linestyle, linewidth=linewidth, color=color)

    if label:
        x_min, _ = ax.get_xlim()
        ax.text(
            x_min,
            y,
            label,
            fontsize=10,
            color=color,
            ha="left",
            va="bottom"
        )


def highlight_point(ax, x, y, label=None, color="#000000"):
    """
    Highlight a key point
    """
    ax.scatter(x, y, color=color, zorder=5)

    if label:
        ax.text(
            x,
            y,
            label,
            fontsize=10,
            color=color,
            ha="left",
            va="bottom"
        )