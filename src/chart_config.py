CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025.csv",
    "data_format": "wide",
    "chart_type": "dot",
    "sort_descending": True,

    "x_col": "month",
    "y_col": "sunshine_hours",

    "title": "East Anglia’s sunshine exploded in spring",
    "subtitle": "Monthly sunshine hours in 2025 rose sharply from winter lows to a June peak, before dropping back hard by October. Months should stay in calendar order, not be ranked.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "category_comparison",

    "sort_descending": False,

    "highlight_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "label": "Peak: June"
        }
    ],

    "reference_lines": [
        {
            "y": 165.8,
            "label": "2025 monthly average"
        }
    ],

    "annotate_points": [],

    "show_data_labels": False,
    "auto_end_labels": False
}