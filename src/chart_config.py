CHART_CONFIG = {
    "data_file": "data/scotch_whisky_region_profiles.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Average_Score",
    "y_col": "Flavour",

    "series_col": None,
    "value_col": None,

    "title": "Islay is the outlier, not the standard",
    "subtitle": "Most Scotch regions lean sweet, fruity and malty. Islay separates itself through smoke and medicinal intensity.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "comparison",

    "x_label": "Average flavour score, 0–4",
    "y_label": "",

    "x_min": 0,
    "x_max": 4,

    "sort_by": "Flavour",
    "sort_order": "desc",

    "default_colour": "#B8B8B8",
    "highlight_colour": "#C44E52",

    "highlight_points": [
        {"target": "Smoky", "column": "Flavour"},
        {"target": "Medicinal", "column": "Flavour"}
    ],

    "figure_size": (12, 8.5),
    "show_grid": True
}