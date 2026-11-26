(() => {
'use strict';
const $=id=>document.getElementById(id),routes=$('btb-story-routes'),counting=$('btb-story-counting');
if(routes){
 const choices=[{"name":"Career periods","question":"Did his films become better over time?","method":"Group films into broad career periods and compare average ratings.","strength":"Provides a simple summary of film ratings.","weakness":"Arbitrary time periods conceal individual films. Ratings do not directly measure career reinvention.","decision":"Reconsider"},{"name":"Franchise comparison","question":"How does Twilight compare with his other films?","method":"Compare the five Twilight titles with the other 28 rated films.","strength":"Reveals an interesting contrast between voting activity and film ratings.","weakness":"The sample is curated, and group averages can conceal variation between films.","decision":"Explore further"},{"name":"Cast connections","question":"Had Pattinson already worked with people from the Bond films?","method":"Investigate shared performers and verify their individual roles.","strength":"Reveals specific, memorable human connections.","weakness":"The verified examples are not exhaustive and cannot establish why he was cast.","decision":"Strong editorial potential"}],radios=Array.from(routes.querySelectorAll('input[name="btb-story-route"]')),panel=$('btb-story-review-panel');let selected=0;
 function render(){const a=choices[selected];$('btb-story-question').textContent=a.question;$('btb-story-method').textContent=a.method;panel.hidden=true;}
 radios.forEach(r=>r.addEventListener('change',()=>{if(r.checked){selected=Number(r.value);render();}}));
 $('btb-story-review').addEventListener('click',()=>{const a=choices[selected];$('btb-story-strength').textContent=a.strength;$('btb-story-weakness').textContent=a.weakness;$('btb-story-decision').textContent=a.decision;panel.hidden=false;});
 $('btb-story-reset').addEventListener('click',()=>{selected=0;radios.forEach(r=>r.checked=r.value==='0');render();});render();
}
if(counting){
 const buttons=Array.from(counting.querySelectorAll('[data-story-grain]'));
 function render(mode){const people=mode==='people';$('btb-story-count').textContent=people?'6':'14';$('btb-story-count-label').textContent=people?'Verified distinct performers':'Film-pair connections';$('btb-story-count-note').textContent=people?'Count people once, then identify their actual roles.':'A performer can appear in more than one film relationship. Counting those relationships does not tell us how many individual people are involved.';$('btb-story-people').hidden=!people;buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.storyGrain===mode)));}
 buttons.forEach(b=>b.addEventListener('click',()=>render(b.dataset.storyGrain)));render('pairs');
}
})();
