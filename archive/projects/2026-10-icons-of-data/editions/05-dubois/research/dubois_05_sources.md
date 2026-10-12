# Icons of Data #05 — W. E. B. Du Bois source and claim audit
**Researched:** 12 October 2026
**State:** Original object verified; all four numbers read against the original LoC JPEG (800×1000) and corroborated independently in Yale National Initiative Unit 26.01.04 (2026); US Census total reconciliation checked. Visual render completed for editorial review, not yet approved for GitHub image publication.

## Exact original artefact
- **Library of Congress:** [The Georgia Negro — City and rural population. 1890](https://www.loc.gov/item/2013650430/), **LCCN 2013650430**; LOT 11931 no. 11 [P&P]; **digital ID ppmsca.33873**; digitised original, a roughly 710×560 mm ink and watercolour drawing.
- Chart's subject year **1890**, artwork created **circa 1900**, displayed as part of the American Negro Exhibit at **the 1900 Paris Exposition**. Never date the physical drawing as 1890 because of its title.
- LoC catalogue credits **W. E. B. Du Bois** as creator and states chart was prepared by Du Bois; **Cooper Hewitt/Smithsonian** and LoC wider-collection records credit Du Bois **and Atlanta University collaborators** for the larger series. Phrase cautiously rather than assuming every colour stroke was painted by Du Bois himself.
- **Usage:** LoC item specifically says **“No known restrictions on publication”**, not a grant of copyright permission. Assess UK/US reproduction rights on this precise item before publishing. Original may be linked for editorial review even while image clearance is evaluated.
- Digital asset catalog: https://www.loc.gov/pictures/item/2013650430/ ; published JPEG mirror when verified: `https://tile.loc.gov/storage-services/service/pnp/ppmsca/33800/33873v.jpg`. Fetch/provenance validate exact file before self-hosting.
- Cooper Hewitt / Smithsonian, Ellen Lupton (2023), [The Typography of W. E. B. Du Bois](https://www.cooperhewitt.org/2023/02/23/the-typography-of-w-e-b-du-bois/), directly identifies the **long red spiral comparing rural Black Georgia with smaller urban groups** and discusses hand-lettered exhibition posters.
- Library of Congress blog (2020), [African Americans at the Turn of the 20th Century: A Graphic Visualization](https://blogs.loc.gov/picturethis/2020/04/african-americans-at-the-turn-of-the-20th-century-a-graphic-visualization/), describes the largest category as “country and villages” and smaller urban categories as straight marks.

## Research on purpose and historical context
- LoC [collection summary](https://www.loc.gov/item/2005682657/) and [72-object chart group](https://www.loc.gov/item/2005679642/) record the exhibition as a comprehensive picture of the life, education, conditions and progress of Black Americans under post-emancipation conditions.
- Smithsonian Magazine, [How W.E.B. Du Bois Disrupted America's Dominance at the World's Fair](https://www.smithsonianmag.com/smithsonian-institution/how-web-du-bois-disrupted-americas-dominance-at-the-worlds-fair-180981538/), explains his critique of colonial power and US racism. This single rural-population chart does not on its own prove specific social or economic progress.
- LoC wider record's 72 artworks (various specific groups) are distinct from early promotional statements about 32 selected charts; do NOT present these as contradictory totals for exactly the same set.

## Independent source checks completed 12 October 2026
- **Primary image inspected:** LoC original `https://tile.loc.gov/storage-services/service/pnp/ppmsca/33800/33873v.jpg`, from catalogue item `2013650430`. Legible numeric labels: **78,139** (cities over 10,000), **8,025** (cities 5,000–10,000), **37,699** (cities 2,500–5,000), **734,952** (country and villages).
- **Independent university transcript:** [Yale National Initiative, curriculum unit 26.01.04 (2026)](https://teachers.yale.edu/curriculum/units/2026/1/4/8), supplies precisely **78,139, 8,025, 37,699, 734,952**, and distinguishes the 1890 size-boundary groupings. This is corroboration, not a second historical primary record.
- **Secondary example:** [W. E. B. Du Bois recreations, SpeakerDeck](https://speakerdeck.com/ajstarks/recreations-of-w-dot-e-b-du-bois-data-portraits), also reproduces the same four counts.
- The four independently corroborated group counts sum to the official 1890 Georgia Black-population figure **858,815**, referenced to US Census historical Table 25. Ratio 734,952 / 858,815 = **85.577%**, round **85.6%**.
- The older *provisional* data file and two conflicting republished captions remain for audit only. Use **`data/verified_population_1890.csv`** exclusively for any modern chart.
- No claim that we inspected the larger 25MB/51MB TIFF; the actual *LoC medium original JPEG* was legible and displayed and the independent Yale counts corroborate its labels.
- **Rights:** Original LoC item states *No known restrictions on publication*. It does not guarantee a global waiver; credit Du Bois/Atlanta University contributors where appropriate and LoC reproduction number `LC-DIG-ppmsca-33873`.
- No website edit or merge is authorised by approval of the title.

## Numerical evidence (verified primary-image transcription)
| 1890 category printed in the chart | Verified LoC / Yale reading | Verification status |
|---|---:|---|
| Cities over 10,000 inhabitants | 78,139 | Verified LoC image and Yale (secondary reproductions conflict) |
| Cities 5,000–10,000 | 8,025 | Verified LoC image + Yale |
| Cities 2,500–5,000 | 37,699 | Provisional; source reproductions conflict |
| Country and villages | 734,952 | Verified LoC original JPEG and Yale |
| Sum | **858,815** | The four verified source figures sum to this, matching the official 1890 Georgia total; independent original-image reading and Yale table, not arithmetic alone, establish the individual values |

- **US Census Bureau**, [Georgia: Race and Hispanic Origin, 1790 to 1990, table 25](https://www2.census.gov/library/working-papers/2002/demo/pop-twps0056/table25.pdf): Black Georgia population **858,815 in 1890**.
- A Smithsonian Magazine article's [reproduction PDF](https://r-class.github.io/paf-515-course-materials/labs/wk03/smithsonianmag.com-WEB-Du-Bois-Visionary-Infographics-Come-Together-for-the-First-Time-in-Full-Color.pdf) transcribes one urban group as **70,839**, conflicting with the all-category census reconciliation; the New Yorker [essay](https://www.newyorker.com/books/page-turner/what-web-du-bois-conveyed-in-his-captivating-infographics) displays **78,139**, but its description gives **37,899** for the 2,500–5,000 category, conflicting with **37,699** in the Smithsonian page image. Do NOT silently resolve these from secondary sources.
- Compute checks: 78,139 + 8,025 + 37,699 + 734,952 = **858,815**. Rural/villages = 734,952/858,815 = **85.58%** (rounded ≈86%) using the verified source transcription. Urban three groups together = 123,863 (≈14.42%).
- Different historical source **Du Bois, Negro Landowner in Georgia** tabulates settlements **4,000+** using a *different city size threshold*, yielding a different 'urban' subtotal. Do not mix categories or swap in these figures as if from the original spiral chart.
- Interpret geometry carefully: the red coiled line visualises the overwhelming magnitude and saves page space. Exact proportionality of **drawn path lengths** must be measured/verified before claiming this is a strict line-length scale or claiming colour semantics beyond which group each line represents.
- Historical chart legend uses outdated racial language; quote only what is needed for faithful historical attribution and use respectful contemporary narrative otherwise.
- The chart is a snapshot of one census year, not evidence that urbanisation occurred **because** of any specific law, policy or migration driver.

## Publication gates
1. **Completed:** Inspect LoC original JPEG with readable category labels; cross-check all four counts against Yale independent transcript and Census total; record contradictory secondary reprints rather than patching numbers.
2. Clear the precise original image's reproduction rights (LoC 'no known restrictions' is positive but not a substitute for assessment).
3. **Completed for author visual review:** draw a zero-based chart #02 from the four source-confirmed 1890 Georgia counts; show counts as printed and 85.6% as explicitly calculated.
4. Original poster photo must be authentic and cited; never use generated imitation as historical artefact.
5. Final author visual approval + desktop/mobile QA + explicit PR merge/publishing approval.
