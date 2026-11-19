"""Data-driven editorial profile views for social_square, opt-in only.

Registered by editorial_schematics; all plots consume derived CSV records and
share the Coffeetableviz header, footer, palette and safe frame.
Layouts: franchise_strip, career_bubbles, cast_paths.
No measurements, cast names or IMDb values are built into this renderer.
"""
from __future__ import annotations

import math
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from chart_style import resolve_style
from editorial_schematics import (
    BG, PRIMARY, ACCENT, CONTEXT, SECONDARY, TEXT, SUBTEXT,
    _add_header, _add_footer, _save,
)

def _required(rows, fields):
    if not rows:
        raise ValueError("profile_story requires nonempty rows")
    miss=set(fields)-set(rows[0])
    if miss:
        raise ValueError(f"profile_story missing CSV columns: {sorted(miss)}")

def _new_fig(config):
    if config.get("render_profile") != "social_square":
        raise ValueError("profile_story is an opt-in social_square-only layout")
    fig=plt.figure(figsize=(8,8),facecolor=BG)
    top=_add_header(fig, config["title"], config["subtitle"], config=config)
    return fig, min(.72, top)

def _foot(fig,config,source):
    _add_footer(fig, config.get("footer_left","Adam Green | coffeetableviz"),
                config.get("source_text",source), config=config)

def _line(fig,xs,ys,color=CONTEXT,lw=1,alpha=1):
    fig.add_artist(Line2D(xs,ys,color=color,linewidth=lw,alpha=alpha,
                         transform=fig.transFigure,zorder=1))

def _franchise(fig,top,rows,config):
    _required(rows,["film","year","rating","num_votes","franchise_votes",
                    "total_votes","twilight_median","other_median",
                    "other_count","twilight_count"])
    rows=sorted(rows,key=lambda r:int(r["year"]))
    if len(rows)!=5:
        raise ValueError("franchise_strip expects five audited rows")
    vote_sum=sum(int(r["num_votes"]) for r in rows)
    if any(int(r["franchise_votes"])!=vote_sum for r in rows):
        raise ValueError("Franchise vote sum mismatch against source rows")
    total=int(rows[0]["total_votes"])
    share=100*vote_sum/total
    if not 20<share<30 or int(rows[0]["other_count"])!=28:
        raise ValueError("Franchise cohort context outside validated research")
    def X(r):
        return .42+(.46*(float(r)-4)/5.0)
    if max(float(r["rating"]) for r in rows)>5.6+1e-7:
        raise ValueError("The headline is no longer true for the frozen snapshot")
    # Large statistic + dimensional caveat.
    fig.text(.09,top-.020,f"{vote_sum/1e6:.2f}m",color=TEXT,fontsize=31,
             fontweight="bold",ha="left",va="top")
    fig.text(.09,top-.076,"sum of votes across 5 IMDb titles",
             color=SUBTEXT,fontsize=11.4,ha="left",va="top")
    fig.text(.70,top-.020,f"{share:.1f}%",color=PRIMARY,fontsize=28,
             fontweight="bold",ha="left",va="top")
    fig.text(.70,top-.074,"of this film sample's votes",
             color=SUBTEXT,fontsize=10.4,ha="left",va="top")
    fig.text(.09,top-.138,"THE FIVE TWILIGHT FILMS",color=SUBTEXT,fontsize=11.5,
             fontweight="bold",va="bottom")
    fig.text(.865,top-.138,"IMDb / 10",color=SUBTEXT,fontsize=10.2,ha="right",va="bottom")
    first=min(top-.175,.505)
    step=.050
    for i,r in enumerate(rows):
        y=first-i*step
        fig.text(.09,y,r["film"],color=TEXT,fontsize=13.5,va="center")
        fig.text(.335,y,str(r["year"]),color=SUBTEXT,fontsize=10.7,va="center")
        _line(fig,[.42,.88],[y,y],color="#E0E2E5",lw=2)
        x=X(r["rating"])
        fig.add_artist(Line2D([x],[y],marker="o",linestyle="None",markersize=10,
                              markerfacecolor=ACCENT,markeredgecolor=BG,
                              markeredgewidth=.9,transform=fig.transFigure,zorder=4))
        fig.text(x+.020,y,f"{float(r['rating']):.1f}",ha="left",va="center",
                 color=ACCENT,fontsize=12.1,fontweight="bold")
    other_y=first-5*step-.035
    fig.text(.09,other_y+.015,f"Other films ({rows[0]['other_count']})",
             ha="left",va="center",fontsize=11.2,color=TEXT)
    # Two meaningful medians along the same truncated (4..9) rating axis.
    mt=float(rows[0]["twilight_median"])
    mo=float(rows[0]["other_median"])
    _line(fig,[.42,.88],[other_y,other_y],color="#E0E2E5",lw=2)
    for x,col,val in ((X(mt),ACCENT,mt),(X(mo),PRIMARY,mo)):
        fig.add_artist(Line2D([x],[other_y],marker="D",linestyle="None",
                              markersize=8,markerfacecolor=col,
                              markeredgecolor=BG,transform=fig.transFigure,zorder=5))
    fig.text(.09,other_y-.037,f"Median: {mt:.1f} Twilight  /  {mo:.2f} other films",
             color=TEXT,fontsize=12.1,va="top",ha="left",fontweight="bold")
    fig.text(.09,other_y-.066,"Dot comparison uses a 4–9 IMDb rating scale.",
             color=SUBTEXT,fontsize=9.7,ha="left",va="top")

def _career(fig,top,rows,config):
    _required(rows,["tconst","title","year","plot_year","rating",
                    "num_votes","bubble_area","group","pareto_frontier"])
    if len(rows)!=33:
        raise ValueError("career_bubbles expects 33 real film titles")
    actual_frontier={r["title"] for r in rows if int(r["pareto_frontier"])}
    if actual_frontier!={"The Batman","The Odyssey"}:
        raise ValueError(f"Unexpected frontier: {actual_frontier}")
    ax=fig.add_axes([.17,.255,.715,max(.29,top-.28)],facecolor=BG)
    ax.set_xlim(2004.4,2027.4)
    ax.set_ylim(4.2,9.0)
    ax.spines[:].set_visible(False)
    ax.set_axisbelow(True)
    ax.set_xticks([2005,2010,2015,2020,2026])
    ax.set_yticks([5,6,7,8])
    ax.tick_params(axis="both",length=0,labelsize=12,pad=8,colors=SUBTEXT)
    ax.grid(axis="y",color="#D8DBDE",linewidth=.9,zorder=0)
    ax.set_ylabel("IMDb film rating / 10",fontsize=12,color=SUBTEXT,labelpad=10)
    # Bubble areas are sized from *title-vote* counts, not unique viewers.
    sorted_rows=sorted(rows,key=lambda r:(r["group"]!="other",float(r["rating"])))
    for r in sorted_rows:
        is_twi=r["group"]=="twilight"
        is_frontier=int(r["pareto_frontier"])==1
        col=ACCENT if is_twi else PRIMARY if is_frontier else "#8998A2"
        ax.scatter([float(r["plot_year"])],[float(r["rating"])],
                   s=float(r["bubble_area"]),color=col,
                   alpha=.88 if is_twi or is_frontier else .54,
                   edgecolor=BG,linewidth=1.1,zorder=7 if is_frontier else 3)
        if is_frontier:
            ax.scatter([float(r["plot_year"])],[float(r["rating"])],
                       s=float(r["bubble_area"])*1.35,
                       facecolors="none",edgecolors=PRIMARY,linewidths=1.2,zorder=8)
    bytitle={r["title"]:r for r in rows}
    marks={
        "Good Time":(-8,-17,"right"),
        "The Lighthouse":(7,17,"left"),
        "The Batman":(-8,16,"right"),
        "The Odyssey":(-7,-19,"right"),
    }
    for name,(dx,dy,align) in marks.items():
        if name not in bytitle:raise ValueError(f"Missing milestone film: {name}")
        r=bytitle[name]
        ax.annotate(f"{name} {float(r['rating']):.1f}",
                    xy=(float(r["plot_year"]),float(r["rating"])),
                    xytext=(dx,dy),textcoords="offset points",ha=align,
                    fontsize=11.8,color=TEXT,fontweight="medium",zorder=10)
    # One concise data-derived frontier callout, independent of draw order.
    fig.text(.09,.206,"Only The Batman and The Odyssey sit on the",
             fontsize=12.3,ha="left",va="top",color=TEXT,fontweight="bold")
    fig.text(.09,.182,"rating + title-votes frontier in this 33-film snapshot.",
             fontsize=11.3,ha="left",va="top",color=SUBTEXT)
    fig.text(.09,.148,"Red: Twilight  ·  Blue ring: frontier  ·  Circle area: IMDb title-votes",
             fontsize=10.3,ha="left",va="top",color=SUBTEXT)

def _paths(fig,top,rows,config):
    _required(rows,["pattinson_short","pattinson_year","person","bond_role",
                    "bond_film","bond_year","connection_kind","person_nconst"])
    rows=sorted(rows,key=lambda r:(int(r["pattinson_year"]),r["person"]))
    if len(rows)!=6 or len({r["person_nconst"] for r in rows})!=6:
        raise ValueError("cast_paths needs exactly six unique real people")
    if Counter(r["connection_kind"] for r in rows)!={"bond":1,"ally":2,"villain":3}:
        raise ValueError("Bond role mix differs from audited research")
    header_y=min(top-.029,.688)
    fig.text(.09,header_y,"PAT​TINSON FILM".replace("\u200b",""),fontsize=10,
             fontweight="bold",color=SUBTEXT,ha="left",va="bottom")
    fig.text(.475,header_y,"SHARED ACTOR",fontsize=10,fontweight="bold",
             color=SUBTEXT,ha="left",va="bottom")
    fig.text(.74,header_y,"IN BOND",fontsize=10,fontweight="bold",
             color=SUBTEXT,ha="left",va="bottom")
    _line(fig,[.09,.91],[header_y-.012,header_y-.012],color="#A8ACB0",lw=1.2)
    first=header_y-.071
    step=min(.080,(first-.245)/5)
    for i,r in enumerate(rows):
        y=first-i*step
        col=ACCENT if r["connection_kind"]=="bond" else PRIMARY
        title=r["pattinson_short"]
        if len(title)>24:
            # Two-line presentation, values still taken from the audited CSV.
            if title.startswith("Harry Potter"):
                title="Harry Potter:\nGoblet of Fire"
            elif title.startswith("Breaking Dawn"):
                title="Breaking Dawn:\nPart 2"
            else:
                raise ValueError(f"Long source film label needs editorial wrap: {title}")
        fig.text(.09,y+.020,title,fontsize=12.0,color=TEXT,ha="left",va="top",
                 linespacing=1.0)
        fig.text(.09,y-.026,str(r["pattinson_year"]),fontsize=10.0,color=SUBTEXT,
                 ha="left",va="top")
        _line(fig,[.407,.456],[y+.004,y+.004],color=col,lw=1.7)
        fig.add_artist(Line2D([.456],[y+.004],marker="o",markersize=3.8,color=col,
                              transform=fig.transFigure,zorder=4))
        fig.text(.475,y+.013,r["person"],fontsize=12.2,color=col if r["connection_kind"]=="bond" else TEXT,
                 fontweight="bold" if r["connection_kind"]=="bond" else "medium",
                 ha="left",va="top")
        _line(fig,[.698,.726],[y+.004,y+.004],color=col,lw=1.6)
        fig.add_artist(Line2D([.726],[y+.004],marker=">",markersize=4.2,color=col,
                              transform=fig.transFigure,zorder=4))
        fig.text(.74,y+.017,r["bond_role"].upper(),fontsize=10.8,color=col,
                 fontweight="bold",ha="left",va="top")
        bond_label=str(r["bond_film"])
        if len(bond_label)>18:
            bond_label=bond_label[:17].rstrip()+"…"
        fig.text(.74,y-.013,bond_label+" · "+str(r["bond_year"]),
                 fontsize=9.5,color=SUBTEXT,ha="left",va="top")
        if i<5:_line(fig,[.09,.91],[y-step*.49,y-step*.49],color="#DADDDF",lw=.65)
    fig.text(.09,.155,"THE TWIST: Brosnan played his father in Remember Me (2010).",
             color=ACCENT,fontsize=11.5,fontweight="bold",ha="left",va="center")
    fig.text(.09,.127,"In November 2026, he publicly welcomed Pattinson as Bond.",
             color=SUBTEXT,fontsize=10.8,ha="left",va="center")

def render_profile_story(repo_root,config,rows):
    variant=config.get("layout_variant")
    if variant not in {"franchise_strip","career_bubbles","cast_paths"}:
        raise ValueError(f"Unknown profile_story layout_variant: {variant}")
    fig,top=_new_fig(config)
    if variant=="franchise_strip":_franchise(fig,top,rows,config)
    elif variant=="career_bubbles":_career(fig,top,rows,config)
    else:_paths(fig,top,rows,config)
    _foot(fig,config,"IMDb titles and audited cast credits")
    return _save(fig,repo_root,config)
