# Dr Seuss word invention — story plan

## Dataset read

The working dataset contains **12 aggregate observations** transcribed from Teuber (2018):

- 5 part-of-speech shares;
- 4 rhyme/alliteration shares;
- 3 Z letter-frequency comparison shares.

The source study analyses 377 type-2 nonce words from 33 Dr Seuss books. The data is intentionally aggregate: this project does not need a copyrighted book-text corpus to tell the story.

## What the data says

- 61% of the sampled nonce words are common nouns and 27% are proper nouns.
- Those two noun categories make up 88% of the published part-of-speech distribution.
- 48% are influenced by rhyme only, 19% by rhyme plus alliteration, and 17% by alliteration only.
- Together, rhyme and/or alliteration account for roughly 84%.
- Z accounts for 4.42% of letters in the nonce-word sample.
- In the paper's comparison lists, Z is 1.02% of letters in the top 1,000 US surnames and 0.10% in 3,000 common English words.
- The published 4.42% versus 0.10% figures imply a 44.2× ratio.

## Story options

### 1. The nonsense has rules — recommended

**Core argument:** Seuss's invented words look unruly, but the sample shows a strong internal logic: he mostly names things, heavily uses rhyme/alliteration, and gives Z unusually frequent work.

**Why it works:** it turns a familiar cultural impression into a compact, evidence-led language story. Each chart changes scale — grammar, sound, then letters — while advancing the same argument.

**Data required:** the 12 published aggregate metrics in `data/dr_seuss_word_invention_metrics.csv`.

**Risk / weakness:** the sample must not be presented as every Seuss coinage ever written.

### 2. Why does Seuss sound like Seuss?

**Core argument:** focus almost entirely on phonology — rhyme, alliteration and recurring sound patterns.

**Why it works:** closest to the reading experience.

**Risk / weakness:** the available aggregate source gives fewer distinct visual beats, and the story loses the useful grammatical and letter-frequency contrast.

### 3. Seuss by the letter

**Core argument:** focus on over- and under-used letters, with Z as the hero.

**Why it works:** visually memorable and easy to grasp.

**Risk / weakness:** a full alphabet comparison would require additional transcription from the published table and could turn a good punchline into a busier, less focused article.

## Recommended three-chart narrative

### Chart 1 — Seuss mostly invented things

- **Role:** Set the scene.
- **Story question:** What kinds of words dominate the 377-word nonce sample?
- **Chart type:** horizontal bar.
- **Data needed:** the five `part_of_speech_share` rows.
- **Key stat:** common + proper nouns = 88% of the published distribution.
- **Why this chart matters:** it gives the reader an intuitive first insight: Seuss's coinages overwhelmingly name things and characters rather than actions.
- **Potential issue / QA risk:** the paper's percentages are rounded; the chart should not imply more precision than the source.

### Chart 2 — The nonsense follows the sound

- **Role:** Build the tension.
- **Story question:** How often do rhyme and alliteration shape the coinages?
- **Chart type:** horizontal bar.
- **Data needed:** the four `sound_influence_share` rows.
- **Key stat:** rhyme and/or alliteration = roughly 84%.
- **Why this chart matters:** it turns “nonsense” into visible structure.
- **Potential issue / QA risk:** category labels must make the overlap explicit so “rhyme + alliteration” is not double-counted.

### Chart 3 — Z does much more work in Seuss

- **Role:** Land the aha moment.
- **Story question:** How unusual is the letter Z in the nonce-word sample?
- **Chart type:** ranked dot plot.
- **Data needed:** the three `z_letter_share` rows.
- **Key stat:** Z = 4.42% of letters in the Seuss sample versus 0.10% in the 3,000-common-word comparison, a 44.2× derived ratio.
- **Why this chart matters:** it gives the story one tiny, memorable visual fingerprint after the broader grammar and sound patterns.
- **Potential issue / QA risk:** the three comparison lists have different sizes; the chart must compare percentages only and identify the comparison sets clearly.

## Recommended story route

**The nonsense has rules.** In a published sample of 377 Seuss nonce words, the invented vocabulary is overwhelmingly noun-heavy, usually shaped by rhyme and/or alliteration, and unusually fond of Z. The joke is not that Seuss threw letters at the page; it is how much structure sits underneath the apparent chaos.

## Next build step

Render the three locked-template configs from the aggregate dataset, run data/config/layout QA, then present the exact PNGs for Adam's visual review before creating any live-site publication package.
