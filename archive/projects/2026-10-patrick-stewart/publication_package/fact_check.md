# Patrick Stewart — editorial fact check

Checked 31 October 2026 against the frozen dataset and primary sources. Opinion/metaphor is editorial commentary, not a statistical claim.

| Claim | Result | Evidence / qualification | Source |
|---|---|---|---|
| 70 documented movies; 68 rated | PASS | 70 unique IDs; missing rating/votes: The Anatomist, A Minority Pastime | data/films_expanded.csv; IMDb documentation |
| Xavier: 8 films / 61%; Picard: 4 / 4.6% | PASS | Xavier 5,338,592 / 8,739,244 = 61.0876%; Picard 404,702 / 8,739,244 = 4.6309%. Whole-film vote counts, not actor votes. | data/verified_summary.json |
| Logan first, Days of Future Past second, Ted third | PASS | 945,609; 800,953; 722,549. | data/top25_votes.csv |
| Picard ranks 17, 20, 21 and 23 | PASS | First Contact; Generations; Nemesis; Insurrection, respectively. | data/top25_votes.csv |
| Ted is narrated by Stewart | PASS | Agency CV lists TED I & II (Narrator). | https://www.independenttalent.com/actors/patrick-stewart/ |
| Joined RSC in 1966; Picard debut 1987; 21-year gap | PASS | RSC tribute says 1966; official Star Trek page gives 1987–1994; 1987−1966=21. | https://www.rsc.org.uk/news/in-tribute-to-rsc-honorary-associate-artist-sir-patrick-stewart ; https://www.startrek.com/shows/star-trek-the-next-generation |
| Prospero and Xavier in 2006 | PASS | RSC Tempest record; IMDb release year + agency Xavier credit for The Last Stand. | https://www.rsc.org.uk/the-tempest/past-productions ; agency CV; films_expanded.csv |
| Hamlet 2008; Merchant of Venice 2011 | PASS / clarified | Claudius and Ghost, rather than Hamlet; Shylock in 2011. | https://www.rsc.org.uk/hamlet/past-productions/in-focus-gregory-doran-2008 ; https://www.rsc.org.uk/the-merchant-of-venice/past-productions/rupert-goold-2011-production |
| Hirst with McKellen in No Man’s Land, West End 2016 | PASS | Official London Theatre identifies roles, Wyndham’s Theatre, closing 17 Dec 2016. | https://officiallondontheatre.com/show/no-mans-land-356944/ |
| Top three Other ratings at ≥1,000 votes: 8.0 / 7.9 / 7.7 | PASS | Computed across all 56 rated Other films; vote tie-break. Nausicaä 200,096; Earth 15,006; Plague Dogs 10,301. | data/verified_summary.json |
| Ted most-voted Other, about 723k | PASS | 722,549, rounds to 723,000. | data/films_expanded.csv |
| All four labelled Other films feature his voice | PASS | Agency CV: Earth narrator, Ted narrator, Plague Dogs Major voice, Nausicaä Lord Yupa voice; GKIDS lists English cast. | https://www.independenttalent.com/actors/patrick-stewart/ ; https://gkids.com/films/nausicaa-of-the-valley-of-the-wind/ |
| 1940–2026 tribute | PASS | RSC confirms born 1940 and death. Original requested date 30 Oct was incorrect: reported death Wed 28 Oct, announcement 29 Oct. Draft does not print a day. | https://www.rsc.org.uk/news/in-tribute-to-rsc-honorary-associate-artist-sir-patrick-stewart ; https://www.itv.com/news/2026-10-29/patrick-stewart-dies-at-86 |
| Stage chart additional dates: Christmas Carol 1991; Picard 2020 | PASS | IBDB opening 19 Dec 1991; official series release record 2020. | https://www.ibdb.com/broadway-production/a-christmas-carol-4655 ; https://www.startrek.com/shows/star-trek-picard |
| Ratings/votes represent films and all versions | PASS / scope limit | IMDb definition: averageRating weighted average; numVotes title total. Dataset is a documented selection, not complete filmography. Missing values retained as missing. | https://data.imdb.com/non-commercial-datasets/ |

The article now describes a genuine top 25, rather than top 15 plus selected Picard films. It specifies Stewart’s Hamlet roles. All dynamic IMDb values refer to the saved snapshot, not a claim about permanently current ratings.
