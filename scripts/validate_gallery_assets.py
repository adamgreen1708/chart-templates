"""Fail publication if gallery media referenced by an exhibit is missing or changed."""
from pathlib import Path
import argparse
import hashlib
import re

def require(condition, message):
    if not condition:
        raise SystemExit(message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

parser = argparse.ArgumentParser()
parser.add_argument("--built", type=Path)
args = parser.parse_args()
site = Path("site")
pages = list((site / "gallery").rglob("*.html"))
require(bool(pages), "Gallery pages missing")
pattern = re.compile(r"/assets/gallery/[A-Za-z0-9_./-]+")
referenced = set()
for page in pages:
    for match in pattern.findall(page.read_text(encoding="utf-8")):
        path = site / match.lstrip("/")
        require(path.is_file() and path.stat().st_size > 0, f"{page}: missing {path}")
        referenced.add(path)
    if args.built and page.name == "index.html":
        output = args.built / page.relative_to(site)
        require(output.is_file() and output.stat().st_size > 0, f"Missing built page: {output}")

approved = {}
for manifest in sorted(Path("archive/projects").glob("*/ASSETS.sha256")):
    if manifest.parent.name == "2026-11-interwoven":
        continue  # Existing original/recovery validation remains in publish-blog.yml.
    for line in manifest.read_text().splitlines():
        fields = line.split(maxsplit=1)
        if len(fields) != 2:
            continue
        expected, name = fields
        path = Path(name.lstrip("*"))
        if not path.as_posix().startswith("site/assets/gallery/"):
            continue
        require(re.fullmatch(r"[0-9a-f]{64}", expected), f"Invalid checksum: {manifest}")
        require(path not in approved or approved[path] == expected, f"Conflicting checksum: {path}")
        approved[path] = expected

for path in referenced:
    if path.parts[3] != "interwoven":
        require(path in approved, f"Missing approved checksum: {path}")
for path, expected in approved.items():
    require(path.is_file() and digest(path) == expected, f"Approved media missing or changed: {path}")
for path in referenced | set(approved):
    if args.built:
        output = args.built / path.relative_to(site)
        require(output.is_file() and digest(output) == digest(path), f"Built media missing or changed: {output}")
print(f"Gallery validation passed: {len(referenced)} references, {len(approved)} approved media files.")
