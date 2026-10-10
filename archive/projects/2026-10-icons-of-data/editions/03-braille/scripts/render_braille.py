"""Icons of Data #03 — deterministic explanatory diagrams of UK Unified English Braille.
Based on RNIB + UKAAF/ICEB UEB. Modern code, not 1829 French Braille. 
These are on-screen schematics, not tactile braille.
"""
from pathlib import Path
import hashlib
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle, Arc
from matplotlib.lines import Line2D
from PIL import Image

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'visuals';OUT.mkdir(exist_ok=True,parents=True)
BG='#F3F4F6'; WHITE='#FEFEFE'; TEXT='#15181A'; MUTED='#56616A'; LIGHT='#D3D9DD'; TEAL='#1F8FA8'; RED='#C44E52'; MUTE_FILL='#DCE2E5'; PAPER='#FFFFFF'; INK='#333B40'
plt.rcParams.update({'font.family':'Inter','figure.facecolor':BG,'savefig.facecolor':BG,'text.color':TEXT})
HEAD='Inter Display'; BODY='Inter'; MONO='DejaVu Sans Mono'
# UEB dot numbering: left column top-bottom 1 2 3; right column 4 5 6.
POS={1:(0,2),2:(0,1),3:(0,0),4:(1,2),5:(1,1),6:(1,0)}
SIGNS={"a":(1,),"b":(1,2),"c":(1,4),"number indicator":(3,4,5,6)}
assert SIGNS['a']==(1,) and SIGNS['b']==(1,2) and SIGNS['c']==(1,4)
assert SIGNS['number indicator']==(3,4,5,6)

def glyph(dots):
    bit=sum(1<<(n-1) for n in dots)
    return chr(0x2800+bit)
assert glyph(SIGNS['a'])=='⠁'
assert glyph(SIGNS['b'])=='⠃'
assert glyph(SIGNS['c'])=='⠉'
assert glyph(SIGNS['number indicator'])=='⠼'
assert glyph(SIGNS['number indicator'])+glyph(SIGNS['a'])=='⠼⠁'

def fig_base():
    f=plt.figure(figsize=(8,8),dpi=240)
    return f

def txt(fig,x,y,s,sz=10,color=TEXT,weight='regular',family=BODY,ha='left',va='center',z=10):
    return fig.text(x,y,s,fontfamily=family,fontsize=sz,color=color,fontweight=weight,ha=ha,va=va,zorder=z)

def rule(f,y,x1=.075,x2=.925,color=LIGHT,lw=.8):
    f.add_artist(Line2D([x1,x2],[y,y],transform=f.transFigure,color=color,lw=lw,zorder=10))

def rect(f,x,y,w,h,fc=WHITE,ec=None,lw=0,r=0):
    if r:
        z=FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',transform=f.transFigure,facecolor=fc,edgecolor=ec or fc,linewidth=lw,zorder=1)
    else:
        z=Rectangle((x,y),w,h,transform=f.transFigure,facecolor=fc,edgecolor=ec or fc,linewidth=lw,zorder=1)
    f.add_artist(z)
    return z

def line(f,x1,y1,x2,y2,color=TEXT,lw=1.0):
    f.add_artist(Line2D([x1,x2],[y1,y2],transform=f.transFigure,color=color,lw=lw,zorder=11))

def circle(f,x,y,r,fc,ec=None,lw=0,z=7):
    c=Circle((x,y),r,facecolor=fc,edgecolor=ec or fc,linewidth=lw,transform=f.transFigure,zorder=z)
    f.add_artist(c)


def cell(f,cx,cy,size,dots=(),raised=TEAL,empty=MUTE_FILL,label_numbers=False,border=False):
    """Six-dot cell in figure coordinates, size = height of cell, with proportional x spacing."""
    dx=size*.208;dy=size*.265; radius=size*.078
    dot_set=set(dots)
    if border:rect(f,cx-.156*size,cy-.42*size, .515*size,.9*size,fc=WHITE,ec=LIGHT,lw=.8,r=.035*size)
    coords={}
    for n,(x,y) in POS.items():
        xx=cx+(x-.0)*dx; yy=cy+(y-1)*dy
        circle(f,xx,yy,radius, raised if n in dot_set else empty, z=13)
        coords[n]=(xx,yy)
        if label_numbers:
            txt(f,xx,yy,str(n),sz=max(7,size*29),color=WHITE if n in dot_set else MUTED,
                ha='center',va='center',weight='bold',z=14)
    return coords

def footer(f,number,desc):
    rule(f,.102,color='#C5CDD2')
    txt(f,.075,.081,'COFFEETABLEVIZ  /  ICONS OF DATA',sz=9.1,weight='bold')
    txt(f,.925,.081,f'03  /  BRAILLE · {number}',sz=9,color=MUTED,ha='right',family=MONO)
    txt(f,.075,.123,desc,sz=7.5,color=MUTED)

def header(f,title,subtitle):
    txt(f,.075,.946,title,sz=22.3,weight='bold',family=HEAD,va='top')
    txt(f,.075,.890,subtitle,sz=10.4,color=MUTED,va='top')
    rule(f,.847,color=INK,lw=.9)

def draw_02():
    f=fig_base();header(f,'Six places. Many patterns.','A tiny grid turns dot positions into characters and numbers.')
    # Main scene
    rect(f,.075,.477,.85,.343,WHITE,ec=LIGHT,lw=.9)
    txt(f,.098,.788,'THE SIX-DOT CELL',sz=10.8,weight='bold')
    txt(f,.098,.752,'Two columns. Three rows.',sz=9.5,color=MUTED)
    cell(f,.205,.646,.26,(1,2,3,4,5,6),raised=TEAL,label_numbers=True)
    line(f,.405,.66,.467,.66,color=LIGHT,lw=1.4)
    txt(f,.50,.72,'6 dot positions',sz=16.2,weight='bold',family=HEAD)
    txt(f,.50,.661,'2⁶  =  64',sz=19.3,weight='bold',family=MONO,color=TEAL)
    txt(f,.50,.605,'possible on/off states',sz=10.2,color=TEXT)
    txt(f,.50,.550,'63 with raised dots  +  1 empty',sz=9.0,color=MUTED)
    # examples
    txt(f,.075,.439,'SAME CELL. DIFFERENT PATTERNS.',sz=10.2,weight='bold')
    y=.254;h=.157; gaps=.012
    for i,(letter,dots) in enumerate((('a',(1,)),('b',(1,2)),('c',(1,4)))):
        x=.075+i*(.85/3)
        w=.85/3-gaps
        rect(f,x,y,w,h,WHITE,ec=LIGHT,lw=.9)
        cell(f,x+.055,y+.073,.105,dots,raised=TEAL)
        txt(f,x+.145,y+.106,letter,sz=23.5,weight='bold',family=HEAD)
        txt(f,x+.145,y+.052,'dots '+', '.join(map(str,dots)),sz=9.1,color=MUTED)
    # bottom context
    txt(f,.075,.228,'AND CONTEXT CHANGES THE MEANING.',sz=10.2,weight='bold')
    rect(f,.075,.151,.85,.059,WHITE,ec=LIGHT,lw=.9)
    cell(f,.110,.183,.083,SIGNS['number indicator'],raised=RED)
    txt(f,.157,.181,'number sign',sz=9.3,color=TEXT)
    txt(f,.318,.181,'+',sz=13.2,color=MUTED,ha='center')
    cell(f,.357,.183,.083,SIGNS['a'],raised=TEAL)
    txt(f,.403,.181,'a pattern',sz=9.3,color=TEXT)
    txt(f,.548,.181,'→',sz=16.2,color=MUTED,ha='center')
    txt(f,.592,.183,'1',sz=18.0,weight='bold',family=MONO)
    txt(f,.656,.180,'in UK UEB',sz=10.3,color=MUTED)
    footer(f,'01','Modern UK Unified English Braille (UEB) · uncontracted examples · diagrams, not raised Braille')
    path=OUT/'02_six_places_many_patterns.png';f.savefig(path,dpi=240);plt.close(f);return path

def draw_03():
    f=fig_base();header(f,'Decode the Icon.','Four ideas behind a writing system made to be felt.')
    coords=[(.075,.488,.411,.332),(.514,.488,.411,.332),(.075,.148,.411,.325),(.514,.148,.411,.325)]
    for x,y,w,h in coords:rect(f,x,y,w,h,WHITE,ec=LIGHT,lw=.85)
    def panel_heading(i,name,sub):
        x,y,w,h=coords[i]
        txt(f,x+.026,y+h-.044,f'0{i+1}   {name}',sz=13.0,weight='bold',family=HEAD)
        txt(f,x+.026,y+h-.083,sub,sz=9.0,color=MUTED)
    panel_heading(0,'Positions','Two columns. Three rows.')
    panel_heading(1,'Patterns','Same places, different signs.')
    panel_heading(2,'Context','A prefix changes what follows.')
    panel_heading(3,'Touch, not ink','The marks are physically raised.')
    # 01 positions
    cell(f,.220,.585,.163,(1,2,3,4,5,6),label_numbers=True)
    txt(f,.336,.626,'Each dot has',sz=10.8,color=TEXT)
    txt(f,.336,.590,'a fixed',sz=10.8,color=TEXT)
    txt(f,.336,.554,'position.',sz=10.8,color=TEXT)
    # 02 patterns
    for i,(sym,dots) in enumerate([('a',(1,)),('b',(1,2)),('c',(1,4))]):
        x=.572+i*.114
        cell(f,x,.601,.110,dots,raised=TEAL)
        txt(f,x+.018,.531,sym,sz=18.0,weight='bold',ha='center',family=HEAD)
    # 03 prefix
    cell(f,.143,.258,.100,(3,4,5,6),raised=RED)
    txt(f,.177,.193,'number',sz=9,color=MUTED,ha='center')
    txt(f,.242,.257,'+',sz=17.5,color=MUTED,ha='center')
    cell(f,.284,.258,.100,(1,),raised=TEAL)
    txt(f,.320,.193,'a',sz=9.4,color=MUTED,ha='center')
    txt(f,.382,.258,'→ 1',sz=16.4,color=TEXT,weight='bold',family=HEAD)
    # 04 physical medium - explicitly schematic side elevation; not image of a real tactile object
    txt(f,.540,.367,'SCREEN DIAGRAM',sz=8.3,weight='bold',color=MUTED)
    for n in range(3):
        circle(f,.590+n*.070,.325,.022,TEAL)
    txt(f,.540,.275,'SIDE-VIEW SCHEMATIC',sz=8.3,weight='bold',color=MUTED)
    line(f,.554,.212,.872,.212,color=INK,lw=1.25)
    # domes above paper, show 3 raised humps
    from matplotlib.patches import Arc
    for x in (.600,.705,.810):
        f.add_artist(Arc((x,.213),.064,.054,theta1=0,theta2=180,color=INK,lw=2.2,transform=f.transFigure,zorder=13))
    txt(f,.540,.173,'Real Braille uses raised dots.',sz=8.65,color=MUTED)
    footer(f,'02','UK UEB · positions 1–6 · number sign + a = 1 · a screen drawing cannot convey touch')
    path=OUT/'03_decode_the_icon.png';f.savefig(path,dpi=240);plt.close(f);return path

if __name__=='__main__':
    for f in [draw_02(),draw_03()]:
        im=Image.open(f)
        assert im.size==(1920,1920),im.size
        print(f'{f.name} {im.size} {f.stat().st_size} bytes sha256={hashlib.sha256(f.read_bytes()).hexdigest()}')
    print('UK UEB QA: a=1; b=12; c=14; numeric indicator=3456; 1=3456-1; 63 non-empty + 1 empty; no original photo copied')
