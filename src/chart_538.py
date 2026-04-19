import matplotlib.pyplot as plt


def apply_538_template(
    ax,
    fig,
    *,
    title="",
    subtitle="",
    source_text="Source: data",
    footer_left="Adam Green | coffeetableviz",
    vertical_gridlines=False,
):
    """
    Apply the locked 538-style layout to a matplotlib chart.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Chart axes.
    fig : matplotlib.figure.Figure
        Figure object.
    title : str
        Main chart title.
    subtitle : str
        Chart subtitle.
    source_text : str
        Footer source text shown at bottom-right.
    footer_left : str
        Footer text shown at bottom-left.
    vertical_gridlines : bool
        Whether to show vertical gridlines.
    """

    # ---- COLOURS ----
    bg = "#F3F4F6"
    header_line = "#222222"
    footer_bg = "#E6E6E6"
    title_color = "#111111"
    subtitle_color = "#333333"
    axis_color = "#555555"

    # ---- BACKGROUND ----
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # ---- HEADER RULE ----
    fig.lines.append(
        plt.Line2D(
            [0.05, 0.95],
            [0.965, 0.965],
            transform=fig.transFigure,
            color=header_line,
            linewidth=3,
        )
    )

    # ---- HEADER TEXT ----
    if title:
        fig.text(
            0.07,
            0.92,
            title,
            ha="left",
            va="top",
            fontsize=22,
            fontweight="bold",
            color=title_color,
        )

    if subtitle:
        fig.text(
            0.07,
            0.865,
            subtitle,
            ha="left",
            va="top",
            fontsize=13,
            color=subtitle_color,
        )

    # ---- CHART AREA ----
    fig.subplots_adjust(
        left=0.08,
        right=0.96,
        top=0.70,
        bottom=0.22,
    )

    # ---- GRIDLINES ----
    ax.grid(axis="y", linestyle="-", linewidth=0.5, alpha=0.10)
    if vertical_gridlines:
        ax.grid(axis="x", linestyle="-", linewidth=0.5, alpha=0.10)

    # ---- SPINES ----
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_alpha(0.15)
    ax.spines["bottom"].set_alpha(0.15)

    # ---- TICKS ----
    ax.tick_params(axis="both", labelsize=10, length=0, colors=axis_color)

    # ---- FOOTER BAR ----
    footer = plt.Rectangle(
        (0, 0),
        1,
        0.08,
        transform=fig.transFigure,
        color=footer_bg,
        zorder=-1,
    )
    fig.patches.append(footer)

    fig.text(0.07, 0.035, footer_left, fontsize=11, color="#333333")
    fig.text(0.75, 0.035, source_text, fontsize=11, color="#333333")