# Redesign v2 — real GitHub render and mobile QA results

**Date:** 7 November 2026  
**Status:** Layout and data-contract checks passed on draft assets; **all 24 costume image/code references remain provisional**. No production publication.

## GitHub workflows actually executed
- [Three v2 final renders produced by GitHub](https://github.com/adamgreen1708/chart-templates/actions/runs/42421383137): **success**; `src/render_538.py` registered `palette_story` and rendered the gallery, scorecard and five colour twins as 1600×1600 PNGs.
- [V2 contract and 320px/390px PNG export QA](https://github.com/adamgreen1708/chart-templates/actions/runs/42421609455): **success**. Tests compare derived views against the real 24-character pilot, verify all role/publisher cohorts, enforce colour twin matches and social_square configs.
- Actual exported 1600px images were visually inspected after rendering and a title-overlap issue in chart 2 was corrected. All six final 320px and 390px resized PNGs were inspected for title/deck collision, names, colour chips, contrast, footers, and four-edge clipping.
- The QA script `scripts/qa_palette_v2.py` checks image size 1600×1600, background `#F3F4F6`, significant-foreground safe margins ≥7% on all four edges, and exports phone reviews.
- The temporary branch-only QA workflow file was removed after execution. The script and tests remain with this redesign.

## Assets for review
- `output/superhero_v2_01_costume_gallery.png`
- `output/superhero_v2_02_role_scorecard.png`
- `output/superhero_v2_03_colour_twins.png`
- `output/qa_v2/*_320.png` and `output/qa_v2/*_390.png` for each chart.
- `config/chart_v2_01_costume_gallery.py`, `chart_v2_02_role_scorecard.py`, `chart_v2_03_colour_twins.py`
- `content/blog_draft_v2.md`
- `content/editorial_v2.md`

## What changed versus rejected v1
- Main/second/accent ordered hue fingerprints let the **person** back into the story, without made-up suit-area percentages.
- Twenty-four named source characters underpin a two-role/four-publisher scorecard with actual colour tiles, not just four anonymous bars.
- Five independently derived cross-alignment matches turn the ending into a concrete question about the meaning of a main colour.
- The titles introduce a human question, a conflict, and a reveal instead of using generic category descriptions.
- The new graph type is integrated in `src/editorial_palette.py` via GitHub's shared renderer with the approved social_square header, footer and page style. This is an opt-in new renderer feature, not a redesign of all existing charts.

## Still blocked
Full-body comic-art/issue-level provenance and reliable dominant-colour determination for all 24 costume versions remain incomplete. Publisher URLs frequently give background rather than a measured or exact suit reference. No claims about all Marvel/DC characters, fabric-area percentages, colour causality or representativeness should be published. Explicit editorial approval and separate Jekyll site PR are required.
