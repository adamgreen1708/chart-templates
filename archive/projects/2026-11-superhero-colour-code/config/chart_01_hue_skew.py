# Coffeetableviz comic colour pilot — PROVISIONAL DATA; not for publication
# Render via src/render_538.py, using the locked social_square profile.
CHART_CONFIG = {
    "data_format": "wide",
    "orientation": "horizontal",
    "series_col": None,
    "value_col": None,
    "filters": [],
    "source_text": "Source: Marvel/DC; curated pilot",
    "footer_left": "Adam Green | coffeetableviz",
    "render_profile": "social_square",
    "profile_overrides": {},
    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",
    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "Hero share minus villain share (pp)",
    "y_label": "",
    "x_margin": 0.08,
    "x_axis": {
        "min": -50,
        "max": 45,
        "tick_interval": 20,
        "format": ".0f"
    },
    "y_axis": {
        "min": None,
        "max": None,
        "tick_interval": None,
        "format": None
    },
    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,
    "x_tick_labels": [],
    "y_tick_labels": [],
    "sort": {
        "by": "hero_minus_villain_pct",
        "ascending": True
    },
    "sort_descending": False,
    "line_width": 2.6,
    "marker_size": 90,
    "show_markers": True,
    "auto_end_labels": False,
    "dot_style": {
        "color": "#D9D9D9",
        "size": 120,
        "alpha": 0.9
    },
    "point_style": {
        "color": "#D9D9D9",
        "size": 95,
        "alpha": 0.9
    },
    "bar_style": {
        "color": "#7A7A7A",
        "alpha": 0.98
    },
    "highlight_style": {
        "color": "#1F8FA8",
        "size": 165,
        "alpha": 1
    },
    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 0.8,
        "alpha": 0.25
    },
    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.2,
        "alpha": 1
    },
    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2,
        "alpha": 0.9
    },
    "reference_lines": [
        {
            "axis": "x",
            "value": 0,
            "color": "#555555",
            "linewidth": 1,
            "linestyle": "-",
            "alpha": 0.75
        }
    ],
    "trend_line": {
        "enabled": False,
        "color": "#7A7A7A",
        "linewidth": 1.4,
        "linestyle": "-",
        "alpha": 0.8
    },
    "highlight_points": [
        {
            "column": "colour",
            "target": "red",
            "color": "#C44E52"
        },
        {
            "column": "colour",
            "target": "blue",
            "color": "#1F8FA8"
        },
        {
            "column": "colour",
            "target": "orange",
            "color": "#D4863F"
        },
        {
            "column": "colour",
            "target": "yellow",
            "color": "#D4A017"
        },
        {
            "column": "colour",
            "target": "purple",
            "color": "#8654A8"
        },
        {
            "column": "colour",
            "target": "green",
            "color": "#2D9067"
        }
    ],
    "annotate_points": [],
    "end_labels": [],
    "label_style": {
        "enabled": False,
        "label_col": None,
        "label_format": "{}",
        "position": "right",
        "fontsize": 11.5
    },
    "title_fontsize": 26,
    "subtitle_fontsize": 16,
    "tick_label_fontsize": 12,
    "axis_label_fontsize": 12,
    "footer_fontsize": 10.5,
    "title_wrap_width": 32,
    "subtitle_wrap_width": 54,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,
    "fig_width": 8,
    "fig_height": 8,
    "title_x": 0.09,
    "title_y": 0.91,
    "subtitle_x": 0.09,
    "subtitle_y": 0.84,
    "footer_left_x": 0.09,
    "footer_right_x": 0.91,
    "footer_y": 0.09,
    "plot_top": 0.72,
    "plot_bottom": 0.22,
    "plot_left": 0.17,
    "plot_right": 0.87,
    "vertical_gridlines": False,
    "dpi": 200,
    "output_file": "output/superhero_01_hue_skew.png",
    "data_file": "archive/projects/2026-11-superhero-colour-code/data/chart_01_hue_skew.csv",
    "chart_type": "bar",
    "x_col": "hero_minus_villain_pct",
    "y_col": "display_label",
    "title": "Red leans hero. Green leans villain.",
    "subtitle": "Which dominant costume colours favour each side in 24 familiar comic characters?"
}
