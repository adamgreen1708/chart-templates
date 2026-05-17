CHART_CONFIG = {
    "data_file": "data/scotch_whisky_region_profiles.csv",
    "data_format": "long",
    "chart_type": "dot",

    "x_col": "Average_Score",
    "y_col": "Flavour",

    "series_col": "Region",
    "value_col": "Average_Score",

    "title": "Islay is the outlier, not the standard",
    "subtitle": "Most Scotch regions lean sweet, fruity and malty. Islay separates itself through smoke and medicinal intensity.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "comparison",

    "x_label": "Average flavour score, 0–4",
    "y_label": "",

    "x_min": 0,
    "x_max": 4,

    "default_colour": "#B8B8B8",
    "highlight_colour": "#C44E52",

    "focus_series": "Islay",

    "figure_size": (12, 10),

    "show_grid": True,

    "label_strategy": "focus_only"
}