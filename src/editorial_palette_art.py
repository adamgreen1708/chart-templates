"""Comic-book editorial treatments for the existing, data-driven palette_story.

One colour chip means one coded colour; one equal wheel wedge means one
character. No image model, logos, percentage-of-fabric claims, or hardcoded
character identities. Layout text comes only from the dataset and config.
"""
import math
from matplotlib.colors import to_rgb
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, Wedge, Circle, Polygon

BG="#F3F4F6"
INK="#111111"
MUTED="#555555"
PANEL="#E9EDF0"
RULE="#CDD2D8"
HERO="#1F8FA8"
VILLAIN="#C44E52"

def txt(fig,x,y,s,size=12,bold=False,color=INK,align="left",zorder=8):
    return fig.text(x,y,str(s),transform=fig.transFigure,
        ha=align,va="center",fontsize=size,fontweight="bold" if bold else "normal",
        color=color,zorder=zorder)

def rect(fig,x,y,w,h,color,border=None,lw=0,z=2):
    patch=Rectangle((x,y),w,h,transform=fig.transFigure,facecolor=color,
        edgecolor=border if border else color,linewidth=lw,zorder=z)
    fig.add_artist(patch)
    return patch

def line(fig,x0,y0,x1,y1,color=RULE,lw=.65,z=3):
    fig.add_artist(Line2D([x0,x1],[y0,y1],transform=fig.transFigure,
        color=color,lw=lw,zorder=z))

def hue(x):
    if not x or len(str(x))!=7 or str(x)[0]!="#":
        raise ValueError(f"Invalid palette hue: {x!r}")
    to_rgb(x)
    return x

def need(rows,columns,n):
    if len(rows)!=n:
        raise ValueError(f"Expected exactly {n} observed character rows, found {len(rows)}")
    for r in rows:
        if not set(columns).issubset(r):
            raise ValueError(f"Palette contract missing {set(columns)-set(r)}")

def render_comic_lineup(fig,rows,top,config):
    """Two opposing costume strips, each containing six individual named records."""
    cols=("role","sort_order","display","publisher","dominant_hex","secondary_hex","accent_hex")
    need(rows,cols,12)
    top=min(top,.724)
    # Character cards use equal-size chips; they explicitly do not mean fabric shares.
    rect(fig,.494,.233,.002,.440,"#B8BFC6",z=1)
    for role,x0,x1,accent in (("Hero",.09,.483,HERO),("Villain",.524,.91,VILLAIN)):
        group=sorted([r for r in rows if r["role"]==role],
                    key=lambda r:int(r["sort_order"]))
        if len(group)!=6 or [int(r["sort_order"]) for r in group]!=list(range(1,7)):
            raise ValueError(f"Lineup expected six {role} records sorted 1-6")
        txt(fig,x0,top-.018,"HEROES" if role=="Hero" else "VILLAINS",
            16.5,True,accent)
        txt(fig,x1,top-.018,"06",13.5,True,accent,"right")
        rect(fig,x0,top-.049,x1-x0,.005,accent,z=4)
        for i,r in enumerate(group):
            center=top-.103-i*.0715
            left=x0;right=x1
            rect(fig,left,center-.028,right-left,.061,PANEL,z=1)
            rect(fig,left,center-.028,.008,.061,hue(r["dominant_hex"]),z=2)
            txt(fig,left+.019,center+.014,r["display"],12.5,True)
            txt(fig,left+.019,center-.013,r["publisher"],9.6,False,MUTED)
            base=left+.221
            for j,k in enumerate(("dominant_hex","secondary_hex","accent_hex")):
                color=r.get(k)
                if color:
                    rect(fig,base+j*.0545,center-.020,.048,.038,
                        hue(color),border=INK if color.upper()=="#FFFFFF" else None,
                        lw=.4 if color.upper()=="#FFFFFF" else 0,z=4)
    txt(fig,.09,.207,"MAIN  /  SECOND  /  ACCENT",10.8,True,MUTED)
    txt(fig,.09,.171,"Equal chips show colour roles, not the amount of costume fabric.",
        10.6,False,MUTED)

def render_comic_wheels(fig,rows,top,config):
    """Two 12-slice categorical wheels. Each equally sized wedge is one character."""
    cols=("publisher","role","tile_index","primary_flag","dominant_hex","character")
    need(rows,cols,24)
    top=min(top,.728)
    for role,cx,accent in (("Hero",.295,HERO),("Villain",.710,VILLAIN)):
        group=[r for r in rows if r["role"]==role]
        if len(group)!=12:
            raise ValueError("Wheel requires exactly twelve "+role+" characters")
        records=[]
        counts={}
        for pub in ("DC","Marvel"):
            cohort=sorted([r for r in group if r["publisher"]==pub],
                        key=lambda r:int(r["tile_index"]))
            if len(cohort)!=6 or [int(r["tile_index"]) for r in cohort]!=list(range(1,7)):
                raise ValueError("Wheel requires six ordered "+pub+" "+role+" costumes")
            records.extend(cohort)
            counts[pub]=sum(int(r["primary_flag"]) for r in cohort)
        count=sum(counts.values())
        txt(fig,cx,top-.023,"HEROES" if role=="Hero" else "VILLAINS",
            16.5,True,accent,"center")
        line(fig,cx-.15,top-.051,cx+.15,top-.051,accent,1.4)
        cy=top-.251
        radius=.159
        for i,r in enumerate(records):
            # Every observed character gets precisely 30 degrees. Hue is categorical.
            a=90-30*(i+1);b=90-30*i
            wedge=Wedge((cx,cy),radius,a,b,width=.059,
                        transform=fig.transFigure,facecolor=hue(r["dominant_hex"]),
                        edgecolor=BG,linewidth=1.6,zorder=4)
            fig.add_artist(wedge)
        # Meaningful DC/Marvel divider rather than optical colour area estimates.
        for angle in (90,270):
            t=math.radians(angle)
            line(fig,cx+.101*math.cos(t),cy+.101*math.sin(t),
                 cx+.170*math.cos(t),cy+.170*math.sin(t),INK,1.1,5)
        fig.add_artist(Circle((cx,cy),.095,transform=fig.transFigure,
                              facecolor=BG,edgecolor=RULE,linewidth=.6,zorder=5))
        txt(fig,cx,cy+.012,f"{count}/12",26,True,INK,"center")
        txt(fig,cx,cy-.030,"primary hues",10.6,False,MUTED,"center")
        txt(fig,cx,cy-.189,f"DC  {counts['DC']}/6",12.7,True,accent,"center")
        txt(fig,cx,cy-.224,f"MARVEL  {counts['Marvel']}/6",12.7,True,accent,"center")
    txt(fig,.09,.196,"One slice = one character. Six DC, then six Marvel (clockwise).",
        11.0,False,INK)
    txt(fig,.09,.164,"Primaries = red, blue and yellow (traditional artist's colours).",
        10.8,False,MUTED)

def render_comic_showdowns(fig,rows,top,config):
    """Five matched-costume confrontations with supporting-colour differences."""
    cols=("pair_rank","shared_colour","shared_hex","hero_display",
          "hero_secondary","hero_secondary_hex","villain_display",
          "villain_secondary","villain_secondary_hex")
    need(rows,cols,5)
    data=sorted(rows,key=lambda r:int(r["pair_rank"]))
    if [int(x["pair_rank"]) for x in data]!=list(range(1,6)):
        raise ValueError("The five matched pairs need consecutive editorial ranks")
    top=min(top,.728)
    txt(fig,.105,top-.014,"HERO",15.2,True,HERO)
    txt(fig,.5,top-.014,"SHARED COLOUR",12.5,True,MUTED,"center")
    txt(fig,.895,top-.014,"VILLAIN",15.2,True,VILLAIN,"right")
    line(fig,.09,top-.045,.91,top-.045,INK,1.0)
    for i,r in enumerate(data):
        y=top-.115-i*.091
        rect(fig,.09,y-.032,.82,.078,PANEL,z=1)
        rect(fig,.09,y-.032,.006,.078,HERO,z=3)
        rect(fig,.904,y-.032,.006,.078,VILLAIN,z=3)
        txt(fig,.105,y+.017,r["hero_display"],13.4,True)
        txt(fig,.895,y+.017,r["villain_display"],13.4,True,INK,"right")
        txt(fig,.106,y-.014,"+ "+r["hero_secondary"],10.3,False,MUTED)
        txt(fig,.867,y-.014,"+ "+r["villain_secondary"],10.3,False,MUTED,"right")
        if r["hero_secondary_hex"]:
            color=hue(r["hero_secondary_hex"])
            rect(fig,.326,y-.023,.022,.021,color,
                 border=INK if color.upper()=="#FFFFFF" else None,
                 lw=.6 if color.upper()=="#FFFFFF" else 0,z=5)
        if r["villain_secondary_hex"]:
            color=hue(r["villain_secondary_hex"])
            rect(fig,.652,y-.023,.022,.021,color,
                 border=INK if color.upper()=="#FFFFFF" else None,
                 lw=.6 if color.upper()=="#FFFFFF" else 0,z=5)
        # Main costume hue repeats across both identities. The angular
        # 'battle strip' is a label, not a percentage or quantitative axis.
        c=hue(r["shared_hex"])
        points=[(.440,y+.037),(.560,y+.037),(.585,y+.006),
                (.560,y-.024),(.440,y-.024),(.415,y+.006)]
        poly=Polygon(points,closed=True,transform=fig.transFigure,
                    facecolor=c,edgecolor=BG,linewidth=1.2,zorder=6)
        fig.add_artist(poly)
        lum=sum(a*b for a,b in zip(to_rgb(c),(.2126,.7152,.0722)))
        txt(fig,.5,y+.005,r["shared_colour"].upper(),11.6,True,
            INK if lum>.52 else "#FFFFFF","center",zorder=9)
    txt(fig,.09,.187,"Same leading hue, different supporting colours.",11.4,False,INK)
    txt(fig,.09,.159,"Five selected pairings; shades are categorical, not measured.",
        10.3,False,MUTED)
