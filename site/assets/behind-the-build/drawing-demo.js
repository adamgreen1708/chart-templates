(() => {
'use strict';
const $=id=>document.getElementById(id),ns='http://www.w3.org/2000/svg';
const raster=$('btb-draw-raster');
if(raster){const zoom=$('btb-draw-zoom'),resolution=$('btb-draw-resolution'),vector=$('btb-draw-vector'),pixels=$('btb-draw-pixels');let lastN=0;
function render(){const z=Number(zoom.value),n=Number(resolution.value),box=[80-80/z,80-80/z,160/z,160/z].join(' ');vector.setAttribute('viewBox',box);pixels.setAttribute('viewBox',box);$('btb-draw-zoom-value').textContent=z.toFixed(1)+'×';if(lastN!==n){const nodes=[];for(let i=0;i<n*n;i++){const r=document.createElementNS(ns,'rect'),x=i%n,y=Math.floor(i/n);Object.entries({x:x*160/n,y:y*160/n,width:160/n+.05,height:160/n+.05,fill:Math.hypot(x+.5-n/2,y+.5-n/2)<=n*44/160?'#1f8fa8':'#fff'}).forEach(([k,v])=>r.setAttribute(k,v));nodes.push(r);}pixels.replaceChildren(...nodes);pixels.setAttribute('aria-label','Simulated raster circle at '+n+' by '+n+' pixels');lastN=n;}}
zoom.addEventListener('input',render);resolution.addEventListener('change',render);$('btb-draw-raster-reset').addEventListener('click',()=>{zoom.value='1';resolution.value='12';render();});render();}
const triangle=$('btb-draw-triangle');
if(triangle){const rotation=$('btb-draw-rotation'),corners=[[0,1,3],[1,2,0],[2,3,1],[3,0,2]],vertices=[[20,20],[140,20],[140,140],[20,140]],groups=Array.from(triangle.querySelectorAll('[data-vertex]'));
function render(){const points=corners[Number(rotation.value)].map(i=>vertices[i]);$('btb-draw-polygon').setAttribute('points',points.map(p=>p.join(',')).join(' '));groups.forEach((g,i)=>{const [x,y]=points[i],c=g.querySelector('circle'),t=g.querySelector('text');c.setAttribute('cx',x);c.setAttribute('cy',y);t.setAttribute('x',x);t.setAttribute('y',y+3.5);});$('btb-draw-path').textContent='ctx.beginPath();\nctx.moveTo('+points[0].join(', ')+');\nctx.lineTo('+points[1].join(', ')+');\nctx.lineTo('+points[2].join(', ')+');\nctx.closePath();\nctx.fill();';}
rotation.addEventListener('change',render);$('btb-draw-triangle-reset').addEventListener('click',()=>{rotation.value='0';render();});render();}
const area=$('btb-draw-area');
if(area){const multiple=$('btb-draw-multiple'),buttons=Array.from(area.querySelectorAll('[data-sizing]'));let mode='area';
function render(){const v=Number(multiple.value),ratio=mode==='area'?Math.sqrt(v):v,ar=mode==='area'?v:v*v;$('btb-draw-second-circle').setAttribute('r',22*ratio);['second','circle-value','multiple-value'].forEach(k=>$('btb-draw-'+k).textContent=String(v));$('btb-draw-radius-mult').textContent=ratio.toFixed(2)+'×';$('btb-draw-area-mult').textContent=ar+'×';$('btb-draw-area-label').textContent='Area: '+ar+'× reference';$('btb-draw-area-note').textContent=mode==='radius'&&v>1?"The circle's area exaggerates the intended comparison.":"The circle's area correctly represents the relative value.";buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sizing===mode)));}
multiple.addEventListener('input',render);buttons.forEach(b=>b.addEventListener('click',()=>{mode=b.dataset.sizing;render();}));$('btb-draw-area-reset').addEventListener('click',()=>{multiple.value='4';mode='area';render();});render();}
})();
