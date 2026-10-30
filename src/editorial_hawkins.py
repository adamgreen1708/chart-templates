"""Approved-house presentation of Ed Hawkins' climate stripe idea.

Uses pinned Met Office HadCRUT5 5.2.0.0 annual anomalies, 1850–2025.
This modern reconstruction is not the University of Reading's original art.
Preserve the scientific blue-red temperature scale and 95% confidence limits.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm

from chart_style import BG, PRIMARY, ACCENT, TEXT, MUTED, resolve_style

DATA_SHA256="7f750b673bb34aad722736ee21f122b5ea692c99877fa0b1066df65e51f32c04"
STRIPE_COLORS=[
    "#08306b", "#2166ac", "#67a9cf", "#DCEAF1",
    "#F9E6DE", "#EF9E85", "#C44E52", "#98002E",
]
COLOR_MAP=LinearSegmentedColormap.from_list("warming", STRIPE_COLORS, N=256)
COLOR_NORM=TwoSlopeNorm(vmin=-1.25, vcenter=0, vmax=1.25)
SOURCE="HadCRUT5 v5.2 · 1961–1990 reference"


def validate_hawkins_source(repo_root, config, rows):
    """Fail when annual time series, anomaly values, confidence intervals, or pin drift."""
    data=Path(repo_root)/config["data_file"]
    if not data.is_file() or sha256(data.read_bytes()).hexdigest()!=DATA_SHA256:
        raise ValueError("Pinned HadCRUT5 annual CSV changed")
    years=[int(r["Time"]) for r in rows]
    if years!=list(range(1850,2027)):
        raise ValueError("Expected 177 annual rows, including incomplete 2026")
    complete=rows[:-1]
    a=np.array([float(r["Anomaly (deg C)"]) for r in complete])
    lo=np.array([float(r["Lower confidence limit (2.5%)"]) for r in complete])
    hi=np.array([float(r["Upper confidence limit (97.5%)"]) for r in complete])
    if not (len(a)==176 and np.all(np.isfinite(a)) and np.all(np.isfinite(lo)) and np.all(np.isfinite(hi))):
        raise ValueError("Missing or nonfinite HadCRUT5 annual values")
    if not (np.all(lo<a) and np.all(a<hi)):
        raise ValueError("Invalid 95% interval bounds")
    offset=float(np.mean(a[np.logical_and(np.array(years[:-1])>=1961,
                                           np.array(years[:-1])<=2010)]))
    if abs(offset-0.18100777836)>1e-9 or abs(a[-1]-1.0732167)>1e-7:
        raise ValueError("HadCRUT5 baseline/2025 expected values drifted")
    native_period_mean=np.mean(a[111:141]) # 1961–1990 inclusive
    if abs(native_period_mean)>0.03:
        raise ValueError("Native 1961–1990 anomaly baseline validation failed")
    return np.array(years[:-1]),a,lo,hi


def render_hawkins_stripes(repo_root, config, rows):
    from editorial_schematics import _add_header, _add_footer, _save

    if config.get("render_profile")!="social_square":
        raise ValueError("Hawkins vNext uses centrally approved social_square house style")
    years, anomalies, lower, upper=validate_hawkins_source(repo_root,config,rows)
    st=resolve_style(config)
    fig=plt.figure(figsize=(8,8),facecolor=BG)
    _add_header(fig,config["title"],config["subtitle"],config=config)

    shared_left=.19
    shared_width=.67
    shared_bounds=(1849.5,2025.5)
    stripe_ax=fig.add_axes([shared_left,.607,shared_width,.128],facecolor=BG)
    stripe_ax.imshow(anomalies[np.newaxis,:],cmap=COLOR_MAP,norm=COLOR_NORM,
             interpolation="nearest",aspect="auto",
             extent=[shared_bounds[0],shared_bounds[1],0,1])
    stripe_ax.set_xlim(*shared_bounds)
    stripe_ax.set_axis_off()

    fig.text(shared_left,.589,"1850",fontsize=11.2,color=MUTED,ha="left")
    fig.text(shared_left+shared_width,.589,"2025",fontsize=11.2,color=MUTED,ha="right")

    plot=fig.add_axes([shared_left,.335,shared_width,.214],facecolor=BG)
    plot.axvspan(1960.5,1990.5,color="#DDD6C9",alpha=.64,zorder=0,lw=0)
    plot.fill_between(years,lower,upper,color=PRIMARY,alpha=.20,lw=0,zorder=2)
    plot.plot(years,anomalies,color=TEXT,lw=1.8,zorder=4)
    plot.axhline(0,color=MUTED,lw=.8,ls="--",zorder=3)
    plot.scatter([2025],[float(anomalies[-1])],s=38,color=ACCENT,zorder=6)
    plot.set_xlim(*shared_bounds)
    plot.set_ylim(-.90,1.48)
    plot.set_xticks([1850,1900,1950,2000,2025])
    plot.set_yticks([-.5,0,.5,1.0])
    plot.set_ylabel("Anomaly (°C)",fontsize=st["axis_label_fontsize"],labelpad=10,color=MUTED)
    plot.tick_params(axis="both",which="both",length=0,labelsize=st["tick_label_fontsize"],colors=MUTED,pad=7)
    for sp in plot.spines.values():sp.set_visible(False)
    plot.grid(axis="y",color="#D9D9D9",lw=.75,zorder=0)
    plot.set_axisbelow(True)
    plot.annotate("2025",xy=(2025,anomalies[-1]),xytext=(-6,10),
        textcoords="offset points",ha="right",va="bottom",
        fontsize=11.5,fontweight="bold",color=ACCENT)

    # Both panels must place every annual centre at the same x-coordinate.
    a=stripe_ax.get_position().bounds
    b=plot.get_position().bounds
    if not (abs(a[0]-b[0])<1e-12 and abs(a[2]-b[2])<1e-12 and
            np.allclose(stripe_ax.get_xlim(),plot.get_xlim())):
        raise ValueError("Stripe/temperature horizontal alignment drift")
    if len(anomalies)!=int(shared_bounds[1]-shared_bounds[0]):
        raise ValueError("One annual stripe per completed year required")
    for year in (1850,1900,1961,1975,1990,2025):
        x1=a[0]+a[2]*(year-shared_bounds[0])/(shared_bounds[1]-shared_bounds[0])
        x2=b[0]+b[2]*(year-shared_bounds[0])/(shared_bounds[1]-shared_bounds[0])
        if abs(x1-x2)>1e-12:
            raise ValueError(f"Stripe alignment failed in {year}")

    fig.text(.09,.281,"Blue band: 95% uncertainty · tan: 1961–1990 reference.",fontsize=12.4,color=MUTED)
    fig.text(.09,.241,"HadCRUT5 reconstruction · completed years 1850–2025",fontsize=12.2,color=MUTED)
    fig.text(.09,.199,"2026 excluded · not Reading's original stripes.",fontsize=12.1,color=MUTED)

    _add_footer(fig,"Adam Green | coffeetableviz",config["source_text"],config=config)
    return _save(fig,repo_root,config)
