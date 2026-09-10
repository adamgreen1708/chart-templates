# Story plan: James Bond villains

## Recommended story route

Bond villains did not simply get steadily younger; Bond actors increasingly met villains closer to their own age or younger.

## Why this is the strongest route

The raw villain-age spread is interesting, but the richer pattern appears when villain age is compared with Bond's age in the same film. Early Eon Bond is usually the younger man facing older antagonists. From the Roger Moore era onward that gap largely disappears or reverses, and the Craig era finishes almost perfectly age-matched on average.

This route is stronger than a simple `villains got younger` claim because the villain ages themselves do not show a clean steady decline. The relationship between Bond's age and his opponent's age is the more defensible and more surprising story.

## Story options considered

### Option 1 — Villain age spread

**Core argument:** Bond villains have been played across a wide age range, from the early 30s to about 65.

**Why it works:** Immediate, concrete and easy to read.

**Data required:** First-listed villain actor age at exact UK release date; retain both `Die Another Day` portrayals for the actor-level view.

**Likely chart sequence:** Ranked age spread, decade/era comparison, oldest/youngest examples.

**Risk / weakness:** Interesting as a distribution, but it does not explain how the casting relationship changed across the franchise.

### Option 2 — Bond used to fight his elders

**Core argument:** Early Bond was substantially younger than his first-listed villains; later Bond often became the older man.

**Why it works:** It turns actor ages into a franchise-level relationship with a clear before/after pattern.

**Data required:** Exact Bond age and first-listed villain age at UK release for all 25 Eon films.

**Likely chart sequence:** Villain age spread, film-level age gap, Bond-era age relationship.

**Risk / weakness:** Must state the first-listed-villain rule clearly and avoid implying age caused any creative or commercial outcome.

### Option 3 — SPECTRE through film chronology

**Core argument:** SPECTRE dominates early film antagonists, disappears, then returns.

**Why it initially looked promising:** Strong recognisable organisation and apparent chronological shape.

**Risk / weakness:** Eon film release order does not follow Fleming publication order. Using film chronology to imply literary evolution would be misleading. This route was therefore demoted rather than forced.

### Option 4 — Who got the best Bond film to be evil in?

**Core argument:** Rank first-listed villains by the IMDb rating of the film they appear in.

**Why it works:** Fun companion chart with recognisable films and villains.

**Risk / weakness:** IMDb rates the film, not the villain. It is context only and should not be interpreted as a villain-quality ranking or causal relationship.

**Decision:** Promote this to a small bonus chart after the core age story, rather than turning it into a fourth step in the main age narrative.

## Recommended 3-chart story

### Chart 1 — Bond villains range from 32 to 65

**Role:** Set the scene.

**Story question:** How old has a Bond villain been when the film reached UK audiences?

**Chart type:** Ranked dot plot.

**Data needed:** `data/bond_villains_chart_01_actor_age.csv`

**Key stat:** First-listed villain actor portrayals range from Will Yun Lee at about 31.7 to Lotte Lenya at about 65.0 years old at UK release.

**Why this chart matters:** Establishes the broad casting range before asking how those ages compare with Bond himself.

**Potential issue / QA risk:** Long villain labels and repeated Blofeld appearances require unique year-suffixed labels and generous left margin. `Die Another Day` has two actor portrayals and must appear as two actor-level observations.

### Chart 2 — Bond used to fight his elders

**Role:** Build the tension.

**Story question:** Was the villain older or younger than Bond in each film?

**Chart type:** Film-by-film dot plot of `villain age - Bond age`.

**Data needed:** `data/bond_villains_chart_02_age_gap.csv`

**Key stat:** Across 1962–1971, first-listed villains averaged 14.3 years older than Bond; from 1973 onward they averaged 2.6 years younger.

**Why this chart matters:** Reveals that the interesting change is relative age, not simply villain age.

**Potential issue / QA risk:** The zero reference line must be obvious because it carries the meaning `same age`. `Die Another Day` must count once using the mean age of Toby Stephens and Will Yun Lee.

### Chart 3 — Bond grew into his villains

**Role:** Land the aha moment.

**Story question:** How did the Bond-villain age relationship change by Bond actor era?

**Chart type:** Scatter plot of average Bond age against average first-listed villain age, with an equal-age diagonal.

**Data needed:** `data/bond_villains_chart_03_era_age.csv`

**Key stat:** Connery's villains averaged 13.8 years older; Brosnan's averaged 7.6 years younger; Craig and his villains were almost exactly age-matched at +0.4 years.

**Why this chart matters:** It explains the film-level shift in one compact final view: Bond grew into his villains.

**Potential issue / QA risk:** X and Y scales must be identical so distance from the same-age diagonal is visually honest. The diagonal label must remain inside the safe plotting area.

## Bonus companion chart

### Chart 4 — Le Chiffre got the best Bond film to be evil in

**Role:** A small piece of dessert after the main age story, not part of the core three-chart argument.

**Story question:** Which first-listed villain appears in the highest-rated Eon Bond film in the IMDb snapshot?

**Chart type:** Ranked dot plot.

**Data needed:** `data/bond_villains_chart_04_imdb_companion.csv`

**Key stat:** `Casino Royale` leads at 8.0, ahead of `Skyfall` at 7.8 and `Goldfinger` at 7.7; `Die Another Day` is lowest at 6.1.

**Why this chart matters:** It gives the post one recognisable, playful side statistic without weakening the age thesis.

**Framing / QA risk:** IMDb rates the film, not the villain. Keep all 25 Eon films, use unique villain + film labels, and highlight Le Chiffre only.

## Editorial sequence

1. **Set up:** Bond villains cover a much wider age range than a single stereotype suggests.
2. **Hook:** Early Bond repeatedly faced older villains.
3. **Rising insight:** The age gap shrinks and often reverses after the early Connery/Lazenby films.
4. **Suspense:** Did villains suddenly become younger?
5. **Aha:** Not really. Bond actors themselves got older relative to the antagonists they faced.
6. **Bonus:** Le Chiffre appears in the highest-rated Eon Bond film in the IMDb snapshot.
7. **TLDR:** Bond stopped being the young man walking into a room full of older enemies.

## Method notes

- Use official 007.com UK release dates for the exact-date age calculations.
- Use exact actor dates of birth.
- Use one first-listed villain identity per film for film-level comparison; do not relabel this as an objective `main villain` definition.
- For `Die Another Day`, retain Toby Stephens and Will Yun Lee separately in Chart 1; use their mean for the film-level and era-level comparisons so the film contributes once.
- IMDb companion data is film-level context only and uses the verified snapshot dated 9 September 2026.

## Next build step

Merge the QA-approved Chart 04 companion config/data/output into the project archive, verify the PNG in `main`, then publish from the updated publication package.
