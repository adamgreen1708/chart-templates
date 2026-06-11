# Archive policy

The goal of archiving is to keep the active repo lean while preserving project work clearly.

## Archive when

Archive files when:

- the project is complete;
- the dataset has already been generated;
- the script or workflow is project-specific;
- the file is no longer needed for active rendering;
- the active root is becoming cluttered.

## Do not archive when

Do not archive files when they are part of the reusable chart system:

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

Do not archive current work-in-progress files unless the user asks or the project is being formally parked.

## Archive location

Use:

```text
archive/projects/YYYY-MM-project-name/
```

Recommended mapping:

```text
data files        -> archive/projects/.../data/
scripts           -> archive/projects/.../scripts/
project src files -> archive/projects/.../src/
workflows         -> archive/projects/.../workflows/
chart configs     -> archive/projects/.../config/
outputs           -> archive/projects/.../output/
blog/social text  -> archive/projects/.../content/
```

## Safe archive process

1. Inventory files.
2. Classify files as core, active, or project-specific.
3. Map each project-specific file to the correct project archive folder.
4. Create an archive branch.
5. Move files without changing content.
6. Compare branch with `main`.
7. Confirm GitHub reports renames/moves with zero content changes when possible.
8. Open a PR with a clear summary.
9. Merge only if the diff matches the intended cleanup.
10. Verify key archived files and key active files after merge.

## PR summary should include

- source paths moved;
- destination folders;
- files deliberately left active;
- changed file count;
- whether content was unchanged;
- verification after merge.
