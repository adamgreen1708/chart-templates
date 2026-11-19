# Pattinson → Bond article: fact-check and editorial gate

**Research freeze:** 18 November 2026 IMDb official datasets and independently audited cast roles. **Article draft:** `content/blog_draft_v2.md`. Prepared for editor review on 19 November 2026; **not published**.

## Verified story claims

| Proposed claim | Evidence | Outcome |
|---|---|---|
| Pattinson announced as James Bond on **16 November 2026** | [Amazon MGM studio announcement](https://www.aboutamazon.com/news/entertainment/james-bond-robert-pattinson-cast-amazon-mgm-film); [Associated Press](https://www.ap.org/news-highlights/spotlights/2026/robert-pattinson-is-named-the-seventh-james-bond-taking-over-from-daniel-craig/) | Confirmed |
| **33** released/rated Pattinson film credits in research scope | `generated/story_v2_qa.json`, `chart_v2_02_career.csv` from [successful research run #44615518367](https://github.com/adamgreen1708/chart-templates/actions/runs/44615518367) | Confirmed; includes some supporting roles and one English-dub role, not just leading performances |
| Five Twilight film ratings average **5.18 → 5.2** | `chart_v2_01_twilight.csv`; `build_story_v2.py` computes the arithmetic mean from one film-level weighted IMDb score per title | Confirmed; not the median (5.1) and not a vote-weighted mean |
| Other 28 films average **6.59643 → 6.6** | Same QA and build script, excluding the five Twilight titles | Confirmed |
| Five Twilight titles total **1,723,898** title-votes, **24.84%** of the **6,939,190** vote counts across the 33 titles | Same QA snapshot `twilight_film_votes_sum`, `total_film_votes_sum`, `twilight_votes_pct` | Confirmed; aggregate title votes are **not distinct people** |
| *The Batman* has the most IMDb title-votes (**958,793**), original *Twilight* has the most within the Twilight group (**539,310**), and *The Odyssey* has the highest IMDb rating (**8.4/10**) | `chart_v2_02_career.csv`, `annotation_role` derived by tested rank selection, [IMDb The Odyssey](https://www.imdb.com/title/tt33764258/) | Confirmed within snapshot; voting/rating values will change |
| Six distinct cast bridges; one Bond, two Bond allies, three villains | `chart_v2_03_bond_paths.csv`; ID-keyed `data/bond_roles_verified.csv` and audited supplementary credits | Confirmed as **verified examples, not an exhaustive historical co-star total** |
| Ralph Fiennes and Pattinson share *Harry Potter and the Goblet of Fire* cast; Fiennes later portrayed M | Audited `audited_additional_credits.csv`, `audited_bond_cast_links.csv` and official Bond film register | Confirmed |
| Christoph Waltz worked with Pattinson on *Water for Elephants* | [BBFC film cast](https://www.bbfc.co.uk/release/water-for-elephants-q29sbgvjdglvbjpwwc00nzaxmja) | Confirmed |
| Mathieu Amalric worked with Pattinson on *Cosmopolis* | [Alfama Films official film page](https://alfamafilms.com/en/film/cosmopolis) | Confirmed. **He had already played Dominic Greene in 2008; do not call him a 'future villain'** |
| Rami Malek worked with Pattinson on *Breaking Dawn – Part 2* | [Fandango cast listing](https://www.fandango.com/the-twilight-saga-breaking-dawn-part-2-2012-135731/cast-and-crew) | Confirmed |
| Jeffrey Wright worked with Pattinson on *The Batman* | [Official DC page](https://www.dc.com/movies/the-batman-2022) | Confirmed |
| Brosnan played Pattinson's father in *Remember Me* (2010), then publicly welcomed him as Bond | [Digital Spy, 19 Nov 2026](https://www.digitalspy.com/movies/a74473685/pierce-brosnan-responds-robert-pattinson-cast-james-bond/), [Variety, 19 Nov 2026](https://au.variety.com/2026/film/global/robert-pattinson-pierce-brosnan-james-bond-42741/) | Confirmed; avoid implying a personal casting influence |

## Editorial cautions

- IMDb film ratings describe titles, **not Pattinson's individual acting quality**. All 33 are rated credits, including supporting roles.
- IMDb vote counts do not measure ticket sales, a film's audience size, or unique voters across titles.
- Do not treat the verified six co-stars as an exhaustive list or imply these relationships motivated Amazon MGM's casting.
- The new charts are **already approved for visual review**; preserve them unchanged unless asked. PR #221 remains draft/unmerged.
- Before site publishing, check IMDb's [non-commercial dataset terms](https://developer.imdb.com/non-commercial-datasets/) and use a proper chart/source footer.
- No Jekyll site/_posts page, publication image assets, or GitHub Pages merge/deployment is authorised at this editorial-review step.
