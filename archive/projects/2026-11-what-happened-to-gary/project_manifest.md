# What Happened to Gary? — research and review branch

**Status:** source-analysis and chart-render trial; NOT publication-approved.

**Question:** How did Gary rise from rare in England and Wales to the 16th-ranked boys' name in 1964, then become uncommon among newborns? Is Gary exceptional, and did famous Garys help?

## Source contract
- Geography: **England and Wales only**, not all of the UK.
- Historical 1904–1994: ONS/General Register Office decade top-100 **ranks**, not counts. Five actual ranked Gary observations in `data/gary_historical_ranks.csv`. He is absent in 1994; do not chart an invented rank.
- Annual 1996–2024: exact first-name counts and ranks from the ONS-derived CSV curated by TidyTuesday 2026-06-16; upstream Git blob hash is checked before processing. The file's years, counts and sex are validated by `scripts/build_chart_views.py`.
- 2025: the ONS has released it; the source CSV in this build stops in 2024. An externally reported **six** Gary registrations for 2025 is *not* in the charted dataset; do not silently claim it is. Upgrade to the primary ONS 2025 workbook after a separate source verification.
- Counts under three are suppressed and cannot be treated as zero.
- Source URLs:
  - https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesenglandandwalestop100babynameshistoricaldata
  - https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/datasets/babynamesinenglandandwalesfrom1996
  - https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-06-16/england_wales_names.csv
  - https://www.behindthename.com/name/gary/top/england-wales-historical/

## Competing hypotheses — pre-chart editorial gate
1. **A post-war import:** Gary jumps from #95 (1944) to #16 (1964). Its timing is consistent with a possible Gary Cooper cultural influence, not proof. Need to test difference from other rising imported names.
2. **Long goodbye:** annual baby Gary registrations contract after 1996. Test magnitude and shape vs Nigel, Wayne, Barry and Kevin; avoid saying unique if peer declines are similar.
3. **The generation gap:** Arthur revives while Gary does not. Test both annual series, and whether the popular reversal is more distinctive than the other peers.

## Trial three-chart editorial sequence
1. Historical decade rank snapshots (no fabricated annual historical curve).
2. Gary's measured annual 1996–2024 registration series.
3. Gary–Arthur annual contrast, only if it earns its place against alternative peers.

## Cultural hypothesis to investigate
- Gary Cooper's rise as a film star is historically credited with popularising the stage name in the US. UK timing aligns loosely; no British causal result established.
- Gary Lineker, Gary Barlow, Gary Oldman and other later celebrities: choose public-event dates through independently verified sources, check annual changes rather than decorating the timeline with names. Do not overinterpret celebrities already bearing the name as drivers of parent behaviour.
- If later fame did not lift registrations, that may itself be the most interesting contrast, contingent on data.

## QA/publishing gates
1. Build derived CSV and `story_evidence.md` on GitHub CI with pinned source-hash verification.
2. Test every statistical claim and peer selection using the resulting data.
3. Inspect rendered original 1600px and exact 390px and 320px phone versions, margins, labels, footers and axis semantics.
4. Revisit/chart-edit or discard weak graphics before user review.
5. No Jekyll post, site asset copying, live publication or merge without user approval.

## QA-only output
The project opts into reproducible 390px and 320px downscaled inspection PNGs using `qa_mobile.enabled`. These are not independently authored data charts and will not be copied to the live website.

## 20 November editorial revision
- Historical Chart 1 was trialled as a rank-standing bar but superseded by a rank-versus-year slopegraph (No. 1 at the top). The final chart displays only five observed decade rankings, highlights 1964, and labels each verified rank. Lines are connecting guides, **not annual observations**. ONS has no pre-1996 historical birth counts.
- Chart 2 adds x/y clearance for both red endpoints. A small negative y padding is geometric only; all measured registrations remain positive.
- Chart 3's values and layout are unchanged.
- Blog revised for original gentle humour and transparent attribution to Fay Schopen's 2015 Guardian feature; celebrity associations remain hypotheses, not causal claims.
- Render and inspect all three real GitHub-produced images, plus the reproducible 390px and 320px PNGs, prior to approval.

## Approved site publication — 20 November 2026
- User approved the final historical slopegraph, all three chart renders, and the editorial copy.
- Publication mapping: `publish_asset_map.csv` copies **exact render outputs** into `site/assets/charts/gary/` on the review branch; no manual image reconstruction.
- Jekyll story: `site/_posts/2026-11-20-what-happened-to-gary.md` (Society), with Chart 2 used as factual hero/card image; no separate editorial illustration is introduced.
- Keep all main-site paths validated and merge only after the PR Pages build succeeds; then verify GitHub Pages deployment and public story URL.
