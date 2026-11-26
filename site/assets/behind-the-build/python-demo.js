(() => {
 'use strict';
 const $=id=>document.getElementById(id),root=$('btb-py-transform'),validation=$('btb-py-validation');if(!root||!validation)return;
 const fixtures=[{"date":"2025-08-23","home":"Arsenal","away":"Leeds","hg":5,"ag":0,"r":"H"},{"date":"2025-08-17","home":"Man United","away":"Arsenal","hg":0,"ag":1,"r":"A"},{"date":"2025-08-17","home":"Chelsea","away":"Crystal Palace","hg":0,"ag":0,"r":"D"}],description=['Read the original fixture from the CSV file. At this stage, one row represents one match.','Check the score against the recorded result. Make sure the goals are valid numbers.','Create two records, reversing goals for and against for the away club.','Determine whether each club won, drew or lost, and award the appropriate points.','Prepare the transformed records for structured storage and use by the website.'];
 const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
 const table=(headers,rows)=>'<table class="btb-py-table"><thead><tr>'+headers.map(h=>'<th scope="col">'+esc(h)+'</th>').join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+r.map(v=>'<td>'+esc(v)+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
 const code=(label,value)=>'<div class="btb-py-code"><p>'+esc(label)+'</p><pre><code>'+esc(value)+'</code></pre></div>';
 const note=t=>'<p class="btb-meta">'+esc(t)+'</p>';
 const result=(gf,ga)=>gf>ga?'W':gf===ga?'D':'L';
 const earned=r=>r==='W'?3:r==='D'?1:0;
 const records=f=>[{club:f.home,venue:'H',gf:f.hg,ga:f.ag},{club:f.away,venue:'A',gf:f.ag,ga:f.hg}].map(r=>({...r,result:result(r.gf,r.ga),points_earned:earned(result(r.gf,r.ga))}));
 const complete=f=>Number.isInteger(f.hg)&&Number.isInteger(f.ag)&&f.hg>=0&&f.ag>=0;
 const agrees=f=>complete(f)&&f.r===(f.hg>f.ag?'H':f.hg===f.ag?'D':'A');
 let step=0;
 const picker=$('btb-py-fixture'),buttons=Array.from(root.querySelectorAll('[data-step]'));
 function render(){
  const f=fixtures[Number(picker.value)],rs=records(f);
  $('btb-py-step').textContent='INSTRUCTION '+(step+1)+' OF 5';$('btb-py-description').textContent=description[step];
  buttons.forEach((b,i)=>b.setAttribute('aria-pressed',String(i===step)));
  let html='';
  if(step===0)html=code('ORIGINAL CSV ROW','Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR\n'+[f.date,f.home,f.away,f.hg,f.ag,f.r].join(','))+note('FTHG and FTAG are full-time home and away goals. FTR is the recorded full-time result.');
  if(step===1)html='<div class="btb-py-check-list"><p>✓ Home and away goals are non-negative integers</p><p>✓ Recorded result agrees with the score</p></div>'+note('Two of the actual checks performed by the archived Python script.');
  if(step===2)html=table(['Club','Venue','GF','GA'],rs.map(r=>[r.club,r.venue==='H'?'Home':'Away',r.gf,r.ga]))+note('GF = goals for. GA = goals against.');
  if(step===3)html=table(['Club','Result','Points'],rs.map(r=>[r.club,{W:'Win',D:'Draw',L:'Loss'}[r.result],r.points_earned]))+note('Points earned from this fixture alone.');
  if(step===4)html=code('SIMPLIFIED JSON EXTRACT',JSON.stringify(rs.map(r=>({club:r.club,venue:r.venue,result:r.result,points_earned:r.points_earned})),null,2))+note('The production file groups matches by club and also stores dates, opponents, goals, match numbers, cumulative points and season totals. points_earned is an illustrative field, not the production cumulative points field.');
  $('btb-py-content').innerHTML=html;$('btb-py-prev').disabled=step===0;$('btb-py-next').textContent=step===4?'Start again':'Next instruction';
 }
 buttons.forEach((b,i)=>b.addEventListener('click',()=>{step=i;render()}));
 picker.addEventListener('change',()=>{step=0;render()});
 $('btb-py-prev').addEventListener('click',()=>{step=Math.max(0,step-1);render()});
 $('btb-py-next').addEventListener('click',()=>{step=(step+1)%5;render()});
 const radios=Array.from(validation.querySelectorAll('input[type="radio"]'));
 function scenario(){const mode=radios.find(r=>r.checked).value,f={...fixtures[0]};if(mode==='missing')f.ag=null;if(mode==='wrong')f.r='A';return mode==='duplicate'?[f,{...f}]:[f];}
 function input(){const rows=scenario();$('btb-py-input').innerHTML=table(['Home','Away','HG','AG','FTR'],rows.map(f=>[f.home,f.away,f.hg,f.ag===null?'—':f.ag,f.r]));$('btb-py-checks').innerHTML='';}
 function check(){
  const rows=scenario(),unique=new Set(rows.map(f=>JSON.stringify([f.home,f.away]))).size===rows.length,valid=rows.every(complete),consistent=rows.every(agrees),pass=unique&&valid&&consistent;
  const checks=[['Unique fixture',unique],['Complete score',valid],['Score agrees with result',consistent]];
  const message=pass?'These example checks passed.':!unique?'Counting the same fixture twice would distort the totals.':!valid?'A missing score must never be interpreted as zero.':'A 5–0 home victory cannot be recorded as an away win.';
  $('btb-py-checks').innerHTML='<div class="btb-py-check-list">'+checks.map(([name,ok])=>'<p class="'+(ok?'btb-py-pass':'btb-py-fail')+'">'+esc(name)+' — '+(ok?'Pass':'Fail')+'</p>').join('')+'<p><strong>'+(pass?'Eligible for further processing.':'Validation failed — stop processing.')+'</strong></p><p>'+esc(message)+'</p></div>';
 }
 radios.forEach(r=>r.addEventListener('change',input));$('btb-py-run').addEventListener('click',check);$('btb-py-reset').addEventListener('click',()=>{radios[0].checked=true;input()});render();input();
})();
