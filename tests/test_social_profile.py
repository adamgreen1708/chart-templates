"""Social variant is opt-in and the existing standard remains unchanged."""
import pytest
from src.chart_style import resolve_style, label_fontsize, footer_left, SOCIAL_SAFE_MARGIN

def test_standard_retains_project_values():
    st=resolve_style({"title_fontsize":21,"subtitle_fontsize":11,"footer_fontsize":8})
    assert (st["title_fontsize"],st["subtitle_fontsize"],st["footer_fontsize"])==(21,11,8)

def test_standard_missing_footer_preserves_previous_empty_value():
    assert footer_left({}) == ""

def test_social_overrides_legacy_sizes():
    cfg={"render_profile":"social_square","title_fontsize":19,"subtitle_fontsize":8}
    st=resolve_style(cfg)
    assert (st["title_fontsize"],st["subtitle_fontsize"],st["tick_label_fontsize"])==(26,16,12)
    assert label_fontsize(cfg,8)==11.5
    assert footer_left(cfg)=="Adam Green | coffeetableviz"

def test_profile_exceptions_are_explicit():
    assert resolve_style({"render_profile":"social_square","profile_overrides":{"subtitle_fontsize":17}})["subtitle_fontsize"]==17

def test_invalid_profile_rejected():
    with pytest.raises(ValueError):
        resolve_style({"render_profile":"unknown"})
    with pytest.raises(ValueError):
        resolve_style({"render_profile":"social_square","profile_overrides":{"unapproved":1}})


def test_social_shared_safe_frame():
    st = resolve_style({"render_profile":"social_square"})
    assert SOCIAL_SAFE_MARGIN == .085
    assert st["title_x"] == st["subtitle_x"] == st["footer_left_x"] == .09
    assert st["footer_right_x"] == .91
    assert st["title_y"] == .91 and st["footer_y"] == .09
    assert st["plot_left"] > st["title_x"] and st["plot_right"] < st["footer_right_x"]



def test_new_chart_template_uses_approved_house_vnext_by_default():
    from src.chart_config_template import CHART_CONFIG as template
    from src.chart_style import PRODUCTION_PROFILE
    assert PRODUCTION_PROFILE == "social_square"
    assert template["render_profile"] == PRODUCTION_PROFILE
    assert template["profile_overrides"] == {}
    style = resolve_style(template)
    assert (style["title_fontsize"], style["subtitle_fontsize"]) == (26, 16)
    assert (style["tick_label_fontsize"], style["axis_label_fontsize"]) == (12, 12)
    assert (style["title_x"], style["footer_right_x"]) == (.09, .91)
    assert style["plot_bottom"] == .22
    assert footer_left(template) == "Adam Green | coffeetableviz"


def test_old_configs_keep_legacy_layout_until_migrated():
    legacy = {"title_fontsize": 21, "subtitle_fontsize": 11, "plot_bottom": .14}
    style = resolve_style(legacy)
    assert style["subtitle_fontsize"] == 11
    assert style["plot_bottom"] == .14
    assert label_fontsize(legacy, 8) == 8
