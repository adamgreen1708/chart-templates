"""Icons of Data 04 | deterministic publication-review artwork.
Review-only: no website/git publishing. Uses 24 HistData rows verified against GitHub repo.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, FancyBboxPatch, Rectangle, FancyArrowPatch
import hashlib

HERE=Path(__file__).resolve().parent
OUT=HERE/'visuals'
OUT.mkdir(exist_ok=True)
df=pd.read_csv(HERE/'data_nightingale_24_months.csv',parse_dates=['Date'])
assert len(df)==24 and str(df.iloc[0].Date.date())=='1854-04-01' and str(df.iloc[-1].Date.date())=='1856-03-01'
assert [int(df.iloc[:12][col].sum()) for col in ['Disease','Wounds','Other']]==[11157,772,1365]
assert [int(df.iloc[12:][col].sum()) for col in ['Disease','Wounds','Other']]==[3319,986,383]
for cnt,rate in [('Disease','Disease.rate'),('Wounds','Wounds.rate'),('Other','Other.rate')]:
    assert np.max(np.abs(df[rate]-12000*df[cnt]/df['Army']))<=0.051
assert df.iloc[9]['Disease.rate']==1022.8 and df.iloc[-1]['Disease.rate']==3.9
BG='#F3F4F6'; WHITE='#FFFFFF'; INK='#141819'; MUTE='#5A6771'; GRID='#D7DDDF'; BLUE='#218CA8'; RED='#C44E52'; DARK='#3A454A'; PALE='#E7EAEB'; LIGHTBLUE='#DCEFF4'
plt.rcParams.update({'font.family':'Inter','font.size':15,'text.color':INK,'axes.edgecolor':GRID,'axes.labelcolor':MUTE,'xtick.color':MUTE,'ytick.color':MUTE,'savefig.facecolor':BG, 'mathtext.fontset':'dejavusans'})
DPI=160

def fig0():
    f=plt.figure(figsize=(12,12),dpi=DPI,facecolor=BG)
    f.text(.067,.953,'COFFEETABLEVIZ  /  ICONS OF DATA',fontsize=11.2,fontweight='bold',va='top',color=INK)
    f.text(.934,.953,'04  /  NIGHTINGALE',fontsize=11.2,ha='right',va='top',color=MUTE)
    f.add_artist(plt.Line2D([.067,.933],[.925,.925],transform=f.transFigure,c=INK,lw=1.4))
    return f

def text(f,x,y,s,sz=14,**kw):return f.text(x,y,s,fontsize=sz,transform=f.transFigure,**kw)

def footer(f,s):
    f.add_artist(plt.Line2D([.067,.933],[.07,.07],transform=f.transFigure,c=GRID,lw=1.3))
    text(f,.067,.047,'COFFEETABLEVIZ  /  ICONS OF DATA',10.5,fontweight='bold')
    text(f,.933,.047,s,10.5,ha='right',color=MUTE)

def chart02():
    fig=fig0()
    text(fig,.067,.868,'The biggest problem was blue.',33,fontweight='bold')
    text(fig,.067,.823,'Annualised deaths per 1,000 soldiers · monthly observations',17.5,color=MUTE)
    # simple legend
    for x,c,lab in [(.091,BLUE,'Disease'),(.310,RED,'Wounds'),(.524,DARK,'Other causes')]:
        fig.add_artist(plt.Line2D([x,x+.033],[.764,.764],transform=fig.transFigure,c=c,lw=5,solid_capstyle='round'))
        text(fig,x+.045,.76,lab,14.3,va='center',color=INK)
    ax=fig.add_axes([.105,.355,.82,.364],facecolor=BG)
    xx=np.arange(24)
    ax.axvspan(-.45,11.5,color='#E6EAEC',alpha=.62,zorder=0)
    for r in [0,200,400,600,800,1000]:ax.axhline(r,c=GRID,lw=1,alpha=.95,zorder=0)
    ax.axvline(11.5,c='#8B969E',lw=1.25,ls=(0,(4,4)),zorder=1)
    for col,c,z,lw in [('Disease.rate',BLUE,6,4.0),('Wounds.rate',RED,5,2.9),('Other.rate',DARK,4,2.9)]:
        ax.plot(xx,df[col],lw=lw,color=c,zorder=z,marker='o',markersize=5.2 if col=='Disease.rate' else 3.5,
                markeredgewidth=0,solid_capstyle='round',solid_joinstyle='round')
    ax.scatter([9],[1022.8],s=150,color=BLUE,edgecolors=BG,linewidths=3,zorder=8)
    ax.annotate('Jan 1855 peak\n1,022.8',xy=(9,1022.8),xytext=(6.7,887),fontsize=14,ha='center',va='center',fontweight='bold',color=INK,
                arrowprops=dict(arrowstyle='-',color=MUTE,lw=1.1,connectionstyle='angle3,angleA=5,angleB=92'),zorder=9)
    ax.scatter([23],[3.9],s=88,color=BLUE,edgecolors=BG,linewidths=2,zorder=8)
    ax.set_xlim(-.5,23.3);ax.set_ylim(0,1130)
    ax.set_yticks([0,200,400,600,800,1000]);ax.set_yticklabels(['0','200','400','600','800','1,000'])
    ax.set_xticks([0,3,6,9,12,15,18,21,23]);ax.set_xticklabels(['Apr\n1854','Jul','Oct','Jan\n1855','Apr','Jul','Oct','Jan\n1856','Mar'])
    ax.tick_params(axis='x',length=0,pad=15,labelsize=12.5)
    ax.tick_params(axis='y',length=0,pad=10,labelsize=12.5)
    for spine in ax.spines.values():spine.set_visible(False)
    ax.text(.01,1.04,'APR 1854 – MAR 1855',transform=ax.transAxes,fontsize=11,fontweight='bold',color=MUTE)
    ax.text(.55,1.04,'APR 1855 – MAR 1856',transform=ax.transAxes,fontsize=11,fontweight='bold',color=MUTE)
    text(fig,.106,.278,'RATE = deaths in that month ÷ estimated army strength × 12,000',13.3,color=INK)
    text(fig,.106,.244,'Annualised means scaled to a year — not deaths in a single month.',12.2,color=MUTE)
    fig.add_artist(plt.Line2D([.105,.925],[.206,.206],transform=fig.transFigure,c=GRID,lw=1.0))
    text(fig,.106,.174,'The sharp decline is real in these records.',17,fontweight='bold',color=INK)
    text(fig,.106,.143,'The chart alone cannot tell us what caused it.',14.0,color=MUTE)
    text(fig,.106,.099,'Source: HistData Nightingale · 24 months · annualised rates per 1,000 soldiers',11.5,color=MUTE)
    footer(fig,'04   /   NIGHTINGALE  ·  02')
    out=OUT/'02_what_the_numbers_reveal.png'
    fig.savefig(out,dpi=DPI,facecolor=BG); plt.close(fig)
    return out

def panel(fig,x,y,w,h,n,title,subtitle):
    fig.add_artist(Rectangle((x,y),w,h,transform=fig.transFigure,facecolor=WHITE,edgecolor=GRID,lw=1.15,zorder=0))
    text(fig,x+.025,y+h-.047,n+'  '+title,16.0,fontweight='bold',va='top')
    text(fig,x+.025,y+h-.089,subtitle,11.9,color=MUTE,va='top')

def chart03():
    fig=fig0()
    text(fig,.067,.868,'Decode the Icon.',34,fontweight='bold')
    text(fig,.067,.825,'Four decisions behind a very persuasive diagram.',16.5,color=MUTE)
    L=.067;G=.022;W=(.866-G)/2; H=.302;T=.776;B=T-H-.020
    coords=[(L,T-H),(L+W+G,T-H),(L,B-H),(L+W+G,B-H)]
    titles=[('01','Time gets an angle','Twelve months. Twelve equal slices.'),('02','Area carries the rate','Not the radius.'),('03','Three causes. One centre.','Colour separates the categories.'),('04','A comparison, not a cause','What else changed between periods?')]
    for (x,y),(n,heading,sub) in zip(coords,titles): panel(fig,x,y,W,H,n,heading,sub)
    # panel1: equal slices drawn as ring sectors
    x,y=coords[0]; ax=fig.add_axes([x+.04,y+.026,W*.53,H*.56]);ax.set_xlim(-1.3,1.3);ax.set_ylim(-1.3,1.3);ax.set_aspect('equal');ax.axis('off')
    for i in range(12):
        c=LIGHTBLUE if i!=0 else BLUE
        ax.add_patch(Wedge((0,0),1.03,90-(i+1)*30,90-i*30,width=.58,facecolor=c,edgecolor=WHITE,lw=2))
    ax.add_patch(Circle((0,0),.33,facecolor=WHITE,edgecolor=GRID,lw=1))
    ax.text(0,0,'12',ha='center',va='center',fontsize=19,fontweight='bold',color=INK)
    text(fig,x+.245,y+.165,'30°',24,fontweight='bold',color=BLUE)
    text(fig,x+.245,y+.13,'per month',12.8,color=MUTE)
    text(fig,x+.036,y+.03,'Each slice has the same angle, not the same value.',10.5,color=MUTE)
    # panel2: accurate areas with 1:4 schematic
    x,y=coords[1]
    ax=fig.add_axes([x+.045,y+.06,W*.89,H*.53]);ax.set_xlim(0,10);ax.set_ylim(0,5);ax.set_aspect('equal');ax.axis('off')
    ax.add_patch(Wedge((2.7,2.7),1.07,0,65,facecolor=BLUE,edgecolor=GRID,lw=1.2))
    ax.add_patch(Wedge((6.8,2.7),2.14,0,65,facecolor=BLUE,edgecolor=GRID,lw=1.2))
    ax.text(2.7,.24,'Area = 1',fontsize=12,ha='center',color=INK)
    ax.text(6.8,.24,'Area = 4',fontsize=12,ha='center',color=INK)
    text(fig,x+.036,y+.032,'Illustration only · radius ×2 → area ×4',10.5,color=MUTE)
    # panel3: different annualised cause rates from the same zero; separate sector shapes avoids implying stacks
    x,y=coords[2]
    p=fig.add_axes([x+.043,y+.068,W*.89,H*.53]);p.set_xlim(-.5,10.5);p.set_ylim(-.2,3.5);p.set_aspect('equal');p.axis('off')
    items=[(1.25,2.04,BLUE,'Disease'),(4.6,1.46,RED,'Wounds'),(7.65,.92,DARK,'Other')]
    for cx,r,c,label in items:
        p.add_patch(Wedge((cx,0),r,15,75,facecolor=c,edgecolor=c,lw=1))
        p.plot([cx,cx+.2],[0,0],color=INK,lw=.6)
        p.text(cx+r*.28,2.55,label,fontsize=11,ha='center',color=INK)
    text(fig,x+.036,y+.034,'Shown apart here; overlapped from centre originally.',10.4,color=MUTE)
    # panel4: editorial caution, intentionally not a false quantitative chart
    x,y=coords[3]
    text(fig,x+.041,y+.166,'OBSERVED',12.6,fontweight='bold',color=BLUE)
    text(fig,x+.041,y+.128,'Mortality rates changed.',14.0,color=INK)
    text(fig,x+.041,y+.098,'NOT ESTABLISHED',12.6,fontweight='bold',color=RED)
    text(fig,x+.041,y+.065,'One reform alone caused the decline.',11.5,color=INK)
    text(fig,x+.041,y+.027,'Also changed: seasons, troop strength, conditions.',10.4,color=MUTE)
    text(fig,.067,.116,'Two periods can show a pattern without proving why it happened.',11.8,color=MUTE)
    text(fig,.067,.092,'Source: Nightingale, 1858 · HistData · explanatory drawings are schematics',10.4,color=MUTE)
    footer(fig,'04   /   NIGHTINGALE  ·  03')
    out=OUT/'03_decode_the_icon.png'
    fig.savefig(out,dpi=DPI,facecolor=BG);plt.close(fig)
    return out

if __name__=='__main__':
    for p in [chart02(),chart03()]:
        from PIL import Image
        im=Image.open(p)
        assert im.size==(1920,1920), (p,im.size)
        print(str(p),im.size,'sha256',hashlib.sha256(p.read_bytes()).hexdigest(),p.stat().st_size)
