"""Regenerate the compact cast index beneath chart 2 from the project scorecard CSV.

This is a deterministic Markdown reference, not a change to the chart encoding.
Run from repository root or any working directory:
  python archive/projects/2026-11-superhero-colour-code/scripts/build_blog_draft_v3.py
"""
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCORECARD=ROOT/"data/chart_v2_02_role_scorecard.csv"
TEMPLATE=ROOT/"content/blog_draft_v3.template.md"
OUTPUT=ROOT/"content/blog_draft_v3.md"
PRIMARIES={"red","yellow","blue"}

def create_table(records):
    if len(records)!=24:
        raise ValueError(f"Expected 24 character observations, got {len(records)}")
    indexed={}
    for role in ("Hero","Villain"):
        for publisher in ("DC","Marvel"):
            group=sorted((r for r in records if r["role"]==role and r["publisher"]==publisher),
                         key=lambda r:int(r["tile_index"]))
            if len(group)!=6 or [int(r["tile_index"]) for r in group]!=list(range(1,7)):
                raise ValueError(f"Invalid wheel order/cohort: {publisher} {role}")
            indexed[(role,publisher)]=group
    assert len({(r["publisher"],r["character"]) for r in records})==24
    def show(r):
        if r["dominant_colour"] in PRIMARIES:
            hue=f'**{r["dominant_colour"]}**'
        else:
            hue=r["dominant_colour"]
        if "|" in r["display"] or "|" in hue:
            raise ValueError("Unsupported Markdown pipe in character/hue")
        return f'{r["display"]} · {hue}'
    output=["| Role | DC character · main hue | Marvel character · main hue |",
            "|:--|:--|:--|"]
    for role in ("Hero","Villain"):
        for i in range(6):
            output.append(f'| {role} | {show(indexed[(role,"DC")][i])} | {show(indexed[(role,"Marvel")][i])} |')
    return "\n".join(output)

def render():
    with SCORECARD.open(encoding="utf-8",newline="") as fp:
        records=list(csv.DictReader(fp))
    template=TEMPLATE.read_text(encoding="utf-8")
    if template.count("{{CAST_TABLE}}")!=1:
        raise ValueError("The blog template must have one CAST_TABLE marker")
    return template.replace("{{CAST_TABLE}}",create_table(records))

def main():
    body=render()
    OUTPUT.write_text(body,encoding="utf-8")
    print(f"Updated {OUTPUT}; 24 characters in 12 compact data-driven table rows")

if __name__=="__main__":
    main()
