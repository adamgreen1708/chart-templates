# QA log — original Tableau concept revision (21 November 2026)

- [x] User-provided Tableau screenshot inspected. It shows monthly stacked W/D/L circles separated by home and away, selected club's position, home/away totals and all-club final-points positioning.
- [x] Prior points-trajectory chart rejected as conceptually different. Its JS/HTML/CSS replaced rather than supplemented.
- [x] Read pinned source: 380 real 2025–26 fixtures, 20 clubs, 19 home/19 away, 38 each; no invented matchweek mapping.
- [x] Data includes real calendar dates, opponents, venue, score, result and cumulative points.
- [x] Max fixture count per month and venue = 4, fitting new 4-dot stacks (at 320px CSS sizing).
- [x] Club home / away metrics recomputed from the selected team's real results, no hard-coded sample values.
- [x] Individual month dots encode W (red), D (light grey), L (dark grey), matching screenshot semantics.
- [x] Final-points badges positioned using their final points on shared 0–90 horizontal scale.
- [x] User-approved 40%-opacity / 2px backdrop-blur tooltip settings preserved on #303133 dark canvas.
- [x] JavaScript source parse check performed before PR update.
- [ ] Jekyll PR-build rerun on revised head SHA.
- [ ] Real browser desktop and mobile QA: position tooltip near edges, 320px and 390px, W/D/L stack space, SVG badge collision.
- [ ] Accessibility QA including VoiceOver; at mobile select an overlapping final-points badge.
- [ ] Actual team-crests asset provenance/licensing if adding them instead of present text badges.
- [ ] Editorial approval; do not merge/publish.
