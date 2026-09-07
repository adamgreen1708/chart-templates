# Brad Pitt IMDb list — story plan

## Source scope

Source: IMDb list export supplied by Adam Green on 7 September 2026.

The supplied export contains 54 film rows. Treat the analysis as a story about the films in this IMDb list. Do not claim the source is a complete Brad Pitt filmography unless that completeness is separately verified.

## Recommended story route

Brad Pitt films in this list reward patience: longer films tend to carry stronger IMDb ratings, while the strongest repeat-director partnership and the late-1990s run add useful context to the broader career pattern.

## Why this is the strongest route

The clearest relationship in the supplied data is runtime versus IMDb rating. Films under 110 minutes average about 6.09, while films running 130 minutes or more average about 7.59. That is a stronger editorial hook than a generic chronology of ratings.

## 3-chart story

### Chart 1 — Brad Pitt films reward patience

- Role: Set the scene.
- Story question: Do longer films in this list tend to rate better?
- Chart type: Scatter.
- Data needed: Title, Runtime (mins), IMDb Rating.
- Key stat: 14 films under 110 minutes average 6.09; 19 films at 130+ minutes average 7.59.
- Why this chart matters: It establishes the clearest relationship in the data immediately.
- QA risk: Annotation collisions around the high-rating cluster and the right edge near Babylon.

### Chart 2 — Fincher gets the best-rated Pitt

- Role: Build the tension.
- Story question: Which repeat directors are associated with the strongest-rated films in the list?
- Chart type: Dot plot.
- Data needed: Director, film count, average IMDb rating.
- Counting rule: Split comma-separated director credits into individual directors; each credited director receives one film credit. Only directors with at least two credited films are retained. None of the co-directors from multi-director rows appears twice, so this rule does not alter the six repeat-director results.
- Key stat: David Fincher's three films average 8.40: Seven 8.6, Fight Club 8.8, The Curious Case of Benjamin Button 7.8.
- Repeat-director ranking: Fincher 8.40 (3), Tarantino 8.00 (2), Tony Scott 7.50 (2), Soderbergh 7.03 (3), Andrew Dominik 6.85 (2), Ridley Scott 6.50 (2).
- Why this chart matters: It shifts the story from film length to collaboration and shows where some of the strongest ratings cluster.
- QA risk: Keep film-count labels inside the right safe margin.

### Chart 3 — From 4.6 to 8.8

- Role: Land the aha moment.
- Story question: How wide is the rating spread across the 54-film list, and where do the peaks sit in time?
- Chart type: Scatter timeline.
- Data needed: Year, Title, IMDb Rating, five-year-window highlight flag.
- Key stat: Ratings span 4.2 points, from Cutting Class at 4.6 to Fight Club at 8.8.
- Window rule: Compare every rolling five-year period and retain windows containing at least three films. The highest average is 1995–99: seven films averaging 7.63.
- Why this chart matters: It finishes on the full rating spread while showing that the strongest sustained run came relatively early in the list.
- QA risk: Multiple films share years; use selective labels and highlight the seven 1995–99 films rather than labelling every point.

## Build order

1. Build and QA Chart 1.
2. Derive and build Chart 2 using the explicit director-credit rule.
3. Derive and build Chart 3 using the rolling five-year-window rule.
4. Produce the publication package once all charts are stable.
