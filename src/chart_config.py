CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025_wide.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "month",
    "y_col": "sunshine_hours",

    "title": "June sits clearly on top of East Anglia’s sunshine rankings",
    "subtitle": "Monthly sunshine hours in 2025 ranked from highest to lowest show a clear leader, with June well ahead of the rest.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "auto_end_labels": True,
    "sort_descending": True,

    "reference_lines": [
        {
            "value": 165.8,
            "label": "2025 monthly average"
        }
    ],

    "highlight_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "label": "#1"
        }
    ],

    "annotate_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "text": "June is the clear peak"
        }
    ],

    "end_labels": []
}