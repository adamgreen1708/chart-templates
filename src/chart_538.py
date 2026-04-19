def apply_538_template(ax, fig, *, title="", subtitle="", vertical_gridlines=False):
    """
    Apply a minimal locked 538-style template.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Chart axes to style.
    fig : matplotlib.figure.Figure
        Parent figure.
    title : str, optional
        Chart title.
    subtitle : str, optional
        Chart subtitle.
    vertical_gridlines : bool, default False
        Whether vertical gridlines should be shown.
    """
    bg = "#F3F4F6"

    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # Safe margins
    fig.subplots_adjust(left=0.08, right=0.97, top=0.82, bottom=0.11)

    # Title and subtitle
    if title:
        fig.text(
            0.08,
            0.94,
            title,
            ha="left",
            va="top",
            fontsize=18,
            fontweight="bold",
        )

    if subtitle:
        fig.text(
            0.08,
            0.90,
            subtitle,
            ha="left",
            va="top",
            fontsize=11,
        )

    # Gridlines
    ax.grid(axis="y", linestyle="-", linewidth=0.6, alpha=0.3)
    if vertical_gridlines:
        ax.grid(axis="x", linestyle="-", linewidth=0.6, alpha=0.3)

    # Minimal spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Clean ticks
    ax.tick_params(axis="both", labelsize=10)