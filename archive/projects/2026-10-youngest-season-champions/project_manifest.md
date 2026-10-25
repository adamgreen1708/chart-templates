# Project manifest — youngest season-long sporting champions

- Started: 2026-10-25
- Status: **Review / awaiting final render verification and approval**
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
- Repository-specific renderer execution: **pending**.
- GitHub Actions validation: **pending**.
- Output image pixel inspection: **pending for repository-produced outputs**.
- Blog copy, social and hero feature image: **not yet prepared**.
- Published URL: **none**.

## Publication process
Finish render + QA, show exact proposed final images for approval, then take the separately approved step to prepare publication assets and submit/merge the relevant PR.
