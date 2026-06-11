import matplotlib.pyplot as plt

from src.chart_538 import BG, apply_538_template
from src.render_538 import _axis_formatter, _to_float


# ---- TEMPLATE CORE ----


def test_template_runs_with_square_canvas_defaults():
    fig, ax = plt.subplots(figsize=(8.0, 8.0))
    ax.plot([1, 2, 3], [1, 2, 3])

    apply_538_template(
        ax,
        fig,
        title="Test",
        subtitle="Sub",
        source_text="Source",
        footer_left="Footer",
    )

    width, height = fig.get_size_inches()
    assert width == 8.0
    assert height == 8.0
    assert fig is not None


def test_background_not_white():
    fig, ax = plt.subplots(figsize=(8.0, 8.0))
    apply_538_template(ax, fig)

    assert fig.get_facecolor() != (1.0, 1.0, 1.0, 1.0)
    assert ax.get_facecolor() != (1.0, 1.0, 1.0, 1.0)
    assert fig.get_facecolor() == plt.matplotlib.colors.to_rgba(BG)


def test_horizontal_gridlines_default_on_vertical_off():
    fig, ax = plt.subplots(figsize=(8.0, 8.0))
    ax.plot([1, 2, 3], [1, 2, 3])

    apply_538_template(ax, fig)

    assert any(line.get_visible() for line in ax.get_ygridlines())
    assert not any(line.get_visible() for line in ax.get_xgridlines())


def test_vertical_gridlines_can_be_enabled():
    fig, ax = plt.subplots(figsize=(8.0, 8.0))
    ax.plot([1, 2, 3], [1, 2, 3])

    apply_538_template(ax, fig, vertical_gridlines=True)

    assert any(line.get_visible() for line in ax.get_xgridlines())


# ---- RENDERER HELPERS ----


def test_to_float_handles_symbols_and_blanks():
    assert _to_float("$1,200") == 1200.0
    assert _to_float("45%") == 45.0
    assert _to_float(12) == 12.0
    assert _to_float("") is None


def test_axis_formatter_supports_billions():
    formatter = _axis_formatter("billions")
    assert formatter(13, None) == "$13bn"
