"""Reusable, deterministic colour-palette editorial layouts for social_square.

The three layouts consume actual CSV rows from CHART_CONFIG. No measured
costume-area proportions, invented values, images, logos or character art.
Editorial example selections live in project scripts/data, never here.
"""
from pathlib import Path
from collections import Counter

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib.colors import to_rgb

BG="#F3F4F6"
INK="#111111"
MUTED="#555555"
RULE="#D4D8DB"
HERO="#1F8FA8"
VILLAIN="#C44E52"

def _require(rows, fields, expected):
    if len(rows)!=expected:
        raise ValueError(f"palette_story needs {expected} rows, got {len(rows)}")
    missing=set(fields)-set(rows[0]) if rows else set(fields)
    if missing:
        raise ValueError("palette_story missing columns: "+", ".join(sorted(missing)))

def _colour(code):
    """Reject unsupported or blank swatch values when called for a real hue."""
    if not code or not str(code).startswith("#") or len(str(code))!=7:
        raise ValueError(f"Missing/invalid swatch hex {code!r}")
    to_rgb(code)
    return str(code)

def _text(fig,x,y,value,fontsize=12,colour=INK,weight="normal",ha="left",va="center"):
    return fig.text(x,y,str(value),ha=ha,va=va,color=colour,fontsize=fontsize,
                    fontweight=weight,zorder=8)

def _swatch(fig,x,y,colour,w=.046,h=.03,border=False):
    fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,
            facecolor=_colour(colour),edgecolor=INK if border else BG,
            linewidth=0.5 if border else 0.65,zorder=4))

def _rule(fig,x1,y,x2,alpha=1):
    fig.add_artist(Line2D([x1,x2],[y,y],transform=fig.transFigure,
                           lw=.55,color=RULE,alpha=alpha,zorder=1))

def _heading(fig,top,word,x1,x2,colour):
    _text(fig,x1,top,word,fontsize=15.8,weight="bold",colour=colour)
    _rule(fig,x1,top-.027,x2)

def _footer_note(fig,s):
    _text(fig,.09,.165,s,fontsize=10.8,colour=MUTED)

def render_gallery(fig,rows,top,config):
    _require(rows,("role","sort_order","display","publisher",
                   "dominant_hex","secondary_hex","accent_hex"),12)
    groups={"Hero":[],"Villain":[]}
    for r in rows:
        if r["role"] not in groups:
            raise ValueError("Unexpected role "+str(r["role"]))
        groups[r["role"]].append(r)
    if any(len(x)!=6 for x in groups.values()):
        raise ValueError("Gallery requires six heroes and six villains")
    top=min(top,.721)
    sides=(("Hero",.09,.48,HERO,"HEROES"),("Villain",.53,.91,VILLAIN,"VILLAINS"))
    for role,x1,x2,role_colour,title in sides:
        _heading(fig,top,title,x1,x2,role_colour)
        selected=sorted(groups[role],key=lambda x:int(x["sort_order"]))
        if [int(r["sort_order"]) for r in selected]!=list(range(1,7)):
            raise ValueError("Gallery role order must be consecutive 1..6")
        for i,r in enumerate(selected):
            y=top-.071-i*.069
            _text(fig,x1,y+.010,r["display"],fontsize=13,weight="bold")
            _text(fig,x1,y-.021,r["publisher"],fontsize=9.8,colour=MUTED)
            for j,key in enumerate(("dominant_hex","secondary_hex","accent_hex")):
                code=r.get(key)
                if code:
                    _swatch(fig,x1+.223+j*.056,y-.022,code,w=.047,h=.035,
                            border=(str(code).upper()=="#FFFFFF"))
            _rule(fig,x1,y-.046,x2)
    _text(fig,.09,top-.505,"Reading each costume: MAIN  /  SECOND  /  ACCENT",
          fontsize=11.0,colour=MUTED)
    _footer_note(fig,"Swatches show colour roles, NOT costume-area percentages.")

def render_scorecard(fig,rows,top,config):
    _require(rows,("publisher","role","tile_index","primary_flag",
                   "dominant_hex","character"),24)
    top=min(top,.72)
    for role,x1,x2,accent in (("Hero",.09,.46,HERO),("Villain",.55,.91,VILLAIN)):
        group=[r for r in rows if r["role"]==role]
        if len(group)!=12: raise ValueError("Scorecard requires 12 "+role)
        primary=sum(int(r["primary_flag"]) for r in group)
        _text(fig,x1,top,role.upper()+"S",fontsize=16,colour=accent,weight="bold")
        _text(fig,x1,top-.083,str(primary),fontsize=48,weight="bold")
        _text(fig,x1+.104,top-.089,"/ 12",fontsize=24,colour=MUTED)
        _text(fig,x1,top-.147,"PRIMARY DOMINANT",fontsize=10.8,colour=MUTED,weight="bold")
        _rule(fig,x1,top-.167,x2)
        for gi,pub in enumerate(("DC","Marvel")):
            sub=sorted([r for r in group if r["publisher"]==pub],
                       key=lambda r:int(r["tile_index"]))
            if len(sub)!=6 or [int(r["tile_index"]) for r in sub]!=list(range(1,7)):
                raise ValueError("Expected six uniquely ordered characters in "+pub+" "+role)
            label_y=top-.217-gi*.158
            _text(fig,x1,label_y,pub,fontsize=12.3,weight="bold")
            count=sum(int(r["primary_flag"]) for r in sub)
            _text(fig,x2,label_y,f"{count} / 6",fontsize=12.1,
                  colour=accent,ha="right",weight="bold")
            for ix,r in enumerate(sub):
                xx=x1+ix*.0605
                yy=label_y-.088
                _swatch(fig,xx,yy,r["dominant_hex"],w=.053,h=.057)
                # Tight black rule under a primary tile, no misleading ratios.
                if int(r["primary_flag"]):
                    fig.add_artist(Line2D([xx,xx+.053],[yy-.008,yy-.008],
                        transform=fig.transFigure,color=INK,lw=1.6,zorder=5))
    _text(fig,.09,.207,"Each block is ONE character's main costume colour.",fontsize=11.0,
          colour=INK)
    _footer_note(fig,"Black underline = red, yellow or blue (traditional RYB primary).")

def render_twins(fig,rows,top,config):
    _require(rows,("pair_rank","shared_colour","shared_hex",
        "hero_display","hero_secondary","hero_secondary_hex",
        "villain_display","villain_secondary","villain_secondary_hex"),5)
    ordered=sorted(rows,key=lambda r:int(r["pair_rank"]))
    if [int(r["pair_rank"]) for r in ordered]!=list(range(1,6)):
        raise ValueError("Twin pair ranks must be 1..5")
    top=min(top,.72)
    _heading(fig,top,"HERO",.09,.36,HERO)
    _heading(fig,top,"MATCHING HUE",.415,.635,MUTED)
    _heading(fig,top,"VILLAIN",.68,.91,VILLAIN)
    for i,r in enumerate(ordered):
        y=top-.085-i*.079
        colour=_colour(r["shared_hex"])
        _text(fig,.09,y+.009,r["hero_display"],fontsize=14.2,weight="bold")
        _text(fig,.09,y-.019,
              "plus "+(r["hero_secondary"] or "no second hue"),
              fontsize=10.9,colour=MUTED)
        if r["hero_secondary_hex"]:
            _swatch(fig,.312,y-.029,r["hero_secondary_hex"],w=.021,h=.018,
                    border=str(r["hero_secondary_hex"]).upper()=="#FFFFFF")
        _text(fig,.68,y+.009,r["villain_display"],fontsize=14.2,weight="bold")
        _text(fig,.68,y-.019,
              "plus "+(r["villain_secondary"] or "no second hue"),
              fontsize=10.9,colour=MUTED)
        if r["villain_secondary_hex"]:
            _swatch(fig,.881,y-.029,r["villain_secondary_hex"],w=.021,h=.018,
                    border=str(r["villain_secondary_hex"]).upper()=="#FFFFFF")
        fig.add_artist(Line2D([.34,.45],[y,y],transform=fig.transFigure,
                               lw=1.25,color=RULE,zorder=1))
        fig.add_artist(Line2D([.60,.67],[y,y],transform=fig.transFigure,
                               lw=1.25,color=RULE,zorder=1))
        _swatch(fig,.45,y-.019,colour,w=.15,h=.043)
        # Preserve readable label contrast for every swatch, including yellow.
        luminance=sum(t*w for t,w in zip(to_rgb(colour),(.2126,.7152,.0722)))
        _text(fig,.525,y+.002,r["shared_colour"].upper(),fontsize=11.9,
              weight="bold",colour="#FFFFFF" if luminance<.52 else INK,ha="center")
        _rule(fig,.09,y-.050,.91,alpha=.85)
    _text(fig,.09,.204,"Five coded pairings from the selected 24 costume versions.",
          fontsize=11.3,colour=INK)
    _footer_note(fig,"Shared colour = coded dominant hue; supporting colour can differ.")

def render_palette_story(repo_root,config,rows,add_header,add_footer,save):
    if config.get("render_profile")!="social_square":
        raise ValueError("palette_story requires the approved social_square profile")
    variant=config.get("layout_variant")
    render={"gallery":render_gallery,
            "scorecard":render_scorecard,
            "twins":render_twins}.get(variant)
    if render is None:
        raise ValueError("palette_story layout_variant must be gallery/scorecard/twins")
    fig=plt.figure(figsize=(8,8),facecolor=BG)
    top=add_header(fig,config["title"],config["subtitle"],config=config)
    render(fig,rows,top,config)
    add_footer(fig,config.get("footer_left","Adam Green | coffeetableviz"),
               config.get("source_text","Source: curated comic costume pilot"),
               config=config)
    return save(fig,repo_root,config)
