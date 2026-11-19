# Coffeetableviz: senior editorial judgement standard

**Status:** proposed reusable standard, drafted 19 November 2026 after the Pattinson-to-Bond project. This complements the locked renderer/style; it does not change them.

## The governing test

**A chart must earn its space.** Being correct, attractive and successfully rendered does not make it worth publishing. Before code, ask:

> What does the reader discover here that they did not know before, why is that interesting, and why is this the clearest honest way to show it?

Aim for **creativity, flair, clarity and intrigue with accuracy as the absolute floor**. A plain dot plot with a beautiful insight beats a showy diagram without one. Novelty must come from the evidence or the genuine way it is communicated, not decoration.

## The job is editorial analysis, not three charts by default

1. **Research and delimit.** Verify the topical hook (especially current news) with primary sources. Resolve identity, titles, dates, units, population, rating/vote definitions, dataset completeness and licence. Freeze a dated source snapshot. Record what the source cannot establish. A supporting role is not a leading-role performance; a title vote is not a unique viewer, sale or box-office receipt.
2. **Interrogate before drawing.** Compute distributions, coverage, missingness, extremes, rankings, meaningful comparators, possible confounders, chronological changes, thresholds, contradictions and human connections. Where a source is incomplete (e.g. truncated principal cast), verify supplementary links, retain source flags, and de-duplicate at the right analytical grain (unique people versus film-pair edges).
3. **Generate competing stories.** Explore at least three substantively different hypotheses, not three chart types showing the same statistic. Rank by strength of verified evidence, surprise, relevance to a non-expert, visual potential and originality. Reject weak options explicitly; don't attach a generic chart simply to reach a three-chart quota. Consider additional source research before conceding a weak story.
4. **Select an argument.** One-sentence central idea; identify the counter-intuitive finding, the reason it matters and the strongest qualifying caveat. A three-chart sequence should usually **establish → complicate → reveal**, with a different piece of information in each. If the evidence supports only one great chart, make one, not three fillers.
5. **Design to reveal.** For each chart, document the exact question, population and denominator, measurable claim, chosen form, selection rules for highlights/annotations, and a rejected alternative form. Consider timeline, distribution, connected dot, range, slope, ranked table, scatter, alluvial/network/schematic or small multiples according to the question—not merely familiarity or novelty. Use a registered deterministic GitHub specialist renderer when a standard type hides the real discovery.
6. **Challenge the draft *before* render.** Ask: Is this obvious without the chart? Is it just three means? Am I counting source rows rather than actual subjects? Do the labels select genuinely important observations by a consistently testable rule? Does the chart contain a new comparison or relationship? Would I be happy defending every title claim in public? If not, go back to discovery.
7. **Render only in GitHub.** All quantitative/factual data graphics, including exploratory review charts and revisions, must be produced from real files and recomputed derived datasets using GitHub-controlled scripts, `CHART_CONFIG` and the approved `src/render_538.py` or a registered reproducible specialist. **Never create, fake, edit or redraw a data chart using ChatGPT image generation or manual layout tools.** Non-data moodboards/wireframes are allowed only if explicitly labelled conceptual, carry no measured values, and are never substituted for a chart.
8. **QA numbers and language as well as pixels.** Independently recalculate statistics in the code. Prefer unweighted mean when the intended plain-language claim is “average film score”; median is appropriate for skew/robustness but must be called *median*. Do not quietly switch statistic mid-review; update all claims and annotations together. If the sample is curated, say so. State axes, units, baselines and truncations. Use plain language instead of jargon unless the term provides real value and is explained.
9. **Encode consistently.** Same colour = same meaning across the series. Neutral statistics must not borrow a colour whose semantic role is different (e.g. a blue percentage adjacent to a blue comparison group). Match inline legend text to markers, not merely marker shapes. Explain size in reader language (“Bigger circle = more IMDb votes”), not “area proportional to count”. For any network show actual people, entities and links, with verified role and edge provenance; an abstract count is not a substitute for the relationships.
10. **Justify annotations.** Choose by repeatable rules—highest value, largest vote count, most for a defined subgroup, specific time point, documented exception—or disclose that selection is an editorial example and why it matters. Do not label famous cases because they are famous while implying the labels are a rank. Check ties and denominators. De-duplicate same person across films before computing people counts.
11. **Perform real visual QA.** Inspect the finished 1600px image plus 390px and 320px exports, not just CI success. Verify every axis tick, headline, legend, detail, source, footer, annotation line, overlap, spacing and all four edge margins. Re-run after *each* revision. Clipped paragraphs, unlabeled scales, illegible legends and colour ambiguity are rejection criteria.
12. **Get the evidence and editorial approvals separately.** Show a copy of the actual GitHub artifact with source/version. Record accepted chart hash; publish that exact byte sequence. A passing build is not an editorial approval. Charts, article, feature illustration and site release are separate approval gates. Feature illustrations may be created imaginatively, but must remain explicitly non-data art, story-specific, reviewed and stored as approved.
13. **Publish through the repo.** Draft branch → reproducible build → data QA → visual/manual review → explicit approval → reviewed PR → Pages deployment → verify the actual public URL. Do not describe a live page as checked when only the deploy status is known.

## Senior analyst's “kill the chart” questions

For each proposed chart write answers *before* building:

| Test | Hard question |
|---|---|
| Discovery | Is there a non-obvious fact, tension or connection, not just a ranking or average? |
| Significance | Why should someone outside the subject care? |
| Precision | Exactly which records, units, dates and aggregation support the claim? |
| Comparison | What meaningful counterfactual, baseline or relevant reference makes the difference visible? |
| Intent | Why this form—not the obvious first chart type—and what would be lost with the alternative? |
| Encoding | Can a first-time reader tell what position, colour, shape and size represent? |
| Labelling | Why is *this* point named? Would the rule select it if the title changed? |
| Honesty | What is *not* in the data? What would contradict or weaken the headline? |
| Cohesion | Does each chart add information rather than retell the previous one? |
| QA | Could any source, label or missing tick embarrass us if viewed at phone size? |

**If the answers are weak, stop chart production and research more.** “Technically correct” is not a pass.

## Reusable first handback

Keep this concise, editorial and grounded:

```text
Three strongest story routes (ranked, with evidence + weaknesses):
1. ...
2. ...
3. ...

My preferred route and why it wins:
...

Three revelations (or a justified different count):
1. What readers discover — data/source and visual form
2. What changes our understanding — data/source and visual form
3. The surprising payoff — data/source and visual form

Deliberately rejected:
...
What could make the story misleading:
...
GitHub data → render → full/mobile QA → editorial approval gates:
...
```

## A mechanical preflight that does not pretend to judge creativity

Use `python scripts/qa_story_discovery.py <path-to-project-story-review.json>` for real project story manifests. It tests auditable numbers, distinct hypotheses, annotations, meaningful chart roles and encoding provenance. **It does not certify whether an idea is original, engaging or beautifully designed.** A responsible editor must still answer the judgement questions and inspect rendered pixels.

Reference: `docs/lessons/2026-11-19-pattinson-editorial-retrospective.md`. Upstream styling and renderer authority remains `spec/538_template_rules.md`.
