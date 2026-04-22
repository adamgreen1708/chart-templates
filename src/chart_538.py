import matplotlib.pyplot as plt

BG = "#F3F4F6"
GRID = "#D9D9D9"
TEXT = "#111111"
SUBTEXT = "#555555"


def apply_538_template(
    ax,
    fig,
    title="",
    subtitle="",
    source_text="",
    footer_left="",
    vertical_gridlines=True,

    title_fontsize=24,
    subtitle_fontsize=15,
    footer_fontsize=10,

    title_y=0.93,
    subtitle_y=0.885,

    plot_top=0.78,
    plot_bottom=0.16,
    plot_left=0.12,
    plot_right=0.95,
):
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    # Clean axes
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#B0B0B0")

    # Ticks
    ax.tick_params(axis="x", colors=SUBTEXT, labelsize=12, length=0)
    ax.tick_params(axis="y", colors=SUBTEXT, labelsize=12, length=0)

    # Grid
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    if vertical_gridlines:
        ax.grid(axis="x", color=GRID, linewidth=0.35, alpha=0.6)

    # Layout
    fig.subplots_adjust(
        top=plot_top,
        bottom=plot_bottom,
        left=plot_left,
        right=plot_right,
    )

    # Title
    fig.text(
        plot_left,
        title_y,
        title,
        ha="left",
        va="top",
        fontsize=title_fontsize,
        fontweight="bold",
        color=TEXT,
    )

    # Subtitle
    fig.text(
        plot_left,
        subtitle_y,
        subtitle,
        ha="left",
        va="top",
        fontsize=subtitle_fontsize,
        color=SUBTEXT,
    )

    # Footer left
    fig.text(
        plot_left,
        0.06,
        footer_left,
        ha="left",
        va="bottom",
        fontsize=footer_fontsize,
        color=SUBTEXT,
    )

    # Source right
    fig.text(
        plot_right,
        0.06,
        source_text,
        ha="right",
        va="bottom",
        fontsize=footer_fontsize,
        color=SUBTEXT,
    )