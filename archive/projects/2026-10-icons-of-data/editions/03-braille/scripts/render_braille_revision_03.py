"""New editorial Chart 3 for Icons of Data 03: Why Braille was a breakthrough.

Works alongside unchanged Chart 2; NO actual tactile Braille is generated.
Historical comparisons per Perkins; modern UEB conventions per RNIB/UKAAF/ICEB.
Original four-panel Coffeetableviz house treatment, deterministic 1920x1920.
"""
from pathlib import Path
import importlib.util, hashlib, math
from PIL import Image
from matplotlib.patches import Arc, Polygon, FancyArrowPatch, PathPatch
from matplotlib.path import Path as MplPath
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('base_braille',HERE/'render_braille.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

f=b.fig_base()
b.header(f,'Why Braille was a breakthrough.','Not just a clever code. A practical way to read and write.')
coords=[(.075,.491,.411,.329),(.514,.491,.411,.329),(.075,.147,.411,.329),(.514,.147,.411,.329)]
for x,y,w,h in coords:b.rect(f,x,y,w,h,b.WHITE,ec=b.LIGHT,lw=.85)

def label(i,name,sub):
    x,y,w,h=coords[i]
    b.txt(f,x+.026,y+h-.047,'0'+str(i+1)+'   '+name,sz=12.7,weight='bold',family=b.HEAD)
    b.txt(f,x+.026,y+h-.086,sub,sz=9.1,color=b.MUTED)

label(0,'The fingertip test','Smaller signs, easier to take in.')
label(1,'Read AND write','People could produce their own text.')
label(2,'Context matters','One pattern, more than one meaning.')
label(3,'Designed for touch','An image does not recreate the feeling.')

# Panel 1: true historical change is grid size (two columns, six rows -> 2x3).
# These are blank cell guides, NOT transcribed Barbier/Braille signs.
def grid_cell(cx, cy, rows, colour, radius=.0108, vert=.029, horiz=.031):
    for i in range(rows):
        for col in range(2):
            xx=cx+col*horiz
            yy=cy+(rows-1)/2*vert-i*vert
            b.circle(f,xx,yy,radius,b.MUTE_FILL if colour=='muted' else b.TEAL,z=12)

grid_cell(.171,.632,6,'muted',radius=.0106,vert=.0268,horiz=.031)
grid_cell(.361,.632,3,'teal',radius=.0125,vert=.032,horiz=.035)
b.txt(f,.290,.632,'→',sz=18.5,color=b.MUTED,ha='center')
b.txt(f,.155,.533,'BARBIER',sz=8.6,color=b.MUTED,weight='bold')
b.txt(f,.155,.514,'12-dot cell',sz=8.1,color=b.MUTED)
b.txt(f,.326,.533,'BRAILLE',sz=8.6,color=b.TEAL,weight='bold')
b.txt(f,.326,.514,'6-dot cell',sz=8.1,color=b.MUTED)

# Panel 2: icon-like original drawing of tactile reading and independent writing.
# Open-page visual: outline two pages, central fold and simple 'embossed marks'.
book_x=.577;book_y=.605
b.line(f,book_x-.027,book_y-.036,book_x+.001,book_y-.052,color=b.INK,lw=2)
b.line(f,book_x+.001,book_y-.052,book_x+.033,book_y-.036,color=b.INK,lw=2)
b.line(f,book_x-.027,book_y-.036,book_x-.027,book_y+.051,color=b.INK,lw=2)
b.line(f,book_x+.033,book_y-.036,book_x+.033,book_y+.051,color=b.INK,lw=2)
b.line(f,book_x-.027,book_y+.051,book_x+.001,book_y+.040,color=b.INK,lw=2)
b.line(f,book_x+.001,book_y+.040,book_x+.033,book_y+.051,color=b.INK,lw=2)
b.line(f,book_x+.001,book_y-.052,book_x+.001,book_y+.040,color=b.INK,lw=1.6)
for xx,yy in [(book_x-.019,book_y+.024),(book_x-.010,book_y+.024),(book_x-.019,book_y+.008),(book_x+.014,book_y+.023),(book_x+.023,book_y+.023),(book_x+.014,book_y+.009)]:
    b.circle(f,xx,yy,.0038,b.TEAL,z=14)
b.txt(f,.644,.604,'→',sz=19,color=b.MUTED,ha='center')
# Slate and stylus, original simplified tool, not a photograph.
sx=.675;sy=.574
b.rect(f,sx,sy,.192,.110,fc=b.WHITE,ec=b.INK,lw=1.4,r=.006)
for row in range(3):
    for col in range(6):
        b.circle(f,sx+.020+col*.029,sy+.083-row*.030,.0059,b.MUTE_FILL,z=12)
b.line(f,.868,.699,.837,.652,color=b.RED,lw=3.2)
b.circle(f,.868,.699,.005,b.RED,z=14)
b.txt(f,.576,.519,'READ',sz=9.0,weight='bold',color=b.TEAL,ha='center')
b.txt(f,.767,.519,'WRITE',sz=9.0,weight='bold',color=b.RED,ha='center')

# Panel 3: one small pattern is understood through code context, without a
# second technical matrix of dot arrangements (Chart 2 already does that).
b.txt(f,.107,.370,'Same dot pattern',sz=10.3,weight='bold',color=b.TEXT)
# Only draw the a/digit-1 pattern once.
b.cell(f,.151,.269,.144,(1,),raised=b.TEAL)
b.line(f,.249,.269,.291,.269,color=b.LIGHT,lw=1.2)
b.txt(f,.307,.327,'letter context',sz=9,color=b.MUTED)
b.txt(f,.307,.294,'a',sz=21.5,weight='bold',family=b.HEAD)
b.txt(f,.307,.255,'after number sign',sz=9,color=b.MUTED)
b.txt(f,.307,.222,'1',sz=21.5,weight='bold',family=b.HEAD,color=b.RED)
b.txt(f,.110,.179,'Modern UK UEB · dot 1 is unchanged.',sz=8.0,color=b.MUTED)

# Panel 4: graphic versus raised media, not a simulated tactile photo.
b.txt(f,.539,.360,'ON SCREEN',sz=8.3,color=b.MUTED,weight='bold')
for dx in (0,.038,.076):b.circle(f,.568+dx,.315,.012,b.TEAL,z=12)
b.txt(f,.539,.280,'Flat circles',sz=8.3,color=b.MUTED)
b.line(f,.697,.252,.697,.382,color=b.LIGHT,lw=1.1)
b.txt(f,.721,.360,'ON PAPER',sz=8.3,color=b.MUTED,weight='bold')
b.line(f,.722,.300,.896,.300,color=b.INK,lw=1.25)
for xpos in (.749,.798,.848):
    f.add_artist(Arc((xpos,.300),.040,.033,theta1=0,theta2=180,color=b.INK,lw=2.0,transform=f.transFigure,zorder=14))
b.txt(f,.721,.264,'Raised marks',sz=8.3,color=b.MUTED)
b.txt(f,.540,.178,'A drawing explains. Touch reads.',sz=9.0,color=b.TEXT,weight='bold')

b.footer(f,'02','History: Perkins (Barbier 12 vs Braille 6) · UK UEB: RNIB/UKAAF · drawn diagrams, not tactile Braille')
path=HERE/'visuals'/'03_why_braille_mattered.png'
f.savefig(path,dpi=240)
plt.close(f)
im=Image.open(path)
assert im.size==(1920,1920)
print(path,im.size,path.stat().st_size,hashlib.sha256(path.read_bytes()).hexdigest())
