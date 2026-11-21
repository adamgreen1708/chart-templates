# EPL 2025–26 · Season Unfolded (interactive experiment)

**Status:** draft GitHub review implementation. Not published. Does not modify the existing Patrick Stewart post, existing static renderer, or the original Tableau workbook.

## Editorial route

Three possible season lenses were tested against the verified match-level dataset:

1. **Cumulative points by each club's 1st–38th match** — selected. Lets readers explore whether clubs built up points early, late or steadily, while keeping equal match counts comparable.
2. **Official league positions by numbered matchweek** — deferred. This CSV does not include official matchweek identifiers; assigning them by sorted match dates would risk incorrect positions where fixtures were rearranged.
3. **Final-table ranking only** — rejected for the primary interaction because it hides the trajectory and does not advance the original unfolding-season idea.

Central editorial promise: *The final table tells you who finished where; the point trajectories show how each club got there.*

The linked original Tableau Public dashboard (EPL202021SeasonUnfolded/202021EPLSeason) was not inspectable through the available external page readers. This reconstruction therefore matches the broad season-unfolding premise but is **not** yet verified against the exact original layout, mark types or interactions.

## Source and reproducibility

- Upstream: Football-Data.co.uk 2025–26 E0: https://www.football-data.co.uk/mmz4281/2526/E0.csv
- Retrieved via mirror: https://github.com/qhtexas/football-dataset/blob/9ec38fd9149216e3110d8b6edb1c0e8457d3016b/datasets/premier-league/season-2526.csv
- Mirror blob SHA: `92c659f51c53f7a0212892ed2796db8e324da74d`
- Retrieved: 2026-11-21
- Frozen six-column selection: `data/matches_2526.csv` (Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR)
- Transform: `scripts/build_data.py`
- Published-browser dataset, once merged: `site/assets/data/epl-2526-unfolded.json`
- Output page (pending review and approval): `/resources/epl-2025-26-unfolded/`

Rebuild with:

```sh
python archive/projects/2026-11-epl-2526-unfolded/scripts/build_data.py
```

The transform checks 380 unique fixtures, 20 clubs, 38 matches per club, non-negative scores and result consistency, and independently verifies Arsenal 85pts / Manchester City 78pts against the official Premier League table. The browser validates the dimensions again before drawing.

## Important definitions

- One record = one Premier League match, no duplicated fixtures.
- The horizontal axis means a **club's nth completed match**, not a simultaneous calendar matchweek or a reconstructed historical table position. Rearranged fixtures are therefore not incorrectly assigned to rounds.
- The vertical axis means cumulative league points (W=3, D=1, L=0) from full-time results only.
- Each hover/tap tooltip shows the fixture and the points *after* that club's nth match; final position is always the confirmed final finishing position, not an in-season league rank.
- Ties in the *final* ranking sorted by points, goal difference, then goals scored. There are no unresolved ties on all three metrics in the 2025–26 final table.

## Interaction / visual contract

- Focus line: `#1F8FA8`; optional comparison line `#C44E52`; remaining lines grey, **43% opacity** when a club is selected.
- Tooltip: `rgba(243,244,246,0.40)` with `backdrop-filter: blur(2px)`, keeping type fully opaque.
- Hover to preview on pointer devices; tap/click to select and pin; reselect same line or click empty plot to deselect.
- Select team/compare from dropdowns; step through game 1–38; tap a row in the final standings to focus a team.
- Responsive SVG: no horizontal scrolling on standard phone widths. Check 390px and 320px in actual browser before merge.
- Layout and site assets follow existing Jekyll / GitHub Pages conventions; no changes to locked 538/FT static renderers.

## QA status / next steps

- Verified 380 fixtures and per-club 38-match histories.
- Generated JSON checked against official final totals and ranks.
- JavaScript parse succeeds.
- Remaining before editorial sign-off: real browser interaction test, iPhone touch and VoiceOver, screenshot/pixel QA at 390px and 320px, Jekyll preview build, contrast across live plot marks, exact conceptual comparison against original Tableau screenshot.
- **Do not merge or claim live deployment until approved.**
