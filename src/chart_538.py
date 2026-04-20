import matplotlib.pyplot as plt
import textwrap


def apply_538_template(
    ax,
    fig,
    title="",
    subtitle="",
    source_text="",
    footer_left="",
    vertical_gridlines=True,
):
    """
    Apply the locked 538/coffeetableviz template styling.

    Notes
    -----
    - Vertical gridlines are now always on by design.
    - Outer whitespace is intentionally generous and consistent.
    - Footer is locked:
        left  = footer_left
        right = source_text
    """

    bg = "#F3F4F6"
    title_color = "#111111"
    subtitle_color = "#555555"
    footer_color = "#666666"
    tick_color = "#333333"
    grid_y = "#D0D0D0"
    grid_x = "#E6E6E6"

    # --- Figure / axes background ---
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # --- Remove spines ---
    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)

    # --- Gridlines ---
    # Always on: stronger horizontal, lighter vertical
    ax.grid(axis="y", color=grid_y, linewidth=1.0)
    ax.grid(axis="x", color=grid_x, linewidth=0.8)

    # --- Tick styling ---
    ax.tick_params(
        axis="both",
        which="both",
        length=0,
        labelsize=10,
        colors=tick_color,
        pad=6,
    )

    # --- Title ---
    if title:
        fig.text(
            0.10,
            0.945,
            title,
            fontsize=20,
            fontweight="bold",
            ha="left",
            va="top",
            color=title_color,
        )

    # --- Subtitle ---
    if subtitle:
        wrap_width = max(58, int(fig.get_figwidth() * 8.5))
        wrapped_subtitle = "\n".join(textwrap.wrap(subtitle, width=wrap_width))

        fig.text(
            0.10,
            0.892,
            wrapped_subtitle,
            fontsize=12,
            color=subtitle_color,
            ha="left",
            va="top",
            linespacing=1.25,
        )

    # --- Footer ---
    if footer_left:
        fig.text(
            0.10,
            0.050,
            footer_left,
            fontsize=9,
            color=footer_color,
            ha="left",
            va="bottom",
        )

    if source_text:
        fig.text(
            0.90,
            0.050,
            source_text,
            fontsize=9,
            color=footer_color,
            ha="right",
            va="bottom",
        )

    # --- Layout spacing ---
    # Equal-feeling generous whitespace around the full chart system
    plt.subplots_adjust(
        left=0.10,
        right=0.90,
        top=0.79,
        bottom=0.18,
    )