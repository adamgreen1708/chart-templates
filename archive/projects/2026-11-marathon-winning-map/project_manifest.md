# Marathon Majors: where did the outsiders go?

**Draft editorial revision 2. No live publication.**

Pinned input: `data/marathon-majors/`, commit `999b9b57c2cf61a1222bb4f08a4bdd885898e09a` (Shorts in Sports source, not fully independently checked).

## Narrative visual contract

1. **Visual prequel:** use a decade-wide race × year dot matrix of 51 women's winners in 2000–09; 29 red dots were outside Kenya/Ethiopia. The Berlin row has six red dots from 2000–05, and the builder checks all six are Japanese winners. There are ten nationalities in that decade.
2. **Matched-layout comparison:** plot 53 source-backed 2010s winning results in race/year positions; red exception dots are Biktimirova (Tokyo 2010), Flanagan (NYC 2017) and Linden (Boston 2018). Seven blank year/race cells indicate excluded source rows, **not cancelled races**. Red outside; grey Kenya/Ethiopia.
3. **Reveal who changed most:** 0–100% slope of share of wins from outside Kenya/Ethiopia. Women 29/51 (56.9%) → 3/53 (5.7%), −51.2 pp. Men 12/51 (23.5%) → 5/53 (9.4%), −14.1 pp. Same definition, matched race-years; percentage-point difference.

The opening detail — Berlin's women winners 2000–05 all from Japan — is supported by the official Berlin winners guide: https://www.bmw-berlin-marathon.com/fileadmin/media/events/berlinmarathon/fotos/Presse/Mediaguide/Statistiken/BM25AlleSiegerInnenBERLIN-MARATHON.pdf

Spot-verified 2010s exception names:
- Tokyo official 2010: https://www.marathon.tokyo/en/about/past/2010/
- NYRR 2017: https://testcache.nyrr.org/media-center/press-release/20171107_nycm_2017racehighlights
- Boston Athletic Association 2018: https://www.baa.org/races/boston-marathon/history/

Source scope: six historical races only, not Sydney or every modern WMM; matched men's/women's completed in-person source years 2000–25; exclude source result flags, disqualification mentions, virtual/cancelled, 2026 and blank nationality. Exactly 133 paired events, 51 in the 2000s and 53 in the 2010s. Tokyo appears from 2007. These checks are **not** blanket verification of all source rows.

**Deliberate composition:** Charts 1 and 2 use identical six-race y positions, ten-year x spans and dot sizes. This is an intentional before/after visual reveal, not two disconnected scatterplots. Mobile QA must detect header/subtitle collision, bottom-row cropping and 2010s red-dot labels. Chart 3 has a full 0–100% y scale and angled endpoints must not overlap the x-axis. Derived CSVs rebuilt by `scripts/build_chart_views.py`.

Charts use repository `src/render_538.py`, `social_square`, approved Coffeetableviz palette, deterministic data and 1600px/390px/320px QA. Do not merge or publish this draft PR without approval. No site files or publishing map added.

**Final geometry QA:** Dot matrices set explicit y limits 0–7 for six race rows, creating actual marker clearance above the x-axis and below the title instead of allowing Matplotlib autoscaling to crop the top/bottom markers. Both charts share this range.
