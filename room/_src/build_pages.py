import json, re, html
SRC='/workspace/room-wt/index.html'
src=open(SRC).read()
lines=src.split('\n')
# hero+panels block: from '<header class="hero">' to the closing '</section>' of panels
start=src.index('<header class="hero">'); end=src.index('</section>', src.index('<section class="panels"'))+len('</section>')
SP='https://open.spotify.com/artist/48cIusfYn89O9pA7eVWTlr'; AM='https://music.apple.com/us/artist/loveandnate/1625477213'
SPSVG=re.search(r'<a class="sp"[^>]*>\s*(<svg.*?</svg>)',src,re.S).group(1)
AMSVG=re.search(r'<a class="am"[^>]*>\s*(<svg.*?</svg>)',src,re.S).group(1).replace('am-grad','am-grad2')
W,H=1280,720
def pct(b,pad=0):
    x0,y0,x1,y1=b; x0-=pad;y0-=pad;x1+=pad;y1+=pad
    return f'left:{x0/W*100:.3f}%;top:{y0/H*100:.3f}%;width:{(x1-x0)/W*100:.3f}%;height:{(y1-y0)/H*100:.3f}%'
def qs(q): return ' '.join(f'{x},{y}' for x,y in q)
def bbox(q): xs=[p[0] for p in q]; ys=[p[1] for p in q]; return [min(xs),min(ys),max(xs),max(ys)]
R={
 'a':dict(name='Detroit loft',tv=[[533,335],[688,335],[688,447],[533,447]],tvbody=[509,315,750,469],
          laptop=[[969,422],[1138,430],[1120,560],[947,533]],phone=[[1152,590],[1198,599],[1150,622],[1099,611]],
          record=[219,322,415,481]),
 'b':dict(name='Art deco study',tv=[[487,331],[595,331],[595,407],[487,407]],tvbody=[450,302,631,446],
          laptop=[[870,435],[1011,444],[996,543],[854,523]],phone=[[1055,563],[1096,574],[1058,593],[1014,582]],
          record=[222,381,412,446]),
 'c':dict(name='Night studio',tv=[[586,345],[738,345],[738,462],[586,462]],tvbody=[569,329,765,488],
          laptop=[[1015,447],[1188,455],[1172,580],[988,572]],phone=[[874,584],[923,612],[866,619],[819,594]],
          record=[287,425,506,488]),
}
CSS=open('/workspace/room/work/room.css').read(); JS=open('/workspace/room/work/room.js').read()
for n,r in R.items():
    meta=json.load(open(f'/workspace/room/work/meta-{n}.json'))
    wb=meta['windows']; wbox=[min(w['box'][0] for w in wb),min(w['box'][1] for w in wb),max(w['box'][2] for w in wb),max(w['box'][3] for w in wb)]
    wnames=', '.join(w['name'] for w in wb)
    lb=bbox(r['laptop']); pb=bbox(r['phone'])
    hot=lambda id_,href,box,label,sub,pad=8,ext='',cls='': (
      f'<a class="hot {cls}" id="{id_}" href="{href}"{ext} style="{pct(box,pad)}" aria-label="{html.escape(label+" — "+sub)}">'
      f'<span class="tag" aria-hidden="true"><b>{label}</b><i>{sub}</i></span></a>')
    ext=' target="_blank" rel="noopener noreferrer"'
    room=f'''<section class="room room--{n}" aria-label="The LOVEANDNATE studio, {r['name']} concept">
  <canvas id="stars" style="display:none"></canvas><div class="panels" style="display:none"></div>
  <div class="room-pan" tabindex="0" aria-label="Studio room. Drag or scroll sideways to look around.">
  <div class="room-scene">
    <img class="room-bg" src="/room/assets/room-{n}.webp" alt="" width="2560" height="1440" fetchpriority="high">
    <div class="screen tv" data-quad="{qs(r['tv'])}" aria-hidden="true">
      <video muted loop playsinline autoplay preload="metadata" poster="/wellwellwell/bg-poster.webp"><source src="/wellwellwell/bg.mp4" type="video/mp4"></video><i class="crt"></i>
    </div>
    <div class="screen laptop" data-quad="{qs(r['laptop'])}" aria-hidden="true">
      <video muted loop playsinline preload="none" poster="/smplfrks/media/trailer/poster-1280.webp" data-desktop-only><source src="/smplfrks/media/trailer/trailer-720.mp4" type="video/mp4"></video><i class="glare"></i>
    </div>
    <div class="screen phone" data-quad="{qs(r['phone'])}" aria-hidden="true"><img src="/room/assets/innerpool-screen.webp" alt=""></div>
    {hot('windows','/windows',wbox,'Windows','Hand-painted, sold out',10,cls='tag-below')}
    {hot('books','https://www.amazon.com/Marvin-Stench-Zepp/dp/1540831094',meta['book'],'Books','Marvin Stench on Amazon',8)}
    {hot('movies','/wellwellwell',r['tvbody'],'Movies','WELL WELL WELL',4)}
    {hot('nfts','/smplfrks',lb,'NFTs','SMPL FRKS',6)}
    {hot('apps','#innerpool',pb,'Apps','Innerpool, coming soon',12,cls='small')}
    <div class="hot-music" style="{pct(r['record'],6)}">
      <a class="hot" id="music" href="{SP}"{ext} aria-label="Music — Listen now on Spotify"></a>
      <span class="tag tag-music"><b>Music</b><i>21 albums released in 24 hours</i>
        <span class="streams"><span class="listen">Listen now</span>
        <a class="sp" href="{SP}"{ext} aria-label="LOVEANDNATE on Spotify">{SPSVG}</a>
        <a class="am" href="{AM}"{ext} aria-label="LOVEANDNATE on Apple Music">{AMSVG}</a></span></span>
    </div>
  </div>
  </div>
  <div class="room-copy">
    <p class="eyebrow">Creative studio</p>
    <h1>Six disciplines.<br><em>One practice.</em></h1>
    <p class="hint">Hover or tap anything in the room.</p>
  </div>
  <div class="room-list" role="navigation" aria-label="Disciplines in the room">
    <a href="{SP}"{ext}><span class="n">01</span><b>Music</b><i>Listen now · Spotify / Apple Music</i></a>
    <a href="https://www.amazon.com/Marvin-Stench-Zepp/dp/1540831094"><span class="n">02</span><b>Books</b><i>Marvin Stench</i></a>
    <a href="#innerpool"><span class="n">03</span><b>Apps</b><i>Innerpool, coming soon</i></a>
    <a href="/wellwellwell"><span class="n">04</span><b>Movies</b><i>WELL WELL WELL</i></a>
    <a href="/smplfrks"><span class="n">05</span><b>NFTs</b><i>SMPL FRKS</i></a>
    <a href="/windows"><span class="n">06</span><b>Windows</b><i>Sold-out gallery</i></a>
  </div>
</section>'''
    out=src[:start]+room+src[end:]
    out=out.replace('</style>',CSS+'\n</style>',1)
    out=out.replace('</body>','<script>\n'+JS+'\n</script>\n</body>',1)
    out=out.replace('<title>',f'<meta name="robots" content="noindex">\n<title>[Room concept {n.upper()}] ',1)
    open(f'/workspace/room-wt/room/{n}.html','w').write(out); print(n,'ok',wnames)
