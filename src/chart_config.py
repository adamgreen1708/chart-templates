CHART_CONFIG = {
    "data_file": "data/self-reported-trust-attitudes.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "Year",
    "y_col": "Trust in others",
    "series_col": "Entity",
    "value_col": "Trust in others",

    "title": "Britain’s trust slump has been reversed",
    "subtitle": "Self-reported trust in others in the UK fell sharply from the late 1990s to the mid-2000s, but by 2022 it had recovered to slightly above its 1984 level. Other countries stay in the background for context.",
    "source_text": "Source: Self-reported trust attitudes dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "focus_vs_context",

    "focus_series": "United Kingdom",
    "secondary_series": None,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.35,
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.2,
        "alpha": 1.0,
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9,
    },

    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "y_axis_min": 0,
    "y_axis_max": 100,
    "y_tick_interval": 20,
    "y_tick_format": ".0f",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,

    "auto_end_labels": True,

    "reference_lines": [
        {
            "axis": "y",
            "value": 42.48,
            "label": "UK 1984 level",
            "color": "#9A9A9A",
            "linestyle": "--",
            "linewidth": 1.2,
            "alpha": 0.8,
        }
    ],

    "highlight_points": [
        {
            "series": "United Kingdom",
            "x": 2004,
            "y": 28.54928,
            "label": "Low point",
        },
        {
            "series": "United Kingdom",
            "x": 2022,
            "y": 43.31179,
            "label": "Recovered by 2022",
        }
    ],

    "annotate_points": [
        {
            "series": "United Kingdom",
            "x": 2004,
            "y": 28.54928,
            "text": "Trust bottomed out in the mid-2000s",
        },
        {
            "series": "United Kingdom",
            "x": 2022,
            "y": 43.31179,
            "text": "Back above the 1984 level",
        }
    ],

    "end_labels": [],
}