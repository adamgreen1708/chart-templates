CHART_CONFIG = {
    "data_file": "archive/projects/2026-09-james-bond-villains/data/bond_villains_chart_03_era_age.csv",
    "data_format": "wide",
    "chart_type": "scatter",
    "orientation": None,

    "x_col": "avg_bond_age",
    "y_col": "avg_villain_age",
    "series_col": None,
    "value_col": None,

    "filters": [],

    "title": "Bond grew into his villains",
    "subtitle": "Connery's villains averaged 13.8 years older. Brosnan's averaged 7.6 younger. Craig and his villains are almost exactly the same age.",
    "source_text": "Source: 007.com; Wikipedia actor biographies",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "Average Bond actor age",
    "y_label": "Average villain actor age",
    "x_margin": 0.08,

    "x_axis": {
        "min": 27,
        "max": 55,
        "tick_interval": 5,
        "format": ".0f"
    },

    "y_axis": {
        "min": 27,
        "max": 55,
        "tick_interval": 5,
        "format": ".0f"
    },
    "y_axis_min": 27,
    "y_axis_max": 55,
    "y_tick_interval": 5,
    "y_tick_format": ".0f",

    "sort": None,
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

    "point_style": {
        "color": "#1F8FA8",
        "size": 72,
        "alpha": 0.85
    },

    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.9
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 105,
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
            "axis": "diagonal",
            "value": 0,
            "label": "Same age",
            "rotation": 34,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
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
        {"bond_actor": "Sean Connery"},
        {"bond_actor": "Pierce Brosnan"},
        {"bond_actor": "Daniel Craig"}
    ],

    "annotate_points": [
        {
            "bond_actor": "George Lazenby",
            "text": "Lazenby +17.6",
            "xytext": (7, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "arrowprops": None
        },
        {
            "bond_actor": "Sean Connery",
            "text": "Connery +13.8",
            "xytext": (7, 8),
            "ha": "left",
            "va": "bottom",
            "fontsize": 8,
            "arrowprops": None
        },
        {
            "bond_actor": "Roger Moore",
            "text": "Moore −2.2",
            "xytext": (-7, 0),
            "ha": "right",
            "va": "center",
            "fontsize": 8,
            "arrowprops": None
        },
        {
            "bond_actor": "Timothy Dalton",
            "text": "Dalton −2.0",
            "xytext": (-7, -4),
            "ha": "right",
            "va": "top",
            "fontsize": 8,
            "arrowprops": None
        },
        {
            "bond_actor": "Pierce Brosnan",
            "text": "Brosnan −7.6",
            "xytext": (7, -8),
            "ha": "left",
            "va": "top",
            "fontsize": 8,
            "arrowprops": None
        },
        {
            "bond_actor": "Daniel Craig",
            "text": "Craig +0.4",
            "xytext": (7, 8),
            "ha": "left",
            "va": "bottom",
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
    "tick_label_fontsize": 10,
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
    "plot_left": 0.15,
    "plot_right": 0.88,

    "vertical_gridlines": True,

    "dpi": 200,
    "output_file": "output/bond_villains_era_age.png"
}
