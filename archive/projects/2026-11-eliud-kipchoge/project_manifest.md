# Eliud Kipchoge — The record fell. The legacy didn't.

Status: **editorial / production preview only**. No Jekyll post or site assets are included.
Date: 2026-11-16. Category intended for site publication: Sport.

## Source and scope
- Fixed source CSV: https://github.com/adamgreen1708/chart-templates/blob/2e784456670858668696c016fc5ea44ef9d4228d/data/marathon-majors/marathon_major_winners_men_2000_2026.csv
- The project reads the repository-local original path `data/marathon-majors/marathon_major_winners_men_2000_2026.csv`, without modifying it.
- This is the six-marathon dataset, not every marathon or the entire present-day seven-race Majors series.
- The source includes 154 rows, 149 completed events; several results elsewhere in the file remain explicitly flagged or unverified.
- Boston/New York 2026 and other non-Kipchoge rows with source flags are not silently treated as independently confirmed.
- **2026 Berlin is missing** from the source CSV, so the coverage is not a complete inventory of all 2026 editions. All ranks are explicitly scoped to included observations.
- One name alias is canonicalised for counts: `Robert Cheruiyot` -> `Robert Kipkoech Cheruiyot`.
- Tokyo's 2021-labelled edition was held 6 March 2022. Chart 2 plots the actual year, not the race's edition year.
- Chart 2 shows winning performances only, not every attempted marathon or chronological career races.
- World-record comparisons use an official 2002 baseline and ten subsequent record improvements through April 2026. These are changes in **official** records; Kipchoge's unofficial INEOS 1:59 event is not treated as a world record.
- Winners, record times, and quantitative values are derived and validated by `scripts/build_chart_views.py`. Outputs regenerate during `render-archived-project.yml`.

## External verification
- Eliud Kipchoge major wins and 2016 London: https://www.londonmarathonevents.co.uk/london-marathon/article/legendary-eliud-kipchoge-race-2025-tcs-london-marathon
- World Athletics Berlin 2018 2:01:39 (78-second WR improvement): https://worldathletics.org/awards/news/berlin-marathon-2018-eliud-kipchoge-world-rec
- World Athletics Berlin 2022 2:01:09 (30-second WR improvement): https://worldathletics.org/news/press-releases/ratified-record-kipchoge-marathon-tebogo-jamaica
- World Athletics London 2026 1:59:30 (65-second WR improvement): https://worldathletics.org/news/report/sawe-two-hour-assefa-world-record-london-marathon
- Tokyo 2021 edition held March 2022: https://www.marathon.tokyo/en/media/press-release/pdf/210917release_en.pdf

## Editorial sequence
1. **Eleven wins. Next best: five.** — scale of dominance.
2. **Four years. Two world records.** — winning times fluctuate; two Berlin performances stand out.
3. **The 78-second leap still leads.** — record improvement remains largest since 2002.

## Workflow / QA
- All 3 configs use the approved `social_square` renderer.
- Script validates original counts, winner-time consistency, 11 wins, and 78/65s changes.
- Render all three through the archive project's push-triggered workflow.
- Before acceptance inspect final exported 1600px and 390/320px previews, outer 7% clear frame, labels/title/footer and plot colour.
- Do not add `publish_asset_map.csv` or site/_posts before explicit approval.

## Render review correction (16 November 2026)
The first successful GitHub render revealed clipped and unsafe left-side labels on the two ranked dot charts. Both dot configs now use an explicitly documented social-square `profile_overrides` of `plot_left=0.29` and `plot_right=0.88` so that names remain inside the 7% border. The scatter chart keeps the canonical shared profile unchanged. Reinspect the final full-size and mobile exports; a green workflow is not by itself visual QA.

## Editorial QA adjustment
Chart 2 title revised to avoid falsely implying monotonically improving times. Across wins, times fluctuate because courses and conditions differ; 2018 and 2022 are the two verified world records.

The longer second-chart headline wrapped into the subtitle on the actual rendered PNG, so it was shortened rather than shrinking production typography. Final output must be reinspected at full resolution and 320px.
