# coffeetableviz repo-aware production flow

This document shows the standard process for running a coffeetableviz data story through the `adamgreen1708/chart-templates` repo-aware workflow.

It is designed for ChatGPT-assisted production, where the assistant should inspect the repo, suggest better approaches, reduce manual copy/paste, create/update files where useful, QA outputs, and archive project-specific assets.

## Process flow diagram

```mermaid
flowchart TD
    A[Start: idea, dataset, chart request, or cleanup request] --> B{Is the request clear enough to act?}

    B -->|Yes| C[Inspect repo context]
    B -->|No| B1[Make best effort from available context]
    B1 --> C

    C --> C1[Check active files, docs, templates, archive, current config, workflows]
    C1 --> D{What type of task is this?}

    D -->|New data story| E[Frame story and source needs]
    D -->|Dataset task| F[Create or validate dataset]
    D -->|Chart task| G0{Is this blog/data-story work?}
    D -->|Renderer/template issue| H[Assess reusable system change]
    D -->|Blog/social package| I[Create publication assets]
    D -->|Cleanup/archive| J[Classify active vs project-specific files]

    E --> E1[Define project slug]
    E1 --> E2[Identify source, audience, hook, likely chart angle]
    E2 --> F

    F --> F1[Use real data only]
    F1 --> F2[Check rows, columns, types, missing values, units, dates]
    F2 --> F3{Script or workflow needed?}
    F3 -->|Yes| F4[Create repo script/workflow on branch]
    F3 -->|No| S0[Run story discovery]
    F4 --> S0

    G0 -->|Yes| S0
    G0 -->|No: config-only task| G[Inspect data and create/update CHART_CONFIG]

    S0 --> S1[Scan for ranking, outlier, trend, comparison, concentration, gap, shift, relationship]
    S1 --> S2[Present strongest story options]
    S2 --> S3[Recommend 3-chart editorial plan]
    S3 --> S4{Story route clear?}
    S4 -->|No| S5[Ask Adam to choose or refine route]
    S5 --> S4
    S4 -->|Yes| S6[Create derived datasets needed for chosen charts]
    S6 --> G

    G --> G1[Use docs/chart_config_prompt.txt and src/chart_config_template.py]
    G1 --> G2[Set x_col, y_col, labels, axis ranges, highlights, annotations]
    G2 --> G3[Apply chart QA checklist]
    G3 --> K{Reusable lesson found?}

    H --> H1[Compare renderer, spec, config template, prompt, tests]
    H1 --> H2[Patch template/control files if needed]
    H2 --> K

    K -->|Yes| K1[Update spec, config template, prompt, tests]
    K -->|No| L[Create branch and commit focused changes]
    K1 --> L

    I --> I1[Create WordPress, excerpt, LinkedIn, Instagram, cartoon scene, image prompt]
    I1 --> L

    J --> J1[Map files to archive/projects/YYYY-MM-project-name]
    J1 --> J2[Prefer move/rename with no content changes]
    J2 --> L

    L --> M[Compare branch against main]
    M --> N{Diff matches intent?}
    N -->|No| N1[Fix branch before PR]
    N1 --> M
    N -->|Yes| O[Open PR]

    O --> P{Safe to merge?}
    P -->|No| P1[Explain blocker or leave PR open]
    P -->|Yes| Q[Merge PR]

    Q --> R[Verify key files on main]
    R --> T[Summarise changes, checks, and next sensible improvement]
```

## Operating principles

1. Inspect before changing files.
2. Use real data only.
3. Prefer direct GitHub file work when it saves Adam manual effort.
4. Keep active repo areas lean.
5. Do not leave reusable fixes trapped in one project config.
6. Do not jump from dataset inspection straight to chart config for blog/data-story work.
7. Present the strongest story route and 3-chart editorial plan before building configs.
8. Compare before PR and merge.
9. Verify after merge.
10. End with a clear summary and next suggested improvement.

## Key decision points

### Is this a one-off project change or a reusable improvement?

If the change improves only one chart, keep it in that chart config.

If it improves future charts, update the relevant template/control files:

- `spec/538_template_rules.md`
- `src/chart_config_template.py`
- `docs/chart_config_prompt.txt`
- `tests/test_538_rules.py`
- `AGENTS.md` if agent behaviour changes

### Does this need story discovery before config?

For blog/data-story work, yes.

Use `docs/story_discovery_and_3_chart_flow.md` before creating configs. The assistant should inspect the dataset, find the story, present the strongest options, recommend a 3-chart editorial plan, and only then build derived datasets and chart configs.

For a narrow config-only request, the assistant can proceed straight to `CHART_CONFIG` creation after inspecting the dataset.

### Does this belong in the active repo or archive?

Active repo:

- reusable renderer files;
- active chart config;
- active reusable workflows;
- process and template docs.

Archive:

- completed project data;
- one-off project scripts;
- one-off workflows;
- final outputs;
- blog/social project assets.

### What should ChatGPT hand back?

At the end of a repo task, ChatGPT should report:

- PR number and title;
- merge commit if merged;
- files changed;
- what was deliberately left untouched;
- checks performed;
- next sensible improvement.
