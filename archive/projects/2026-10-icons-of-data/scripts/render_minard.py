"""Deterministic editorial reconstructions of Charles Joseph Minard's 1869 chart.

Original map is represented separately, unmodified, from Wikimedia Commons:
https://commons.wikimedia.org/wiki/File:Minard.png

Data: HistData/Minard.troops, Minard.cities, Minard.temp (via Rdatasets).
All figures are historical plot estimates; temperature in degrees Reaumur (°Ré).
No historical facts or dates are inferred from missing cells.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon, Rectangle
from matplotlib.lines import Line2D

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'
OUT=ROOT/'visuals'
OUT.mkdir(parents=True,exist_ok=True)
troops=pd.read_csv(DATA/'minard_troops.csv')
cities=pd.read_csv(DATA/'minard_cities.csv')
temp=pd.read_csv(DATA/'minard_temperature.csv')

# Source QA: no spurious points, numeric columns, missing dates retained
assert len(troops)==51 and len(cities)==20 and len(temp)==9
assert troops.groupby(['group','direction'], sort=False).size().sum()==51
assert int(temp.date.isna().sum())==1
assert set(troops.direction)=={'A','R'}
assert troops.survivors.min()>=0
assert all(troops.groupby(['group','direction']).size()>=2)
assert troops.iloc[0].survivors==340000 and troops.iloc[15].survivors==100000
assert troops[(troops.group==1)&(troops.direction=='R')].iloc[-1].survivors==4000
assert temp['temp'].min()==-30
assert [int(troops[(troops.direction=='A') & (troops.group==i)].iloc[0].survivors) for i in (1,2,3)]==[340000,60000,22000]

BG='#F3F4F6'; TEXT='#16191B'; SECOND='#5D636B'; GRID='#DCE0E4'; BEIGE='#D7B38A'; BLACK='#24272B'; TEAL='#1F8FA8'; RED='#C44E52'
plt.rcParams.update({'font.family':'DejaVu Sans','text.color':TEXT,'axes.facecolor':BG,'figure.facecolor':BG,
                     'savefig.facecolor':BG,'axes.edgecolor':GRID,'axes.labelcolor':SECOND,
                     'xtick.color':SECOND,'ytick.color':SECOND,'font.size':10})

def ribbon(ax, subset, color, scale=1.33, zorder=3, alpha=1):
    """Smooth segmented line: stroke *width* linear in troop estimates.

    Draw each segment at its mean endpoint value and place round joins sized to the
    values at each source vertex. This avoids polygon self-intersections at turns.
    The display thickness remains a proportional encoding, not proportional area.
    """
    x=subset['long'].to_numpy(dtype=float); y=subset['lat'].to_numpy(dtype=float)
    count=subset.survivors.to_numpy(dtype=float)
    widths=(count/10000)*scale
    for i in range(len(x)-1):
        ax.plot(x[i:i+2],y[i:i+2],linewidth=(widths[i]+widths[i+1])/2,
                color=color,alpha=alpha,solid_capstyle='round',zorder=zorder)
    for xx,yy,ww in zip(x,y,widths):
        ax.plot([xx],[yy],marker='o',markersize=ww,markeredgewidth=0,
                markerfacecolor=color,alpha=alpha,zorder=zorder)


def base_map(ax):
    ax.set_xlim(23.4,38.5);ax.set_ylim(53.6,56.3)
    ax.set_xticks([24,28,32,36]); ax.set_xticklabels([])
    ax.set_yticks([])
    for sp in ax.spines.values():sp.set_visible(False)
    ax.grid(axis='x',color=GRID,linewidth=0.7,zorder=0)
    ax.tick_params(axis='x',length=0,labelsize=9,pad=7)

def paths(ax, groups=(1,2,3), width=True, direction=True, scale=1.33):
    ax.figure.canvas.draw() # needed for display-space width geometry
    for direction_name in ('A','R'):
        for group in groups:
            chunk=troops[(troops.direction==direction_name)&(troops.group==group)]
            if chunk.empty:continue
            col=BEIGE if direction_name=='A' else BLACK
            if width:ribbon(ax,chunk,col,scale=scale,zorder=2 if direction_name=='A' else 3)
            else:ax.plot(chunk['long'],chunk.lat,color=col if direction else TEAL,linewidth=2,solid_joinstyle='round',zorder=3)

def footer(fig,note):
    fig.text(.085,.067,'COFFEETABLEVIZ  /  ICONS OF DATA',fontsize=9.5,fontweight='bold',color=TEXT,ha='left')
    fig.text(.915,.067,'01  /  MINARD · 1869',fontsize=9,color=SECOND,ha='right')
    fig.add_artist(Line2D([.085,.915],[.095,.095],transform=fig.transFigure,lw=.8,color='#CBD0D4'))
    fig.text(.085,.105,note,fontsize=8,color=SECOND,ha='left')

def draw_fig2():
    fig=plt.figure(figsize=(8,8),dpi=240)
    fig.text(.085,.94,'One journey. A shrinking army.',fontsize=23.5,fontweight='bold',va='top')
    fig.text(.085,.884,"Line width represents Minard's estimated troop strength — not a death toll.",fontsize=11,color=SECOND,va='top')
    # legend
    fig.add_artist(Line2D([.09,.128],[.827,.827],transform=fig.transFigure,lw=8,color=BEIGE,solid_capstyle='butt'))
    fig.text(.142,.827,'Into Russia',fontsize=10.5,va='center',color=TEXT)
    fig.add_artist(Line2D([.35,.389],[.827,.827],transform=fig.transFigure,lw=5,color=BLACK,solid_capstyle='butt'))
    fig.text(.406,.827,'Retreat',fontsize=10.5,va='center',color=TEXT)
    fig.text(.913,.827,'THREE ROUTE GROUPS',fontsize=8.5,color=SECOND,ha='right',va='center')
    ax=fig.add_axes([.085,.397,.83,.392]);base_map(ax);paths(ax)
    names={'Kowno':(24,55),'Smolensk':(32,54.8),'Moscou':(37.6,55.8),'Polotzk':(28.7,55.5)}
    for name,(x,y) in names.items():
        if name=='Moscou':dx,dy=-.25,.30;ha='right'
        elif name=='Kowno':dx,dy=.30,.90;ha='left'
        elif name=='Smolensk':dx,dy=.2,-.49;ha='left'
        else: dx,dy=.1,.36;ha='left'
        ax.annotate('MOSCOW' if name=='Moscou' else name.upper(),xy=(x,y),xytext=(x+dx,y+dy),fontsize=9,weight='bold',color=TEXT,
                    ha=ha,va='center',arrowprops=dict(arrowstyle='-',lw=.75,color=SECOND),zorder=9)
    # note under upper map
    fig.text(.085,.369,'At the western start: 340k + 60k + 22k = 422k across three plotted groups.',
             color=SECOND,fontsize=9.5)
    # temp plot; 9 existing values only (no inferred date)
    fig.text(.085,.315,'THE RETREAT GETS COLDER',fontsize=10.5,color=TEXT,weight='bold')
    fig.text(.915,.315,'Temperature (°Réaumur)',fontsize=9,color=SECOND,ha='right')
    temp_ax=fig.add_axes([.085,.17,.83,.119]);temp_ax.set_xlim(23.4,38.5);temp_ax.set_ylim(-34,5)
    temp_ax.grid(axis='y',color=GRID,lw=.7)
    temp_ax.plot(temp['long'],temp['temp'],color=RED,lw=2.3,marker='o',markersize=4.5,solid_capstyle='round',zorder=3)
    temp_ax.set_yticks([0,-15,-30]);temp_ax.set_yticklabels(['0°','−15°','−30°'],fontsize=9)
    temp_ax.set_xticks([])
    temp_ax.tick_params(length=0,pad=6)
    for sp in temp_ax.spines.values():sp.set_visible(False)
    temp_ax.annotate('18 Oct · 0°Ré',(37.6,0),xytext=(-3,7),textcoords='offset points',ha='right',fontsize=8.5,color=SECOND)
    temp_ax.annotate('6 Dec · −30°Ré',(26.7,-30),xytext=(4,-6),textcoords='offset points',fontsize=8.5,color=RED,weight='bold',va='top')
    footer(fig,'Source: Minard (1869), HistData digitisation · °Ré = degrees Réaumur · map positions approximate')
    name=OUT/'02_shrinking_army.png';fig.savefig(name,dpi=240);plt.close(fig)
    return name

def small_panel(fig,rect,title,subtitle):
    x,y,w,h=rect
    fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,fill=False,edgecolor='#D5DADE',lw=.95))
    fig.text(x+.025,y+h-.044,title,fontsize=12.5,fontweight='bold',va='top',color=TEXT)
    fig.text(x+.025,y+h-.080,subtitle,fontsize=9,va='top',color=SECOND)
    return fig.add_axes([x+.036,y+.040,w-.072,h-.155])

def draw_fig3():
    fig=plt.figure(figsize=(8,8),dpi=240)
    fig.text(.085,.94,'One map. Four different jobs.',fontsize=23.5,fontweight='bold',va='top')
    fig.text(.085,.883,'Pull Minard’s graphic apart and the design decisions become visible.',fontsize=11,color=SECOND,va='top')
    r1=[.085,.479,.398,.343];r2=[.517,.479,.398,.343]
    r3=[.085,.123,.398,.343];r4=[.517,.123,.398,.343]
    ax1=small_panel(fig,r1,'01   Position','Geography locates the journey')
    ax2=small_panel(fig,r2,'02   Width','Thicker line = more men')
    ax3=small_panel(fig,r3,'03   Colour','Pale out. Dark back.')
    ax4=small_panel(fig,r4,'04   Temperature','A second view of the retreat')
    for ax in [ax1,ax2,ax3]:
        ax.set_xlim(23.4,38.5);ax.set_ylim(53.8,56.25)
        ax.set_xticks([]);ax.set_yticks([])
        for sp in ax.spines.values():sp.set_visible(False)
    # Panel1: geographic position, both plotted routes without width
    for grp in (1,2,3):
        for direction_name in ('A','R'):
            g=troops[(troops.group==grp)&(troops.direction==direction_name)]
            ax1.plot(g['long'],g['lat'],lw=1.6,color=TEAL,alpha=.85)
    ax1.text(24,54.15,'KOWNO',fontsize=8,color=SECOND,va='top')
    ax1.text(37.5,56.05,'MOSCOW',fontsize=8,color=SECOND,ha='right')
    # Panel2: varying width shows troop estimates for main advancing group
    g=troops[(troops.group==1)&(troops.direction=='A')]
    fig.canvas.draw()
    ribbon(ax2,g,BEIGE,scale=.68,zorder=3)
    ax2.text(24.05,53.93,'340,000',fontsize=10.4,color=TEXT,weight='bold')
    ax2.text(37.35,56.07,'100,000',fontsize=10.4,color=TEXT,weight='bold',ha='right')
    # Panel3: direction + contrast; same source geometry but constant thickness
    for direction_name,col in [('A',BEIGE),('R',BLACK)]:
        g=troops[(troops.group==1)&(troops.direction==direction_name)]
        ax3.plot(g['long'],g['lat'],lw=4.3,color=col,solid_capstyle='round',zorder=3)
    ax3.text(24,55.63,'ADVANCE →',fontsize=8.3,color=TEXT)
    ax3.text(24,54.07,'← RETREAT',fontsize=8.3,color=TEXT)
    # Panel4: x is true digitised longitude not time; labels are individual source dates.
    ax4.set_xlim(24.1,38.4);ax4.set_ylim(-35,5)
    ax4.plot(temp['long'],temp['temp'],color=RED,marker='o',markersize=4,lw=2)
    ax4.set_xticks([25,31,37]);ax4.set_xticklabels(['WEST','', 'EAST'],fontsize=7.7)
    ax4.set_yticks([0,-15,-30]);ax4.set_yticklabels(['0°Ré','−15°Ré','−30°Ré'],fontsize=8)
    ax4.grid(axis='y',lw=.65,color=GRID)
    ax4.tick_params(length=0,pad=4)
    for sp in ax4.spines.values():sp.set_visible(False)
    ax4.annotate('6 Dec',xy=(26.7,-30),xytext=(7,5),textcoords='offset points',fontsize=8,color=RED,fontweight='bold')
    footer(fig,'From Minard (1869), reconstructed with HistData · not a modern historical estimate')
    name=OUT/'03_decode_the_icon.png';fig.savefig(name,dpi=240);plt.close(fig)
    return name

if __name__=='__main__':
 for f in (draw_fig2(),draw_fig3()):
  from PIL import Image
  im=Image.open(f);print('rendered:',f,'dimensions:',im.size,'bytes:',f.stat().st_size)
 print('QA: datasets 51/20/9; groups 3; 1 missing temperature date retained; °Ré labels; historic source notes')
