# IMDb actor project kickoff prompt

Use this after the standard project kickoff prompt when the subject is an actor's film work.

```text
Kick off a new coffeetableviz chart project about [ACTOR NAME] using the current chart-templates repository and its documented project workflow.

Acquire the data directly from IMDb's official non-commercial datasets at https://datasets.imdbws.com/. Do not ask me to download or upload the source files unless direct access fails after retrying. Stream and filter large gzip files instead of saving the complete global datasets in the repository.

Identity and joins
1. Resolve [ACTOR NAME] in name.basics.tsv.gz and verify the exact nconst. Do not guess. If the name is ambiguous, show the candidates and stop for confirmation.
2. Filter title.principals.tsv.gz to that nconst.
3. Join matching tconst values to title.basics.tsv.gz for title, type, year, runtime and genres.
4. Join title.ratings.tsv.gz for averageRating and numVotes.
5. Join title.crew.tsv.gz, then resolve director nconst values through name.basics.tsv.gz.
6. Use title.akas.tsv.gz only when regional or alternative titles matter. Use title.episode.tsv.gz only when television episodes are explicitly in scope.

Default analytical scope
- principal actor/actress credits
- titleType=movie
- released titles with a year and rating
- apply and disclose a sensible minimum-vote floor before drawing conclusions
- preserve all excluded, unrated and unreleased records in an audit file

Outputs and validation
- Create one clean joined CSV, one exclusions/audit CSV, reproducible acquisition/build code, and source metadata containing URLs, access time and each file's upstream run date.
- Validate the resolved person ID, row counts at every stage, duplicate tconst values, missing years/runtimes/ratings, vote coverage and join coverage.
- Make clear that title.principals is a principal-credit subset, not a guaranteed complete filmography, and that IMDb ratings describe titles, not the actor's individual performance or critical acclaim.
- Inspect the dataset before choosing charts. Rank 3–5 defensible story angles, state sample-size and selection risks, and recommend a connected three-chart narrative. Stop for approval before writing chart configs unless I explicitly ask you to continue through rendering.

Brand and delivery
- Use only the current coffeetableviz palette: background #F3F4F6, focus blue #1F8FA8, highlight red #C44E52, context grey #D9D9D9, secondary grey #7A7A7A, text #111111 and supporting text #555555.
- Do not introduce, reinterpret or substitute colours.
- Use the repository's locked renderer and chart rules.
- Work on a new branch and open a draft pull request so I can review it easily on mobile.
```

## Short launcher

```text
Use the IMDb actor project prompt for [ACTOR NAME]. Resolve the identity first, stream-filter and join the official IMDb datasets, create the reproducible joined dataset and audit trail, then rank story angles and recommend a three-chart plan before configs. Keep the current coffeetableviz palette unchanged and deliver through a draft PR.
```
