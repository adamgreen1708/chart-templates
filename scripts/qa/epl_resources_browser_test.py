#!/usr/bin/env python3
"""Browser QA: current season belongs in Resources, archived season in its post."""
from __future__ import annotations
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

SITE="http://127.0.0.1:8766"
OUTPUT=Path("qa_screenshots/epl-resources")
OUTPUT.mkdir(parents=True,exist_ok=True)
matches=json.loads(Path("site/assets/data/epl-2526-unfolded.json").read_text(encoding="utf-8"))
if matches["meta"]["matchCount"]!=380:
    raise AssertionError("2025-26 archival data must contain all 380 completed matches")
checks=[]
def verify(ok,message):
    if not ok: raise AssertionError(message)
    checks.append(message)

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=True,args=["--no-sandbox"])
    for width,height in [(1440,960),(390,844),(320,760)]:
        page=browser.new_page(viewport={"width":width,"height":height},device_scale_factor=1,is_mobile=width<500,has_touch=width<500)
        errors=[]
        page.on("pageerror",lambda error: errors.append(str(error)))
        resp=page.goto(SITE+"/resources/",wait_until="domcontentloaded",timeout=30000)
        verify(resp is not None and resp.status==200,f"{width}: Resources responds")
        feature=page.locator(".resource-feature").first
        verify(feature.get_attribute("href")=="/resources/epl-2026-27-unfolded/",f"{width}: current season featured")
        verify("2026–27" in feature.inner_text(),f"{width}: current season label")
        verify(feature.locator("img").get_attribute("src")=="/assets/features/epl-2627-season-unfolded-editorial.svg",f"{width}: 2026–27 cover art")
        verify(page.locator("a[href='/resources/epl-2025-26-unfolded/']").count()==0,f"{width}: completed season no longer listed as Resource")
        verify(not page.evaluate("document.documentElement.scrollWidth>innerWidth+2"),f"{width}: Resources no overflow")
        page.screenshot(path=str(OUTPUT/f"resources_{width}.png"),full_page=True)
        resp=page.goto(SITE+"/stories/premier-league-season-unfolded-2025-26/",wait_until="domcontentloaded",timeout=30000)
        verify(resp is not None and resp.status==200,f"{width}: archived Sport article responds")
        page.locator("#eplu-calendar .eplu-match").first.wait_for(timeout=30000)
        verify(page.locator("#epl-unfolded").count()==1,f"{width}: original interactive embedded once")
        verify(page.locator("#eplu-team option").count()==20,f"{width}: twenty real clubs available")
        verify(page.locator("#eplu-calendar .eplu-match").count()==38,f"{width}: Arsenal's 38 real matches")
        verify(page.locator("#eplu-calendar .eplu-month").count()==10,f"{width}: ten calendar months")
        verify(page.locator("#eplu-points-svg g[data-club]").count()==20,f"{width}: all twenty clubs on final-points plot")
        verify(page.locator("a[href='/resources/epl-2026-27-unfolded/']").count()==1,f"{width}: blog links to current Resource")
        verify(page.locator("#epl-2526-interactive").count()==1,f"{width}: stable deep-link anchor")
        verify(page.locator("#eplu-totals-body tr").count()==2,f"{width}: home and away table")
        verify(page.locator("#eplu-totals-body").evaluate("(el)=>getComputedStyle(el.closest('table')).display")=="table",f"{width}: embedded table not broken by blog CSS")
        page.locator("#eplu-team").select_option(label="Tottenham")
        verify(page.locator("#eplu-club-name").inner_text().strip()=="TOTTENHAM",f"{width}: archived club picker interactive")
        verify(page.locator("#eplu-calendar .eplu-match").count()==38,f"{width}: Tottenham 38 historical matches")
        page.locator("#eplu-calendar .eplu-match").first.click()
        verify(page.locator("#eplu-tooltip").is_visible(),f"{width}: historical result tooltip works")
        verify(page.locator("#eplu-tooltip svg.eplu-tip-mini path").count()==20,f"{width}: twenty club trends in archive tooltip")
        verify(not errors,f"{width}: archived story JavaScript error-free: {errors}")
        verify(not page.evaluate("document.documentElement.scrollWidth>innerWidth+2"),f"{width}: archived story no horizontal overflow")
        page.screenshot(path=str(OUTPUT/f"archive_{width}.png"),full_page=True)
        resp=page.goto(SITE+"/resources/epl-2025-26-unfolded/",wait_until="domcontentloaded",timeout=30000)
        page.wait_for_url("**/stories/premier-league-season-unfolded-2025-26/",timeout=10000)
        verify("/stories/premier-league-season-unfolded-2025-26/" in page.url,f"{width}: old URL redirects to archived story")
        verify(not errors,f"{width}: redirect no JavaScript error")
        page.close()
    browser.close()

OUTPUT.joinpath("checks.json").write_text(json.dumps({"passed":len(checks),"checks":checks},indent=2)+"\n")
print(f"PASS: {len(checks)} Resources/archive browser checks across 1440/390/320")
for check in checks:print(" ✓ "+check)
