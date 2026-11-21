(()=>{ // ROOM concept: map real content onto the screens in the backdrop, mobile pan
  const scene=document.querySelector('.room-scene'); if(!scene) return;
  const BW=1280;
  function H(src,dst){const A=[],b=[];for(let i=0;i<4;i++){const[x,y]=src[i],[u,v]=dst[i];A.push([x,y,1,0,0,0,-u*x,-u*y]);b.push(u);A.push([0,0,0,x,y,1,-v*x,-v*y]);b.push(v);}
    for(let c=0;c<8;c++){let p=c;for(let r=c+1;r<8;r++)if(Math.abs(A[r][c])>Math.abs(A[p][c]))p=r;[A[c],A[p]]=[A[p],A[c]];[b[c],b[p]]=[b[p],b[c]];
      for(let r=0;r<8;r++){if(r===c)continue;const f=A[r][c]/A[c][c];for(let k=c;k<8;k++)A[r][k]-=f*A[c][k];b[r]-=f*b[c];}}
    return b.map((v,i)=>v/A[i][i]);}
  const screens=[...scene.querySelectorAll('.screen[data-quad]')].map(el=>({el,q:el.dataset.quad.split(' ').map(p=>p.split(',').map(Number))}));
  function layout(){const k=scene.clientWidth/BW;
    for(const{el,q}of screens){const w=el.offsetWidth,h=el.offsetHeight;
      const m=H([[0,0],[w,0],[w,h],[0,h]],q.map(([x,y])=>[x*k,y*k]));
      el.style.transform=`matrix3d(${m[0]},${m[3]},0,${m[6]},${m[1]},${m[4]},0,${m[7]},0,0,1,0,${m[2]},${m[5]},0,1)`;}}
  new ResizeObserver(layout).observe(scene); layout();
  const mobile=matchMedia('(max-width:760px)').matches;
  scene.querySelectorAll('video').forEach(v=>{ if(mobile&&v.hasAttribute('data-desktop-only')) return; v.play().catch(()=>{}); });
  const pan=document.querySelector('.room-pan'); if(mobile&&pan){pan.scrollLeft=(pan.scrollWidth-pan.clientWidth)*.5;}
})();
