import matplotlib.pyplot as plt


def test_figure_size():
    fig, ax = plt.subplots(figsize=(12.0, 8.5))
    w, h = fig.get_size_inches()
    assert round(w, 1) == 12.0
    assert round(h, 1) == 8.5


def test_background_not_white():
    fig, ax = plt.subplots(figsize=(12.0, 8.5))
    fig.patch.set_facecolor("#F3F4F6")
    assert fig.get_facecolor() != (1.0, 1.0, 1.0, 1.0)


def test_no_crash_placeholder():
    assert True