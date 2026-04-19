def apply_538_template(ax, fig, *, title="", subtitle="", vertical_gridlines=False):
    bg = "#F3F4F6"

    # Background
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # ---- LAYOUT ----
    fig.subplots_adjust(
        left=0.10,
        right=0.96,
        top=0.72,
        bottom=0.15
    )

    # ---- TITLE BLOCK ----
    if title:
        fig.text(
            0.10, 0.88,
            title,
            ha="left",
            va="top",
            fontsize=20,
            fontweight="bold",
            color="#111111"
        )

    if subtitle:
        fig.text(
            0.10, 0.83,
            subtitle,
            ha="left",
            va="top",
            fontsize=11,
            color="#555555"
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
    ax.tick_params(
        axis="both",
        labelsize=9,
        length=0,
        colors="#555555"
    )