CHART_CONFIG = {
    "data_file": "data/test_chart.csv",
    "chart_type": "line",
    "title": "Test chart for locked 538 template",
    "subtitle": "Standard config schema with reusable annotations and styling.",
    "source_text": "Source: test data",
    "footer_left": "Adam Green | coffeetableviz",
    "vertical_gridlines": False,
    "x_col": "x",
    "y_col": "y",
    "xlim_right_pad": 0.8,
    "series": [
        {
            "name": "Main",
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