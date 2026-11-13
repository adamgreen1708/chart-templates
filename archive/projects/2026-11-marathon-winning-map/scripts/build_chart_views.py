"""Regenerate all three source-derived editorial chart views."""
import csv
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parents[1]/"data"
SOURCE=ROOT/"data"/"marathon-majors"
POS={"Tokyo":6,"Boston":5,"London":4,"Berlin":3,"Chicago":2,"New York City":1}
EAST={"Kenya","Ethiopia"}
def load(sex):
    with (SOURCE/f"marathon_major_winners_{sex}_2000_2026.csv").open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==154
    keyed={(r["Race"],int(r["Year"])):r for r in rows}
    assert len(keyed)==len(rows)
    return keyed
def eligible(r):
    return r["Event_Status"]=="Completed" and r["Result_Status"]=="Not independently checked" and r["Nationality"] and int(r["Year"])<=2025
def write(name,headers,rows):
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/name).open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f,lineterminator="\n");w.writerow(headers);w.writerows(rows)
def main():
    m,w=load("men"),load("women")
    matched=[(k,m[k],w[k]) for k in sorted(set(m)&set(w),key=lambda k:(k[1],k[0])) if eligible(m[k]) and eligible(w[k])]
    assert len(matched)==133
    early=[a for a in matched if 2000<=a[0][1]<=2009]
    later=[a for a in matched if 2010<=a[0][1]<=2019]
    assert len(early)==51 and len(later)==53
    counts=Counter(w["Nationality"] for k,m,w in early)
    assert len(counts)==10
    write("01_women_nationalities.csv",["Nationality","Wins"],sorted(counts.items(),key=lambda a:(-a[1],a[0])))
    # Matched-layout prequel: one dot per completed, source-filtered race-year.
    berlin=[a for a in early if a[0][0]=="Berlin" and 2000<=a[0][1]<=2005]
    assert len(berlin)==6 and all(a[2]["Nationality"]=="Japan" for a in berlin)
    earlydots=[]
    for (race,year),m,w in sorted(early,key=lambda a:(a[0][1],-POS[a[0][0]])):
        group="Kenya/Ethiopia" if w["Nationality"] in EAST else "Outside"
        earlydots.append((year,race,POS[race],w["Winner"],w["Nationality"],group))
    write("01_winner_race_year.csv",["Year","Race","RaceRow","Winner","Nationality","Group"],earlydots)
    dots=[];names=[]
    for (race,year),m,w in sorted(later,key=lambda a:(a[0][1],-POS[a[0][0]])):
        group="Kenya/Ethiopia" if w["Nationality"] in EAST else "Outside"
        dots.append((year,race,POS[race],w["Winner"],w["Nationality"],group))
        if group=="Outside":names.append(w["Winner"])
    assert sorted(names)==sorted(("Alevtina Biktimirova","Shalane Flanagan","Desiree Linden"))
    write("02_exception_race_year.csv",["Year","Race","RaceRow","Winner","Nationality","Group"],dots)
    slope=[]
    for sex in ("Women","Men"):
        for i,(label,sample) in enumerate((("2000–09",early),("2010–19",later)),1):
            n=len(sample);outside=sum(1 for k,m,w in sample if (w if sex=="Women" else m)["Nationality"] not in EAST)
            slope.append((i,label,sex,f"{outside/n:.6f}",outside,n))
    assert [(s[2],s[4],s[5]) for s in slope]==[("Women",29,51),("Women",3,53),("Men",12,51),("Men",5,53)]
    write("03_outside_winners_share.csv",["PeriodIndex","Period","Sex","OutsideShare","OtherWins","TotalWins"],slope)
    print("PASS: 133 matched; outsiders women 29/51 to 3/53, men 12/51 to 5/53.")
if __name__=="__main__":main()
