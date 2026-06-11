# Story discovery and 3-chart flow

This is the standard editorial step between receiving a dataset and creating chart configs.

The assistant should not normally jump straight from dataset inspection to `CHART_CONFIG` generation. The default process is:

```text
dataset -> story discovery -> 3-chart editorial plan -> derived datasets -> chart configs -> render/QA -> content package
```

## Why this exists

A chart can be technically correct but still miss the story.

This step is designed to reduce wasted iteration by making the assistant find the strongest editorial route before creating configs or renderer outputs.

## Required sequence

### 1. Inspect the dataset

Check:

- source and credibility;
- row count;
- column names;
- data types;
- missing values;
- duplicates;
- units;
- date handling;
- obvious derived fields;
- whether the data supports the proposed blog idea.

### 2. Find the story

Scan for:

- rankings;
- outliers;
- trends;
- comparisons;
- concentration;
- gaps;
- shifts;
- relationships;
- surprising absences;
- misleading first impressions;
- strongest single takeaway.

The assistant should be willing to say when the original idea is weaker than another angle visible in the data.

### 3. Present the strongest story options

Before building configs, present the strongest possible routes.

Do not only describe chart types. Describe the editorial argument.

Useful format:

```text
Story option:
Core argument:
Why it works:
Data required:
Likely chart sequence:
Risk / weakness:
```

### 4. Present the recommended 3-chart story

Default to a 3-chart story unless the dataset or post clearly calls for fewer or more charts.

The 3-chart structure is:

| Chart | Role | Purpose |
|---|---|---|
| Chart 1 | Set the scene | Establish the broad pattern or starting point. |
| Chart 2 | Build the tension | Reveal the shift, gap, concentration, outlier, contradiction, or breakdown. |
| Chart 3 | Land the aha moment | Deliver the clearest takeaway the post should leave behind. |

For each proposed chart, provide:

```text
Chart title:
Story question:
Chart type:
Data needed:
Key stat:
Why this chart matters:
Potential issue / QA risk:
```

### 5. Ask for editorial direction only when useful

If the direction is obvious, proceed with the recommended route.

If there are multiple good routes, ask Adam to choose or state which route you recommend.

Do not ask for clarification when a reasonable best-effort route is available.

### 6. Build only after the story route is clear

Once the story route is selected or strongly recommended:

1. create the derived datasets needed for the chosen charts;
2. create or update chart configs;
3. render and QA outputs;
4. produce the blog/social/cartoon package;
5. archive project-specific files when complete or parked.

## Handback format before building

Use this concise format when presenting the plan:

```text
Recommended story route:
[one-sentence editorial argument]

Why this is the strongest route:
[short explanation grounded in the data]

3-chart story:
1. [Chart 1 title] — [role and key point]
2. [Chart 2 title] — [role and key point]
3. [Chart 3 title] — [role and key point]

Next build step:
[derived dataset / config / render / content package]
```

## Important rule

Do not treat `CHART_CONFIG` creation as the first analytical step.

For blog/data-story work, `CHART_CONFIG` creation comes after dataset inspection, story discovery, and the 3-chart editorial plan.
