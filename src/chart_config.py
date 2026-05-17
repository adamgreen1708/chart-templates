CHART_CONFIG = {
    "data_file": "data/scotch_whisky_peat_avoider_score.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Peat_Avoider_Score",
    "y_col": "Distillery",

    "series_col": None,
    "value_col": None,

    "title": "A whisky map for peat avoiders",
    "subtitle": "Most Scotch sits comfortably away from the smoky Islay extreme once medicinal and peaty notes are penalised.",

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
            "alpha": 0.55
        }
    ],

    "highlight_points": [
        {"target": "Ardbeg", "column": "Distillery"},
        {"target": "Lagavulin", "column": "Distillery"},
        {"target": "Laphroig", "column": "Distillery"},
        {"target": "Caol Ila", "column": "Distillery"},
        {"target": "Bowmore", "column": "Distillery"},
        {"target": "Bruichladdich", "column": "Distillery"},
        {"target": "Bunnahabhain", "column": "Distillery"}
    ],

    "highlight_style": {
        "color": "#C44E52",
        "size": 120,
        "alpha": 1.0
    },

    "highlight_colour": "#C44E52",

    "annotate_points": [
        {
            "target": "Laphroig",
            "column": "Distillery",
            "text": "Islay dominates the smoky stereotype",
            "xytext": (28, 0),
            "ha": "left",
            "color": "#555555",
            "fontsize": 9
        }
    ],

    "dot_style": {
        "color": "#1F8FA8",
        "alpha": 0.40,
        "size": 48
    },

    "figure_size": (10, 18),

    "plot_left": 0.22,
    "plot_right": 0.90,
    "plot_top": 0.80,
    "plot_bottom": 0.10,

    "tick_label_fontsize": 6.5,
    "axis_label_fontsize": 10,
    "title_fontsize": 24,
    "subtitle_fontsize": 12,

    "title_wrap_width": 42,
    "subtitle_wrap_width": 78
}