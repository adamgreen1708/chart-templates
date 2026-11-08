"""Check 1600px house exports and produce 390px / 320px review images.

Purpose: project-specific draft QA only. Automated checks do not replace
a person reviewing the final PNGs for readability and overlap.
"""
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/"output"
FILES=(
  "superhero_01_hue_skew.png",
  "superhero_02_marvel_dc_primary.png",
  "superhero_03_costume_rebels.png",
)
BG=(243,244,246)
SIZE=1600
SAFE=round(SIZE*0.07)
THRESHOLD=55
def check_edge(img,name):
    rgb=img.convert("RGB")
    if rgb.getpixel((0,0))!=BG:
        raise ValueError(f"{name}: wrong canvas background {rgb.getpixel((0,0))}")
    # significant dark/colour foreground must not bleed into the outer 7%.
    px=rgb.load()
    for y in range(SIZE):
        for x in list(range(SAFE))+list(range(SIZE-SAFE,SIZE)):
            c=px[x,y]
            if max(abs(c[i]-BG[i]) for i in range(3))>=THRESHOLD:
                raise ValueError(f"{name}: foreground at x={x},y={y} (7% border)")
    for y in list(range(SAFE))+list(range(SIZE-SAFE,SIZE)):
        for x in range(SAFE,SIZE-SAFE):
            c=px[x,y]
            if max(abs(c[i]-BG[i]) for i in range(3))>=THRESHOLD:
                raise ValueError(f"{name}: foreground at x={x},y={y} (7% border)")
def main():
    target=OUTPUT/"qa"
    target.mkdir(parents=True,exist_ok=True)
    for name in FILES:
        path=OUTPUT/name
        with Image.open(path) as img:
            if img.size!=(SIZE,SIZE):
                raise ValueError(f"{name}: expected 1600px square, got {img.size}")
            check_edge(img,name)
            for size in (390,320):
                dest=target/f"{path.stem}_{size}.png"
                img.convert("RGB").resize((size,size),Image.Resampling.LANCZOS).save(dest)
                print(f"Created {dest}; manual phone legibility review still required")
    print("PASS: square exports, grey canvas and significant-ink 7% margins")
if __name__=="__main__":
    main()
