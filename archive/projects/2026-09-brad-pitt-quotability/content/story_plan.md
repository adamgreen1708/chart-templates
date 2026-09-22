# Brad Pitt quotability — story discovery

## Recommended story route

**Brad Pitt's most quotable character is Tyler Durden — and IMDb's character quote pages give us a measurable way to look at which roles have accumulated the most user-curated quote entries.**

This is deliberately a story about **IMDb quote entries**, not the amount of dialogue in each screenplay and not an objective measure of cultural importance. Quote counts are user-curated, can change over time, and are affected by role size, fandom and IMDb participation.

## Why this route works

The existing 54-film Brad Pitt IMDb list already gives us film year and rating. The new enrichment adds the count displayed on Brad Pitt's IMDb character page for each film.

The verified 44-film sample is visually strong:

- Tyler Durden / *Fight Club*: 105 quote entries
- Louis / *Interview with the Vampire*: 60
- Billy Beane / *Moneyball*: 53
- Achilles / *Troy*: 50
- Sonny Hayes / *F1*: 46
- Mills / *Seven*: 45
- Rusty Ryan / *Ocean's Eleven*: 42

The gap between *Fight Club* and the rest is large enough to create a clear opening chart without inventing a subjective quote score.

Across these 44 verified films, quote-entry count and IMDb rating have a **moderate positive association**:
- Pearson correlation: **0.54**
- Spearman rank correlation: **0.46**

That is useful editorially because it is neither zero nor destiny. Highly rated supporting roles such as *12 Years a Slave* (8.1 rating, 2 Pitt quote entries) and *The Big Short* (7.8, 4) sit well away from the broad pattern, while *Sinbad* has 39 quote entries at a 6.8 rating.

These figures are provisional until the ten unresolved films are either verified or explicitly documented as unavailable.

## Story options considered

### Option A — Which Brad Pitt characters are most quotable?
Core argument: IMDb users have preserved some Pitt characters in far more quote entries than others.
Why it works: measurable, visual and directly connected to the idea.
Risk: quote counts are user-curated and partly reflect role size and fandom.
Recommendation: **use this as the main route**.

### Option B — Do better-rated films produce more Pitt quote entries?
Core argument: there is a moderate positive relationship in the verified sample, but rating clearly does not explain the whole pattern.
Why it works: reuses the existing ratings dataset and produces useful counterexamples rather than a simplistic correlation story.
Risk: role size is a major confounder. Treat as descriptive only; do not imply quotes cause ratings or vice versa.
Recommendation: **retain as Chart 2**, with outliers doing the storytelling.

### Option C — How does the same character change across sequels?
Core argument: Rusty Ryan has 42 quote entries in *Ocean's Eleven*, 13 in *Ocean's Twelve* and 17 in *Ocean's Thirteen*.
Why it works: same actor and character gives a cleaner mini-comparison.
Risk: only three films.
Recommendation: strong closing chart / small-multiple detail.

## Recommended 3-chart story

### Chart 1 — Tyler Durden isn't even close
**Role:** Set the scene  
**Question:** Which Brad Pitt characters have the most IMDb quote entries?  
**Chart type:** ranked dot plot or horizontal bars  
**Data:** verified Brad Pitt film rows enriched with IMDb character quote-entry count  
**Key stat:** Tyler Durden = 105; next highest Louis = 60  
**Why it matters:** gives the piece an immediate, concrete hook.  
**QA risk:** do not call this total dialogue or screenplay lines.

### Chart 2 — Ratings help. They don't explain the quotes.
**Role:** Build the tension  
**Question:** Do films with more Pitt quote entries also have higher IMDb ratings?  
**Chart type:** scatter plot, quote entries vs IMDb rating  
**Data:** quote-count enrichment joined to the existing 54-film ratings list  
**Key stat:** verified n=44; Pearson r=0.54; Spearman rho=0.46  
**Story labels:** Tyler Durden / *Fight Club*; *12 Years a Slave*; *The Big Short*; *Sinbad*  
**Why it matters:** tests the obvious assumption and shows where it breaks down.  
**QA risk:** supporting roles naturally tend to have fewer attributed quotes; association is descriptive and role size is a confounder.

### Chart 3 — Rusty did most of his talking on the first job
**Role:** Land the aha / character detail  
**Question:** What happened to Rusty Ryan's IMDb quote count across the Ocean's trilogy?  
**Chart type:** three-point line or dot sequence  
**Data:** *Ocean's Eleven* 42, *Ocean's Twelve* 13, *Ocean's Thirteen* 17  
**Why it matters:** a controlled recurring-character example and a neat dry finish.  
**QA risk:** three observations are illustrative, not a trend claim.

## Data definition

`imdb_quote_entries` = the number labelled “Quotes” on Brad Pitt's IMDb character page for that title at the time checked.

It is:
- a current IMDb page count;
- user-curated;
- mutable;
- not a screenplay line count;
- not a screen-time measure;
- not an objective cultural-impact score.

## Coverage

- Existing Brad Pitt source list: 54 films.
- Quote count verified: 44 films.
- Unresolved after indexed-source checks: 10 films.
- Unresolved is **not zero**.

The unresolved titles should be kept in an audit list and excluded from quote-count calculations unless a reliable count is obtained.

## Next build step

1. Create an explicit unresolved-title audit for the remaining ten films.
2. Re-check those titles through a source path that exposes the character-page count reliably.
3. Re-check duplicate characters and multi-role credits.
4. Freeze the verified snapshot date and coverage.
5. Build the three derived chart datasets.
6. Create CHART_CONFIG files through the locked 538 workflow and render/QA only after the coverage gate is accepted.
