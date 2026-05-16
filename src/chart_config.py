CHART_CONFIG = {
    "data_file": "data/scotch_whisky_smoky_distribution.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Percent",
    "y_col": "Smoky_Score",

    "series_col": None,
    "value_col": None,

    "title": "Peat is whisky’s loud minority",
    "subtitle": "Most distilleries sit at the low-to-mid smoke end of the scale, with only a small group scoring at the extreme.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "x_label": "% of distilleries",
    "y_label": "Smoky score, 0–4",

    "x_min": 0,
    "x_max": 50,

    "sort_by": "Smoky_Score",
    "sort_order": "asc",

    "default_colour": "#1F8FA8",
    "highlight_colour": "#C44E52",

    "highlight_points": [
        {"target": 4, "column": "Smoky_Score"}
    ],

    "figure_size": (12, 8.5)
}