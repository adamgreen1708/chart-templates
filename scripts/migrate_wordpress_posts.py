#!/usr/bin/env python3
"""Migrate selected public WordPress.com posts into the Jekyll site.

The script reads WordPress REST API JSON files, localises the featured and
inline images, and writes posts that retain the original URL paths. It is kept
deliberately dependency-free so future archive batches can use it unchanged.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import re
import shutil
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path


CATEGORIES = {
    "the-story-to-glory-a-22-year-wait": "Sport",
    "the-worlds-highest-paid-athletes": "Sport",
    "the-wee-dram-a-small-sip-with-lingering-notes": "Culture",
    "forbes-most-valuable-sports-teams": "Sport",
    "more-articles-are-now-created-by-ai-than-humans": "Technology",
    "the-uks-hottest-years-are-also-shining-through": "Climate",
    "the-uks-rapeseed-rollercoaster": "Environment",
    "how-is-war-shaping-fuel-prices": "Economy",
    "table-vs-viz-a-delicate-dance-in-the-grand-data-opera": "Design",
    "zero-the-rarest-number-in-football": "Sport",
    "sinner-vs-alcaraz-wimbledon-2025-a-triangle-tale": "Sport",
    "who-rules-the-road": "Sport",
    "shades-of-heroism": "Culture",
    "creating-for-fun": "Design",
    "how-to-find-stories-in-data-channelling-our-inner-journo": "Storytelling",
    "colour-bank-no-6-tom-hanks-filmography": "Culture",
}


def plain_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(html.unescape(value))).strip()


def description_for(post: dict) -> str:
    source = plain_text(post.get("excerpt", ""))
    if not source:
        match = re.search(r"<p[^>]*>(.*?)</p>", post["content"], re.I | re.S)
        source = plain_text(match.group(1)) if match else plain_text(post["content"])
    if len(source) <= 240:
        return source
    clipped = source[:240].rsplit(" ", 1)[0]
    return clipped.rstrip(" ,;:") + "…"


def safe_filename(url: str, fallback: str) -> str:
    name = Path(urllib.parse.urlparse(html.unescape(url)).path).name or fallback
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-").lower()
    return name or fallback


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        return
    request = urllib.request.Request(html.unescape(url), headers={"User-Agent": "coffeetableviz-migrator/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response, destination.open("wb") as output:
        shutil.copyfileobj(response, output)


def unique_destination(directory: Path, name: str, used: set[str]) -> Path:
    stem, suffix = Path(name).stem, Path(name).suffix
    candidate = name
    counter = 2
    while candidate in used:
        candidate = f"{stem}-{counter}{suffix}"
        counter += 1
    used.add(candidate)
    return directory / candidate


def clean_content(post: dict, asset_directory: Path, public_directory: str) -> str:
    content = post["content"]
    used: set[str] = set()

    def replace_image(match: re.Match[str]) -> str:
        attributes = match.group(0)
        source_match = re.search(r'data-large-file="([^"]+)"', attributes, re.I)
        if not source_match:
            source_match = re.search(r'data-orig-file="([^"]+)"', attributes, re.I)
        if not source_match:
            source_match = re.search(r'src="([^"]+)"', attributes, re.I)
        if not source_match:
            return ""
        source = html.unescape(source_match.group(1))
        filename = safe_filename(source, "image.png")
        destination = unique_destination(asset_directory, filename, used)
        download(source, destination)
        alt_match = re.search(r'alt="([^"]*)"', attributes, re.I)
        title_match = re.search(r'data-image-title="([^"]*)"', attributes, re.I)
        alt = plain_text(alt_match.group(1)) if alt_match and alt_match.group(1) else ""
        if not alt and title_match:
            alt = plain_text(title_match.group(1)).replace("_", " ").replace("-", " ")
        if not alt:
            alt = f"Visual from {html.unescape(post['title'])}"
        return f'<img src="/{public_directory}/{destination.name}" alt="{html.escape(alt, quote=True)}" loading="lazy">'

    content = re.sub(r"<img\b[^>]*>", replace_image, content, flags=re.I)
    def replace_figure(match: re.Match[str]) -> str:
        if "wp-block-gallery" in match.group(0):
            return '<figure class="image-grid">'
        return '<figure class="story-chart full-bleed">'

    content = re.sub(r'<figure\b[^>]*>', replace_figure, content, flags=re.I)
    content = re.sub(r'<figcaption\b[^>]*>', '<figcaption>', content, flags=re.I)
    content = re.sub(
        r'\sclass="(?!image-grid|story-chart full-bleed)[^"]*"',
        "",
        content,
    )
    content = re.sub(r'\sstyle="[^"]*"', "", content)
    content = re.sub(r"\n{3,}", "\n\n", content).strip()
    return content


def yaml_string(value: str) -> str:
    return json.dumps(html.unescape(value), ensure_ascii=False)


def migrate(json_path: Path, site_root: Path) -> tuple[Path, int]:
    post = json.loads(json_path.read_text(encoding="utf-8"))
    slug = post["slug"]
    date = post["date"]
    day = date[:10]
    asset_directory = site_root / "assets" / "migrated" / slug
    public_directory = f"assets/migrated/{slug}"
    asset_directory.mkdir(parents=True, exist_ok=True)

    featured = post.get("featured_image", "")
    hero_path = ""
    if featured:
        feature_name = safe_filename(featured, "feature.png")
        suffix = Path(feature_name).suffix or ".png"
        feature_destination = asset_directory / f"feature{suffix}"
        download(featured, feature_destination)
        if feature_destination.stat().st_size > 750_000 and shutil.which("convert"):
            optimised_destination = asset_directory / "feature.webp"
            subprocess.run(
                [
                    "convert",
                    str(feature_destination),
                    "-resize",
                    "1600x1600>",
                    "-strip",
                    "-quality",
                    "84",
                    str(optimised_destination),
                ],
                check=True,
            )
            feature_destination.unlink()
        hero_path = f"/{public_directory}/{feature_destination.name}"
        if not feature_destination.exists():
            feature_destination = asset_directory / "feature.webp"
            hero_path = f"/{public_directory}/{feature_destination.name}"

    body = clean_content(post, asset_directory, public_directory)
    word_count = len(re.findall(r"\b[\w’'-]+\b", plain_text(body)))
    read_time = max(2, math.ceil(word_count / 220))
    title = html.unescape(post["title"])
    lines = [
        "---",
        f"title: {yaml_string(title)}",
        f"date: {date.replace('T', ' ')}",
        f"slug: {slug}",
        f"permalink: /{day.replace('-', '/')}/{slug}/",
        f"description: {yaml_string(description_for(post))}",
        f"category: {CATEGORIES.get(slug, 'Data story')}",
        f"read_time: {read_time} minute read",
    ]
    if hero_path:
        lines.extend(
            [
                f"card_image: {hero_path}",
                f"hero_image: {hero_path}",
                f"hero_alt: {yaml_string('Feature image for ' + title + '.')}",
            ]
        )
    lines.extend([f"legacy_url: {post['URL']}", "---", "", body, ""])
    output = site_root / "_posts" / f"{day}-{slug}.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    return output, len(list(asset_directory.iterdir()))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_directory", type=Path)
    parser.add_argument("site_root", type=Path)
    parser.add_argument("slugs", nargs="+")
    args = parser.parse_args()
    for slug in args.slugs:
        output, asset_count = migrate(args.json_directory / f"{slug}.json", args.site_root)
        print(f"{output.name}: {asset_count} assets")


if __name__ == "__main__":
    main()
