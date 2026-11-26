(() => {
  'use strict';
  const root=document.getElementById('btb-bauhaus-demo');
  if(!root)return;
  const $=id=>document.getElementById(id),ns='http://www.w3.org/2000/svg';
  const rows=[{"label":"Jan","value":42},{"label":"Feb","value":58},{"label":"Mar","value":74},{"label":"Apr","value":63},{"label":"May","value":85},{"label":"Jun","value":91},{"label":"Jul","value":68},{"label":"Aug","value":82},{"label":"Sep","value":60},{"label":"Oct","value":95},{"label":"Nov","value":70},{"label":"Dec","value":65}],palettes={"bauhaus":{"bg":"#f7f0db","c":["#c7412e","#e9b725","#26599c","#191919"],"muted":"#867e71"},"ctv":{"bg":"#eff0f1","c":["#1f8fa8","#c44e52","#252d35","#e5ac32"],"muted":"#5b6770"},"night":{"bg":"#202126","c":["#eabb43","#d95144","#f7eedb","#78b8c0"],"muted":"#b6b3b0"}};
  const sorted=rows.map(r=>r.value).sort((a,b)=>a-b),min=sorted[0],max=sorted[sorted.length-1],median=(sorted[5]+sorted[6])/2;
  const ratio=(v,min,max,scale)=>scale==="contrast"?(max===min?.65:.1+.9*(v-min)/(max-min)):(max>0?v/max:0);
  const dims=(area,shape)=>shape==="circle"?Math.sqrt(area/Math.PI):shape==="square"?Math.sqrt(area):Math.sqrt(4*area/Math.sqrt(3));
  const num=v=>Number(v.toFixed(6));
  const shape=$('btb-bh-shape'),palette=$('btb-bh-palette'),labels=$('btb-bh-labels');
  const marks=root.querySelectorAll('.btb-bh-mark'),cells=root.querySelectorAll('.btb-bh-cell'),labelGroups=root.querySelectorAll('.btb-bh-label');
  function el(tag,attrs){const n=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,v));return n;}
  function render(){
    const scale=root.querySelector('input[name="btb-bh-scale"]:checked').value,colour=root.querySelector('input[name="btb-bh-colour"]:checked').value,p=palettes[palette.value],dark=palette.value==='night',ink=dark?'#f7eedb':'#333333';
    $('btb-bh-paper').style.background=p.bg;$('btb-bh-paper').style.color=ink;
    rows.forEach((r,i)=>{
      const a=.34*64*64*ratio(r.value,min,max,scale),d=dims(a,shape.value),fill=p.c[colour==='median'?(r.value>=median?0:2):i%4];
      let mark;
      if(shape.value==='circle')mark=el('circle',{cx:40,cy:38,r:num(d),fill});
      else if(shape.value==='square')mark=el('rect',{x:num(40-d/2),y:num(38-d/2),width:num(d),height:num(d),fill});
      else {const h=d*Math.sqrt(3)/2;mark=el('polygon',{points:[[40,38-h*2/3],[40+d/2,38+h/3],[40-d/2,38+h/3]].map(p=>p.map(num).join(',')).join(' '),fill});}
      marks[i].replaceChildren(mark);cells[i].setAttribute('stroke',dark?'#555555':'#b8b5aa');labelGroups[i].style.display=labels.checked?'':'none';labelGroups[i].setAttribute('fill',ink);
    });
    $('btb-bh-explanation').textContent=scale==='zero'?'Filled shape area proportional to miles.':'Min–max contrast · 10% minimum area · not zero-based.';
    const names={bauhaus:['Red','Blue'],ctv:['Teal','Charcoal'],night:['Gold','Cream']}[palette.value];
    $('btb-bh-colour-key').textContent=colour==='median'?names[0]+': at or above '+median+' miles. '+names[1]+': below '+median+' miles.':'Colours are decorative; they do not encode a value.';
    $('btb-bh-swatches').querySelectorAll('span').forEach((s,i)=>s.style.background=p.c[i]);
    root.querySelector('svg').setAttribute('aria-label','Twelve illustrative monthly running values, '+shape.value+' shapes, '+scale+' area scale, '+colour+' colour rule.');
  }
  [shape,palette,labels,...root.querySelectorAll('input[type="radio"]')].forEach(n=>n.addEventListener('change',render));
  $('btb-bh-reset').addEventListener('click',()=>{
    shape.value='circle';palette.value='bauhaus';labels.checked=true;
    root.querySelector('input[name="btb-bh-scale"][value="zero"]').checked=true;
    root.querySelector('input[name="btb-bh-colour"][value="median"]').checked=true;
    render();
  });
  render();
})();
