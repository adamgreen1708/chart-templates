# Repo structure

This repo should stay clean enough that a new data story can start without hunting through old files.

## Active root

### `src/`

Reusable chart system only.

Current expected active files:

```text
src/chart_538.py
src/chart_utils.py
src/chart_config.py
src/chart_generator.py
src/chart_config_template.py
src/render_538.py
```

Project-specific source/build scripts should not remain in `src/` after the project is complete.

### `.github/workflows/`

Reusable active workflows only.

Current expected active workflows:

```text
.github/workflows/render-538.yml
.github/workflows/render-chart.yml
```

Project-specific dataset build workflows should be archived with their project.

### `docs/`

Operating model, prompt templates, QA checklists, and repo process guidance.

### `output/`

Current chart output location. Avoid using this as a permanent archive.

## Archive structure

Every project should use:

```text
archive/projects/YYYY-MM-project-name/
```

Recommended subfolders:

```text
data/       source and derived datasets
scripts/    one-off project scripts
src/        project-specific source/build files originally created under src
workflows/  project-specific workflows
config/     chart configs
output/     final chart images or exports
content/    blog, LinkedIn, Instagram, cartoon prompts, notes
```

## Naming rules

Use lowercase, readable, hyphenated project folders:

```text
2026-05-scotch-whisky-flavours
2026-05-arsenal-title-race
2026-04-global-fuel-prices
```

Use lowercase, underscore-separated data and script files:

```text
arsenal_vs_top10.csv
build_arsenal_story_datasets.py
```

## Avoid

- dumping finished project files into `/data`, `/scripts`, or `/src`;
- keeping one-off workflows active after a dataset is built;
- overwriting renderer files for one project unless it improves the reusable system;
- ambiguous filenames like `chart.csv`, `data.csv`, `final.csv`, or `test.py`.
