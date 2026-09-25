# Mel Gibson career pivot — validated story discovery

## Dataset read

The official IMDb non-commercial dataset pass resolves **Mel Gibson = nm0000154**, born 1956, profession `actor,producer,director`.

Analytical scope follows the repo's actor-project rules:

- principal acting credits from `title.principals`;
- directing credits from `title.crew`;
- `titleType=movie`;
- released titles with a year and IMDb rating;
- minimum **1,000 votes**;
- excluded/unrated/unreleased/non-movie records retained in the audit CSV.

Validation result:

- 103 acting/directing career-title IDs before analytical filters;
- 65 released movie titles;
- 63 rated released movie titles;
- 62 titles meet the 1,000-vote floor;
- **62 analytical rows** with no duplicate `tconst` values;
- **58 acting rows**;
- **6 directing rows**;
- **2 films where Gibson both acts and directs**: *The Man Without a Face* and *Braveheart*;
- 100% title-basics join coverage;
- 98.41% of rated released movies survive the vote floor.

IMDb ratings describe the titles, not Gibson's individual acting or directing performance. IMDb principal ordering is not a formal screen-time or billing measure.

## What the data says

### The remembered peak is real in the title ratings

*Lethal Weapon* (1987) is rated **7.6** and *Braveheart* (1995) **8.3**, the highest-rated eligible acting title in this dataset.

Across eligible acting movies:

- 1980s: 11 titles, mean rating 6.75, median 7.1;
- 1990s: 13 titles, mean 6.72, median 6.7;
- 2010s: 9 titles, mean 6.49, median 6.6;
- 2020–25: 16 titles, mean 5.26, median 5.6.

The recent acting run is therefore **busier but lower-rated at title level**.

### He did not simply disappear

The largest gap between years containing an eligible acting movie is **seven release years**, from 2003 to 2010. There are no eligible acting movies in 2004–09.

After the return:

- 2010s: 9 eligible acting films;
- 2020–25: **16** eligible acting films;
- the whole 1990s: **13**.

So the clean data contradicts a simple "he vanished" narrative. Output eventually became higher than the decade most associated with his movie-star peak.

A supporting, carefully worded indicator also changes: all 13 eligible acting movies in the 1990s place Gibson first in IMDb's principal ordering, compared with 7 of 16 in 2020–25. This is useful context, but principal order must not be described as screen time or formal billing.

### Directing is a sparse second career

The six released directing features in the analytical dataset are:

| Year | Film | IMDb rating | Gap from previous |
|---|---|---:|---:|
| 1993 | The Man Without a Face | 6.7 | — |
| 1995 | Braveheart | 8.3 | 2 years |
| 2004 | The Passion of the Christ | 7.3 | 9 years |
| 2006 | Apocalypto | 7.9 | 2 years |
| 2016 | Hacksaw Ridge | 8.1 | 10 years |
| 2025 | Flight Risk | 5.2 | 9 years |

The Academy records Gibson winning Directing for *Braveheart* at the 1996 ceremony and returning as a Directing nominee for *Hacksaw Ridge* at the 2017 ceremony.

The important pattern is not that every Gibson-directed film is highly rated — *Flight Risk* clearly breaks that idea. It is that directing became an infrequent, long-gap second lane that produced several of the strongest-rated titles associated with his later career.

## Ranked story options

### 1. He didn't disappear. He changed jobs, then came back differently. — recommended

**Core argument:** The nostalgic movie-star peak is visible in the data, but the surprise is what follows. Gibson has a genuine acting gap, then returns to increasingly prolific acting work — 16 eligible films in 2020–25 — while the films themselves rate markedly lower than the 1980s–90s run. In parallel, directing becomes a sparse second career with several conspicuous peaks.

**Why it leads:** It answers Adam's actual question without forcing a simplistic rise/fall story. It gives *Lethal Weapon* and *Braveheart* a genuine editorial role and lets the later data overturn the assumption that Gibson simply stopped working.

**Risk / weakness:** IMDb ratings are title-level audience ratings, not measures of Gibson's performance. Credit volume is not commercial scale. The 2020s comparison covers six years (2020–25), not a full decade.

### 2. More films. Less centre stage.

**Core argument:** The 2020–25 acting run contains more eligible films than the 1990s, but lower title ratings and fewer first-position principal credits.

**Why it works:** This is the cleanest contradiction in the data.

**Risk / weakness:** Principal ordering is useful context but not a formal billing or screen-time metric, so it should not carry the headline alone.

### 3. The director became the second career.

**Core argument:** Six directing features across 32 years include *Braveheart*, *Apocalypto* and *Hacksaw Ridge*, with gaps as long as 10 years.

**Why it works:** It directly answers "where did he take the career?" and gives the article a strong final act.

**Risk / weakness:** Six films are a sequence, not enough observations for broad causal or trend claims.

## Recommended story route

**He didn't disappear. He changed jobs, then came back differently.**

The personal hook remains the same: Martin Riggs is the movie star Adam remembers; *Braveheart* is the hinge. The data then adds the less obvious answer: after the long acting gap, Gibson eventually became prolific again, but in a much more uneven set of titles, while directing stayed rare and capable of producing major peaks.

## Recommended three-chart story

### Chart 1 — The peak is where memory puts it

- **Role:** Set the scene.
- **Story question:** Where do the strongest-rated eligible acting films sit across Gibson's career?
- **Chart type:** scatter timeline of all 58 eligible acting movies.
- **Data needed:** year, title, IMDb rating, votes, principal order.
- **Key stat:** *Lethal Weapon* 7.6; *Braveheart* 8.3. The 1980s median is 7.1 and the 1990s median 6.7, versus 5.6 for 2020–25.
- **Why this chart matters:** It validates the nostalgia rather than merely using it as decoration.
- **Potential issue / QA risk:** multiple films share years; labels should be limited to the two story anchors. A truncated rating axis is acceptable for scatter but must be clearly labelled.

### Chart 2 — He didn't stop acting. He got busier.

- **Role:** Build the tension.
- **Story question:** Did Gibson actually disappear from feature acting?
- **Chart type:** annual line of eligible acting-film counts, including explicit zero years.
- **Data needed:** year and eligible acting-film count.
- **Key stat:** the 2003→2010 release-year gap is the largest; 2020–25 contains 16 eligible acting films versus 13 in the 1990s, with six in 2022 alone.
- **Why this chart matters:** This is the counter-intuitive reveal. The later career is not quiet in volume.
- **Potential issue / QA risk:** the 1,000-vote floor means this is a count of eligible analytical films, not every credit Gibson has ever had.

### Chart 3 — Directing became the second career

- **Role:** Land the aha moment.
- **Story question:** What happened when Gibson moved into directing?
- **Chart type:** six-point chronological scatter of directing features by IMDb rating.
- **Data needed:** year, title, rating, votes, years since previous directing release, Academy milestone.
- **Key stat:** six released features from 1993–2025; *Braveheart* 8.3, *Apocalypto* 7.9, *Hacksaw Ridge* 8.1; gaps of 9, 10 and 9 years separate later directing releases.
- **Why this chart matters:** It answers where the career went without pretending every later project was a success.
- **Potential issue / QA risk:** sparse sequence; labels must stay inside the square canvas and *Flight Risk* should remain visible as a counterexample.

## Next build step

Build the three derived chart datasets, create locked 538 configs, render them, then run `docs/chart_qa_checklist.md` before any publication package is created.
