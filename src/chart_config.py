CHART_CONFIG = {
    "data_file": "data/scotch_whisky_flavour_quadrants.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Peat_Index",
    "y_col": "Approachable_Index",

    "series_col": None,
    "value_col": None,

    "title": "Most Scotch sits nowhere near the peat extreme",
    "subtitle": "Sweetness, fruit and honey dominate much of the Scotch landscape once smoky and medicinal notes are isolated.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",

    "x_label": "Peat index (smoky + medicinal)",
    "y_label": "Approachable index (sweet + fruity + honey)",

    "x_axis": {
        "min": 0,
        "max": 8
    },

    "y_axis": {
        "min": 0,
        "max": 10
    },

    "reference_lines": [
        {
            "axis": "x",
            "value": 4,
            "label": "high peat",
            "color": "#777777",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.6
        },
        {
            "axis": "y",
            "value": 5,
            "label": "more approachable",
            "color": "#777777",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.6
        }
    ],

    "highlight_points": [
        {"target": "Ardbeg", "column": "Distillery"},
        {"target": "Lagavulin", "column": "Distillery"},
        {"target": "Laphroig", "column": "Distillery"},
        {"target": "Macallan", "column": "Distillery"},
        {"target": "Glenlivet", "column": "Distillery"},
        {"target": "Aberlour", "column": "Distillery"}
    ],

    "highlight_style": {
        "color": "#C44E52",
        "size": 140,
        "alpha": 1.0
    },

    "highlight_colour": "#C44E52",

    "annotate_points": [
        {
            "target": "Laphroig",
            "column": "Distillery",
            "text": "classic peat monster",
            "xytext": (20, 0),
            "ha": "left",
            "color": "#555555",
            "fontsize": 9
        },
        {
            "target": "Macallan",
            "column": "Distillery",
            "text": "rich but approachable",
            "xytext": (-30, 20),
            "ha": "right",
            "color": "#555555",
            "fontsize": 9
        }
    ],

    "dot_style": {
        "color": "#1F8FA8",
        "alpha": 0.45,
        "size": 60
    },

    "figure_size": (10, 10),

    "plot_left": 0.14,
    "plot_right": 0.92,
    "plot_top": 0.80,
    "plot_bottom": 0.14,

    "title_y": 0.93,
    "subtitle_y": 0.885,
    "footer_y": 0.055,

    "tick_label_fontsize": 9,
    "axis_label_fontsize": 10,
    "title_fontsize": 24,
    "subtitle_fontsize": 12
}
