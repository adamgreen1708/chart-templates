CHART_CONFIG = {
    "data_file": "data/snooker_world_championship_winners.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "year",
    "y_col": "winner",

    "series_col": None,
    "value_col": None,

    "title": "The Crucible opened the door",
    "subtitle": (
        "Six overseas champions broke through during a Crucible era otherwise "
        "dominated by UK winners."
    ),

    "source_text": "Source: World Snooker Championship winners 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "outlier",

    "output_file": "output/crucible_non_uk_winners.png",

    "x_axis": {
        "label": "",
        "min": 1977,
        "max": 2027,
        "tick_interval": 5
    },

    "y_axis": {
        "label": ""
    },

    "highlight_points": [
        {
            "x": 1980,
            "y": "Cliff Thorburn",
            "label": "Canada"
        },
        {
            "x": 1997,
            "y": "Ken Doherty",
            "label": "Ireland"
        },
        {
            "x": 2010,
            "y": "Neil Robertson",
            "label": "Australia"
        },
        {
            "x": 2023,
            "y": "Luca Brecel",
            "label": "Belgium"
        },
        {
            "x": 2025,
            "y": "Zhao Xintong",
            "label": "China"
        },
        {
            "x": 2026,
            "y": "Wu Yize",
            "label": "China"
        }
    ],

    "annotate_points": [],

    "label_strategy": "highlight_only",

    "label_settings": {
        "font_size": 9,
        "x_offset": 0.35,
        "y_offset": 0,
        "avoid_overlap": True
    },

    "style": {
        "context_colour": "#D7D7D7",
        "focus_colour": "#C44E52",

        "point_size": 44,
        "highlight_point_size": 90,

        "alpha": 0.50,
        "highlight_alpha": 1.0,

        "label_colour": "#333333",
        "highlight_label_colour": "#333333"
    },

    "show_grid": True,
    "show_x_grid": True,
    "show_y_grid": True,

    "title_wrap_width": 34,
    "subtitle_wrap_width": 76,

    "layout": {
        "left": 0.24,
        "right": 0.90,
        "top": 0.76,
        "bottom": 0.18
    }
}