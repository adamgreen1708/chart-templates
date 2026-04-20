CHART_CONFIG = {
    "data_file": "data/inflation-1989-2025.csv",
    "data_format": "wide",
    "chart_type": "line",
    "title": "Inflation didn’t just rise — it snapped back",
    "subtitle": "UK inflation surged in the early 2020s to levels not seen since the early 1990s",
    "source_text": "Source: ONS",
    "footer_left": "Adam Green | coffeetableviz",
    "vertical_gridlines": True,
    "x_col": "year",
    "y_col": "rate",
    "series_col": None,
    "value_col": None,
    "xlim_right_pad": 1,
    "sort_descending": False,
    "series_style": {
        "color": "#1F8FA8",
        "linewidth": 2.5
    },
    "series_overrides": {},
    "reference_lines": [
        {
            "y": 2.65,
            "label": "Pre-2020 average",
            "color": "#C44E52",
            "linestyle": "--",
            "linewidth": 1.5,
            "label_x": 1992,
            "label_offset": 0.1
        }
    ],
    "highlight_points": [
        {
            "x": 2022,
            "y": 7.9,
            "label": "Post-pandemic spike",
            "color": "#C44E52",
            "dx": 0,
            "dy": 0.5,
            "ha": "center",
            "size": 90
        }
    ],
    "auto_end_labels": False,
    "end_labels": []
}