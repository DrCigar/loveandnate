import sys, os, json
sys.path.insert(0,'/workspace/tile-art/work'); sys.path.insert(0,'/workspace/tile-art/v3')
import numpy as np, cv2
from PIL import Image, ImageFilter
import compose4 as C4
K=C4.K
OUT='/workspace/room-wt/room/assets/'; os.makedirs(OUT,exist_ok=True)
S=2  # 1280 coords -> 2560
cover=np.asarray(Image.open('cover_rect.png').convert('RGB'))[:, :, :]
cover=cover[8:968,28:992]   # trim photo spine/edge slivers
cpoly=np.array([[0,0],[cover.shape[1],0],[cover.shape[1],cover.shape[0]],[0,cover.shape[0]]],float)
ROOMS={
 'a':dict(win=[('08',430,165,112),('14',605,150,200),('19',780,165,112)],book=(1082,371,74),amb=.30,gain=1.15,bdim=.72,wdim=1.0),
 'b':dict(win=[('08',315,165,88),('15',440,160,140),('19',565,165,88)],book=(890,300,72),amb=.42,gain=1.35,bdim=.62,wdim=.9),
 'c':dict(win=[('14',255,175,190),('18',445,165,130)],book=(990,413,84),amb=.40,gain=1.30,bdim=.62,wdim=1.0),
}
NAMES={'08':'Amy Window','14':'Owl Window','15':'Gaga Window','18':'The King Has Left The Planet Window','19':'Hendrix Window'}
def run(n):
    R=ROOMS[n]; p=f'/workspace/room/bg/{n}-2560.png'
    im=Image.open(p) if os.path.exists(p) else Image.open(f'/workspace/room/bg/{n}.jpg').resize((2560,1440),Image.LANCZOS)
    bg=np.asarray(im.convert('RGB')).astype(np.float32); H,W,_=bg.shape
    L=C4.lightmap(bg,sigma=W*.05); L=np.clip(L,0,1.2)
    meta={'windows':[]}
    for wn,cx,cy,w in R['win']:
        src,q=C4.wsrc(wn); s=w*S/np.ptp(q[:,0]); h=np.ptp(q[:,1])*s
        C4.place(bg,src,q,s,(cx*S,cy*S-0*h/2),L=L,ambient=R['amb'],gain=R['gain'],
                 shadows=((.002,.006,.008,.55),(0,.0015,.002,.5)),sharpen=(1.0,30,2),dim=R['wdim'])
        meta['windows'].append({'id':wn,'name':NAMES[wn],'box':[cx-w/2,cy-h/S/2,cx+w/2,cy+h/S/2]})
    bx,by,bw=R['book']; s=bw*S/cover.shape[1]; bh=cover.shape[0]*s
    C4.place(bg,cover,cpoly,s,(bx*S,by*S-bh/2-1),L=L,ambient=R['amb']+.05,gain=R['gain'],
             shadows=((.003,.002,.006,.6),(0,.0012,.0015,.7)),sharpen=(1.0,30,2),dim=R['bdim'])
    meta['book']=[bx-bw/2,by-bh/S,bx+bw/2,by]
    out=Image.fromarray(np.clip(bg,0,255).astype('uint8'))
    out.save(OUT+f'room-{n}.webp',quality=80,method=6)
    out.resize((1280,720),Image.LANCZOS).save(f'prev-{n}.png')
    json.dump(meta,open(f'meta-{n}.json','w'),indent=1,default=float)
    print(n,os.path.getsize(OUT+f'room-{n}.webp')//1024,'KB',meta)
for n in sys.argv[1:]: run(n)
