"""Recover missing website media, never alter the original approval manifest."""
from pathlib import Path
import hashlib, subprocess, sys
import cv2, numpy as np
from scipy.interpolate import CubicHermiteSpline
from PIL import Image

base=Path(__file__).resolve().parent
root=base.parents[2]
out=root/'site/assets/gallery/interwoven'
out.mkdir(parents=True,exist_ok=True)
manifest=base/'ASSETS.sha256'
expected={name.split('/')[-1]: digest for digest,name in (s.split() for s in manifest.read_text().splitlines() if s.strip())}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if all((out/n).is_file() and digest(out/n)==v for n,v in expected.items()):
    print('All original approved assets already present.')
    sys.exit(0)
assert not any((out/n).exists() for n in expected), 'Refuse to overwrite existing media'
subprocess.run([sys.executable,str(base/'render_interwoven.py')],check=True)
for src,name,pixels in [
    ('interwoven_form_flow_v3.png','artwork.png','fd5c65b5a9750e11b57972738f571c7ab3b6454c59b6b62e30f0f346678f0098'),
    ('interwoven_detail_v3.png','detail.png','676658b3ea1a7da30f8a0324a5bd6377a9d6504eb8b2295765c91923775703ac')]:
    p=base/src
    assert hashlib.sha256(Image.open(p).convert('RGB').tobytes()).hexdigest()==pixels, 'Approved artwork pixels differ: '+name
    (out/name).write_bytes(p.read_bytes())
    print(name,'approved pixels verified; exact file bytes:',digest(out/name)==expected[name])
# Same camera path as the approved continuous loop, using a verified compressed
# copy of the same empty gallery backdrop, with approved artwork composited in.
back=base/'gallery-backdrop-recovery.webp'
assert digest(back)=='39536b721e7e4843a3681f93933cf7f57c29ce9c0be7c15da284aa1090e4d690'
cv2.setNumThreads(2)
bg0=cv2.resize(cv2.imread(str(back)),(1672,941),interpolation=cv2.INTER_CUBIC)
h,w=bg0.shape[:2]; x0,x1=207,1464; y0,y1=290,626; ny0,ny1=245,664
bg=np.concatenate([cv2.resize(bg0[:y0],(w,ny0),interpolation=cv2.INTER_CUBIC),cv2.resize(bg0[y0:y1],(w,ny1-ny0),interpolation=cv2.INTER_CUBIC),cv2.resize(bg0[y1:],(w,h-ny1),interpolation=cv2.INTER_CUBIC)],axis=0)
art=cv2.imread(str(out/'artwork.png'))
assert art.shape[:2]==(2000,6000)
S=3;scene=cv2.resize(bg,(w*S,h*S),interpolation=cv2.INTER_CUBIC)
scene[ny0*S:ny1*S,x0*S:x1*S]=cv2.resize(art,((x1-x0)*S,(ny1-ny0)*S),interpolation=cv2.INTER_AREA)
T=23;keys=[0,3.5,7.5,17.5,T]
poses=[[836,470,1660,0],[650,457,1200,.11],[410,365,430,.015],[1250,385,430,.015],[836,470,1660,0]]
vel=[[-28,-1,0,.018],[-65,-13,-180,0],[30,2,0,0],[35,3,0,0],[-28,-1,0,.018]]
spline=CubicHermiteSpline(keys,poses,vel,axis=0)
W,H=1600,900;corn=np.float32([[0,0],[W-1,0],[W-1,H-1],[0,H-1]])
def camera(t):
    cx,cy,fw,sk=spline(t%T);fh=fw*H/W;hl=fh*(1-sk);hr=fh*(1+sk)
    q=np.float32([[cx-fw/2,cy-hl/2],[cx+fw/2,cy-hr/2],[cx+fw/2,cy+hr/2],[cx-fw/2,cy+hl/2]])
    return cv2.warpPerspective(scene,cv2.getPerspectiveTransform(q*S,corn),(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REPLICATE)
assert np.array_equal(camera(0),camera(T))
assert np.allclose(spline(0,1),spline(T,1))
assert np.min(np.linalg.norm(spline(np.linspace(0,T,1000),1)[:,:3],axis=1))>1
assert cv2.imwrite(str(out/'gallery.jpg'),camera(0),[cv2.IMWRITE_JPEG_QUALITY,94])
card=Image.new('RGB',(1600,1600),'#F3F4F6')
card.paste(Image.open(out/'gallery.jpg').convert('RGB'),(0,350));card.save(out/'card.jpg',quality=94)
cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s','1600x900','-r','30','-i','-','-an','-c:v','libx264','-threads','4','-preset','fast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(out/'walkthrough.mp4')]
proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for i in range(T*30):proc.stdin.write(camera(i/30).tobytes())
proc.stdin.close()
assert proc.wait()==0
for n in ('artwork.png','detail.png','card.jpg','gallery.jpg'):
    with Image.open(out/n) as im: im.verify()
import json
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,width,height,r_frame_rate:format=duration','-of','json',str(out/'walkthrough.mp4')]))
v=probe['streams'][0]
assert (v['codec_name'],v['width'],v['height'],v['r_frame_rate'])==('h264',1600,900,'30/1')
assert float(probe['format']['duration'])==23
(base/'RECOVERY_ASSETS.sha256').write_text(''.join(digest(out/n)+'  '+str((out/n).relative_to(root))+'\n' for n in sorted(expected)))
print('Verified recovered media:',probe)
