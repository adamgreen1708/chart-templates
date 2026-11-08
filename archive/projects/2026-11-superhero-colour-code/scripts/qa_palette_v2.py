"""Inspect the three *actual* v2 GitHub PNGs, export 320px and 390px previews.

Automated 7% margin and background checks complement, never replace, visual
inspection of actual exported pixels for clipping, internal collisions, and legibility.
"""
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"output"
FILES=(
    "superhero_v2_01_costume_gallery.png",
    "superhero_v2_02_role_scorecard.png",
    "superhero_v2_03_colour_twins.png",
)
BG=(243,244,246)
SIZE=1600
EDGE=int(0.07*SIZE)
LIMIT=55

def check_file(path):
    with Image.open(path) as original:
        assert original.size==(SIZE,SIZE), f"Not square 1600px: {path} {original.size}"
        im=original.convert("RGB")
    assert im.getpixel((0,0))==BG, (path,im.getpixel((0,0)))
    p=im.load()
    for y in range(SIZE):
        for x in list(range(EDGE))+list(range(SIZE-EDGE,SIZE)):
            pixel=p[x,y]
            if max(abs(pixel[k]-BG[k]) for k in range(3))>=LIMIT:
                raise AssertionError(f"7% margin breach {path}: ({x},{y})")
    for y in list(range(EDGE))+list(range(SIZE-EDGE,SIZE)):
        for x in range(EDGE,SIZE-EDGE):
            pixel=p[x,y]
            if max(abs(pixel[k]-BG[k]) for k in range(3))>=LIMIT:
                raise AssertionError(f"7% margin breach {path}: ({x},{y})")
    out=DIR/"qa_v2"
    out.mkdir(parents=True,exist_ok=True)
    for size in (390,320):
        target=out/f"{path.stem}_{size}.png"
        im.resize((size,size),Image.Resampling.LANCZOS).save(target)
        print(f"PASS: {target} — visually inspect actual phone export")

def main():
    for name in FILES:
        check_file(DIR/name)
    print("PASS 3 new full-size images: exact 1600px, grey canvas, 7% significant-ink safe frame")
if __name__=="__main__":
    main()
