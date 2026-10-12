"""Icons of Data #05: approved colour-restored Coffeetableviz review artwork.

Deliberately scoped historical category colours, no changes to shared renderer defaults.
The original circa-1900 Library of Congress object must be reproduced from LoC,
not generated from this script. Re-rendered PNG pixels may vary by font backend.
"""
from pathlib import Path
import math, csv, hashlib, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from PIL import Image

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'visuals';OUT.mkdir(parents=True,exist_ok=True)
BG='#F3F4F6'; PRIMARY='#1F8FA8'; RED='#C44E52'
HIST_GREEN='#43855A'; HIST_BLUE='#2A83A6'; HIST_YELLOW='#D1A53A'
CONTEXT='#D9D9D9'; SECONDARY='#7A7A7A'; TEXT='#111111'
SUB='#555555'; GRID='#D9D9D9'
plt.rcParams.update({'font.family':'Inter','font.size':13,'text.color':TEXT,'figure.facecolor':BG,'savefig.facecolor':BG,'axes.labelcolor':SUB,'xtick.color':SUB,'ytick.color':SUB})
DPI=240
rows=[]
with open(ROOT/'population_1890_verified.csv',newline='',encoding='utf-8') as f:
    for r in csv.DictReader(f):
        rows.append(dict(label=r['category_display'],count=int(r['people'])))
rows=sorted(rows,key=lambda r:r['count'],reverse=True)
assert [r['count'] for r in rows]==[734952,78139,37699,8025]
assert sum(r['count'] for r in rows)==858815
pct=100*rows[0]['count']/sum(r['count'] for r in rows)
assert round(pct,1)==85.6

def fig0():
    fig=plt.figure(figsize=(8,8),dpi=DPI,facecolor=BG)
    fig.text(.067,.953,'COFFEETABLEVIZ  /  ICONS OF DATA',fontsize=11.2,fontweight='bold',va='top',color=TEXT)
    fig.text(.933,.953,'05  /  DU BOIS',fontsize=11.2,ha='right',va='top',color=SUB)
    fig.add_artist(Line2D([.067,.933],[.923,.923],transform=fig.transFigure,color=TEXT,lw=1.3))
    return fig

def tx(fig,x,y,txt,size=14,weight=None,color=TEXT,ha='left',va='center',**kw):
    return fig.text(x,y,txt,fontsize=size,fontweight=weight,ha=ha,va=va,color=color,**kw)

def footer(fig,which,source):
    fig.add_artist(Line2D([.067,.933],[.075,.075],transform=fig.transFigure,color=GRID,lw=1.0))
    tx(fig,.067,.053,'COFFEETABLEVIZ  /  ICONS OF DATA',10.2,weight='bold')
    tx(fig,.933,.053,f'05  /  DU BOIS  ·  {which}',10.2,color=SUB,ha='right')
    tx(fig,.067,.101,source,9.5,color=SUB)

def header(fig,title,subtitle):
    tx(fig,.067,.865,title,32,weight='bold',va='top')
    tx(fig,.067,.802,subtitle,16.0,color=SUB,va='top')

def chart2():
    fig=fig0()
    header(fig,'The spiral, unwound.','In 1890, 85.6% lived in the country and villages.')
    ax=fig.add_axes([.366,.323,.525,.395],facecolor=BG)
    vals=[r['count'] for r in rows]
    labels=[r['label'] for r in rows]
    yy=np.arange(4)
    ax.barh(yy,vals,color=[RED,HIST_GREEN,HIST_YELLOW,HIST_BLUE],height=.46,alpha=.98,zorder=3)
    ax.invert_yaxis()
    ax.set_xlim(0,850000)
    ax.set_ylim(3.65,-.65)
    ax.set_yticks(yy,labels=labels)
    ax.tick_params(axis='y',pad=14,length=0,labelsize=12.0)
    ax.set_xticks([0,200000,400000,600000,800000],labels=['0','200k','400k','600k','800k'])
    ax.tick_params(axis='x',length=0,pad=12,labelsize=11.0)
    ax.grid(axis='x',color=GRID,linewidth=.8,zorder=0)
    for sp in ax.spines.values():sp.set_visible(False)
    for i,count in enumerate(vals):
        ax.annotate(f'{count:,}',(count,i),xytext=(9,0),textcoords='offset points',ha='left',va='center',fontsize=12.0,fontweight='bold' if i==0 else 'normal',color=TEXT,zorder=9)
    tx(fig,.366,.754,'BLACK RESIDENTS OF GEORGIA  ·  1890',11.1,weight='bold',color=SUB)
    tx(fig,.067,.243,'734,952 of 858,815',19,weight='bold',color=TEXT)
    tx(fig,.067,.211,'were counted in the country and villages.',14.2,color=SUB)
    tx(fig,.067,.165,'Original-inspired colours. One common, zero-based scale.',12.2,color=SUB)
    footer(fig,'02','Source: Du Bois, c.1900 · LoC 2013650430 · US Census (1890)')
    out=OUT/'02_the_spiral_unwound_historic_palette.png';fig.savefig(out,dpi=DPI,facecolor=BG);plt.close(fig);return out

def panel(fig,x,y,w,h,num,title,subtitle):
    fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,facecolor=BG,edgecolor=GRID,lw=1.15))
    tx(fig,x+.023,y+h-.041,num+'   '+title,13.0,weight='bold',va='top')
    tx(fig,x+.023,y+h-.080,subtitle,10.8,color=SUB,va='top')

def chart3():
    fig=fig0()
    header(fig,'Decode the Icon.','Four choices that made a big number hard to ignore.')
    L=.067;G=.022;W=(.866-G)/2;H=.284
    coords=[(L,.461),(L+W+G,.461),(L,.159),(L+W+G,.159)]
    titles=[('01','Fit the page','A long mark curls into a spiral.'),('02','Use colour','Four groups. Four historic hues.'),('03','Print the count','The label gives us precision.'),('04','Define the groups','These are 1890 categories.')]
    for (x,y),(n,t,s) in zip(coords,titles):panel(fig,x,y,W,H,n,t,s)
    x,y=coords[0]
    fig.add_artist(Line2D([x+.047,x+.144],[y+.151,y+.151],transform=fig.transFigure,color=RED,lw=5,solid_capstyle='round'))
    tx(fig,x+.093,y+.114,'long mark',10.3,ha='center',color=SUB)
    tx(fig,x+.183,y+.151,'→',24,color=SECONDARY,ha='center')
    cx=x+.303;cy=y+.109;coords_sp=[]
    for t in np.linspace(0,4.6*np.pi,350):
        r=.043*(1-t/(4.6*np.pi))+.007
        coords_sp.append((cx+r*math.cos(t),cy+r*math.sin(t)))
    fig.add_artist(Line2D([p[0] for p in coords_sp],[p[1] for p in coords_sp],transform=fig.transFigure,color=RED,lw=4.5,solid_capstyle='round'))
    tx(fig,cx,y+.041,'coiled mark',10.3,ha='center',color=SUB)
    x,y=coords[1]
    original_palette=[(HIST_GREEN,'Cities over 10,000'),(HIST_BLUE,'Cities 5,000–10,000'),
                      (HIST_YELLOW,'Cities 2,500–5,000'),(RED,'Country and villages')]
    for j,(c,label) in enumerate(original_palette):
        yy=y+.158-j*.032
        fig.add_artist(Line2D([x+.046,x+.092],[yy,yy],transform=fig.transFigure,color=c,lw=5.8,solid_capstyle='round'))
        tx(fig,x+.113,yy,label,9.95,color=TEXT)
    tx(fig,x+.043,y+.027,'Colours echo the original artwork.',8.9,color=SUB)
    x,y=coords[2]
    tx(fig,x+.045,y+.140,'734,952',27,weight='bold',color=RED)
    tx(fig,x+.045,y+.094,'Country and villages',12.2,color=TEXT)
    fig.add_artist(Line2D([x+.044,x+W-.043],[y+.075,y+.075],transform=fig.transFigure,color=GRID,lw=.9))
    tx(fig,x+.045,y+.046,'You cannot read that exactly',10.8,color=SUB)
    tx(fig,x+.045,y+.023,'from the coil alone.',10.8,color=SUB)
    x,y=coords[3]
    tx(fig,x+.045,y+.139,'1890',27,weight='bold',color=PRIMARY)
    tx(fig,x+.173,y+.147,'Census categories',10.6,color=TEXT)
    tx(fig,x+.045,y+.085,'City-size boundaries then',10.8,color=SUB)
    tx(fig,x+.045,y+.059,'are not today’s definitions.',10.8,color=SUB)
    tx(fig,x+.045,y+.027,'One year is not a migration trend.',10.1,color=SUB)
    tx(fig,.067,.124,'What matters: space, colour, labels — and what the original categories meant.',10.1,color=SUB)
    footer(fig,'03','Source: Du Bois, c.1900 · LoC 2013650430 · schematic decoder')
    out=OUT/'03_decode_the_spiral_historic_palette.png';fig.savefig(out,dpi=DPI,facecolor=BG);plt.close(fig);return out

if __name__=='__main__':
    stats={}
    for path in [chart2(),chart3()]:
        im=Image.open(path)
        assert im.size==(1920,1920)
        stats[path.name]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'pixels':im.size,'bytes':path.stat().st_size}
    (ROOT/'qa' ).mkdir(exist_ok=True)
    for path in OUT.glob('*.png'):
        im=Image.open(path)
        for w in [600,390,320]:
            im.resize((w,w),Image.Resampling.LANCZOS).save(ROOT/'qa'/f'{path.stem}_{w}.png')
    (ROOT/'visual_manifest.json').write_text(json.dumps({'version':'house_historic_palette','spec':'spec/538_template_rules.md','source':'original LoC item 2013650430 / Census Table 25','values':rows,'total':sum(r['count'] for r in rows),'percentage':pct,'graphics':stats},indent=2)+'\n')
    print(json.dumps(stats,indent=2))
