# David Bowie reinvention — research plan

## Core question

Can we show, with transparent real data, that David Bowie's long recording career was not simply durable but repeatedly changed musical direction — and can we do it without pretending a genre tag is the same thing as creativity?

## Scope definition

The phrase “over five decades” is ambiguous. Bowie’s lifetime solo studio chronology runs from the 1967 debut to *Blackstar* in 2016: a 49-year difference across **six named calendar decades**.

The validated focus scope contains **26 studio albums**.

Two catalogue decisions matter:

- **Include *The Buddha of Suburbia* (1993).** Bowie's official store identifies it as his 19th studio album, even though MusicBrainz also marks it as a soundtrack.
- **Exclude *Toy* from the lifetime chronology.** Bowie's official archive describes it as previously unreleased; the standalone release arrived in 2022.

Live albums, compilations, *Peter and the Wolf* and Tin Machine are outside the solo studio-album sequence.

## Source strategy

### Chronology and identity

Use MusicBrainz for reproducible artist/release-group identity and album dates, then cross-check Bowie-specific edge cases against davidbowie.com.

### Style metadata

Use **AllMusic album-level Styles** as the primary like-for-like style vocabulary for the reinvention analysis.

Reason: MusicBrainz genre coverage is uneven across the chronology. Mixing missing MusicBrainz genre sets with zeros would create false “no change” observations.

AllMusic currently exposes Styles for 25 of the 26 scoped albums. Its *The Next Day* page exposes no Styles values. MusicBrainz genres for that album are retained only as supplemental context and are **not** mixed into the Jaccard calculation.

## Reinvention measure

For adjacent albums with AllMusic Styles metadata on both sides:

- represent each album as its complete observed AllMusic Styles set;
- calculate Jaccard similarity = intersection / union;
- define style reset score = `1 - similarity`;
- retain the introduced and dropped style labels for auditability;
- leave a transition missing when either side lacks AllMusic Styles.

This yields 23 measured transitions out of 25.

The score measures **metadata turnover between adjacent albums**. It is not an objective creativity, quality or influence score.

## QA findings

- The official Bowie catalogue overrides a naive MusicBrainz secondary-type filter for *The Buddha of Suburbia*.
- *Toy* must not be allowed into the lifetime sequence merely because catalogue databases expose it as an album.
- AllMusic’s broad umbrella labels are very persistent: Contemporary Pop/Rock appears on 24 of 25 tagged albums, Art Rock on 23 and Experimental Rock on 22.
- Because broad labels persist, famous musical pivots can receive modest reset scores. That is a property of the taxonomy, not evidence that the pivot did not happen.
- *The Next Day* remains missing in the AllMusic Styles field, so the two adjacent transitions around it are explicitly missing rather than imputed.

## Analytical result

The style-turnover calculation is useful but imperfect:

- median measured reset: 0.3333;
- debut -> *Space Oddity*: 0.8889;
- *Tonight* -> *Never Let Me Down*: 0.7500;
- *Diamond Dogs* -> *Young Americans*: 0.6667;
- *Let's Dance* -> *Tonight*: 0.6250;
- *Scary Monsters* -> *Let's Dance*: 0.6000;
- *The Buddha of Suburbia* -> *1. Outside*: 0.6000.

The counterexample is editorially valuable: *Station to Station* -> *Low* scores 0.3333 because six broad AllMusic labels remain shared.

## Recommended route

The strongest first story is now **Bowie-only**:

1. establish the 26-album, six-decade chronology;
2. show the style labels appearing/disappearing through the catalogue;
3. show what happens when we try to reduce reinvention to one simple score.

The wider peer cohort remains useful for a later extension about longevity, but it should not hold up the Bowie story or become an unsupported “most reinvented” ranking.

See `content/story_plan.md` for the approval-ready three-chart editorial sequence.
