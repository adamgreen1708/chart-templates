"""Shared, opt-in Coffeetableviz rendering profiles.

Standard continues respecting existing project overrides. Social takes
precedence over legacy project sizes and only allows documented exceptions.
"""
BG="#F3F4F6"
PRIMARY="#1F8FA8"
ACCENT="#C44E52"
TEXT="#111111"
MUTED="#555555"
BRAND_FOOTER="Adam Green | coffeetableviz"

STANDARD={
 "title_fontsize":22,"subtitle_fontsize":12,
 "tick_label_fontsize":10,"axis_label_fontsize":10,
 "footer_fontsize":10,"annotation_fontsize":9,
 "title_wrap_width":40,"subtitle_wrap_width":74,
 "title_max_lines":2,"subtitle_max_lines":2,
 "title_x":.10,"title_y":.92,"subtitle_x":.10,"subtitle_y":.86,
 "footer_left_x":.10,"footer_right_x":.90,"footer_y":.08,
 "plot_top":.75,"plot_bottom":.14,"plot_left":.12,"plot_right":.90,
}
# Every social render shares this outer safe frame. The plot sits farther
# inside it to leave room for tick labels and y-axis units.
SOCIAL_SAFE_MARGIN = 0.085
SOCIAL_SQUARE={**STANDARD,
 "title_fontsize":26,"subtitle_fontsize":16,
 "tick_label_fontsize":12,"axis_label_fontsize":12,
 "footer_fontsize":10.5,"annotation_fontsize":11.5,
 "title_wrap_width":32,"subtitle_wrap_width":54,
 "title_x":.09,"title_y":.91,
 "subtitle_x":.09,"subtitle_y":.84,
 "footer_left_x":.09,"footer_right_x":.91,"footer_y":.09,
 "plot_top":.72,"plot_bottom":.22,"plot_left":.17,"plot_right":.87,
}
PROFILES={"standard":STANDARD,"social_square":SOCIAL_SQUARE}

def resolve_style(config):
    name=config.get("render_profile","standard")
    if name not in PROFILES:
        raise ValueError(f"Unknown render_profile: {name!r}")
    style=PROFILES[name].copy()
    if name=="standard":
        style.update({key:config[key] for key in STANDARD if key in config})
    overrides=config.get("profile_overrides") or {}
    if not isinstance(overrides,dict) or set(overrides)-set(STANDARD):
        raise ValueError("Invalid profile_overrides; only known style keys allowed")
    style.update(overrides)
    return style

def label_fontsize(config,size):
    if config.get("render_profile","standard")=="social_square":
        return max(float(size),resolve_style(config)["annotation_fontsize"])
    return size

def footer_left(config):
    return BRAND_FOOTER if config.get("render_profile","standard")=="social_square" else config.get("footer_left","")
