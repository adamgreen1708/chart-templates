CHART_CONFIG = {
    "data_file": "data/snooker_world_championship_winners.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Year",
    "y_col": "Winner",
    "series_col": None,
    "value_col": None,

    "title": "The Crucible usually stayed close to home",
    "subtitle": "Plotting every champion by year shows long UK-dominated eras, with non-UK winners cutting through as rarer breaks in the pattern.",
    "source_text": "Source: World Snooker Championship results, 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "category_timeline",

    "x_axis": {
        "min": 1977,
        "max": 2026,
        "tick_interval": 5,
        "label": "Year"
    },

    "y_axis": {
        "label": "Champion"
    },

    "highlight_rules": {
        "column": "Winner_Nation_Group",
        "highlight_value": "Non-UK",
        "label_highlighted": True,
        "label_column": "Winner",
        "highlight_colour": "#C44E52",
        "context_colour": "#B8B8B8"
    },

    "highlight_points": [
        {
            "match": {"Winner_Nation_Group": "Non-UK"},
            "label": "{Winner}",
            "colour": "#C44E52",
            "size": 70,
            "alpha": 1.0
        }
    ],

    "label_strategy": "highlight_only",

    "label_settings": {
        "label_col": "Winner",
        "only_label_where": {
            "Winner_Nation_Group": "Non-UK"
        },
        "font_size": 9,
        "x_offset": 0.4,
        "y_offset": 0,
        "avoid_overlap": True
    },

    "style": {
        "context_colour": "#B8B8B8",
        "focus_colour": "#C44E52",
        "point_size": 45,
        "highlight_point_size": 75,
        "alpha": 0.65,
        "highlight_alpha": 1.0
    },

    "notes": "Requires a Winner_Nation_Group column with UK / Non-UK classification. UK should include England, Scotland, Wales and Northern Ireland."
}