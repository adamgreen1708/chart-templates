# Initial QA report — 21 November 2026

- [x] Season determined as latest completed Premier League season 2025–26, not in-progress 2026–27.
- [x] Frozen, traceable 380-match dataset from Football-Data.co.uk mirror.
- [x] Exactly 20 clubs; exactly 38 games for each club; no duplicate home-away fixtures.
- [x] W/D/L matches the goals and FTR in all records; points earned are calculated per team.
- [x] Final Arsenal 85, Manchester City 78, Manchester United 71, Tottenham 41, West Ham 39; matches official table.
- [x] Source definition and 38-equal-game framing explicitly documented.
- [x] Standalone JSON generated and checked from snapshot.
- [x] Main JS source passed JavaScript syntax parse check.
- [x] Site in an isolated feature branch with responsive CSS.
- [ ] Actual GitHub Pages Jekyll PR build not yet verified.
- [ ] Full real-browser touch/hover/keyboard tests not yet verified.
- [ ] 390px and 320px pixel screenshots not yet reviewed.
- [ ] Original Tableau visual exact layout not confirmed (public Tableau preview could not be inspected).
- [ ] Editorial approval and merge — deliberately not done.

**Rendering policy:** This interactive is a dedicated browser-based specialist using an immutable GitHub-derived JSON dataset, not a change to any locked matplotlib renderer. No additional simulated statistics or made-up fixtures.
