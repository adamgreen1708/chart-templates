from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence, Tuple

from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


CANVAS_SIZE: Tuple[float, float] = (12.0, 8.5)
BACKGROUND_COLOR = "#F3F4F6"
GRIDLINE_COLOR = "#D1D5DB"
TEXT_COLOR = "#111827"
SUBTITLE_COLOR = "#4B5563"
SPINE_COLOR = "#D1D5DB"
DEFAULT_SERIES_COLOR = "#2E75B6"


@dataclass(frozen=True)
class Template538Config:
    """Configuration for the locked 538-style chart template."""

    canvas_size: Tuple[float, float] = CANVAS_SIZE
    background_color: str = BACKGROUND_COLOR
    gridline_color: str = GRIDLINE_COLOR
    text_color: str = TEXT_COLOR
    subtitle_color: str = SUBTITLE_COLOR
    spine_color: str = SPINE_COLOR
    default_series_color: str = DEFAULT_SERIES_COLOR

    # Figure margins implement the required generous padding.
    left_margin: float = 0.085
    right_margin: float = 0.975
    bottom_margin: float = 0.11
    top_margin: float = 0.79

    # Title block sits within safe bounds and clear of the plot area.
    title_x: float = 0.085
    title_y: float = 0.955
    subtitle_x: float = 0.085
    subtitle_y: float = 0.905

    title_fontsize: int = 22
    subtitle_fontsize: int = 12
    tick_fontsize: int = 11
    axis_label_fontsize: int = 12

    gridline_width: float = 0.8
    gridline_alpha: float = 0.7


DEFAULT_538_CONFIG = Template538Config()


def create_538_figure(
    *,
    config: Template538Config = DEFAULT_538_CONFIG,
) -> tuple[Figure, Axes]:
    """Create a figure and axes with the locked canvas and background."""
    fig, ax = plt.subplots(figsize=config.canvas_size)
    configure_538_layout(fig, ax, config=config)
    return fig, ax


def configure_538_layout(
    fig: Figure,
    ax: Axes,
    *,
    config: Template538Config = DEFAULT_538_CONFIG,
) -> None:
    """Apply locked canvas size, matching backgrounds, and padded figure margins."""
    fig.set_size_inches(*config.canvas_size, forward=True)
    fig.patch.set_facecolor(config.background_color)
    ax.set_facecolor(config.background_color)
    fig.subplots_adjust(
        left=config.left_margin,
        right=config.right_margin,
        bottom=config.bottom_margin,
        top=config.top_margin,
    )


def apply_538_template(
    ax: Axes,
    fig: Figure,
    *,
    vertical_gridlines: bool = False,
    config: Template538Config = DEFAULT_538_CONFIG,
) -> None:
    """
    Apply the locked 538 template styling rules to a matplotlib chart.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Chart axes to style.
    fig : matplotlib.figure.Figure
        Parent figure.
    vertical_gridlines : bool, default False
        Whether vertical gridlines should be shown.
    config : Template538Config, default DEFAULT_538_CONFIG
        Styling configuration for the locked template.
    """
    configure_538_layout(fig, ax, config=config)
    _style_axes(ax, vertical_gridlines=vertical_gridlines, config=config)


def add_538_titles(
    fig: Figure,
    *,
    title: str,
    subtitle: Optional[str] = None,
    config: Template538Config = DEFAULT_538_CONFIG,
) -> None:
    """Add left-aligned title and subtitle within safe figure bounds."""
    fig.text(
        config.title_x,
        config.title_y,
        title,
        ha="left",
        va="top",
        fontsize=config.title_fontsize,
        fontweight="bold",
        color=config.text_color,
    )

    if subtitle:
        fig.text(
            config.subtitle_x,
            config.subtitle_y,
            subtitle,
            ha="left",
            va="top",
            fontsize=config.subtitle_fontsize,
            color=config.subtitle_color,
        )


def plot_538_line(
    ax: Axes,
    x: Sequence[float],
    y: Sequence[float],
    *,
    color: str = DEFAULT_SERIES_COLOR,
    linewidth: float = 2.5,
    marker_size: float = 36,
) -> None:
    """Draw a simple reusable line series using the default 538-style accent color."""
    ax.plot(x, y, color=color, linewidth=linewidth)
    ax.scatter(x, y, color=color, s=marker_size, zorder=3)


def save_538_png(
    fig: Figure,
    output_path: str,
    *,
    dpi: int = 150,
    config: Template538Config = DEFAULT_538_CONFIG,
) -> None:
    """Export a PNG while preserving the locked ratio and canvas background."""
    fig.set_size_inches(*config.canvas_size, forward=True)
    fig.savefig(output_path, dpi=dpi, facecolor=config.background_color)


def _style_axes(
    ax: Axes,
    *,
    vertical_gridlines: bool,
    config: Template538Config,
) -> None:
    """Apply minimal axis styling and subtle gridlines."""
    ax.set_axisbelow(True)

    ax.grid(
        axis="y",
        color=config.gridline_color,
        linewidth=config.gridline_width,
        alpha=config.gridline_alpha,
    )

    if vertical_gridlines:
        ax.grid(
            axis="x",
            color=config.gridline_color,
            linewidth=config.gridline_width,
            alpha=config.gridline_alpha,
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(config.spine_color)
    ax.spines["bottom"].set_linewidth(0.8)

    ax.tick_params(
        axis="both",
        which="both",
        length=0,
        labelsize=config.tick_fontsize,
        colors=config.subtitle_color,
    )

    ax.xaxis.label.set_color(config.text_color)
    ax.yaxis.label.set_color(config.text_color)
    ax.xaxis.label.set_size(config.axis_label_fontsize)
    ax.yaxis.label.set_size(config.axis_label_fontsize)
