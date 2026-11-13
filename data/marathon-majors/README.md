# Marathon major winners, 2000–2026 — Bauhaus-ready splits

Two derived CSV files for **Coffeetableviz's Bauhaus Art Studio**, separated by the source's `Sex` value. These files are not a newly verified results database.

## Files

| File | Source `Sex` | Rows | Nonblank `Time` | Missing `Time` |
| --- | --- | ---: | ---: | ---: |
| [marathon_major_winners_men_2000_2026.csv](marathon_major_winners_men_2000_2026.csv) | `Men` | 154 | 150 | 4 |
| [marathon_major_winners_women_2000_2026.csv](marathon_major_winners_women_2000_2026.csv) | `Women` | 154 | 150 | 4 |
| **Total** | | **308** | **300** | **8** |

**Original source:** [Shorts in Sports — SIS-marathon_major_winners_2000_2026.csv](https://github.com/shortsinsports/Data/blob/4ea0ca9e403d706a734d41088ad63e571ab0ca21/SIS-marathon_major_winners_2000_2026.csv), pinned to commit `4ea0ca9e403d706a734d41088ad63e571ab0ca21` (repository `shortsinsports/Data`). Credit the original community dataset when publishing a chart.

## Transformation rules

- Keep **all 308 source observations** in their original order, split exactly by `Sex = Men` or `Sex = Women`. Nothing is quietly dropped, including `NO RACE` rows.
- Preserve the **nine original source columns** and their text exactly: `Race`, `Year`, `Sex`, `Winner`, `Nationality`, `Time`, `Notes`, `Birth_Country`, `Birth_Country_Source`.
- Append two derived fields:
  - `Race_Year` — a ready-to-label string such as `Tokyo (2007)`. Original `Race` and `Year` remain unchanged.
  - `Time_Seconds` — convert a nonblank `H:MM:SS` finishing time to elapsed whole seconds (`2:09:45` = `7785`); preserve a blank `Time_Seconds` when source `Time` is blank. No invented zeroes.
- All values were copied or mechanically derived from that source commit. Results, nationalities, notes and disputed or user-supplied entries have **not** been independently fact-checked.

## Using the files in Bauhaus Art Studio

Visit [Bauhaus Art Studio](https://coffeetableviz.com/resources/bauhaus-art-studio/) → **Data Art** → choose public GitHub account **adamgreen1708** → repository **chart-templates** → search **marathon_major_winners**. Choose either file and click **Load this dataset**.

Recommended mapping:
- **Label column:** `Race_Year` for race/year labels, or `Winner` for people's names.
- **Numeric value column:** `Time` (studio recognises elapsed `H:MM:SS` and displays it as time), or `Time_Seconds` for explicit numeric seconds.
- **Optional category filter:** `Race` to compare within Tokyo, Boston, London, Berlin, Chicago or New York City; alternatively `Year` to compare races in one year.

The studio displays at most the **first 64 valid rows** from the current selection. Filtering by `Race` or `Year` before creating artwork makes subsets easier to interpret. The eight original no-time observations remain in the files and should be excluded **only from time-measured plots**, not counted as zero.

## Source-quality caveat

The source includes explicit notes such as **user-supplied**, **verify**, cancelled races and later disqualifications. This stage does not reconcile or replace those claims. Any editorial story or public factual comparison should validate relevant winners, dates and times against primary race results first.

## Validation performed for this split

- Parsed the source with CSV-aware quoting rather than splitting on commas.
- Confirmed the source has 308 records and nine columns, with no malformed record widths.
- Confirmed **154 men + 154 women = 308**, no unexpected `Sex` values, and **150 nonblank + 4 blank** time fields in each group.
- Confirmed each output re-parses as a valid CSV and that its original nine columns match the matching source records, in order, without altering values.
- Checked `H:MM:SS` conversion and kept missing values blank.
