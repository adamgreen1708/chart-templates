import textwrap

BG = "#F2E04E"
GRID = "#D9D9D9"
TEXT = "#111111"
SUBTEXT = "#555555"


def _wrap_text(text: str, width: int, max_lines: int | None = None) -> str:
    if not text:
        return ""
    wrapped = textwrap.wrap(str(text), width=width)
    if max_lines is not None and len(wrapped) > max_lines:
        wrapped = wrapped[:max_lines]
        wrapped[-1] = wrapped[-1].rstrip(" .,;:") + "…"
    return "\n".join(wrapped)


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
    title_fontsize=22,
    subtitle_fontsize=13,
    tick_label_fontsize=12,
    footer_fontsize=10,
    title_wrap_width=28,
    subtitle_wrap_width=56,
    title_max_lines=2,
    subtitle_max_lines=2,
    title_x=0.10,
    title_y=0.93,
    subtitle_x=0.10,
    subtitle_y=0.855,
    footer_left_x=0.10,
    footer_right_x=0.90,
    footer_y=0.075,
    plot_top=0.72,
    plot_bottom=0.15,
    plot_left=0.10,
    plot_right=0.90,
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

    fig.subplots_adjust(
        top=plot_top,
        bottom=plot_bottom,
        left=plot_left,
        right=plot_right,
    )

    wrapped_title = _wrap_text(title, title_wrap_width, title_max_lines)
    wrapped_subtitle = _wrap_text(subtitle, subtitle_wrap_width, subtitle_max_lines)

    fig.text(
        title_x,
        title_y,
        wrapped_title,
        ha="left",
        va="top",
        fontsize=title_fontsize,
        fontweight="bold",
        color=text_color,
        linespacing=1.08,
    )

    fig.text(
        subtitle_x,
        subtitle_y,
        wrapped_subtitle,
        ha="left",
        va="top",
        fontsize=subtitle_fontsize,
        color=subtext_color,
        linespacing=1.15,
    )

    fig.text(
        footer_left_x,
        footer_y,
        footer_left,
        ha="left",
        va="bottom",
        fontsize=footer_fontsize,
        color=subtext_color,
    )

    fig.text(
        footer_right_x,
        footer_y,
        source_text,
        ha="right",
        va="bottom",
        fontsize=footer_fontsize,
        color=subtext_color,
    )
