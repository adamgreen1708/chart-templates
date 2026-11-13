'use strict';
// Build reproducible Bauhaus-ready marathon datasets from the pinned upstream CSV.
// Run: node scripts/build_marathon_bauhaus.js
// Check: node scripts/build_marathon_bauhaus.js --check
// No external dependencies; source fields are never altered.
const base='data/marathon-majors/';
const original=['Race','Year','Sex','Winner','Nationality','Time','Notes','Birth_Country','Birth_Country_Source'];
const extras=['Race_Year','Time_Seconds','Speed_kmh','Speed_mph','Pace_Mile','Pace_Km','Decade',
 'Winner_Wins_In_File','Winner_Wins_At_Race','Nationality_Region','Event_Status','Result_Status',
 'Race_Record_To_Date','Seconds_Faster_Than_Previous_Race_Record','Global_Time_Rank'];
const regions={
 Brazil:'South America',China:'East Asia',Eritrea:'East Africa',Ethiopia:'East Africa',
 Germany:'Western Europe',Israel:'Western Asia',Japan:'East Asia',Kenya:'East Africa',
 Latvia:'Northern Europe',Morocco:'North Africa',Netherlands:'Western Europe',
 Portugal:'Southern Europe',Romania:'Eastern Europe',Russia:'Eastern Europe',
 'South Africa':'Southern Africa','South Korea':'East Asia',Sweden:'Northern Europe',
 Switzerland:'Western Europe',Uganda:'East Africa','United Kingdom':'Northern Europe',
 'United States':'North America'
};
const distanceKm=42.195,miles=distanceKm/1.609344;
function assert(value,msg){if(!value)throw Error(msg)}
function readCSV(raw){
 raw=raw.replace(/^\uFEFF/,'').replace(/\r\n?/g,'\n');
 let rows=[],row=[],field='',quoted=false;
 for(let i=0;i<raw.length;i++){
  let c=raw[i];
  if(c==='"'){if(quoted&&raw[i+1]==='"'){field+='"';i++;}else if(quoted||field==='')quoted=!quoted;else throw Error('Unexpected quote at row '+(rows.length+1));}
  else if(c===','&&!quoted){row.push(field);field='';}
  else if(c==='\n'&&!quoted){row.push(field);if(row.some(x=>x!==''))rows.push(row);row=[];field='';}
  else field+=c;
 }
 assert(!quoted,'Unclosed quoted field');
 row.push(field);if(row.some(x=>x!==''))rows.push(row);
 assert(rows.length>1,'Expected CSV with header and records');
 const header=rows.shift();
 assert(new Set(header).size===header.length,'Duplicate CSV header');
 rows.forEach((r,i)=>assert(r.length===header.length,'Wrong number of columns on row '+(i+2)));
 return {header,rows};
}
function writeCSV(header,rows){
 const cell=value=>{
  let s=String(value===undefined||value===null?'':value);
  return /[",\n\r]/.test(s)?'"'+s.replace(/"/g,'""')+'"':s;
 };
 return [header,...rows].map(r=>r.map(cell).join(',')).join('\n')+'\n';
}
function seconds(time){
 if(!time)return null;
 assert(/^\d+:[0-5]\d:[0-5]\d$/.test(time),'Invalid HH:MM:SS: '+time);
 const p=time.split(':').map(Number);return p[0]*3600+p[1]*60+p[2];
}
function clockPace(value){
 let n=Math.round(value);return Math.floor(n/60)+':'+String(n%60).padStart(2,'0');
}
function fixed(value){return value.toFixed(2);}
function eventStatus(r){
 if(r.Winner==='NO RACE'||/cancelled/i.test(r.Notes))return 'Cancelled';
 if(/virtual/i.test(r.Notes))return 'Virtual';
 return 'Completed';
}
function resultStatus(r,status){
 if(status==='Cancelled')return 'Cancelled';
 if(status==='Virtual')return 'Virtual event';
 if(/user-supplied|inferred|verify|kept per user/i.test(r.Notes))return 'Source flagged for review';
 if(/disqualif/i.test(r.Notes))return 'Disqualification mentioned';
 if(/verified|source: world athletics/i.test(r.Notes))return 'Source claims checked';
 return 'Not independently checked';
}
function countMap(rows,key){
 const m=new Map();rows.forEach(r=>m.set(key(r),(m.get(key(r))||0)+1));return m;
}
function build(source){
 const p=readCSV(source);
 assert(JSON.stringify(p.header)===JSON.stringify(original),'Upstream header changed; stop and review');
 assert(p.rows.length===308,'Upstream expected 308 rows, found '+p.rows.length);
 const rows=p.rows.map((cells,index)=>{
  const r=Object.fromEntries(original.map((h,i)=>[h,cells[i]]));
  assert(['Men','Women'].includes(r.Sex),'Unexpected Sex on row '+(index+2));
  assert(/^\d{4}$/.test(r.Year),'Unexpected Year');
  assert(!r.Nationality||regions[r.Nationality],'Nationality needs mapping: '+r.Nationality);
  r._index=index;r._seconds=seconds(r.Time);r.Event_Status=eventStatus(r);
  r.Result_Status=resultStatus(r,r.Event_Status);
  r._eligible=r.Event_Status==='Completed'&&r._seconds!==null;
  return r;
 });
 assert(rows.filter(r=>r.Sex==='Men').length===154&&rows.filter(r=>r.Sex==='Women').length===154,'Sex totals changed');
 assert(rows.filter(r=>r._seconds===null).length===8,'Missing-time total changed');
 assert(rows.filter(r=>r.Event_Status==='Virtual').length===2,'Virtual-event total changed');
 const counts={};
 for(const sex of ['Men','Women']){
  const eligible=rows.filter(r=>r.Sex===sex&&r._eligible);
  counts[sex]={overall:countMap(eligible,r=>r.Winner),race:countMap(eligible,r=>r.Race+'|'+r.Winner)};
  const ranking=eligible.slice().sort((a,b)=>a._seconds-b._seconds||a._index-b._index);
  ranking.forEach((r,i)=>{r.Global_Time_Rank=String(ranking.findIndex(x=>x._seconds===r._seconds)+1);});
  const races=[...new Set(rows.filter(r=>r.Sex===sex).map(r=>r.Race))];
  for(const race of races){
   const subset=eligible.filter(r=>r.Race===race).sort((a,b)=>Number(a.Year)-Number(b.Year)||a._index-b._index);
   let best=null;
   for(const r of subset){
    r.Race_Record_To_Date=best===null||r._seconds<best?'Yes':'No';
    r.Seconds_Faster_Than_Previous_Race_Record=best===null?'':String(Math.max(0,best-r._seconds));
    best=best===null?r._seconds:Math.min(best,r._seconds);
   }
  }
 }
 const enriched=rows.map(r=>{
  const eligible=r._eligible,t=r._seconds,sc=counts[r.Sex],speed=eligible?distanceKm*3600/t:null;
  return {...r,Race_Year:r.Race+' ('+r.Year+')',Time_Seconds:t===null?'':String(t),
   Speed_kmh:eligible?fixed(speed):'',Speed_mph:eligible?fixed(miles*3600/t):'',
   Pace_Mile:eligible?clockPace(t/miles):'',Pace_Km:eligible?clockPace(t/distanceKm):'',
   Decade:Math.floor(Number(r.Year)/10)*10+'s',
   Winner_Wins_In_File:eligible?String(sc.overall.get(r.Winner)):'',
   Winner_Wins_At_Race:eligible?String(sc.race.get(r.Race+'|'+r.Winner)):'',
   Nationality_Region:r.Nationality?regions[r.Nationality]:'',
   Race_Record_To_Date:eligible?r.Race_Record_To_Date:'',
   Seconds_Faster_Than_Previous_Race_Record:eligible?r.Seconds_Faster_Than_Previous_Race_Record:'',
   Global_Time_Rank:eligible?r.Global_Time_Rank:''
  };
 });
 const eligible=enriched.filter(r=>r._eligible);
 assert(eligible.length===298,'Eligible completed records: expected 298, got '+eligible.length);
 const sourceKeys=original.concat(extras);
 const toCSV=(records,columns)=>writeCSV(columns,records.map(r=>columns.map(h=>r[h]??'')));
 const files={};
 const reduced=['Race_Year','Winner','Nationality','Nationality_Region','Race','Year','Sex','Time',
  'Time_Seconds','Speed_kmh','Speed_mph','Pace_Mile','Event_Status','Result_Status','Notes','Global_Time_Rank'];
 for(const [sex,slug] of [['Men','men'],['Women','women']]){
  const full=enriched.filter(r=>r.Sex===sex),valid=full.filter(r=>r._eligible);
  assert(full.length===154&&valid.length===149,'Wrong '+sex+' counts');
  files[base+'marathon_major_winners_'+slug+'_2000_2026.csv']=toCSV(full,sourceKeys);
  const ranked=valid.slice().sort((a,b)=>a._seconds-b._seconds||a._index-b._index);
  files[base+'marathon_major_winners_'+slug+'_fastest12.csv']=toCSV(ranked.slice(0,12),reduced);
  const races=[...new Set(valid.map(r=>r.Race))].sort();
  const best=races.map(race=>ranked.find(r=>r.Race===race));
  assert(best.length===6&&best.every(Boolean),'Expected six races in '+sex);
  files[base+'marathon_major_winners_'+slug+'_best_by_race.csv']=toCSV(best,reduced);
  const groups=new Map();
  valid.forEach(r=>{
   if(!groups.has(r.Winner))groups.set(r.Winner,[]);
   groups.get(r.Winner).push(r);
  });
  const champions=[...groups.entries()].filter(([,rr])=>rr.length>=2)
   .map(([winner,rr])=>({
    Winner:winner,Nationality:rr[0].Nationality,Nationality_Region:rr[0].Nationality_Region,
    Wins:rr.length,First_Win_Year:Math.min(...rr.map(r=>Number(r.Year))),
    Last_Win_Year:Math.max(...rr.map(r=>Number(r.Year))),
    Distinct_Races_Won:new Set(rr.map(r=>r.Race)).size,
    Fastest_Winning_Time:rr.slice().sort((a,b)=>a._seconds-b._seconds)[0].Time,
    Fastest_Speed_kmh:fixed(distanceKm*3600/Math.min(...rr.map(r=>r._seconds)))
   })).sort((a,b)=>b.Wins-a.Wins||a.Winner.localeCompare(b.Winner));
  files[base+'marathon_major_repeat_winners_'+slug+'.csv']=toCSV(champions,
   ['Winner','Nationality','Nationality_Region','Wins','First_Win_Year','Last_Win_Year',
    'Distinct_Races_Won','Fastest_Winning_Time','Fastest_Speed_kmh']);
  const nations=new Map();
  valid.forEach(r=>{if(!nations.has(r.Nationality))nations.set(r.Nationality,[]);nations.get(r.Nationality).push(r)});
  const summary=[...nations].map(([country,rr])=>({
   Nationality:country,Nationality_Region:rr[0].Nationality_Region,Wins:rr.length,
   Share_of_Wins_pct:fixed(rr.length/valid.length*100),
   First_Win_Year:Math.min(...rr.map(r=>Number(r.Year))),
   Last_Win_Year:Math.max(...rr.map(r=>Number(r.Year))),
   Fastest_Winning_Time:rr.slice().sort((a,b)=>a._seconds-b._seconds)[0].Time,
   Fastest_Speed_kmh:fixed(distanceKm*3600/Math.min(...rr.map(r=>r._seconds)))
  })).sort((a,b)=>b.Wins-a.Wins||a.Nationality.localeCompare(b.Nationality));
  files[base+'marathon_major_wins_by_nationality_'+slug+'.csv']=toCSV(summary,
   ['Nationality','Nationality_Region','Wins','Share_of_Wins_pct','First_Win_Year',
    'Last_Win_Year','Fastest_Winning_Time','Fastest_Speed_kmh']);
 }
 // Preserve every upstream cell exactly, in order, in the first nine master columns.
 for(const sex of ['Men','Women']){
  const master=readCSV(files[base+'marathon_major_winners_'+sex.toLowerCase()+'_2000_2026.csv']);
  const ref=p.rows.filter(r=>r[2]===sex);
  assert(master.rows.length===ref.length,'Master row mismatch');
  master.rows.forEach((r,i)=>assert(JSON.stringify(r.slice(0,9))===JSON.stringify(ref[i]),'Source altered: '+sex+' row '+i));
 }
 for(const [filename,csv] of Object.entries(files)){
  const parsed=readCSV(csv);
  assert(parsed.header.length>1&&parsed.rows.length>0,'Empty generated CSV '+filename);
 }
 return {files,summary:{sourceRows:rows.length,completed:eligible.length,cancelled:rows.filter(r=>r.Event_Status==='Cancelled').length,
  virtual:rows.filter(r=>r.Event_Status==='Virtual').length,men:149,women:149,
  outputs:Object.fromEntries(Object.entries(files).map(([name,c])=>[name,readCSV(c).rows.length]))}};
}
if(typeof module!=='undefined')module.exports={build,readCSV,writeCSV};
if(typeof require==='function'&&typeof module!=='undefined'&&require.main===module){
 const fs=require('node:fs'),path=require('node:path'),root=path.resolve(__dirname,'..');
 const source=fs.readFileSync(path.join(root,base,'source/SIS-marathon_major_winners_2000_2026.csv'),'utf8');
 const result=build(source),check=process.argv.includes('--check');
 for(const [filename,content] of Object.entries(result.files)){
  const destination=path.join(root,filename);
  if(check){assert(fs.existsSync(destination),'Missing '+filename);assert(fs.readFileSync(destination,'utf8')===content,'Generated file differs: '+filename);}
  else {fs.mkdirSync(path.dirname(destination),{recursive:true});fs.writeFileSync(destination,content);}
 }
 console.log(JSON.stringify({mode:check?'check':'build',...result.summary},null,2));
}
