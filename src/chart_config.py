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

    "figure_size": (12, 8.5),
    "output_file": "output/crucible_non_uk_winners.png",

    "x_axis": {
        "label": "",
        "min": 1977,
        "max": 2026,
        "tick_interval": 5
    },

    "y_axis": {
        "label": ""
    },

    "highlight_points": [
        {"x": 1979, "y": "Cliff Thorburn", "label": ""},
        {"x": 1997, "y": "Ken Doherty", "label": ""},
        {"x": 2010, "y": "Neil Robertson", "label": ""},
        {"x": 2023, "y": "Luca Brecel", "label": ""},
        {"x": 2025, "y": "Zhao Xintong", "label": ""},
        {"x": 2026, "y": "Wu Yize", "label": ""}
    ],

    "label_strategy": "none",

    "style": {
        "context_colour": "#1F8FA8",
        "focus_colour": "#C44E52",

        "point_size": 52,
        "highlight_point_size": 86,

        "alpha": 0.85,
        "highlight_alpha": 1.0
    },

    "show_grid": True,
    "show_x_grid": True,
    "show_y_grid": True,

    "title_wrap_width": 38,
    "subtitle_wrap_width": 78,

    "layout": {
        "left": 0.30,
        "right": 0.94,
        "top": 0.80,
        "bottom": 0.16
    }
}