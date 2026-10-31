from pathlib import Path
import sys
from PIL import Image
D=Path(__file__).resolve().parents[1];R=D.parents[2]
sys.path.insert(0,str(R))
from scripts.qa_social_rendered import check_chart
for n in [1,2,3]:
 p=D/f'output/patrick_stewart_{n}.png';check_chart(p)
 im=Image.open(p)
 for size in [390,320]:im.resize((size,size),Image.Resampling.LANCZOS).save(p.with_name(f'{p.stem}_{size}.png'))
print('Phone previews exported: manual legibility inspection required.')
