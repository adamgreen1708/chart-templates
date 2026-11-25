from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import numpy as np,math,datetime,csv
BASE=Path(__file__).resolve().parent
names=['Arsenal','Man City','Man United','Aston Villa','Liverpool','Bournemouth','Sunderland','Brighton','Brentford','Chelsea','Fulham','Newcastle','Everton','Leeds','Crystal Palace',"Nott'm Forest",'Tottenham','West Ham','Burnley','Wolves']
with (BASE/'data'/'matches_2526.csv').open() as f:
 rows=[((datetime.date.fromisoformat(r['Date'])-datetime.date(2025,8,15)).days,names.index(r['HomeTeam']),names.index(r['AwayTeam']),int(r['FTHG']),int(r['FTAG'])) for r in csv.DictReader(f)]
clubs=names.copy();clubs[15]='Nott’m Forest'
W,H=6000,2000; left,right,top,bottom=540,5260,235,1810; OFF=12
X=lambda j:round(left+(right-left)*j/379);Y=lambda t:round(top+(bottom-top)*t/19)
hist=[[] for _ in clubs]
for j,(d,h,a,g,b) in enumerate(rows):hist[h].append((j,g,b,True));hist[a].append((j,b,g,False))
runs=[]
for t,seq in enumerate(hist):
 run=[]
 for rec in seq+[(-1,0,0,False)]:
  if rec[1]>rec[2]:run.append(rec)
  else:
   if len(run)>=5:runs.append((t,run[:]))
   run=[]
assert sorted(len(r) for t,r in runs)==[5,5,5,5,6,8]
assert all(sum(x[3] for x in h)==19 for h in hist)
xx=np.linspace(-1,1,W,dtype=np.float32)[None,:]; yy=np.linspace(-1,1,H,dtype=np.float32)[:,None]
bg=(13+5*np.exp(-1.7*(xx*xx+yy*yy))).astype(np.uint8);im=Image.fromarray(bg,'L').convert('RGB');dr=ImageDraw.Draw(im)
for t in range(20):dr.line((left-22,Y(t),right+22,Y(t)),fill=(35,)*3,width=1)
for j,(d,h,a,g,b) in enumerate(rows):
 x=X(j); y0,y1=sorted([Y(h)-OFF,Y(a)+OFF]); total=g+b
 v=48+min(total,7)*8; width=2 if total<5 else 3
 if g==b:
  for p in range(y0,y1,19):dr.line((x,p,x,min(p+10,y1)),fill=(v,)*3,width=width)
 else:dr.line((x,y0,x,y1),fill=(v,)*3,width=width)
for t,run in runs:
 a,b=X(run[0][0]),X(run[-1][0]); y=Y(t); h=49; w=b-a+1
 gx=np.arange(w);gy=np.arange(h)-h//2;taper=np.minimum(1,np.minimum((gx+1)/9,(w-gx)/9))
 intensity=(.13+.017*(len(run)-5))*np.exp(-(gy[:,None]/7.5)**2)*taper[None,:]
 rgba=np.full((h,w,4),235,dtype=np.uint8);rgba[:,:,3]=np.uint8(intensity*255);s=Image.fromarray(rgba,'RGBA');im.paste(s,(a,y-h//2),s)
 dr=ImageDraw.Draw(im);dr.line((a,y,b,y),fill=(82+9*(len(run)-5),)*3,width=2)
 for z in [a,b]:dr.line((z,y-3,z,y+3),fill=(100,)*3,width=2)
S=81;q=np.arange(S,dtype=float)-S//2;dx,dy=np.meshgrid(q,q);rr=np.hypot(dx,dy)
def sprite(g,win,clean):
 r=4.8*math.sqrt(1+1.25*g);ring=16.0
 glow=(.19*np.exp(-(rr/14)**2)+.08*np.exp(-((rr-ring)/3)**2)+.74*np.exp(-((rr-ring)/.85)**2)) if win else np.zeros_like(rr)
 rgba=np.full((S,S,4),242,dtype=np.uint8);rgba[:,:,3]=np.uint8(np.clip(glow,0,1)*255)
 out=Image.fromarray(rgba,'RGBA')
 mask=np.clip(r+.5-rr,0,1)
 light=52+94*np.exp(-(((dx+.32*r)/(.66*r))**2+((dy+.42*r)/(.60*r))**2))+ (115 if clean else 70)*np.exp(-((rr-r+.7)/1.0)**2)+125*np.exp(-(((dx+.30*r)/(.20*r))**2+((dy+.38*r)/(.19*r))**2))
 light+=49*np.exp(-(((dx-.23*r)/(.50*r))**2+((dy-.48*r)/(.18*r))**2))
 a=np.zeros((S,S,4),dtype=np.uint8);a[:,:,:3]=np.clip(light,0,255).astype(np.uint8)[:,:,None];a[:,:,3]=(mask*255).astype(np.uint8)
 return out,Image.fromarray(a,'RGBA')
cache={(g,w,c):sprite(g,w,c) for g in range(6) for w in (False,True) for c in (False,True)}
for layer in (0,1):
 for j,(d,h,a,g,b) in enumerate(rows):
  for t,score,against,offset in ((h,g,b,-OFF),(a,b,g,OFF)):
   s=cache[score,score>against,against==0][layer];im.paste(s,(X(j)-S//2,Y(t)+offset-S//2),s)
dr=ImageDraw.Draw(im)
f=lambda size:ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-Regular.ttf',size)
fmed=lambda size:ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-Medium.ttf',size)
mono=lambda size:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',size)
dr.text((105,65),'I N T E R W O V E N',font=fmed(49),fill=(228,)*3)
dr.text((105,130),'PREMIER LEAGUE 2025/26  /  FORM AND FLOW',font=f(24),fill=(135,)*3)
last=None
for j,(d,*_) in enumerate(rows):
 date=datetime.date(2025,8,15)+datetime.timedelta(days=d)
 if date.month!=last:
  dr.text((X(j),184),date.strftime('%b').upper(),font=mono(22),fill=(137,)*3,anchor='mm');last=date.month
for x,lab in [(5420,'HOME W'),(5635,'AWAY W'),(5840,'PTS')]:dr.text((x,184),lab,font=mono(21),fill=(150,)*3,anchor='mm')
for t,seq in enumerate(hist):
 y=Y(t);hw=sum(g>b and home for _,g,b,home in seq);aw=sum(g>b and not home for _,g,b,home in seq);pts=sum(3 if g>b else 1 if g==b else 0 for _,g,b,_ in seq)
 dr.text((105,y),f'{t+1:02}',font=mono(24),fill=(105,)*3,anchor='lm');dr.text((173,y),clubs[t],font=f(32),fill=(205,)*3,anchor='lm')
 for x,v in [(5420,hw),(5635,aw),(5840,pts)]:dr.text((x,y),f'{v:02}',font=mono(28),fill=(205 if x==5840 else 158,)*3,anchor='mm')
 print(clubs[t],hw,aw,pts)
dr.text((105,1916),'HOME ABOVE  /  AWAY BELOW  ·  SPHERE AREA: GOALS  ·  RING: WIN  ·  DASHED LINK: DRAW  ·  BRIGHTER LINK: MORE GOALS  ·  RIBBON: 5+ WINS',font=f(24),fill=(140,)*3)
dr.text((5890,1916),'COFFEETABLEVIZ',font=f(24),fill=(140,)*3,anchor='ra')
assert len(rows)==380 and sum(len(s) for s in hist)==760 and sum(g!=b for _,_,_,g,b in rows)==276
im.save(BASE/'interwoven_form_flow_v3.png',dpi=(300,300));im.resize((3000,1000),Image.Resampling.LANCZOS).save(BASE/'interwoven_form_flow_preview_v3.png')
im.crop((70,155,1850,850)).save(BASE/'interwoven_detail_v3.png')
