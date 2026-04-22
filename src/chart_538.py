import textwrap

BG = "#F3F4F6"
GRID = "#D9D9D9"
TEXT = "#111111"
SUBTEXT = "#555555"


def _wrap_text(text, width):
    if not text:
        return ""
    return textwrap.fill(str(text), width=width)


def apply_538_template(
    ax,
    fig,
    title="",
    subtitle="",
    source_text="",
    footer_left="",
    vertical_gridlines=True,
    fig_bg=BG,
    plot_bg=BG,
    text_color=TEXT,
    subtext_color=SUBTEXT,
    grid_color=GRID,
    title_fontsize=24,
    subtitle_fontsize=14,
    tick_label_fontsize=13,
    footer_fontsize=10,
    title_wrap_width=34,
    subtitle_wrap_width=72,
    title_x=0.14,
    title_y=0.955,
    subtitle_x=0.14,
    subtitle_y=0.89,
    footer_left_x=0.14,
    footer_right_x=0.96,
    footer_y=0.06,
    plot_top=0.74,
    plot_bottom=0.16,
    plot_left=0.14,
    plot_right=0.96,
):
    fig.patch.set_facecolor(fig_bg)
    ax.set_facecolor(plot_bg)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#B0B0B0")
    ax.tick_params(axis="x", colors=subtext_color, labelsize=tick_label_fontsize, length=0)
    ax.tick_params(axis="y", colors=subtext_color, labelsize=tick_label_fontsize, length=0)
    ax.grid(axis="y", color=grid_color, linewidth=0.8)
    if vertical_gridlines:
        ax.grid(axis="x", color=grid_color, linewidth=0.35, alpha=0.6)
    fig.subplots_adjust(top=plot_top, bottom=plot_bottom, left=plot_left, right=plot_right)
    fig.text(title_x, title_y, _wrap_text(title, title_wrap_width), ha="left", va="top", fontsize=title_fontsize, fontweight="bold", color=text_color)
    fig.text(subtitle_x, subtitle_y, _wrap_text(subtitle, subtitle_wrap_width), ha="left", va="top", fontsize=subtitle_fontsize, color=subtext_color)
    fig.text(footer_left_x, footer_y, footer_left, ha="left", va="bottom", fontsize=footer_fontsize, color=subtext_color)
    fig.text(footer_right_x, footer_y, source_text, ha="right", va="bottom", fontsize=footer_fontsize, color=subtext_color)
