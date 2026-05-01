CHART_CONFIG = {
    "data_file": "data/human_vs_ai_content_long.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "date",
    "y_col": "pct",
    "series_col": "type",
    "value_col": "pct",

    "title": "AI rose as human content fell",
    "subtitle": "Detected AI-created articles climbed from around 2% in 2020 to more than half by late 2024, mirroring the fall in human-created content.",
    "source_text": "Source: Graphite.io study; user-provided dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "crossover",
    "focus_series": "AI",
    "secondary_series": "Human",
    "label_strategy": "focus_only",

    "x_is_datetime": True,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": None,
        "max": None,
        "tick_interval": None,
        "format": "%Y"
    },

    "y_axis_min": 0,
    "y_axis_max": 1.0,
    "y_tick_interval": 0.25,
    "y_tick_format": "percent",

    "sort": {
        "by": "date",
        "ascending": True
    },
    "sort_descending": False,

    "line_width": 2.8,
    "marker_size": 60,
    "show_markers": False,
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
        "linewidth": 2.6,
        "alpha": 0.9,
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.2,
        "alpha": 1.0,
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.6,
        "alpha": 0.9,
    },

    "reference_lines": [
        {
            "axis": "y",
            "value": 0.50,
            "label": "50%",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.7
        }
    ],

    "highlight_points": [
        {"date": "2024-11-01", "type": "AI"},
        {"date": "2024-11-01", "type": "Human"}
    ],

    "annotate_points": [
        {
            "x": "2024-11-01",
            "y": 0.5108,
            "label": "AI moves ahead",
            "xytext": (-10, 10),
            "ha": "right",
            "va": "bottom",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None
        }
    ],

    "end_labels": [
        {
            "x": "2025-05-01",
            "y": 0.5172,
            "label": "AI",
            "fontsize": 9,
            "color": "#1F8FA8",
            "fontweight": "bold"
        },
        {
            "x": "2025-05-01",
            "y": 0.4828,
            "label": "Human",
            "fontsize": 9,
            "color": "#7A7A7A",
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
    "output_file": "output/human_vs_ai_content_crossover.png"
}