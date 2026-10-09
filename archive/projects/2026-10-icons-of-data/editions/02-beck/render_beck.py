"""Icons of Data 02 — deterministic, original 2013 London Underground teaching graphics.

Source: De Domenico et al. (PNAS, 2014) CoMuNeLab network dataset,
collected from TfL in 2013; ODbL 1.0 / Database Contents License 1.0.

Both figures are original editorial compositions, not a traced TfL or Beck map.
The diagrams use a 2013 ten-station / ten-edge subset, not 1933 lines.
"""
from pathlib import Path
import math, csv, hashlib
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, Circle, Polygon

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'inputs'
OUT=ROOT/'visuals'; OUT.mkdir(parents=True,exist_ok=True)
S=pd.read_csv(DATA/'stations_2013.csv')
E=pd.read_csv(DATA/'connections_2013.csv')
assert S.shape==(10,5) and E.shape==(10,3)
assert S.station_id.is_unique and not S[['latitude','longitude']].isna().any().any()
assert not E.duplicated().any()
assert set(E['from']).union(E['to'])==set(S.station_id)
assert E.line.value_counts().to_dict()=={'piccadilly':4,'bakerloo':3,'central':3}

BG='#F3F4F6'; TEXT='#17191C'; SUB='#535A64'; LIGHT='#D1D8DC'; TEAL='#1F8FA8'; RED='#C44E52'; INK='#3B3E43'; WHITE='#FFFFFF'; GOLD='#BBA181'
LINES={'central':TEAL,'bakerloo':INK,'piccadilly':RED}
SHORT={'bondstreet':'Bond Street','regentspark':"Regent's Park",'greenpark':'Green Park','oxfordcircus':'Oxford Circus',
       'charingcross':'Charing Cross','coventgarden':'Covent Garden','holborn':'Holborn',
       'tottenhamcourtroad':'Tottenham Ct Rd','piccadillycircus':'Piccadilly Circus','leicestersquare':'Leicester Square'}

clat=float(S.latitude.mean()); clon=float(S.longitude.mean())
GEO={row.station_id:((row.longitude-clon)*111.32*math.cos(math.radians(clat)),(row.latitude-clat)*111.32) for row in S.itertuples()}
SCHEM={
 'bondstreet':(.25,2.65),'oxfordcircus':(1.35,2.65),'tottenhamcourtroad':(2.55,2.65),'holborn':(3.95,2.65),
 'regentspark':(1.35,4.35),'piccadillycircus':(1.35,1.25),'charingcross':(1.35,.28),
 'greenpark':(.20,1.25),'leicestersquare':(2.55,1.25),'coventgarden':(3.20,1.90),
}
assert GEO.keys()==SCHEM.keys()
for e in E.itertuples(index=False):
 x1,y1=SCHEM[e[1]];x2,y2=SCHEM[e[2]]
 dx=abs(x2-x1);dy=abs(y2-y1)
 assert dx<1e-7 or dy<1e-7 or abs(dx-dy)<1e-7, (e,dx,dy)

plt.rcParams.update({'font.family':'DejaVu Sans','figure.facecolor':BG,'axes.facecolor':BG,
 'savefig.facecolor':BG,'text.color':TEXT,'axes.edgecolor':LIGHT,'xtick.color':SUB,'font.size':11})

def title(fig,headline,sub):
 fig.text(.073,.945,headline,fontsize=22.5,fontweight='bold',va='top',ha='left',color=TEXT)
 fig.text(.073,.89,sub,fontsize=10.8,color=SUB,ha='left',va='top')
 fig.add_artist(Line2D([.073,.927],[.847,.847],transform=fig.transFigure,linewidth=1.1,color=TEXT))

def foot(fig,small):
 fig.add_artist(Line2D([.073,.927],[.102,.102],transform=fig.transFigure,linewidth=.7,color=LIGHT))
 fig.text(.073,.081,'COFFEETABLEVIZ  /  ICONS OF DATA',fontsize=9.4,fontweight='bold',color=TEXT)
 fig.text(.927,.081,'02  /  BECK · 1933',fontsize=9.3,color=SUB,ha='right')
 fig.text(.073,.12,small,fontsize=8.2,color=SUB)

def draw_network(ax,where,kind):
 ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([])
 for sp in ax.spines.values(): sp.set_visible(False)
 for e in E.itertuples(index=False):
  line,fr,to=e
  x,y=where[fr];x2,y2=where[to]
  ax.plot([x,x2],[y,y2],color=LINES[line],linewidth=4.7,solid_capstyle='round',zorder=2)
 inter={'oxfordcircus','piccadillycircus','holborn'}
 for k,(x,y) in where.items():
  ax.scatter([x],[y],s=kind=='schematic' and 130 or 115,marker='o',facecolor=WHITE,
             edgecolor=INK,linewidth=1.1,zorder=5)
  if k in inter:
   ax.scatter([x],[y],s=kind=='schematic' and 33 or 30,marker='o',facecolor=TEAL,
               edgecolor=TEAL,linewidth=0,zorder=6)
 if kind=='schematic':
  ax.set_xlim(-.30,4.70);ax.set_ylim(-.20,4.75)
 else:
  ax.set_xlim(-1.5,1.37);ax.set_ylim(-1.05,1.55)

GEOLABEL={
 'regentspark':(.02,.19,'left'),
 'bondstreet':(-.01,-.21,'left'),
 'oxfordcircus':(.03,.23,'left'),
 'piccadillycircus':(.10,-.38,'left'),
 'holborn':(.04,.19,'center')}
SCHEMLABEL={
 'regentspark':(.14,.15,'left'),
 'bondstreet':(-.22,.42,'left'),
 'oxfordcircus':(.09,-.29,'left'),
 'piccadillycircus':(.08,-.27,'left'),
 'holborn':(.08,.23,'right')}

def labels(ax,where,offsets):
 for station,(dx,dy,ha) in offsets.items():
  x,y=where[station]
  ax.text(x+dx,y+dy,SHORT[station],fontsize=7.9 if where is GEO else 7.65,color=TEXT,
          fontweight='bold' if station in ('oxfordcircus','piccadillycircus','holborn') else 'normal',
          ha=ha,va='center',zorder=20)

def fig2():
 fig=plt.figure(figsize=(8,8),dpi=240)
 title(fig,'Same network. Different priorities.',
       'Geography shows where stations are. A diagram brings connections forward.')
 legend_y=.815
 for i,(line,col) in enumerate(LINES.items()):
  x=.09+i*.283
  fig.add_artist(Line2D([x,x+.043],[legend_y,legend_y],transform=fig.transFigure,linewidth=4.4,color=col,solid_capstyle='round'))
  fig.text(x+.057,legend_y,line.capitalize()+' line',fontsize=9.2,color=TEXT,va='center')
 p=[(.073,.222,.411,.55),(.516,.222,.411,.55)]
 for i,(x,y,w,h) in enumerate(p):
  fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,facecolor=WHITE,edgecolor=LIGHT,linewidth=.95,zorder=0))
  fig.text(x+.018,y+h-.03,'01  /  GEOGRAPHIC POSITION' if i==0 else '02  /  TEACHING DIAGRAM',fontsize=10.3,
           fontweight='bold',ha='left',va='top',color=TEXT)
  fig.text(x+.018,y+h-.07,'Station coordinates · 2013' if i==0 else 'New layout · same connections',fontsize=8.6,ha='left',va='top',color=SUB)
  ax=fig.add_axes([x+.042,y+.086,w-.084,h-.207]);ax.patch.set_alpha(0)
  where=GEO if i==0 else SCHEM
  draw_network(ax,where,kind='geographic' if i==0 else 'schematic')
  labels(ax,where,GEOLABEL if i==0 else SCHEMLABEL)
  fig.text(x+.018,y+.041,'10 stations / 10 straight links' if i==0 else '10 stations / 10 same links',
           fontsize=8.5,color=SUB)
 fig.text(.073,.182,'Stations move around. The connections stay exactly the same.',
          fontsize=11.2,fontweight='bold',color=TEXT)
 foot(fig,'2013 network: De Domenico et al./TfL · straight links · editorial palette · NOT Beck’s 1933 map')
 p=OUT/'02_geography_vs_connections.png';fig.savefig(p,dpi=240);plt.close(fig);return p

def panel(fig,rect,num,title,subtitle):
 x,y,w,h=rect
 fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,fill=False,edgecolor=LIGHT,lw=1))
 fig.text(x+.027,y+h-.045,num+'   '+title,fontsize=13.3,fontweight='bold',va='top',color=TEXT)
 fig.text(x+.027,y+h-.09,subtitle,fontsize=9.25,color=SUB,va='top')
 return fig.add_axes([x+.043,y+.038,w-.086,h-.168])

def mini(ax,xmin=0,xmax=5,ymin=0,ymax=3.5):
 ax.set_xlim(xmin,xmax);ax.set_ylim(ymin,ymax);ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([])
 for sp in ax.spines.values():sp.set_visible(False)
 ax.patch.set_alpha(0)

def fig3():
 fig=plt.figure(figsize=(8,8),dpi=240)
 title(fig,'One diagram. Four design decisions.',
       'The encoding that helped make the Underground easier to navigate.')
 rects=[(.073,.484,.411,.337),(.516,.484,.411,.337),(.073,.16,.411,.315),(.516,.16,.411,.315)]
 a=panel(fig,rects[0],'01','Connections','Which stop leads to which?')
 b=panel(fig,rects[1],'02','Geometry','Simple angles make routes readable')
 c=panel(fig,rects[2],'03','Spacing','Give the busy middle room')
 d=panel(fig,rects[3],'04','Symbols + colour','Show lines and places to change')
 mini(a,xmax=5,ymax=3.2)
 pts={'oxford':(2.35,2.65),'piccadilly':(2.35,1.52),'charing':(2.35,.45),'green':(.55,1.52),'leicester':(4.3,1.52)}
 for u,v,col in [('oxford','piccadilly',INK),('piccadilly','charing',INK),('green','piccadilly',RED),('piccadilly','leicester',RED)]:
  a.plot([pts[u][0],pts[v][0]],[pts[u][1],pts[v][1]],lw=5,color=col,solid_capstyle='round')
 for key,(x,y) in pts.items():
  a.scatter([x],[y],s=110,color=WHITE,edgecolor=INK,lw=1,zorder=3)
 a.scatter([2.35],[1.52],s=35,color=TEAL,zorder=4)
 a.text(2.53,1.8,'Change here',fontsize=9.5,color=TEXT,fontweight='bold')
 mini(b,xmax=5,ymax=3.3)
 bx=[.5,1.8,3.2,4.25];by=[.65,.65,2.05,2.05]
 b.plot(bx,by,color=TEAL,lw=5.5,solid_capstyle='round')
 for x,y in zip(bx,by):b.scatter([x],[y],s=110,color=WHITE,edgecolor=INK,lw=1,zorder=3)
 b.text(.48,.18,'HORIZONTAL',fontsize=7.5,color=SUB)
 b.text(2.15,2.70,'45°',fontsize=11,color=TEAL,fontweight='bold')
 b.text(3.1,.18,'SIMPLIFIED ROUTE',fontsize=7.3,color=SUB)
 mini(c,xmax=5,ymax=3.3)
 c.text(.1,2.85,'Crowded station marks',fontsize=9,color=SUB)
 c.plot([.6,1.55,1.9,2.2,4.35],[2.22]*5,color=LIGHT,lw=2.6)
 for x in [.6,1.55,1.9,2.2,4.35]: c.scatter([x],[2.22],s=100,color=WHITE,edgecolor=INK,lw=1.0,zorder=3)
 c.annotate('',(2.52,1.55),(2.52,1.83),arrowprops=dict(arrowstyle='->',lw=1.2,color=SUB))
 c.text(.1,1.23,'Regularised for reading',fontsize=9,color=SUB)
 c.plot([.6,1.55,2.5,3.42,4.35],[.55]*5,color=INK,lw=3.7)
 for x in [.6,1.55,2.5,3.42,4.35]:c.scatter([x],[.55],s=100,color=WHITE,edgecolor=INK,lw=1,zorder=3)
 mini(d,xmax=5,ymax=3.3)
 d.plot([.45,4.4],[2.1,2.1],lw=6,color=RED,solid_capstyle='round')
 d.plot([2.42,2.42],[.37,3.0],lw=6,color=TEAL,solid_capstyle='round')
 for x,y in [(.7,2.1),(4.17,2.1),(2.42,.6),(2.42,2.8)]: d.scatter([x],[y],s=90,facecolor=WHITE,edgecolor=INK,lw=1.1,zorder=4)
 d.scatter([2.42],[2.1],s=190,facecolor=WHITE,edgecolor=INK,lw=1.1,zorder=4)
 d.scatter([2.42],[2.1],s=38,facecolor=TEAL,edgecolor=TEAL,zorder=5)
 foot(fig,'2013-based teaching sketches · Beck’s principles · original graphics, NOT historic Tube artwork')
 path=OUT/'03_decode_the_icon.png';fig.savefig(path,dpi=240);plt.close(fig);return path

if __name__=='__main__':
 from PIL import Image
 for path in (fig2(),fig3()):
  im=Image.open(path)
  assert im.size==(1920,1920)
  h=hashlib.sha256(path.read_bytes()).hexdigest()
  print(f'{path.name}: {im.size}, {path.stat().st_size} bytes, SHA256={h}')
 print('QA: source stations=10; station IDs unique; edges=10; 3 lines; layouts share exact station-edge identity; year=2013.')
