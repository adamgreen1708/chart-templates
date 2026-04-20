CHART_CONFIG = {
    "data_file": "data/uk-mean-temperature.csv",
    "data_format": "csv",

    "chart_type": "line",

    "title": "UK temperatures have left the past behind",
    "subtitle": "After hovering around ~8.3°C for over a century, recent years are consistently pushing toward — and beyond — 10°C, with 2025 the highest on record.",

    "source_text": "Source: UK Met Office historical temperature data",
    "footer_left": "Adam Green | coffeetableviz",

    "vertical_gridlines": False,

    "x_col": "Year",
    "y_col": "Annual mean temperature (°C)",
    "series_col": None,
    "value_col": "Annual mean temperature (°C)",

    "xlim_right_pad": 2,

    "sort_descending": False,

    "series_style": {
        "color": "#1F8FA8",
        "linewidth": 2.6
    },

    "series_overrides": {},

    "reference_lines": [
        {
            "y": 8.3,
            "label": "20th century average (~8.3°C)",
            "color": "#999999",
            "linestyle": "--",
            "linewidth": 1,
            "label_x": 0.02,
            "label_offset": 0
        }
    ],

    "highlight_points": [
        {
            "x": 2025,
            "y": 10.09,
            "label": "2025: 10.1°C (record high)",
            "color": "#C44E52",
            "dx": -10,
            "dy": 10,
            "ha": "right",
            "size": 10
        }
    ],

    "auto_end_labels": False,
    "end_labels": []
}