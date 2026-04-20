CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "year",
    "y_col": "sunshine_hours",
    "series_col": "month",
    "value_col": "sunshine_hours",

    "title": "Spring is arriving brighter in East Anglia",
    "subtitle": "March sunshine has trended upward over the long run, suggesting the darker months are giving way earlier. Recent decades have delivered some of the brightest early springs in the series.",
    "source_text": "Source: Met Office regional climate statistics (East Anglia sunshine)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "comparison",

    "focus_series": "Mar",
    "secondary_series": "Apr",

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.28,
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.2,
        "alpha": 1.0,
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.1,
        "alpha": 0.9,
    },

    "label_strategy": "focus_and_secondary",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "y_axis_min": 0,
    "y_axis_max": 200,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,

    "auto_end_labels": True,

    "reference_lines": [
        {
            "axis": "y",
            "value": 100,
            "label": "100 hours",
            "color": "#9A9A9A",
            "linestyle": "--",
            "linewidth": 1.2,
            "alpha": 0.8,
        }
    ],

    "highlight_points": [
        {
            "series": "Mar",
            "x": 2022,
            "y": 185.5,
            "label": "Exceptional March",
        },
        {
            "series": "Apr",
            "x": 2020,
            "y": 224.8,
            "label": "Record April",
        }
    ],

    "annotate_points": [
        {
            "series": "Mar",
            "x": 2022,
            "y": 185.5,
            "text": "March 2022 was one of the brightest early-spring months on record",
        },
        {
            "series": "Apr",
            "x": 2020,
            "y": 224.8,
            "text": "April 2020 delivered an extraordinary sunshine spike",
        }
    ],

    "end_labels": [],
}