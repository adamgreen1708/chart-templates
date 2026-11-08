"""Browser QA for Pixel Universe: real Jekyll HTML at phone and desktop sizes.

Called from .github/workflows/pixel-universe-gallery-qa.yml after the Jekyll
build. Screenshots are GitHub Actions artifacts for visual review.
"""
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8765"
OUT = Path("output/pixel-universe-mobile-qa")
OUT.mkdir(parents=True, exist_ok=True)


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for width, expected_columns in ((320, 1), (390, 1), (768, 2), (1280, 3)):
            page = browser.new_page(viewport={"width": width, "height": 850}, device_scale_factor=1)
            page.goto(BASE + "/resources/pixel-universe/", wait_until="networkidle", timeout=45000)
            assert page.title(), "Jekyll page missing a title"
            assert page.locator(".pu-card").count() == 12
            assert page.locator("#heroes .pu-card").count() == 6
            assert page.locator("#villains .pu-card").count() == 6
            assert page.locator(".pu-mosaic img").count() == 2
            links = page.locator("a.pu-open")
            assert links.count() == 12
            for link in links.all():
                href = link.get_attribute("href")
                assert href is not None
                assert re.fullmatch(
                    r"/resources/8x8-pixel-art-builder/#size=16&art=[0-9a-f]{256}", href
                ), "Broken edit link: " + repr(href)
            dimensions = page.evaluate("""() => {
              const root = document.documentElement;
              const grid = document.querySelector('.pu-grid');
              const page = document.querySelector('.pu-page');
              const images = Array.from(document.querySelectorAll('.pu-page img'));
              const cards = Array.from(document.querySelectorAll('.pu-card'));
              return {
                viewport: window.innerWidth,
                documentWidth: root.scrollWidth,
                gridColumns: getComputedStyle(grid).gridTemplateColumns.trim().split(/\\s+/).length,
                minCardLeft: Math.min(...cards.map(e => e.getBoundingClientRect().left)),
                maxCardRight: Math.max(...cards.map(e => e.getBoundingClientRect().right)),
                pageLeft: page.getBoundingClientRect().left,
                pageRight: page.getBoundingClientRect().right,
                imagesLoaded: images.every(img => img.complete && img.naturalWidth > 0)
              };
            }""")
            assert dimensions["documentWidth"] <= width + 1, "Horizontal overflow at " + str(width) + ": " + str(dimensions)
            assert dimensions["gridColumns"] == expected_columns, "Wrong responsive grid: " + str(dimensions)
            assert dimensions["minCardLeft"] >= -1
            assert dimensions["maxCardRight"] <= width + 1
            assert dimensions["pageLeft"] >= -1 and dimensions["pageRight"] <= width + 1
            assert dimensions["imagesLoaded"], "Gallery artwork failed to load: " + str(width)
            page.screenshot(path=str(OUT / f"pixel-universe-{width}px.png"), full_page=True)
            if width == 390:
                # Genuine click-through checks the deployed page's exact permalink,
                # hash format, and that the existing Studio loads the 256-cell canvas.
                links.first.click()
                page.wait_for_url(re.compile(r"/resources/8x8-pixel-art-builder/#size=16&art=[0-9a-f]{256}"))
                assert page.locator(".pixel-cell").count() == 256
                assert page.locator("#pixel-count").inner_text().endswith("/ 256 painted")
                page.screenshot(path=str(OUT / "pixel-studio-open-and-remix-390px.png"), full_page=True)
            print(f"PASS browser/mobile gallery {width}px ({expected_columns} columns)")
            page.close()
        browser.close()


if __name__ == "__main__":
    main()
