# A line that disappears
*Icons of Data · Edition 01 · Charles Joseph Minard (1869)*
**Draft — not published · original source and images still to be checked for specific use rights**

Imagine drawing a long road across a map and then letting the road itself grow thinner every time fewer people are left to travel it.

That, broadly, is what Charles Joseph Minard did in 1869.

His famous diagram traces Napoleon's Russian campaign of 1812–1813. The line moves east towards Moscow, turns back west and becomes strikingly narrow. This is not simply a route map. The **width** tells part of the story.

## When a line stops being just a line

Minard's French legend explains that the width of the coloured bands represents the number of men, at a scale of one millimetre per ten thousand. A warm-toned band represents the march into Russia; a dark band represents the return.

Now the geography is doing two jobs. The route shows *where*. The width shows *how many*. The band's shrinking form lets the reader see a disastrous change without reading a column of figures.

And the map doesn't stop there. Place names, troop-count annotations and a lower temperature trace add context along the retreat.

This is the key editorial trick: the graphic keeps the important information near the place where it matters.

**[Figure 1: full historical original, credited to BnF collection / specific digitisation to be approved; annotations prepared separately.]**

## A remarkable picture. Not a perfect record.

There is a temptation to describe this as a precise count of everyone who died in Napoleon's campaign. It is not that.

Minard was working from contemporary histories and an army pharmacist's journal. He also stated that, for clarity, he represented certain detached corps as if they had remained with the main body. In other words, the map is a *designed historical synthesis*, with assumptions made visible in the small print.

Nor does the cold temperature trace establish that temperature alone caused every loss. The campaign was more complicated than one freezing night or one bad decision.

Those cautions make Minard more interesting rather than less. A compelling picture can contain careful judgement. The duty of a reader — and anyone reconstructing it — is not to mistake that judgement for a census.

**[Figure 2: troop bands reconstructed from HistData's 51 observations, with branch/group QA and explicit source note. No made-up troop counts.]**

## Four ways to encode one disaster

Pull the composition apart and the choices become clearer.

- **Geographic position** locates the journey.
- **Band width** represents the estimated size of the army.
- **Colour and direction** distinguish outward movement from retreat.
- **Temperature marks, dates and annotations** add a separate, time-linked view of the conditions.

Put these together and a long historical narrative becomes one connected visual argument.

Crucially, Minard didn't need a 3D chart, a dashboard, or a particularly excitable colour palette. He needed the right channels for the job.

**[Figure 3: Decode the Icon decomposition; exact original markings plus faithful recreation from the sourced temperature and route tables.]**

## The encoding lesson

The great idea isn't that every data story should look like Minard's. Most really shouldn't.

It's that **a mark can carry meaning through more than one property**. A line can show where something went and, through its width, how much of it remained.

The difficulty is knowing when that extra encoding clarifies and when it merely crowds the page.

Minard managed an unusually ambitious balance. It is why we're opening *Icons of Data* with his chart.

And why we should read the legend before marvelling at the line.

## TLDR

In 1869 Minard made troop strength part of the route itself. His bands change width as the plotted size of the army changes. The result shows what carefully chosen encodings can achieve — with the important reminder that the historical figures are estimates and the design incorporates explicit assumptions.

## Sources and method (pre-publication)
- Primary provenance: Bibliothèque nationale de France, *Carte figurative des pertes successives en hommes ... campagne de Russie 1812–13*, 1869: https://catalogue.bnf.fr/ark:/12148/cb40650878p
- Original French legend transcription / public-domain image metadata: https://commons.wikimedia.org/wiki/File:Minard.png (verify precise scan licence before reuse).
- Structured plotting data: `HistData` through `Rdatasets`, originally sourced from Lee Wilkinson / *Grammar of Graphics*. See https://friendly.github.io/HistData/reference/Minard.html. Current digitisation comprises 51 troop path records, 20 city records and 9 temperature records; these are *derived representations* of the historic diagram, not newly measured military history.
- QA note: the HistData help text mistakenly calls the campaign **1815**. The original 1869 title specifies **1812–1813**. Temperature is labelled in the original as Réaumur; do not silently call it Celsius.
- Next: check named troop labels against source scan, exact image licence and alt text; render and manually QA all reconstruction panels.
