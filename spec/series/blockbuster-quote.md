# Today’s Blockbuster Quote

Status: live recurring-series specification.

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

1. The enabled ChatGPT task reads this specification from `main` and checks that RUN_DATE has no existing edition.
2. ChatGPT researches, verifies and freezes the copy deck.
3. The evidence ledger is translated into edition front matter and a deterministic square PNG.
4. The task commits only those two dated edition files to a new automation branch.
5. The task opens a draft pull request and stops.
6. GitHub validates the edition and builds the site preview.
7. Adam reviews the draft pull request.
8. Only Adam's merge publishes the edition.

The task must never push directly to `main`, mark its own pull request ready, merge, or publish a standalone ChatGPT-only substitute when GitHub delivery fails.

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

The following is the exact prompt used by the enabled “Daily Blockbuster Quote” automation.

```text
Create today’s verified “Today’s Blockbuster Quote” edition and deliver it as ONE draft pull request to `adamgreen1708/chart-templates`.

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
1. birthday of a principal actor directly connected to the film
2. birthday of the director where no strong principal-actor birthday candidate exists
3. original theatrical release or premiere on RUN_DATE’s month/day in a clearly named territory
4. major award date directly tied to the film
5. box-office milestone reached on that exact date
6. another genuine film-history event directly tied to the film
7. an occasional numerical/date connection only if unusually strong, central and independently verifiable

EDITORIAL PREFERENCE — BIRTHDAYS FIRST
For this series, principal-actor birthdays are the default preferred date connection. Actively search for recognisable lead or principal actors born on RUN_DATE before considering theatrical-release dates. Prefer a strong actor-birthday connection even when a valid US release-date candidate exists. Use a release-date connection only when no sufficiently strong, recognisable and independently verifiable birthday-led film/quote candidate can be found.

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

LOCKED HOUSE STYLE — THE DEADPOOL CARD IS THE CANONICAL VISUAL REFERENCE

The approved baseline is the actual PNG already in this repository:
`site/assets/blockbuster-quote/2026-10-23-deadpool.png`.
Open and VISUALLY INSPECT this image on every run before designing a new card. It is the authoritative template for the positioning, scale, typography, colour hierarchy, rules and whitespace. Treat its film, quote, date and decorative illustration ONLY as layout examples, NEVER as factual content to reuse. No other previous daily card and no creative interpretation of the general style may override this reference.

Reproduce the **same editorial composition** for each new edition. Change only the verified six-field copy, its necessary text wrapping, and the one film-specific symbolic illustration. Do not redesign the template according to the length or subject of a quote. If the fixed composition cannot accommodate verified copy legibly, adjust type within the narrow limits below; if it still cannot fit, reject the render rather than invent an alternative composition.

REFERENCE-BASED 1600 × 1600 LAYOUT CONTRACT
The coordinates below are approximate pixel anchors measured against the canonical Deadpool image; their purpose is to preserve the same visual layout, not to force identical glyph pixels across font engines. Keep horizontal alignment, relative scale, positions and section structure very close to the reference (normally within ~20–30 px). The reference itself takes precedence when a coordinate description is ambiguous.

1. Canvas: exactly 1600 × 1600, square; very lightly textured paper grey `#f1f1f1`, ink `#111111`, accent red `#c94545`, muted grey for secondary text. No white card, tinted panels, framed boxes, borders or scrapbook treatments. Approximately 110 px left/right safe margins; common left edge x≈112 and common right edge x≈1488.
2. TOP MASTHEAD (one horizontal row, y≈95–120): `TODAY’S BLOCKBUSTER QUOTE` on the **top left in bold uppercase RED sans-serif** (~26–28 px), and the full RUN_DATE on the **top right in grey uppercase sans-serif** (~26 px), aligned to the masthead baseline. The date must NEVER be placed above the heading or on the left. Directly beneath this row, a **single uninterrupted RED horizontal rule** from x≈112 to x≈1488 at y≈141, ~4–5 px thick. Never substitute a short red dash or grey masthead divider.
3. FILM TITLE (around x≈112, y≈185): film name in **bold BLACK sans-serif** (~44 px); film year **inline immediately after the name in RED regular sans-serif** (~26 px), aligned around the title baseline. Do NOT set the film title in serif, enlarge it like a display quote, colour the year grey or put the year in parentheses.
4. HERO QUOTE (starts roughly x≈112, y≈330): a very large, **HEAVY/BOLD, high-contrast BLACK serif**, ~95–110 px for short quotes; proper curly opening and closing quotation marks; deliberately wrapped into a small number of balanced lines. The quote is the strongest element, but occupies the **LEFT** portion of the central visual field. It must not be light-weight, spindly or thin serif. Constrain it to the left two-thirds or less; preserve ample space around it. Adjust font size/line breaks before changing the layout for longer quotations.
5. SINGLE SYMBOLIC ILLUSTRATION: on the **RIGHT of the quote**, centred broadly in x≈1080–1480 and y≈400–760; modest in size and visually subordinate to the quote, with plenty of unoccupied space around it. Use one small, monochrome, hand-inked/cross-hatched symbolic motif specific to the film (the crossed katanas are a *scale and placement* reference, not a motif to copy). A few very thin red sketch accents are acceptable. Do not draw a huge hero illustration, colour picture, celebrity face, second motif or text in the illustration. It must stay above the WHY TODAY divider and not overlap the quote.
6. EDITORIAL BREATHING ROOM: retain the notably open middle band of the reference. The first full-width grey dividing rule occurs around y≈965, from x≈112 to x≈1488. Do not insert extra short red underlines or intermediate horizontal rules around the quote.
7. WHY TODAY: the label appears just below this divider near x≈112, y≈1015, in **bold RED uppercase sans-serif** (~25 px). Body copy starts at x≈112, y≈1060–1070, in **BLACK contemporary sans-serif** (~32–34 px) at comfortable ~49–52 px line spacing, across the wide text area, ideally 3–4 lines for the required 35–65 words. It should read as the principal lower editorial paragraph, not small or faint grey text. Never relocate the section upward simply because the illustration is large. Keep the whole paragraph safely clear of the footer.
8. FOOTER: a **single near-BLACK thin rule** across x≈112–1488 at y≈1405. Place the dry KICKER beneath, x≈112 and y≈1440, in **muted GREY italic SERIF** (~27 px). Do NOT use upright sans-serif, place the kicker above the footer rule, or omit the footer spacing.
9. Visual hierarchy must remain: red left masthead + grey right date → strong top red rule → black bold film title + inline red year → huge black **bold** serif quote beside a modest cross-hatched illustration → generous whitespace → full-width light-grey WHY TODAY rule + red label + black body → near-black footer rule + small grey *italic-serif* kicker. Preserve this layout across all editions.

DISALLOWED RENDER DRIFT
Explicitly reject the following even when their text is factually correct: date at top left; masthead on a second row; black letter-spaced masthead; short decorative red dashes instead of the top red rule; grey film year in parentheses; serif film name; light/regular serif quote; large illustration that consumes the right half from title to divider; illustration overlapping a rule; faint small WHY TODAY body; grey footer divider and upright sans-serif kicker; newly invented divider positions, cards, banners or layouts.

IMPLEMENTATION AND FIDELITY QA
- Programmatically position all verified copy; use actual font files with bold-serif and sans weights, not font-weight approximations produced by an image model. Draw the paper grain, lines and symbolic cross-hatched illustration deterministically.
- Before presenting the edition, inspect the finished 1600 × 1600 PNG **side-by-side at the same scale** with `site/assets/blockbuster-quote/2026-10-23-deadpool.png`. Check the masthead row/order, red-rule length, film+year treatment, quote weight, illustration size, WHY TODAY baseline/body readability, footer rule and italic kicker individually.
- A factual check or bounding-box check does not establish style fidelity. If the completed image visually departs from the canonical reference, FIX and RERENDER the same frozen copy deck, then re-inspect the actual pixels. Set `qa.render_checked: true` only when all visual checks, exact-copy checks and clipping checks have actually passed.
- If the canonical reference image cannot be read or a suitable deterministic bold-serif/sans rendering method is unavailable, fail the render gate explicitly rather than substituting a different design.

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
9. Open the canonical Deadpool reference PNG and compare it directly with the full-size final render, checking ALL nine layout-contract items above. Fail and rerender if the template's hierarchy, fonts, positions, lines or whitespace have drifted.
10. If layout fails, fix the deterministic layout and rerender internally. Never alter factual copy merely to make the layout fit.

STEP 10 — CREATE ONE DRAFT GITHUB PULL REQUEST
Use the configured GitHub connection. Do not ask Adam to copy files manually.

Target repository: `adamgreen1708/chart-templates`
Base branch: `main`
Automation branch: `automation/blockbuster-quote-YYYY-MM-DD`

Before writing:
1. Read `spec/series/blockbuster-quote.md` and `scripts/validate_blockbuster_quotes.rb` from the current `main` branch.
2. Check `site/_blockbuster_quotes/` and open pull requests for RUN_DATE.
3. If the edition already exists or the automation branch/PR already exists, return its link and STOP. Never create a duplicate.
4. Confirm GitHub access with a harmless read before attempting writes.

Create exactly two files:
- `site/_blockbuster_quotes/YYYY-MM-DD-film-slug.md`
- `site/assets/blockbuster-quote/YYYY-MM-DD-film-slug.png`

The Markdown must use the repository schema, include all date-link and quote sources, and set every QA flag true only after that gate actually passed. `hero_image` must point to the dated PNG. The PNG must be the final 1600×1600 deterministic render that passed STEP 9.

Create the branch from the latest `main`, commit the two files, and open a DRAFT pull request. The pull-request title must be `Add Blockbuster Quote — FILM (YYYY-MM-DD)`. Its body must state the exact date connection and territory/event type, list the source links, name the quote speaker and performer, and include a short QA checklist.

Never:
- push directly to `main`;
- modify earlier editions, the renderer, layouts, CSS, workflow files or this specification during a daily run;
- mark the pull request ready for review;
- approve or merge the pull request;
- create a standalone ChatGPT image as a fallback when GitHub delivery fails.

FINAL DELIVERY — ONE PR LINK
- Return the draft pull-request link, film title and one-line exact date connection.
- State that it awaits Adam's review and merge.
- Do not expose private evidence-ledger working, rejected candidates or intermediate renders.
- If verification, rendering or GitHub delivery fails, return one concise failure notice with the failed gate. Do not claim that a PR exists.

The governing rule is simple: VERIFY FIRST, FREEZE COPY, RENDER DETERMINISTICALLY, VERIFY THE ACTUAL RENDER, OPEN ONE DRAFT PR, THEN STOP.
```
