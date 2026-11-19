#!/usr/bin/env python3
"""Coffeetableviz LinkedIn carousel: layout-only; approved GitHub chart PNGs used verbatim.

Run on GitHub Actions, not a chart render. No plot generation or data recalculation.
All inputs are site assets generated through documented GitHub procedures.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

SIZE = 1080
BG = HexColor('#F3F4F6')
DARK = HexColor('#16191C')
MID = HexColor('#56616B')
RED = HexColor('#C44E52')
BLUE = HexColor('#1F8FA8')
ARTICLE = 'https://coffeetableviz.com/stories/robert-pattinson-was-already-in-bonds-orbit/'

FILES = (
    ('site/assets/features/robert-pattinson-bond.png', '22021795d42e0b39dd332cf689bce5366339a0802ba6b9f6ce0ef17c10e65d4a'),
    ('site/assets/charts/robert-pattinson-bond/01_twilight_average.png', '5a08a62773ba68b45120bfd1d6cc895e00bd295087a09896ccf35375eb677ed5'),
    ('site/assets/charts/robert-pattinson-bond/02_reinvention.png', 'afcaaec8e57a06ca28873a08f7d12625e671139f6e14b6cdf20bc79641cd1c19'),
    ('site/assets/charts/robert-pattinson-bond/03_bond_connections.png', '722b42c58661b6aa3fbb7c95b9ee2874bcfab949fded2aae451e84029e65d9cd'),
)

def register_fonts():
    font_dir = Path('/usr/share/fonts/truetype/dejavu')
    paths = {'CTV': font_dir/'DejaVuSans.ttf', 'CTV-Bold': font_dir/'DejaVuSans-Bold.ttf'}
    for alias, path in paths.items():
        if not path.exists():
            raise FileNotFoundError(f'Missing system font: {path}. Install fonts-dejavu-core.')
        if alias not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(alias, str(path)))

def txt(c, content, x, y, size, *, font='CTV', color=DARK):
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawString(x, y, content)

def line(c, x1, y1, x2, y2, color=RED, width=3):
    c.setStrokeColor(color); c.setLineWidth(width)
    c.line(x1, y1, x2, y2)

def draw_cover(c, feature):
    c.setFillColor(BG); c.rect(0,0,SIZE,SIZE,fill=1,stroke=0)
    txt(c, 'COFFEETABLEVIZ   /   FILM + DATA', 78, 1018, 17, font='CTV-Bold',color=MID)
    line(c,78,987,1002,987,color=HexColor('#CFD4D7'),width=1.7)
    line(c,78,987,202,987,color=RED,width=5)
    txt(c, "THE NAME'S PATTINSON.", 75, 888, 57, font='CTV-Bold')
    txt(c, 'ROBERT PATTINSON.', 75, 805, 67, font='CTV-Bold')
    txt(c, 'From Twilight to 007, via a few unexpected co-stars.',75,748,22,color=MID)
    # Portrait-free cover artwork: the exact approved file, not regenerated or recoloured.
    c.drawImage(ImageReader(str(feature)), 356, 104, width=644, height=644, mask='auto')
    for y,n,caption in ((585,'5','TWILIGHT FILMS'),(428,'33','RATED FILMS'),(271,'6','BOND CAST LINKS')):
        txt(c,n,81,y,61,font='CTV-Bold',color=RED if n=='6' else DARK)
        txt(c,caption,83,y-38,17,font='CTV-Bold',color=MID)
    line(c,78,86,1002,86,color=HexColor('#CFD4D7'),width=1)
    txt(c,'ADAM GREEN   |   COFFEETABLEVIZ.COM',78,52,16,font='CTV-Bold',color=MID)
    # Large and readable rather than a tiny swipe cue.
    c.setFont('CTV',16)
    txt(c,'SWIPE FOR THREE CHARTS',740,52,15,font='CTV-Bold',color=DARK)
    c.showPage()

def draw_chart(c, path):
    # Page image uses the exact original pixels - no plotting, labels, recolouring or crop.
    c.drawImage(ImageReader(str(path)),0,0,width=SIZE,height=SIZE,mask='auto')
    c.showPage()

def draw_closing(c):
    c.setFillColor(BG);c.rect(0,0,SIZE,SIZE,fill=1,stroke=0)
    txt(c,'THE UNEXPECTED BOND CONNECTION',78,1019,17,font='CTV-Bold',color=MID)
    line(c,78,987,1002,987,color=HexColor('#CFD4D7'),width=1.7)
    line(c,78,987,202,987,color=RED,width=5)
    txt(c,"HE'D ALREADY",75,888,72,font='CTV-Bold')
    txt(c,'MET BOND.',75,795,82,font='CTV-Bold')
    line(c,78,749,1002,749,color=RED,width=6)
    txt(c,'PIERCE BROSNAN',81,677,25,font='CTV-Bold',color=RED)
    txt(c,"played Pattinson's father",79,614,42,font='CTV-Bold')
    txt(c,'in Remember Me (2010).',79,559,37,font='CTV')
    txt(c,'Sixteen years later, he welcomed',79,456,34)
    txt(c,'Pattinson to the Bond family.',79,409,34)
    # Link zone deliberately placed above source caveat and footer.
    c.setFillColor(DARK);c.roundRect(78,235,924,113,12,stroke=0,fill=1)
    txt(c,'READ THE FULL STORY',106,298,28,font='CTV-Bold',color=HexColor('#FFFFFF'))
    txt(c,'coffeetableviz.com',106,258,24,color=HexColor('#E7EDF1'))
    c.linkURL(ARTICLE,(78,235,1002,348),relative=0,thickness=0)
    txt(c,'IMDb film ratings, not acting scores. Vote totals are not unique viewers.',79,169,17,color=MID)
    txt(c,'Source snapshot: 18 November 2026. Cast connections are verified examples.',79,139,17,color=MID)
    line(c,78,85,1002,85,color=HexColor('#CFD4D7'),width=1)
    txt(c,'SIMPLE CHARTS. CLEAR STORIES.',78,51,18,font='CTV-Bold',color=DARK)
    txt(c,'ADAM GREEN   |   COFFEETABLEVIZ',682,51,15,font='CTV-Bold',color=MID)
    c.showPage()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo-root',type=Path,default=Path.cwd())
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    register_fonts()
    inputs=[]
    for name,expect in FILES:
        p=args.repo_root/name
        if not p.exists():raise FileNotFoundError(f'GitHub asset not found: {p}')
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if digest!=expect:raise ValueError(f'Approved image hash changed: {name}\n {digest} != {expect}')
        inputs.append(p)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(args.output), pagesize=(SIZE,SIZE), pageCompression=1)
    c.setTitle("The name's Pattinson. Robert Pattinson. | Coffeetableviz")
    c.setAuthor('Adam Green | Coffeetableviz')
    c.setSubject('Five-page LinkedIn carousel using three approved IMDb-based GitHub chart renders')
    draw_cover(c, inputs[0])
    for p in inputs[1:]:draw_chart(c,p)
    draw_closing(c)
    c.save()
    print('Created',args.output,args.output.stat().st_size,'bytes; 5 square pages')
    print('All four GitHub image SHA256 hashes validated; no chart rerendering')

if __name__ == '__main__':main()