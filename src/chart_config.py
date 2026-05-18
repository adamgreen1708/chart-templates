CHART_CONFIG = {
    "data_file": "data/region_quadrants/scotch_whisky_quadrants_speyside.csv",

    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Peat_Index",
    "y_col": "Approachable_Index",

    "series_col": None,
    "value_col": None,

    "title": "Speyside lives far from the peat extreme",
    "subtitle": "Most Speyside whiskies cluster around sweeter, fruitier and more approachable flavour profiles.",

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

    "highlight_points": [
        {"target": "Macallan", "column": "Distillery"},
        {"target": "Glenlivet", "column": "Distillery"},
        {"target": "Aberlour", "column": "Distillery"}
    ],

    "highlight_style": {
        "color": "#C44E52",
        "size": 130,
        "alpha": 1.0
    },

    "annotate_points": [
        {
            "target": "Macallan",
            "column": "Distillery",
            "text": "rich and approachable",
            "xytext": (-25, 20),
            "ha": "right",
            "color": "#555555",
            "fontsize": 9
        },
        {
            "target": "Glenlivet",
            "column": "Distillery",
            "text": "classic easy-drinking Speyside",
            "xytext": (15, -18),
            "ha": "left",
            "color": "#555555",
            "fontsize": 9
        }
    ],

    "dot_style": {
        "color": "#1F8FA8",
        "alpha": 0.55,
        "size": 70
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