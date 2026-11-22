# QA log — original Tableau concept revision (21 November 2026)

- [x] User-provided Tableau screenshot inspected. It shows monthly stacked W/D/L circles separated by home and away, selected club's position, home/away totals and all-club final-points positioning.
- [x] Prior points-trajectory chart rejected as conceptually different. Its JS/HTML/CSS replaced rather than supplemented.
- [x] Read pinned source: 380 real 2025–26 fixtures, 20 clubs, 19 home/19 away, 38 each; no invented matchweek mapping.
- [x] Data includes real calendar dates, opponents, venue, score, result and cumulative points.
- [x] Max fixture count per month and venue = 4, fitting new 4-dot stacks (at 320px CSS sizing).
- [x] Club home / away metrics recomputed from the selected team's real results, no hard-coded sample values.
- [x] Individual month dots encode W (red), D (light grey), L (dark grey), matching screenshot semantics.
- [x] Final-points badges positioned using their final points on shared 0–90 horizontal scale.
- [x] User-approved 45%-opacity / 2px backdrop-blur tooltip settings preserved on #303133 dark canvas.
- [x] JavaScript source parse check performed after PR update.
- [x] Mocked-DOM runtime smoke test: renders Arsenal's 10 month columns and all 38 real result dots, 2 summary rows, 20 final-points club badges; selected dot fades other 37 and pins tooltip, reselect clears, club selector switches to Tottenham (rank 17).
- [ ] Jekyll PR-build rerun on revised head SHA.
- [x] CSS layout arithmetic verified at 320px (10 columns, at least 25.9px each for 22px dots) and 390px (32px per column for 23px dots) with the site's documented narrow-screen shell margins.
- [ ] Actual browser screenshot and touch QA at 320px and 390px: inspect tooltip positioning, 10-column W/D/L single row, touch targets and points badge collisions.
- [ ] Accessibility QA including VoiceOver; at mobile select an overlapping final-points badge.
- [ ] Actual team-crests asset provenance/licensing if adding them instead of present text badges.
- [ ] Editorial approval; do not merge/publish.

## Colour and chronology revision (club-specific primary palette)
- [x] Verified representative home-kit colour families against the Premier League 2025–26 kits overview; curated hex choices explicitly treated as **display approximations**, not asserted licensed brand values.
- [x] 20/20 club names resolved in the dynamic primary palette.
- [x] Win dots and W key now inherit selected club's primary colour; selected club badge also uses primary.
- [x] Dot text chooses dark or white contrast automatically. Dark-fill dots use a subtle light outline.
- [x] Heading automatically lightens primary colour to minimum WCAG 4.5:1 contrast against #303133; checked 20/20 teams (minimum 4.5:1).
- [x] HOME dots are bottom-aligned, month-and-venue fixture order reversed in DOM so earliest is nearest the month at the bottom; AWAY dots are top-aligned, earliest nearest the label at the top. Verified source sequence across all clubs and months.
- [x] Tooltip maintains #303133 at 45% opacity / 2px blur, with explicit white text for match title, score, points and other detail to override general site text colours.
- [x] Original 10-column August–May single-row layout retained on phones.
- [x] JavaScript syntax and source-statistics validation passed after revision.
- [ ] Actual browser/physical-device contrast and tooltip placement QA remains prior to publication.

## Cumulative points mini-chart in glass tooltip (exploratory)
- [x] Reused the 20 verified cumulative-points sequences in the site JSON (38 games each); no extra source or simulated results.
- [x] Miniature chart plots 0–38 on x-axis for **each club's own nth match**, and 0–90 cumulative points on y-axis (not shared matchweek or calendar date).
- [x] Grey context paths for 19 other clubs, selected club's primary-colour path lightened only if needed for legibility.
- [x] Focus marker at selected match number with correct points; a club-badge hover shows the selected club at its pinned game, or after match 38.
- [x] Visible text specifies 20 clubs, club-specific game number and points.
- [x] Tooltip remains dark background at 45% opacity and 2px blur, with light and contrasting text.
- [x] New source JavaScript parses; all 20 data curves separately checked to match each club's documented final points.
- [ ] Check on a physical phone that the taller tooltip does not obscure too many monthly result circles, and adjust direction/placement as necessary.
- [ ] Real browser QA of SVG rendering / VoiceOver labels before merge.

## Browser QA and HTTPS preview — 22 November 2026

- [x] Production-isolated **HTML preview** committed under `preview/epl-2025-26/index.html` on feature branch, with no Jekyll-only syntax and only branch-local relative HTML/CSS/JS/data URLs. No changes to the `main` GitHub Pages deployment.
- [x] Public HTTPS review URL verified by GitHub Actions using GET, HTML MIME type check and expected page content:
  https://raw.githack.com/adamgreen1708/chart-templates/feature/epl-2526-interactive-unfolded/preview/epl-2025-26/index.html
- [x] Real Chromium / Playwright browser QA across 1440px desktop, 390px phone and 320px narrow phone; **72 checks passed**.
- [x] All 380 games load correctly, all 20 clubs selectable, all 38 result dots appear, ten month columns stay in exactly one row, home and away aggregate table contains two real-data rows, 20 final-points badges appear.
- [x] On click/tap: tooltip pins, all 20 cumulative lines draw, match marker draws, 37 unselected result dots fade, second click clears selection and restores context.
- [x] CSS independently checked at all three viewports for 45% `rgba(48,49,51,.45)` and 2px backdrop blur.
- [x] No page-wide horizontal scrolling or JavaScript runtime errors at test widths.
- [x] Newcastle and Manchester City dropdown transitions succeed without missing data.
- [x] Browser full-page screenshot artifacts captured and manually inspected for a 320px / 390px / desktop selected-match and Newcastle context. Source: GitHub Actions run https://github.com/adamgreen1708/chart-templates/actions/runs/44964613184
- [ ] UX decision: miniature cumulative chart creates a taller selected tooltip on mobile, obscuring several month dots while pinned; review on user's actual iPhone before editorial approval.
- [ ] Physical iPhone Safari and VoiceOver sign-off remain; Chromium mobile emulation is not a substitute for the physical device.
- [ ] Licensed club crests are not included yet; three-letter badges deliberately remain until artwork provenance is resolved.

**Review gate:** PR #230 must remain draft and unmerged until user has opened the preview in Safari, approved the mobile interaction, and approved the article. The raw.githack temporary proxy may display a one-time confirmation and is *not* intended as a permanent production host.

## Final home-lane baseline polish — 22 November 2026

- [x] Based on user's iPhone Safari screenshot of **West Ham August**, home-dot stack was flush with the month-name baseline. The entire home stack now has **8px bottom inset**, leaving visible clearance; away stack and month label are unchanged.
- [x] 10 August–May columns remain in a single row at desktop, 390px and 320px.
- [x] Real Chromium / Playwright QA **252 checks passed** on the latest CSS (up from 72). Includes geometry verification of exactly **8.0px clearance** for every nonempty home month in Arsenal and West Ham at 1440/390/320px; every home and away month retains centre-outwards chronological sequence.
- [x] Verified 380 matches, 38 results per club, 20 club badges, home/away totals, 45% opacity / 2px blur tooltip, all 20 mini-chart trajectories, click-to-clear, club switching, no JavaScript runtime errors or horizontal page overflow.
- [x] Screenshots captured and visually reviewed, particularly West Ham at 390px, where the lowest home circle now clears the line. QA run: https://github.com/adamgreen1708/chart-templates/actions/runs/44965174261
- [x] GitHub Pages build succeeded on test head.
- [ ] **Editorial sign-off and merge** not performed. User still to approve final publication. Keep PR #230 draft and unmerged pending approval.
