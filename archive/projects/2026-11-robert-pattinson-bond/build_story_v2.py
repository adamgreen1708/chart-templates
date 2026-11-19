#!/usr/bin/env python3
"""Prepare *auditable* editorial v2 data from the frozen IMDb research extract.

All numerical displays come from exported IMDb rows, never mocked values.
The only manual lookup is a source-linked Bond character attribution table.
"""
from __future__ import annotations

import csv
import json
import math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERATED = HERE / "generated"
AUDITED = HERE / "data" / "bond_roles_verified.csv"

def read(name, base=GENERATED):
    with (base / name).open(encoding="utf-8", newline="") as fp:
        return list(csv.DictReader(fp))

def write(name, rows, fields):
    with (GENERATED / name).open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=fields, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)

def is_twilight(title):
    return title == "Twilight" or title.startswith("The Twilight Saga:")

def main():
    films = read("chart_01_film_rating_timeline.csv")
    bonds = read("chart_03_official_bond_connections.csv")
    bond_register = read("bond_films.csv")
    roles = read("bond_roles_verified.csv", base=HERE / "data")
    metadata = json.loads((GENERATED / "metadata.json").read_text(encoding="utf-8"))
    if metadata["editorial_as_of"] != "2026-11-18":
        raise ValueError("Frozen IMDb research version changed: editorial revalidation required")
    if len(films) != 33 or len({r["tconst"] for r in films}) != 33:
        raise ValueError("Expected 33 distinct released/rated Pattinson films")
    if len(bond_register) != 27 or Counter(r["bond_series"] for r in bond_register) != {"eon":25,"non_eon":2}:
        raise ValueError("Bond film register coverage changed")
    if any(r.get("rating", "") == "" or int(r["num_votes"]) <= 0 for r in films):
        raise ValueError("Missing rated-film row or vote count")

    twilight = [r for r in films if is_twilight(r["title"])]
    other = [r for r in films if not is_twilight(r["title"])]
    if len(twilight) != 5 or len(other) != 28 or len({r["year"] for r in twilight}) != 5:
        raise ValueError("Twilight group does not cover exactly five titles across five years")

    def median(data):
        scores = sorted(float(r["rating"]) for r in data)
        n = len(scores)
        return (scores[n//2] if n%2 else (scores[n//2-1]+scores[n//2])/2)

    votes_twilight = sum(int(r["num_votes"]) for r in twilight)
    votes_total = sum(int(r["num_votes"]) for r in films)
    twilight_med, other_med = median(twilight), median(other)
    if not (votes_twilight < votes_total and 0 < twilight_med < other_med <= 10):
        raise ValueError("Unexpected Twilight comparison")

    short = {
        "Twilight": "Twilight",
        "The Twilight Saga: New Moon": "New Moon",
        "The Twilight Saga: Eclipse": "Eclipse",
        "The Twilight Saga: Breaking Dawn - Part 1": "Breaking Dawn 1",
        "The Twilight Saga: Breaking Dawn - Part 2": "Breaking Dawn 2",
    }
    if set(short) != {r["title"] for r in twilight}:
        raise ValueError("Twilight display labels no longer match the IMDb source rows")
    franchise = []
    for r in sorted(twilight, key=lambda x:int(x["year"])):
        franchise.append({
            "tconst":r["tconst"], "film":short[r["title"]], "year":r["year"],
            "rating":r["rating"], "num_votes":r["num_votes"],
            "franchise_votes":votes_twilight, "total_votes":votes_total,
            "twilight_median":round(twilight_med,2), "other_median":round(other_med,2),
            "other_count":len(other), "twilight_count":len(twilight)
        })
    write("chart_v2_01_twilight.csv", franchise, list(franchise[0]))

    # Chart 2: area proportional to IMDb title votes; place every film once.
    # Stable chronology jitter distinguishes same-year film dots, not additional time.
    byyear=Counter()
    time_rows=[]
    for r in sorted(films,key=lambda x:(int(x["year"]),x["title"])):
        year=int(r["year"])
        byyear[year]+=1
        group="twilight" if is_twilight(r["title"]) else "other"
        time_rows.append({
            "tconst":r["tconst"], "title":r["title"], "year":year,
            "rating":float(r["rating"]), "num_votes":int(r["num_votes"]),
            "group":group, "credit_source":r["credit_source"], 
            "ordinal_within_year":byyear[year]-1
        })
    maximum=max(r["num_votes"] for r in time_rows)
    for r in time_rows:
        c=Counter(v["year"] for v in time_rows)[r["year"]]
        r["plot_year"]=r["year"]+(r["ordinal_within_year"]-(c-1)/2)*0.25
        # Matplotlib marker s is area in points^2, so 360*(votes/max) encodes
        # vote-volume magnitude without mistakenly making radius proportional.
        r["bubble_area"]=round(55+360*r["num_votes"]/maximum,1)
        r["pareto_frontier"]=int(not any(
            (other["rating"]>=r["rating"] and other["num_votes"]>=r["num_votes"])
            and (other["rating"]>r["rating"] or other["num_votes"]>r["num_votes"])
            for other in time_rows
        ))
    leaders=[r["title"] for r in time_rows if r["pareto_frontier"]]
    if set(leaders)!={"The Batman","The Odyssey"}:
        raise ValueError(f"Unexpected IMDb rating-vote frontier: {leaders}")
    write("chart_v2_02_career.csv",time_rows,list(time_rows[0]))

    # Chart 3: film-to-person-to-role links. Join on IMDb IDs and reject roles
    # lacking a corresponding documented Pattinson-film/Bond-film cast edge.
    roles_by_nconst={r["person_nconst"]:r for r in roles}
    if len(roles_by_nconst)!=6 or len(roles)!=6:
        raise ValueError("Expected exactly six role attributions")
    connected={}
    for r in bonds:
        key=(r["person_nconst"],r["pattinson_tconst"])
        connected.setdefault(key,[]).append(r)
    distinct_people={r["person_nconst"] for r in bonds}
    if set(roles_by_nconst)!=distinct_people or len(connected)!=6:
        raise ValueError("Audited Bond role records do not match the six source connections")
    shorts={
        "Harry Potter and the Goblet of Fire":"Harry Potter: Goblet of Fire",
        "Remember Me":"Remember Me",
        "Water for Elephants":"Water for Elephants",
        "Cosmopolis":"Cosmopolis",
        "The Twilight Saga: Breaking Dawn - Part 2":"Breaking Dawn: Part 2",
        "The Batman":"The Batman",
    }
    roles_out=[]
    for (nid,tid),edges in connected.items():
        role=roles_by_nconst[nid]
        matching=[r for r in edges if r["bond_tconst"]==role["example_bond_tconst"]]
        if len(matching)!=1:
            raise ValueError(f"Role/source Bond title mismatch {nid}: {role}")
        chosen=matching[0]
        title=chosen["pattinson_title"]
        if title not in shorts: raise ValueError(f"Missing display title: {title}")
        roles_out.append({
            "pattinson_tconst":tid,
            "pattinson_film":title,
            "pattinson_short":shorts[title],
            "pattinson_year":chosen["pattinson_year"],
            "person_nconst":nid,
            "person":chosen["person"],
            "bond_role":role["bond_role"],
            "connection_kind":role["connection_kind"],
            "bond_tconst":chosen["bond_tconst"],
            "bond_film":chosen["bond_title"],
            "bond_year":chosen["bond_year"],
            "bond_actor":chosen["bond_actor"],
            "cast_source":chosen["cast_source"],
            "role_source":role["bond_role_source"],
        })
    roles_out.sort(key=lambda r:(int(r["pattinson_year"]),r["person"]))
    if Counter(r["connection_kind"] for r in roles_out)!={"bond":1,"ally":2,"villain":3}:
        raise ValueError("Bond character classification changed")
    write("chart_v2_03_bond_paths.csv",roles_out,list(roles_out[0]))
    report={
        "source_snapshot":"2026-11-18 IMDb TSV.gz extract",
        "released_rated_films":len(films),
        "twilight_n":len(twilight),
        "twilight_film_votes_sum":votes_twilight,
        "total_film_votes_sum":votes_total,
        "twilight_votes_pct":round(100*votes_twilight/votes_total,2),
        "twilight_median_rating":twilight_med,
        "other_films_n":len(other),
        "other_median_rating":other_med,
        "pareto_frontier_titles":leaders,
        "verified_bond_people":len(distinct_people),
        "verified_bond_pathways":len(roles_out),
        "bond_actor_roles":dict(Counter(r["connection_kind"] for r in roles_out)),
        "caveat":"IMDb weighted movie ratings, not ratings of an individual actor; summed film votes are not unique viewers. This is an audited subset of cast links, not exhaustive cast history."
    }
    (GENERATED/"story_v2_qa.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    main()
