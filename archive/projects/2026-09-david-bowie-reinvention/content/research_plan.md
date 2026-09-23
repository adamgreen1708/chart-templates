# David Bowie reinvention — research plan

## Core question

Can we show, with transparent real data, that David Bowie's long recording career was not simply durable but repeatedly changed musical direction?

## Scope definition

The phrase “over five decades” is ambiguous. For this project, the context cohort means **qualifying studio albums appearing in six or more named calendar decades**.

For Bowie, the focus chronology begins with the 1967 debut and ends with *Blackstar* in 2016. That crosses the 1960s, 1970s, 1980s, 1990s, 2000s and 2010s without claiming more than 50 elapsed years.

## Primary data route

Use MusicBrainz because it gives us:

- stable artist identifiers;
- release-group entities that represent the album concept rather than individual reissues;
- first-release dates;
- primary/secondary release-group types;
- genre metadata through `inc=genres`;
- a public non-commercial API.

The acquisition script must respect MusicBrainz's one-request-per-second guidance and use a meaningful User-Agent.

## Focus-scope validation

MusicBrainz type metadata is useful but not sufficient on its own to define “David Bowie studio album”.

Before any reset metric is frozen:

1. retain only exact Bowie artist-credit album release groups in the raw focus export;
2. inspect secondary types and collaborations;
3. cross-check the chronology against the official David Bowie site;
4. document any manual inclusion/exclusion in the final story plan;
5. do not silently repair questionable dates or classifications.

This is especially important for catalogue edge cases, posthumous issues and releases whose MusicBrainz primary type alone could make them look like ordinary studio albums.

## Reinvention measure

The initial candidate is an adjacent-album genre reset score based on MusicBrainz release-group genres.

Possible implementation after inspection:

- represent each album as its observed genre set;
- calculate Jaccard similarity between each adjacent pair: intersection / union;
- define reset score as `1 - similarity`;
- only calculate a pair when both albums meet a minimum genre-coverage threshold;
- run a sensitivity check using all genres versus a fixed top-N by MusicBrainz genre count.

The score measures **metadata change between adjacent albums**. It does not measure creativity, quality, influence or intent.

## Known QA risks

- MusicBrainz genres are community tags, not a controlled expert classification.
- Genre coverage may vary substantially by album and era.
- Broad tags such as “rock” can make two otherwise different albums look artificially similar.
- A top-N rule can introduce a different form of arbitrariness.
- The context cohort is illustrative unless we build an exhaustive population search.
- Bands and solo artists have different membership/identity dynamics, so the peer chart must be labelled as context, not a league table of “most reinvented”.
- Tin Machine should not be silently folded into Bowie's solo album chronology; if used, it needs an explicit separate rule.
- UK chart peaks are optional context only because chart systems and catalogue/reissue behaviour change across eras.

## Provisional story routes to test after acquisition

### Route A — The chameleon, measured

Core argument: Bowie's six-decade album chronology contains repeated, measurable breaks in genre metadata rather than one long gradual drift.

Likely sequence:
1. long-career peer context;
2. Bowie album genre timeline;
3. adjacent-album reset score with the sharpest changes annotated.

Strength: closest to Adam's original idea and gives “reinvention” a transparent definition.

Risk: depends on sufficiently complete and stable MusicBrainz genre coverage.

### Route B — Reinvention came in waves

Core argument: the strongest resets cluster into distinct career phases rather than occurring evenly.

Likely sequence:
1. full Bowie chronology;
2. genre reset score;
3. decade/era summary showing clusters of high-reset albums.

Strength: more Bowie-focused and potentially a stronger editorial narrative.

Risk: era boundaries must emerge from data or be externally sourced, not invented to fit the chart.

### Route C — Longevity is common; repeated change is the story

Core argument: several peers span many calendar decades, but Bowie's catalogue is interesting because the internal genre profile keeps changing.

Likely sequence:
1. peer longevity comparison;
2. Bowie genre breadth/change;
3. biggest resets.

Strength: makes the comparison cohort useful without pretending it measures artistic reinvention across all artists.

Risk: the peer cohort must stay clearly illustrative.

## Current recommendation

Start with Route A, but do not create chart configs yet.

The next repo step is to run `scripts/build_musicbrainz_dataset.py`, inspect the generated cohort and Bowie genre coverage, then write `content/story_plan.md` using the locked story-discovery flow.
