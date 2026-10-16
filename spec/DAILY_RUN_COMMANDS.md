# Daily Run Commands

These are the standard launch and publish prompts for the Coffeetableviz daily editorial series.

Use each series in a fresh or pinned ChatGPT conversation. Keep creation, review, approval, and publishing for a single edition in the same conversation.

GitHub is the source of truth for the current series specifications and publishing instructions. The prompts explicitly invoke `@GitHub` so the repository connection is surfaced in a fresh chat.

## Strict execution contract

This contract applies to every daily-series run and publish action.

- Re-read the current command, series specification, reference/source instructions and validator from `main` at the start of every run. Do not rely on memory, a previous turn, a prior render or an earlier copy of the prompt.
- Execute the repository steps as written. Do not silently substitute a weaker, approximate or assumed check for a required step.
- A QA flag may be set to `true` only when that exact check was actually completed on the current edition during the current run.
- If a required check cannot be performed because a tool, file, source or render is unavailable, fail that gate explicitly. Never claim that the edition passed QA.
- User approval is approval of the displayed edition; it does not retrospectively validate a skipped repository gate.
- When a specification requires inspection of the final render, inspect the actual final output pixels—not the rendering code, dimensions, bounding-box calculations or an earlier/intermediate image.
- If the final image contains clipping, overlap, collisions, unreadable text, unsafe margins or any other specified render failure, fix and rerender before presenting it for approval.

---

## Run Blockbuster

Run today’s Blockbuster using @GitHub.

Before doing anything else, read the current Blockbuster specification and any relevant publishing/validation instructions in my `adamgreen1708/chart-templates` GitHub repository. Treat the repository as the source of truth rather than relying on previous chat history or memory.

Create and QA today’s edition, then show me the finished image for approval. Do not publish anything to GitHub yet.

---

## Publish Blockbuster

OK to push using @GitHub.

Publish the exact Blockbuster edition I just approved to `adamgreen1708/chart-templates`, following the current repository publishing instructions. Do not regenerate or alter the approved image or copy. Create the required branch, commit and PR rather than merging directly to main, unless the repository instructions explicitly say otherwise.

---

## Run Data Lens

Run today’s Data Lens using @GitHub.

Before doing anything else, read the current Data Lens specification, `spec/series/data-lens-reference-sources.md`, and any relevant publishing/validation instructions in my `adamgreen1708/chart-templates` GitHub repository. Complete the reference-source pass before choosing today’s topic. Treat the repository as the source of truth rather than relying on previous chat history or memory.

Create and QA today’s edition, then inspect the actual final PNG at full size before showing it to me. Confirm that every text block, axis/tick label, caption, annotation, panel boundary and footer/source line has safe clearance and that nothing clips, overlaps, collides or becomes unreadable. Only then may `render_checked` be treated as true.

Show me the finished image for approval. Do not publish anything to GitHub yet. If the final-pixel inspection fails, rerender and reinspect before presenting anything.

---

## Publish Data Lens

OK to push using @GitHub.

Publish the exact Data Lens edition I just approved to `adamgreen1708/chart-templates`, following the current repository publishing instructions. Do not regenerate or alter the approved image or copy. Create the required branch, commit and PR rather than merging directly to main, unless the repository instructions explicitly say otherwise.
