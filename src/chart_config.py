CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "year",
    "y_col": "sunshine_hours",
    "series_col": "month",
    "value_col": "sunshine_hours",

    "title": "East Anglia’s winters are getting brighter",
    "subtitle": "January, February and December sunshine have all trended upward over the long run. January shows the clearest lift, while February has delivered some of the biggest recent spikes.",
    "source_text": "Source: Met Office regional climate statistics (East Anglia sunshine)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "comparison",

    "focus_series": "Jan",
    "secondary_series": ["Feb", "Dec"],

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

    "label_strategy": "focus_and_secondary",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "y_axis_min": 0,
    "y_axis_max": 150,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,

    "auto_end_labels": True,

    "reference_lines": [
        {
            "axis": "y",
            "value": 50,
            "label": "50 hours",
            "color": "#9A9A9A",
            "linestyle": "--",
            "linewidth": 1.2,
            "alpha": 0.8,
        }
    ],

    "highlight_points": [
        {
            "series": "Jan",
            "x": 2022,
            "y": 96.0,
            "label": "Record January",
        },
        {
            "series": "Feb",
            "x": 2019,
            "y": 137.2,
            "label": "Exceptional February",
        }
    ],

    "annotate_points": [
        {
            "series": "Jan",
            "x": 2022,
            "y": 96.0,
            "text": "January hit a record high in 2022",
        },
        {
            "series": "Feb",
            "x": 2019,
            "y": 137.2,
            "text": "February spiked dramatically in 2019",
        }
    ],

    "end_labels": [],
}