"""Fail social QA for chart bleed, white plot cards or wrong dimensions.

Visual inspection at 390px/320px is still required in addition to these
basic pixel tests. This script checks **rendered PNGs**, not declarations.
"""
from pathlib import Path
import numpy as np
from PIL import Image

BACKGROUND = np.array([243, 244, 246], dtype=np.int16)
SAFE_BORDER_FRACTION = 0.07
MAX_WHITE_PLOT_FRACTION = 0.02


def check_chart(path: Path) -> None:
    im = Image.open(path).convert("RGB")
    assert im.size == (1600, 1600), (path, im.size)
    pixels = np.asarray(im, dtype=np.int16)
    h, w, _ = pixels.shape
    margin = round(w * SAFE_BORDER_FRACTION)

    # Reject all text/marks encroaching into the 7% minimum safe band.
    # Antialiased pixels and tiny background differences are ignored.
    dark_or_coloured = np.max(np.abs(pixels - BACKGROUND), axis=2) > 35
    strips = {
        "top": dark_or_coloured[:margin, :],
        "bottom": dark_or_coloured[-margin:, :],
        "left": dark_or_coloured[:, :margin],
        "right": dark_or_coloured[:, -margin:],
    }
    for side, region in strips.items():
        count = int(region.sum())
        assert count == 0, f"{path.name} breaches {side} outer 7% margin: {count} coloured pixels"

    # The chart body must share the grey canvas; no white rectangular plot card.
    body = pixels[int(h * 0.30):int(h * 0.65), int(w * 0.48):int(w * 0.82)]
    pure_white = np.all(body >= 252, axis=2)
    proportion = float(np.mean(pure_white))
    assert proportion < MAX_WHITE_PLOT_FRACTION, (
        f"{path.name} has a likely white plot card: {proportion:.1%} of central plot region"
    )
    print(f"PASS: {path.name} | outer margin >=7%, central-white {proportion:.2%}")


if __name__ == "__main__":
    paths = sorted(Path("archive/projects").glob("2026-10-*/output/social_review_*.png"))
    assert len(paths) == 3, f"Expected 3 chart previews; found {len(paths)}"
    for item in paths:
        check_chart(item)
