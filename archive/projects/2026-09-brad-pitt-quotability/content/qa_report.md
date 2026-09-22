# Brad Pitt quotability — render QA report

## QA date

23 September 2026

## Method

The three project configs were rendered locally against the current locked `src/render_538.py` behaviour before repository output commit. No renderer or template file was changed.

## First pass

All three charts rendered successfully at 1600 × 1600, but visual inspection found:

- long two-line titles colliding with subtitles;
- long source text colliding with the left footer in Charts 1 and 2;
- insufficient bottom spacing around axis labels/footer.

## Project-level fixes

Only the three project configs were changed:

- reduce title font size from 22 to 20;
- tighten chart-specific title wrap widths;
- move title to `0.94`;
- move subtitle to `0.81`;
- move footer to `0.055`;
- increase plot bottom to `0.18`;
- shorten source text;
- shorten Chart 1 headline to “Fury started it. Tyler Durden owns the answer.”

## Second pass

PASS.

- Chart 1: no clipping; long role labels fit; Tyler and Wardaddy annotations clear; Fury remains red.
- Chart 2: no clipping; five annotations remain readable; Fury remains red; trend line clear.
- Chart 3: no clipping; zero baseline retained; all three Ocean's labels clear.
- All outputs: 1600 × 1600.
- Renderer/template files: unchanged.

## Next gate

Create the exact repository PNG outputs through the GitHub archived-project render path and verify them before Adam's visual approval/publication stage.
