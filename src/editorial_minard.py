"""Shared-house reconstruction of Minard's 1812 campaign visualisation.

Source: pinned HistData Minard.troops / Minard.cities / Minard.temp CSVs.
Longitude/latitude placements are digitised historical-plot estimates, not
navigation coordinates. Width is linear in survivors estimates, NOT deaths.
Temperatures are Réaumur (°Ré); missing date fields are never invented.
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from chart_style import BG, TEXT, MUTED, ACCENT, resolve_style

OUTWARD="#D7B38A"
RETURN="#24272B"
GRID="#DCE0E4"
ROOT_DATA="archive/projects/2026-10-icons-of-data/data"
REQUIRED_TROOPS={"long","lat","survivors","direction","group"}
REQUIRED_TEMP={"long","temp","days","date"}


def _csv(path):
    with Path(path).open(newline="",encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def load_validate_minard(repo_root, config, route_rows):
    """Use source CSVs in GitHub and validate the published historical framing."""
    directory=Path(repo_root)/ROOT_DATA
    troops=_csv(directory/"minard_troops.csv")
    cities=_csv(directory/"minard_cities.csv")
    temperatures=_csv(directory/"minard_temperature.csv")
    if not (len(route_rows)==51 and len(troops)==51 and len(cities)==20 and len(temperatures)==9):
        raise ValueError("Expected original 51 troop, 20 city, nine temperature records")
    if not REQUIRED_TROOPS.issubset(troops[0]) or not REQUIRED_TEMP.issubset(temperatures[0]):
        raise ValueError("Minard data columns missing")
    if not all(str(x["rownames"])==str(y["rownames"]) and
               str(x["survivors"])==str(y["survivors"]) for x,y in zip(route_rows,troops)):
        raise ValueError("CHART_CONFIG troop rows don't match pinned historical troop CSV")
    if set(r["direction"] for r in troops)!={"A","R"}:
        raise ValueError("Expected separate outward and return routes")
    if set(int(r["group"]) for r in troops)!={1,2,3}:
        raise ValueError("Expected three route groups")
    groups=defaultdict(list)
    for r in troops:
        key=(int(r["group"]),r["direction"])
        groups[key].append(r)
        if int(r["survivors"])<0:
            raise ValueError("Negative troop strength")
    if any(len(v)<2 for v in groups.values()) or len(groups)!=6:
        raise ValueError("Minard route group missing")
    starts=[int(groups[(i,"A")][0]["survivors"]) for i in (1,2,3)]
    if starts!=[340000,60000,22000]:
        raise ValueError("Source start estimates have changed")
    if int(groups[(1,"A")][-1]["survivors"])!=100000 or int(groups[(1,"R")][-1]["survivors"])!=4000:
        raise ValueError("Main route endpoint estimates have changed")
    if sum(not str(r["date"]).strip() for r in temperatures)!=1:
        raise ValueError("Exactly one missing historical temperature date must be retained")
    if min(int(r["temp"]) for r in temperatures)!=-30:
        raise ValueError("Historical recorded minimum changed")
    return groups,cities,temperatures


def _ribbon(ax, records, colour, scale=1.05, z=3):
    """Line width is proportional to source troop estimate."""
    xs=np.array([float(r["long"]) for r in records])
    ys=np.array([float(r["lat"]) for r in records])
    strengths=np.array([int(r["survivors"]) for r in records])
    widths=(strengths/10000.0)*scale
    for i in range(len(xs)-1):
        ax.plot(xs[i:i+2],ys[i:i+2],lw=(widths[i]+widths[i+1])/2,
                color=colour,zorder=z,solid_capstyle="round")
    for x,y,width in zip(xs,ys,widths):
        ax.plot([x],[y],marker="o",markersize=width,markeredgewidth=0,
                color=colour,zorder=z)


def render_minard_campaign(repo_root, config, rows):
    from editorial_schematics import _add_header, _add_footer, _save

    if config.get("render_profile")!="social_square":
        raise ValueError("Minard vNext requires the approved Coffeetableviz house profile")
    groups,cities,temps=load_validate_minard(repo_root,config,rows)
    style=resolve_style(config)
    fig=plt.figure(figsize=(8,8),facecolor=BG)
    _add_header(fig,config["title"],config["subtitle"],config=config)

    # Keep historic map ribbons while inheriting a standard frame and grey plot.
    legend_y=.748
    fig.add_artist(Line2D([.13,.174],[legend_y,legend_y],
                    transform=fig.transFigure,lw=7,color=OUTWARD,solid_capstyle="butt"))
    fig.text(.19,legend_y,"Into Russia",fontsize=13.0,color=TEXT,va="center")
    fig.add_artist(Line2D([.445,.485],[legend_y,legend_y],
                    transform=fig.transFigure,lw=5,color=RETURN,solid_capstyle="butt"))
    fig.text(.505,legend_y,"Retreat",fontsize=13.0,color=TEXT,va="center")

    ax=fig.add_axes([.155,.444,.715,.268],facecolor=BG)
    ax.set_xlim(23.25,38.6)
    ax.set_ylim(53.48,56.42)
    ax.set_xticks([]);ax.set_yticks([])
    for sp in ax.spines.values():sp.set_visible(False)
    for group in (1,2,3):
        _ribbon(ax,groups[(group,"A")],OUTWARD,z=2)
        _ribbon(ax,groups[(group,"R")],RETURN,z=3)

    # Source place labels — locations are on the digitised Minard map, not new geography.
    spots={
       "Kowno":(24,55.0,(9,17),"left"),
       "Smolensk":(32,54.8,(3,-17),"left"),
       "Moscou":(37.6,55.8,(-10,19),"right"),
       "Polotzk":(28.7,55.5,(6,10),"left"),
    }
    for name,(x,y,shift,side) in spots.items():
        if name not in {c["city"] for c in cities}:
            raise ValueError(f"Missing historical city: {name}")
        ax.annotate("MOSCOW" if name=="Moscou" else name.upper(),
                    xy=(x,y),xytext=shift,textcoords="offset points",ha=side,va="center",
                    fontsize=12.2,color=TEXT,fontweight="bold",
                    arrowprops={"arrowstyle":"-","color":MUTED,"lw":.7},zorder=8)

    fig.text(.09,.410,"Western start: 422k across three plotted groups.",
            fontsize=12.3,color=MUTED)

    fig.text(.09,.377,"THE RETREAT GETS COLDER",fontsize=12.7,fontweight="bold",color=TEXT)
    fig.text(.91,.377,"Temperature (°Réaumur)",fontsize=11.3,ha="right",color=MUTED)
    temperature=fig.add_axes([.155,.219,.715,.126],facecolor=BG)
    tx=np.array([float(r["long"]) for r in temps])
    ty=np.array([float(r["temp"]) for r in temps])
    temperature.set_xlim(23.25,38.6)
    temperature.set_ylim(-34,5)
    temperature.plot(tx,ty,lw=2.4,color=ACCENT,marker="o",markersize=4.0,zorder=3)
    temperature.set_yticks([0,-15,-30])
    temperature.set_yticklabels(["0°","−15°","−30°"],fontsize=style["tick_label_fontsize"])
    temperature.set_xticks([])
    temperature.tick_params(length=0,pad=6,colors=MUTED)
    temperature.grid(axis="y",color=GRID,lw=.8)
    for sp in temperature.spines.values():sp.set_visible(False)
    temperature.annotate("18 Oct · 0°Ré",(37.6,0),xytext=(-3,3),
        textcoords="offset points",ha="right",fontsize=10.6,color=MUTED)
    temperature.annotate("6 Dec · −30°Ré",(26.7,-30),xytext=(6,-11),
        textcoords="offset points",ha="left",va="top",fontsize=10.6,
        color=ACCENT,fontweight="bold")

    fig.text(.09,.158,"Map positions approximate · width = estimated troop strength.",
            fontsize=11.0,color=MUTED)
    fig.text(.09,.128,"°Ré is Réaumur; temperature dates are from source records.",
            fontsize=10.5,color=MUTED)

    _add_footer(fig,"Adam Green | coffeetableviz",config["source_text"],config=config)
    return _save(fig,repo_root,config)
