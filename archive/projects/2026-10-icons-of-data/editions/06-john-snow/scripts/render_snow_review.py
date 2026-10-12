"""Render John Snow #06 review charts from pinned HistData CSVs.

Authentic historical original is retrieved separately, never reconstructed by this
file. Custom cartographic renderer stays local to this edition; shared 538 config
is not modified. Local drawing coordinates are not latitude/longitude.
"""
from pathlib import Path
from collections import defaultdict
import csv, math, hashlib, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
OUT=ROOT/"qa"/"visuals"
OUT.mkdir(parents=True,exist_ok=True)
BG="#F3F4F6"; TEXT="#111111"; SUB="#59636D"; GRID="#D5D9DE"
TEAL="#1F8FA8"; RED="#C44E52"; CHARCOAL="#252B2E"; STREETS="#C4CBD1"
plt.rcParams.update({"font.family":"Inter","figure.facecolor":BG,"savefig.facecolor":BG,
"font.size":12,"text.color":TEXT,"axes.labelcolor":SUB,"xtick.color":SUB,"ytick.color":SUB})

def load(name):
    with (DATA/name).open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
deaths=load("Snow.deaths.csv")
pumps=load("Snow.pumps.csv")
streets=load("Snow.streets.csv")
assert len(deaths)==578 and len(pumps)==13 and len(streets)==1241
assert len({r["street"] for r in streets})==528
broad=[r for r in pumps if r["label"]=="Broad St"]
assert len(broad)==1 and int(broad[0]["pump"])==7

def t(fig,x,y,content,size=13,color=TEXT,weight=None,ha="left",va="center"):
    fig.text(x,y,content,fontsize=size,color=color,fontweight=weight,va=va,ha=ha)
def line(fig,x1,y1,x2,y2,color=GRID,width=1):
    fig.add_artist(Line2D([x1,x2],[y1,y2],lw=width,color=color,transform=fig.transFigure))
def frame(edition):
    fig=plt.figure(figsize=(8,8),dpi=240,facecolor=BG)
    t(fig,.067,.951,"COFFEETABLEVIZ  /  ICONS OF DATA",11.1,weight="bold",va="top")
    t(fig,.933,.951,"06  /  JOHN SNOW",11,color=SUB,ha="right",va="top")
    line(fig,.067,.924,.933,.924,color=TEXT,width=1.3)
    return fig
def heading(fig,title,subtitle):
    t(fig,.067,.865,title,29.7,weight="bold",va="top")
    t(fig,.067,.798,subtitle,15.2,color=SUB,va="top")
def footer(fig,part,source):
    t(fig,.067,.102,source,9.1,color=SUB)
    line(fig,.067,.077,.933,.077,width=.95)
    t(fig,.067,.053,"COFFEETABLEVIZ  /  ICONS OF DATA",10.0,weight="bold")
    t(fig,.933,.053,f"06  /  JOHN SNOW  ·  {part}",10,color=SUB,ha="right")
def save(fig,name):
    p=OUT/name
    fig.savefig(p,dpi=240,facecolor=BG)
    plt.close(fig)
    im=Image.open(p)
    assert im.size==(1920,1920)
    return p

def chart2():
    fig=frame("06")
    heading(fig,"The pattern, mapped.","A pump at the centre of an uncomfortable question.")
    t(fig,.108,.739,"SOHO, LONDON  ·  1854",11.2,weight="bold",color=SUB)
    # Visible key (not a clinical risk or distance metric).
    t(fig,.119,.704,"■",12,color=CHARCOAL);t(fig,.139,.704,"Mapped fatal attack",10.1)
    t(fig,.420,.704,"✚",14,color=TEAL);t(fig,.440,.704,"Other water pumps",10.1)
    t(fig,.714,.704,"◆",12,color=RED);t(fig,.735,.704,"Broad St pump",10.1)
    ax=fig.add_axes([.105,.236,.790,.438],facecolor=BG)
    bystreet=defaultdict(list)
    for r in streets:bystreet[r["street"]].append((float(r["x"]),float(r["y"])))
    for r in bystreet.values():
        ax.plot([p[0] for p in r],[p[1] for p in r],lw=.88,c=STREETS,zorder=1,solid_capstyle="round")
    ax.scatter([float(r["x"]) for r in deaths],[float(r["y"]) for r in deaths],
        s=10,marker="s",c=CHARCOAL,edgecolors="none",zorder=3,alpha=.96)
    other=[r for r in pumps if r["label"]!="Broad St"]
    ax.scatter([float(r["x"]) for r in other],[float(r["y"]) for r in other],
               marker="+",s=61,linewidths=1.85,c=TEAL,zorder=5)
    bx=float(broad[0]["x"]);by=float(broad[0]["y"])
    ax.scatter([bx],[by],marker="D",s=85,c=RED,edgecolors=BG,linewidths=1.3,zorder=7)
    ax.annotate("BROAD STREET\nPUMP",xy=(bx,by),xytext=(bx+2.4,by-2.1),
                ha="left",va="center",fontsize=10.2,fontweight="bold",color=RED,
                bbox=dict(boxstyle="square,pad=.23",facecolor=BG,edgecolor="none",alpha=.95),
                arrowprops=dict(arrowstyle="-",color=RED,lw=1.45),zorder=9)
    ax.set_xlim(3.15,20.05);ax.set_ylim(3.0,18.95)
    ax.set_aspect("equal",adjustable="box")
    ax.axis("off")
    t(fig,.107,.199,"578 digitised fatal-attack marks  ·  13 mapped pumps",13.0,weight="bold")
    t(fig,.107,.165,"Locations are reconstructed map coordinates, not GPS.",11.3,color=SUB)
    t(fig,.107,.133,"No population denominators → these marks are not mortality rates.",10.9,color=SUB)
    footer(fig,"02","Source: HistData / John Snow · 1855 book map digitisation")
    return save(fig,"02_the_pattern_mapped.png")

def panel(fig,x,y,w,h,n,title,subtitle):
    fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,edgecolor=GRID,facecolor=BG,lw=1.15))
    t(fig,x+.023,y+h-.040,n+"  "+title,12.7,weight="bold",va="top")
    t(fig,x+.023,y+h-.083,subtitle,10.5,color=SUB,va="top")
def chart3():
    fig=frame("06")
    heading(fig,"Decode the Icon.","Four things the pattern can—and cannot—tell us.")
    L=.067;G=.022;W=(.866-G)/2;H=.284
    xy=[(L,.460),(L+W+G,.460),(L,.158),(L+W+G,.158)]
    meta=[
      ("01","Mark the deaths","One short bar per fatal attack."),
      ("02","Locate the pumps","A route is more than a straight line."),
      ("03","Counts are not rates","No population denominator on the map."),
      ("04","The dates are missing","The map is not a time series.")
    ]
    for (x,y),(n,title,sub) in zip(xy,meta):panel(fig,x,y,W,H,n,title,sub)
    x,y=xy[0]
    # Schematic street + house: intentionally not a replica of any historical address.
    line(fig,x+.059,y+.122,x+W-.06,y+.122,color=STREETS,width=2.7)
    fig.add_artist(Rectangle((x+.152,y+.132),.063,.050,facecolor="#E8EAED",edgecolor=STREETS,transform=fig.transFigure,lw=1))
    for j in range(4):
        fig.add_artist(Rectangle((x+.158+j*.012,y+.139),.008,.031,
                   facecolor=CHARCOAL,edgecolor="none",transform=fig.transFigure))
    t(fig,x+.043,y+.056,"Four drawn bars = four deaths",10.6,color=CHARCOAL)
    t(fig,x+.043,y+.025,"Illustrative address, not source data",9.3,color=SUB)
    x,y=xy[1]
    # Schematic disconnected crossing lines and water-pump symbol.
    line(fig,x+.055,y+.103,x+W-.055,y+.103,color=STREETS,width=2.4)
    line(fig,x+.116,y+.031,x+.116,y+.177,color=STREETS,width=2.4)
    line(fig,x+.270,y+.045,x+.270,y+.157,color=STREETS,width=2.4)
    fig.add_artist(Circle((x+.116,y+.103),.014,transform=fig.transFigure,color=RED))
    fig.add_artist(Circle((x+.270,y+.103),.013,transform=fig.transFigure,facecolor=BG,edgecolor=TEAL,lw=2.2))
    t(fig,x+.050,y+.025,"Close on paper ≠ water used",10.4,color=SUB)
    x,y=xy[2]
    t(fig,x+.044,y+.147,"6 deaths",20.5,weight="bold",color=CHARCOAL)
    t(fig,x+.237,y+.148,"÷",20.5,color=SUB)
    t(fig,x+.298,y+.146,"? people",16.7,weight="bold",color=RED)
    line(fig,x+.044,y+.107,x+W-.045,y+.107,color=GRID)
    t(fig,x+.044,y+.073,"You need people at risk",11,color=TEXT)
    t(fig,x+.044,y+.042,"to calculate a rate.",11,color=SUB)
    t(fig,x+.044,y+.017,"Illustrative figures only",9,color=SUB)
    x,y=xy[3]
    t(fig,x+.044,y+.152,"8 SEPT 1854",16.9,color=TEAL,weight="bold")
    t(fig,x+.044,y+.105,"Broad Street handle removed",10.4,color=TEXT)
    line(fig,x+.044,y+.083,x+W-.044,y+.083)
    t(fig,x+.044,y+.052,"Outbreak already declining.",10.9,weight="bold")
    t(fig,x+.044,y+.022,"No dates attached to map marks.",10.1,color=SUB)
    t(fig,.067,.122,"What matters: place, counting, access — and evidence beyond the map.",10.15,color=SUB)
    footer(fig,"03","Source: Snow (1855) · HistData · schematic decoder")
    return save(fig,"03_decode_the_icon.png")
def main():
    entries={}
    for path in (chart2(),chart3()):
        im=Image.open(path)
        entries[path.name]={"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"dimensions":im.size,"bytes":path.stat().st_size}
        for width in (600,390,320):
            p=OUT/f"{path.stem}_preview_{width}.png"
            im.resize((width,width),Image.Resampling.LANCZOS).save(p)
    (ROOT/"qa"/"render_manifest.json").write_text(json.dumps({"scope":"visual-review only","figures":entries,"counts":{"mapped_marks":len(deaths),"pumps":len(pumps),"street_polyline_groups":len({r['street'] for r in streets})},"background":BG,"notes":["map coordinates are local diagram coords, not GPS","no fabricated rates / timeline","figure 3 diagrams all schematic"]},indent=2)+"\n")
    print(json.dumps(entries,indent=2))
if __name__=="__main__":main()
