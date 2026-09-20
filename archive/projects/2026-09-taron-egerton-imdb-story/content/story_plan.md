# Taron Egerton IMDb story plan

## Dataset read

- Verified person: Taron Egerton, IMDb `nm5473782`.
- Source snapshot: `name.basics`, `title.principals` and `title.basics` run 20 September 2026; `title.ratings` and `title.crew` run 19 September 2026.
- Scope found: 226 principal-credit rows, of which 95 use the actor category. Twenty-one are movie-type records.
- Analytical set: 14 released, rated movies with at least 1,000 votes.
- Audit set: 74 non-movie actor credits, four rated movies below 1,000 votes and three movie records without a year or rating.
- Across the 14-film analytical set, the mean rating is 6.79 and the median is 7.0.

IMDb ratings measure the title, not Egerton's individual performance. `title.principals` is also a principal-credit subset rather than a guaranteed complete filmography.

## Ranked story angles

### 1. Real people are his strongest top-billed lane

The three Biography-tagged films where Egerton is first in IMDb principal ordering are remarkably consistent: *Eddie the Eagle* 7.3, *Rocketman* 7.3 and *Tetris* 7.4. Their 7.33 mean is 1.13 points above the 6.2 mean for first-ordered Action-tagged films: *Kingsman: The Golden Circle* 6.7, *Robin Hood* 5.4 and *Carry-On* 6.5.

Why it leads: the comparison follows a reproducible rule instead of hand-picking favourites, and it creates a clear career claim without pretending to rate the performances themselves.

Risk: only three titles sit in each comparison group. Show every film and the group mean.

### 2. The breakout remains the high-water mark

*Kingsman: The Secret Service* is the highest-rated eligible film at 7.7 and the most-voted at 784,718. Nothing in the later eligible set exceeds it, although *Tetris* comes closest at 7.4.

Why it works: instantly recognisable and simple to show on a career timeline.

Risk: this is a title-level audience rating, not a measure of career importance or performance quality.

### 3. His two franchises moved in opposite directions

The second *Kingsman* falls from 7.7 to 6.7, while *Sing 2* rises from 7.1 to 7.3.

Why it works: a compact, memorable final comparison.

Risk: each franchise has only two eligible observations, so this is a paired comparison rather than a trend.

### 4. The 2018 trough split the career

The eligible 2014–17 titles average 7.15. The eligible 2018–26 titles average 6.51, pulled down by *Billionaire Boys Club* and *Robin Hood* before a rebound through *Rocketman*, *Sing 2* and *Tetris*.

Why it is secondary: the period boundary is visually obvious, but the later period is a mixed set and the small sample makes a broad decline claim too strong.

## Recommended three-chart narrative

### Chart 1 — Kingsman set the early ceiling

- Role: Establish the career shape.
- Question: How have IMDb title ratings moved across Egerton's released movie credits?
- Chart: Timeline scatter plot of all 14 eligible titles.
- Key statistic: *Kingsman: The Secret Service* leads at 7.7 and 784,718 votes.
- Visual treatment: context grey for most films; current blue for the three first-ordered Biography films; current red only for the key breakout annotation.
- QA: label selectively, disclose the 1,000-vote floor and avoid implying a continuous yearly series.

### Chart 2 — Real people are his strongest lead roles

- Role: Explain the most defensible pattern.
- Question: How do his first-ordered Biography films compare with his first-ordered Action films?
- Chart: Two-group dot plot showing all six titles plus a mean marker.
- Key statistic: 7.33 versus 6.20, a 1.13-point gap.
- Visual treatment: current blue for Biography, context grey for Action and current red for the gap annotation only.
- QA: retain individual dots and group sizes so the chart cannot hide the small samples.

### Chart 3 — Two sequels, opposite directions

- Role: Finish with the recognisable franchise contrast.
- Question: Did the second eligible film improve on the first?
- Chart: Two paired slopes, one for *Kingsman* and one for *Sing*.
- Key statistic: *Kingsman* −1.0; *Sing* +0.2.
- Visual treatment: current red for the fall, current blue for the rise and no additional colours.
- QA: describe this as two pairs, not two long-running trends.

## Palette lock

Use the current coffeetableviz house palette only:

- background `#F3F4F6`
- focus blue `#1F8FA8`
- highlight red `#C44E52`
- context grey `#D9D9D9`
- secondary grey `#7A7A7A`
- text `#111111`
- supporting text `#555555`

No palette changes are authorised.
