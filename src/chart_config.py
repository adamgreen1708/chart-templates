CHART_CONFIG = {
    # =========================
    # DATA
    # =========================
    "data_file": "data/snooker_world_championship_winners.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "year",
    "y_col": "winner",

    "series_col": None,
    "value_col": None,

    # =========================
    # EDITORIAL
    # =========================
    "title": "The Crucible occasionally opened the door",
    "subtitle": (
        "The World Championship has mostly stayed with UK winners, "
        "but five overseas champions broke through across the Crucible era."
    ),

    "story_angle": "outlier",

    # =========================
    # FOOTER
    # =========================
    "source_text": "Source: World Snooker Championship winners 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    # =========================
    # EXPORT
    # =========================
    "output_file": "output/crucible_non_uk_winners.png",

    # =========================
    # AXES
    # =========================
    "x_axis": {
        "label": "",
        "min": 1977,
        "max": 2026,
        "tick_interval": 5
    },

    "y_axis": {
        "label": ""
    },

    # =========================
    # HIGHLIGHTS
    # IMPORTANT:
    # This mirrors the working chart structure:
    # explicit x/y point references, not match wrappers.
    # =========================
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
        }
    ],

    # =========================
    # ANNOTATIONS
    # =========================
    "annotate_points": [
        {
            "x": 1980,
            "y": "Cliff Thorburn",
            "label": "First overseas Crucible champion",
            "x_offset": 1.2,
            "y_offset": -0.35
        },
        {
            "x": 2025,
            "y": "Zhao Xintong",
            "label": "Latest overseas breakthrough",
            "x_offset": -8.5,
            "y_offset": 0.4
        }
    ],

    # =========================
    # LABELS
    # =========================
    "label_strategy": "highlight_only",

    "label_settings": {
        "font_size": 10,
        "x_offset": 0.5,
        "y_offset": 0,
        "avoid_overlap": True
    },

    # =========================
    # STYLE
    # =========================
    "style": {
        "context_colour": "#D7D7D7",
        "focus_colour": "#C44E52",

        "point_size": 46,
        "highlight_point_size": 92,

        "alpha": 0.55,
        "highlight_alpha": 1.0,

        "label_colour": "#333333",
        "highlight_label_colour": "#333333"
    },

    # =========================
    # GRID
    # =========================
    "show_grid": True,
    "show_x_grid": True,
    "show_y_grid": True,

    # =========================
    # TEXT WRAP
    # =========================
    "title_wrap_width": 42,
    "subtitle_wrap_width": 82,

    # =========================
    # LAYOUT
    # =========================
    "layout": {
        "left": 0.18,
        "right": 0.94,
        "top": 0.82,
        "bottom": 0.14
    }
}