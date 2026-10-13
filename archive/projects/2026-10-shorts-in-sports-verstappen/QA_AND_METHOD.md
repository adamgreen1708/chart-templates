# Shorts in Sports × coffeetableviz — Max Verstappen: review and reproducibility

*Editorial version: 13 October 2026. Source: The Data Taylor's GitHub workbook, `SIS- Max Verstappen.xlsx`. Prepared for peer review; not published.*

## Editorial argument

- Chart 1: Grand Prix winning shares changed dramatically between the 2021 breakthrough, 2023 peak and 2025.
- Chart 2: grid position is associated with classified finishing position, but unusually large gains occur.
- Chart 3: exhaustive set of all seven eligible 2015–2025 races with net position gain ≥13. São Paulo 2024 is the biggest comeback ending in a victory, although Russia 2021 has the biggest raw gain.

## Reconciliation with workbook

| Gate | Value | Criterion |
|---|---:|---|
| Source workbook | 250 rows | Seasons 2015 through 2026 Singapore |
| Completed-season analysis | 233 rows | Seasons 2015–2025 inclusive |
| Marked retirements | 33 rows | Original PositionText = `R` |
| Classified finish rows | 200 | PositionText is numeric, 2015–2025 |
| Irregular grid exclusions | 1 | São Paulo 2025 official pit-lane start despite numeric starting grid P19 |
| Valid grid-versus-finish analysis | 199 rows | Numeric classified finish and normal grid start |
| Large net gains | 7 | StartingGrid − FinalPosition ≥ 13 over 199 valid results |
| Large net gains ending P1 | 2 | São Paulo 2024 (+16); Belgium 2022 (+13) |

No Sprint race results included. All annual wins based on original `PositionText = '1'`; seasonal win rate = wins ÷ Grands Prix counted in the workbook × 100. **19 / 22 = 86.3636%** → **86.4%** rounded to one decimal. Formula 1's prose sometimes reports **86.3%**; the mathematically rounded figure is 86.4%.

An `R` row may still have a numerical final-position value. Thus do not use the final position column alone to classify a normal finish. Net position changes are not pass counts and do not measure driver talent independent of strategy, penalties, retirements, weather, car performance, and the opposing field.

## All seven qualifying recoveries

| Race | Grid | Finish | Net gain | Verification |
|---|---:|---:|---:|---|
| Russia 2021 | 20 | 2 | +18 | [Official F1 grid](https://www.formula1.com/en/results/2021/races/1077/russia/starting-grid), [result](https://www.formula1.com/en/results/2021/races/1077/russia/race-result) |
| São Paulo 2024 | 17 | 1 | +16 | [FIA race report](https://www.fia.com/news/f1-vestappen-takes-stunning-sao-paulo-win-p17-grid-alpine-score-double-podium) |
| United States 2018 | 18 | 2 | +16 | [Official F1 grid](https://www.formula1.com/en/results/2018/races/996/united-states/starting-grid), [F1 race results](https://www.formula1.com/en/racing/2018/united-states) |
| Russia 2018 | 19 | 5 | +14 | [Official F1 grid](https://www.formula1.com/en/results/2018/races/994/russia/starting-grid), [race analysis](https://www.grandprix.com/races/russian-gp-2018-race-notes.html) |
| Saudi Arabia 2023 | 15 | 2 | +13 | [Official F1 grid](https://www.formula1.com/en/results/2023/races/1142/saudi-arabia/starting-grid), [result](https://www.formula1.com/en/results/2023/races/1142/saudi-arabia/race-result) |
| Belgium 2022 | 14 | 1 | +13 | [FIA report](https://www.fia.com/news/f1-verstappen-takes-dominant-belgian-grand-prix-win-red-bull-claim-1-2-finish) |
| China 2017 | 16 | 3 | +13 | [FIA official starting grid](https://www.fia.com/sites/default/files/official_starting_grid_41.pdf), [classification](https://www.fia.com/events/fia-formula-one-world-championship/season-2017/race-classification-7) |

## Partial 2026 — text only

- The workbook includes 17 Grands Prix in 2026 through the 11 October Singapore Grand Prix. These are intentionally excluded from all 3 plotted datasets.
- At Australia 2026: P20→P6, net +14, verified with [F1 starting grid](https://www.formula1.com/en/results/2026/races/1279/australia/starting-grid) and [F1 result](https://www.formula1.com/en/results/2026/races/1279/australia/race-result).
- The two 2026 wins through Singapore: [Bahrain Grand Prix in Malaysia](https://www.formula1.com/en/results/2026/races/1308/bahrain/race-result), [Singapore](https://www.formula1.com/en/results/2026/races/1296/singapore/race-result), verified with the official F1 results.

## Graphic quality / accessibility

- All three charts 1600×1600 px, square and matching site light-grey `#F3F4F6`; the source and credit appear on every image.
- Chart 1 bar axis starts at zero; annual percentages divide win totals by rows for the corresponding completed season.
- Chart 2 starts grid P1→P20 from left to right, finish P1 at the top. Dot **area** scales with frequency of identical pairs. Its diagonal is x=y; a point above represents a net position gain. No spurious causal assertion.
- Chart 3 flips the horizontal position axis intentionally (P20 left → P1 right) for improvement to read left to right. Grey is start, blue/red is finish. Red is an editorial comparison, not exclusive win status.
- Data source is a community-curated spreadsheet. The public repository's README licenses reuse with credit but does not document an underlying data feed. Official confirmations above support specifically reported race results, not a full independently reconstructed dataset.
- The alt text supplied with each article image explains the marks, chart population and key takeaway.
- Some labels appear small on a narrow phone screen. Use the full-resolution image and allow tap-to-zoom in the site layout if possible. No claim is made that this independent Matplotlib prototype is the locked `src/render_538.py` output.

## Reproduction

The supplied files `season_win_rates.csv`, `grid_finish_derived.csv` and `selected_comebacks.csv` are the chart-ready datasets. Run `python revise_chart12.py` and `python render_chart3.py` with Python 3 and Matplotlib to recreate the three PNG/SVG drafts. Do not use the earlier `render_drafts.py` as the canonical source.

## Before publication

1. Review chart 3's new China 2017 row and source references.
2. Copy the precise approved PNGs and Jekyll post to `site/` paths given in the review package. Ensure the asset and data ZIP URLs resolve.
3. Decide whether the chart 3 visual serves as the story-specific card/social artwork, or whether a separate house-compliant illustration is required.
4. Review branch/PR against `main`, verify site build and mobile chart layout.
5. Merge only after explicit approval, verify GitHub Pages deployment and final article URL.
