# Marathon Majors: a world of winners, then four exceptions

**Draft editorial revision 3 — not for live publication.** Source: `data/marathon-majors` at commit `999b9b57c2cf61a1222bb4f08a4bdd885898e09a`; upstream Shorts in Sports pinned in that README.

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

The original source is **not a blanket independently verified official result archive**. The explicitly mentioned winners and streak were verified independently; additional source flags may require a wider audit before publication among a global specialist audience. This is six historical races, not all current World Marathon Majors (Sydney omitted).

## Release gate

All three PNGs must pass source-backed 1600px/390px/320px QA, including one-line headlines, source-footer, complete 0–100% axis and no cut-off dot rows. Review the blog and images in the draft PR. No `site/_posts`, site asset map or live publication without approval.
