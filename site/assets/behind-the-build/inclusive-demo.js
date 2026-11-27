(() => {
'use strict';
const $=id=>document.getElementById(id),contrastDemo=$('btb-inclusive-contrast'),labelsDemo=$('btb-inclusive-labels'),grid=$('btb-inclusive-grid');
// Exact source functions from site/assets/js/epl-2627-unfolded.js, isolated for teaching.
  function srgb(hex) {
    return [1,3,5].map(i => parseInt(hex.slice(i,i+2),16)/255).map(c => c<=.04045 ? c/12.92 : Math.pow((c+.055)/1.055,2.4));
  }
  function luminance(hex) {
    const [r,g,b]=srgb(hex);
    return .2126*r+.7152*g+.0722*b;
  }
  function contrast(a,b) {
    const l1=luminance(a), l2=luminance(b);
    return (Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
  }
  function textOn(hex) { return contrast('#FFFFFF',hex)>=contrast('#202326',hex) ? '#FFFFFF' : '#202326'; }
  function lightenForTitle(hex) {
    const bg='#303133';
    if(contrast(hex,bg)>=4.5)return hex;
    const rgb=[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16));
    for(let amount=1;amount<=100;amount++){
      const blend='#'+rgb.map(v=>Math.round(v+(255-v)*amount/100).toString(16).padStart(2,'0')).join('');
      if(contrast(blend,bg)>=4.5)return blend;
    }
    return '#FFFFFF';
  }

if(contrastDemo){
 const clubs=[{"name":"Chelsea","hex":"#034694"},{"name":"West Ham","hex":"#7A263A"},{"name":"Newcastle","hex":"#111111"},{"name":"Arsenal","hex":"#EF0107"},{"name":"Man City","hex":"#6CABDD"},{"name":"Wolves","hex":"#FDB913"}],picker=$('btb-inclusive-club'),adjust=$('btb-inclusive-adjust'),dots=Array.from(contrastDemo.querySelectorAll('[data-inclusive-club-dot]'));
 function render(){const c=clubs[Number(picker.value)],ink=adjust.checked?lightenForTitle(c.hex):c.hex,r=contrast(ink,'#303133'),heading=$('btb-inclusive-heading');heading.textContent=c.name.toUpperCase();heading.style.color=ink;dots.forEach(d=>d.style.backgroundColor=c.hex);$('btb-inclusive-ratio').textContent=r.toFixed(2)+':1';$('btb-inclusive-verdict').textContent=r>=4.5?'Meets our heading contrast target.':'Below our heading contrast target.';$('btb-inclusive-colour-values').textContent='Original colour: '+c.hex.toUpperCase()+' · Heading colour: '+ink.toUpperCase();}
 picker.addEventListener('change',render);adjust.addEventListener('change',render);$('btb-inclusive-contrast-reset').addEventListener('click',()=>{picker.value='0';adjust.checked=false;render();});render();
}
if(labelsDemo){
 const colours={"W":"#EF0107","D":"#D9D9D9","L":"#777777"},greys={"W":"#939393","D":"#AAAAAA","L":"#777777"},labels=$('btb-inclusive-show-labels'),mono=$('btb-inclusive-mono'),dots=Array.from(labelsDemo.querySelectorAll('[data-inclusive-result]')),texts=Array.from(labelsDemo.querySelectorAll('[data-inclusive-result-label]'));
 function render(){dots.forEach(d=>d.setAttribute('fill',(mono.checked?greys:colours)[d.dataset.inclusiveResult]));texts.forEach(t=>{const bg=(mono.checked?greys:colours)[t.dataset.inclusiveResult];t.style.display=labels.checked?'':'none';t.setAttribute('fill',textOn(bg));});$('btb-inclusive-label-status').textContent=labels.checked?'The letters provide another way to distinguish results without relying entirely on colour.':'The reader must distinguish results using colour alone.';}
 labels.addEventListener('change',render);mono.addEventListener('change',render);$('btb-inclusive-label-reset').addEventListener('click',()=>{labels.checked=false;mono.checked=false;render();});render();
}
if(grid){
 const pixels=["#FFFFFF","#1F8FA8","#FFFFFF","#1F8FA8","#C44E52","#1F8FA8","#FFFFFF","#1F8FA8","#FFFFFF"],cells=Array.from(grid.querySelectorAll('[data-inclusive-pixel]')),dirs=Array.from(grid.querySelectorAll('[data-inclusive-dir]')),board=$('btb-inclusive-board'),size=3;let index=4;
 function render(next,focus=false){index=next;cells.forEach((c,i)=>{c.tabIndex=i===index?0:-1;c.setAttribute('aria-pressed',String(i===index));c.querySelector('span').textContent=i===index?'＋':'';});$('btb-inclusive-pixel-label').textContent='Row '+(Math.floor(index/size)+1)+', column '+((index%size)+1)+': '+(index===4?'Red':pixels[index]==='#FFFFFF'?'White':'Blue');if(focus)cells[index].focus();}
 function move(key,focus){let next=index;if(key==='ArrowRight')next=Math.min(size*size-1,index+1);else if(key==='ArrowLeft')next=Math.max(0,index-1);else if(key==='ArrowDown')next=Math.min(size*size-1,index+size);else if(key==='ArrowUp')next=Math.max(0,index-size);else if(key==='Home')next=index-index%size;else if(key==='End')next=index+size-1-index%size;else return false;render(next,focus);return true;}
 cells.forEach(c=>{c.addEventListener('click',()=>render(Number(c.dataset.inclusivePixel)));c.addEventListener('focus',()=>{const next=Number(c.dataset.inclusivePixel);if(next!==index)render(next);});});board.addEventListener('keydown',e=>{if(move(e.key,true))e.preventDefault();});dirs.forEach(d=>d.addEventListener('click',()=>move(d.dataset.inclusiveDir,false)));$('btb-inclusive-grid-reset').addEventListener('click',()=>render(4));render(4);
}
})();
