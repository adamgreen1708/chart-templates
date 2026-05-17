CHART_CONFIG = {
    "data_file": "data/scotch_whisky_peat_avoider_score.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Peat_Avoider_Score",
    "y_col": "Distillery",

    "series_col": None,
    "value_col": None,

    "title": "A whisky map for peat avoiders",
    "subtitle": "Sweet, fruity, malty and honeyed profiles rise to the top once smoky and medicinal notes are penalised.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "x_label": "Peat avoider score",
    "y_label": "",

    "x_axis": {
        "min": -6,
        "max": 13
    },

    "sort_by": "Peat_Avoider_Score",
    "sort_order": "desc",

    "reference_lines": [
        {
            "axis": "x",
            "value": 0,
            "label": "neutral",
            "color": "#777777",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.7
        }
    ],

    "highlight_points": [
        {"target": "Aberlour", "column": "Distillery"},
        {"target": "Glenturret", "column": "Distillery"},
        {"target": "Glenmorangie", "column": "Distillery"},
        {"target": "Glenlivet", "column": "Distillery"},
        {"target": "Macallan", "column": "Distillery"},
        {"target": "Laphroig", "column": "Distillery"},
        {"target": "Lagavulin", "column": "Distillery"},
        {"target": "Ardbeg", "column": "Distillery"}
    ],

    "highlight_colour": "#C44E52",

    "annotate_points": [
        {
            "target": "Aberlour",
            "column": "Distillery",
            "text": "sweet/fruity comfort zone",
            "xytext": (-110, 0),
            "ha": "right",
            "color": "#C44E52"
        },
        {
            "target": "Laphroig",
            "column": "Distillery",
            "text": "peat-heavy avoid zone",
            "xytext": (30, 0),
            "ha": "left",
            "color": "#C44E52"
        }
    ],

    "dot_style": {
        "color": "#1F8FA8",
        "alpha": 0.75,
        "size": 55
    },

    "figure_size": (10, 18),

    "plot_left": 0.20,
    "plot_right": 0.90,
    "plot_top": 0.82,
    "plot_bottom": 0.12,

    "tick_label_fontsize": 7,
    "axis_label_fontsize": 10,
    "title_fontsize": 24,
    "subtitle_fontsize": 12
}