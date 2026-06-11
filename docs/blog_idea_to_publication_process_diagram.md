# Blog idea to publication process diagram

Use this diagram as the simple interaction model for starting a new coffeetableviz data story.

The key rule is: do not jump straight from dataset to chart config. Find the story first.

## Process diagram

```mermaid
flowchart TD
    A[Adam has a blog idea] --> B[Adam provides three inputs]

    B --> B1[Blog idea / rough angle]
    B --> B2[Dataset pointer]
    B --> B3[Intended outcome]

    B1 --> C[ChatGPT applies Project Kickoff Prompt]
    B2 --> C
    B3 --> C

    C --> D[Inspect repo context]
    D --> D1[Check docs, specs, templates, renderer, workflows, archive]

    D1 --> E[Inspect or retrieve dataset]
    E --> E1[Check source, rows, columns, types, missing values, units, dates]

    E1 --> F[Find the story]
    F --> F1[Scan for rankings, outliers, trends, gaps, shifts, concentration, relationships]
    F1 --> F2[Identify strongest editorial route]

    F2 --> G[Present 3-chart editorial plan]
    G --> G1[Chart 1: set the scene]
    G --> G2[Chart 2: build the tension]
    G --> G3[Chart 3: land the aha moment]

    G1 --> H{Adam approves or tweaks?}
    G2 --> H
    G3 --> H

    H -->|Tweak| G
    H -->|Approve / obvious route| I[Build derived datasets]

    I --> J[Create chart configs]
    J --> J1[Use chart_config_prompt and chart_config_template]

    J1 --> K[Render and QA]
    K --> K1[Check title, subtitle, axes, labels, margins, highlights, source]

    K1 --> L{Reusable lesson found?}
    L -->|Yes| L1[Update template / prompt / spec]
    L -->|No| M[Create publication package]
    L1 --> M

    M --> M1[WordPress post]
    M --> M2[Excerpt]
    M --> M3[LinkedIn post]
    M --> M4[Instagram copy]
    M --> M5[Cartoon scene and image prompt]

    M1 --> N[Archive or park project files]
    M2 --> N
    M3 --> N
    M4 --> N
    M5 --> N

    N --> O[Final handback]
    O --> O1[What changed]
    O --> O2[PR / merge commit]
    O --> O3[What was verified]
    O --> O4[Next sensible improvement]
```

## Simple prompt to start

```text
Use my Project Kickoff Prompt.

Blog idea:
[my rough idea / hunch]

Dataset:
[paste link, repo path, upload name, CSV source, Kaggle/OWID link]

Intended outcome:
[3-chart story only / chart configs / full blog package]
```

## Expected first response

```text
Recommended story route:
[best editorial angle]

Why this is the strongest route:
[short explanation grounded in the data]

3-chart story:
1. [Chart 1] — set the scene
2. [Chart 2] — build the tension
3. [Chart 3] — land the aha moment

Next build step:
[derived dataset / config / render / content package]
```

## Mental model

```text
Idea + dataset
-> inspect
-> find the story
-> present 3-chart plan
-> build charts
-> write post
-> publish package
-> archive
```
