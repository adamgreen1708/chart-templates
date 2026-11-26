(() => {
  'use strict';
  const root=document.getElementById('btb-dot-demo');
  if(!root)return;
  const $=id=>document.getElementById(id);
  const density=$('btb-dot-density'), diameter=$('btb-dot-diameter'), marks=$('btb-dot-marks');
  const sample=(x,y)=>{if(y>.79+.045*Math.sin(x*12))return [35,62,73];if(y>.63+.08*Math.sin(x*9))return [74,108,106];if(y>.28+Math.abs(x-.35)*1.15)return [113,137,145];if(Math.hypot(x-.77,y-.21)<.13)return [232,201,79];return [188,209,218]};
  const lum=c=>(.2126*c[0]+.7152*c[1]+.0722*c[2])/255;
  const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));
  const dotDiameter=(c,d,s)=>clamp(d/100*(s==="uniform"?1:1+.8*((.28+1.25*(s==="dark"?1-lum(c):lum(c)))-1)),.06,1.4);
  const num=x=>Number(x.toFixed(4));
  const shade=c=>Math.round(Math.round(lum(c)*7)*255/7);
  function render(){
    const n=Number(density.value), d=Number(diameter.value);
    const sizing=root.querySelector('input[name="btb-dot-sizing"]:checked').value;
    const treatment=root.querySelector('input[name="btb-dot-treatment"]:checked').value;
    const fragment=document.createDocumentFragment();
    for(let i=0;i<n*n;i++){
      const x=(i%n+.5)/n,y=(Math.floor(i/n)+.5)/n,c=sample(x,y),s=shade(c);
      const dot=document.createElementNS('http://www.w3.org/2000/svg','circle');
      dot.setAttribute('cx',num(x*160));dot.setAttribute('cy',num(y*160));
      dot.setAttribute('r',num(dotDiameter(c,d,sizing)*80/n));
      dot.setAttribute('fill','rgb('+(treatment==='grey'?[s,s,s]:c).join(',')+')');
      fragment.append(dot);
    }
    marks.replaceChildren(fragment);
    $('btb-dot-count').textContent=(n*n).toLocaleString('en-GB');
    $('btb-dot-grid-label').textContent=n+' × '+n+' grid';
    $('btb-dot-diameter-output').textContent=d+'%';
    diameter.setAttribute('aria-valuetext',d+'% of grid spacing');
    $('btb-dot-art').setAttribute('aria-label','Landscape represented by '+n*n+' dots, '+treatment+' treatment, '+sizing+' size rule.');
  }
  density.addEventListener('change',render);
  diameter.addEventListener('input',render);
  root.querySelectorAll('input[type="radio"]').forEach(el=>el.addEventListener('change',render));
  $('btb-dot-reset').addEventListener('click',()=>{
    density.value='20';diameter.value='90';
    root.querySelector('input[name="btb-dot-sizing"][value="uniform"]').checked=true;
    root.querySelector('input[name="btb-dot-treatment"][value="colour"]').checked=true;
    render();
  });
  render();
})();
