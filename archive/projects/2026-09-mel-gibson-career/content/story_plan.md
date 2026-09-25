# Mel Gibson career pivot — provisional story discovery

## Status

This is the **pre-dataset editorial hypothesis**. It is based on current IMDb credit information, Academy records and contemporary Reuters reporting. The repo's official IMDb acquisition script must be run before any chart config is created.

## Strongest story options

### 1. Riggs made the star. Braveheart changed the job. — recommended

**Core argument:** The nostalgia version of Mel Gibson is the actor — *Mad Max*, Martin Riggs, *Braveheart*. But *Braveheart* is also the hinge where his career becomes two careers. The later story is not simply "the leading man faded"; directing becomes a sparse but repeatedly consequential second lane.

**Why it works:** It starts exactly where the personal hook is — *Lethal Weapon* and *Braveheart* — then answers "where did he go?" with a measurable change in credit type rather than gossip or a subjective rise/fall narrative.

**Data required:** Full principal-acting movie chronology, directing chronology, IMDb rating, vote count, year, role lane; Academy milestones as annotations.

**Risk / weakness:** The full acting-output break and era averages must be validated from the downloadable IMDb data. Public controversies are context, not a causal variable.

### 2. Two careers, different peaks

**Core argument:** Gibson's acting career generated the scale and familiarity; his much smaller directing filmography produced the clearest awards milestones.

**Why it works:** Six released feature directing credits can be compared with the much larger acting set without pretending they are the same kind of work.

**Data required:** Actor/director title counts, ratings, awards and optionally inflation-safe box-office context.

**Risk / weakness:** Directing has a tiny sample. Average-rating comparisons could overstate a six-film sequence.

### 3. The career went quiet, then the director returned

**Core argument:** A visible gap in mainstream acting/directing work after the mid-2000s is followed by *Hacksaw Ridge* in 2016, which returned Gibson to the Academy's Directing nominees.

**Why it works:** It gives the post-*Braveheart* question a clean second act.

**Data required:** Year-by-year acting/directing credits plus sourced timeline events.

**Risk / weakness:** It is easy to turn chronology into a causal story about his 2006 conduct. The article should state the documented industry context while keeping the chart claim to "what happened when".

## Recommended story route

**Riggs made the star. Braveheart changed the job.**

The most interesting answer is not that Mel Gibson disappeared. It is that his career changed shape: from a high-volume, highly visible acting run into a two-lane career where directing was infrequent but carried disproportionate cultural and awards weight.

The downloadable IMDb data should now test that claim rather than merely illustrate it.

## Recommended three-chart story

### Chart 1 — Riggs made the movie star

- **Role:** Set the scene.
- **Story question:** What does Gibson's eligible acting-film timeline look like from *Mad Max* through the 2020s?
- **Chart type:** scatter/timeline of eligible acting movies, year vs IMDb rating.
- **Data needed:** year, title, rating, votes, acted flag.
- **Key stat:** To be calculated after acquisition.
- **Editorial anchors:** *Lethal Weapon* (1987) and *Braveheart* (1995), with only a small number of other labels.
- **Why this matters:** Shows the dense star period before we introduce the second career lane.
- **QA risk:** Over-labelling; treating IMDb title ratings as performance scores; titles with low vote counts.

### Chart 2 — Then the job changed

- **Role:** Build the tension.
- **Story question:** How did the mix of acting and directing credits change over time?
- **Chart type:** five-year-period comparison of eligible acting titles and directed features, or a role-lane timeline if period counts hide too much.
- **Data needed:** year, acted, directed, career_lane.
- **Key stat:** To be calculated after acquisition — especially the acting-output gap/decline and directing gaps.
- **Why this matters:** This is the actual answer to "where did he take his career?" rather than a greatest-hits chart.
- **Context annotation:** A sourced 2006 marker may be included in the article/timeline, but not as a causal divider unless the evidence supports that wording.
- **QA risk:** Acting and directing counts are different kinds of credits; labels must make that explicit.

### Chart 3 — The awards came back behind the camera

- **Role:** Land the aha moment.
- **Story question:** What happened across Gibson's released feature films as director?
- **Chart type:** chronological dot plot of directed feature films and IMDb rating, with Academy annotations.
- **Data needed:** year, title, rating, votes, directed flag; Academy milestones.
- **Verified anchors:** *Braveheart* won Gibson the Directing Oscar in 1996; *Hacksaw Ridge* brought another Directing nomination in 2017.
- **Why this matters:** The directing lane is small, but it explains why the later career cannot be summarised as a simple fade-out.
- **QA risk:** Six released feature films is a small sequence, not a population; do not imply a trend from sparse points.

## Feature-art seed — not for generation yet

If this route survives the dataset pass, the story-specific visual metaphor should be **a film clapperboard splitting into two paths: one path becomes an action-film silhouette / police badge echoing the acting-star era, the other becomes a director's chair / camera viewfinder**. A single muted-red hinge at the split represents *Braveheart* as the pivot.

This is deliberately more specific than generic medieval/action imagery. Final feature art should only be generated after the chart sequence is approved, using the repo's feature-image rules.

## Next build step

Run `scripts/build_imdb_actor_director_dataset.py`, inspect the clean and audit datasets, calculate the exact era statistics, then confirm or revise the three-chart route. Only after that should configs be created.
