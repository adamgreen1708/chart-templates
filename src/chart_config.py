CHART_CONFIG = {
    "chart_type": "line",
    "x_col": "x",
    "y_col": "value",
    "series_col": None,

    "title": "Britain keeps getting warmer",
    "subtitle": "Annual mean temperature has trended upward over the long run, with 2025 the warmest year in this series.",
    "footer_left": "Adam Green | coffeetableviz",

    "colour": "#1F8FA8",
    "highlight_colour": "#C44E52",

    "sort_descending": True,

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "y_axis_min": 7.0,
    "y_axis_max": 10.5,
    "y_tick_interval": 0.5,
    "y_tick_format": "{:.1f}°C",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,
    "show_grid_x": True,
    "show_grid_y": True,

    "auto_end_labels": False,

    "reference_lines": [
        {
            "axis": "y",
            "value": 8.5,
            "label": "Long-run average",
            "colour": "#999999",
            "linestyle": "--",
            "linewidth": 1.0
        }
    ],

    "highlight_points": [
        {
            "x": 2025,
            "y": 10.09,
            "label": "2025",
            "colour": "#C44E52"
        }
    ],

    "annotate_points": [
        {
            "x": 2025,
            "y": 10.09,
            "text": "Warmest year in the series",
            "xytext": (-36, -18),
            "ha": "right"
        }
    ]
}