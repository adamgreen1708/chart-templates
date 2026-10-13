"""QA revision for charts 1 and 2, based on derived source data; no invented race facts."""
from pathlib import Path
import csv, math, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT=Path(__file__).resolve().parent
BG='#F3F4F6';BLUE='#1F8FA8';RED='#C44E52';MID='#7A7A7A';DARK='#111111';SUB='#555555';GRID='#D7DCE0'
plt.rcParams.update({'font.family':'DejaVu Sans','figure.facecolor':BG,'savefig.facecolor':BG,
                     'axes.facecolor':BG,'font.size':11,'svg.fonttype':'none'})

def frame(title,subtitle,number):
    fig=plt.figure(figsize=(8,8),dpi=200,facecolor=BG)
    a=[]
    a.append(fig.text(.1,.928,'COFFEETABLEVIZ  /  SHORTS IN SPORTS',ha='left',va='bottom',fontsize=8.2,color=MID,weight='bold'))
    a.append(fig.text(.10,.876,title,ha='left',va='top',fontsize=20.5,weight='bold',color=DARK))
    a.append(fig.text(.10,.798,subtitle,ha='left',va='top',fontsize=10.1,color=SUB,linespacing=1.45))
    fig.add_artist(Line2D([.1,.9],[.107,.107],transform=fig.transFigure,color='#D0D0D0',lw=.9))
    a.append(fig.text(.10,.085,'COFFEETABLEVIZ',ha='left',va='center',fontsize=9,color=DARK,weight='bold'))
    a.append(fig.text(.90,.085,f'THE DATA TAYLOR  /  {number} OF 3',ha='right',va='center',fontsize=8.3,color=SUB))
    return fig,a

def qa(fig,important,tag,axes=None):
    fig.canvas.draw();renderer=fig.canvas.get_renderer();canvas=fig.bbox
    pix=fig.get_figwidth()*fig.dpi
    valid=[]
    for name,obj in important:
        bb=obj.get_window_extent(renderer)
        assert bb.x0>=12 and bb.x1<=canvas.x1-12,(tag,'x overflow',name,bb)
        assert bb.y0>=12 and bb.y1<=canvas.y1-12,(tag,'y overflow',name,bb)
        valid.append((name,bb))
    # Check title vs subtitle and chart vs lower information blocks.
    importantdict={key:obj.get_window_extent(renderer) for key,obj in important}
    assert importantdict['title'].y0>importantdict['subtitle'].y1+14,(tag,'title/subtitle collision')
    if axes is not None:
        axbb=axes.get_window_extent(renderer)
        assert importantdict['subtitle'].y0>axbb.y1+22,(tag,'subtitle/chart collision')
    print(tag,'TEXT_QA_OK',len(valid),'items', 'WIDTH',pix)


def export(fig,stem):
    fig.savefig(ROOT/f'{stem}.png',dpi=200,facecolor=BG)
    fig.savefig(ROOT/f'{stem}.svg',facecolor=BG)
    plt.close(fig)

with (ROOT/'season_win_rates.csv').open(newline='',encoding='utf-8') as f:
    seasons=list(csv.DictReader(f))
for d in seasons:
    d['season']=int(d['season']);d['grand_prix_rows']=int(d['grand_prix_rows']);d['wins']=int(d['wins'])
    d['win_rate_percent']=d['wins']/d['grand_prix_rows']*100
assert [(s['season'],s['wins']) for s in seasons if s['season'] in (2021,2023,2025)]==[(2021,10),(2023,19),(2025,8)]
assert sum(s['wins'] for s in seasons if s['season']<=2020)==10
peak=next(s['win_rate_percent'] for s in seasons if s['season']==2023)
latest=next(s['win_rate_percent'] for s in seasons if s['season']==2025)
assert round(peak-latest,1)==53.0

# CHART 1: label only three editorial milestones, and explain EACH in the summary band.
fig,t=frame('The year he almost won everything',
    'Grand Prix win rate, 2015–2025 (completed seasons only).\nThe breakthrough in 2021 became a peak in 2023 — then fell back.',1)
important=[('title',t[1]),('subtitle',t[2])]
ax=fig.add_axes([.115,.277,.76,.405],facecolor=BG)
x=list(range(len(seasons)))
rates=[s['win_rate_percent'] for s in seasons]
bars=ax.bar(x,rates,width=.66,color=[RED if s['season']==2023 else BLUE for s in seasons],edgecolor='none')
ax.set_ylim(0,102);ax.set_xlim(-.6,len(seasons)-.4)
ax.set_yticks([0,20,40,60,80,100]);ax.set_yticklabels([f'{v}%' for v in [0,20,40,60,80,100]],color=SUB,fontsize=9)
ax.yaxis.grid(True,color=GRID,lw=.8);ax.set_axisbelow(True)
ax.set_xticks(x);ax.set_xticklabels([str(s['season'])[2:] for s in seasons],fontsize=10.7,color=SUB)
ax.tick_params(axis='both',length=0,pad=6)
for sp in ax.spines.values():sp.set_visible(False)
for year in (2021,2023,2025):
    idx=year-2015;v=rates[idx];bb=bars[idx]
    lab=ax.text(bb.get_x()+bb.get_width()/2,bb.get_height()+2.2,f'{v:.1f}%',
                color=RED if year==2023 else DARK,fontsize=10.3,
                weight='bold' if year==2023 else 'medium',ha='center',va='bottom')
    important.append((f'{year} label',lab))

# Insight strip connects the three annotated years to a reason for their labels.
insights=[
    (.11,'2021  ·  10 wins','= all 2015–20 wins combined'),
    (.405,'2023  ·  19 of 22','86.4% — the peak'),
    (.685,'2025  ·  8 of 24','Down 53.0 percentage points'),
]
for i,(xx,stat,context) in enumerate(insights):
    a=fig.text(xx,.213,stat,fontsize=10.4,color=RED if i==1 else DARK,weight='bold',va='center')
    b=fig.text(xx,.183,context,fontsize=8.4,color=SUB,va='center')
    important.extend([(f'{i} key',a),(f'{i} info',b)])
source=fig.text(.10,.128,'Source: The Data Taylor / Shorts in Sports; key totals checked with Formula 1.',color=SUB,fontsize=7.8)
important.append(('source',source))
qa(fig,important,'CHART_1',ax)
export(fig,'01_verstappen_win_share')

# CHART 2: rebalance margins and ensure leftmost bubbles are fully visible.
with (ROOT/'grid_finish_derived.csv').open(newline='',encoding='utf-8') as f:
    entries=list(csv.DictReader(f))
valid=[r for r in entries if r['classified']=='True' and not r['exclude_grid_analysis']]
assert len(valid)==199
counts=collections.Counter((int(r['starting_grid']),int(r['final_position'])) for r in valid)
fig,t=frame('The grid is a guide, not a verdict',
    'Grid position vs classified finish across 199 races, 2015–2025.\nLarger circles = more races with the same start and finish.',2)
important=[('title',t[1]),('subtitle',t[2])]
# Left/right canvas margins: 13% / 10%; y-axis label stays within figure.
ax=fig.add_axes([.13,.252,.77,.418],facecolor=BG)
ax.plot([1,20],[1,20],color=MID,lw=1.2,ls='--',alpha=.75,zorder=1)
for (start,finish),cnt in sorted(counts.items(),key=lambda z:-z[1]):
    ax.scatter(start,finish,s=30+cnt*27,alpha=.42,color=BLUE,edgecolor=BG,linewidth=.8,zorder=2)
# Key stories: all three officially verified; selected points are not statistical outlier claims.
for xx,yy in ((17,1),(20,2),(14,1)):
    ax.scatter(xx,yy,s=110 if (xx,yy)!=(17,1) else 130,color=RED,alpha=1,edgecolor=BG,linewidth=1.6,zorder=5)
common={'textcoords':'offset points','arrowprops':{'arrowstyle':'-','color':MID,'lw':.8},'zorder':9}
lbl= ax.annotate('São Paulo 2024\nP17 → P1',(17,1),xytext=(-70,-30),ha='right',fontsize=8.8,color=RED,weight='bold',**{**common,'arrowprops':{'arrowstyle':'-','color':RED,'lw':.8}})
important.append(('Sao Paulo label',lbl))
lbl=ax.annotate('Russia 2021\nP20 → P2',(20,2),xytext=(-20,34),ha='right',fontsize=8.1,color=DARK,**common)
important.append(('Russia label',lbl))
lbl=ax.annotate('Belgium 2022\nP14 → P1',(14,1),xytext=(-59,17),ha='right',fontsize=8.1,color=DARK,**common)
important.append(('Belgium label',lbl))
ax.set_xlim(-.15,21.1);ax.set_ylim(21.4,-.5)
ax.set_xticks([1,5,10,15,20]);ax.set_yticks([1,5,10,15,20])
ax.set_xlabel('Starting grid position',fontsize=10,color=SUB,labelpad=8)
ax.set_ylabel('Final classified position',fontsize=10,color=SUB,labelpad=8)
ax.grid(True,color=GRID,lw=.7);ax.set_axisbelow(True)
for spine in ax.spines.values():spine.set_visible(False)
ax.tick_params(axis='both',length=0,labelsize=10,colors=SUB,pad=5)
important.append(('x axis',ax.xaxis.label));important.append(('y axis',ax.yaxis.label))
explainer=fig.text(.125,.155,'Above the diagonal = net positions gained.',color=DARK,fontsize=10.0,weight='bold')
source=fig.text(.10,.126,'2015–2025 · 33 retirements and one pit-lane start excluded. The Data Taylor / F1.',color=SUB,fontsize=7.65)
important.extend([('diagonal explainer',explainer),('source',source)])
qa(fig,important,'CHART_2',ax)
export(fig,'02_verstappen_grid_vs_finish')
print('PASS: All numerical and canvas checks')
