CHART_CONFIG = {
    "data_file": "east_anglia_sunshine_2025_wide.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "month",
    "y_col": "sunshine_hours",
    "series_col": None,
    "value_col": None,

    "title": "June blows the rest away",
    "subtitle": "East Anglia’s 2025 sunshine surged through spring before peaking at 276.8 hours in June, well above the monthly average.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "",

    "story_angle": "category_comparison",

    "focus_series": None,
    "secondary_series": None,

    "sort_descending": False,
    "auto_end_labels": False,

    "reference_lines": [
        {
            "y": 149.1,
            "label": "2025 monthly average"
        }
    ],

    "highlight_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "label": "Peak: June"
        }
    ],

    "annotate_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "label": "276.8 hours"
        }
    ],

    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_fontsize": 22,
    "subtitle_fontsize": 13,
    "tick_label_fontsize": 12,
    "footer_fontsize": 10,

    "title_wrap_width": 30,
    "subtitle_wrap_width": 58,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "title_x": 0.11,
    "title_y": 0.94,
    "subtitle_x": 0.11,
    "subtitle_y": 0.865,

    "footer_left_x": 0.11,
    "footer_right_x": 0.89,
    "footer_y": 0.075,

    "plot_top": 0.70,
    "plot_bottom": 0.16,
    "plot_left": 0.11,
    "plot_right": 0.89
}