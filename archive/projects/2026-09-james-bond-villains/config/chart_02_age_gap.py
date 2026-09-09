CHART_CONFIG = {
    "data_file": "archive/projects/2026-09-james-bond-villains/data/bond_villains_chart_02_age_gap.csv",
    "data_format": "wide",
    "chart_type": "dot",
    "orientation": None,

    "x_col": "age_gap",
    "y_col": "villain_label",
    "series_col": None,
    "value_col": None,

    "filters": [],

    "title": "Bond used to fight his elders",
    "subtitle": "Across the 1962–71 films, first-listed villains averaged 14.3 years older than Bond. From 1973 onward they averaged 2.6 years younger.",
    "source_text": "Source: 007.com; Wikipedia actor biographies",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "shift",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "Villain age minus Bond age (years)",
    "y_label": "",
    "x_margin": 0.08,

    "x_axis": {
        "min": -20,
        "max": 35,
        "tick_interval": 5,
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

    "sort": {
        "by": "film_no",
        "ascending": True
    },
    "sort_descending": False,

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,

    "dot_style": {
        "color": "#D9D9D9",
        "size": 58,
        "alpha": 0.75
    },

    "point_style": {
        "color": "#D9D9D9",
        "size": 48,
        "alpha": 0.55
    },

    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.9
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 88,
        "alpha": 1.0
    },

    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 0.8,
        "alpha": 0.25
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.2,
        "alpha": 1.0
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9
    },

    "reference_lines": [
        {
            "axis": "x",
            "value": 0,
            "label": "Same age",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.8
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
        {"film_no": 1},
        {"film_no": 2},
        {"film_no": 3},
        {"film_no": 4},
        {"film_no": 5},
        {"film_no": 6},
        {"film_no": 7}
    ],

    "annotate_points": [
        {
            "film_no": 2,
            "text": "Klebb +31.9",
            "xytext": (-7, 0),
            "ha": "right",
            "va": "center",
            "fontsize": 8,
            "arrowprops": None
        },
        {
            "film_no": 20,
            "text": "Graves / Moon −16.9",
            "xytext": (7, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "arrowprops": None
        }
    ],
    "end_labels": [],

    "label_style": {
        "enabled": False,
        "label_col": None,
        "label_format": "{}",
        "position": "right",
        "fontsize": 8
    },

    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 8,
    "axis_label_fontsize": 10,
    "footer_fontsize": 9,

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
    "plot_left": 0.27,
    "plot_right": 0.90,

    "vertical_gridlines": True,

    "dpi": 200,
    "output_file": "output/bond_villains_age_gap.png"
}
