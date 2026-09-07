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
- Data needed: Director, film count, average IMDb rating, individual titles where useful.
- Key stat: David Fincher's three films in the list average 8.40: Seven 8.6, Fight Club 8.8, The Curious Case of Benjamin Button 7.8.
- Why this chart matters: It shifts the story from film length to collaboration and explains where some of the strongest ratings cluster.
- QA risk: Multi-director credits need a clear counting rule before deriving repeat-director totals.

### Chart 3 — From 4.6 to 8.8

- Role: Land the aha moment.
- Story question: How wide is the rating spread across the 54-film list, and where do the peaks sit in time?
- Chart type: Timeline dot plot.
- Data needed: Year, Title, IMDb Rating.
- Key stat: Ratings span 4.2 points, from Cutting Class at 4.6 to Fight Club at 8.8; the late-1990s are a particularly strong run.
- Why this chart matters: It finishes on the full career-scale spread rather than another aggregate.
- QA risk: Multiple films in the same year can overlap; labels should be selective.

## Build order

1. Build and QA Chart 1.
2. Define the multi-director counting rule and derive Chart 2 data.
3. Derive and build Chart 3 timeline data.
4. Produce the publication package once all charts are stable.
