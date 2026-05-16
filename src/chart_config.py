CHART_CONFIG = {
    "data_file": "data/scotch_whisky_flavours_enriched.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Peat_Index",
    "y_col": "Distillery",

    "series_col": None,
    "value_col": None,

    "title": "The peat monsters",
    "subtitle": "Ardbeg, Lagavulin and Laphroig sit at the smoky, medicinal end of Scotland’s whisky flavour map.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "x_label": "Peat index",
    "y_label": "",

    "x_min": 0,
    "x_max": 10,

    "sort_by": "Peat_Index",
    "sort_order": "desc",

    "top_n": 20,

    "highlight_points": [
        {"target": "Ardbeg", "column": "Distillery"},
        {"target": "Lagavulin", "column": "Distillery"},
        {"target": "Laphroig", "column": "Distillery"},
        {"target": "Caol Ila", "column": "Distillery"},
        {"target": "Clynelish", "column": "Distillery"},
        {"target": "Talisker", "column": "Distillery"}
    ],

    "default_colour": "#B8B8B8",
    "highlight_colour": "#C44E52",

    "figure_size": (12, 8.5)
}