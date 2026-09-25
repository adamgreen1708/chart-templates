# Mel Gibson career arc — story discovery

## Dataset read

The discovery layer contains 72 released feature-film rows from 1977–2025. It records role flags rather than reception scores.

Derived from that table:
- 65 acting-credit rows.
- 6 directing-credit rows.
- 14 producing-credit rows.
- 3 writing-credit rows.
- The 1980s contain 12 acting-credit rows and no feature directing credits.
- Gibson's feature directing debut arrives in 1993 with *The Man Without a Face*; *Braveheart* follows in 1995.
- There are no released feature acting credits in the 2005–2009 calendar years; *Edge of Darkness* marks the 2010 feature acting return.
- 2020–2025 contains 16 acting-credit rows — the same raw count as the full 1990s — so "he disappeared" is not a good description of the later career.
- The 2022 filmography alone contains seven acting-credit rows.

The important limitation is equally clear: credit volume is not the same thing as theatrical scale, cultural visibility or acclaim. Variety's reporting provides context that his post-2006 acting was rarely in major Hollywood tentpoles or studio films, but a chart should not silently turn that contextual description into a metric.

The director snapshot contains six released features from 1993–2025. Current lifetime worldwide box office in The Numbers spans roughly $24.8m (*The Man Without a Face*) to $622.3m (*The Passion of the Christ*). *Hacksaw Ridge* arrives after a 10-year directing gap; *Flight Risk* arrives nine years later.

## Strongest story options

### 1. Riggs built the star. Braveheart changed the job. — recommended

**Core argument:** The nostalgic memory is of Gibson in front of the camera, but *Braveheart* marks the point where the career becomes two careers. Acting remains prolific, while directing becomes rare, high-stakes and unusually central to the big later chapters.

**Why it works:** It starts exactly where the user starts — *Lethal Weapon* and *Braveheart* — then answers "where did he go?" without reducing the answer to a simple rise-and-fall graph.

**Data required:** verified IMDb acting-movie chronology/ratings; role flags; six-film directing snapshot; selected box-office context.

**Risk / weakness:** the film-count discovery layer cannot by itself measure "star power" or prove why studio scale changed.

### 2. He didn't disappear. The scale changed.

**Core argument:** There is a genuine 2005–09 feature-acting gap, but the later filmography becomes extremely busy: 16 acting credits in 2020–25 and seven in 2022 alone.

**Why it works:** It overturns the first impression created by nostalgia. The credits came back; the kind of visibility attached to them changed.

**Data required:** verified IMDb movie credits by year, plus a reproducible scale measure if the chart goes beyond activity counts.

**Risk / weakness:** "scale changed" needs a metric or clearly attributed industry context. Do not use fame or title recognition as data.

### 3. The rare director became the second career.

**Core argument:** Gibson has only six released feature directing credits across 32 release years, but they include *Braveheart*, *The Passion of the Christ*, *Apocalypto* and the 2016 *Hacksaw Ridge* return.

**Why it works:** The directing gaps themselves are part of the story, and the commercial spread is striking.

**Data required:** director chronology plus current-lifetime box office and, after official IMDb acquisition, rating/vote context.

**Risk / weakness:** nominal lifetime box office is not an inflation-adjusted cross-era success measure; current totals can include re-releases.

## Recommended story route

**Lethal Weapon made the star. Braveheart changed the job.**

The career is more interesting as a change of shape than as a decline. *Lethal Weapon* sits inside an almost entirely acting-led 1980s. By the mid-1990s, *Braveheart* makes directing and producing part of the identity. The 2006 controversy belongs in the explanation as sourced context, not as a charted causal variable. After the acting gap, the credits return in quantity, while directing remains the rarer, higher-stakes lane.

## Why this is the strongest route

It preserves the personal nostalgia hook but lets the data contradict a lazy "whatever happened to him?" narrative. The surprising fact is that the later career is busy. The more defensible question becomes: **why does it feel less visible?** The chart sequence can separate activity from industry scale rather than confusing the two.

## Recommended 3-chart story

### Chart 1 — Riggs built the star. Braveheart changed the job.

- **Role:** Set the scene.
- **Story question:** When did Gibson's screen career stop being only an acting story?
- **Chart type:** career timeline / role strip, with released feature credits in context and directing features highlighted.
- **Data needed:** year, title, actor flag, director flag, producer flag; verified against official IMDb where applicable.
- **Key stat:** 12 acting-credit rows and zero feature directing credits in the 1980s; directing begins in 1993 and *Braveheart* follows in 1995.
- **Why this chart matters:** the reader sees the pivot before being told what happened later.
- **Potential issue / QA risk:** 72 films will crowd a square chart; label only story anchors and do not imply that all actor credits are equivalent in billing or screen time.

### Chart 2 — The acting credits came back in force.

- **Role:** Build the tension.
- **Story question:** Did Gibson actually disappear from feature acting?
- **Chart type:** annual acting-credit count across the verified movie dataset, with the 2005–09 zero-credit stretch and 2010 return annotated.
- **Data needed:** verified IMDb movie year/title rows; annual count; optionally principal order as context, never as screen time.
- **Key stat:** discovery data shows no feature acting releases in 2005–09, followed by 16 acting-credit rows in 2020–25 and seven in 2022.
- **Why this chart matters:** it separates presence from prominence. The later career is active even though Variety notes those post-2006 roles were rarely major Hollywood tentpoles or studio films.
- **Potential issue / QA risk:** the 2020s are a partial decade; compare annual/period counts transparently and do not label activity as box-office success.

### Chart 3 — Directing became the second career.

- **Role:** Land the aha moment.
- **Story question:** What did Gibson do when he stepped behind the camera?
- **Chart type:** six-point chronological dot/scatter of directed features, with current-lifetime worldwide box office as the quantitative measure and long directing gaps annotated.
- **Data needed:** year, title, current-lifetime worldwide box office, source date; optional verified IMDb rating/votes added after acquisition.
- **Key stat:** six released feature directing credits from 1993–2025; *The Passion of the Christ* currently stands at about $622.3m worldwide, while *Hacksaw Ridge* follows a 10-year directing gap and *Flight Risk* a further nine-year gap.
- **Why this chart matters:** it answers "where did he take the career?" — not away from film, but into intermittent directing bets alongside a prolific acting return.
- **Potential issue / QA risk:** box office is nominal and current-lifetime, so the chart must not present it as an inflation-adjusted ranking of artistic or commercial success.

## Epilogue, not chart data

Variety reported in May 2026 that the two-part *The Resurrection of the Christ* had wrapped filming, with Part One planned for 6 May 2027 and Part Two for 25 May 2028. These are future releases and must not be mixed into the released-film dataset.

## Next build step

Run the official IMDb acquisition defined in `docs/imdb_actor_project_prompt.md`, validate the exact identity and analytical set, then rebuild Charts 1–2 datasets from that source. If the story survives validation, create the three chart configs from the locked template and run chart QA. No config work before that gate.
