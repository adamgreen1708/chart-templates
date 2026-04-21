CHART_CONFIG = {
    "data_file": "data/temp_vs_sunshine.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "avg_temp",
    "y_col": "sunshine_hours",

    "title": "Warmer years tend to be sunnier in East Anglia",
    "subtitle": "Average temperature and sunshine hours move together, though not perfectly.",
    "source_text": "Source: Met Office combined datasets",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",

    "y_axis_min": 1200,
    "y_axis_max": 1700,
    "y_tick_interval": 100,
    "y_tick_format": ".0f",

    "auto_end_labels": False,
    "sort_descending": False,

    "show_regression_line": True,
    "show_r_squared": True,
    "scatter_point_size": 55,

    "reference_lines": [],
    "highlight_points": [],
    "annotate_points": [],
    "end_labels": []
}