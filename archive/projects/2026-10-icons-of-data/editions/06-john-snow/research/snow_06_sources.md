# Icons of Data #06 — research audit (John Snow)
**Date:** 12 October 2026
**State:** institutional source, versioned original reproduction and digitised map datasets verified. Editorial kickoff only; no charts or website assets generated.

## Specific original and date/edition
- **1854** is the cholera outbreak in central London's Soho/Broad Street area, **not** the publication year of the main map.
- **1855**: John Snow, [*On the Mode of Communication of Cholera*, 2nd edition](https://wellcomecollection.org/works/uqa27qrt), John Churchill, London. Wellcome catalogue says 162 pages and two folded maps; book digitisation marked **Public Domain Mark**.
- **Chosen precise map photo**: [Wellcome L0063431 on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Map_showing_deaths_from_Cholera_in_Broad_Street..._Wellcome_L0063431.jpg), titled *Map showing deaths from Cholera in Broad Street, Golden Square and the neighbourhood, from 19th August to 30th September 1854*. Metadata associates it with Snow's **1855 second-edition book** and records image size **5064×4856**; specific reproduction released **CC BY 4.0** on Commons: https://creativecommons.org/licenses/by/4.0/ . Source photograph Wellcome Collection. At publication time verify the exact image bytes, licence, attribution and transformations.
- **Different map**: St James Parish Cholera Inquiry Committee report (July 1855) contains another image, [*Plan Showing the Ascertained Deaths from Cholera*](https://wellcomecollection.org/works/dx4prdbj), separate Wellcome object and edition. Do not attribute the parish plate to the second-edition book or silently interchange their geometries/extra annotations.
- UCLA [historical mapping and myth explanation](https://epi-snow.ph.ucla.edu/Stream2_BSPoutbreak_f.html) documents a **December 1854** map display followed by later published versions and a corrected pump position. Avoid asserting the book map was the first ever drawn or the exact map consulted before handle removal.

## Map encoding and limits
- **Black bars** stand for fatalities associated with houses where fatal attacks began, and multiple bars at one address are stacked. **Pumps** are other marked features; street position enables a qualitative proximity investigation. Data on each individual's water access were established through interviews and records, not encoded by each short mark.
- [University of Chicago Data 8 teaching chapter](https://data8.datascience.uchicago.edu/chapters/02/1/observation-and-visualization-john-snow-and-the-broad-street-pump.html) describes marks as deaths, pumps, and explains that apparent geographic counterexamples require attention to the street network.
- [Peer-reviewed overview of map's historical role](https://pmc.ncbi.nlm.nih.gov/articles/PMC8504888/) discusses Snow's position, comparison of London water suppliers, household investigations and limits of pictorial interpretation.
- The map **does not** directly encode case-onset dates, infections that were not fatal, person movements or exposure to specific pump water. Black marks are **counts**, not rates, and household population denominators are absent.
- Snow already reasoned about polluted water **before** plotting this map. It did not by itself discover the source. His text supplied interviews, anomalies, exposure histories and competing explanations. Avoid simplified inventor-genius mythology.
- **Pump-handle removal**: authorities removed the handle **8 September 1854**, but daily new fatal attacks had already fallen sharply from the peak. [UCLA primary-source retrospective and Whitehead account](https://epi-snow.ph.ucla.edu/Stream2_BSPoutbreak_e.html), [UCLA original text context](https://epi-snow.ph.ucla.edu/Stream2_BSPoutbreak_f.html), and [historians' critique](https://pmc.ncbi.nlm.nih.gov/articles/PMC7108616/) warn against claiming removal *ended* the outbreak. This does not imply removal could not have prevented later exposures.
- No claim Snow first invented all disease maps, proved germ theory, discovered the pathogen, or demonstrated causation from an unadjusted spatial clustering alone.
- [Critical historical interpretation and exact period](https://historiamedica.org/sources/john-snow-cholera-map/) explicitly cautions about the 19 August–30 September 1854 mapped period, selected deaths and unavailable population/risk denominators.

## Digitised reconstruction dataset (not original addresses or a modern GPS file)
- CRAN `HistData` Snow documentation: https://www.stat.ethz.ch/CRAN/web/packages/HistData/refman/HistData.html ; https://rdrr.io/rforge/HistData/man/Snow.html .
- Public versioned source files from `vincentarelbundock/Rdatasets` master branch, with blob SHA pins:
  - `csv/HistData/Snow.deaths.csv` — **578** observations, columns `rownames,case,x,y`, Git blob `de97ca1939d6277782a1a50bf94eadafed158507`.
  - `csv/HistData/Snow.pumps.csv` — **13** rows, `rownames,pump,label,x,y`, Git blob `c739dd38f267e2db8222c16dbf7f9d707b2254db`.
  - `csv/HistData/Snow.streets.csv` — **1,241** vertex rows / **528** grouped street segments, `rownames,street,n,x,y`, Git blob `300b3b266a50b29511c2ac8a35e04000a5c22f24`.
- The x/y values are local, arbitrary historical drawing-map coordinates; stacked display positions do **not** prove actual address point precision. Snow.deaths' `case` is an arbitrary randomized ID — **not a date or chronological sequence**.
- Do not treat 578 as a modern count of *all* local cholera deaths (elsewhere outbreak total is estimated/reported differently), or `n` in streets as the number of people. No individual dates exist in `Snow.deaths`.
- One Broad Street pump in dataset: `label=Broad St`, index `pump=7`, local x **12.5713596**, y **11.72717**. Plot with other twelve for context; do not convert to geospatial latitude/longitude without documented georeferencing.
- Separate 1855 parish report map can contain a **boundary for distances to pumps**; adding that boundary to a reconstruction of the book edition would misattribute an illustration unless explicitly marked as a separately sourced analytical layer.

## Publication check-list
- Full original image verifiable, source creator/CC BY attribution/resizing.
- Reconstruction records precisely 578 marks / 13 pumps; verify 528 polyline street segment groups; equal aspect; no data fabrication or false axes.
- Comparative designs must not imply mortality **rates** where at-risk populations are missing.
- Temporal claim separated from visual appearance of 1855 map.
- Accessibility captions and 390/320px QA; approval required at editorial, image and final Pages merge stages.
