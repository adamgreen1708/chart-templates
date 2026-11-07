"""Build provisional three-chart views from the hand-coded comic costume seed.
Run from repository root: python archive/projects/2026-11-superhero-colour-code/scripts/build_chart_views.py
No external packages or inferred costume percentages.
"""
import csv
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"data/character_palette_seed.csv"
PRIMARY={"red","blue","yellow"}
SECONDARY={"green","purple","orange"}
ALLOWED=PRIMARY|SECONDARY|{"black","white","grey","silver","gold"}
ROLES=("Hero","Villain")
PUBLISHERS=("DC","Marvel")

def read_rows():
    with SOURCE.open(encoding="utf-8",newline="") as fh:
        records=list(csv.DictReader(fh))
    assert len(records)==24, f"Expected 24 pilot rows, got {len(records)}"
    keys=[(r["publisher"],r["character"]) for r in records]
    assert len(keys)==len(set(keys)), "Duplicate publisher/character"
    for row in records:
        assert row["dominant_colour"] in ALLOWED, row
        assert row["source_url"].startswith("https://"), row
    for pub in PUBLISHERS:
        for role in ROLES:
            assert sum(r["publisher"]==pub and r["role"]==role for r in records)==6
    return records

def write_csv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as fh:
        writer=csv.DictWriter(fh,fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def main():
    rows=read_rows()
    out=ROOT/"data"
    freq=[]
    for role in ROLES:
        subset=[r for r in rows if r["role"]==role]
        counts=Counter(r["dominant_colour"] for r in subset)
        for colour in ("red","blue","yellow","green","purple","orange"):
            n=counts[colour]
            freq.append(dict(role=role,colour=colour,chart_label=f"{role} · {colour}",n_characters=n,n_in_role=len(subset),share_percent=round(100*n/len(subset),1)))
    write_csv(out/"chart_01_colour_frequency.csv",["role","colour","chart_label","n_characters","n_in_role","share_percent"],freq)
    pub_view=[]
    for publisher in PUBLISHERS:
        for role in ROLES:
            subset=[r for r in rows if r["publisher"]==publisher and r["role"]==role]
            n=sum(r["dominant_colour"] in PRIMARY for r in subset)
            pub_view.append(dict(publisher=publisher,role=role,chart_label=f"{publisher} {role.lower()}s",n_primary_dominant=n,n_in_group=len(subset),share_percent=round(100*n/len(subset),1)))
    write_csv(out/"chart_02_primary_by_publisher.csv",["publisher","role","chart_label","n_primary_dominant","n_in_group","share_percent"],pub_view)
    exceptions=[]
    for r in rows:
        is_primary=r["dominant_colour"] in PRIMARY
        if (r["role"]=="Hero" and not is_primary) or (r["role"]=="Villain" and is_primary):
            exceptions.append(dict(character=r["character"],publisher=r["publisher"],role=r["role"],dominant_colour=r["dominant_colour"],chart_label=f'{r["character"]} ({r["publisher"]})',primary_dominant=int(is_primary),exception_type="Hero without primary dominant" if r["role"]=="Hero" else "Villain with primary dominant"))
    write_csv(out/"chart_03_exceptions.csv",["character","publisher","role","dominant_colour","chart_label","primary_dominant","exception_type"],exceptions)
    print(f"Pilot records: {len(rows)}; exceptions: {len(exceptions)}")
    print("Provisional only: costume-image validation is required before publication")

if __name__=="__main__":
    main()
