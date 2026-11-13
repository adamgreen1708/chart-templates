# Bauhaus Art Studio — public GitHub CSV import and duration QA

**Scope:** `site/resources/bauhaus-art-studio/index.html` only. Review branch; no change to `main` until explicitly approved.

## What changed
- Accept `https://github.com/<owner>/<repo>/blob/main/<path>.csv` or a **full 40-character commit permalink** from **any public** GitHub repository, plus the equivalent `raw.githubusercontent.com` links.
- Retain the HTTPS + permitted-host validation, CSV filename/path checks, 2 MB download limit, 10,000-record import limit, timeout, and 64-plotted-row cap. No tokens, private repository support, or third-party proxy.
- Fetch from the owner/repository in the supplied URL instead of hard-coding `adamgreen1708/chart-templates`; show that owner/repository and filename (and shortened commit when pinned) in source attribution.
- Recognise unambiguous `H:MM:SS` / `MM:SS` durations as **elapsed seconds** for proportional artwork geometry, retaining the original CSV field for tap inspection. Display clock-style durations as clock times, not as raw seconds.
- Prefer the actual duration field in initial column selection when the nonblank entries are valid clock times, even if other rows are blank; continue to omit missing values, never interpreting them as zero.
- Keep the existing Bowie `duration_seconds` formatting as `M:SS` and ordinary numeric fields as numbers.

## Source-based checks
Input: `shortsinsports/Data`, `SIS-marathon_major_winners_2000_2026.csv`. The public CSV was fetched directly through GitHub at the time of this change.

- **308 data records**, **9 columns**, valid consistent row widths.
- **300** valid `H:MM:SS` time fields and **8** empty time fields.
- `2:09:45` correctly means **7,785 seconds**, and `2:31:01` means **9,061 seconds**.
- Default mapped label: `Race`; initial numeric value: `Time`. With no filter, the first **64 valid** time rows are displayed, and all 8 missing values are excluded from the available observations.

## Repeatable regression
Run `node scripts/test_bauhaus_public_csv.js` from the repository root. The test compiles the production inline JavaScript and tests:
- Foreign-repository URLs at `main`, pinned SHA and raw URLs;
- Existing Coffeetableviz URL regression;
- Rejection of HTTP, unsupported hosts, folders, unsupported refs and non-CSV paths;
- Realistic clock-value conversion, blanks, invalid values, initial field mapping and output formatting;
- Bowie `duration_seconds` and normal numeric formatting regressions.

## Still requiring browser QA before merge
In the deployed GitHub Pages preview (or locally served site), load the user's exact pinned and `main` links; confirm loading messages/source credit, change the category `Race` and numeric field `Time`, then create a poster. Confirm both the drawn values and tap-to-inspect show the original clock times, no clipped headings/credit at mobile sizes, and a working PNG download. Re-check the existing Bowie and Daily visits presets. A production iPhone Safari test and actual Canvas pixel-level inspection have **not** been performed by this change.
