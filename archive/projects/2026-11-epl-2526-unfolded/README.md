# EPL 2025–26 · Season Unfolded (monthly results board)

**Status: revised draft PR #230. Not merged or published.** The reference is the user-supplied screenshot of the original 2020–21 Tableau visual.

## Fidelity to original concept

The screenshot shows:
- A restrained **dark charcoal canvas** and spaced editorial header.
- One **selected club**, with its **final league position** in a circular badge.
- Results **grouped into calendar months**. Each match is a coloured W/D/L circle, separated into **HOME (above)** and **AWAY (below)**.
- Separate compact HOME and AWAY season aggregates: **MP, W, D, L, GF, GA, GD, PTS**.
- A **horizontal final-points scale** at the bottom, positioning all 20 clubs by their final point totals, with club-crest icons.

This revised implementation mirrors that **visual grammar and storytelling sequence**, rather than showing the previous generic cumulative-points lines. It defaults to Arsenal and uses genuine 2025–26 results. On mobile, all 10 month columns remain in a **single August–May row**. The result dots shrink to 22–23px on narrow screens to fit without horizontal scrolling, while the selected match's large tooltip retains the precise score and date. The final-points rail uses clickable three-letter club badges rather than unsourced copyrighted crest artwork; this remains a deliberate visual limitation against the original.

## Source and reproducibility

- Upstream full-time results: https://www.football-data.co.uk/mmz4281/2526/E0.csv
- Frozen GitHub source commit: https://github.com/qhtexas/football-dataset/blob/9ec38fd9149216e3110d8b6edb1c0e8457d3016b/datasets/premier-league/season-2526.csv
- Git blob SHA of source: `92c659f51c53f7a0212892ed2796db8e324da74d`
- Retrieved: 21 November 2026
- Stored under `data/matches_2526.csv` (one row per real game; 380 games).
- Regenerate with `python archive/projects/2026-11-epl-2526-unfolded/scripts/build_data.py`.
- JSON at `site/assets/data/epl-2526-unfolded.json`.
- Jekyll URL after eventual approved merge: `/resources/epl-2025-26-unfolded/`.

The pinned data are grouped by **calendar month of the actual fixture date**. Every W/D/L marker is one real match, with home/away, full-time scores, opponent and date available on selection. Win dots and the club heading use a curated, season-appropriate club primary colour; contrast-adjusted text/borders remain legible for very dark or white kits. For each month, earliest home fixtures sit immediately above the centre label and later results stack upwards; earliest away fixtures sit immediately below the centre label and later results stack downwards. Month-by-venue dot stacks order matches chronologically. A month can have more/fewer fixtures, reflecting actual rescheduling.

Full season ranking is sorted by points, goal difference and goals scored. Home/away totals are recomputed from the 19 fixtures for each venue, not hard-coded. No invented historical league positions.

## Interaction contract

- Choose a team from top select or from the full 20-club bottom points strip.
- Hover match circle for a temporary tooltip, click/tap to pin. Tap the **same** dot or empty background to clear.
- Selected match remains full opacity with a ring; **other match dots fade to 43%**.
- Bottom club selection highlights its badge and leaves other club badges subdued.
- Glass tooltip background matches chart's charcoal `#303133` at **40% opacity**, with **2px backdrop blur**, subtle border and shadow. All text remains opaque.
- Mobile responsive **10-column single-row August–May display** and compact home/away summary. No horizontal scrolling in chart; dots become 22–23px at narrow widths.
- Every W/D/L dot has a screen-reader description with real home/away team names, score, date and result. No fake icons, club crests, or placeholder statistics.

## QA

- [x] 380 unique full-time matches, 20 clubs, 38 games each, 19 home / 19 away.
- [x] Final league points cross-check: Arsenal 85, Manchester City 78.
- [x] All monthly dots are produced directly from verified JSON and ordered by actual fixture date.
- [x] CSS/JS keep the approved tooltip parameters, not the earlier 50% / 15px experiment.
- [x] No changes to locked static 538/FT production renderer.
- [ ] Actual 320px/390px and desktop screenshot inspection.
- [ ] Interactive touch, hover, keyboard and accessibility review.
- [ ] New Jekyll build run for revised PR head.
- [ ] Visual sign-off and merge/publish approval.

**Technical note:** an additional date-parsing/provenance review is useful before final release. Design compares month-by-month results, not synchronized gameweek tables.
