# Tom Hanks Colour Bank revisited — story plan

## Scope

Source: IMDb non-commercial datasets accessed 20 September 2026. The uploaded ratings file matches the official IMDb file whose upstream run date is 19 September 2026.

The joined source contains 65 rated movie-type records where Tom Hanks (`nm0000158`) appears as an actor in IMDb's principal-credit table. Four documentary records are excluded from the narrative-film analysis, leaving 61 films from 1980 to 2026.

This is a story about rated narrative films among IMDb principal credits. It is not presented as a guaranteed complete Tom Hanks filmography. IMDb ratings describe audience ratings for each film, not critical acclaim or an assessment of Hanks' individual performance.

## Recommended story route

Tom Hanks' ratings record changes sharply in 1992: 10 of the next 14 films rate 7.5 or higher, compared with none of the previous 15. The broad peak ends, but the five *Toy Story* films maintain an above-median thread across 31 years.

## Why this is the strongest route

The 1992–2002 period is a much stronger editorial argument than a generic decade ranking. Its 14 films average 7.79 on IMDb and 10 rate 7.5 or higher. Before the run, none of 15 films reaches that threshold; after it, 6 of 32 do. The *Toy Story* sequence provides a recognisable, useful Friday-night landing point without pretending that a film rating measures one actor's performance.

## Three-chart story

### Chart 1 — Hanks found another gear in 1992

- Role: Set the scene.
- Story question: When did the film ratings materially change?
- Chart type: Scatter timeline.
- Data needed: Year, title, IMDb rating, 1992–2002 highlight flag.
- Key stat: The 14 films released from 1992–2002 average 7.79; 10 rate 7.5+.
- Why this chart matters: It shows the whole career and makes the shift visible before summarising it.
- QA risk: Several films share a year. Use restrained labels and enough x/y breathing room; do not imply that the rating measures Hanks' performance.

### Chart 2 — Ten hits in eleven years

- Role: Build the tension.
- Story question: How different was the peak run from the periods around it?
- Chart type: Ranked dot comparison.
- Data needed: Period, film count, films rated 7.5+, share rated 7.5+.
- Key stat: 0 of 15 before the run, 10 of 14 during it, and 6 of 32 after it rate 7.5+.
- Why this chart matters: It quantifies the distribution shift without hiding behind a single average.
- QA risk: Make the unequal film counts explicit in labels and subtitle; format the x-axis as percentages.

### Chart 3 — Woody outlasted the golden run

- Role: Land the aha moment.
- Story question: Which recognisable thread remained above the career median long after the peak?
- Chart type: Line chart across franchise releases.
- Data needed: Year, title and IMDb rating for the five *Toy Story* films.
- Key stat: All five rate above the 6.9 overall median; the franchise median is 7.9 across 1995–2026.
- Why this chart matters: It converts the career analysis into a clear, relatable film-night takeaway.
- QA risk: Ratings are a dated snapshot, and the 2026 film has had less time to accumulate votes. Connect points as franchise sequence, not as a continuous annual trend.

## Visual direction

Use the current coffeetableviz house palette only:

- background `#F3F4F6`
- focus blue `#1F8FA8`
- highlight red `#C44E52`
- context grey `#D9D9D9`
- secondary grey `#7A7A7A`
- text `#111111`
- supporting text `#555555`

Do not reuse the old Colour Bank No.6 palette in the refreshed charts.
