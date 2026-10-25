# Project manifest — youngest season-long sporting champions

- Started: 2026-10-25
- Status: **Research/render script QA complete; publication package not started**
- Repo: `adamgreen1708/chart-templates`
- Slug: `2026-10-youngest-season-champions`
- Working headline: **Too young to win? Sport's youngest season champions**
- Source hook: BBC 2026 Antonelli/F1 youngest-champion reporting; factual baseline is F1 and Guinness championship records.

## Contents
- `data/youngest_season_champions.csv` — selected season-long title examples with source URLs, calendar ages, sex/open category, formats and age basis.
- `data/f1_youngest_record_progression.csv` — confirmed historic youngest champion records plus unconfirmed 2026 age scenario.
- `scripts/render_charts.py` — project-scoped, deterministic 3-chart Matplotlib renderer, separate from core `src/`.

## Planned visual outputs
- `output/season_champions_01_f1_record.png`
- `output/season_champions_02_cross_sport.png`
- `output/season_champions_03_title_formats.png`

## Key decisions
- A senior, season-long ranking can qualify even if named No. 1 rather than championship; include ATP/WTA, golf Orders of Merit and FedExCup.
- Exclude majors/Olympics/one-off individual events.
- Colour system for this series: F1 red; other motor racing blue; other sports grey.
- Leader lines on F1 record timeline; sport in brackets on format groups.
- No global across-sport absolute youngest claim from a sample of 13.
- Conditional Antonelli 2026 marker never plotted as a confirmed record.

## QA gates
- Dataset row count and unique titles: checked in original preview; 13 entries.
- Date-of-birth / award-date consistency: checked in original preview where date present.
- Project-scoped repository renderer execution: **PASS** — exact committed Python script content verified against local test copy (Unicode codepoint checksum 0x61e61d79) and executed using 13 matching research records.
- GitHub Actions validation: **not run** — this project script is standalone and no matching PR CI run was returned.
- Output image pixel inspection: **PASS on local reproduction** — all three 1600×1600 PNGs were opened and inspected at full size for titles, label clearance, leaders, colour, sport labels, legends, and footers. Files are not yet pushed into repo.
- 1997 WTA ranking: Hingis 1997 No.1 confirmed by WTA; dated 24 November 1997 ranking corroborated by historical ranking archive (see https://tennis.quickfound.net/history/wta_top_20_1989-present.html).\n- Blog copy, social and hero feature image: **not yet prepared**.
- Published URL: **none**. Refresh F1 title status after 25 October 2026 United States GP before writing final copy.

## Publication process
Finish render + QA, show exact proposed final images for approval, then take the separately approved step to prepare publication assets and submit/merge the relevant PR.
