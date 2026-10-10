# Nightingale #04 — source and claim audit
**Checked:** 10 October 2026
**State:** institutional/source research complete for working manuscript; finished visuals and author approval outstanding.

| Claim | Evidence | Decision |
|---|---|---|
| The original diagram was published with Nightingale's `Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army` in **1858**. | Wellcome (plate L0041105), Commons file metadata, Royal Statistical Society history, original 1858 volume | **Verified**. Other related figures were printed in **1859**; never blur their exact editions. |
| Right circle Apr 1854–Mar 1855; left circle Apr 1855–Mar 1856. | Original captions and historiography | Verified. |
| Blue = “preventable or mitigable zymotic diseases”, red = wounds, black = other causes. | Original plate legend, historical interpretation | Verified. Retain historical category wording; modern term 'infection' alone is not equivalent. |
| Wedges show **annualised rates per 1,000 soldiers** by area rather than by radius. | Original plate; R HistData dataset documentation; statistical historians | Verified. For fixed angle area ∝ radius²; so radius ∝ sqrt(rate). |
| Colours are drawn from a **common centre** rather than additive bands. | Original plate legend; Royal Statistical Society commentary | Verified. Don't draw mistaken stacked polar bars. |
| HistData has exactly **24** monthly records, April 1854–March 1856, with counts, average army strength and annualised rates. | HistData official docs and direct archived CSV from Rdatasets, blob `0e69a3b02360ba23669cfb94a2d53c8521a59a3f` | Verified. Formula: 12 × 1000 × cause deaths / average estimated army strength; published rates rounded to 1 d.p. |
| First period Apr 1854–Mar 1855 disease=11,157, wounds=772, other=1,365; total=13,294. | Independent summation of twelve HistData rows | Verified calculated result. Disease share 11,157/13,294 = **83.925%**. Use ~84% **of recorded first-period deaths**, NOT proportion of area in a chart. |
| Second period Apr 1855–Mar 1856 disease=3,319, wounds=986, other=383, total=4,688. | Summation of other 12 rows | Verified. Comparisons of *total counts* need care because army strengths changed. |
| Jan 1855 was disease annualised-rate peak in transcription: 1,022.8 per 1,000 troops. | Record: army strength 32,393; disease 2,761; formula above | Verified. It is **annualised**, not a claim 1,023 per 1,000 actually died in one month. |
| Sanitary reforms and other changes happened as first/second periods differ. | Nightingale publication; statistical historians / MIT Press | Supported context. **Not** causal isolation from the chart. |
| Nightingale invented the polar-area chart (or every 'rose' element). | Statistical historians indicate **predecessors** | Reject. Her significance includes using visual rhetoric/political persuasion, careful data categorisation and revising an earlier misleading radial chart. |
| Nightingale called this graphic itself a 'coxcomb'. | Royal Statistical Society sources disagree with common shorthand | Avoid this claim. 'Polar-area diagram' is more accurate; mention 'rose' only as later nickname. |

## Authoritative research / object references
- **Primary scan and image licence**, Wellcome L0041105, 1858: https://commons.wikimedia.org/wiki/File:Diagram_of_the_causes_of_mortality_in_the_army_Wellcome_L0041105.jpg ; CC BY 4.0 https://creativecommons.org/licenses/by/4.0/
- Wellcome collection work record associated with L0041105: https://wellcomecollection.org/works/sz9sms2m
- **Primary work / 1858 Notes**, Wellcome digitisation catalogue: https://wellcomecollection.org/works/b20387118
- **Official dataset docs**: https://search.r-project.org/CRAN/refmans/HistData/html/Nightingale.html
- Direct dataset: https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/HistData/Nightingale.csv (24 observations).
- **Royal Statistical Society historic essay**: Helen Joyce, *Florence Nightingale: a lady with more than a lamp* (2008), https://rss.onlinelibrary.wiley.com/doi/full/10.1111/j.1740-9713.2008.00327.x — historical context, wedge areas, common centre, impact.
- **MIT Press history**: Murray Dick, *Visualizing Data To Save Lives* (2020), https://thereader.mitpress.mit.edu/history-of-early-public-health-infographics/ — charts as a sequence of data-informed reform arguments.
- **Statistical history**: Michael Friendly/RJ Andrews, *The Radiant Diagrams of Florence Nightingale* (2021) DOI 10.2436/20.8080.02.106; historical geometry and collaboration.
- **Historia Medica historical object profile**: https://historiamedica.org/sources/nightingale-polar-area-diagram/ — original 1858, two years, rates, historical limits.

## Specific QA concerns
- First-year death totals are archival transcription figures, not verified individual deaths from every battlefield/hospital; avoid claims about all Crimean War casualties.
- Avoid writing that blue areas shrank *because* sanitation alone changed; cannot prove a causal factor in the observational before/after comparison.
- 'Zymotic' is a 19th-century epidemiological grouping; code for causes may have been inconsistent. Preserve label with accessible explanation.
- Original year circle layout is chronologically reversed left to right (older on right).
- A polar area diagram is easy to mis-draw as radius-proportional; use square-root transform and equal angles.
- Rights: digitised **specific photo** L0041105 is CC BY 4.0; include Wellcome attribution and modifications if used. Do not assume the licence covers another historic Nightingale image.
