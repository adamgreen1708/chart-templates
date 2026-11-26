(() => {
 'use strict';
 const $=id=>document.getElementById(id),style=$('btb-hc-style'),template=$('btb-hc-template'),spacing=$('btb-hc-spacing'),responsive=$('btb-hc-responsive');
 if(style){
  const enabled=$('btb-hc-styled'),space=$('btb-hc-space'),size=$('btb-hc-size'),page=$('btb-hc-page'),buttons=Array.from(style.querySelectorAll('[data-hc-accent]'));let accent='#156B7F';
  function render(){const on=enabled.checked;page.classList.toggle('is-styled',on);page.style.setProperty('--hc-space',space.value+'px');page.style.setProperty('--hc-size',size.value+'px');page.style.setProperty('--hc-accent',accent);$('btb-hc-space-value').textContent=space.value+'px';$('btb-hc-size-value').textContent=size.value+'px';space.disabled=size.disabled=!on;buttons.forEach(b=>{b.disabled=!on;const selected=b.dataset.hcAccent===accent;b.setAttribute('aria-pressed',String(selected));b.textContent=selected?'✓':'';});$('btb-hc-style-code').textContent=on?'h1 { font-size: '+size.value+'px; }\nsection { padding: '+space.value+'px; gap: '+space.value+'px; }\na { color: '+accent+'; }':'Custom styling disabled.\nThe content remains.';}
  enabled.addEventListener('change',render);space.addEventListener('input',render);size.addEventListener('input',render);buttons.forEach(b=>b.addEventListener('click',()=>{accent=b.dataset.hcAccent;render();}));$('btb-hc-style-reset').addEventListener('click',()=>{enabled.checked=true;space.value='12';size.value='28';accent='#156B7F';render();});render();
 }
 if(template){
  const articles=[{"title":"Python — Making sense of the numbers","description":"What actually happens when we say Python transforms the data?"},{"title":"JavaScript — Bringing things to life","description":"What actually happens when we say JavaScript builds the interactive visualisation?"},{"title":"HTML and CSS — Giving everything a home","description":"How we turn a collection of content into a website with its own identity."}],picker=$('btb-hc-article');
  function render(){const a=articles[Number(picker.value)];$('btb-hc-meta').textContent='title: "'+a.title+'"\n\ndescription: "'+a.description+'"';$('btb-hc-preview-title').textContent=a.title;$('btb-hc-preview-description').textContent=a.description;}
  picker.addEventListener('change',render);$('btb-hc-template-reset').addEventListener('click',()=>{picker.value='0';render();});render();
 }
 if(spacing){const buttons=Array.from(spacing.querySelectorAll('[data-hc-spacing]'));function render(mode){$('btb-hc-spacing-preview').dataset.mode=mode;$('btb-hc-margin').textContent=mode==='original'?'4rem':'1.4rem';$('btb-hc-padding').textContent=mode==='original'?'8rem':'3rem';buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.hcSpacing===mode)));}buttons.forEach(b=>b.addEventListener('click',()=>render(b.dataset.hcSpacing)));render('compact');}
 if(responsive){const buttons=Array.from(responsive.querySelectorAll('[data-hc-device]'));function render(mode){$('btb-hc-device').dataset.device=mode;buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.hcDevice===mode)));}buttons.forEach(b=>b.addEventListener('click',()=>render(b.dataset.hcDevice)));render('desktop');}
})();
