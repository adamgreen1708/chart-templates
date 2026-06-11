# chart-templates

A repo for producing coffeetableviz data stories: datasets, chart configuration, rendering workflows, and archived project assets.

The repo now works as a small production system rather than a file dump. Active files should stay lean. Project-specific files should live with the project that created them.

## Active areas

- `src/` contains the reusable chart and rendering system.
- `.github/workflows/` contains active reusable workflows only.
- `docs/` contains prompts, operating rules, QA checklists, and process guidance.
- `output/` is for current rendered chart outputs.

## Archived project areas

Completed or project-specific files belong under:

```text
archive/projects/YYYY-MM-project-name/
```

Recommended subfolders:

```text
archive/projects/YYYY-MM-project-name/data/
archive/projects/YYYY-MM-project-name/scripts/
archive/projects/YYYY-MM-project-name/src/
archive/projects/YYYY-MM-project-name/workflows/
archive/projects/YYYY-MM-project-name/config/
archive/projects/YYYY-MM-project-name/output/
archive/projects/YYYY-MM-project-name/content/
```

## Core principle

Keep the active repo ready for the next chart. Move old project machinery into the archive once it has served its purpose.

## Key docs

- `docs/chatgpt_operating_model.md` — how ChatGPT should operate in this repo.
- `docs/project_lifecycle.md` — full data story workflow.
- `docs/repo_structure.md` — what belongs where.
- `docs/archive_policy.md` — when and how to archive.
- `docs/chart_qa_checklist.md` — quality checks before declaring a chart done.
- `docs/prompt_starter.md` — reusable prompt to start the automated workflow.
- `docs/project_manifest_template.md` — template for recording project assets.
- `docs/chart_config_prompt.txt` — locked CHART_CONFIG generation prompt.
