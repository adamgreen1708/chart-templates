CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "archive/projects/2026-09-brad-pitt-imdb-list/data/brad_pitt_chart_03_timeline.csv",
    "data_format": "wide",
    "chart_type": "scatter",
    "orientation": None,

    "x_col": "Year",
    "y_col": "IMDb Rating",
    "series_col": None,
    "value_col": None,

    "filters": [],

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "From 4.6 to 8.8",
    "subtitle": "The 54-film list spans 4.2 rating points; 1995–99 is its strongest five-year run, averaging 7.63 across seven films.",
    "source_text": "Source: IMDb list export",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "time_relationship",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "Film year",
    "y_label": "IMDb rating",
    "x_margin": 0.08,

    "x_axis": {
        "min": 1986,
        "max": 2027,
        "tick_interval": 5,
        "format": ".0f"
    },

    "y_axis": {
        "min": 4.2,
        "max": 9.1,
        "tick_interval": 1,
        "format": ".1f"
    },
    "y_axis_min": 4.2,
    "y_axis_max": 9.1,
    "y_tick_interval": 1,
    "y_tick_format": ".1f",

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "Year",
        "ascending": True
    },
    "sort_descending": False,

    # ---------------------------
    # MARKS
    # ---------------------------
    "line_width": 2.6,
    "marker_size": 58,
    "show_markers": True,
    "auto_end_labels": False,

    # ---------------------------
    # STYLING
    # ---------------------------
    "dot_style": {
        "color": "#D9D9D9",
        "size": 48,
        "alpha": 0.55
    },

    "point_style": {
        "color": "#D9D9D9",
        "size": 58,
        "alpha": 0.70
    },

    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.9
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

    # ---------------------------
    # REFERENCE LINES / TREND
    # ---------------------------
    "reference_lines": [
        {
            "axis": "y",
            "value": 7.1,
            "label": "List median 7.1",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.7
        }
    ],

    "trend_line": {
        "enabled": False,
        "color": "#7A7A7A",
        "linewidth": 1.4,
        "linestyle": "-",
        "alpha": 0.8
    },

    # ---------------------------
    # ANNOTATIONS
    # ---------------------------
    "highlight_points": [
        {"column": "Peak 1995-99", "value": 1},
    ],

    "annotate_points": [
        {
            "Title": "Fight Club",
            "text": "Fight Club · 8.8",
            "xytext": (7, -10),
            "ha": "left",
            "va": "top",
            "fontsize": 8,
            "arrowprops": None,
        },
        {
            "Title": "Cutting Class",
            "text": "Cutting Class · 4.6",
            "xytext": (7, 8),
            "ha": "left",
            "va": "bottom",
            "fontsize": 8,
            "arrowprops": None,
        },
    ],

    "end_labels": [],

    "label_style": {
        "enabled": False,
        "label_col": None,
        "label_format": "{}",
        "position": "right",
        "fontsize": 8
    },

    # ---------------------------
    # TYPOGRAPHY
    # ---------------------------
    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 74,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    # ---------------------------
    # LAYOUT
    # ---------------------------
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

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/brad_pitt_timeline_ratings.png"
}
