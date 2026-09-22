# Brad Pitt quotability — story discovery

## Recommended story route

Brad Pitt's most quotable film-role page is Tyler Durden in Fight Club — but Fury gives us the human way into the story because Don 'Wardaddy' Collier sits high in the current IMDb quote-count snapshot.

This is deliberately a story about IMDb quote entries attached to Brad Pitt's film-role pages, not the amount of dialogue in each screenplay and not an objective measure of cultural importance. Quote counts are user-curated, can change over time, and are affected by role size, fandom and IMDb participation.

## Why this route works

The existing 54-film Brad Pitt IMDb list already gives us film year and rating. The new enrichment adds the count displayed on Brad Pitt's IMDb character page for each film.

The verified 44-film sample is visually strong:

- Tyler Durden / Fight Club: 105 quote entries
- Louis / Interview with the Vampire: 60
- Billy Beane / Moneyball: 53
- Achilles / Troy: 50
- Sonny Hayes / F1: 46
- Mills / Seven: 45
- Rusty Ryan / Ocean's Eleven: 42
- Don 'Wardaddy' Collier / Fury: 40

Fury is therefore not a token mention. Wardaddy ranks 8th among the 44 verified film-role pages.

The important definition is film role rather than unique character. A recurring character such as Rusty Ryan has a separate IMDb quote count for each Ocean's film, which becomes the point of Chart 3 rather than being silently aggregated in Chart 1.

Across the 44 verified film-role pages, quote-entry count and IMDb rating have a moderate positive association:
- Pearson correlation: 0.54
- Spearman rank correlation: 0.46

That is useful editorially because it is neither zero nor destiny. Highly rated supporting roles such as 12 Years a Slave (8.1 rating, 2 Pitt quote entries) and The Big Short (7.8, 4) sit well away from the broad pattern, while Sinbad has 39 quote entries at a 6.8 rating. Fury itself sits at 40 quote entries and a 7.6 rating.

## Recommended 3-chart story

### Chart 1 — Fury started it. Tyler Durden owns the answer.
Role: Set the scene.
Question: Which verified Brad Pitt film roles have the most IMDb quote entries?
Chart type: ranked dot plot.
Display: top 12 verified film-role pages.
Key stat: Tyler Durden = 105; Wardaddy = 40 and ranks 8th.
Why it matters: Fury supplies the personal trigger while the data supplies the stronger headline.
QA risk: do not call the count total dialogue, screenplay lines or a unique-character total.

### Chart 2 — Ratings help. They don't explain the quotes.
Role: Build the tension.
Question: Do films with more Pitt quote entries also have higher IMDb ratings?
Chart type: scatter plot with a linear trend line.
Data: all 44 verified film-role pages.
Key stat: Pearson r = 0.54; Spearman rho = 0.46.
Story labels: Fight Club, Fury, 12 Years a Slave, The Big Short and Sinbad.
Why it matters: tests the obvious assumption and shows where it breaks down.
QA risk: role size, fandom and IMDb participation are confounders; association is descriptive only.

### Chart 3 — Rusty did most of his talking on the first job
Role: Land the aha / character detail.
Question: What happened to Rusty Ryan's IMDb quote count across the Ocean's trilogy?
Chart type: three-point line.
Data: Ocean's Eleven 42, Ocean's Twelve 13, Ocean's Thirteen 17.
Why it matters: the same recurring character gives us a cleaner controlled example and resolves the film-role vs unique-character distinction.
QA risk: three observations are illustrative, not a general trend.

## Quote examples in the eventual blog post

The article must include a small number of short, verified Brad Pitt lines so the quote-count analysis feels concrete rather than abstract.

Preferred examples:
- Fury / Wardaddy: “Ideals are peaceful. History is violent.”
- Fight Club / Tyler Durden: “The things you own end up owning you.”
- Moneyball / Billy Beane: “How can you not be romantic about baseball?”
- Troy / Achilles: “You gave me peace in a lifetime of war.”
- F1 / Sonny Hayes: “Hope is not a strategy.”
- Ocean's Eleven / Rusty Ryan: “Been practicing that speech, haven't you?”

Use 3–5 across the post, not all mechanically. Quotes are supporting texture; do not imply that any single line explains the IMDb quote-entry count.

## Editorial framing

The eventual post can open from the real trigger:

I was watching Fury and wondering where Don 'Wardaddy' Collier would actually land if you tried to measure Brad Pitt's most quotable film roles.

Feature-art direction:
- tank silhouette or commander hatch;
- quote-burst / speech-fragment motif;
- light grey background;
- black/charcoal artwork;
- one muted red accent;
- no actor likeness required.

## Data definition

IMDb Quote Entries = the number labelled Quotes on Brad Pitt's IMDb character page for that title at the time checked.

It is:
- a current IMDb page count;
- user-curated;
- mutable;
- not a screenplay line count;
- not a screen-time measure;
- not an objective cultural-impact score.

## Coverage

- Existing Brad Pitt source list: 54 films.
- Quote count verified: 44 film-role pages.
- Unresolved after indexed-source checks: 10 films.
- Unresolved is not zero.
- Snapshot date: 23 September 2026.

## Next build step

The final chart specs, derived datasets and CHART_CONFIG files are staged. A local locked-renderer QA pass exposed and fixed only project-level spacing issues; the second pass produced clean 1600 × 1600 charts. Next gate is to create the repository PNG outputs through the GitHub archived-project render path and present those exact images for approval; no site publication should happen before that.
