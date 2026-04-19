from __future__ import annotations


BACKGROUND = "#F3F4F6"
TEXT_COLOR = "#111827"
SUBTITLE_COLOR = "#4B5563"
GRID_COLOR = "#D1D5DB"
SPINE_COLOR = "#D1D5DB"

CANVAS_WIDTH = 12.0
CANVAS_HEIGHT = 8.5

LEFT_MARGIN = 0.08
RIGHT_MARGIN = 0.97
TOP_MARGIN = 0.81
BOTTOM_MARGIN = 0.11

TITLE_X = 0.08
TITLE_Y = 0.955
SUBTITLE_X = 0.08
SUBTITLE_Y = 0.905

TITLE_SIZE = 18
SUBTITLE_SIZE = 11
TICK_SIZE = 10


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
    _set_canvas(fig, ax)
    _set_layout(fig)
    _add_titles(fig, title=title, subtitle=subtitle)
    _style_gridlines(ax, vertical_gridlines=vertical_gridlines)
    _style_spines(ax)
    _style_ticks(ax)


def _set_canvas(fig, ax):
    """Preserve locked canvas compatibility and the full grey background."""
    fig.set_size_inches(CANVAS_WIDTH, CANVAS_HEIGHT, forward=True)
    fig.patch.set_facecolor(BACKGROUND)
    ax.set_facecolor(BACKGROUND)


def _set_layout(fig):
    """Apply generous margins that leave safe room for titles above the plot."""
    fig.subplots_adjust(
        left=LEFT_MARGIN,
        right=RIGHT_MARGIN,
        top=TOP_MARGIN,
        bottom=BOTTOM_MARGIN,
    )


def _add_titles(fig, *, title, subtitle):
    """Add left-aligned title text with safer vertical separation."""
    if title:
        fig.text(
            TITLE_X,
            TITLE_Y,
            title,
            ha="left",
            va="top",
            fontsize=TITLE_SIZE,
            fontweight="bold",
            color=TEXT_COLOR,
        )

    if subtitle:
        fig.text(
            SUBTITLE_X,
            SUBTITLE_Y,
            subtitle,
            ha="left",
            va="top",
            fontsize=SUBTITLE_SIZE,
            color=SUBTITLE_COLOR,
        )


def _style_gridlines(ax, *, vertical_gridlines):
    """Keep horizontal gridlines subtle and vertical ones opt-in only."""
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=GRID_COLOR, linestyle="-", linewidth=0.7, alpha=0.55)

    if vertical_gridlines:
        ax.grid(axis="x", color=GRID_COLOR, linestyle="-", linewidth=0.7, alpha=0.55)


def _style_spines(ax):
    """Preserve minimal spine styling."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(SPINE_COLOR)
    ax.spines["bottom"].set_linewidth(0.8)


def _style_ticks(ax):
    """Keep axis labels and ticks clean and understated."""
    ax.tick_params(axis="both", which="both", length=0, labelsize=TICK_SIZE, colors=SUBTITLE_COLOR)
