# 2026–27 Season Unfolded · review project

Reference: merged PR #230, EPL 2025–26 (design, interactions, mobile QA). All 2025–26 files remain untouched.

## Source and freshness

- Intended canonical feed: https://www.football-data.co.uk/mmz4281/2627/E0.csv
- Initial Football-Data-derived snapshot: https://github.com/learningEngineer24/premier-league-predictor/blob/main/data/raw/E0_2627.csv (Git blob a1d185c4329eeb7b1868c64dc66f9d9f3044544b)
- Review snapshot: **80 completed results through 2026-10-25**. The mirror may lag the latest real-world fixtures; do not describe this baseline as today's table.
- Only completed, scored, validated fixtures are imported. Unplayed future fixtures cannot appear.
- Data: `data/matches_2627.csv`; generated JSON: `site/assets/data/epl-2627-unfolded.json`.
- Regenerate: `python archive/projects/2026-11-epl-2627-unfolded/scripts/build_data.py --check`. Fetch directly from upstream: use `--refresh`.

## QA and publication gating

- Unique home–away pairing; expected twenty named clubs; score/result coherence; date range; no future match results; no removed or retrospectively changed results; <=19 at each venue; recomputed 3/1/0 points, totals and trajectories.
- Provisional order uses points, goal difference, goals scored, and club name for remaining unresolved ties. It is **not an official live standings service**, and games played can differ.
- Preserve dark charcoal styling, one ten-month row, 8px home-dot gap, 43% selection fade, 45%/2px tooltip, club-colour wins and the twenty-club cumulative trajectories.
- Scheduled GitHub workflow is gated by `EPL_AUTO_PUBLISH_ENABLED`. Do not switch this on until **a live workflow_dispatch has shown direct feed download, data-only PR creation, full browser QA, successful PR CI checks and PR merge**.
- A fine-grained `EPL_PR_TOKEN` (Contents: read/write; Pull requests: read/write, access to this repo) is required unless repository settings permit Actions to create pull requests. PAT-triggered PR events run browser CI; `GITHUB_TOKEN`-authored PRs normally do not.
- Initial publication requires user review and merge; weekly data-only PR merges may be automatic *only after proven and explicitly enabled*. Other changes never auto-merge.

### Page links

- After approval and deployment: `/resources/epl-2026-27-unfolded/`.
- Unmerged preview: `https://raw.githack.com/adamgreen1708/chart-templates/feature/epl-2627-season-unfolded/preview/epl-2026-27/index.html` (branch proxy, not GitHub Pages).

## Authenticated football-data.org adapter (added while draft PR is under review)

- New preferred refresh endpoint: `GET https://api.football-data.org/v4/competitions/PL/matches?season=2026`, authenticated from GitHub Actions using repository secret `FOOTBALL_DATA_ORG_TOKEN`. The API token is never embedded in public JS or site content.
- The adapter accepts only `FINISHED` results with explicit non-negative full-time scores, verifies league, season, date, team aliases and winner, then reuses the original strict history checks.
- On PR #231, independent QA tests the real authenticated feed **read-only**. A passing probe establishes connectivity and agreement with the baseline, not that the chart's committed data is fresh.
- The original 80-match Football-Data.co.uk-derived review snapshot remains clearly attributed to its original source until a newer provider candidate is validated and committed. `--check` preserves that attribution.
- Refresh the candidate from the new provider with `python archive/projects/2026-11-epl-2627-unfolded/scripts/build_data.py --refresh --provider football-data-org`. This relabels source provenance only when it actually writes the new provider data.
- Auto-publication remains OFF; the PR stays draft until visual/data review and explicit approval. Automated Monday runs are not enabled by adding this API secret alone.
