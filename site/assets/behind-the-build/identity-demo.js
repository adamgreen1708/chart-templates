(() => {
'use strict';
const $=id=>document.getElementById(id),colour=$('btb-identity-colour'),type=$('btb-identity-type');
if(colour){
 const buttons=Array.from(colour.querySelectorAll('[data-identity-mode]')),dots=Array.from(colour.querySelectorAll('[data-identity-dot]')),target=$('btb-identity-target'),control=$('btb-identity-target-control');
 const colourful=['#C44E52','#1F8FA8','#579568','#E0AD43','#9068A6','#D78652'];let mode='focus';
 const notes={uniform:'Everything has equal visual importance.',colourful:'Lots of colour creates variety, but nothing has a particularly clear priority.',focus:'A single accent directs attention whilst the surrounding marks provide context.'};
 function render(){const t=Number(target.value);dots.forEach((d,i)=>d.setAttribute('fill',mode==='uniform'?'#7A7A7A':mode==='colourful'?colourful[(i*7+Math.floor(i/8))%6]:i===t?'#C44E52':'#D9D9D9'));buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.identityMode===mode)));control.hidden=mode!=='focus';$('btb-identity-position').textContent=(t+1)+' of 48';target.setAttribute('aria-valuetext','Dot '+(t+1)+' of 48');$('btb-identity-colour-note').textContent=notes[mode];}
 buttons.forEach(b=>b.addEventListener('click',()=>{mode=b.dataset.identityMode;render();}));target.addEventListener('input',render);$('btb-identity-colour-reset').addEventListener('click',()=>{mode='focus';target.value='14';render();});render();
}
if(type){
 const profiles={legacy:[22,12,10,10],current:[26,16,12,10.5]},profileButtons=Array.from(type.querySelectorAll('[data-identity-profile]')),screenButtons=Array.from(type.querySelectorAll('[data-identity-screen]')),fonts=Array.from(type.querySelectorAll('[data-identity-font]'));let profile='current',screen='320';
 function render(){fonts.forEach(f=>f.setAttribute('font-size',String(profiles[profile][Number(f.dataset.identityFont)])));$('btb-identity-screen').style.width=screen+'px';profileButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.identityProfile===profile)));screenButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.identityScreen===screen)));$('btb-identity-screen-note').textContent=(profile==='current'?'Current':'Legacy')+' profile · target width '+screen+'px. The preview scales down further if the available screen is narrower.';}
 profileButtons.forEach(b=>b.addEventListener('click',()=>{profile=b.dataset.identityProfile;render();}));screenButtons.forEach(b=>b.addEventListener('click',()=>{screen=b.dataset.identityScreen;render();}));$('btb-identity-type-reset').addEventListener('click',()=>{profile='current';screen='320';render();});render();
}
})();
