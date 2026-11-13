# Marathon major winners — Bauhaus-ready data collection

**Scope:** Six races (Tokyo, Boston, London, Berlin, Chicago and New York City), source years 2000–2026, with Tokyo appearing from 2007. The dataset does **not** include Sydney or claim to contain all seven current World Marathon Majors.

**Pinned source:** [Shorts in Sports / Data — marathon winners CSV](https://github.com/shortsinsports/Data/blob/4ea0ca9e403d706a734d41088ad63e571ab0ca21/SIS-marathon_major_winners_2000_2026.csv) at Git commit `4ea0ca9e403d706a734d41088ad63e571ab0ca21`. Exact source snapshot: [source CSV](source/SIS-marathon_major_winners_2000_2026.csv). Credit **Shorts in Sports** alongside Coffeetableviz when publishing.

**Important accuracy boundary:** These are source-derived entries, not an independently verified official-results database. Some source notes say `User-supplied`, `verify`, or mention disqualifications. The original nine source columns and every original row remain intact. Derived rankings are **rankings within this supplied file**, not official world records or career-wide totals.

## Data files

| CSV | Rows | Suitable Bauhaus use | Label | Value |
| --- | ---: | --- | --- | --- |
| [Men — enriched master](marathon_major_winners_men_2000_2026.csv) | 154 | Exploring / filtering | `Race_Year` | `Speed_kmh` |
| [Women — enriched master](marathon_major_winners_women_2000_2026.csv) | 154 | Exploring / filtering | `Race_Year` | `Speed_kmh` |
| [Men — Fastest 12](marathon_major_winners_men_fastest12.csv) | 12 | Stripe Study / Circle Study | `Race_Year` | `Speed_kmh` |
| [Women — Fastest 12](marathon_major_winners_women_fastest12.csv) | 12 | Stripe Study / Circle Study | `Race_Year` | `Speed_kmh` |
| [Men — best by race](marathon_major_winners_men_best_by_race.csv) | 6 | Broadside / Circles | `Race` | `Speed_kmh` |
| [Women — best by race](marathon_major_winners_women_best_by_race.csv) | 6 | Broadside / Circles | `Race` | `Speed_kmh` |
| [Men — repeat champions](marathon_major_repeat_winners_men.csv) | 33 | Broadside / Mosaic | `Winner` | `Wins` |
| [Women — repeat champions](marathon_major_repeat_winners_women.csv) | 35 | Broadside / Mosaic | `Winner` | `Wins` |
| [Men — wins by nationality](marathon_major_wins_by_nationality_men.csv) | 15 | Mosaic / Broadside | `Nationality` | `Wins` |
| [Women — wins by nationality](marathon_major_wins_by_nationality_women.csv) | 12 | Mosaic / Broadside | `Nationality` | `Wins` |

Men's and women's files are independent. Fastest 12 and best-by-race CSVs retain source `Notes` and `Result_Status` so questionable entries remain visible.

## Source, eligibility and missing data

- **308 original source rows:** 154 men and 154 women. Original columns are `Race`, `Year`, `Sex`, `Winner`, `Nationality`, `Time`, `Notes`, `Birth_Country` and `Birth_Country_Source`, preserved exactly and first in both master files.
- **8 cancelled/no-race rows:** retained in masters. Their numeric metrics remain blank.
- **2 virtual New York City 2020 entries:** retained in masters, labelled `Virtual`, excluded from the completed-race rankings and summary counts.
- **298 eligible completed in-person entries:** 149 men + 149 women. All eight small extracts derive from these records. A completed entry counts according to source classifications; it does not prove official event eligibility or identity.
- Blank values remain **blank**, not zero. No false zero times, no fabricated missing birth-country information.
- Some source notes explicitly concern disqualification and need manual editorial review. `Result_Status` classifies the note, **not an independent verification**.

## Enriched master columns

The nine original fields plus `Race_Year` and `Time_Seconds` are retained, with these additions:

| Field | Meaning |
| --- | --- |
| `Speed_kmh` | `42.195 × 3600 / Time_Seconds`, to two decimals; **larger means faster** |
| `Speed_mph` | `(42.195/1.609344) × 3600 / Time_Seconds`, to two decimals |
| `Pace_Mile` | Elapsed `M:SS` per mile, rounded to nearest second |
| `Pace_Km` | Elapsed `M:SS` per kilometre, rounded to nearest second |
| `Decade` | Year grouped as `2000s`, `2010s` or `2020s` |
| `Winner_Wins_In_File` | Matching winner-name count, eligible entries in **that sex's file** only |
| `Winner_Wins_At_Race` | Eligible entry count for matching winner and race |
| `Nationality_Region` | Deterministic geographical grouping from stated nationality; **not birth country** |
| `Event_Status` | `Completed`, `Cancelled` or `Virtual` inferred from explicit source notes and `NO RACE` |
| `Result_Status` | Source-note classification: unreviewed, flagged, claims checked or disqualification mentioned |
| `Race_Record_To_Date` | `Yes` on a new **fastest winning time in this source subset** (by race and sex, chronological), `No` otherwise; **not an official course record** |
| `Seconds_Faster_Than_Previous_Race_Record` | Seconds faster than the previous best *winning time in this file*: blank before a prior comparator exists; 0 if no improvement |
| `Global_Time_Rank` | Ascending elapsed time rank **within this sex's eligible entries**, tied times share a rank; not a world ranking |

All numeric calculations use full unrounded source seconds; speeds are rounded only for display. `Speed_kmh` is the recommended Bauhaus measure. Do not use `Pace_Mile` text or `Time_Seconds` as a larger-is-better score.

## How to use in Bauhaus

Open [Bauhaus Art Studio](https://coffeetableviz.com/resources/bauhaus-art-studio/) and choose **Data Art** → GitHub account `adamgreen1708` → repository `chart-templates` → search `marathon_major`. Load one of the files above.

For the master file set `Label = Race_Year`, `Numeric value = Speed_kmh`, and `Optional category filter = Race` (or `Year`). The renderer keeps **only the first 64 valid input rows before sorting the artwork**. For a reliable actual-fastest selection use the sorted **Fastest 12** file, rather than expecting a master-file descending sort to find the global fastest 12.

For repeat champions, use `Winner` and `Wins`. For nationality, use `Nationality` and `Wins`. Both summary files are pre-sorted in descending order so high counts appear first. The source country refers to the nationality field, not athlete birthplace. Nationality summary denominator is 149 completed winners per sex, not 154 source rows.

A low finishing time is **good**, but raw Bauhaus mark area increases with the plotted value. Using speed gives an accurate zero-based larger-is-faster encoding. Differences between elite speeds are visually subtle; do not transform them into arbitrary scores.

## Regeneration and QA

A self-contained, offline deterministic build script creates **all ten** output CSVs from the archived pinned source snapshot:

```bash
node scripts/build_marathon_bauhaus.js
node scripts/build_marathon_bauhaus.js --check
```

The `--check` mode verifies every committed output matches the generator. It also asserts: 308 source rows, nine exact source columns, 154 records per sex, eight missing times, two virtual entries, 298 eligible completed entries, correct CSV round-trip and exact preservation of all nine original fields in the master files.

Any source corrections should be documented and reviewed separately rather than silently changing the pinned source or derived summaries.
