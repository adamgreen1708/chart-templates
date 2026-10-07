# QA report

Status: **PASS — ready for Adam visual review**

## Data checks

- Annual rows: 22 calendar years, 2005–2026.
- Career totals reconcile to 208 appearances and 126 goals.
- 2005–20 totals independently recomputed: 142 appearances, 71 goals, 0.500 goals/app.
- 2021–26 totals independently recomputed: 66 appearances, 55 goals, 0.833 goals/app.
- Era shares: 31.7% of appearances and 43.7% of goals in 2021–26.
- Major-finals table: 9 finals; first four runner-up, next four champion, final 2026 runner-up.
- No youth or Olympic matches included in cap/goal totals.

## Config checks

- Three configs use only locked renderer chart types: bar, scatter, dot.
- Chart 1 bars start at zero.
- Chart 2 uses explicit categorical tick labels rather than pretending the nine finals are evenly spaced in calendar time.
- Chart 3 axis starts at zero and compares the same metric, scope and unit.
- Output paths are project-scoped.
- Source text is present on all charts.
- No renderer or reusable template changes were required.

## Render QA

- Initial archived-project render: run 37678465723 — success.
- Visual QA found Chart 2's champion highlights and row-matched annotations were not resolving after CSV numeric coercion.
- Config-only correction used float-compatible row matches and slightly larger final markers.
- Final archived-project render: run 37678949173 — success.
- Chart 1: PASS — title/subtitle clear, final-year highlight visible, source/footer inside safe margins.
- Chart 2: PASS — four champions highlighted, runner-ups remain context grey, 2016/2021 annotations visible, tick labels readable.
- Chart 3: PASS — late-career comparison highlighted, labels clear, zero baseline retained.
- Final 1600 × 1600 PNGs show no clipping, title/subtitle collisions, footer collisions or unsafe edge labels.

## Editorial QA

- The three charts follow the intended sequence: longevity → finals reversal → scoring acceleration.
- The story does not infer that trophies caused the scoring-rate increase.
- 2026 World Cup runner-up remains visible rather than presenting the late career as an uninterrupted victory sequence.
