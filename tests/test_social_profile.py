"""Social variant is opt-in and the existing standard remains unchanged."""
import pytest
from src.chart_style import resolve_style, label_fontsize, footer_left

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
