CHART_CONFIG = {
    "title": "Test chart for locked 538 template",
    "subtitle": "Now using a config-driven 538 renderer with reusable annotations.",
    "footer_left": "Adam Green | coffeetableviz",
    "source_text": "Source: test data",
    "vertical_gridlines": False,
    "xlim_right_pad": 0.8,
    "series": [
        {
            "name": "Main series",
            "x": [2019, 2020, 2021, 2022, 2023, 2024],
            "y": [48, 52, 55, 61, 58, 64],
            "color": "#1F8FA8",
            "linewidth": 3,
        }
    ],
    "reference_lines": [
        {
            "y": 50,
            "label": "Baseline",
            "color": "#999999",
            "linestyle": "--",
            "linewidth": 1.5,
            "label_x": "left",
            "label_offset": 0.5,
        }
    ],
    "highlight_points": [
        {
            "x": 2022,
            "y": 61,
            "label": "Peak test point",
            "color": "#C44E52",
            "dx": 0.15,
            "dy": 1.0,
            "ha": "left",
            "size": 45,
        }
    ],
    "end_labels": [
        {
            "x": 2024,
            "y": 64,
            "label": "Latest",
            "color": "#1F8FA8",
            "dx": 0.15,
        }
    ],
}