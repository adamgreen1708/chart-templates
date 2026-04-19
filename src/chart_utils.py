def add_reference_line(
    ax,
    y,
    label=None,
    color="#999999",
    linestyle="--",
    linewidth=1.5,
    label_x="left",
    label_offset=0.0,
):
    """
    Add a horizontal reference line with an optional label.
    """
    ax.axhline(y, linestyle=linestyle, linewidth=linewidth, color=color)

    if label:
        x_min, x_max = ax.get_xlim()

        if label_x == "right":
            x_pos = x_max
            ha = "right"
        else:
            x_pos = x_min
            ha = "left"

        ax.text(
            x_pos,
            y + label_offset,
            label,
            fontsize=10,
            color=color,
            ha=ha,
            va="bottom",
        )


def highlight_point(
    ax,
    x,
    y,
    label=None,
    color="#000000",
    size=45,
    dx=0,
    dy=0,
    ha="left",
):
    """
    Highlight a single point and optionally label it.
    """
    ax.scatter(x, y, color=color, s=size, zorder=5)

    if label:
        ax.text(
            x + dx,
            y + dy,
            label,
            fontsize=10,
            color=color,
            ha=ha,
            va="bottom",
        )


def add_end_label(ax, x, y, label, color="#111111", dx=0.2):
    """
    Add a label just to the right of the end of a series.
    """
    ax.text(
        x + dx,
        y,
        label,
        fontsize=10,
        color=color,
        ha="left",
        va="center",
    )