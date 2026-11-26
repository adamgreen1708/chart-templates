(() => {
 'use strict';
 const $=id=>document.getElementById(id),root=$('btb-iw-demo');if(!root)return;
 const fixtures=[{"home":"Arsenal","away":"Leeds","date":"23 August 2025","hg":5,"ag":0,"label":"Arsenal 5–0 Leeds"},{"home":"Arsenal","away":"Man City","date":"21 September 2025","hg":1,"ag":1,"label":"Arsenal 1–1 Man City"},{"home":"Man United","away":"Arsenal","date":"17 August 2025","hg":0,"ag":1,"label":"Man United 0–1 Arsenal"},{"home":"Chelsea","away":"Crystal Palace","date":"17 August 2025","hg":0,"ag":0,"label":"Chelsea 0–0 Crystal Palace"}],ns='http://www.w3.org/2000/svg';
 const picker=$('btb-iw-fixture'),labels=$('btb-iw-labels'),finish=$('btb-iw-finish');
 const radius=g=>9.6*Math.sqrt(1+1.25*g),brightness=(g,a)=>48+8*Math.min(g+a,7);
 function circle(attrs){let c=document.createElementNS(ns,'circle');Object.entries(attrs).forEach(([k,v])=>c.setAttribute(k,v));return c;}
 function render(){
  const f=fixtures[Number(picker.value)],total=f.hg+f.ag,draw=f.hg===f.ag,b=brightness(f.hg,f.ag),link=$('btb-iw-link');
  const text={date:f.date,score:f.label,home:f.home,away:f.away,hg:f.hg+' goals',ag:f.ag+' goals',hr:f.hg>f.ag?'Winner halo':draw?'Draw':'No halo',ar:f.ag>f.hg?'Winner halo':draw?'Draw':'No halo',total:String(total),kind:draw?'Dashed':'Solid'};
  Object.entries(text).forEach(([k,v])=>$('btb-iw-'+k).textContent=v);
  link.setAttribute('stroke','rgb('+b+','+b+','+b+')');link.setAttribute('stroke-width',total>=5?3:2);
  if(draw)link.setAttribute('stroke-dasharray','8 6');else link.removeAttribute('stroke-dasharray');
  const nodes=[];
  [[f.hg,f.ag,62],[f.ag,f.hg,186]].forEach(([g,a,y])=>{
   if(g>a){nodes.push(circle({cx:160,cy:y,r:40,fill:'url(#btb-iw-glow)'}),circle({cx:160,cy:y,r:32,fill:'none',stroke:'#e7e7e7','stroke-width':1.5}));}
   nodes.push(circle({cx:160,cy:y,r:radius(g).toFixed(6),fill:finish.checked?'url(#btb-iw-glass)':'#c8c8c8',stroke:a===0?'#fff':'#888'}));
  });
  $('btb-iw-beads').replaceChildren(...nodes);
  $('btb-iw-annotations').style.display=labels.checked?'':'none';
  $('btb-iw-svg').setAttribute('aria-label',f.label+'; '+(draw?'dashed draw connection, no winner halo':(f.hg>f.ag?f.home:f.away)+' winner halo')+'; sphere area increases with goals.');
 }
 [picker,labels,finish].forEach(n=>n.addEventListener('change',render));
 $('btb-iw-reset').addEventListener('click',()=>{picker.value='0';labels.checked=true;finish.checked=true;render();});
 render();
})();
