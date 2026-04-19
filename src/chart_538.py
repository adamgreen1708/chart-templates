def apply_538_template(ax, fig, *, title="", subtitle="", vertical_gridlines=False):
    bg = "#F3F4F6"

    # Background
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # ---- LAYOUT SYSTEM (LOCKED) ----
    # Top = title block
    # Middle = plot
    # Bottom = axis

    fig.subplots_adjust(
        left=0.08,
        right=0.98,
        top=0.78,   # pushes plot DOWN (more header space)
        bottom=0.12
    )

    # ---- TITLE BLOCK (EXPLICIT POSITIONS) ----
    if title:
        fig.text(
            0.08, 0.94,
            title,
            ha="left",
            va="top",
            fontsize=20,
            fontweight="bold"
        )

    if subtitle:
        fig.text(
            0.08, 0.89,
            subtitle,
            ha="left",
            va="top",
            fontsize=12,
            alpha=0.85
        )

    # ---- GRIDLINES ----
    ax.grid(axis="y", linestyle="-", linewidth=0.6, alpha=0.25)
    if vertical_gridlines:
        ax.grid(axis="x", linestyle="-", linewidth=0.6, alpha=0.25)

    # ---- AXIS CLEANUP ----
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # soften remaining spines
    ax.spines["left"].set_alpha(0.3)
    ax.spines["bottom"].set_alpha(0.3)

    # ---- TICKS (QUIETER) ----
    ax.tick_params(
        axis="both",
        labelsize=10,
        length=0
    )