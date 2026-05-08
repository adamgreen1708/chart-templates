CHART_CONFIG = {
    "data_file": "data/crucible_world_championship_winners.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "year",
    "y_col": "winner",

    "series_col": None,
    "value_col": None,

    "title": "The Crucible usually stayed close to home",
    "subtitle": (
        "Most champions came from England, Scotland, Wales or Northern Ireland, "
        "with overseas winners appearing only occasionally across nearly 50 years."
    ),

    "source_text": "Source: World Snooker Championship results, 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "outlier",

    "output_file": "output/crucible_non_uk_winners.png",

    "x_axis": {
        "label": "Year",
        "min": 1977,
        "max": 2026,
        "tick_interval": 5
    },

    "y_axis": {
        "label": "Champion"
    },

    "label_strategy": "highlight_only",

    "highlight_points": [
        {
            "match": {"year": 1980, "winner": "Cliff Thorburn"},
            "label": "Thorburn"
        },
        {
            "match": {"year": 1997, "winner": "Ken Doherty"},
            "label": "Doherty"
        },
        {
            "match": {"year": 2010, "winner": "Neil Robertson"},
            "label": "Robertson"
        },
        {
            "match": {"year": 2023, "winner": "Luca Brecel"},
            "label": "Brecel"
        },
        {
            "match": {"year": 2025, "winner": "Zhao Xintong"},
            "label": "Zhao"
        }
    ],

    "style": {
        "context_colour": "#B8B8B8",
        "focus_colour": "#C44E52",
        "point_size": 45,
        "highlight_point_size": 85,
        "alpha": 0.65,
        "highlight_alpha": 1.0
    },

    "label_settings": {
        "font_size": 9,
        "x_offset": 0.5,
        "y_offset": 0,
        "avoid_overlap": True
    },

    "show_grid": True,
    "show_x_grid": True,
    "show_y_grid": True,

    "title_wrap_width": 38,
    "subtitle_wrap_width": 92,

    "layout": {
        "left": 0.14,
        "right": 0.96,
        "top": 0.86,
        "bottom": 0.16
    }
}