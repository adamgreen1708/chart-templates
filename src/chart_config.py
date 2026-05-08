CHART_CONFIG = {
    # =========================
    # DATA
    # =========================
    "data_file": "data/snooker_world_championship_winners.csv",

    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "year",
    "y_col": "winner",

    "series_col": None,
    "value_col": None,

    # =========================
    # EDITORIAL
    # =========================
    "title": "The Crucible usually stayed close to home",

    "subtitle": (
        "England, Scotland, Wales and Northern Ireland dominated most "
        "of the Crucible era, with overseas winners only occasionally "
        "breaking through."
    ),

    "story_angle": "outlier",

    # =========================
    # FOOTER
    # =========================
    "source_text": "Source: World Snooker Championship results, 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    # =========================
    # FIGURE / EXPORT
    # =========================
    "figure_size": (12, 8.5),
    "output_file": "output/crucible_non_uk_winners.png",

    # =========================
    # X AXIS
    # =========================
    "x_axis": {
        "label": "Year",
        "min": 1977,
        "max": 2026,
        "tick_interval": 5
    },

    # =========================
    # Y AXIS
    # =========================
    "y_axis": {
        "label": "Champion"
    },

    # =========================
    # STYLING
    # =========================
    "background_colour": "#F3F4F6",
    "grid_colour": "#D9D9D9",

    "style": {
        "context_colour": "#B8B8B8",
        "focus_colour": "#C44E52",

        "point_size": 45,
        "highlight_point_size": 80,

        "alpha": 0.65,
        "highlight_alpha": 1.0
    },

    # =========================
    # LABELS
    # =========================
    "label_strategy": "highlight_only",

    "label_settings": {
        "font_size": 9,
        "x_offset": 0.5,
        "y_offset": 0,
        "avoid_overlap": True
    },

    # =========================
    # HIGHLIGHTED NON-UK WINNERS
    # =========================
    "highlight_points": [

        {
            "match": {
                "year": 1980,
                "winner": "Cliff Thorburn"
            },
            "label": "Thorburn"
        },

        {
            "match": {
                "year": 1997,
                "winner": "Ken Doherty"
            },
            "label": "Doherty"
        },

        {
            "match": {
                "year": 2010,
                "winner": "Neil Robertson"
            },
            "label": "Robertson"
        },

        {
            "match": {
                "year": 2023,
                "winner": "Luca Brecel"
            },
            "label": "Brecel"
        },

        {
            "match": {
                "year": 2025,
                "winner": "Zhao Xintong"
            },
            "label": "Zhao"
        }
    ],

    # =========================
    # GRIDLINES
    # =========================
    "show_grid": True,
    "show_x_grid": True,
    "show_y_grid": True,

    # =========================
    # TITLE WRAPPING
    # =========================
    "title_wrap_width": 34,
    "subtitle_wrap_width": 90,

    # =========================
    # MARGINS / PADDING
    # =========================
    "layout": {
        "left": 0.12,
        "right": 0.96,
        "top": 0.86,
        "bottom": 0.16
    }
}