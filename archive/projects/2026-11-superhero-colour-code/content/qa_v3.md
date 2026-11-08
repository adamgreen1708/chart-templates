# V3 chart art-direction QA — reproducible comic palette

**Status:** Creative prototypes for review only. Not an approved article, measurement or release.

## GitHub execution
- [Actual GitHub-rendered three new 1600×1600 PNGs](https://github.com/adamgreen1708/chart-templates/actions/runs/42474298588) — success.
- [V3 dataset tests, pixel margins and 320px/390px exports](https://github.com/adamgreen1708/chart-templates/actions/runs/42474545085) — success.
- Verified all 24 source-character records remain the basis of the wheel's 24 sectors. No character was duplicated in a cohort. Wheel counters are computed from 8/12 heroes and 3/12 villains; subgroup labels are DC 3/6 vs 1/6 and Marvel 5/6 vs 2/6.
- The 12-character gallery reproduces exact main/second/accent hue values from the project CSV. The five showdowns have equal coded main hue on both sides, different supporting hues and documented roles.
- Native full-size images were visually inspected for title/deck collisions, off-canvas text, semantic hue encoding, legible names and 7% margins. Final **320px and 390px** exports inspected individually for clipping and overlap. All look clear in the delivered form, though typography is necessarily compact on the six-row line-up at 320px.

## Native output
- `output/superhero_v3_01_comic_lineup.png`
- `output/superhero_v3_02_colour_wheels.png`
- `output/superhero_v3_03_showdowns.png`

## Phone previews
- `output/qa_v3/superhero_v3_01_comic_lineup_320.png`, `*_390.png`
- `output/qa_v3/superhero_v3_02_colour_wheels_320.png`, `*_390.png`
- `output/qa_v3/superhero_v3_03_showdowns_320.png`, `*_390.png`

## Data and release caveat
- All 24 costumes remain provisional manually coded interpretations, pending character-/issue-specific artwork verification.
- Equal chips and equal wheel sectors encode categorical observations, **not fabric-area percentages**.
- Groups were purposively curated for editorial comparison; no claims about all Marvel/DC characters are justified.
- Do not overwrite V2 imagery or merge PRs #192/#193 without approval. This branch is for review; no live `site/` files were changed.

## Final editorial changes (8 November 2026)
- **Chart 3 symmetry:** Moved the villain `+ colour` label anchor from figure-x `0.867` to **`0.895`**, matching the right edge of the villain names; the villain secondary-colour square stays at `x=0.652`, opposite the hero square at `x=0.326`. No row values or other chart geometry were changed.
- [GitHub archived-project rerender](https://github.com/adamgreen1708/chart-templates/actions/runs/42475773318) **passed**, producing the revised `output/superhero_v3_03_showdowns.png`.
- **Chart 2 blog reference:** `content/blog_draft_v3.md` includes a **12-row / 24-character** compact table, immediately below the wheel. It is generated from the exact `data/chart_v2_02_role_scorecard.csv` powering the wheels, with the DC and Marvel display order preserved for each role. The table is a reference list, not cross-publisher pairings. Bold colour words mark strict traditional RYB primaries.
- Regeneration: `scripts/build_blog_draft_v3.py` reads `content/blog_draft_v3.template.md` and the source scorecard; `tests/test_palette_blog_table_v3.py` verifies that the checked-in draft exactly matches its regenerated output and includes all 24 characters.
- [GitHub pytest and updated phone-size QA](https://github.com/adamgreen1708/chart-templates/actions/runs/42475851357) **passed**, including source data alignment, safe frame and 320px/390px PNG exports. Both final chart 3 mobile PNGs were visually inspected; text is right-aligned without crowding, collisions or clipping.
- The one-off workflow used for this check was removed from the branch after passing; routine project rendering remains unchanged.
