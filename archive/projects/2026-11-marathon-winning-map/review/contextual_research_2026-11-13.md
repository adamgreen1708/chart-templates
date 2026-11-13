# Why did the red dots disappear? External context and evidence review

**Editorial research date:** 13 November 2026 (Europe/London).  
**Status:** Research context for the published post `site/_posts/2026-11-13-can-you-find-the-four-outsiders.md`. It is not a change to the race-winner dataset and does not prove a causal explanation.

## Strict separation of evidence

The underlying Coffeetableviz **source-derived observations** remain unchanged:

- Six historical big-city races, 2000–09: women's winning nationalities outside Kenya/Ethiopia = **31/53 = 58.5%**; men = **12/53 = 22.6%**.
- Same races, 2010–19: women = **4/59 = 6.8%**; men = **6/59 = 10.2%**.
- Difference in share: women **−51.7 percentage points**; men **−12.5 percentage points**.
- Dataset: [Shorts in Sports pinned original](https://github.com/shortsinsports/Data/blob/4ea0ca9e403d706a734d41088ad63e571ab0ca21/SIS-marathon_major_winners_2000_2026.csv); charting source at `data/marathon-majors/` pinned to commit `999b9b57c2cf61a1222bb4f08a4bdd885898e09a`.
- The archive's `data/qa_report.json` is the authoritative DQ evidence. It explicitly states that a **full official results audit is not complete** and that 216 completed source rows are classified `Not independently checked`.

The following findings come from **additional external scholarship or World Athletics reporting**. They are explanations **consistent with** the pattern, **not variables measured or causes identified** by our six-race chart data.

## External findings and source links

1. **Gender barriers and new professional pathways.** Michelle M. Sikes, a historian and author of *Kenya's Running Women*, describes women historically having fewer international racing and US university scholarship opportunities than Kenyan men, with access to paid international racing widening from the late 1980s and 1990s. First-hand interview with author from Penn State University, 1 Dec 2023:  
   https://www.psu.edu/news/research/story/qa-kenyas-trailblazing-women-runners-chart-course-success-new-book  
   Independent peer-reviewed social-anthropological account also supports professionalisation increasing Kenyan women's access:  
   https://rai.onlinelibrary.wiley.com/doi/10.1111/1467-9655.13961

2. **Rising Ethiopian marathon depth.** World Athletics' **2010** year-end road running review reported the annual count of Ethiopian female marathon runners under **2:26** rising from **eight in 2009** to **18 in 2010** (and its historical list gave one in 2000). The same review discussed Japan's difficulty replacing its exceptional generation in international majors. This is a measure of worldwide elite marathon times **not our selected race winners**:  
   https://worldathletics.org/news/news/2010-end-of-year-reviews-road-runningrace

3. **Broader East African women's world-ranking depth.** The **2011** World Athletics year-end road review counted **16 women from Kenya and Ethiopia in the world top 20** marathoners (eight from each country). Not a numerator or denominator for the six race-year matrices:  
   https://worldathletics.org/news/news/2011-end-of-year-reviews-road-runningrace

4. **Multiple contributing factors; no one 'magic gene'.** Wilber & Pitsiladis (2012), *Kenyan and Ethiopian distance runners: what makes them so good?*, *International Journal of Sports Physiology and Performance*, 7(2), 92–102, PMID 22634972, DOI 10.1123/ijspp.7.2.92. Reviews altitude, training, body characteristics, running economy and economic motivation; concludes no one unique genetic/physiological characteristic explains success.  
   https://pubmed.ncbi.nlm.nih.gov/22634972/  
   Additional peer-reviewed review on complex genetic/environmental/cultural interaction:  
   https://bjsm.bmj.com/content/47/9/545

5. **Japan's historical transition is not a national running collapse.** Historian Thomas R. H. Havens, *Marathon Japan: Distance Racing and Civic Culture*, ch. 6 *From Peak to Plateau: Elite Runners in the 2000s* (2015): Takahashi, Noguchi and Japanese Olympic successes in 2000–04 followed by comparatively poorer championship performances in 2008 and 2012, while mass/community running grew.  
   https://academic.oup.com/hawaii-scholarship-online/book/16704/chapter-abstract/173813798  
   World Athletics contemporary 2010 review (above) independently documents the international elite succession challenge.

## Evidence-quality and editorial rules

- **Do not claim causation.** Winners-only data do not contain entrants, finishing fields, nationality-adjusted race participation rates, coaching participation, prize incentives, doping tests or injury histories. We cannot quantify which mechanism explains the observed shift.
- **Do not conflate** '2010 annual worldwide runners under 2:26' with winners in six events; independent series with a distinct measure and denominator.
- **Do not imply a genetic determinism** about any country or ethnicity; peer-reviewed sport science finds multifactorial effects.
- **Do not claim Japan stopped producing marathon runners.** The evidence is about one exceptional generation and top international results; Japan also holds other elite races not in this six-race dataset.
- **Do not infer doping as an explanation** from nationality or winner's country. Any outcome revisions must be verified individually through official organisers. The source's eight explicitly flagged events were separately reviewed in `review/source_event_qa.md`.
- **Do not alter the chart CSVs, configs, images, source pin or the approved source-derived numbers** to accommodate contextual research.
- The post's deliberately conditional wording—'suggests', 'may', 'possibility', 'not proved'—is not a rhetorical flourish; it marks the boundary between the additional research and causal inference.

## Publication package

Article adds `## So why did the red dots disappear?` **after chart three, before TLDR**, and updates TLDR. In keeping with the house narrative, it adds insight without turning the piece into a literature review. The original charts/hero are unchanged. Links are to source reports/scholarship, not fictional explanatory data.
