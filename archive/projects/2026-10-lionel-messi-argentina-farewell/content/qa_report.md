# QA report

Status: **PASS — revised three-chart set ready for Adam visual review**

## Data checks

- Annual rows: 22 calendar years, 2005–2026.
- Career totals reconcile to 208 appearances and 126 goals.
- 2005–20 totals independently recomputed: 142 appearances, 71 goals, 0.500 goals/app.
- 2021–26 totals independently recomputed: 66 appearances, 55 goals, 0.833 goals/app.
- Era shares: 31.7% of appearances and 43.7% of goals in 2021–26.
- Major-finals table: 9 finals; first four runner-up, next four champion, final 2026 runner-up.
- No youth or Olympic matches included in cap/goal totals.

## Final chart sequence

1. **208 caps. Plenty left for the final act.**
   - Annual Argentina appearances.
   - Makes the 2021–26 period explicit: 66 of 208 caps.
   - Marks 2021 as the career-high appearance year (16) and 2026 as the farewell year (12).

2. **Four finals lost. Then four won.**
   - Nine senior finals in sequence.
   - Adds chapter labels: 2007–16 = 4 finals / 0 titles; 2021–24 = 4 finals / 4 titles.
   - Keeps the 2026 World Cup runner-up visible as the final coda.

3. **The scoring lift wasn’t a blip**
   - Replaces the earlier two-dot era comparison with an annual goals-per-appearance line, 2005–2026.
   - Shows the 2012 prior peak for context and highlights 2022 and 2026 late-career output.
   - Includes 2005–20 (0.50) and 2021–26 (0.83) reference averages plus the 2021 first-senior-title marker.

## Config checks

- Chart types: bar, scatter, line — all supported by the locked renderer.
- Chart 1 bars start at zero.
- Chart 2 uses ordered-final positions with explicit categorical labels; it does not imply calendar spacing.
- Chart 3 y-axis starts at zero and compares the same senior-international scoring-rate metric across all years.
- Output paths are project-scoped.
- Source text is present on all charts.
- No renderer or reusable template files changed.

## Render QA

- Initial archived-project render: run 37678465723 — success.
- Chart 2 numeric row-match correction render: run 37678949173 — success.
- Revised three-chart render: run 37681849180 — success.
- Chart 1 final: PASS — title/subtitle clear; 2021 divider and career-high annotation readable; 2026 highlight visible; no clipping.
- Chart 2 final: PASS — chapter labels use the central negative space cleanly; champion/runner-up distinction clear; 2026 coda readable; no collisions.
- Chart 3 final: PASS — full annual journey visible; 2012/2022/2026 annotations readable; both average lines and 2021 marker clear; no clipping.
- All final PNGs reviewed at 1600 × 1600; titles, subtitles, axes, annotations, source/footer and safe margins pass.

## Editorial QA

- The sequence now reads clearly as **longevity → trophy reversal → late-career scoring performance**.
- Chart 1 owns appearance volume; Chart 3 owns scoring-rate detail.
- The story does not infer that trophies caused the scoring-rate increase.
- The 2026 World Cup runner-up remains visible rather than presenting the late career as an uninterrupted victory sequence.
