# Bauhaus Art Studio — live GitHub CSV dataset browser QA

**Status:** Proposed, review-only branch. Do not merge without explicit approval.

## User issue
On iPhone, **Choose a repository dataset** was a fixed two-option list (Daily visits and David Bowie). Other CSV files in the repository never appeared, even though pasting a GitHub CSV link worked.

## Implementation
- Replace the hard-coded options with live public GitHub REST API discovery. **GitHub account** defaults to `adamgreen1708`, but can be changed to another public account such as `shortsinsports`.
- Load up to 1,000 public repositories via `/users/{owner}/repos` (paginated), then fetch the selected repository’s default-branch recursive tree via `/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1`.
- List every `.csv` blob path, including nested `archive/` and `data/` folders. Keep all paths searchable; show up to **120 matching entries** in the native iPhone dropdown at once and disclose when the search narrows the list.
- The Load button uses the actual selected repository/branch/path. No other owner or file is silently substituted. Existing Daily visits and Bowie preferred column mappings are retained.
- A manual public GitHub link continues to work (including a full 40-character pinned commit SHA). Support single-segment branch names such as `main` and `master`; permit normal Unicode and spaces in CSV filenames, while rejecting path traversal and non-CSV files.
- No authentication token, private-repository access, backend, or proxy. Friendly messages for GitHub API rate limits, oversized/truncated trees, empty repositories and timeouts. The manual link remains usable if discovery is unavailable.
- Load the browser only when entering Data Art or opening a direct data example, reducing unnecessary GitHub API traffic.
- Add mobile-safe wrapping for the imported filename and GitHub panel.

## Checks run against production functions
`scripts/test_bauhaus_public_csv.js` — **passed** with an isolated runtime simulation:
- External and Coffeetableviz GitHub URL parsing
- Pinned SHA, `main` and alternate branch refs
- Rejection of invalid URLs/encoded path separators
- Marathon `H:MM:SS` numeric conversion and existing Bowie duration formatting

`scripts/test_bauhaus_github_browser.js` — **passed** with mocked GitHub responses and DOM:
- Multiple repository discovery and default chart-templates selection
- Four CSV files discovered within a tree, including nested and Unicode names; non-CSV files excluded
- Search filtering, selection and Load enabled state
- Switching repositories clears old file selections
- Refresh preserves the selected repository
- Changing public GitHub owner to `shortsinsports` exposes its `Data` repository and marathon CSV fixture
- Explicit truncated tree error and rate-limit fallback
- Production inline JavaScript compiles

## Browser QA required before merge
1. Open the branch preview for `/resources/bauhaus-art-studio/` on **iPhone Safari** and desktop.
2. Select Data Art. Confirm **GitHub account = adamgreen1708**, chart-templates defaults, and the dataset list contains more than two CSVs.
3. Search for `bowie`, choose a CSV, load, select a metric and Create; check no old poster remains under mismatched controls.
4. Change the GitHub account to `shortsinsports`; choose `Data`, then `SIS-marathon_major_winners_2000_2026.csv`. Confirm **Race / Time** defaults and `2:09:45` appears as elapsed time, not 7,785 in displayed text.
5. Confirm the original full commit permalink also loads via the manual URL field.
6. Inspect long filenames and panel messages on iPhone: no horizontal clipping. Export PNG and check chart labels, source attribution and safe margins.
7. Check a GitHub API error or throttling displays a meaningful fallback instead of presenting empty or fake data.

**Limitation:** The browser shows public default-branch CSVs only, not private files or historic snapshots. Historic commits can still be loaded by pasting a permalink. An actual live iPhone/browser pixel-level QA run has **not** been completed in this branch.
