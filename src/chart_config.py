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

    "default_colour": "#1F8FA8",
    "default_alpha": 0.35,

    "highlight_colour": "#C44E52",

    "point_size": 70,
    "highlight_point_size": 240,

    "jitter": 0.12,

    "highlight_points": [
        {
            "target": "Ardbeg",
            "column": "Distillery",
            "label": "Ardbeg"
        },
        {
            "target": "Lagavulin",
            "column": "Distillery",
            "label": "Lagavulin"
        },
        {
            "target": "Laphroig",
            "column": "Distillery",
            "label": "Laphroaig"
        },
        {
            "target": "Caol Ila",
            "column": "Distillery",
            "label": "Caol Ila"
        },
        {
            "target": "Bowmore",
            "column": "Distillery",
            "label": "Bowmore"
        }
    ],

    "annotate_points": [
        {
            "target": "Ardbeg",
            "column": "Distillery",
            "text": "Smoke monster",
            "xytext": (-50, 20)
        },
        {
            "target": "Lagavulin",
            "column": "Distillery",
            "text": "Classic Islay",
            "xytext": (-40, -25)
        },
        {
            "target": "Glenfarclas",
            "column": "Distillery",
            "text": "Sweet Speyside",
            "xytext": (20, 10)
        }
    ]
}
