CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "month_num",
    "y_col": "sunshine_hours",
    "series_col": "year",
    "value_col": "sunshine_hours",

    "title": "2025 wasn’t just warm — it was bright",
    "subtitle": "East Anglia’s 2025 sunshine line stands out early, with March and April both setting monthly records in the dataset.",
    "source_text": "Source: https://www.metoffice.gov.uk",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "focus_vs_context",
    "focus_series": 2025,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 1,
        "max": 12,
        "tick_interval": 1,
        "format": ".0f"
    },

    "y_axis_min": 0,
    "y_axis_max": 330,
    "y_tick_interval": 50,
    "y_tick_format": ".0f",

    "sort": {
        "by": "month_num",
        "ascending": True
    },
    "sort_descending": False,

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,

    "dot_style": {
        "color": "#D9D9D9",
        "size": 48,
        "alpha": 0.55
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 90,
        "alpha": 1.0
    },

    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 0.8,
        "alpha": 0.25,
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

    "reference_lines": [],

    "highlight_points": [
        {"year": 2025, "month_num": 3},
        {"year": 2025, "month_num": 4}
    ],

    "annotate_points": [
        {
            "x": 3,
            "y": 222.0,
            "label": "March record",
            "xytext": (-8, 10),
            "ha": "right",
            "va": "bottom",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None
        },
        {
            "x": 4,
            "y": 269.2,
            "label": "April record",
            "xytext": (8, 8),
            "ha": "left",
            "va": "bottom",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None
        }
    ],

    "end_labels": [
        {
            "x": 12,
            "y": 70.8,
            "label": "2025",
            "fontsize": 9,
            "color": "#1F8FA8",
            "fontweight": "bold"
        }
    ],

    "label_style": {
        "enabled": False,
        "label_col": None,
        "label_format": "{}",
        "position": "right",
        "fontsize": 8
    },

    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 74,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_x": 0.10,
    "title_y": 0.92,
    "subtitle_x": 0.10,
    "subtitle_y": 0.86,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.08,

    "plot_top": 0.75,
    "plot_bottom": 0.14,
    "plot_left": 0.12,
    "plot_right": 0.90,

    "vertical_gridlines": False,

    "dpi": 200,
    "output_file": "output/east_anglia_sunshine_2025_monthly_line.png"
}