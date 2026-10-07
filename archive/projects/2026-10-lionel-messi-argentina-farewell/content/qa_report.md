# QA report

Status: DATA + CONFIG PRECHECK PASS; GitHub Actions render pending.

## Data checks

- Annual rows: 22 calendar years, 2005–2026.
- Career totals reconcile to 208 appearances and 126 goals.
- 2005–20 totals independently recomputed: 142 appearances, 71 goals, 0.500 goals/app.
- 2021–26 totals independently recomputed: 66 appearances, 55 goals, 0.833 goals/app.
- Era shares: 31.7% of appearances and 43.7% of goals in 2021–26.
- Major-finals table: 9 finals; first four runner-up, next four champion, final 2026 runner-up.
- No youth or Olympic matches included in cap/goal totals.

## Config precheck

- Three configs use only locked renderer chart types: bar, scatter, dot.
- Bars start at zero.
- Chart 2 uses explicit categorical tick labels rather than pretending the nine finals are evenly spaced in calendar time.
- Chart 3 axis starts at zero and compares the same metric, scope and unit.
- Output paths are project-scoped.
- Source text is present on all charts.
- No renderer or reusable template changes are required at this stage.

## Render QA

Pending automatic archived-project render after this commit. Review required for title/subtitle clearance, axis/tick readability, annotations, footer visibility, clipping and safe margins.
