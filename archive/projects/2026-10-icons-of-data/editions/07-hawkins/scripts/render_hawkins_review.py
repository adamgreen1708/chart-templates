#!/usr/bin/env python3
"""Render Icons of Data #07 on GitHub Actions from a pinned HadCRUT5 snapshot.
Original artwork: genuine University of Reading image, not an imitation.
All three review figures are confined to archive/; no site publication.
"""
from pathlib import Path
from io import BytesIO
from hashlib import sha256
import csv, json, urllib.request
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from PIL import Image, ImageOps

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"HadCRUT.5.2.0.0.analysis.summary_series.global.annual.snapshot_2026-10-19.csv"
OUT=ROOT/"qa"/"visuals"
OUT.mkdir(parents=True,exist_ok=True)
BG="#F3F4F6"; INK="#111820"; MUTED="#58636E"; GRID="#CDD3D9"; TEAL="#1F8FA8"
STRIPE=["#08306b","#2166ac","#67a9cf","#DCEAF1","#F9E6DE","#EF9E85","#C44E52","#98002E"]
CMAP=LinearSegmentedColormap.from_list("warming",STRIPE,N=256)
NORM=TwoSlopeNorm(vmin=-1.25,vcenter=0,vmax=1.25)
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.labelcolor":MUTED,
"xtick.color":MUTED,"ytick.color":MUTED,"figure.facecolor":BG,"savefig.facecolor":BG})
with DATA.open(newline="",encoding="utf8") as f:
    records=list(csv.DictReader(f))
assert len(records)==177, "Unexpected pinned row count"
assert [int(r["Time"]) for r in records]==list(range(1850,2027))
rows=[r for r in records if int(r["Time"])<=2025]
years=np.asarray([int(r["Time"]) for r in rows])
vals=np.asarray([float(r["Anomaly (deg C)"]) for r in rows])
lower=np.asarray([float(r["Lower confidence limit (2.5%)"]) for r in rows])
upper=np.asarray([float(r["Upper confidence limit (97.5%)"]) for r in rows])
assert len(rows)==176 and np.isfinite(vals).all() and np.isfinite(lower).all() and np.isfinite(upper).all()
assert np.all(lower<vals) and np.all(vals<upper)
offset=float(np.mean(vals[(years>=1961)&(years<=2010)]))
assert abs(offset-0.18100777836)<1e-9, "Reference-period regression failure"
assert abs(vals[-1]-1.0732167)<1e-7, "2025 regression failure"
SRC="Met Office HadCRUT5 v5.2.0.0  /  1961-1990 reference"
ORIGINAL="https://collections.reading.ac.uk/art-collections/wp-content/uploads/sites/2/2021/10/UAC_11018-1200px.jpg"
def txt(fig,x,y,s,size=13,color=INK,weight="normal",ha="left",va="center"):
    fig.text(x,y,s,fontsize=size,color=color,weight=weight,ha=ha,va=va)
def rule(fig,x,y,w,color=GRID,lw=1):
    fig.add_artist(Line2D([x,x+w],[y,y],color=color,lw=lw,transform=fig.transFigure))
def base(part,title,deck):
    fig=plt.figure(figsize=(8,8),dpi=240,facecolor=BG)
    txt(fig,.068,.954,"COFFEETABLEVIZ  /  ICONS OF DATA",10.2,weight="bold",va="top")
    txt(fig,.932,.954,"07  /  ED HAWKINS",10,color=MUTED,ha="right",va="top")
    rule(fig,.068,.921,.864,color=INK,lw=1.2)
    txt(fig,.068,.871,title,28.0,weight="bold",va="top")
    txt(fig,.068,.812,deck,12.6,color=MUTED,va="top")
    rule(fig,.068,.083,.864,lw=1)
    txt(fig,.068,.052,"COFFEETABLEVIZ  /  ICONS OF DATA",9.8,weight="bold")
    txt(fig,.932,.052,"07  /  "+part,9.7,color=MUTED,ha="right")
    return fig
def save(fig,name):
    target=OUT/name
    fig.savefig(target,dpi=240,facecolor=BG)
    plt.close(fig)
    with Image.open(target) as im:
        assert im.size==(1920,1920), (target,im.size)
        for size in (600,390,320):
            im.resize((size,size),Image.Resampling.LANCZOS).save(OUT/(target.stem+f"_preview_{size}.png"))
    return {"sha256":sha256(target.read_bytes()).hexdigest(),"width":1920,"height":1920,"bytes":target.stat().st_size}
def figure1():
    req=urllib.request.Request(ORIGINAL,headers={"User-Agent":"Mozilla/5.0 Coffeetableviz non-commercial editorial attribution"})
    with urllib.request.urlopen(req,timeout=45) as resp: data=resp.read()
    if len(data)<15000: raise ValueError("University image download unexpectedly small")
    original=Image.open(BytesIO(data)).convert("RGB")
    if original.width<900 or original.height<400:raise ValueError("Wrong historical image dimensions")
    op=OUT/"01_reading_global_2020_original_unmodified.jpg"
    op.write_bytes(data)
    fig=base("01  /  ORIGINAL","The chart without an axis.","Ed Hawkins turned annual temperatures into colour alone.")
    ax=fig.add_axes([.072,.300,.856,.395],facecolor=BG)
    ax.imshow(original,interpolation="nearest",aspect="equal")
    ax.axis("off")
    txt(fig,.080,.740,"GLOBAL TEMPERATURE STRIPES  /  1850-2020",12,weight="bold")
    txt(fig,.080,.247,"ONE VERTICAL STRIPE REPRESENTS ONE YEAR",12,weight="bold")
    txt(fig,.080,.210,"The original University of Reading artwork, displayed unaltered.",11.1,color=MUTED)
    txt(fig,.080,.173,"This historic edition ends in 2020, not 2025.",11.1,color=MUTED)
    txt(fig,.080,.131,"Ed Hawkins · University of Reading Art Collection UAC/11018",9.4,color=MUTED)
    meta=save(fig,"01_the_original_warming_stripes.png")
    meta["original_sha256"]=sha256(data).hexdigest()
    meta["original_dimensions"]=[original.width,original.height]
    return meta
def figure2():
    fig=base("02  /  RECONSTRUCTION","The years turn red.","The same 176 annual temperatures, shown two different ways.")
    txt(fig,.082,.753,"ONE YEAR  =  ONE STRIPE",11.7,weight="bold")
    ax=fig.add_axes([.085,.608,.830,.126])
    ax.imshow(vals[np.newaxis,:],cmap=CMAP,norm=NORM,aspect="auto",
              extent=[1849.5,2025.5,0,1],interpolation="nearest")
    ax.set_xlim(1849.5,2025.5);ax.set_axis_off()
    txt(fig,.086,.585,"1850",10.4,color=MUTED)
    txt(fig,.913,.585,"2025",10.4,color=MUTED,ha="right")
    txt(fig,.082,.535,"NOW ADD THE NUMBERS BACK",11.7,weight="bold")
    ax2=fig.add_axes([.125,.284,.740,.224],facecolor=BG)
    ax2.fill_between(years,lower,upper,color=TEAL,alpha=.20,lw=0,label="95% range")
    ax2.plot(years,vals,color=INK,lw=1.7,zorder=3,label="Annual estimate")
    ax2.axhline(0,color=MUTED,lw=.8,ls="--")
    ax2.scatter([2025],[vals[-1]],s=28,color="#C44E52",zorder=5)
    ax2.set_xlim(1850,2029);ax2.set_ylim(-.9,1.48)
    ax2.set_xticks([1850,1900,1950,2000,2025])
    ax2.set_yticks([-.5,0,.5,1])
    ax2.set_ylabel("Temperature anomaly (°C)",fontsize=10.1,labelpad=10)
    ax2.tick_params(length=0,labelsize=9.4,pad=6)
    ax2.grid(axis="y",color=GRID,lw=.7)
    for spine in ax2.spines.values():spine.set_visible(False)
    txt(fig,.810,.472,"2025",9.5,color="#B5444B",weight="bold")
    txt(fig,.086,.245,"Each band uses the same source year as the line below.",11.3)
    txt(fig,.086,.212,"Shading shows the Met Office published 95% uncertainty range.",10.3,color=MUTED)
    txt(fig,.086,.165,"Source: "+SRC,9.5,color=MUTED)
    txt(fig,.086,.138,"Fixed palette: -1.25 to +1.25°C · not a Reading replica.",9.5,color=MUTED)
    return save(fig,"02_the_century_shifts_colour.png")
def rectangle(fig,x,y,w,h,face=BG,edge=GRID,lw=1):
    fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,
              facecolor=face,edgecolor=edge,linewidth=lw))
def panel(fig,x,y,w,h,n,title,subtitle):
    rectangle(fig,x,y,w,h)
    txt(fig,x+.024,y+h-.033,n+"  "+title,11.1,weight="bold",va="top")
    txt(fig,x+.024,y+h-.069,subtitle,9.8,color=MUTED,va="top")
def figure3():
    fig=base("03  /  DECODER","Decode the Icon.","Four choices hiding inside a row of coloured stripes.")
    L=.068;gap=.022;W=(.864-gap)/2;H=.286
    places=[(L,.451),(L+W+gap,.451),(L,.150),(L+W+gap,.150)]
    descriptions=[
      ("01","One slot per year","Ten real annual observations."),
      ("02","Colour carries change","Shade follows temperature anomaly."),
      ("03","What the stripes hide","Degrees and uncertainty matter."),
      ("04","Which reference period?","Same 2025 data. Different zero.")]
    for (x,y),(n,h,s) in zip(places,descriptions):panel(fig,x,y,W,H,n,h,s)
    x,y=places[0]
    sel=(years>=2016)&(years<=2025)
    sv=vals[sel];sy=years[sel]
    ax=fig.add_axes([x+.034,y+.084,W-.068,.090])
    ax.imshow(sv[np.newaxis,:],cmap=CMAP,norm=NORM,aspect="auto",interpolation="nearest",extent=[2015.5,2025.5,0,1])
    ax.axis("off")
    txt(fig,x+.032,y+.064,"2016",9.7,color=MUTED)
    txt(fig,x+W-.032,y+.064,"2025",9.7,color=MUTED,ha="right")
    txt(fig,x+.032,y+.030,"Equal width. Chronological order.",9.3,color=MUTED)
    x,y=places[1]
    ax=fig.add_axes([x+.042,y+.105,W-.085,.073])
    a=np.linspace(-1.25,1.25,256)
    ax.imshow(a[np.newaxis,:],aspect="auto",cmap=CMAP,norm=NORM,
              extent=[-1.25,1.25,0,1]);ax.axis("off")
    txt(fig,x+.042,y+.083,"-1.25°C",9.5,color=MUTED)
    txt(fig,x+W/2,y+.083,"0°C",9.5,color=MUTED,ha="center")
    txt(fig,x+W-.042,y+.083,"+1.25°C",9.5,color=MUTED,ha="right")
    txt(fig,x+.040,y+.034,"Relative to 1961-1990 mean",9.4,color=MUTED)
    x,y=places[2]
    ax=fig.add_axes([x+.051,y+.084,W-.092,.095])
    m=years>=1980
    ax.fill_between(years[m],lower[m],upper[m],color=TEAL,alpha=.25)
    ax.plot(years[m],vals[m],lw=1.6,color=INK)
    ax.axhline(0,color=MUTED,lw=.7,ls="--")
    ax.set_xlim(1980,2025);ax.set_ylim(-.22,1.48)
    ax.set_xticks([1980,2000,2025]);ax.set_yticks([0,1])
    ax.tick_params(labelsize=8.2,length=0,pad=3)
    for sp in ax.spines.values():sp.set_visible(False)
    ax.grid(axis="y",lw=.6,color=GRID)
    txt(fig,x+.037,y+.040,"2025 = +1.07°C; with 95% limits",9.5,color=MUTED)
    x,y=places[3]
    txt(fig,x+.034,y+.158,"+1.07°C",20.2,weight="bold",color=INK)
    txt(fig,x+.224,y+.158,"vs",11.5,color=MUTED)
    txt(fig,x+.269,y+.158,"+0.89°C",18.9,weight="bold",color="#C44E52")
    txt(fig,x+.034,y+.112,"vs 1961-1990",9.3,color=MUTED)
    txt(fig,x+.266,y+.112,"vs 1961-2010",9.3,color=MUTED)
    rule(fig,x+.034,y+.088,W-.068)
    txt(fig,x+.034,y+.056,"Mean shift: +0.181°C; same 2025 value.",9.0,color=MUTED)
    txt(fig,x+.034,y+.030,"Rebasing changes the zero, not the climate.",9.0,color=MUTED)
    txt(fig,.074,.122,"Source: "+SRC+"  |  2025 is last complete year.",9.1,color=MUTED)
    txt(fig,.074,.103,"The examples use HadCRUT5, not Reading's original series.",9.1,color=MUTED)
    return save(fig,"03_decode_the_icon.png")
def main():
    figures={}
    for name,fn in (("01",figure1),("02",figure2),("03",figure3)):
        figures[name]=fn()
    report={"run_scope":"REVIEW ONLY — no website publication",
      "original_url":ORIGINAL,"original_provenance":"UAC/11018, Ed Hawkins, University of Reading, 2021 digitisation of Global 2020",
      "data_source":"HadCRUT.5.2.0.0 analysis global annual; 19 Oct 2026 source snapshot",
      "native_baseline":"1961-1990","start_year":1850,"end_year":2025,
      "observations":len(rows),"year_2026_excluded":True,
      "reference_1961_2010_offset_C":offset,"value_2025_C":float(vals[-1]),
      "color_scale_C":[-1.25,1.25],"illustration_not_identical_to_reading":True,
      "source_csv_sha256":sha256(DATA.read_bytes()).hexdigest(),
      "figures":figures}
    (ROOT/"qa"/"render_manifest.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf8")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
