# Mel Gibson career pivot — QA report

## Result

**PASS — charts are ready for editorial review.**

No live-site publication has been performed.

## Data QA

- Official IMDb non-commercial exports were acquired on 25 September 2026.
- Resolved identity: Mel Gibson, IMDb `nm0000154`, birth year 1956.
- Six exact-name IMDb candidates were found on the first acquisition attempt; the script was tightened to validate name + expected nconst + birth year before continuing.
- 103 acting/directing career title IDs entered the join.
- 65 released movie titles were found.
- 63 released movies had IMDb ratings.
- 62 met the 1,000-vote analytical floor.
- Analytical dataset: 62 rows.
- Acting rows: 58.
- Directing rows: 6.
- Acting + directing rows: 2.
- Audit rows: 41.
- Title-basics join coverage: 100%.
- Vote-floor coverage of rated released movies: 98.41%.
- Duplicate analytical `tconst` values: 0.
- Missing analytical year/runtime/rating values: 0.

## Story QA

The provisional "where did he go?" framing was re-tested against the acquired data rather than assumed.

The strongest supported route is:

> **He didn't disappear. He changed jobs, then came back differently.**

Evidence used by the three-chart sequence:

- *Lethal Weapon* IMDb rating: 7.6.
- *Braveheart* IMDb rating: 8.3.
- 1990s eligible acting movies: 13; median rating 6.7.
- 2020–25 eligible acting movies: 16; median rating 5.6.
- Largest gap between years containing an eligible acting movie: 2003 → 2010.
- 2022 eligible acting movies: 6.
- Released feature directing credits: 6 from 1993–2025.
- *Braveheart*: 8.3; *Apocalypto*: 7.9; *Hacksaw Ridge*: 8.1; *Flight Risk*: 5.2.
- Later directing release-year gaps include 9, 10 and 9 years.

The story avoids claiming that title ratings measure Gibson's individual performance or that historical controversies caused changes in the plotted career data.

## Chart QA

### Chart 1 — The peak is where memory puts it

- Chart type: scatter.
- 58 eligible acting titles.
- Explicit axis labels: Film year / IMDb rating.
- Rating axis is intentionally non-zero because this is a scatter comparison, not a bar chart.
- Highlights limited to *Lethal Weapon* and *Braveheart*.
- No trend line or causal inference.
- Initial render failed the safe-title-margin check; title copy was shortened.
- Final title, subtitle, plot and footer do not overlap.
- Final output: 1600×1600.

### Chart 2 — He didn't stop acting. He got busier.

- Chart type: line over an ordered annual sequence.
- Every year from 1979–2025 is present; zero years are explicit.
- Y-axis starts at zero.
- 2004–09 gap is annotated.
- 2022 six-film peak is the only red highlight.
- No dual axis.
- Final title, subtitle, annotation, axes and footer remain inside safe margins.
- Final output: 1600×1600.

### Chart 3 — Directing became the second career

- Chart type: scatter.
- Six released directing features.
- Explicit axis labels: Film year / IMDb rating.
- All six titles are labelled because the sequence is small enough to remain readable.
- Academy annotations are restricted to the verified *Braveheart* Directing Oscar and *Hacksaw Ridge* Directing nomination.
- *Flight Risk* remains visible as a lower-rated counterexample.
- Initial render failed the safe-title-margin check; title copy was shortened.
- Final labels do not clip or collide with the title/subtitle/footer.
- Final output: 1600×1600.

## Renderer/workflow QA

- Official IMDb acquisition final run: GitHub Actions run `36196147108` — success.
- Initial archived render: run `36197124576` — success; visual QA then caught title clipping.
- Final archived render after copy fix: run `36197297368` — success.
- Final PNGs were committed back to the project branch by the reusable render workflow.

## Template-system decision

A reusable improvement **was** warranted for acquisition, so `.github/workflows/build-archived-imdb-career-data.yml` was added.

A renderer/template change was **not** warranted. The first-render issue was caused by project headline length; shortening the copy fixed it while preserving the locked template rules.
