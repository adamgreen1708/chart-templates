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

    "x_axis": {"min": 0, "max": 4},

    "focus_series": "Islay",

    "context_style": {
        "color": "#B8B8B8",
        "alpha": 0.50,
        "size": 70,
    },

    "focus_style": {
        "color": "#C44E52",
        "alpha": 1.0,
        "size": 130,
    },

    "annotate_points": [
        {
            "target": "Smoky",
            "column": "Flavour",
            "series": "Islay",
            "text": "Islay dominates smoke",
            "xytext": (24, -10),
            "color": "#C44E52",
        },
        {
            "target": "Medicinal",
            "column": "Flavour",
            "series": "Islay",
            "text": "Medicinal is another Islay signature",
            "xytext": (24, 12),
            "color": "#C44E52",
        }
    ],

    "figure_size": (12, 8.5),
    "plot_top": 0.74,
    "plot_bottom": 0.18,
    "plot_left": 0.14,
    "plot_right": 0.92,
}