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
            pub_view.append(dict(publisher=publisher,role=role,chart_label=f"{publisher} {'heroes' if role == 'Hero' else 'villains'}",n_primary_dominant=n,n_in_group=len(subset),share_percent=round(100*n/len(subset),1)))
    write_csv(out/"chart_02_primary_by_publisher.csv",["publisher","role","chart_label","n_primary_dominant","n_in_group","share_percent"],pub_view)
    exceptions=[]
    for r in rows:
        is_primary=r["dominant_colour"] in PRIMARY
        if (r["role"]=="Hero" and not is_primary) or (r["role"]=="Villain" and is_primary):
            exceptions.append(dict(character=r["character"],publisher=r["publisher"],role=r["role"],dominant_colour=r["dominant_colour"],chart_label=f'{r["character"]} ({r["publisher"]})',primary_dominant=int(is_primary),exception_type="Hero without primary dominant" if r["role"]=="Hero" else "Villain with primary dominant"))
    write_csv(out/"chart_03_exceptions.csv",["character","publisher","role","dominant_colour","chart_label","primary_dominant","exception_type"],exceptions)
    # Six-row diverging hue comparison: positive = more frequent among heroes.
    palette={"red":"#C44E52","blue":"#1F8FA8","yellow":"#D4A017","green":"#2D9067","purple":"#8654A8","orange":"#D4863F"}
    frequency={(r["role"],r["colour"]):r for r in freq}
    differences=[]
    for colour in ("red","blue","yellow","green","purple","orange"):
        hero=frequency[("Hero",colour)]
        villain=frequency[("Villain",colour)]
        diff=round(hero["share_percent"]-villain["share_percent"],1)
        differences.append(dict(colour=colour,display_label=colour.title(),
            hero_count=hero["n_characters"],villain_count=villain["n_characters"],
            hero_pct=hero["share_percent"],villain_pct=villain["share_percent"],
            hero_minus_villain_pct=diff,role_skew="heroes" if diff>0 else "villains" if diff<0 else "equal",
            colour_hex=palette[colour]))
    differences.sort(key=lambda r:r["hero_minus_villain_pct"],reverse=True)
    write_csv(out/"chart_01_hue_skew.csv",["colour","display_label","hero_count","villain_count","hero_pct","villain_pct","hero_minus_villain_pct","role_skew","colour_hex"],differences)
    # Publisher-text-supported uncertainties: possible costume/era variants, NOT measured areas.
    with (ROOT/"data/colour_coding_alternatives.csv").open(encoding="utf-8",newline="") as fh:
        alternatives=list(csv.DictReader(fh))
    assert len(alternatives)==5, "Keep the manually curated sensitivity cases explicit"
    by_character={r["character"]:r for r in rows}
    alt={}
    for r in alternatives:
        assert r["character"] in by_character, f"Unknown alternative {r['character']}"
        assert by_character[r["character"]]["dominant_colour"]==r["current_dominant"]
        assert r["alternate_dominant"] in ALLOWED
        alt[r["character"]]=r["alternate_dominant"]
    bounds=[]
    for role in ROLES:
        subset=[r for r in rows if r["role"]==role]
        base=sum(r["dominant_colour"] in PRIMARY for r in subset)
        minimum=sum((r["dominant_colour"] in PRIMARY) and (r["character"] not in alt or alt[r["character"]] in PRIMARY) for r in subset)
        maximum=sum((r["dominant_colour"] in PRIMARY) or (r["character"] in alt and alt[r["character"]] in PRIMARY) for r in subset)
        n=len(subset)
        bounds.append(dict(role=role,n_characters=n,baseline_primary=base,low_primary=minimum,high_primary=maximum,baseline_pct=round(100*base/n,1),low_pct=round(100*minimum/n,1),high_pct=round(100*maximum/n,1)))
    write_csv(out/"chart_coding_sensitivity.csv",["role","n_characters","baseline_primary","low_primary","high_primary","baseline_pct","low_pct","high_pct"],bounds)
    assert bounds[0]["low_primary"]>bounds[1]["high_primary"], "Pilot difference is not robust to documented alternatives"
    print(f"Pilot records: {len(rows)}; exceptions: {len(exceptions)}")
    print("Provisional only: costume-image validation is required before publication")

if __name__=="__main__":
    main()
