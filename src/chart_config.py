CHART_CONFIG = {
    "data_file": "data/region_quadrants/scotch_whisky_quadrants_lowlands.csv",

    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Peat_Index",
    "y_col": "Approachable_Index",

    "series_col": None,
    "value_col": None,

    "title": "Lowlands stay firmly approachable",
    "subtitle": "Lowland whiskies cluster around lighter, softer and less smoky flavour profiles than most other Scotch regions.",

    "source_text": "Source: Kaggle Scotch Whisky Flavour Dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",

    "x_label": "Peat index (smoky + medicinal)",
    "y_label": "Approachable index (sweet + fruity + honey)",

    "x_axis": {
        "min": 0,
        "max": 11
    },

    "y_axis": {
        "min": 0,
        "max": 11
    },

    "reference_lines": [
        {
            "axis": "x",
            "value": 4,
            "label": "high peat",
            "color": "#999999",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.5
        },
        {
            "axis": "y",
            "value": 5,
            "label": "more approachable",
            "color": "#999999",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.5
        }
    ],

    "label_style": {
        "enabled": True,
        "label_col": "Distillery",
        "fontsize": 8,
        "position": "right",
        "label_format": "{}"
    },

    "dot_style": {
        "color": "#1F8FA8",
        "alpha": 0.75,
        "size": 75
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
    "subtitle_fontsize": 12,

    "title_wrap_width": 42,
    "subtitle_wrap_width": 78
}