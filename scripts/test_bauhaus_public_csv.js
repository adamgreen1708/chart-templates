'use strict';
// Run: node scripts/test_bauhaus_public_csv.js
// Verifies the production page's URL parser, duration logic and default mapping.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const page=fs.readFileSync(path.resolve(__dirname,'../site/resources/bauhaus-art-studio/index.html'),'utf8');
const script=page.match(/<script>([\s\S]*?)<\/script>/);
assert.ok(script,'Bauhaus page must contain an inline script');
new Function(script[1]); // Compile whole production JavaScript, without executing the DOM setup.
function section(start,end){
 const a=script[1].indexOf(start),b=script[1].indexOf(end,a);
 assert.ok(a>=0&&b>a,'Cannot locate '+start);
 return script[1].slice(a,b);
}
const repoCsvUrl=new Function(section('function repoCsvUrl(input)','async function readGithub(url)')+'return repoCsvUrl;')();
const pinned='4ea0ca9e403d706a734d41088ad63e571ab0ca21';
const csv='SIS-marathon_major_winners_2000_2026.csv';
const urls=[
 ['https://github.com/shortsinsports/Data/blob/main/'+csv,'https://raw.githubusercontent.com/shortsinsports/Data/main/'+csv],
 ['https://github.com/shortsinsports/Data/blob/'+pinned+'/'+csv,'https://raw.githubusercontent.com/shortsinsports/Data/'+pinned+'/'+csv],
 ['https://raw.githubusercontent.com/shortsinsports/Data/main/'+csv,'https://raw.githubusercontent.com/shortsinsports/Data/main/'+csv],
 ['https://github.com/adamgreen1708/chart-templates/blob/main/data/site_analytics_daily.csv','https://raw.githubusercontent.com/adamgreen1708/chart-templates/main/data/site_analytics_daily.csv]
];
urls.forEach(([input,expected])=>assert.equal(repoCsvUrl(input).url,expected));
[
 'http://github.com/shortsinsports/Data/blob/main/'+csv,
 'https://bad.example.com/shortsinsports/Data/main/'+csv,
 'https://github.com/shortsinsports/Data',
 'https://github.com/shortsinsports/Data/blob/feature/'+csv,
 'https://github.com/shortsinsports/Data/blob/main/file.png',
 'https://github.com/bad%2Fname/Data/blob/main/file.csv'
].forEach(input=>assert.throws(()=>repoCsvUrl(input)));
const parseCSV=new Function(section('function parseCSV(source)','// Only unambiguous clock-style durations')+'return parseCSV;')();
const {numeric,durationKind}=new Function(section('function durationKind(v)','function fillSelectors(data)')+'return {numeric,durationKind};')();
assert.equal(numeric('2:09:45'),7785);
assert.equal(numeric('2:31:01'),9061);
assert.equal(numeric('03:12'),192);
assert.equal(numeric('1,200'),1200);
assert.ok(Number.isNaN(numeric('')));
assert.ok(Number.isNaN(numeric('DNF')));
assert.ok(Number.isNaN(numeric('2:99:01')));
const rows=parseCSV('Race,Year,Time\nTokyo,2007,2:09:45\nBoston,2008,\n');
assert.equal(rows.records.length,2);
assert.deepEqual(rows.headers,['Race','Year','Time']);
const nodes={label:{appendChild(){},disabled:true},value:{appendChild(){},disabled:true},apply:{disabled:true}};
const fillSelectors=new Function('numeric','durationKind','$','document',section('function fillSelectors(data)','function applyImported()')+'return fillSelectors;')(numeric,durationKind,id=>nodes[id],{createElement:()=>({})});
fillSelectors(rows);
assert.equal(rows.headers[Number(nodes.label.value)],'Race');
assert.equal(rows.headers[Number(nodes.value.value)],'Time');
const format=new Function('state',section('function v3Format(v)','function v3Ink(hex)')+'return v3Value;');
assert.equal(format({metric:'Time',durationFormat:'hms'})(7785),'2:09:45');
assert.equal(format({metric:'Time',durationFormat:'ms'})(192),'3:12');
assert.equal(format({metric:'duration_seconds',durationFormat:null})(234),'3:54');
assert.equal(format({metric:'visits',durationFormat:null})(1200),'1,200');
console.log('Bauhaus GitHub CSV and elapsed-time regression checks passed.');
