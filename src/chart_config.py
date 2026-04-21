CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025.csv",
    "data_format": "long",
    "chart_type": "bar",

    "x_col": "month",
    "y_col": "sunshine_hours",
    "series_col": None,
    "value_col": "sunshine_hours",

    "title": "Spring 2025 delivered a surge of sunshine",
    "subtitle": "East Anglia saw a sharp jump in sunshine hours through spring, with April standing out as the brightest month by a clear margin.",
    "source_text": "Source: East Anglia sunshine dataset (2025)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "category_comparison",

    "sort_descending": False,

    "reference_lines": [
        {
            "value": 165.8,
            "label": "2025 monthly average"
        }
    ],

    "highlight_points": [
        {
            "x": "Apr",
            "y": 269.2
        }
    ],

    "annotate_points": [],

    "auto_end_labels": False
}