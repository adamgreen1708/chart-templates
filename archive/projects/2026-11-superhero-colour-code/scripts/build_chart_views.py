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


# Story v2: richer, fully data-driven colour fingerprints and moral-colour pairings.
# These are editorially selected examples, not a population sample.
COSTUME_SWATCHES={
    "red":"#C44E52","blue":"#1F8FA8","yellow":"#E2B221","green":"#2F9568",
    "purple":"#8756A5","orange":"#E38A3E","black":"#252931","grey":"#727880",
    "white":"#FFFFFF","gold":"#C59B32","silver":"#BCC1C7"
}
SHORT_NAMES={
    "Superman":"Superman","Batman (Bruce Wayne)":"Batman",
    "Wonder Woman (Diana)":"Wonder Woman","The Flash (Barry Allen)":"The Flash",
    "Green Lantern (Hal Jordan)":"Green Lantern","Aquaman (Arthur Curry)":"Aquaman",
    "The Joker":"The Joker","Riddler (Edward Nygma)":"The Riddler",
    "Sinestro (Thaal Sinestro)":"Sinestro","Poison Ivy (Pamela Isley)":"Poison Ivy",
    "Lex Luthor":"Lex Luthor","Black Manta":"Black Manta",
    "Spider-Man (Peter Parker)":"Spider-Man","Iron Man (Tony Stark)":"Iron Man",
    "Captain America (Steve Rogers)":"Captain America","Wolverine (Logan)":"Wolverine",
    "Black Panther (T'Challa)":"Black Panther","Daredevil (Matt Murdock)":"Daredevil",
    "Green Goblin (Norman Osborn)":"Green Goblin","Doctor Doom (Victor von Doom)":"Doctor Doom",
    "Loki (Laufeyson)":"Loki","Thanos":"Thanos","Venom (Eddie Brock)":"Venom",
    "Magneto (Max Eisenhardt)":"Magneto"
}
GALLERY_HEROES=(
    "Superman","The Flash (Barry Allen)","Green Lantern (Hal Jordan)",
    "Spider-Man (Peter Parker)","Wolverine (Logan)","Iron Man (Tony Stark)"
)
GALLERY_VILLAINS=(
    "The Joker","Riddler (Edward Nygma)","Lex Luthor",
    "Green Goblin (Norman Osborn)","Doctor Doom (Victor von Doom)",
    "Magneto (Max Eisenhardt)"
)
COLOUR_TWINS=(
    ("The Flash (Barry Allen)","Magneto (Max Eisenhardt)"),
    ("Superman","Thanos"),
    ("Wolverine (Logan)","Sinestro (Thaal Sinestro)"),
    ("Green Lantern (Hal Jordan)","Green Goblin (Norman Osborn)"),
    ("Black Panther (T'Challa)","Venom (Eddie Brock)")
)

def build_palette_story_v2(rows,out):
    byname={r["character"]:r for r in rows}
    assert len(SHORT_NAMES)==len(byname) and set(SHORT_NAMES)==set(byname)
    def get(name):
        if name not in byname: raise ValueError(f"Missing selected costume: {name}")
        return byname[name]
    def hex_for(colour):
        if not colour: return ""
        if colour not in COSTUME_SWATCHES: raise ValueError(f"Unsupported swatch: {colour}")
        return COSTUME_SWATCHES[colour]
    def accent(r):
        return str(r["accent_colours"]).split(",")[0].strip()
    gallery=[]
    for role, names in (("Hero",GALLERY_HEROES),("Villain",GALLERY_VILLAINS)):
        assert len(names)==6
        for ix,name in enumerate(names,1):
            r=get(name)
            assert r["role"]==role
            main=r["dominant_colour"];second=r["second_major_colour"];third=accent(r)
            gallery.append(dict(character=name,display=SHORT_NAMES[name],
                publisher=r["publisher"],role=role,sort_order=ix,
                dominant_colour=main,secondary_colour=second,accent_colour=third,
                dominant_hex=hex_for(main),secondary_hex=hex_for(second),
                accent_hex=hex_for(third)))
    write_csv(out/"chart_v2_01_costume_gallery.csv",[
        "character","display","publisher","role","sort_order",
        "dominant_colour","secondary_colour","accent_colour",
        "dominant_hex","secondary_hex","accent_hex"],gallery)

    selected=[]
    for role in ROLES:
        for publisher in PUBLISHERS:
            grp=[r for r in rows if r["role"]==role and r["publisher"]==publisher]
            grp=sorted(grp,key=lambda r:(r["dominant_colour"] not in PRIMARY,
                                       SHORT_NAMES[r["character"]].lower()))
            assert len(grp)==6
            for index,r in enumerate(grp,1):
                selected.append(dict(character=r["character"],
                    display=SHORT_NAMES[r["character"]],
                    publisher=publisher,role=role,
                    group=f"{publisher} {'heroes' if role=='Hero' else 'villains'}",
                    dominant_colour=r["dominant_colour"],
                    dominant_hex=hex_for(r["dominant_colour"]),
                    primary_flag=int(r["dominant_colour"] in PRIMARY),
                    tile_index=index,role_total=12))
    write_csv(out/"chart_v2_02_role_scorecard.csv",[
        "character","display","publisher","role","group",
        "dominant_colour","dominant_hex","primary_flag","tile_index","role_total"
    ],selected)

    pairs=[]
    for ix,(hero,villain) in enumerate(COLOUR_TWINS,1):
        h=get(hero);v=get(villain)
        if h["role"]!="Hero" or v["role"]!="Villain" or h["dominant_colour"]!=v["dominant_colour"]:
            raise ValueError(f"Not a documented colour twin: {hero} / {villain}")
        colour=h["dominant_colour"]
        pairs.append(dict(pair_rank=ix,shared_colour=colour,
            shared_hex=hex_for(colour),
            hero_character=hero,hero_display=SHORT_NAMES[hero],
            hero_publisher=h["publisher"],hero_secondary=h["second_major_colour"],
            hero_secondary_hex=hex_for(h["second_major_colour"]),
            villain_character=villain,villain_display=SHORT_NAMES[villain],
            villain_publisher=v["publisher"],villain_secondary=v["second_major_colour"],
            villain_secondary_hex=hex_for(v["second_major_colour"])))
    write_csv(out/"chart_v2_03_colour_twins.csv",[
        "pair_rank","shared_colour","shared_hex",
        "hero_character","hero_display","hero_publisher",
        "hero_secondary","hero_secondary_hex",
        "villain_character","villain_display","villain_publisher",
        "villain_secondary","villain_secondary_hex"],pairs)
    print("Story v2 views: 12 gallery records, 24 scorecard tiles, 5 matched colour twins")

def main():
    rows=read_rows()
    out=ROOT/"data"
    build_palette_story_v2(rows,out)
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
    # Seven named primary-rule exceptions, with costume-hue swatches and two columns.
    # All marks come from the verified seed CSV; this view is still provisional.
    short_names={
        "Batman (Bruce Wayne)":"Batman",
        "Green Lantern (Hal Jordan)":"Green Lantern",
        "Aquaman (Arthur Curry)":"Aquaman",
        "Black Panther (T'Challa)":"Black Panther",
        "Sinestro (Thaal Sinestro)":"Sinestro",
        "Thanos":"Thanos",
        "Magneto (Max Eisenhardt)":"Magneto",
    }
    hues={"grey":"#626A72","green":"#2D9067","orange":"#D4863F",
          "yellow":"#D4A017","black":"#272A31","blue":"#1F8FA8","red":"#C44E52"}
    ordered_names=list(short_names)
    exceptions_by_name={r["character"]:r for r in exceptions}
    assert len(exceptions_by_name)==7, "Unexpected count of exception marks"
    exception_marks=[]
    for index,name in enumerate(ordered_names,1):
        if name not in exceptions_by_name:
            raise ValueError(f"Missing exception: {name}")
        r=exceptions_by_name[name]
        hue=r["dominant_colour"]
        exception_marks.append(dict(character=name,short_label=f"{short_names[name]} · {hue}",
            role=r["role"],publisher=r["publisher"],dominant_colour=hue,
            x_position=-1 if r["role"]=="Hero" else 1,display_order=index,colour_hex=hues[hue]))
    write_csv(out/"chart_03_exception_marks.csv",
        ["character","short_label","role","publisher","dominant_colour",
         "x_position","display_order","colour_hex"],exception_marks)
    # Six-row diverging hue comparison: positive = more frequent among heroes.
    palette={"red":"#C44E52","blue":"#1F8FA8","yellow":"#D4A017","green":"#2D9067","purple":"#8654A8","orange":"#D4863F"}
    frequency={(r["role"],r["colour"]):r for r in freq}
    differences=[]
    for colour in ("red","blue","yellow","green","purple","orange"):
        hero=frequency[("Hero",colour)]
        villain=frequency[("Villain",colour)]
        diff=round(100*(hero["n_characters"]-villain["n_characters"])/12,1)
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
