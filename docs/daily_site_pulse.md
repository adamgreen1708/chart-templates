# Coffeetableviz Daily Pulse

Daily, internal traffic summary built from GoatCounter and rendered in the Coffeetableviz square 538 house style.

## What it reports

- previous complete Europe/London day;
- total visits;
- 14-day visits trend;
- previous seven-day daily average once seven complete prior days exist;
- top three pages on the visual, with the full ranked page list retained in the latest JSON/history;
- top referrer on the visual, with the ranked referrer list retained in the latest JSON/history;
- one deterministic observation based only on the measured data.

The GoatCounter tracker went live on 3 October 2026, so **4 October 2026 is the first complete reporting day**. The workflow deliberately skips earlier dates.

## Files

- `scripts/site_analytics_daily.py` — fetches GoatCounter data, appends history and renders the pulse.
- `data/site_analytics_daily.csv` — growing daily history, created by the first successful run.
- `output/daily_site_pulse.png` — latest square visual.
- `output/daily_site_pulse_summary.md` — latest text summary.
- `output/daily_site_pulse_latest.json` — latest machine-readable summary.
- `.github/workflows/daily-site-pulse.yml` — daily schedule and manual rerun.

## Required GitHub secret

Create a GoatCounter API key in GoatCounter, then add it to this repository as the Actions secret:

`GOATCOUNTER_API_TOKEN`

Do not commit the token to the repository.

GoatCounter API requests use bearer-token authentication and the hosted endpoint:

`https://coffeetableviz.goatcounter.com/api/v0`

## Schedule

The GitHub Action runs every day at **08:15 UTC**. The script itself resolves the report date in **Europe/London** and always reports the previous complete local calendar day.

The first useful scheduled output is therefore expected on **5 October 2026**, reporting **4 October 2026**.

## Manual test

Use **Actions → Daily Coffeetableviz Pulse → Run workflow**.

An optional `report_date` input accepts `YYYY-MM-DD` for an idempotent rerun of a specific date.

## Rendering rules

The visual follows `spec/538_template_rules.md`:

- 8 × 8 square PNG;
- `#F3F4F6` background;
- primary `#1F8FA8`;
- highlight `#C44E52`;
- restrained grid and labels;
- at most one x-axis label per calendar date;
- message-led title;
- source footer;
- safe margins.

No mock traffic data is used in production.
