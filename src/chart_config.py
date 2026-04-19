CHART_CONFIG = {
    "data_file": "data/test_chart.csv",
    "data_format": "wide",  # "wide" = x,y ; "long" = x,series,value
    "chart_type": "line",   # "line", "bar", "scatter", "dot"

    "title": "Test chart for locked 538 template",
    "subtitle": "Stable v1.2 renderer with line, bar, scatter, and dot support.",
    "source_text": "Source: test data",
    "footer_left": "Adam Green | coffeetableviz",
    "vertical_gridlines": False,

    # Column mapping
    "x_col": "x",
    "y_col": "y",
    "series_col": "series",
    "value_col": "value",

    # Layout / behaviour
    "xlim_right_pad": 0.8,
    "sort_descending": True,

    # Default style
    "series_style": {
        "default_color": "#1F8FA8",
        "default_linewidth": 3,
        "default_bar_width": 0.7,
        "default_marker_size": 55,
        "palette": ["#1F8FA8", "#C44E52", "#7A7A7A", "#999999"],
    },

    # Optional per-series overrides
    "series_overrides": {
        # "Actual": {"color": "#1F8FA8", "linewidth": 3},
        # "Benchmark": {"color": "#999999", "linewidth": 2},
    },

    # Guides / labels
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

    "auto_end_labels": True,
    "end_labels": [],
}