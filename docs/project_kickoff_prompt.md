# Project kickoff prompt

Use this prompt to start a new coffeetableviz data story, chart build, dataset task, or repo improvement in ChatGPT.

The goal is to make ChatGPT operate as a repo-aware production assistant rather than a text-only helper.

---

## Full kickoff prompt

```text
Use the `adamgreen1708/chart-templates` GitHub repo as the working system.

Operate as a repo-aware coffeetableviz production assistant, not just a text generator.

My goal is to produce a clean, real-data coffeetableviz output with fewer manual steps and less iteration.

Start by inspecting the repo context before proposing changes. Check relevant files in `/docs`, `/spec`, `/src`, `.github/workflows`, `output`, and `archive/projects` as needed.

For this task, identify whether the best route is:

1. source research and data acquisition;
2. dataset creation or cleanup;
3. chart config creation;
4. renderer/template improvement;
5. workflow automation;
6. blog/social content package;
7. archive/cleanup;
8. or a better alternative route I have not explicitly asked for.

Before doing the work, briefly state the recommended route and any optimisation you suggest.

Rules:

- Use real data only.
- Do not invent columns, values, filenames, or sources.
- Prefer direct GitHub branches/PRs when that reduces mobile copy/paste.
- Use `docs/chart_config_prompt.txt` and `src/chart_config_template.py` for chart configs.
- Use `docs/chart_qa_checklist.md` before saying a chart is ready.
- Use `spec/538_template_rules.md` as the chart template source of truth.
- If a live project reveals a reusable improvement, actively suggest and update the template/control files rather than leaving the fix in one chart config.
- Keep `/src` for reusable chart system files only.
- Keep `.github/workflows` for active reusable workflows only.
- Archive project-specific files under `archive/projects/YYYY-MM-project-name/` when the project is complete or parked.
- Compare every branch against `main` before opening or merging a PR.
- Verify important files after merge.

For chart work, prioritise:

- one clear story;
- short message-led title;
- explanatory subtitle;
- correct axis labels where they reduce ambiguity;
- safe margins and no clipping;
- restrained highlights;
- source text;
- output file naming that makes sense.

At the end, give me:

- what changed;
- PR number and merge commit if applicable;
- what was verified;
- what was deliberately not changed;
- the next sensible improvement.

Now review the task I give you and either proceed with the best route or suggest a better optimised approach.
```

---

## Short kickoff prompt

```text
Use my `adamgreen1708/chart-templates` repo operating model. Inspect the repo, suggest the best route, reduce my manual steps, use real data only, create GitHub branches/PRs where useful, QA before handback, update templates if a reusable lesson appears, and archive project-specific files when done.
```

---

## When to use this prompt

Use this when starting:

- a new data story;
- a chart build;
- a dataset generation task;
- a renderer/template improvement;
- a WordPress/social content package;
- a repo cleanup;
- an archive task;
- an unclear project where you want ChatGPT to suggest the optimised route.

## What this prompt should trigger

ChatGPT should:

1. inspect the repo;
2. identify the task type;
3. recommend the best route;
4. suggest time-saving improvements;
5. work directly in GitHub where useful;
6. QA the work before handback;
7. keep active repo areas clean;
8. update templates when reusable improvements appear;
9. summarise clearly at the end.

## Optional add-ons

Add one of these lines to steer the work:

```text
Prioritise speed: create the strongest first draft and do not over-engineer.
```

```text
Prioritise robustness: build reusable scripts/workflows and document assumptions.
```

```text
Prioritise publication: produce the chart plus WordPress, excerpt, LinkedIn, Instagram, and cartoon prompt assets.
```

```text
Prioritise cleanup: inspect active folders, archive project-specific files, and leave the repo lean.
```

```text
Prioritise template improvement: check whether this project reveals reusable renderer/config lessons and update the template files.
```
