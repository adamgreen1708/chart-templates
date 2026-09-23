# Project manifest: David Bowie reinvention

## Status

- Status: Kickoff / source acquisition scaffold created; dataset not yet frozen
- Started: 23 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-david-bowie-reinvention`
- Working branch: `project/2026-09-david-bowie-reinvention`

## Story

- Rough idea: music artists who sustained recording careers across many decades and repeatedly changed musical direction, with David Bowie as the likely focus.
- Working definition for the longevity cohort: artists with qualifying studio albums in six or more named calendar decades. This is deliberately different from claiming 50+ elapsed years; Bowie's 1967 debut and 2016 Blackstar span six named decades but just under 50 elapsed years.
- Focus artist: David Bowie.
- Audience: coffeetableviz readers plus music/data audiences.
- Intended route: real-data three-chart story, then Jekyll/social publication package if the editorial route is approved.

## Sources

| Source | URL | Use | Notes |
|---|---|---|---|
| MusicBrainz API | https://musicbrainz.org/ws/2/ | Core reproducible source | Artist identity, album release groups, first release dates, community genre tags. API requires a meaningful User-Agent and no more than one request per second. |
| MusicBrainz API docs | https://musicbrainz.org/doc/MusicBrainz_API | Methodology | Confirms release-group browsing and `inc=genres`. |
| David Bowie official site | https://www.davidbowie.com/ | Focus-scope cross-check | Validate Bowie's canonical album chronology and any MusicBrainz edge cases before publication metrics are frozen. |
| Official Charts | https://www.officialcharts.com/artist/19138/david-bowie/ | Optional secondary context only | May be used later for UK chart context; not required for the core reinvention measure. |

## Seed comparison cohort

The initial context cohort is deliberately small and illustrative rather than a claim to be an exhaustive ranking of every long-career artist:

- David Bowie — focus
- Bob Dylan
- Elton John
- Cher
- Neil Young
- Paul McCartney
- Bruce Springsteen
- The Rolling Stones

All identities and album spans must be resolved from MusicBrainz by the acquisition script. No MBIDs or career-span values are guessed in this manifest.

## Measurement concept

The project should separate two ideas:

1. **Longevity** — observed through qualifying studio-album release years and the number of named calendar decades containing at least one album.
2. **Reinvention** — tested for Bowie through change in MusicBrainz release-group genre profiles from one qualifying album to the next.

The likely derived measure is an adjacent-album genre similarity/reset score. It must not be described as an objective measure of artistic quality or personal identity. Genre tags are community metadata and coverage must be audited before use.

## Current editorial hypothesis

The strongest likely route is Bowie-centric rather than a broad ranking of artists:

1. set the context with a transparent peer cohort of long recording careers;
2. show Bowie's album-by-album genre palette changing across the chronology;
3. quantify the largest adjacent-album genre resets and identify where the catalogue changes direction most sharply.

This remains a hypothesis until the dataset is acquired and inspected under `docs/story_discovery_and_3_chart_flow.md`.

## Files

| File | Purpose | Status |
|---|---|---|
| `data/artist_cohort_seed.csv` | Names/roles only for artist resolution | Created |
| `scripts/build_musicbrainz_dataset.py` | Reproducible MusicBrainz acquisition and validation scaffold | Created |
| `content/research_plan.md` | Scope, measurement rules, QA risks and provisional story route | Created |
| `data/artist_album_spans.csv` | Context cohort output | Not generated yet |
| `data/david_bowie_album_genres.csv` | Focus album/genre output | Not generated yet |
| `content/story_plan.md` | Data-grounded ranked story options and final three-chart route | Not created until dataset inspection |

## Approval / build gate

Do not create chart configs, renders or publication copy until:

- the MusicBrainz data has been acquired;
- Bowie album scope is cross-checked against the official Bowie chronology;
- genre coverage/missingness is inspected;
- the story-discovery step is completed;
- the recommended three-chart route is grounded in the observed dataset.
