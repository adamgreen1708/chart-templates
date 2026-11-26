(() => {
 'use strict';
 const $=id=>document.getElementById(id),paint=$('btb-js-paint'),shape=$('btb-js-shape');
 if(paint){
  const palette=[{"id":0,"name":"White","hex":"#ffffff"},{"id":1,"name":"Black","hex":"#111111"},{"id":2,"name":"Blue","hex":"#096ba6"},{"id":3,"name":"Green","hex":"#06ad23"},{"id":5,"name":"Yellow","hex":"#e8c94f"},{"id":6,"name":"Red","hex":"#c34635"}],inks=Array.from(paint.querySelectorAll('[data-ink]')),cells=Array.from(paint.querySelectorAll('[data-pixel]')),values=Array.from(paint.querySelectorAll('[data-value]'));
  const ink=n=>palette.find(p=>p.id===n);
  let pixels=Array(9).fill(0),active=2,last=null,count=0;
  function render(){
   inks.forEach(b=>{const selected=Number(b.dataset.ink)===active;b.setAttribute('aria-pressed',String(selected));b.textContent=selected?'✓':'';});
   $('btb-js-selected').textContent='Selected: '+ink(active).name+' · Value '+active;
   cells.forEach((b,i)=>{b.style.backgroundColor=ink(pixels[i]).hex;b.setAttribute('aria-label','Square '+i+', '+ink(pixels[i]).name);values[i].textContent=String(pixels[i]);values[i].classList.toggle('btb-js-changed',!!last&&last.i===i);});
   $('btb-js-count').textContent=count+' paint action'+(count===1?'':'s');
   $('btb-js-event').textContent=last?'Square '+last.i+' was selected.':'Waiting for you to select a square.';
   $('btb-js-state').textContent=last?'Colour value: '+last.old+' → '+last.next:'All nine squares initially contain zero.';
   $('btb-js-assignment').textContent=last?'pixels['+last.i+'] = '+last.next:'';
   $('btb-js-render').textContent=last?'Display '+ink(last.next).name.toLowerCase()+' using its stored colour code '+ink(last.next).hex+'.':'Display the current colour of each square.';
  }
  inks.forEach(b=>b.addEventListener('click',()=>{active=Number(b.dataset.ink);render();}));
  cells.forEach((b,i)=>b.addEventListener('click',()=>{const old=pixels[i],next=active!==0&&old===active?0:active;pixels[i]=next;last={i,old,next};count++;render();}));
  $('btb-js-reset').addEventListener('click',()=>{pixels=Array(9).fill(0);active=2;last=null;count=0;render();});render();
 }
 if(shape){
  const radius=$('btb-js-radius'),position=$('btb-js-position'),circle=$('btb-js-circle'),centre=$('btb-js-centre'),swatches=Array.from(shape.querySelectorAll('[data-shape-ink]'));let colour='#1F8FA8';
  function draw(){const r=Number(radius.value),x=Number(position.value);circle.setAttribute('r',r);circle.setAttribute('cx',x);circle.setAttribute('fill',colour);centre.setAttribute('cx',x);$('btb-js-radius-value').textContent=String(r);$('btb-js-position-value').textContent=String(x);$('btb-js-instructions').textContent='x = '+x+'\ny = 90\nradius = '+r+'\ncolour = "'+colour+'"';swatches.forEach(b=>{const on=b.dataset.shapeInk===colour;b.setAttribute('aria-pressed',String(on));b.textContent=on?'✓':'';});}
  radius.addEventListener('input',draw);position.addEventListener('input',draw);swatches.forEach(b=>b.addEventListener('click',()=>{colour=b.dataset.shapeInk;draw();}));$('btb-js-shape-reset').addEventListener('click',()=>{radius.value='35';position.value='160';colour='#1F8FA8';draw();});draw();
 }
})();
