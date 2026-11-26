(() => {
  'use strict';
  const root=document.getElementById('btb-truchet');
  if(!root)return;
  const $=id=>document.getElementById(id);
  const slider=$('btb-chaos'), output=$('btb-chaos-output'), status=$('btb-chaos-status'), boundaries=$('btb-truchet-boundaries'), grid=$('btb-truchet-grid'), variation=$('btb-truchet-variation');
  const tiles=$('btb-truchet-tiles').querySelectorAll('polygon');
  const shapes=["0,0 1,0 0,1","1,0 1,1 0,0","1,1 0,1 1,0","0,1 0,0 1,1"];
  let seed=93;
  // The full studio's radial rule, reflection mappings and seeded noise, fixed at n=8.
  const hash=(x,y,s)=>{let h=((x+51)*374761393+(y+37)*668265263+s*1442695041)|0;h=Math.imul(h^(h>>>13),1274126177);return (h^(h>>>16))>>>0};
  const baseTile=(x,y)=>{const u=Math.min(x,7-x),v=Math.min(y,7-y),ring=Math.floor(Math.hypot(u-3.5,v-3.5));let a=(ring+Math.floor(ring/3))%4;if(x>=4)a=[1,0,3,2][a];if(y>=4)a=[3,2,1,0][a];return a};
  function orientation(x,y,chaos) {
    const p=hash(x,y,seed+701)%10000;
    const noise=p<chaos*100 ? hash(x+129,y+17,seed+1903)%4 : 0;
    return (baseTile(x,y)+noise)%4;
  }
  function render(){
    const chaos=Number(slider.value);
    tiles.forEach((tile,i)=>{
      const x=i%8,y=Math.floor(i/8);
      tile.setAttribute('points',shapes[orientation(x,y,chaos)].split(' ').map(pt=>{
        const [u,v]=pt.split(',').map(Number);return [(x+u)*32,(y+v)*32].join(',');
      }).join(' '));
    });
    output.textContent=chaos+'%';
    slider.setAttribute('aria-valuetext',chaos+'% chaos');
    status.textContent=chaos===0?'Perfect four-way reflections.':chaos===100?'Maximum independent rotation. Some tiles can still retain their original orientation.':'Independent rotations are gradually disrupting the mirrored pattern.';
    root.querySelector('svg').setAttribute('aria-label','Eight by eight Truchet pattern, '+chaos+'% chaos.');
    variation.disabled=chaos===0;
    grid.removeAttribute('hidden');
    grid.style.display=boundaries.checked?'':'none';
  }
  slider.addEventListener('input',render);
  boundaries.addEventListener('change',render);
  variation.addEventListener('click',()=>{seed++;render();});
  $('btb-truchet-reset').addEventListener('click',()=>{slider.value=0;seed=93;boundaries.checked=false;render();});
  render();
})();
