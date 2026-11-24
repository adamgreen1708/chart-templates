#!/usr/bin/env python3
"""Real-browser PR QA for the EPL 2026–27 Coffeetableviz interactive.
Run at repository root after serving it over HTTP on port 8765.
No fabricated matches; read JSON, JS and CSS from checked-out PR branch.
"""
from __future__ import annotations
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8765/preview/epl-2026-27/index.html"
OUTPUT = Path("qa_screenshots/epl-2627")
OUTPUT.mkdir(parents=True, exist_ok=True)
checks = []
DATA=json.loads(Path("site/assets/data/epl-2627-unfolded.json").read_text(encoding="utf-8"))
CLUB={x["name"]:x for x in DATA["teams"]}
assert DATA["meta"]["matchCount"]==sum(x["played"] for x in DATA["teams"])//2

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
        stamp=page.locator("#eplu-data-stamp").inner_text()
        verify(DATA["meta"]["lastDate"][-2:]+" " in stamp or stamp.startswith("COMPLETED RESULTS THROUGH"), f"{width}px: snapshot date and provisional label are visible")
        verify(page.locator("#eplu-calendar .eplu-match").count()==CLUB["Arsenal"]["played"], f"{width}px: Arsenal completed results rendered")
        verify(page.locator("#eplu-calendar .eplu-month").count()==10, f"{width}px: ten months rendered")
        verify(page.locator("#eplu-totals-body tr").count()==2, f"{width}px: home and away totals rendered")
        verify(page.locator("#eplu-points-svg g[data-club]").count()==20, f"{width}px: all 20 club badges rendered")
        name=page.locator("#eplu-club-name").inner_text().strip()
        verify(name=="ARSENAL", f"{width}px: default is Arsenal")
        ranks=page.locator("#eplu-rank").inner_text()
        verify(int(ranks)==CLUB["Arsenal"]["rank"], f"{width}px: provisional Arsenal position correct")
        columns=page.locator("#eplu-calendar").evaluate("(el)=>getComputedStyle(el).gridTemplateColumns.split(' ').length")
        verify(columns==10, f"{width}px: one-row August–May calendar")
        levels=page.locator(".eplu-month").evaluate_all("(els)=>els.map(el=>el.getBoundingClientRect().top)")
        verify(max(levels)-min(levels)<3, f"{width}px: all months align on the same row")
        over=page.evaluate("()=>document.documentElement.scrollWidth>window.innerWidth+2")
        verify(not over, f"{width}px: no horizontal page overflow")
        # Verify the latest completed fixture gets the only glass halo by default.
        latest=page.locator("#eplu-calendar .eplu-match.is-latest")
        verify(latest.count()==1, f"{width}px: exactly one latest-result glass halo by default")
        verify(latest.get_attribute("data-match")==str(CLUB["Arsenal"]["played"]),
               f"{width}px: halo follows Arsenal's actual last completed match")
        verify("latest completed result" in latest.get_attribute("aria-label"),
               f"{width}px: latest result announced accessibly")
        halo_style=latest.evaluate("""el => {
            const pseudo=getComputedStyle(el,'::before');
            return {
                content:pseudo.content,
                border:pseudo.borderStyle,
                radius:pseudo.borderRadius,
                shadow:pseudo.boxShadow,
                gradient:pseudo.backgroundImage,
                blur:pseudo.filter,
                layer:pseudo.zIndex,
                top:pseudo.top,
                bottom:pseudo.bottom,
                left:pseudo.left,
                right:pseudo.right,
                extra:getComputedStyle(el,'::after').content
            };
        }""")
        verify(halo_style["content"] not in ("none","normal")
               and halo_style["border"]=="none"
               and halo_style["radius"]=="0px"
               and halo_style["shadow"]=="none"
               and "radial-gradient" in halo_style["gradient"]
               and halo_style["layer"]=="-1"
               and "blur(" in halo_style["blur"]
               and halo_style["extra"] in ("none","normal"),
               f"{width}px: latest result has a diffuse gradient without any outlined circle or circular shadow")
        verify(halo_style["top"]=="0px" and halo_style["bottom"]=="0px"
               and halo_style["left"]=="-9px" and halo_style["right"]=="-9px",
               f"{width}px: glow widens sideways only, preserving vertical space between home/away dots")
        # Existing match-dot geometry must remain unchanged, including the tight home stack.
        halo_geometry=latest.evaluate("""el => {
            const dot=el.getBoundingClientRect();
            const peers=[...el.parentElement.querySelectorAll('.eplu-match')].filter(p=>p!==el);
            return {gap:peers.length?Math.min(...peers.map(p=>{
                const b=p.getBoundingClientRect();
                return Math.max(0,Math.max(b.top-dot.bottom,dot.top-b.bottom));
            })):null};
        }""")
        verify(halo_geometry["gap"] is None or halo_geometry["gap"]>=3,
               f"{width}px: adjacent match-result dot spacing is unchanged")
        page.screenshot(path=str(OUTPUT / f"latest_halo_arsenal_{width}.png"), full_page=True)
        # Tap a real result to pin tooltip. This must include the cumulative plot.
        first=page.locator("#eplu-calendar .eplu-match").first
        first.click()
        verify(page.locator("#eplu-calendar .eplu-match.is-latest").count()==0,
               f"{width}px: selecting any match hides the latest-result halo")
        tooltip=page.locator("#eplu-tooltip")
        verify(tooltip.is_visible(), f"{width}px: tap opens pinned tooltip")
        verify(tooltip.locator("svg.eplu-tip-mini path").count()==20, f"{width}px: 20 cumulative trajectories visible")
        verify(tooltip.locator("svg.eplu-tip-mini circle").count()==2, f"{width}px: selected-match marker visible")
        verify(str(max(t["played"] for t in DATA["teams"])) in tooltip.locator("svg.eplu-tip-mini").get_attribute("aria-label"), f"{width}px: points trend scales to completed match counts")
        # The in-season miniature trend must use the actual highest verified points, not a fixed 90.
        # Preserve a zero baseline and a consistent shared scale when switching clubs.
        current_points_cap=max(1,*(t["points"] for t in DATA["teams"]))
        expected_y_ticks=["0",str((current_points_cap+1)//2),str(current_points_cap)]
        # A 0/1-point opening snapshot has fewer distinct labels; avoid duplicates.
        expected_y_ticks=list(dict.fromkeys(expected_y_ticks))
        svg=tooltip.locator("svg.eplu-tip-mini")
        y_ticks=svg.locator("text").all_text_contents()[:len(expected_y_ticks)]
        verify(y_ticks==expected_y_ticks, f"{width}px: tooltip y axis shows current shared max {current_points_cap}, not 90 (actual {y_ticks})")
        verify(f"Points scale 0 to {current_points_cap}" in svg.get_attribute("aria-label"), f"{width}px: tooltip accessibility describes dynamic points axis")
        # Approved design animates opacity for 150 ms. Wait for the stable 43% state.
        page.wait_for_function("""() => {
            const dot=document.querySelector("#eplu-calendar .eplu-match.is-muted");
            return dot && Math.abs(parseFloat(getComputedStyle(dot).opacity)-0.43)<0.02;
        }""", timeout=3000)
        faded=page.locator("#eplu-calendar .eplu-match.is-muted").first.evaluate("(el)=>getComputedStyle(el).opacity")
        verify(abs(float(faded)-.43)<.02, f"{width}px: unselected markers retain 43% opacity")
        verify(page.locator("#eplu-calendar .eplu-match.is-muted").count()==CLUB["Arsenal"]["played"]-1, f"{width}px: unselected results fade")
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
        verify(page.locator("#eplu-calendar .eplu-match.is-latest").count()==1,
               f"{width}px: latest halo returns after deselecting")
        # Choose examples from the real JSON so both home- and away-latest results are tested.
        venues={v:next(c for c in DATA["teams"] if c["games"][-1]["venue"]==v) for v in ("H","A")}
        for venue,club in venues.items():
            page.locator("#eplu-team").select_option(label=club["name"])
            marker=page.locator("#eplu-calendar .eplu-match.is-latest")
            verify(marker.count()==1 and marker.get_attribute("data-match")==str(club["played"]),
                   f"{width}px {club['name']}: changing club repositions halo to last completed result")
            parent_class=marker.locator("xpath=..").get_attribute("class")
            verify(("eplu-month-home" if venue=="H" else "eplu-month-away") in parent_class,
                   f"{width}px {club['name']}: halo sits in correct {'home' if venue=='H' else 'away'} row")
            stable_match=page.locator(f"#eplu-calendar .eplu-match[data-match='{club['played']}']")
            marker.click()
            verify(page.locator("#eplu-calendar .eplu-match.is-latest").count()==0
                   and page.locator("#eplu-calendar .eplu-match.is-selected").count()==1,
                   f"{width}px {club['name']}: pinned result ring takes priority over halo")
            stable_match.click()
            verify(page.locator("#eplu-calendar .eplu-match.is-latest").count()==1
                   and page.locator("#eplu-calendar .eplu-match.is-selected").count()==0,
                   f"{width}px {club['name']}: clearing selection restores last-result halo")
            page.screenshot(path=str(OUTPUT / f"latest_halo_{venue.lower()}_{width}.png"), full_page=True)
        page.locator("#eplu-team").select_option(label="Newcastle")
        verify(page.locator("#eplu-club-name").inner_text().strip()=="NEWCASTLE", f"{width}px: club selection changes identity")
        verify(page.locator("#eplu-calendar .eplu-match").count()==CLUB["Newcastle"]["played"], f"{width}px: new club has its real completed matches")
        # Changing the focused team must not rescale the twenty-club comparison.
        newcastle_match=page.locator("#eplu-calendar .eplu-match").first
        newcastle_match.click()
        verify(tooltip.locator("svg.eplu-tip-mini text").all_text_contents()[:len(expected_y_ticks)]==expected_y_ticks, f"{width}px: same league-wide points scale after switching to Newcastle")
        newcastle_match.click()
        page.screenshot(path=str(OUTPUT / f"newcastle_{width}.png"), full_page=True)
        # Regression from real iPhone screenshot: home results must clear the month baseline.
        for club_name in ("Coventry", "Arsenal"):
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
        verify("PROVISIONAL" in tooltip.inner_text().upper() or "provisional" in page.locator("#eplu-status").inner_text().lower(), f"{width}px: interim season status labelled provisional")
        page.close()
    browser.close()

OUTPUT.joinpath("checks.json").write_text(json.dumps({"checks":checks,"passed":len(checks)},indent=2)+"\n")
print(f"PASS: {len(checks)} checks across 1440px, 390px, 320px.")
for check in checks: print(" ✓ "+check)
