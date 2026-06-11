# AGENTS.md

This repository contains locked chart template systems and a repo-aware coffeetableviz production workflow.

## 538 template rules

- The source of truth is `spec/538_template_rules.md`.
- Workflow guidance is in `spec/538_workflow.md`.
- CHART_CONFIG prompting rules are in `docs/chart_config_prompt.txt`.
- The reusable config template is `src/chart_config_template.py`.
- Implementation must follow the spec exactly.
- Do not introduce a white plot area.
- Preserve the square 8.0 x 8.0 production canvas unless explicitly changed.
- Preserve padding, title/subtitle spacing, and safe-margin rules.
- Only add vertical gridlines when explicitly requested or clearly useful.

## Development rules

- Prefer simple, reusable matplotlib code.
- Keep implementation modular.
- Do not change renderer behaviour for one project without considering whether the template/spec should also be updated.
- If a live project reveals a reusable lesson, actively suggest and update the template files.
- If implementation conflicts with spec, fix the drift in the same branch.

## Protected active files

Treat these as core system files:

```text
src/render_538.py
src/chart_config.py
src/chart_config_template.py
src/chart_538.py
src/chart_utils.py
src/chart_generator.py
.github/workflows/render-538.yml
.github/workflows/render-chart.yml
```

## Repo operating model

Use `docs/chatgpt_operating_model.md` for how ChatGPT should inspect, suggest, branch, PR, QA, and archive work in this repo.
