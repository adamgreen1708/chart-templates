(() => {
'use strict';
const $=id=>document.getElementById(id),demo=$('btb-publish-demo');if(!demo)return;
const steps=[{"name":"Create a branch","desc":"Create a separate working version of the repository.","action":"Create branch"},{"name":"Commit changes","desc":"Record the new article and supporting files.","action":"Commit article"},{"name":"Open a pull request","desc":"Propose bringing the changes into main.","action":"Open pull request"},{"name":"Run automated checks","desc":"Validate the files and build the proposed website.","action":"Run checks"},{"name":"Human approval","desc":"Review the article and approve publication.","action":"Approve changes"},{"name":"Merge","desc":"Bring the approved changes into main.","action":"Merge changes"},{"name":"Deploy","desc":"Build from main and deploy through GitHub Pages.","action":"Build and deploy"}],rows=Array.from(demo.querySelectorAll('[data-publish-step]')),action=$('btb-publish-action'),failure=$('btb-publish-failure');
let stage=0,blocked=false;
function render(){
 rows.forEach((r,i)=>{const state=i<stage?'complete':i===stage?'current':'pending';r.dataset.state=state;if(state==='current')r.setAttribute('aria-current','step');else r.removeAttribute('aria-current');r.querySelector('[data-publish-description]').hidden=state!=='current';r.querySelector('.btb-publish-step-state').textContent=state==='complete'?'Done':state==='current'?'Current':'Pending';});
 $('btb-publish-branch').style.display=stage>0?'':'none';$('btb-publish-commit').style.display=stage>=2?'':'none';$('btb-publish-merge').style.display=stage>=6?'':'none';$('btb-publish-branch-line').setAttribute('d',stage>=6?'M76 35Q92 35 100 79H222':'M76 35Q92 35 100 79H280');
 $('btb-publish-repo-status').textContent=stage===0?'Original repository':stage<6?'Changes isolated on a working branch':'Approved changes merged into main';
 $('btb-publish-failure-control').hidden=stage!==3||blocked;$('btb-publish-blocked').hidden=!blocked;action.hidden=stage===7;action.textContent=blocked?'Correct the problem':stage<7?steps[stage].action:'';
 $('btb-publish-public-title').textContent=stage===7?'New article published':'Original website';$('btb-publish-public-note').textContent=stage===7?'The simulated deployment succeeded.':'No new article visible yet.';
}
action.addEventListener('click',()=>{if(blocked){blocked=false;failure.checked=false;}else if(stage===3&&failure.checked){blocked=true;}else if(stage<7){stage++;}render();});
 $('btb-publish-reset').addEventListener('click',()=>{stage=0;blocked=false;failure.checked=false;render();});render();
})();
