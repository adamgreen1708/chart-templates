(() => {
'use strict';
const $=id=>document.getElementById(id),context=$('btb-memory-context'),library=$('btb-memory-library'),decision=$('btb-memory-decision');
if(context){
 const buttons=Array.from(context.querySelectorAll('[data-memory-context]')),views=Array.from(context.querySelectorAll('[data-memory-view]'));
 function render(mode){buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.memoryContext===mode)));views.forEach(v=>v.hidden=v.dataset.memoryView!==mode);$('btb-memory-context-status').textContent=mode==='repo'?'Consulting the project instructions.':'Starting from a simple brief.';}
 buttons.forEach(b=>b.addEventListener('click',()=>render(b.dataset.memoryContext)));$('btb-memory-context-reset').addEventListener('click',()=>render('basic'));render('basic');
}
if(library){
 const docs=[{"name":"AGENTS.md","role":"The induction document","desc":"Introduces ChatGPT to our working practices, protected files and important rules.","path":"AGENTS.md","example":"Preserve the square 8.0 x 8.0 production canvas unless explicitly changed."},{"name":"Chart template rules","role":"The design handbook","desc":"Defines our colours, typography, canvas, margins and layout standards.","path":"spec/538_template_rules.md","example":"New project configs must specify \"render_profile\": \"social_square\"."},{"name":"Editorial judgement","role":"The editorial handbook","desc":"Encourages us to investigate competing stories before choosing charts.","path":"docs/editorial_judgement_standard.md","example":"A chart must earn its space."},{"name":"Chart QA checklist","role":"The inspection checklist","desc":"Identifies the data, editorial and visual checks that should happen before approval.","path":"docs/chart_qa_checklist.md","example":"A green CI check does not equal a good story."},{"name":"Project retrospective","role":"Lessons learnt","desc":"Records what didn't work in the Pattinson project and how that experience changed our approach.","path":"docs/lessons/2026-11-19-pattinson-editorial-retrospective.md","example":"No “three charts to fill three slots”."},{"name":"Operating model","role":"Our way of working","desc":"Explains how ChatGPT should inspect the repository, prepare changes and reduce manual work.","path":"docs/chatgpt_operating_model.md","example":"Inspect relevant repo files before proposing changes."}],radios=Array.from(library.querySelectorAll('input[name="btb-memory-document"]')),link=$('btb-memory-link');
 function render(i){const d=docs[i];$('btb-memory-role').textContent=d.role.toUpperCase();$('btb-memory-document-name').textContent=d.name;$('btb-memory-desc').textContent=d.desc;$('btb-memory-extract').textContent=d.example;link.setAttribute('href','https://github.com/adamgreen1708/chart-templates/blob/main/'+d.path);}
 radios.forEach(r=>r.addEventListener('change',()=>{if(r.checked)render(Number(r.value));}));$('btb-memory-library-reset').addEventListener('click',()=>{radios.forEach(r=>r.checked=r.value==='0');render(0);});render(0);
}
if(decision){
 let saved=false;const button=$('btb-memory-capture');
 function render(){$('btb-memory-unsaved').hidden=saved;$('btb-memory-saved').hidden=!saved;button.textContent=saved?'Reset demonstration':'Capture the decision in GitHub';$('btb-memory-decision-status').textContent=saved?'Illustrative saved state: available to future projects.':'Illustrative starting state.';}
 button.addEventListener('click',()=>{saved=!saved;render();});render();
}
})();
