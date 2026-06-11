# Project kickoff quick reference

Use this short prompt when you want ChatGPT to apply the full repo-aware operating model from `docs/project_kickoff_prompt.md` without pasting the full document.

For the common workflow where you have a blog idea and a dataset pointer, use `docs/project_kickoff_practical_reference.md`.

## Copy/paste prompt

```text
Please use the Project Kickoff Prompt in my GitHub repo:

adamgreen1708/chart-templates/docs/project_kickoff_prompt.md

Apply that operating model to this project.

Project idea:
[describe the data story / chart / dataset / cleanup task here]

My intended outcome:
[chart, dataset, blog post, social package, repo cleanup, etc.]

Please inspect the repo context first, suggest the best route, and proceed with the most efficient approach.
```

## Notes

Replace the square-bracket sections before sending.

Use this when you want the assistant to:

- inspect the repo first;
- suggest the best route;
- reduce manual copy/paste;
- find the story and present a 3-chart editorial plan before creating configs where appropriate;
- use GitHub branches and PRs where helpful;
- use real data only;
- update templates when reusable lessons appear;
- QA and verify before handback.
