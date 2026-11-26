(() => {
  'use strict';
  const root = document.getElementById('btb-pixel');
  if (!root) return;
  const palette = ["#ffffff","#111111","#096ba6","#06ad23","#7b898f","#e8c94f","#c34635","#fb8e31","#ee3edc","#8b5a3c","#e8cf9a","#87c9eb","#296647","#6f42c1","#d4a017","#b8bdc3"];
  const names = ["White","Black","Blue","Green","Slate","Yellow","Red","Orange","Pink","Brown","Sand","Sky blue","Forest green","Purple","Gold","Silver"];
  const original = root.dataset.initial;
  if (!/^[0-9a-f]{64}$/.test(original)) return;
  let pixels = [...original].map(v => parseInt(v, 16)), ink = 2;
  const paint = root.querySelector('.btb-pixel-grid'), values = root.querySelector('.btb-value-grid'), swatches = root.querySelector('.btb-palette');
  const cells = [], numbers = [], colours = [];
  const status = root.querySelector('.btb-status');
  const select = i => { ink = i; colours.forEach((b,j) => b.setAttribute('aria-pressed', String(i === j))); };
  palette.forEach((colour,i) => {
    const b = document.createElement('button'); b.type = 'button'; b.style.backgroundColor = colour; b.title = names[i] + ' (' + i.toString(16) + ')'; b.setAttribute('aria-label',b.title); b.addEventListener('click',() => select(i)); swatches.append(b); colours.push(b);
  });
  for(let i=0;i<64;i++) {
    const b = document.createElement('button'); b.type='button'; b.addEventListener('click',() => { pixels[i]=ink; render(); status.textContent='Row '+(Math.floor(i/8)+1)+', column '+(i%8+1)+': '+names[ink]+' ('+ink.toString(16)+')'; });
    b.addEventListener('keydown',e => { const delta={ArrowLeft:-1,ArrowRight:1,ArrowUp:-8,ArrowDown:8}[e.key]; if(delta===undefined)return; e.preventDefault(); const j=i+delta; if(j>=0&&j<64)cells[j].focus(); });
    paint.append(b); cells.push(b);
    const v=document.createElement('span'); values.append(v); numbers.push(v);
  }
  function render(){
    pixels.forEach((v,i)=>{ cells[i].style.backgroundColor=palette[v]; cells[i].setAttribute('aria-label','Row '+(Math.floor(i/8)+1)+', column '+(i%8+1)+': '+names[v]); numbers[i].textContent=v.toString(16); });
    const code=pixels.map(v=>v.toString(16)).join('');
    root.querySelector('.btb-encoded').textContent=code.match(/.{8}/g).join('\n');
    root.querySelector('.btb-open').href=root.dataset.studio+'#art='+code;
  }
  root.querySelector('.btb-reset').addEventListener('click',()=>{pixels=[...original].map(v=>parseInt(v,16));render();status.textContent='Original frog restored.';});
  select(ink);render();
})();
