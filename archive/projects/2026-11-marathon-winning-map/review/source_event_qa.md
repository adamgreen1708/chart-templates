# Source-event evidence and strict QA for the marathon mystery

**Status:** Source-derived chart build with 8 explicitly flagged records checked against independent official results. **Not a complete independent audit of every race result.** This distinction is essential when publishing for #ShortsInSports peers.

## Frozen source integrity

- Original: `data/marathon-majors/source/SIS-marathon_major_winners_2000_2026.csv`, pinned GitHub blob `de9682df90e34943a97d3b963fb3df07bc743c2e`.
- Enriched men/women master blobs: `4707c23f1e3557b2d89897d02225658da50765e9` / `11c4bd6039fc4280bf7adee719fee5faaf74addb`.
- Git commit containing source: `999b9b57c2cf61a1222bb4f08a4bdd885898e09a`.
- `scripts/build_chart_views.py` fails immediately if any blob checksum differs, any one of the original nine columns differs, or the repository's `node scripts/build_marathon_bauhaus.js --check` fails.
- A historical event is included only if both men's and women's rows are `Completed`, with a declared nationality and valid time. New York 2012 was cancelled. Tokyo joined the six-race historical sample in 2007. Results for 2020 onward do not appear in these three charts.
- 53 comparable race-years in 2000–09 and 59 in 2010–19. Every 2000–19 race-year for these six races is accounted for; 112 eligible pairs, 224 sex-specific victories.

## Status-flag review

Every source record in these 20 years labelled **Source flagged for review** or **Disqualification mentioned** has a corresponding verified official-results reference in `review/flagged_source_evidence.csv`, with *exact* Race/Year/Sex/Winner/Nationality/Result_Status matching the unchanged master rows. There are eight such records, and the builder stops if the source or the adjudication ledger changes without coordinated review.

The source data lists Rita Jeptoo as Chicago's recognised winner in **2013**, which is supported by Chicago's published list; the note about a later doping disqualification refers to **2014**, not invalidation of this 2013 victory. The Tokyo 2011, Boston 2014 and London 2010 women are the **recognised replacement winners** after disqualifications and must remain eligible. The two flagged London men (2008 Martin Lel, 2016 Eliud Kipchoge), London women 2009 (Irina Mikitenko) and 2012 (Mary Keitany) match the official London champions' list.

## Editorial verification beyond the flagged eight

- Berlin organiser records show **Japanese women won Berlin 2000, 2001, 2002, 2003, 2004, and 2005**: https://www.bmw-berlin-marathon.com/fileadmin/media/events/berlinmarathon/fotos/Presse/Mediaguide/Statistiken/BM25AlleSiegerInnenBERLIN-MARATHON.pdf
- Tokyo 2010 Alevtina Biktimirova (Russia): https://www.marathon.tokyo/en/about/past/2010/
- Tokyo 2011 Noriko Higuchi (Japan), officially reassigned: https://www.marathon.tokyo/en/about/past/2011/
- NYC 2017 Shalane Flanagan (US): https://prod.nyrr.org/about/history
- Boston 2018 Desiree Linden (US): https://www.baa.org/races/boston-marathon/results/champions/
- New York City 2012 cancellation: https://worldathletics.org/news/news/new-york-marathon-cancelled

All ten original-source nationality winners for the 2000s in these *six races*, and the four 2010s exceptions, are source-defined, not manually invented. **Source results marked 'Not independently checked' should be described as source-supplied, not officially certified.** The builder records 216 such completed sex-specific entries in its generated `data/qa_report.json`.

## Build and visual contract

1. `node scripts/build_marathon_bauhaus.js --check` against 308 preserved source entries.
2. `python archive/projects/2026-11-marathon-winning-map/scripts/build_chart_views.py` reconstructs the chart views and emits data QA report, fails on broken joins, fields, statuses, source flags, Berlin streak, four exceptions or summary fractions.
3. GitHub `render-archived-project.yml` executes the above Python script and three complete `social_square` configs via `src/render_538.py`. Do not substitute local/hand-made plots.
4. Inspect final GitHub-produced **actual PNG pixels** at 1600px, 390px and 320px; review title/subtitle/plot padding, labels, dots, the zero-to-100-percent axis and consistent red meaning.
5. No `site/_posts`, `publish_asset_map.csv`, direct main push or publish without editorial approval.

## Claims that would be incorrect or overreaching

- Do **not** describe these six historical races as all eight current Abbott World Marathon Majors (Sydney and Cape Town have since joined): https://www.worldmarathonmajors.com/about
- Do **not** say all winners were independently checked. The most sensitive flagged cases and highlighted exceptions were reviewed, but most of the file is originally labelled unreviewed.
- Do **not** say these results prove that running participation, nationality of all finishers, world-record performance or the sport overall became less international. The sample describes **only the winning nationalities** in these six races.
- Do not present small time discrepancies from the source as official times or world records; the charts use only race/year, winner and country.
