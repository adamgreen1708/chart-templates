# Project lifecycle

This is the standard lifecycle for a coffeetableviz data story in this repo.

## 1. Idea and story framing

Define:

- topic;
- audience;
- likely hook;
- data source;
- strongest possible chart angle;
- whether the output is a blog post, social post, chart pack, or experiment.

ChatGPT should suggest whether the idea needs fresh web research, existing repo data, a new dataset, or a chart-only config.

## 2. Project setup

Choose a project slug:

```text
YYYY-MM-project-name
```

Create or plan the folders:

```text
archive/projects/YYYY-MM-project-name/data/
archive/projects/YYYY-MM-project-name/scripts/
archive/projects/YYYY-MM-project-name/config/
archive/projects/YYYY-MM-project-name/output/
archive/projects/YYYY-MM-project-name/content/
```

For active work, files can temporarily live in active paths only when required by the renderer or workflow.

## 3. Dataset creation and inspection

Use real data only.

Check:

- source credibility;
- row count;
- column names;
- data types;
- missing values;
- duplicates;
- units;
- date handling;
- derived fields.

If a script is needed, create it in the repo rather than requiring Adam to copy/paste from chat.

## 4. Story discovery and 3-chart planning

Before creating chart configs for a blog/data story, run the story discovery step in `docs/story_discovery_and_3_chart_flow.md`.

The default path is:

```text
dataset -> story discovery -> 3-chart editorial plan -> derived datasets -> chart configs
```

Scan the inspected dataset for:

- ranking;
- outlier;
- trend;
- comparison;
- concentration;
- gap;
- shift;
- relationship;
- surprising absence;
- misleading first impression;
- strongest single takeaway.

Then present a recommended 3-chart story:

| Chart | Role | Purpose |
|---|---|---|
| Chart 1 | Set the scene | Establish the broad pattern or starting point. |
| Chart 2 | Build the tension | Reveal the shift, gap, concentration, outlier, contradiction, or breakdown. |
| Chart 3 | Land the aha moment | Deliver the clearest takeaway the post should leave behind. |

For each chart, present:

```text
Chart title:
Story question:
Chart type:
Data needed:
Key stat:
Why this chart matters:
Potential issue / QA risk:
```

Only move to chart configs after the editorial route is clear or strongly recommended.

## 5. Chart config

Use `docs/chart_config_prompt.txt` as the locked config generation guide.

Before creating or updating a config, inspect the dataset columns and match names exactly.

Do not treat `CHART_CONFIG` creation as the first analytical step for blog/data-story work.

## 6. Render and QA

Use the active render workflow or renderer.

Check:

- chart output path;
- title and subtitle fit;
- labels stay inside safe margins;
- axes are readable;
- highlights match the story;
- no mock data;
- source text is present;
- chart has one clear message.

Use `docs/chart_qa_checklist.md` before asking Adam to review.

## 7. Content package

When a chart is close to final, suggest the publication package:

- WordPress Gutenberg blog post;
- blog excerpt;
- LinkedIn post;
- Instagram caption;
- cartoon scene text;
- locked stencil-style image prompt;
- project manifest update.

## 8. Archive

When the project is finished or the files are no longer active:

- move project data, scripts, workflows, configs, and content into the archive project folder;
- preserve file contents exactly;
- compare the branch and confirm expected renames/moves;
- leave reusable renderer files and active workflows in place.

## 9. Closeout

Every completed project should have a `project_manifest.md` capturing:

- source links;
- data files;
- scripts;
- config files;
- output files;
- content files;
- key decisions;
- final status.
