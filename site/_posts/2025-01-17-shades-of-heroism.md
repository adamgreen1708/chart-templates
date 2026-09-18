---
title: "Shades of Heroism"
date: 2025-01-17 00:13:00+00:00
slug: shades-of-heroism
permalink: /2025/01/17/shades-of-heroism/
description: "Interactive Viz Link The viz Shades of Heroism: The colour code of courage is a quick and simple visualisation looking at 20 movies named after their hero, ordered by IMDb rating along with their approximate primary HEX codes and costume…"
category: Culture
read_time: 4 minute read
card_image: /assets/migrated/shades-of-heroism/feature.png
hero_image: /assets/migrated/shades-of-heroism/feature.png
hero_alt: "Feature image for Shades of Heroism."
legacy_url: https://coffeetableviz.wordpress.com/2025/01/17/shades-of-heroism/
---

<p><a href="https://public.tableau.com/views/Shadesofheroism/shadesofheroism?:language=en-GB&amp;:sid=&amp;:redirect=auth&amp;:display_count=n&amp;:origin=viz_share_link" target="_blank" rel="noreferrer noopener">Interactive Viz Link</a></p>

<h2>The viz</h2>

<p><strong>Shades of Heroism: The colour code of courage</strong> is a quick and simple visualisation looking at 20 movies named after their hero, ordered by IMDb rating along with their approximate primary HEX codes and costume colour proportions.</p>

<h2>What Inspired the Viz</h2>

<p>Looking for inspiration for my next mini viz project I stumbled upon Tim Leongs fun infographic entitled: Good Measures, Superheroes and Primary Colours, depicting superhero’s costume colour ratio in the fantastic book named “Super Graphics”.</p>

<p>Good Measures, Superheroes 🦸‍♂️🦸‍♀️and Primary Colours 🔴🟡🔵 &#8211; Tim Leongs</p>

<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/img_6033.jpg" alt="img 6033" loading="lazy"></figure>

<h2>How did I approach the project</h2>

<p>I challenged myself to use ChatGPT (4o) to give me the data of <strong>20 movies named after their hero’s namesake, add in the IMDb rating, present the costumes HEX colour and approximate proportions in an exportable csv format</strong> ready for use in tableau. &#8211; so forgive me for any inaccuracies in colours, proportions or up to date IMDb ratings in the viz 🥺</p>

<p>When I prompted ChatGPT to provide me with sources and confidence in the data, here is the response:</p>

<pre>The superhero color proportions in the table were derived based on observational analysis of prominent superhero costumes across their most iconic film appearances, as described in movie visuals, posters, and promotional material. These were then approximated into percentages to reflect the dominant, secondary, and accent colors used for each character.<br /><br />The proportions are not sourced from any specific published dataset but are instead approximations intended to highlight general trends in superhero costume design. For further validation or refinement, you could cross-reference with official costume designs or visual studies of superhero media. Let me know if you’d like assistance in sourcing or verifying these proportions more rigorously!<br /><br />How confident are you in the accuracy?<br /><br />I am moderately confident about the hex codes and proportions, but they should be considered approximations rather than precise data.</pre>

<p>I challenged ChatGPT to come up with a witty title for the visualisation “Shades of Heroism: The colour code of courage” here some of my rejected but highly amusing titles: 😏</p>

<pre>1.”Shades of Heroism: The Color Code of Courage”<br />2.”Hue’s the Hero? A Palette of Power”<br />3.”Chromatic Justice: The Colors Behind the Cape”<br />4.”Superhero Spectrum: What Colors Say About Power”<br />5.”Bold, Bright, and Fearless: A Hero’s Palette”<br />6.”Hues of Heroics: The Psychology of Superhero Colors”<br />7.”Masked in Color: The Story Behind the Shades”<br />8.”The Super Color Spectrum: Power in Proportions”<br />9.”Hue-manity’s Heroes: The Science of Their Shades”<br />10.”Color Me Super: Decoding the Hero Palette”</pre>

<p>I asked ChatGPT to come up with the summary takeaway from the data table created:</p>

<pre>Superhero costumes use bold, primary colors like red, blue, and yellow to symbolize traits such as energy, trust, and hope, while darker tones like black and gray convey mystery and complexity. Bright colors dominate for inspiring, approachable heroes, while dark palettes highlight moral ambiguity and power. Gold, yellow, and white are often accents to signal virtue and triumph. Proportions balance a dominant color (60-90%) with minor highlights, ensuring each hero is visually distinct, emotionally resonant, and thematically aligned with their narrative.</pre>

<p>I also asked ChatGPT to visualise the data, add the title and takeaway summary, after circa 10 iterations I managed to get this visual:</p>

<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/img_6040-1.png" alt="img 6040 1" loading="lazy"></figure>

<p>I further prompted ChatGPT for a more creative approach to visualising the data</p>

<figure class="image-grid">
<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/img_6041-1.png" alt="img 6041 1" loading="lazy"></figure>

<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/img_6044-1.png" alt="img 6044 1" loading="lazy"></figure>

<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/img_6042-1.png" alt="img 6042 1" loading="lazy"></figure>

<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/img_6043-1.png" alt="img 6043 1" loading="lazy"></figure>
</figure>

<h2>My viz</h2>

<p>Not totally convinced with ChatGPTs output I set loading the data into Tableau.</p>

<p>My recreation of Tim Leongs viz with my own dataset.</p>

<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/image001-3-1.png" alt="image001 3 1" loading="lazy"></figure>

<p>And my final viz in my own style with ChatGPT prompt title and takeaway text.</p>

<figure class="story-chart full-bleed"><img src="/assets/migrated/shades-of-heroism/img_6038-3-1.png" alt="img 6038 3 1" loading="lazy"></figure>

<h2>Overall Faff-Ometer</h2>

<p>■ / ■■■■■</p>

<p>Trying to get ChatGPT to visualise</p>

<p>■■■■ / ■■■■■</p>

<h2>Data Sources</h2>

<ul>
<li>ChatGPT</li>
</ul>

<h2>TLDR</h2>

<p>ChatGPT saved me a ton of time sourcing and blending data sources. Can pull me a no prep, no hassle data source (with passable accuracy), generate witty titles for the viz and generate a summary takeaway paragraph to complement the viz.</p>

<p>What it couldn’t do is come up with any decent visuals of this data. So what’s my takeaway: a superb copilot, but I believe my human viz role is safe! (for the moment).</p>

<p>Thanks for reading, ping me if you have any questions or thoughts about my viz.</p>

<p>Adam</p>

<p>Powered by 🖤 with a helping hand from ChatGPT</p>
