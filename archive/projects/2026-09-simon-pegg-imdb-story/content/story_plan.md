# Simon Pegg IMDb story plan

## Dataset read

- Verified person: Simon Pegg, IMDb `nm0670408` — the only exact-name match in the source snapshot.
- Scope: IMDb principal actor/actress credits with `titleType=movie`, a release year, a rating and at least 1,000 votes.
- Analytical set: 33 movies released from 2004 to 2025; mean rating 6.58 and median 6.8.
- All 33 analytical rows have a year, runtime and rating; there are no duplicate `tconst` values.
- The audit CSV retains non-acting principal categories, non-movie acting credits, unrated or unreleased movies and titles below the vote floor.

The 1,000-vote threshold removes extremely thin ratings while retaining smaller releases. It is a coverage rule, not a claim that 1,000 votes makes unlike films directly comparable.

IMDb `title.principals` is a principal-credit subset, not a guaranteed complete filmography. IMDb ratings describe each title, not Simon Pegg's individual performance or critical acclaim.

## Ranked story angles

### 1. His highest-rated titles keep coming from three familiar teams

The 12 eligible films in three mutually exclusive, reproducible groups — six *Mission: Impossible* films, three *Star Trek* films and three films directed by Edgar Wright — average between 7.35 and 7.53. The other 21 eligible films average 6.09. Those 12 films also account for 5.41 million of the analytical set's 7.06 million votes (76.6%).

Why it leads: it links the cult-comedy breakthrough to the large ensemble franchises that followed, while showing every eligible title rather than selecting isolated favourites.

Risk: the grouping was found during exploration and mixes one director relationship with two franchises. The chart must define the groups plainly, show every film and avoid implying that Pegg caused the ratings.

### 2. Edgar Wright remains the high-water collaboration

*Shaun of the Dead* and *Hot Fuzz* are both rated 7.8; *The World's End* is 6.9. The three-film mean is 7.50, level with the strongest franchise groupings.

Why it works: it is human, recognisable and central to Pegg's screen identity.

Risk: three titles are too few for a sweeping director-effect claim, and the result partly overlaps the stronger first angle.

### 3. Mission: Impossible became the durable second act

Across six eligible films from 2006 to 2025, the series averages 7.35 and ranges from 6.9 to 7.7. Pegg's IMDb principal ordering moves from ninth in his first appearance to third or fourth in the five later films.

Why it works: it combines longevity, consistently strong title ratings and a visible change in billing prominence.

Risk: IMDb principal ordering is not a formal billing or screen-time measure, so the wording must remain careful.

### 4. Star Trek started highest, then stepped down

The three eligible films move from 7.9 to 7.7 to 7.0.

Why it works: it is the cleanest directional franchise pattern in the data.

Risk: three films make this a sequence, not a trend, and the chart is too narrow to carry the whole post.

### 5. The recent standalone run is the rough patch

Several eligible non-franchise titles from 2018 onwards sit below 6.0, including *Slaughterhouse Rulez*, *Terminal*, *Lost Transmissions*, *Inheritance* and *Nandor Fodor and the Talking Mongoose*.

Why it is weaker: release scale and audience selection vary sharply, while the 1,000-vote floor still leaves large differences in vote count. A broad career-decline claim would overreach.

## Recommended three-chart narrative

### Chart 1 — The peaks keep familiar company

- Role: Set the scene.
- Story question: Where do the strongest-rated eligible films sit across Pegg's movie timeline?
- Chart type: timeline dot plot of all 33 titles.
- Data needed: year, rating, title, votes and partnership group.
- Key stat: 11 of the 12 partnership films are rated 6.9 or higher; the three group means are all above 7.3.
- Why this matters: the recurring names emerge visually before the comparison is stated.
- QA risk: multiple films share years; label only the editorially necessary points and disclose the 1,000-vote floor.

### Chart 2 — Familiar teams rate a point higher

- Role: Build the tension and quantify the split.
- Story question: How do the three recurring partnerships compare with the rest of the eligible movies?
- Chart type: four-group mean dot plot; sample sizes are built into the labels, while charts 1 and 3 retain the individual-film detail.
- Data needed: group, title, rating, votes and sample size.
- Key stat: *Star Trek* 7.53, Edgar Wright 7.50 and *Mission: Impossible* 7.35, versus 6.09 for the other 21 films.
- Why this matters: it is the strongest defensible pattern in the dataset.
- QA risk: keep the groups mutually exclusive, show `n`, and state plainly that two groups contain only three films.

### Chart 3 — Mission: Impossible is the long game

- Role: Land the aha moment through the most durable partnership.
- Story question: How did the three familiar teams unfold film by film?
- Chart type: small-multiple connected dots ordered by release within each group.
- Data needed: partnership group, sequence, year, title, rating and principal order.
- Key stat: six *Mission: Impossible* titles average 7.35 across 19 years; the four most recent sit between 7.1 and 7.7.
- Why this matters: it turns the grouped result into a career story — cult-comedy roots followed by a long, consistently well-rated franchise run.
- QA risk: each line is a finite film sequence, not a continuous trend; ordering annotations must not be described as screen time.

## Brand lock

Use only:

- background `#F3F4F6`
- focus blue `#1F8FA8`
- highlight red `#C44E52`
- context grey `#D9D9D9`
- secondary grey `#7A7A7A`
- text `#111111`
- supporting text `#555555`

No colours may be introduced, reinterpreted or substituted.

## Approval gate

No chart-specific datasets, chart configs, renders or publication copy have been created. Adam's approval of the editorial route is required before that work starts.
