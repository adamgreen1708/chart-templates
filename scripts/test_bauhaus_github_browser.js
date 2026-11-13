'use strict';
// Run: node scripts/test_bauhaus_github_browser.js
// Exercise the *production* GitHub CSV browser functions against a simulated DOM and GitHub API.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const source=fs.readFileSync(path.resolve(__dirname,'../site/resources/bauhaus-art-studio/index.html'),'utf8');
const inline=source.match(/<script>([\s\S]*?)<\/script>/);
assert.ok(inline,'Production Bauhaus script missing');
new Function(inline[1]);
function section(a,b){
 const i=inline[1].indexOf(a),j=inline[1].indexOf(b,i);
 assert.ok(i>=0&&j>i,'Production function not found: '+a);
 return inline[1].slice(i,j);
}
const selectors=['github-owner','github-repo','github-preset','github-filter','github-load','github-refresh','github-browser-info'];
const elements={};
for(const id of selectors){
 const el={
  value:'',disabled:false,textContent:'',options:[],events:{},
  addEventListener(event,fn){this.events[event]=fn;},
  trigger(event){assert.ok(this.events[event],'Missing handler: '+id+' '+event);return this.events[event].call(this);},
  set innerHTML(_){this.options=[];this.value='';},get innerHTML(){return '';}
 };
 elements[id]=el;
}
elements['github-owner'].value='adamgreen1708';
const $=id=>{assert.ok(elements[id],'Missing element '+id);return elements[id];};
const makeOption=(sel,value,label)=>{
 sel.options.push({value:String(value),textContent:String(label)});
 if(sel.options.length===1)sel.value=String(value);
};
const repo=(name,owner='adamgreen1708')=>({
 name,full_name:owner+'/'+name,private:false,default_branch:'main',owner:{login:owner}
});
const csvPaths=[
 {type:'blob',path:'data/site_analytics_daily.csv'},
 {type:'blob',path:'archive/projects/2026-09-david-bowie-track-distributions/data/bowie_track_distribution_rows.csv'},
 {type:'blob',path:'archive/projects/marathons/data/major winners.csv'},
 {type:'blob',path:'data/élite-runners.csv'},
 {type:'blob',path:'notes/readme.md'},
 {type:'tree',path:'not-a-csv.csv'}
];
let failing=false,truncated=false,requests=[];
const fetch=async url=>{
 requests.push(url);
 if(failing) return {ok:false,status:403};
 if(url.includes('/users/shortsinsports/'))return {ok:true,status:200,json:async()=>[repo('Data','shortsinsports')]};
 if(url.includes('/users/'))return {ok:true,status:200,json:async()=>[repo('chart-templates'),repo('chatgpt-github-test')]};
 if(url.includes('/repos/adamgreen1708/chart-templates/git/trees/main'))return {ok:true,status:200,json:async()=>({tree:csvPaths,truncated})};
 if(url.includes('/repos/adamgreen1708/chatgpt-github-test/git/trees/main'))return {ok:true,status:200,json:async()=>({tree:[{type:'blob',path:'fixtures/sample.csv'}],truncated:false})};
 if(url.includes('/repos/shortsinsports/Data/git/trees/main'))return {ok:true,status:200,json:async()=>({tree:[{type:'blob',path:'SIS-marathon_major_winners_2000_2026.csv'}],truncated:false})};
 throw Error('Unexpected request '+url);
};
const code=section('function githubDatasetPaths(tree)','async function readGithub(url)');
const api=new Function('$','makeOption','fetch','AbortController','setTimeout','clearTimeout',
 'var githubBrowserStarted=false,githubRepos=[],githubCsvPaths=[],githubTreeLoadId=0,githubRepoLoadId=0;\n'+
 code+'\nreturn {githubDatasetPaths,renderGithubDatasetOptions,loadGithubRepositoryFiles,loadGithubRepositories};'
)($,makeOption,fetch,AbortController,setTimeout,clearTimeout);
async function run(){
 assert.equal(api.githubDatasetPaths({tree:csvPaths,truncated:false}).length,4);
 assert.throws(()=>api.githubDatasetPaths({tree:csvPaths,truncated:true}),/too large/);
 await api.loadGithubRepositories(false);
 assert.equal(elements['github-repo'].options.length,2,'All public account repositories should appear');
 assert.equal(elements['github-repo'].value,'adamgreen1708/chart-templates');
 assert.equal(elements['github-preset'].options.length,5,'All four CSV paths plus placeholder should appear');
 assert.ok(elements['github-preset'].options.some(o=>o.value==='data/élite-runners.csv'));
 assert.equal(elements['github-load'].disabled,true);
 elements['github-filter'].value='marathon';
 elements['github-filter'].trigger('input');
 assert.equal(elements['github-preset'].options.length,2,'Search should filter the displayed list');
 assert.equal(elements['github-preset'].options[1].value,'archive/projects/marathons/data/major winners.csv');
 elements['github-preset'].value='archive/projects/marathons/data/major winners.csv';
 elements['github-preset'].trigger('change');
 assert.equal(elements['github-load'].disabled,false);
 elements['github-repo'].value='adamgreen1708/chatgpt-github-test';
 await elements['github-repo'].trigger('change');
 assert.equal(elements['github-preset'].options[1].value,'fixtures/sample.csv');
 assert.equal(elements['github-load'].disabled,true,'Switching repo clears previous selected file');
 await elements['github-refresh'].trigger('click');
 assert.equal(elements['github-repo'].value,'adamgreen1708/chatgpt-github-test','Refresh should retain selection');
 elements['github-owner'].value='shortsinsports';
 await elements['github-owner'].trigger('change');
 assert.equal(elements['github-repo'].value,'shortsinsports/Data','Alternate public account should be browsable');
 assert.equal(elements['github-preset'].options[1].value,'SIS-marathon_major_winners_2000_2026.csv');
 elements['github-owner'].value='adamgreen1708';
 await elements['github-owner'].trigger('change');
 truncated=true;
 elements['github-repo'].value='adamgreen1708/chart-templates';
 await elements['github-repo'].trigger('change');
 assert.match(elements['github-browser-info'].textContent,/too large/);
 assert.equal(elements['github-load'].disabled,true);
 failing=true;
 await elements['github-refresh'].trigger('click');
 assert.match(elements['github-browser-info'].textContent,/rate limit/);
 assert.ok(requests.some(x=>x.includes('/git/trees/')));
 console.log('Bauhaus live public GitHub CSV browser regression checks passed.');
}
run().catch(err=>{console.error(err);process.exitCode=1;});
