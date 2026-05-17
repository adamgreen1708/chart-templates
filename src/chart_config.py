CHART_CONFIG = {
    "data_file": "data/scotch_whisky_flavour_menu.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "orientation": "horizontal",

    "x_col": "Peat_Avoider_Score",
    "y_col": "Distillery",

    "series_col": None,
    "value_col": None,

    "title": "Where to start if you dislike peaty Scotch",
    "subtitle": "Sweet, fruity and malty whiskies dominate the friendly end of the flavour spectrum.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "x_label": "Peat avoider score",
    "y_label": "",

    "sort_by": "Peat_Avoider_Score",
    "sort_order": "desc",

    "filters": [
        {
            "column": "Peat_Avoider_Score",
            "operator": ">=",
            "value": 7
        }
    ],

    "x_axis": {
        "min": 0,
        "max": 13
    },

    "highlight_points": [
        {"target": "Aberlour", "column": "Distillery"},
        {"target": "Glenlivet", "column": "Distillery"},
        {"target": "Macallan", "column": "Distillery"},
        {"target": "Balvenie", "column": "Distillery"}
    ],

    "highlight_style": {
        "color": "#C44E52",
        "size": 120,
        "alpha": 1.0
    },

    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.85
    },

    "label_style": {
        "enabled": True,
        "label_col": "Flavour_Profile",
        "fontsize": 8,
        "position": "right",
        "label_format": "{}"
    },

    "annotate_points": [
        {
            "target": "Aberlour",
            "column": "Distillery",
            "text": "rich sherried sweetness",
            "xytext": (10, 0),
            "ha": "left",
            "color": "#555555",
            "fontsize": 8
        },
        {
            "target": "Glenlivet",
            "column": "Distillery",
            "text": "light fruity Speyside style",
            "xytext": (10, 0),
            "ha": "left",
            "color": "#555555",
            "fontsize": 8
        }
    ],

    "figure_size": (10, 10),

    "title_y": 0.93,
    "subtitle_y": 0.885,
    "footer_y": 0.055,

    "plot_left": 0.24,
    "plot_right": 0.90,
    "plot_top": 0.80,
    "plot_bottom": 0.14,

    "tick_label_fontsize": 9,
    "axis_label_fontsize": 10,
    "title_fontsize": 24,
    "subtitle_fontsize": 12,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 74
}