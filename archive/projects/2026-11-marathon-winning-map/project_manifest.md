# Marathon Majors: a world of winners, then four exceptions

**Project status: PUBLISHED / ARCHIVED (13 November 2026).** Source: `data/marathon-majors` at commit `999b9b57c2cf61a1222bb4f08a4bdd885898e09a`; upstream Shorts in Sports pinned in that README.

## Corrected editorial contract

A second round of official-results verification found that Noriko Higuchi (Japan) was the **official reassigned** Tokyo 2011 women's champion following disqualification of the original winner. The initial source-status exclusion incorrectly removed her. Do not claim just three exceptions across all completed 2010s races.

**Defensible like-for-like inclusion rule:** Join men/women by race and source year, keep completed in-person races with nonblank country, and use the source's current winner designation including official reassigned champions. Study full decades 2000–09 and 2010–19; exclude 2020 onward, cancelled/virtual races. **112 matched race-years: 53 and 59.** New York 2012 cancelled after Hurricane Sandy; Tokyo starts in 2007.

## Three-chart story

1. **Visual prequel** — 53 women's winners by race/year in 2000–09, with 31 red marks for countries outside Kenya/Ethiopia. Berlin first six women's winners 2000–05 were all Japanese (confirmed official history).
2. **Visual puzzle** — same dot-matrix layout for 2010–19: 59 completed races, **four red winners**. Russia (Tokyo2010, Biktimirova); Japan (Tokyo2011, Higuchi, reassigned); USA (NYC2017 Flanagan, Boston2018 Linden). One NYC2012 blank is cancelled, not missing data.
3. **Reveal** — 0–100% slope chart of wins from outside Kenya/Ethiopia. Women **31/53 = 58.5%** in 2000s, **4/59 = 6.8%** in 2010s: **−51.7 pp**. Men **12/53 = 22.6%** to **6/59 = 10.2%**: **−12.5 pp**. All measures generated from the original source, not typed into chart datasets.

The archive regenerates all chart CSVs with `scripts/build_chart_views.py` and renders with production GitHub `src/render_538.py`, `render_profile=social_square`, no white card, consistent house colour. **Red always highlights women's wins from outside Kenya/Ethiopia; grey means contextual wins from Kenya/Ethiopia, with men's trend muted grey.** Both matrices have explicit y limits 0–7 to prevent clipping at the plot edge.

## Sources checked for the highlighted claims

- Berlin official winners 2000–05: https://www.bmw-berlin-marathon.com/fileadmin/media/events/berlinmarathon/fotos/Presse/Mediaguide/Statistiken/BM25AlleSiegerInnenBERLIN-MARATHON.pdf
- Tokyo 2010: https://www.marathon.tokyo/en/about/past/2010/
- Tokyo 2011 official reassignment: https://www.marathon.tokyo/2012/past_data/files/120124_2011place_women.pdf
- New York 2017 winner: https://testcache.nyrr.org/media-center/press-release/20171107_nycm_2017racehighlights
- Boston 2018: https://www.baa.org/races/boston-marathon/history/
- NYC 2012 cancelled: https://prod.nyrr.org/tcsnycmarathon/marathon-history

The original source is **not a blanket independently verified official result archive**. The explicitly mentioned winners and streak were verified independently; all other source results still require a wider independent official-results audit before claiming blanket verification. This is six historical races, not all eight current World Marathon Majors (Sydney and Cape Town omitted).

## Publication and final closeout — 13 November 2026

**Article:** https://coffeetableviz.com/stories/can-you-find-the-four-outsiders/  
**Category:** Sport; **credit:** Shorts in Sports and Coffeetableviz  
**Archived data and render PR:** [#214](https://github.com/adamgreen1708/chart-templates/pull/214) — merged and chart archive retained  
**Website publication PR:** [#215](https://github.com/adamgreen1708/chart-templates/pull/215) — merged, commit `3f7c744dfbdfd94d16de792e25125593c5cab243`  
**Jekyll/Pages deployment:** [successful main-branch workflow #43522970207](https://github.com/adamgreen1708/chart-templates/actions/runs/43522970207)

The original full-resolution chart PNGs were copied as **unchanged Git blobs** into `site/assets/charts/marathon-winning-map/`. Exact image hashes:
- Chart 1 and hero/card: `01_berlin_six_and_the_world.png` — `a6860c7eea9ebd9f00bcf6b817673316d18bc622`
- Chart 2: `02_find_the_four.png` — `fe7547eb968cc3abf38b71ed63bc54fee7051ee0`
- Chart 3: `03_women_changed_most.png` — `cccfc16daf8d7780a38c7284f8fe5154435224e8`

**Feature asset decision:** chart 1 is the story-specific square hero/card image: Berlin's six consecutive Japanese winners appear as red exceptions in the 2000s race grid. No generic running illustration, modified chart or new image-model rendering was inserted. Hero alt text reflects those actual dots.

**Rendered-page QA:** The deployed GitHub Pages artifact was inspected directly. It contains `stories/can-you-find-the-four-outsiders/index.html` and all three referenced images; the built HTML includes the article title, its statistical figures and the 216-unverified-entry caveat. The three assets are byte-for-byte identical to approved archived PNGs. The built document declares the canonical URL above. GitHub Pages reported **successful deployment** for the exact merge commit. A direct external HTTP fetch of `coffeetableviz.com` was unavailable from the validation environment; consequently, individual public-browser reachability is **not separately asserted**.

**Publishing guardrails satisfied:** site post + three site assets only; archive source files, renderer and older live posts were not changed. The chart archive remains reproducible. The published method note explicitly warns that 216 source entries are marked `Not independently checked`; this work does **not** claim every official result was independently re-audited.

**Editorial closeout:** Three real-data charts, article, source evidence ledger, deterministic strict-DQ generator and a LinkedIn draft are retained together. The source snapshot is frozen. Any later source correction must be documented and reviewed in a new PR, with chart renders and blog claims regenerated together.

## Stringent reproducible DQ gate (13 November 2026)

The chart build executes a source checksum, original-9-column round-trip and the canonical Node dataset `--check`, checks full 2000–19 race-year completeness and cancellation, and requires an exact record-keyed eight-entry official-evidence ledger. It recomputes all red dots and fractions from rows and writes `data/qa_report.json`. See `review/source_event_qa.md` and `review/flagged_source_evidence.csv`. A successful render **does not** certify all source winners independently; keep the source-derived limitation visible. The current AbbottWMM has eight events (Sydney and Cape Town are not in this historical six-race collection). The source checksum is frozen: changes require a new editorial review and deliberate pin update.

**Rendering contract gate:** the same GitHub builder now parses the three actual `CHART_CONFIG` files and fails if they depart from the approved `social_square` profile, 8×8 / 200 DPI canvas, four semantic endpoint labels, zero-to-100% final axis, matching matrix geometry and highlight meanings, footer or Shorts in Sports credit. The second PNG is now named `02_find_the_four.png` to match its corrected four-exception title.

## Research follow-up: possible causes (13 November 2026)

The published story now includes a brief, source-linked discussion after chart three about plausible mechanisms behind the 2000s-to-2010s change: improved professional pathways for Kenyan women, a documented increase in depth among fast Ethiopian and Kenyan women, and difficulty replacing Japan's exceptional early-2000s elite generation. This editorial context is **not** derived from the six-marathon dataset and cannot establish causality. See `review/contextual_research_2026-11-13.md` for external source links, exact contextual figures and validity boundaries. The TLDR carries the causal caveat. No chart numbers, source rows, CSVs, configs, image assets or rendering rules were changed.
