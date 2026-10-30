"""Nightingale's 24-month annualised cause-of-death rates.

A specialised but centrally styled Coffeetableviz chart type. This module
does not contain data values: it renders the exact pinned HistData rows from
CHART_CONFIG and validates them before drawing. Do not infer causality.
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from chart_style import BG, PRIMARY, ACCENT, TEXT, MUTED, resolve_style

OTHER = "#3A454A"
GRID = "#D7DDDF"
CAUSES = (
    ("Disease.rate", PRIMARY, "Disease", 3.3),
    ("Wounds.rate", ACCENT, "Wounds", 2.0),
    ("Other.rate", OTHER, "Other causes", 2.0),
)
REQUIRED = {
    "Date", "Army", "Disease", "Wounds", "Other",
    "Disease.rate", "Wounds.rate", "Other.rate",
}


def validate_nightingale_rows(rows):
    """Fail closed if the verified source, ordering or rates drift."""
    if len(rows) != 24:
        raise ValueError("Nightingale chart expects 24 monthly HistData records")
    if not REQUIRED.issubset(set(rows[0])):
        raise ValueError(f"Missing Nightingale fields: {sorted(REQUIRED - set(rows[0]))}")
    dates = [datetime.strptime(str(r["Date"]), "%Y-%m-%d") for r in rows]
    if dates[0].strftime("%Y-%m") != "1854-04" or dates[-1].strftime("%Y-%m") != "1856-03":
        raise ValueError("Nightingale date range must be Apr 1854–Mar 1856")
    if any((n.year-p.year)*12 + (n.month-p.month) != 1 for p,n in zip(dates,dates[1:])):
        raise ValueError("Nightingale must contain exactly consecutive months")

    for r in rows:
        strength = float(r["Army"])
        if strength <= 0:
            raise ValueError("Army strength must be positive")
        for cause in ("Disease", "Wounds", "Other"):
            calculated = 12_000 * float(r[cause]) / strength
            if abs(calculated - float(r[cause + ".rate"])) > 0.051:
                raise ValueError(f"Invalid annualised {cause} rate for {r['Date']}")

    totals = tuple(sum(int(r[cause]) for r in rows[:12])
                   for cause in ("Disease","Wounds","Other"))
    later = tuple(sum(int(r[cause]) for r in rows[12:])
                  for cause in ("Disease","Wounds","Other"))
    if totals != (11157, 772, 1365) or later != (3319, 986, 383):
        raise ValueError("Historical period totals no longer match validated source")
    if dates[9].strftime("%Y-%m") != "1855-01" or abs(float(rows[9]["Disease.rate"])-1022.8) > .001:
        raise ValueError("Expected January 1855 annualised-rate peak is missing")
    if abs(float(rows[-1]["Disease.rate"])-3.9) > .001:
        raise ValueError("Expected March 1856 disease rate is missing")
    return dates


def render_nightingale_rates(repo_root, config, rows):
    """Render the original 24-month story in the approved square house frame."""
    from editorial_schematics import _add_header, _add_footer, _save

    dates = validate_nightingale_rows(rows)
    if config.get("render_profile") != "social_square":
        raise ValueError("Nightingale vNext requires the approved shared social_square house profile")
    st = resolve_style(config)
    fig = plt.figure(figsize=(8,8), facecolor=BG)
    _add_header(fig, config["title"], config["subtitle"], config=config)

    # Shared house positioning: all content inside the 8.5% reference frame.
    legend_y = .718
    for x, col, label, _ in ((.11,PRIMARY,"Disease",0),(.38,ACCENT,"Wounds",0),(.60,OTHER,"Other causes",0)):
        fig.add_artist(plt.Line2D([x,x+.045],[legend_y,legend_y],
                    transform=fig.transFigure,color=col,lw=3.6,solid_capstyle="round"))
        fig.text(x+.057,legend_y,label,color=TEXT,va="center",fontsize=12.0)

    ax = fig.add_axes([.17,.348,.70,.293], facecolor=BG)
    x = np.arange(len(dates))
    ax.axvspan(-.5,11.5,facecolor="#E6EAEC",alpha=.70,zorder=0)
    ax.axvline(11.5,color="#8B969E",lw=1.0,ls=(0,(4,4)),zorder=1)
    for key, colour, label, lw in CAUSES:
        vals=np.array([float(row[key]) for row in rows])
        ax.plot(x, vals, color=colour, lw=lw, zorder=3, solid_capstyle="round",
                marker="o", markersize=3.5 if key=="Disease.rate" else 2.1)
    ax.scatter([9],[1022.8],color=PRIMARY,s=72,edgecolor=BG,linewidths=2.0,zorder=7)
    ax.annotate("Jan 1855 peak\\n1,022.8",xy=(9,1022.8),xytext=(13.3,995),
        fontsize=11.7,color=TEXT,fontweight="bold",va="top",ha="left",zorder=8,
        arrowprops={"arrowstyle":"-","color":MUTED,"lw":.9})
    ax.set_xlim(-.5,23.45)
    ax.set_ylim(0,1140)
    ax.set_yticks([0,200,400,600,800,1000])
    ax.set_yticklabels(["0","200","400","600","800","1,000"])
    ax.set_xticks([0,3,6,9,12,15,18,21,23])
    ax.set_xticklabels(["Apr\\n1854","Jul","Oct","Jan\\n1855","Apr","Jul","Oct","Jan\\n1856","Mar"])
    ax.tick_params(axis="both",which="both",length=0,colors=MUTED,labelsize=st["tick_label_fontsize"])
    ax.tick_params(axis="x",pad=8)
    ax.tick_params(axis="y",pad=6)
    for spine in ax.spines.values():spine.set_visible(False)
    ax.grid(axis="y",color=GRID,lw=.85)
    ax.set_axisbelow(True)

    fig.text(.19,.661,"APR 1854–MAR 1855",fontsize=11,color=MUTED,weight="bold")
    fig.text(.555,.661,"APR 1855–MAR 1856",fontsize=11,color=MUTED,weight="bold")

    fig.text(.09,.271,"RATE = monthly deaths ÷ estimated army strength × 12,000",
             fontsize=11.2,color=TEXT)
    fig.text(.09,.236,"Annualised rates are not deaths in a single month.",
             fontsize=11.5,color=MUTED)
    fig.text(.09,.187,"The sharp decline is clear in these records.",
             fontsize=14.1,color=TEXT,weight="bold")
    fig.text(.09,.158,"The chart alone cannot tell us what caused it.",
             fontsize=11.7,color=MUTED)

    _add_footer(fig,"Adam Green | coffeetableviz",
                config["source_text"],config=config)
    return _save(fig,Path(repo_root),config)
