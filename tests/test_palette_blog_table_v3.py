"""Keep the supporting blog table exactly aligned with the colour wheels."""
import sys
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/"archive/projects/2026-11-superhero-colour-code"
sys.path.insert(0,str(PROJECT/"scripts"))
from build_blog_draft_v3 import render,create_table,OUTPUT,SCORECARD

def test_table_has_every_character_and_matches_published_draft():
    with SCORECARD.open(encoding="utf-8",newline="") as f:
        records=list(csv.DictReader(f))
    table=create_table(records)
    assert len(table.splitlines())==14  # header + delimiter + 12 body rows
    assert sum("| Hero |" in line for line in table.splitlines())==6
    assert sum("| Villain |" in line for line in table.splitlines())==6
    for r in records:
        assert r["display"]+" · " in table
    body=OUTPUT.read_text(encoding="utf-8")
    assert body==render(), "Regenerate blog draft from its template and latest scorecard"
    assert table in body
    assert "../output/superhero_v3_02_colour_wheels.png" in body
    assert "../output/superhero_v3_03_showdowns.png" in body
    assert "not hero–villain match-ups" in body
