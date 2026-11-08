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
