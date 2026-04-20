CHART_CONFIG = {
    "data_file": "data/uk-mean-temperature.csv",
    "data_format": "wide",
    "chart_type": "line",

    "title": "UK temperatures are trending upward",
    "subtitle": "Annual mean temperature has risen over time, with 2025 the warmest year in the series.",
    "source_text": "Source: UK Met Office",
    "footer_left": "Adam Green | coffeetableviz",

    "vertical_gridlines": False,

    "x_col": "Year",
    "y_col": "Annual mean temperature (°C)",
    "series_col": None,
    "value_col": None,

    "xlim_right_pad": 0.5,

    "sort_descending": False,

    "series_style": {
        "color": "#1F8FA8",
        "linewidth": 2.5
    },

    "series_overrides": {},

    "reference_lines": [],

    "highlight_points": [
        {
            "x": 2025,
            "y": 10.09,
            "label": "Warmest year on record",
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