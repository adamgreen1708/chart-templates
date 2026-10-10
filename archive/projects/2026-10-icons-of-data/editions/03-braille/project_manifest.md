# Icons of Data — Edition 03: Braille
**Working title:** Six dots. Rather a lot to say.
**Started:** 9 October 2026.
**Status:** Braille Jekyll article, three credited/verified images, final revised Chart 3 and Resources entry staged on draft PR #112; browser QA passed; final author publish approval pending.
**Subject:** Louis Braille's six-dot tactile writing system; started 1824, first published 1829.

## Files
- `content/braille_03_draft.md` — ~350–400 word working article, three figure locations.
- `content/braille_03_visual_plan.md` — original object + six-dot decoding + Decode the Icon.
- `research/braille_03_sources.md` — specialist historical/code sources and key caveats.
- `data/verified_braille_examples.csv` — minimal machine-readable dot-position examples for later deterministic drawing, not a general Braille translator.

## Coding standard — locked for this edition
All *encoding* diagrams and source data use **UK Unified English Braille (UEB), uncontracted examples**, from **RNIB and UKAAF** with ICEB 2024 rules accepted by UKAAF. Do not use legacy American English Braille (EBAE) or older British Standard English Braille (SEB) as the code of the examples. UEB is internationally shared; there is no artificial UK-only basic alphabet. Separate original 1824–1829 French Braille history from modern UK examples.

## Editorial purpose
Broaden 'Icons of Data' beyond pictorial encoding: a system meant to be **felt**, not merely seen. Explain character formation, patterns, context markers and writing as well as reading. Keep six-dot design integrity, don't equate pictures of dots to tactile Braille.

## Next stage
1. Author approves draft article title/voice and the three-picture storyboard.
2. Clear rights for specific historical photo of 1829 book and select real physical embossed Braille image.
3. Two diagrams built and reviewed: Chart 2 explains UK UEB encoding; approved revised Chart 3 explains why tactile writing mattered. GitHub-runner outputs have a tiny rasterisation difference from the reviewed PNGs, documented for final author visual sign-off.
4. Draft Jekyll article, source photograph (licence credited) and Resources Edition 03 link are staged on the PR only, not yet published.
5. Jekyll/desktop/mobile QA passed (run 37998183946). Request explicit author approval before GitHub merge and Pages publishing.

## Safety
The initial project files contain no images or site changes. No WordPress. Original artefact licensing is a publication gate.

## Staged site paths
- `site/_posts/2026-10-09-six-dots-rather-a-lot-to-say.md`
- `site/assets/icons-of-data/braille/01_embossed_braille.jpg` (CC BY 2.0 image by Ralph Aichinger, original photo downscaled)
- `site/assets/icons-of-data/braille/02_six_places_many_patterns.png`
- `site/assets/icons-of-data/braille/03_why_braille_mattered.png`
- `site/resources/icons-of-data/index.html`
- `scripts/render_braille.py`, `scripts/render_braille_revision_03.py` (readable original drawing code)
- `qa/site/` (actual browser screenshots at desktop/mobile/narrow)

Images on the website branch differ *slightly* from the user's originally approved PNG hashes because the Action runner's rasterisation differs. Their layouts were visually inspected, but require final author approval of the full website presentation. The site is NOT live from this draft branch.
