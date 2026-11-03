# Bauhaus My Data → Art — live column and category mapping regression

**Purpose:** Fix the recurring failure reported after the Bauhaus Poster Composer v5 merge: changing **Select category** or **Numeric value column** appears to change the controls but leaves old marks, metric text and values on the canvas.

## Root causes confirmed on `main`

1. The `bh-value` (numeric measure) and `bh-label` selectors had **no change listeners**, so users had to click Create artwork again.
2. `bh-filter-value` had a listener, but `applyImported()` rejected **the entire selected category** when *any* observation was missing/non-numeric/negative. This is significant for the real Bowie data: **Space Oddity** has **10 tracks but one blank `spotify_streams` value**; switching to Spotify streams could not produce artwork.
3. The resulting status did not explain near the category control which observations were not plotted.

## Behaviour fixed

- Once a dataset has been created for the first time, changes to **Label column**, **Numeric value column**, **Optional category filter** and **Select category** re-apply the active source and redraw the poster immediately. No additional Create click or re-fetch.
- A different newly imported CSV still requires **one initial explicit Create**, so mapping its fields cannot silently replace the previous source's artwork.
- Validate **all matching rows** before applying the first-64-*valid*-record cap. Missing/non-numeric/negative measures are **excluded**, never treated as zero or given a fabricated value.
- Show source-relative counts next to the selector and in automatic source credits. For instance: `9 plotted of 10 matching rows · 1 missing/invalid spotify_streams value excluded (not zero)`. Distinguish exclusions from the existing 64-record display cap.
- If **no valid rows** exist or label and numeric fields are identical, leave the last valid artwork intact, restore its previous mapping selections, and show an explicit warning. This avoids showing mismatched controls with a stale chart.
- All-zero **valid** records remain valid and are plotted according to the existing zero-area rules.
- Keep custom editorial text overrides, sort, poster type, visual finishes, tap-to-inspect, source attribution, PNG saving and the existing local/GitHub import pipeline.

## Source-verified Bowie regression

CSV: `archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv`, on `main`.

| Category | Value column | Matching rows | Valid plotted | Excluded |
|---|---|---:|---:|---:|
| Space Oddity | spotify_streams | 10 | 9 | 1 blank |
| Space Oddity | duration_seconds | 10 | 10 | 0 |
| David Bowie | spotify_streams | 14 | 12 | 2 blank |
| All albums | spotify_streams | 275 | first 64 of 239 valid | 36 unavailable |

These figures are validated against source CSV fields `album_title`, `track_title`, `duration_seconds`, and `spotify_streams`. They are not illustrative data.

## Regression tests run (simulated DOM and Canvas)

- Imported real 275-row Bowie CSV; created an artwork once; then changed `album_title` category and numeric value back and forth several times **without clicking Create**.
- Verified mark count, selected metric and editorial headline/deck/source, adjoining status, and actual canvas redraw after each change.
- Tested changing the label field and rejecting an invalid text-valued numeric mapping, with controls restored to the previously valid values.
- Tested 64-record cap on all-album stream data, while clearly disclosing 36 omitted records.
- Switched to **Data Mosaic** and **Circle Study**, repeated the numeric measure and category change. Current composition was preserved.
- Verified existing PNG-export action still works after the changes.
- Loaded a *different* real `data/site_analytics_daily.csv` **without clicking Create** and verified the earlier Bowie artwork remained unchanged; clicking Create once then switched to the analytics source.
- Embedded JavaScript compiled.

**Outstanding:** real iPhone Safari interactions, actual pixel-level PNG inspection and live site verification after merge. Simulated Canvas tests are not a substitute for these.

## Merge and approval

This is a targeted correction to **Bauhaus Art Studio only**, with this QA document. No chart renderer, other Resource, CSV, blog post, CI workflow or global site code is changed. Merge only after explicit approval.
