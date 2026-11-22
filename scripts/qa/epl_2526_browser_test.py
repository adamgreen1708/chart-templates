#!/usr/bin/env python3
"""Real-browser PR QA for the EPL 2025–26 Coffeetableviz interactive.
Run at repository root after serving it over HTTP on port 8765.
No fabricated matches; read JSON, JS and CSS from checked-out PR branch.
"""
from __future__ import annotations
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8765/preview/epl-2025-26/index.html"
OUTPUT = Path("qa_screenshots/epl-2526")
OUTPUT.mkdir(parents=True, exist_ok=True)
checks = []

def verify(condition, message):
    if not condition:
        raise AssertionError(message)
    checks.append(message)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, args=["--no-sandbox"])
    for width, height in [(1440, 960), (390, 844), (320, 760)]:
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1, has_touch=width<500, is_mobile=width<500)
        errors=[]
        page.on("pageerror", lambda error: errors.append(str(error)))
        response = page.goto(BASE, wait_until="domcontentloaded", timeout=30000)
        verify(response is not None and response.status==200, f"{width}px: review URL returns HTTP 200")
        page.locator("#eplu-calendar .eplu-match").first.wait_for(timeout=30000)
        verify(not errors, f"{width}px: no JavaScript errors: {errors}")
        verify(page.locator("#eplu-calendar .eplu-match").count()==38, f"{width}px: 38 real results rendered")
        verify(page.locator("#eplu-calendar .eplu-month").count()==10, f"{width}px: ten months rendered")
        verify(page.locator("#eplu-totals-body tr").count()==2, f"{width}px: home and away totals rendered")
        verify(page.locator("#eplu-points-svg g[data-club]").count()==20, f"{width}px: all 20 club badges rendered")
        name=page.locator("#eplu-club-name").inner_text().strip()
        verify(name=="ARSENAL", f"{width}px: default is Arsenal")
        ranks=page.locator("#eplu-rank").inner_text()
        verify(ranks=="1", f"{width}px: Arsenal finishing position correct")
        columns=page.locator("#eplu-calendar").evaluate("(el)=>getComputedStyle(el).gridTemplateColumns.split(' ').length")
        verify(columns==10, f"{width}px: one-row August–May calendar")
        levels=page.locator(".eplu-month").evaluate_all("(els)=>els.map(el=>el.getBoundingClientRect().top)")
        verify(max(levels)-min(levels)<3, f"{width}px: all months align on the same row")
        over=page.evaluate("()=>document.documentElement.scrollWidth>window.innerWidth+2")
        verify(not over, f"{width}px: no horizontal page overflow")
        # Tap a real result to pin tooltip. This must include the cumulative plot.
        first=page.locator("#eplu-calendar .eplu-match").first
        first.click()
        tooltip=page.locator("#eplu-tooltip")
        verify(tooltip.is_visible(), f"{width}px: tap opens pinned tooltip")
        verify(tooltip.locator("svg.eplu-tip-mini path").count()==20, f"{width}px: 20 cumulative trajectories visible")
        verify(tooltip.locator("svg.eplu-tip-mini circle").count()==2, f"{width}px: selected-match marker visible")
        verify(page.locator("#eplu-calendar .eplu-match.is-muted").count()==37, f"{width}px: unselected results fade")
        background=tooltip.evaluate("(el)=>getComputedStyle(el).backgroundColor")
        verify(background=="rgba(48, 49, 51, 0.45)", f"{width}px: 45% glass background: {background}")
        blur=tooltip.evaluate("(el)=>getComputedStyle(el).backdropFilter")
        verify("blur(2px)" in blur, f"{width}px: 2px blur")
        tip_box=tooltip.bounding_box()
        viz_box=page.locator("#eplu-viz").bounding_box()
        verify(tip_box is not None and viz_box is not None and tip_box["x"]>=viz_box["x"]-2 and tip_box["x"]+tip_box["width"]<=viz_box["x"]+viz_box["width"]+2, f"{width}px: tooltip stays within visualisation horizontally")
        # A screenshot of the crucial selected-tooltip state.
        page.screenshot(path=str(OUTPUT / f"selected_{width}.png"), full_page=True)
        first.click()
        verify(not tooltip.is_visible(), f"{width}px: tapping selected result again closes tooltip")
        verify(page.locator("#eplu-calendar .eplu-match.is-muted").count()==0, f"{width}px: context resets on deselection")
        page.locator("#eplu-team").select_option(label="Newcastle")
        verify(page.locator("#eplu-club-name").inner_text().strip()=="NEWCASTLE", f"{width}px: club selection changes identity")
        verify(page.locator("#eplu-calendar .eplu-match").count()==38, f"{width}px: new club has 38 real matches")
        page.screenshot(path=str(OUTPUT / f"newcastle_{width}.png"), full_page=True)
        # Regression from real iPhone screenshot: home results must clear the month baseline.
        for club_name in ("West Ham", "Arsenal"):
            page.locator("#eplu-team").select_option(label=club_name)
            monthly = page.locator("#eplu-calendar .eplu-month").evaluate_all("""els => els.map(month => {
                const home = [...month.querySelectorAll('.eplu-month-home button')];
                const away = [...month.querySelectorAll('.eplu-month-away button')];
                const baseline = month.querySelector('.eplu-month-name').getBoundingClientRect();
                return {
                  month: month.getAttribute('aria-label'),
                  labelTop: baseline.top,
                  homeBottom: home.length ? home.at(-1).getBoundingClientRect().bottom : null,
                  awayTop: away.length ? away[0].getBoundingClientRect().top : null,
                  homeMatchNumbers: home.map(b => Number(b.dataset.match)),
                  awayMatchNumbers: away.map(b => Number(b.dataset.match)),
                };
            })""")
            for month in monthly:
                if month["homeBottom"] is not None:
                    gap = month["labelTop"] - month["homeBottom"]
                    verify(7 <= gap <= 10, f"{width}px {club_name} {month['month']}: home results clear month baseline by 8px (actual {gap:.1f}px)")
                    verify(month["homeMatchNumbers"] == sorted(month["homeMatchNumbers"], reverse=True),
                           f"{width}px {club_name} {month['month']}: earliest home match nearest centre")
                if month["awayTop"] is not None:
                    verify(month["awayMatchNumbers"] == sorted(month["awayMatchNumbers"]),
                           f"{width}px {club_name} {month['month']}: earliest away match nearest centre")
            page.screenshot(path=str(OUTPUT / f"home_gap_{club_name.lower().replace(' ', '_')}_{width}.png"), full_page=True)
        page.locator("#eplu-team").select_option(label="Man City")
        verify(page.locator("#eplu-club-name").inner_text().strip()=="MAN CITY", f"{width}px: second club change works")
        verify(not errors, f"{width}px: still no JavaScript errors")
        page.close()
    browser.close()

OUTPUT.joinpath("checks.json").write_text(json.dumps({"checks":checks,"passed":len(checks)},indent=2)+"\n")
print(f"PASS: {len(checks)} checks across 1440px, 390px, 320px.")
for check in checks: print(" ✓ "+check)
