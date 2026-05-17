CHART_CONFIG = {
    "data_file": "data/scotch_whisky_flavour_averages.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Average_Score",
    "y_col": "Flavour",

    "series_col": None,
    "value_col": None,

    "title": "Scotch is sweeter than its reputation",
    "subtitle": "Sweet, malty and fruity notes sit above smoke, while medicinal and tobacco-heavy flavours remain rare.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "x_label": "Average flavour score, 0–4",
    "y_label": "",

    "x_min": 0,
    "x_max": 4,

    "sort_by": "Average_Score",
    "sort_order": "desc",

    "default_colour": "#B8B8B8",
    "highlight_colour": "#C44E52",

    "highlight_points": [
        {"target": "Sweetness", "column": "Flavour"},
        {"target": "Fruity", "column": "Flavour"},
        {"target": "Malty", "column": "Flavour"},
        {"target": "Smoky", "column": "Flavour"}
    ],

    "figure_size": (12, 8.5)
}