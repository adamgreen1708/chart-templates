CHART_CONFIG = {
    "data_file": "data/scotch_whisky_flavours_enriched.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Sweetness",
    "y_col": "Smoky",

    "series_col": None,
    "value_col": None,

    "title": "Smoke has a postcode",
    "subtitle": "Scotland’s smokiest whiskies cluster hard on the islands, while sweeter drams dominate Speyside and the Highlands.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",

    "x_label": "Sweetness",
    "y_label": "Smokiness",

    "x_min": 0,
    "x_max": 4.5,

    "y_min": 0,
    "y_max": 4.5,

    "show_grid": True,

    "figure_size": (12, 8.5),

    "default_colour": "#B8B8B8",
    "highlight_colour": "#C44E52",

    "point_size": 90,
    "highlight_point_size": 180,

    "highlight_points": [
        {
            "target": "Ardbeg",
            "column": "Distillery"
        },
        {
            "target": "Lagavulin",
            "column": "Distillery"
        },
        {
            "target": "Laphroig",
            "column": "Distillery"
        },
        {
            "target": "Caol Ila",
            "column": "Distillery"
        },
        {
            "target": "Bowmore",
            "column": "Distillery"
        }
    ],

    "annotate_points": [
        {
            "target": "Ardbeg",
            "column": "Distillery",
            "text": "Smoke monster",
            "xytext": (-40, 20)
        },
        {
            "target": "Lagavulin",
            "column": "Distillery",
            "text": "Classic Islay profile",
            "xytext": (-20, -25)
        },
        {
            "target": "Glenfarclas",
            "column": "Distillery",
            "text": "Sweet Speyside outlier",
            "xytext": (20, 10)
        },
        {
            "target": "Auchentoshan",
            "column": "Distillery",
            "text": "Low-smoke extreme",
            "xytext": (15, -20)
        }
    ]
}