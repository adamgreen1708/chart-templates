import matplotlib.pyplot as plt
from src.chart_538 import apply_538_template


def create_chart():
    fig, ax = plt.subplots(figsize=(12.0, 8.5))
    ax.plot([1, 2, 3], [1, 2, 3])
    apply_538_template(ax, fig, title="Test", subtitle="Sub")
    return fig, ax


def test_figure_size():
    fig, _ = create_chart()
    w, h = fig.get_size_inches()
    assert round(w, 1) == 12.0
    assert round(h, 1) == 8.5


def test_background_colour():
    fig, ax = create_chart()

    # Check figure background
    assert fig.get_facecolor() != (1.0, 1.0, 1.0, 1.0)

    # Check axis background
    assert ax.get_facecolor() != (1.0, 1.0, 1.0, 1.0)


def test_gridlines_present():
    _, ax = create_chart()

    gridlines = ax.get_ygridlines()
    assert len(gridlines) > 0


def test_top_right_spines_removed():
    _, ax = create_chart()

    assert not ax.spines["top"].get_visible()
    assert not ax.spines["right"].get_visible()


def test_margins_applied():
    fig, _ = create_chart()

    left, right, bottom, top = fig.subplotpars.left, fig.subplotpars.right, fig.subplotpars.bottom, fig.subplotpars.top

    # These are approximate checks — not exact pixel-perfect
    assert left >= 0.05
    assert right <= 0.98
    assert top <= 0.90  # leaves space for title
    assert bottom >= 0.08


def test_title_position_exists():
    fig, _ = create_chart()

    texts = [t.get_text() for t in fig.texts]
    assert "Test" in texts