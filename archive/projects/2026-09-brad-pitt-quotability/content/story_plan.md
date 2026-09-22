# Brad Pitt quotability — story discovery

## Recommended story route

**Brad Pitt's most quotable character is Tyler Durden — and IMDb's character quote pages give us a measurable way to look at which roles have lingered most in audience memory.**

This is deliberately a story about **IMDb quote entries**, not the amount of dialogue in each screenplay and not an objective measure of cultural importance. Quote counts are user-curated, can change over time, and are affected by role size and IMDb participation.

## Why this route works

The existing 54-film Brad Pitt IMDb list already gives us film year and rating. The new enrichment adds the count displayed on Brad Pitt's IMDb character page for each film.

The pilot is already visually promising:

- Tyler Durden / *Fight Club*: 105 quote entries
- Louis / *Interview with the Vampire*: 60
- Billy Beane / *Moneyball*: 53
- Achilles / *Troy*: 50
- Sonny Hayes / *F1*: 46
- Mills / *Seven*: 45
- Rusty Ryan / *Ocean's Eleven*: 42

The gap between *Fight Club* and the rest is large enough to create a clear opening chart without inventing a subjective quote score.

## Story options considered

### Option A — Which Brad Pitt characters are most quotable?
Core argument: IMDb users have preserved some Pitt characters in far more quote entries than others.
Why it works: measurable, visual and directly connected to the idea.
Risk: quote counts are user-curated and partly reflect role size and fandom.
Recommendation: **use this as the main route**.

### Option B — Does quotability track film quality?
Core argument: compare IMDb quote-entry count with IMDb film rating.
Why it works: reuses the existing ratings dataset and may reveal interesting outliers.
Risk: role size is a major confounder. Treat as descriptive only; do not imply quotes cause ratings or vice versa.
Recommendation: useful Chart 2 if the completed dataset still shows a worthwhile pattern.

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
**Data:** completed Brad Pitt film list enriched with IMDb character quote-entry count  
**Key stat:** pilot high = Tyler Durden, 105  
**Why it matters:** gives the piece an immediate, concrete hook.  
**QA risk:** do not call this total dialogue or screenplay lines.

### Chart 2 — Quotable is not the same as highly rated
**Role:** Build the tension  
**Question:** Do films with more Pitt quote entries also have higher IMDb ratings?  
**Chart type:** scatter plot, quote entries vs IMDb rating  
**Data:** enriched quote-count dataset joined to the existing 54-film ratings list  
**Key stat:** calculate only after the 54-film enrichment is complete.  
**Why it matters:** tests the obvious assumption rather than merely ranking characters.  
**QA risk:** supporting roles naturally tend to have fewer attributed quotes; keep interpretation descriptive and consider a principal-role flag or billing-order annotation.

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

## Next build step

1. Complete the enrichment for all 54 films in the existing Brad Pitt list.
2. Record missing/unavailable character pages explicitly rather than treating them as zero.
3. Re-check duplicate characters and multi-role credits.
4. Calculate coverage and descriptive statistics.
5. Reassess Chart 2 after role-size / billing-order QA.
6. Only then create derived datasets and CHART_CONFIG files through the locked 538 workflow.
