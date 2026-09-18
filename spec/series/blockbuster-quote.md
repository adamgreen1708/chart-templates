# Today’s Blockbuster Quote

Status: prototype integration specification.

## Purpose

Publish one verified, accessible coffeetableviz edition for a genuinely date-linked blockbuster film. Accuracy outranks speed, novelty and automatic publication.

## Publishing contract

Each edition lives in `site/_blockbuster_quotes/` and must contain:

- the frozen six-field copy deck;
- structured date-link and quote sources;
- explicit QA sign-off flags;
- one deterministic square render;
- accessible HTML text matching the rendered image.

The repository validator must pass before Jekyll builds the site. A failed or uncertain edition is not committed.

## Review model

1. ChatGPT researches and freezes the copy deck.
2. The evidence ledger is translated into edition front matter.
3. The image is rendered deterministically.
4. Repository validation runs.
5. A pull request is reviewed.
6. Only a merge publishes the edition.

Automatic creation of draft pull requests may be considered after a successful reviewed pilot. Automatic merging is out of scope.

## Edition front matter

```yaml
---
date: 2026-09-17
header: "TODAY’S BLOCKBUSTER QUOTE"
film: "Film title"
film_year: 2000
quote: "Exact verified short quote."
character: "Character"
performer: "Performer"
why_today: "35–65 verified words, beginning with the exact date connection."
kicker: "A dry line containing no new factual claim."
connection_type: "original theatrical release"
connection_territory: "United Kingdom"
hero_image: "/assets/blockbuster-quote/2026-09-17-film-title.png"
hero_alt: "Accessible description of the complete editorial card."
sources:
  - role: date_link
    title: "Source title"
    url: "https://example.com/source-one"
  - role: date_link
    title: "Independent source title"
    url: "https://example.com/source-two"
  - role: quote
    title: "Quote source title"
    url: "https://example.com/quote-source"
qa:
  run_date_verified: true
  date_link_verified: true
  quote_verified: true
  speaker_verified: true
  copy_deck_frozen: true
  render_checked: true
---
```

## Current scheduled ChatGPT prompt

The following is the exact prompt captured from the enabled “Daily Blockbuster Quote” automation when this specification was created.

```text
Create today’s “Today’s Blockbuster Quote” as ONE finished, publication-ready square editorial image.

NON-NEGOTIABLE STANDARD
Accuracy is the product. A beautiful wrong image is a failed run.
Priority order: factual accuracy > correct RUN_DATE > source quality > exact quote transcription > deterministic rendering > visual quality > novelty > wit.
If any factual or rendering gate fails, do not present an image.

STEP 0 — RESOLVE RUN_DATE FIRST
This must be the first action on every run.
1. Resolve the current date from the automation execution time in the Europe/London timezone.
2. Freeze it internally as RUN_DATE in full written form.
3. RUN_DATE is the only date that may be treated as “today”.
4. Do not infer today from conversation history, previous runs, cached context, old images, examples, search snippets, model memory or training data.
5. Do not reuse any previous film, quote, date connection, anniversary calculation, copy deck or image prompt unless it is freshly re-researched and re-verified against the current RUN_DATE.
6. If RUN_DATE cannot be resolved confidently, fail the run. Never substitute another date.

STEP 1 — RESEARCH MULTIPLE EXACT-DATE CANDIDATES
Use fresh web research before any image work.
Find several recognisable mainstream blockbuster films with a genuine connection to RUN_DATE’s exact calendar month/day.

Preferred connection hierarchy:
1. original theatrical release or premiere on RUN_DATE’s month/day in a clearly named territory
2. birthday of a principal actor or director directly connected to the film
3. major award date directly tied to the film
4. box-office milestone reached on that exact date
5. another genuine film-history event directly tied to the film
6. an occasional numerical/date connection only if unusually strong, central and independently verifiable

Reject weak, incidental or forced connections.

Do NOT confuse an original release with a re-release, restoration, home-video release, streaming release, production date, filming-start date, copyright date, press screening, retrospective article date, search-result date or unrelated anniversary.

For theatrical-release candidates, explicitly identify whether the evidence refers to world premiere, festival premiere, limited opening, national opening or general theatrical release, and name the territory.

STEP 2 — HARD DATE-LINK VERIFICATION
The date link must PASS before quote research or image work continues.

For the chosen candidate:
1. Open and read the relevant sources. Search snippets alone never count as verification.
2. Verify the exact RUN_DATE month/day using at least TWO independent reliable sources wherever practical.
3. At least ONE source should be primary, institutional or high-authority where available: studio/distributor, AFI, BFI, Academy/AMPAS, official festival/archive, Box Office Mojo, The Numbers or similarly authoritative film records.
4. Record the exact date wording and territory/event from each source.
5. Perform an adversarial check: actively search for a conflicting or alternative release/premiere date and determine why it differs.
6. Explicitly rule out confusion with re-release, premiere vs general release, territory differences, production date or another milestone.
7. If the two sources cannot be reconciled confidently, REJECT the film and choose another.

DATE-LINK PASS CONDITION
Proceed only if all are true:
- the chosen connection matches RUN_DATE’s exact month/day
- the event type is correctly identified
- the territory is correctly identified where relevant
- the chronology is plausible
- no unresolved conflicting date remains

STEP 3 — VERIFY FILM TITLE, YEAR AND INVOLVEMENT
1. Verify the exact film title and release year from a high-authority film source.
2. If using a birthday, separately verify the person’s birth date and their role in the film.
3. If using an award, separately verify the award date and the film-specific result.
4. If using a box-office milestone, separately verify the exact dated milestone and the figure involved.
5. Do not infer any supporting biographical or historical detail that is not directly sourced.

STEP 4 — VERIFY THE QUOTE EXACTLY
1. Use a reliable script, official subtitle/transcript source, studio/film source or another source that clearly reproduces the spoken line.
2. Prefer primary or near-primary wording over unsourced quote aggregators.
3. Cross-check the wording with a second source where practical.
4. Preserve exact wording, spelling and punctuation.
5. If sources disagree materially and the exact spoken line cannot be established confidently, reject the quote or choose another film.
6. Always identify and verify who speaks the quote in the film: character name and actor/performer where reliably established, because this context should normally feed the WHY TODAY section.
7. Keep the quote short enough to typeset cleanly.

STEP 5 — VERIFY ALL DERIVED AND CONTEXT CLAIMS
Explicitly calculate and test any age, anniversary number, elapsed years, ranking, box-office arithmetic, date difference, count or wording claim.
Do not approximate.
Also verify any supporting context intended for WHY TODAY, including speaker/character, actor, scene context, film premise, production detail or relevant biographical detail. Prefer film-specific context that helps the reader understand the quote.
If a derived or contextual fact is unnecessary or cannot be strongly verified, omit it rather than creating another failure point.

STEP 6 — PRIVATE EVIDENCE LEDGER
Before drafting the poster, create an internal evidence ledger for EVERY factual statement or number that might appear:
- EXACT CLAIM
- SOURCE 1
- SOURCE 2 / independent check where appropriate
- DERIVATION / calculation if any
- CONTRADICTION CHECK
- PASS / FAIL

Every factual element must be PASS.
A FAIL or unresolved claim eliminates that wording or the entire candidate.

STEP 7 — FREEZE THE VERIFIED COPY DECK
Only after all evidence passes, freeze exactly these six fields:
DATE — RUN_DATE exactly
HEADER — TODAY’S BLOCKBUSTER QUOTE
FILM — exact film title + verified release year
QUOTE — one short exact verified quote
WHY TODAY — a compact 2–4 sentence mini-story, normally around 35–65 words. It MUST begin by clearly stating the exact verified RUN_DATE connection, including territory/event type where needed. Then add useful verified context around the quote. Where reliably verifiable, prioritise: (a) who says the quote — character and actor/performer; (b) the immediate scene/context in which it is said; and/or (c) one concise detail about the film, character or performer that makes the quote more meaningful. Do not force all three. Choose the strongest details. This section should answer both “why this film today?” and “why this quote?”.
KICKER — one very dry observational line containing NO new factual claim

No other factual text may appear.
Do not add cast lists, unrelated trivia, source names, extra dates, anniversary counts, icons with labels, captions or explanatory metadata outside the frozen six fields. The expanded WHY TODAY is the designated place for verified contextual detail.

STEP 8 — FINAL PRE-RENDER AUDIT
Before rendering, explicitly confirm internally:
□ RUN_DATE came from the current Europe/London execution time.
□ DATE in the frozen deck equals RUN_DATE exactly.
□ The central connection matches RUN_DATE’s exact month/day.
□ The event type and territory are correctly identified.
□ The central date link passed two-source verification or a documented equivalent where two sources genuinely do not exist.
□ The adversarial date search found no unresolved contradiction.
□ Film title and year are verified.
□ Quote wording is verified exactly.
□ Quote speaker/character attribution is verified.
□ Any actor/performer, scene, film-context, person/award/milestone detail used in WHY TODAY is separately verified.
□ WHY TODAY clearly explains the exact date connection first, then adds useful quote/film context.
□ Every number or derived claim has been explicitly checked.
□ Every factual poster element is PASS in the evidence ledger.
□ No stale content from a previous run appears anywhere.

If ANY box fails, do not render. Choose another candidate or fail the run.

CRITICAL RENDERING RULE — FACTUAL TEXT MUST BE DETERMINISTIC
Do NOT use an image-generation model to compose, typeset, rewrite, infer or reproduce the factual poster copy.
Do NOT ask an image model to make the complete poster.

Render all visible text and layout deterministically from the frozen copy deck using a programmatic graphics method such as Python/Pillow, SVG or equivalent.
Every visible character, date, number and punctuation mark must come directly from the frozen deck.
The renderer must not invent or alter text.

ILLUSTRATION RULE
Use exactly ONE symbolic, monochrome, cross-hatched editorial illustration inspired by the film.
Preferred method: create the illustration deterministically with programmatic line art, hatching, geometry or a simple symbolic motif.
If an image-generation model is used at all, it may generate ONLY a text-free decorative illustration asset. It must never receive or render the poster copy, date, film title or quote. Composite the verified deterministic text over/alongside the illustration programmatically afterward.

Prefer symbolic objects, environments or motifs over actor likenesses.
Do not recreate a film poster, publicity still or copyrighted composition.
Do not imitate a celebrity portrait.
The illustration must introduce no new text or factual claim.

LOCKED HOUSE STYLE
- 1:1 square social/editorial card
- soft grey lightly textured paper matching the site background (`#f1f1f1`)
- unusually generous outer padding and negative space
- near-black typography matching the site ink (`#111111`)
- restrained coffeetableviz red accents (`#c94545`)
- muted grey secondary text and divider rules
- large elegant high-contrast serif for the quote
- small uppercase contemporary sans-serif for date, heading and metadata
- thin understated divider rules
- balanced asymmetrical composition
- exactly one symbolic monochrome cross-hatched sketch
- supporting copy visually quiet
- allow enough vertical space for the expanded 2–4 sentence WHY TODAY section; reduce illustration footprint or rebalance negative space if needed, but never shrink contextual copy to illegibility

Avoid pinned notes, pushpins, scrapbook styling, decorative borders, large colour blocks, cards/panels, clutter, multiple illustrations, unnecessary icons, faux movie-poster recreation or celebrity likeness imitation.

STEP 9 — POST-RENDER QA ON THE ACTUAL FINAL IMAGE
Inspect the rendered image itself before presenting it.
1. Read every visible word, date and number.
2. Compare the image character-for-character with the frozen six-field copy deck.
3. Confirm the visible date equals RUN_DATE exactly.
4. Re-open/re-check the central date-link evidence one final time.
5. Confirm quote wording, punctuation, film title, year and the full WHY TODAY copy are unchanged.
6. Confirm the expanded WHY TODAY remains comfortably readable and is not clipped, overcrowded or visually subordinate to the point of illegibility.
7. Reject the render for any typo, wrong date, changed quote, new factual claim, missing text, duplicated text, ghosting, clipping, overlap, malformed lettering, mixed candidate content, accidental extra date, or layout failure.
8. Confirm the illustration contains no text and no new factual claim.
9. If layout fails, fix the deterministic layout and rerender internally. Never alter factual copy merely to make the layout fit.

FINAL DELIVERY — ONE IMAGE ONLY
- Present exactly ONE final QA-passed inline image.
- Never show drafts, previews, failed renders, retries, candidates or alternatives.
- Do not include explanatory prose before or after the image.
- Do not return a filename, file path, markdown link or sandbox link as the main result.
- If a fully verified, correctly rendered image cannot be produced, return a concise failure notice instead of an incorrect image.

The governing rule is simple: VERIFY FIRST, FREEZE COPY, RENDER DETERMINISTICALLY, VERIFY THE ACTUAL RENDER, THEN PRESENT.
```
