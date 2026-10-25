#!/usr/bin/env python3
"""Deterministic Coffeetableviz research render for season-long champions."""
from __future__ import annotations
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[1]
DATA, OUT = ROOT / "data", ROOT / "output"
OUT.mkdir(exist_ok=True)
BG, RED, BLUE, GREY = "#F3F4F6", "#C44E52", "#1F8FA8", "#9EA5AB"
TEXT, MID, GRID = "#111111", "#555555", "#DCE0E3"
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":10,
    "figure.facecolor":BG, "axes.facecolor":BG, "savefig.facecolor":BG,
    "text.color":TEXT, "axes.labelcolor":MID, "xtick.color":MID, "ytick.color":MID})
def records(filename):
    with open(DATA / filename,encoding="utf-8-sig",newline="") as fh:
        return list(csv.DictReader(fh))
items=records("youngest_season_champions.csv")
history=records("f1_youngest_record_progression.csv")
assert len(items)==13 and len(history)==5
assert sum(r["status"].startswith("conditional") for r in history)==1
assert all(r["source_primary"].startswith("https://") for r in items)
items.sort(key=lambda r:float(r["age_years_decimal"]))
def col(row):
    return RED if row["sport"]=="Formula 1" else BLUE if row["sport"] in ("Motorcycling","Rallying") else GREY
def figbase(title,subtitle,num,footer):
    fig=plt.figure(figsize=(8,8),dpi=200,facecolor=BG)
    fig.text(.095,.926,title,fontsize=22,weight="bold",ha="left",va="top")
    fig.text(.095,.852,subtitle,fontsize=10.8,ha="left",va="top",color=MID,linespacing=1.3)
    fig.add_artist(Line2D([.095,.905],[.107,.107],transform=fig.transFigure,color="#D0D0D0",lw=.8))
    fig.text(.095,.077,"COFFEETABLEVIZ  |  "+footer,fontsize=8,color=MID)
    fig.text(.905,.077,num,fontsize=8,color=MID,ha="right")
    return fig
def style(ax):
    ax.grid(color=GRID,linewidth=.8,zorder=0)
    for s in ax.spines.values():s.set_visible(False)
    ax.tick_params(length=0)
def key(fig):
    for i,(lab,color) in enumerate([("F1",RED),("Other motorsport",BLUE),("Other sports",GREY)]):
        x=[.095,.22,.46][i]
        fig.add_artist(Line2D([x],[.137],transform=fig.transFigure,marker="o",
            markersize=6,markerfacecolor=color,markeredgecolor=color,ls="None"))
        fig.text(x+.013,.137,lab,fontsize=8.5,va="center",color=MID)
def save(fig,name):
    fig.savefig(OUT/name,dpi=200,facecolor=BG)
    plt.close(fig)

# Chart 1: the confirmed record only; the hypothetical 2026 endpoint is hollow.
f=figbase("F1’s age record could fall again",
   "Fittipaldi’s 1972 benchmark lasted 33 years.\nAntonelli could lower Vettel’s mark by over three years.",
   "01 / 03","F1, Guinness; conditional 2026 case")
ax=f.add_axes([.13,.20,.74,.50])
past=[r for r in history if r["status"]=="confirmed"]
years=[int(r["year"]) for r in past]; ages=[float(r["age_years_decimal"]) for r in past]
ax.step(years+[2025],ages+[ages[-1]],where="post",c=GREY,lw=2.6,zorder=2)
for i,(x,y) in enumerate(zip(years,ages)):
    ax.scatter(x,y,c=RED if i==len(years)-1 else GREY,s=100,zorder=5,edgecolors=BG)
positions={"Emerson Fittipaldi":(1975,26.7),"Fernando Alonso":(1997.5,24.8),
           "Lewis Hamilton":(1996,22.9),"Sebastian Vettel":(2014.7,24.1)}
short={"Emerson Fittipaldi":"Fittipaldi","Fernando Alonso":"Alonso",
       "Lewis Hamilton":"Hamilton","Sebastian Vettel":"Vettel"}
for r in past:
    x=int(r["year"]); y=float(r["age_years_decimal"])
    name=r["champion"]; c=RED if name=="Sebastian Vettel" else TEXT
    ax.annotate(short[name]+"\n"+str(r["age_years"])+"y "+str(r["days_after_birthday"])+"d",
      (x,y),xytext=positions[name],textcoords="data",fontsize=9.5,ha="left",
      color=c,weight="bold" if c==RED else "normal",
      arrowprops=dict(arrowstyle="-",lw=1.1,color=RED if c==RED else GREY,shrinkA=4,shrinkB=6),
      bbox=dict(facecolor=BG,edgecolor="none",pad=1),zorder=8)
hyp=next(r for r in history if r["status"].startswith("conditional"))
hypage=float(hyp["age_years_decimal"])
ax.plot([2026,2026],[ages[-1],hypage],color=RED,lw=2,ls=(0,(2,3)))
ax.scatter(2026,hypage,s=155,edgecolors=RED,facecolors=BG,linewidths=2.5,zorder=8)
ax.annotate("Antonelli*\n20y 61d",(2026,hypage),xytext=(2008,19.5),
  ha="left",fontsize=10,color=RED,weight="bold",
  bbox=dict(facecolor=BG,edgecolor="none",pad=1),
  arrowprops=dict(arrowstyle="-",color=RED,lw=1.1,shrinkA=4,shrinkB=6))
ax.set(xlim=(1968,2033),ylim=(18.7,27.3),ylabel="Age when title won (years)")
ax.set_xticks([1972,1980,1990,2000,2010,2020,2026])
ax.set_yticks([20,22,24,26]);style(ax)
f.text(.13,.14,"* Conditional: age on 25 Oct 2026. No 2026 title confirmed.",fontsize=8.4,color=RED)
save(f,"season_champions_01_f1_record.png")

# Chart 2: all non-motorsport context grey; only F1 red, other motorsport blue.
f=figbase("A champion at 13. Another at 23.",
 "Selected senior season-wide titles; not one-off majors,\nraces or Olympic medals. ATP and WTA are included.",
 "02 / 03","Sources: organisers, ATP, WTA, FIA")
ax=f.add_axes([.50,.21,.394,.53])
for y,row in enumerate(reversed(items)):
    a=float(row["age_years_decimal"]); c=col(row)
    ax.hlines(y,12,a,color=GRID,lw=1.1)
    ax.scatter(a,y,s=93 if c==RED else 70 if c==BLUE else 55,c=c,zorder=4)
    ax.text(11.66,y,row["sport"]+" · "+row["athlete"],ha="right",va="center",
        fontsize=8.1,clip_on=False,weight="bold" if c==RED else "normal",
        color=TEXT if c!=GREY else MID)
    ax.text(a+.27,y,row["age_years"]+"y",ha="left",va="center",fontsize=8.4,
        color=c if c!=GREY else MID,weight="bold" if c!=GREY else "normal")
ax.set(xlim=(12,26.2),ylim=(-.7,len(items)-.4),xlabel="Age at title (years) · dot scale begins at 12")
ax.set_yticks([]);ax.set_xticks([12,16,20,24]);style(ax);key(f)
save(f,"season_champions_02_cross_sport.png")

# Chart 3: same colour semantics, names carry an explicit sport qualifier.
f=figbase("Three ways to win a season",
 "Same broad test: finish on top across multiple events.\nThe scoring systems are not interchangeable.",
 "03 / 03","Selected examples, not an exhaustive census")
ax=f.add_axes([.52,.225,.37,.51])
group_names=[("TOUR STANDINGS / YEAR-END NO. 1","Tour standings"),
             ("SEASON + PLAY-OFFS / FINALS","Season + finals"),
             ("RACING POINTS CHAMPIONSHIPS","Race points")]
y=14.; pts=[]
for heading,grp in group_names:
    ax.text(12,y,heading,fontsize=8.35,weight="bold",color=MID,clip_on=False,va="center")
    y-=.84
    for row in sorted([r for r in items if r["format_group"]==grp],key=lambda r:float(r["age_years_decimal"])):
        pts.append((y,row));y-=.73
    y-=.38
for yy,row in pts:
    a=float(row["age_years_decimal"]); c=col(row)
    ax.hlines(yy,12,a,color=GRID,lw=1)
    ax.scatter(a,yy,c=c,s=75 if c==RED else 57,zorder=4)
    ax.text(11.74,yy,row["athlete"]+" ("+row["sport"]+")",ha="right",va="center",
        fontsize=7.85,clip_on=False,color=TEXT,weight="bold" if c==RED else "normal")
    ax.text(a+.27,yy,row["age_years"]+"y",va="center",fontsize=8.2,
        color=c if c!=GREY else MID,weight="bold" if c!=GREY else "normal")
ax.set(xlim=(12,26.4),ylim=(y-.23,14.85),xlabel="Age when season title awarded (years)")
ax.set_yticks([]);ax.set_xticks([12,16,20,24]);style(ax);key(f)
save(f,"season_champions_03_title_formats.png")
print("Rendered 3 research-review PNGs to",OUT)
