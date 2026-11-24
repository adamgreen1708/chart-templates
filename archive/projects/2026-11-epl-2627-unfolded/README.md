# 2026–27 Season Unfolded · live resource and daily data workflow

Reference: merged PR #230, EPL 2025–26 (design, interactions, mobile QA). The completed 2025–26 interactive is embedded in its Sport blog post, with legacy URL redirect.

## Source and freshness

- Initial baseline: https://www.football-data.co.uk/mmz4281/2627/E0.csv; authenticated current-season update provider: https://www.football-data.org/ (v4 API, season=2026)
- Initial Football-Data-derived snapshot: https://github.com/learningEngineer24/premier-league-predictor/blob/main/data/raw/E0_2627.csv (Git blob a1d185c4329eeb7b1868c64dc66f9d9f3044544b)
- Original mirror baseline: **80 completed results through 2026-10-25**. The initial live snapshot contains **107 verified completed matches through 2026-11-21**, from football-data.org, tested against all 80 historical scores. Do not mistake the data's last result date for the execution date.
- Only completed, scored, validated fixtures are imported. Unplayed future fixtures cannot appear.
- Data: `data/matches_2627.csv`; generated JSON: `site/assets/data/epl-2627-unfolded.json`.
- Validate: `python archive/projects/2026-11-epl-2627-unfolded/scripts/build_data.py --check`. Authenticated refresh in Actions: `--refresh --provider football-data-org` with the repository secret `FOOTBALL_DATA_ORG_TOKEN`.

## QA and publication gating

- Unique home–away pairing; expected twenty named clubs; score/result coherence; date range; no future match results; no removed or retrospectively changed results; <=19 at each venue; recomputed 3/1/0 points, totals and trajectories.
- Provisional order uses points, goal difference, goals scored, and club name for remaining unresolved ties. It is **not an official live standings service**, and games played can differ.
- Preserve dark charcoal styling, one ten-month row, 8px home-dot gap, 43% selection fade, 45%/2px tooltip, club-colour wins and the twenty-club cumulative trajectories.
- Daily GitHub data checks run even with `EPL_AUTO_PUBLISH_ENABLED` OFF. That variable gates **automatic merging**, not fetching or opening review PRs. Do not enable automatic publication until a live end-to-end refresh has demonstrated data-only PR creation, independent PR QA and a successful authorised merge.
- A fine-grained `EPL_PR_TOKEN` (Contents: read/write; Pull requests: read/write, access to this repo) is required unless repository settings permit Actions to create pull requests. PAT-triggered PR events run browser CI; `GITHUB_TOKEN`-authored PRs normally do not.
- Initial publication requires user review and merge; weekly data-only PR merges may be automatic *only after proven and explicitly enabled*. Other changes never auto-merge.

### Page links

- Published: `/resources/epl-2026-27-unfolded/`.
- Former season's completed story: `/stories/premier-league-season-unfolded-2025-26/`.

## Authenticated football-data.org adapter (added while draft PR is under review)

- New preferred refresh endpoint: `GET https://api.football-data.org/v4/competitions/PL/matches?season=2026`, authenticated from GitHub Actions using repository secret `FOOTBALL_DATA_ORG_TOKEN`. The API token is never embedded in public JS or site content.
- The adapter accepts only `FINISHED` results with explicit non-negative full-time scores, verifies league, season, date, team aliases and winner, then reuses the original strict history checks.
- Independent PR QA checks the committed CSV/JSON and tests the authenticated feed **read-only**. A passing probe establishes connectivity and agreement with the baseline, not that the chart's committed data is fresh.
- The earlier 80-match Football-Data.co.uk-derived baseline has been replaced in the published dataset by 107 authenticated football-data.org results. `--check` preserves that attribution.
- Refresh the candidate from the new provider with `python archive/projects/2026-11-epl-2627-unfolded/scripts/build_data.py --refresh --provider football-data-org`. This relabels source provenance only when it actually writes the new provider data.
- Automatic EPL data-only merging is enabled in the daily workflow only after the first reviewed PR #237; its scheduled runs must pass both the direct browser tests and independent PR checks before merging. The source API secret alone cannot publish anything.

## Provider freshness / editor candidate (22 Nov 2026)

- Authenticated Actions probe: 107 completed EPL matches through 2026-11-21, unchanged against the initial 80 result scores. The API sometimes returned a stale 100-game response from its cache, so the adapter now retries and **fails closed** below the explicitly verified floor (107 / 2026-11-21).
- Browser QA validates the newest candidate, then updates **only the draft feature branch's CSV/JSON** using GitHub Actions; no direct main commit, no merged PR and no automated site publication. This draft-branch synchronisation ceases when the PR is merged or closed.
- The page footer reads source provenance from JSON metadata and the header displays the latest included result date, not the execution date.

## Daily refresh and publication safeguards

- Schedule: every day at 08:30 Europe/London, represented by separate UTC cron entries for BST and GMT. The DST-safe gate runs only the entry matching the current UK offset; GitHub may delay scheduled runs. Daily checks cover Monday-night and midweek matches on the following morning.
- Daily source checks run **even while automated merging is disabled**. No change means no PR, no deployment. A verified new result updates the existing data-only review PR rather than creating another one.
- New completed matches generate a **data-only review PR** using repository secret `EPL_PR_TOKEN`, a fine-grained token with Contents and Pull requests write limited to this repository. `FOOTBALL_DATA_ORG_TOKEN` is a different secret and only authenticates the results API.
- The `EPL_PR_TOKEN` secret is required to create PRs that trigger truly independent GitHub Actions QA. Without it, the workflow fails, preserves the live dataset and opens/updates an issue.
- New data must preserve past scores, dates and fixtures; finished results only, twenty fixed clubs, logical goal scores, no duplicates or future dates. Reject provider cache regressions.
- A gap of over 21 days since the last completed result during an unfinished active season produces a review failure and issue. Such alerts can also reflect unusual schedule gaps, which need human checking.
- PR QA validates the **committed** data without rewriting its CSV/JSON, tests 1440px/390px/320px browser behaviour, and builds the site.
- The daily EPL workflow is opted into automatic publication **for its verified 2026–27 data-only PRs only**. PR #237 is specifically excluded from automated merging, as the user is approving the first release manually. Later scheduled runs create/refresh data-only PRs and merge only after independent checks pass. The emergency-stop variable is `EPL_AUTO_PUBLISH_PAUSED=true` in GitHub Actions repository variables; when unset, automatic EPL merges are enabled. All other Coffeetableviz workflows remain unchanged.
- To test manually after a new match is available, open GitHub Actions > 'Daily EPL 2026-27 verified results refresh' > Run workflow > `main` > `review`; this **never auto-merges**. `publish` mode is explicit and uses the same strict safeguards as the scheduled run. Run the manual `review` mode to investigate unusual updates.
- The merge step confirms the PR targets `main`, uses the exact automated EPL branch and title, and changes **only** the 2026–27 CSV and JSON paths. It waits for successful independent PR checks and uses `--match-head-commit` to prevent merging a different/unverified head. A failed verification raises an actionable GitHub issue, leaving the last published site unchanged.
- Automatic publication may be stopped immediately without editing a workflow by adding/updating GitHub Actions repository **variable** `EPL_AUTO_PUBLISH_PAUSED=true`; remove it or set it to `false` to resume. The variable is used by this EPL workflow only.
