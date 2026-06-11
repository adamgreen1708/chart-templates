# Project kickoff practical reference

Use this when you have a blog idea and can point ChatGPT to a dataset.

You only need to provide three things:

1. the rough blog idea or angle;
2. the dataset location;
3. the intended output.

ChatGPT should then inspect the repo, inspect the dataset, find the story, present the recommended 3-chart editorial plan, and drive the production flow.

## Copy/paste prompt

```text
Please use the Project Kickoff Prompt in my GitHub repo:

adamgreen1708/chart-templates/docs/project_kickoff_prompt.md

Apply that operating model to this project.

Blog idea / rough angle:
[describe the data story or question here]

Dataset:
[paste GitHub path, source link, uploaded file name, Kaggle/OWID page, CSV location, or dataset pointer here]

My intended outcome:
[chart, dataset, WordPress blog post, LinkedIn post, Instagram copy, cartoon prompt, repo cleanup, etc.]

Please inspect the repo context first, inspect the dataset, find the strongest story, present the recommended 3-chart editorial plan, and then proceed with the most efficient build route.
```

## What should happen next

ChatGPT should:

1. inspect the repo context;
2. inspect or retrieve the dataset;
3. check source, rows, columns, data types, missing values, units, dates, and useful derived fields;
4. scan for rankings, outliers, trends, comparisons, concentration, gaps, shifts, relationships, surprising absences, and misleading first impressions;
5. present the strongest story route and recommended 3-chart editorial plan;
6. identify the best build route;
7. suggest any more efficient alternative;
8. create or update data/scripts/configs in GitHub where useful;
9. QA the chart/story before handback;
10. update templates if a reusable lesson appears;
11. produce the requested publication package;
12. archive project-specific files when complete or parked.

## Useful outcome examples

```text
My intended outcome:
One chart, WordPress blog post, excerpt, LinkedIn post, Instagram post, cartoon scene, and image prompt.
```

```text
My intended outcome:
A cleaned dataset and first-pass 3-chart story plan only.
```

```text
My intended outcome:
A cleaned dataset, recommended 3-chart story, and chart configs.
```

```text
My intended outcome:
A repo cleanup/archive pass for this completed project.
```
