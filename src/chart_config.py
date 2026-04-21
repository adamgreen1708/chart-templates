CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025_wide.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "sunshine_hours",
    "y_col": "month",

    "title": "Spring 2025 did the heavy lifting for sunshine",
    "subtitle": "March–May dominate the sunshine rankings in East Anglia, with April peaking far above the rest.",
    "source_text": "Source: East Anglia sunshine dataset (2025)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "focus_series": None,
    "secondary_series": None,

    "sort_order": "descending",

    "annotations": {
        "reference_lines": [],
        "highlight_points": [
            {
                "x": 269.2,
                "y": "Apr",
                "label": "Peak sunshine month"
            }
        ],
        "annotate_points": [
            {
                "x": 222.0,
                "y": "Mar",
                "label": "Start of spring surge"
            },
            {
                "x": 252.8,
                "y": "May",
                "label": "Sustained high sunshine"
            }
        ],
        "auto_end_labels": False
    },

    "style": {
        "dot_size": 60,
        "color": "#1F8FA8",
        "highlight_color": "#C44E52"
    }
}