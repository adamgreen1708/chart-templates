/* Coffeetableviz: EPL 2026–27 Season Unfolded, Tableau-inspired dark seasonal results board.
   Match and club values are read only from the Python-built, pinned, verified GitHub JSON. */
(function () {
  'use strict';
  const root = document.getElementById('epl-unfolded');
  if (!root || root.dataset.loaded === '1') return;
  root.dataset.loaded = '1';
  const viz = root.querySelector('#eplu-viz');
  const calendar = root.querySelector('#eplu-calendar');
  const totalsBody = root.querySelector('#eplu-totals-body');
  const clubName = root.querySelector('#eplu-club-name');
  const rank = root.querySelector('#eplu-rank');
  const picker = root.querySelector('#eplu-team');
  const clear = root.querySelector('#eplu-clear');
  const status = root.querySelector('#eplu-status');
  const tooltip = root.querySelector('#eplu-tooltip');
  const pointsSvg = root.querySelector('#eplu-points-svg');
  const svgNS = 'http://www.w3.org/2000/svg';
  const monthKeys = ['2026-08','2026-09','2026-10','2026-11','2026-12','2027-01','2027-02','2027-03','2027-04','2027-05'];
  const monthLabels = ['AUG','SEP','OCT','NOV','DEC','JAN','FEB','MAR','APR','MAY'];
  const abbreviations = {
    'Arsenal':'ARS','Aston Villa':'AVL','Bournemouth':'BOU','Brentford':'BRE','Brighton':'BRI',
    'Burnley':'BUR','Chelsea':'CHE','Crystal Palace':'CRY','Everton':'EVE','Fulham':'FUL',
    'Coventry':'COV','Hull':'HUL','Ipswich':'IPS','Leeds':'LEE','Liverpool':'LIV','Man City':'MCI','Man United':'MUN','Newcastle':'NEW',
    "Nott'm Forest":'NFO','Sunderland':'SUN','Tottenham':'TOT','West Ham':'WHU','Wolves':'WOL'
  };
  // Representative 2026–27 home-kit primary colours, not licensed brand hex specifications.
  // Black/white home kits intentionally stay black/white; visibility is provided by outline/contrast styling.
  const primaryByClub = Object.freeze({
    'Arsenal':'#EF0107', 'Aston Villa':'#670E36', 'Bournemouth':'#DA291C',
    'Brentford':'#E30613', 'Brighton':'#0057B8', 'Burnley':'#6C1D45',
    'Chelsea':'#034694', 'Crystal Palace':'#1B458F', 'Everton':'#003399',
    'Fulham':'#FFFFFF', 'Leeds':'#FFFFFF', 'Liverpool':'#C8102E',
    'Coventry':'#69B9E7', 'Hull':'#F3A124', 'Ipswich':'#0044A8', 'Man City':'#6CABDD', 'Man United':'#DA291C', 'Newcastle':'#111111',
    "Nott'm Forest":'#DD0000', 'Sunderland':'#EB172B', 'Tottenham':'#FFFFFF',
    'West Ham':'#7A263A', 'Wolves':'#FDB913'
  });
  function srgb(hex) {
    return [1,3,5].map(i => parseInt(hex.slice(i,i+2),16)/255).map(c => c<=.04045 ? c/12.92 : Math.pow((c+.055)/1.055,2.4));
  }
  function luminance(hex) {
    const [r,g,b]=srgb(hex);
    return .2126*r+.7152*g+.0722*b;
  }
  function contrast(a,b) {
    const l1=luminance(a), l2=luminance(b);
    return (Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
  }
  function textOn(hex) { return contrast('#FFFFFF',hex)>=contrast('#202326',hex) ? '#FFFFFF' : '#202326'; }
  function lightenForTitle(hex) {
    const bg='#303133';
    if(contrast(hex,bg)>=4.5)return hex;
    const rgb=[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16));
    for(let amount=1;amount<=100;amount++){
      const blend='#'+rgb.map(v=>Math.round(v+(255-v)*amount/100).toString(16).padStart(2,'0')).join('');
      if(contrast(blend,bg)>=4.5)return blend;
    }
    return '#FFFFFF';
  }
  function applyClubColour(name) {
    const primary=primaryByClub[name]||'#F1F2F2';
    const readable=lightenForTitle(primary);
    const against=textOn(primary);
    viz.style.setProperty('--ev-win',primary);
    viz.style.setProperty('--ev-win-text',against);
    viz.style.setProperty('--ev-win-outline',contrast(primary,'#303133')<2.8?'#CBD1D5':'transparent');
    viz.style.setProperty('--ev-club-heading',readable);
  }
  const numeric = n => Number(n).toLocaleString('en-GB');
  const create = (tag, cls, value) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (value !== undefined) e.textContent = String(value);
    return e;
  };
  const svgNode = (tag, attrs, parent, value) => {
    const e = document.createElementNS(svgNS, tag);
    Object.entries(attrs || {}).forEach(([key,val]) => e.setAttribute(key, String(val)));
    if (value !== undefined) e.textContent = String(value);
    (parent || pointsSvg).appendChild(e);
    return e;
  };
  let season = null;
  let team = null;
  let pickedMatch = null;
  let lastWidth = 0;
  let hovered = false;

  const byName = name => season && season.teams.find(t => t.name === name);
  const fullDate = date => new Date(date + 'T12:00:00Z')
    .toLocaleDateString('en-GB', {day:'numeric',month:'short',year:'numeric',timeZone:'UTC'});
  const resultWord = code => code === 'W' ? 'WIN' : code === 'D' ? 'DRAW' : 'DEFEAT';

  function statsFor(venue) {
    const games = team.games.filter(g => g.venue === venue);
    const wins = games.filter(g => g.result === 'W').length;
    const draws = games.filter(g => g.result === 'D').length;
    const losses = games.filter(g => g.result === 'L').length;
    const gf = games.reduce((s,g) => s+g.gf,0);
    const ga = games.reduce((s,g) => s+g.ga,0);
    const pts = wins*3 + draws;
    return [games.length,wins,draws,losses,gf,ga,gf-ga,pts];
  }

  function makeTotals() {
    totalsBody.replaceChildren();
    ['H','A'].forEach(venue => {
      const tr = create('tr');
      const heading = create('th','',venue === 'H' ? 'HOME' : 'AWAY');
      heading.scope = 'row';
      tr.appendChild(heading);
      statsFor(venue).forEach((value,i) => {
        const td = create('td',i===1?'stat-win':i===2?'stat-draw':i===3?'stat-loss':i===7?'stat-pts':'', (i===6&&value>0?'+':'')+value);
        tr.appendChild(td);
      });
      totalsBody.appendChild(tr);
    });
  }

  function positionTooltip(target) {
    const ownerRect=viz.getBoundingClientRect();
    const rect=target.getBoundingClientRect();
    const width=tooltip.offsetWidth, height=tooltip.offsetHeight;
    const px=rect.left-ownerRect.left + rect.width/2;
    const py=rect.top-ownerRect.top + rect.height/2;
    const margin=10;
    let x=px+17;
    if(x+width>viz.clientWidth-margin)x=px-width-18;
    x=Math.max(margin,Math.min(Math.max(margin,viz.clientWidth-width-margin),x));
    let y=py-height-13;
    if(y<margin)y=py+17;
    y=Math.max(margin,Math.min(Math.max(margin,viz.clientHeight-height-margin),y));
    tooltip.style.left=x+'px';
    tooltip.style.top=y+'px';
  }
  // Miniature twenty-club cumulative-points plot, using the SAME real verified season data.
  // Match N is each club's Nth completed match, not a shared calendar date or fixture round.
  function addCumulativeTooltipChart(focusClub, matchNumber) {
    if (!season || !focusClub || !Array.isArray(season.teams)) return;
    const index = Math.min(focusClub.played, Math.max(0, Number(matchNumber) || focusClub.played));
    const area = create('div','eplu-tip-trajectory');
    const head = create('div','eplu-tip-trajectory-title');
    head.appendChild(create('span','', 'CUMULATIVE POINTS'));
    head.appendChild(create('span','', '20 CLUBS'));
    area.appendChild(head);
    const focusValue = index ? focusClub.games[index-1].points : 0;
    // Use the current league leader's verified points, not the final-season 90-point ceiling.
    // Retain a nonzero denominator for the opening days before any points are earned.
    const pointsCap=Math.max(1,...season.teams.map(t=>t.points));
    const maximumPlayed=Math.max(1,...season.teams.map(c=>c.played));
    const description = 'All 20 clubs, cumulative points through each club\'s completed matches (0 to '+maximumPlayed+'). Points scale 0 to '+pointsCap+', the current league-leading total. '+focusClub.name+' highlighted, at match '+index+' with '+focusValue+' points.';
    const mini = svgNode('svg',{
      viewBox:'0 0 270 142',class:'eplu-tip-mini','aria-label':description,role:'img',
      preserveAspectRatio:'xMidYMid meet'
    },area);
    const left=27,right=259,top=9,bottom=113;
    const x=n=>left+n/maximumPlayed*(right-left);
    const y=n=>bottom-n/pointsCap*(bottom-top);
    // Integer-only labels, with the true maximum shown at the top of the axis.
    [...new Set([0,Math.round(pointsCap/2),pointsCap])].forEach(value=>{
      const ypos=y(value);
      svgNode('line',{x1:left,x2:right,y1:ypos,y2:ypos,stroke:'#E4EAEE','stroke-width':.7,opacity:.3},mini);
      svgNode('text',{x:left-6,y:ypos+3,'text-anchor':'end',fill:'#E3E8EA','font-size':9,'font-family':'monospace'},mini,value);
    });
    [...new Set([0,Math.floor(maximumPlayed/2),maximumPlayed])].forEach(n=>{
      svgNode('text',{x:x(n),y:135,'text-anchor':'middle',fill:'#E3E8EA','font-size':9,'font-family':'monospace'},mini,n);
    });
    const makePath=club=>{
      let d='M'+x(0).toFixed(1)+','+y(0).toFixed(1);
      club.games.forEach(g=>{
        d+='L'+x(g.number).toFixed(1)+','+y(g.points).toFixed(1);
      });
      return d;
    };
    season.teams.filter(club=>club.name!==focusClub.name).forEach(club=>{
      svgNode('path',{d:makePath(club),fill:'none',stroke:'#DFE5E9',
        'stroke-width':.85,opacity:.36,'stroke-linejoin':'round',
        'stroke-linecap':'round'},mini);
    });
    const focusColour=lightenForTitle(primaryByClub[focusClub.name]||'#FFFFFF');
    svgNode('path',{d:makePath(focusClub),fill:'none',stroke:focusColour,
      'stroke-width':3,opacity:1,'stroke-linejoin':'round','stroke-linecap':'round'},mini);
    svgNode('circle',{cx:x(index),cy:y(focusValue),r:5.4,fill:'none',
      stroke:'#FFFFFF','stroke-width':1.4},mini);
    svgNode('circle',{cx:x(index),cy:y(focusValue),r:3.1,fill:focusColour},mini);
    const summary = create('div','eplu-tip-trajectory-summary');
    const focusLabel=create('span','',focusClub.name+' · '+focusValue+' pts after '+index);
    focusLabel.style.color=focusColour;
    summary.appendChild(focusLabel);
    summary.appendChild(create('span','','Each club\'s own game number'));
    area.appendChild(summary);
    tooltip.appendChild(area);
  }
  function matchInfo(game, target, pinned) {
    if (!game || !target) return;
    tooltip.replaceChildren();
    const top=create('div','eplu-tip-overline');
    top.appendChild(create('span','',resultWord(game.result)));
    top.appendChild(create('span','',pinned?'● SELECTED':'MATCH '+game.number+'/'+team.played));
    tooltip.appendChild(top);
    tooltip.appendChild(create('div','eplu-tip-title',team.name+' vs '+game.opponent));
    tooltip.appendChild(create('div','eplu-tip-sub',(game.venue==='H'?'HOME':'AWAY')+' · '+resultWord(game.result)));
    tooltip.appendChild(create('div','eplu-tip-line'));
    const results=create('div','eplu-tip-stats');
    const home=game.venue==='H'?team.name:game.opponent;
    const away=game.venue==='A'?team.name:game.opponent;
    const homeGoals=game.venue==='H'?game.gf:game.ga;
    const awayGoals=game.venue==='A'?game.gf:game.ga;
    const items=[['FULL-TIME',homeGoals+'–'+awayGoals],['POINTS SO FAR',game.points]];
    items.forEach(([label,value])=>{
      const cell=create('div');cell.appendChild(create('small','',label));
      cell.appendChild(create('strong','',value));results.appendChild(cell);
    });
    tooltip.appendChild(results);
    addCumulativeTooltipChart(team,game.number);
    tooltip.appendChild(create('div','eplu-tip-date',fullDate(game.date)+' · '+home+' vs '+away+' · match '+game.number));
    tooltip.hidden=false;
    positionTooltip(target);
  }
  function pointInfo(club, target) {
    tooltip.replaceChildren();
    const top=create('div','eplu-tip-overline');
    top.appendChild(create('span','',season.meta.complete ? 'FINAL POSITION' : 'CURRENT POSITION · PROVISIONAL'));
    top.appendChild(create('span','','#'+club.rank+' OF 20'));
    tooltip.appendChild(top);
    tooltip.appendChild(create('div','eplu-tip-title',club.name));
    tooltip.appendChild(create('div','eplu-tip-sub','2026–27 Premier League'));
    tooltip.appendChild(create('div','eplu-tip-line'));
    const stats=create('div','eplu-tip-stats');
    [['POINTS',club.points],['GOAL DIFF.',(club.gd>0?'+':'')+club.gd]].forEach(([name,value])=>{
      const cell=create('div');
      cell.appendChild(create('small','',name));
      cell.appendChild(create('strong','',value));
      stats.appendChild(cell);
    });
    tooltip.appendChild(stats);
    addCumulativeTooltipChart(team,pickedMatch || team.played);
    tooltip.appendChild(create('div','eplu-tip-date','Tap this club badge to view its monthly results'));
    tooltip.hidden=false;
    positionTooltip(target);
  }
  function hideOrRestore() {
    hovered=false;
    if (!pickedMatch) {tooltip.hidden=true;return;}
    const node=calendar.querySelector('button[data-match="'+pickedMatch+'"]');
    const game=team.games.find(g=>String(g.number)===String(pickedMatch));
    if(node && game) matchInfo(game,node,true);
    else tooltip.hidden=true;
  }
  // A stationary glass halo belongs to the latest completed match only while no match is pinned.
  function syncLatestHalo() {
    calendar.querySelectorAll('.eplu-match').forEach(btn=>{
      btn.classList.toggle('is-latest', !pickedMatch && Number(btn.dataset.match)===team.played);
    });
  }
  function clearPicked() {
    if(!pickedMatch) {tooltip.hidden=true;return;}
    pickedMatch=null;
    clear.disabled=true;
    calendar.querySelectorAll('.eplu-match').forEach(btn=>{
      btn.classList.remove('is-selected','is-muted');
      btn.setAttribute('aria-pressed','false');
    });
    syncLatestHalo();
    tooltip.hidden=true;
  }
  function selectMatch(game) {
    if(pickedMatch===game.number){clearPicked();return;}
    pickedMatch=game.number;
    clear.disabled=false;
    calendar.querySelectorAll('.eplu-match').forEach(btn=>{
      const selected=Number(btn.dataset.match)===pickedMatch;
      btn.classList.toggle('is-selected',selected);
      btn.classList.toggle('is-muted',!selected);
      btn.setAttribute('aria-pressed',String(selected));
    });
    syncLatestHalo();
    const button=calendar.querySelector('button[data-match="'+pickedMatch+'"]');
    if(button)matchInfo(game,button,true);
  }
  function makeCalendar() {
    calendar.replaceChildren();
    pickedMatch=null;
    clear.disabled=true;
    tooltip.hidden=true;
    monthKeys.forEach((month,index) => {
      const column=create('div','eplu-month');
      column.setAttribute('aria-label',monthLabels[index]+' '+(index<5?'2026':'2027'));
      const home=create('div','eplu-month-home');
      const away=create('div','eplu-month-away');
      for (const [venue,host] of [['H',home],['A',away]]) {
        // Chronology radiates outward from the central month label:
        // home earliest = bottom (reverse DOM order), away earliest = top (normal order).
        const dated = team.games.filter(g=>g.date.startsWith(month)&&g.venue===venue);
        if(venue==='H')dated.reverse();
        dated.forEach(game=>{
          const btn=create('button','eplu-match',game.result);
          btn.type='button';
          btn.dataset.result=game.result;
          btn.dataset.match=String(game.number);
          btn.setAttribute('aria-pressed','false');
          const homeName=venue==='H'?team.name:game.opponent;
          const awayName=venue==='H'?game.opponent:team.name;
          const hg=venue==='H'?game.gf:game.ga,ag=venue==='H'?game.ga:game.gf;
          btn.setAttribute('aria-label',fullDate(game.date)+', '+homeName+' '+hg+' to '+ag+' '+awayName+', '+resultWord(game.result).toLowerCase()+', match '+game.number+(game.number===team.played?', latest completed result':''));
          btn.addEventListener('click',e=>{e.stopPropagation();selectMatch(game)});
          btn.addEventListener('pointerenter',e=>{if(e.pointerType==='touch')return;hovered=true;matchInfo(game,btn,game.number===pickedMatch)});
          btn.addEventListener('pointerleave',()=>hideOrRestore());
          btn.addEventListener('focus',()=>{if(!pickedMatch)matchInfo(game,btn,false)});
          btn.addEventListener('blur',()=>hideOrRestore());
          host.appendChild(btn);
        });
      }
      const name=create('div','eplu-month-name',monthLabels[index]);
      name.title=(index<5?'2026':'2027')+' '+monthLabels[index];
      column.append(home,name,away);
      calendar.appendChild(column);
    });
    syncLatestHalo();
  }

  function setTeam(name) {
    const match=byName(name);
    if(!match)return;
    team=match;
    applyClubColour(team.name);
    clubName.textContent=team.name.toUpperCase();
    rank.textContent=String(team.rank);
    rank.setAttribute('aria-label',(season.meta.complete?'Final':'Provisional')+' league position '+team.rank);
    picker.value=name;
    makeTotals();
    makeCalendar();
    makePointsPlot();
    status.textContent=team.name+' · '+team.points+' points · '+team.played+' played · '+team.rank+(team.rank===1?'st':team.rank===2?'nd':team.rank===3?'rd':'th')+' '+(season.meta.complete?'final':'provisional')+' place · results to '+fullDate(season.meta.lastDate);
    const stamp=root.querySelector('#eplu-data-stamp');
    if(stamp)stamp.textContent='COMPLETED RESULTS THROUGH '+fullDate(season.meta.lastDate).toUpperCase()+' · '+season.meta.matchCount+' MATCHES · '+(season.meta.complete?'FINAL':'PROVISIONAL')+' STANDINGS';
    const key=root.querySelector('#eplu-points-key');
    if(key)key.textContent='20 CLUBS · '+season.meta.matchCount+' COMPLETED MATCHES';
  }

  function makePointsPlot() {
    const W=Math.max(240,Math.round(pointsSvg.clientWidth||800));
    lastWidth=W;
    const mobile=W<580;
    const radius=mobile?13:15;
    const touch=mobile?18:20;
    const L=mobile?23:38,R=mobile?21:34;
    const plotWidth=W-L-R;
    const highest=Math.max(0,...season.teams.map(t=>t.points));
    const scaleMax=Math.max(10,Math.ceil((highest+5)/10)*10);
    const x=points=>L+(points/scaleMax)*plotWidth;
    const plotted=[];
    const clubPositions=season.teams.slice().sort((a,b)=>a.points-b.points || a.rank-b.rank).map(club=>{
      const cx=x(club.points);
      let lane=0;
      while(plotted.some(p=>p.lane===lane&&Math.abs(p.cx-cx)<(radius*2+7)))lane++;
      const entry={club,cx,lane};
      plotted.push(entry);
      return entry;
    });
    const maxLane=Math.max(...plotted.map(p=>p.lane));
    const gap=mobile?32:37;
    const baseline=28+maxLane*gap+radius+36;
    const H=baseline+34;
    pointsSvg.replaceChildren();
    pointsSvg.setAttribute('viewBox','0 0 '+W+' '+H);
    svgNode('line',{x1:L,x2:W-R,y1:baseline,y2:baseline,stroke:'#606366','stroke-width':1});
    const tickStep=scaleMax<=30?5:scaleMax<=60?10:20;
    Array.from({length:Math.floor(scaleMax/tickStep)+1},(_,i)=>i*tickStep).concat(scaleMax%tickStep?[scaleMax]:[]).forEach(value=>{
      const cx=x(value);
      svgNode('line',{x1:cx,x2:cx,y1:baseline,y2:baseline+5,stroke:'#74787B'});
      svgNode('text',{x:cx,y:baseline+19,'text-anchor':'middle',fill:'#9FA4A9','font-size':mobile?10:12,'font-family':'IBM Plex Mono, monospace'},undefined,value);
    });
    const ordered=clubPositions.slice().sort((a,b)=>(a.club.name===team.name?1:0)-(b.club.name===team.name?1:0));
    ordered.forEach(entry=>{
      const club=entry.club,cx=entry.cx,cy=28+entry.lane*gap;
      const selected=club.name===team.name;
      svgNode('line',{x1:cx,x2:cx,y1:cy+radius+3,y2:baseline,stroke:selected?'#D6D8D9':'#555A5E',opacity:selected?.65:.3,'stroke-width':1,'pointer-events':'none'});
      const group=svgNode('g',{tabindex:0,role:'button','aria-label':club.name+', '+(season.meta.complete?'final':'provisional')+' position '+club.rank+', '+club.points+' points; select club','aria-pressed':String(selected),'data-club':club.name,style:'cursor:pointer'});
      svgNode('circle',{cx,cy,r:touch,fill:'transparent'},group);
      const fill = selected ? primaryByClub[club.name] : '#4D5256';
      svgNode('circle',{cx,cy,r:radius,fill,stroke:selected?'#D6DFE4':'#95999C','stroke-width':selected?1.9:1,opacity:selected?1:.43},group);
      svgNode('text',{x:cx,y:cy+3.5,'text-anchor':'middle',fill:selected?textOn(fill):'#F7F7F7','font-size':mobile?8:9.5,'font-family':'IBM Plex Mono, monospace','font-weight':600,'pointer-events':'none'},group,abbreviations[club.name]||club.name.slice(0,3).toUpperCase());
      group.addEventListener('click',e=>{e.stopPropagation();setTeam(club.name)});
      group.addEventListener('keydown',e=>{
        if(e.key==='Enter'||e.key===' '){e.preventDefault();e.stopPropagation();setTeam(club.name)}
      });
      group.addEventListener('pointerenter',e=>{
        if(e.pointerType==='touch')return;
        hovered=true;pointInfo(club,group);
      });
      group.addEventListener('pointerleave',()=>hideOrRestore());
      group.addEventListener('focus',()=>{if(!pickedMatch)pointInfo(club,group)});
      group.addEventListener('blur',()=>hideOrRestore());
    });
  }

  function prepareSeason(json) {
    if(!json || json.meta?.season!=='2026–27' || json.meta?.teamCount!==20
      || json.teams?.length!==20 || !Number.isInteger(json.meta.matchCount)
      || json.meta.matchCount<1 || json.meta.matchCount>380)
      throw Error('Expected a verified, partially played 2026–27 Premier League dataset');
    let totalGames=0;
    const seen=new Set();
    for(const club of json.teams) {
      if(!Array.isArray(club.games) || club.games.length!==club.played || club.played>38
        || club.games.some(g=>!monthKeys.includes(g.date.slice(0,7))))
        throw Error('Invalid match count or month for '+club.name);
      const home=club.games.filter(g=>g.venue==='H'),away=club.games.filter(g=>g.venue==='A');
      if(home.length>19||away.length>19||home.length+away.length!==club.played)
        throw Error('Invalid venue count for '+club.name);
      let points=0;
      club.games.forEach((g,i)=>{
        if(g.number!==i+1 || !['W','D','L'].includes(g.result))
          throw Error('Non-sequential match or invalid result for '+club.name);
        points+=g.result==='W'?3:g.result==='D'?1:0;
        if(points!==g.points)throw Error('Invalid cumulative points for '+club.name);
      });
      if(points!==club.points||club.w+club.d+club.l!==club.played)
        throw Error('Invalid totals for '+club.name);
      seen.add(club.name);
      totalGames+=club.played;
    }
    if(seen.size!==20||totalGames!==2*json.meta.matchCount)throw Error('Unbalanced dataset');
    return json;
  }
  picker.addEventListener('change',()=>setTeam(picker.value));
  clear.addEventListener('click',e=>{e.stopPropagation();clearPicked()});
  viz.addEventListener('click',e=>{
    if(!e.target.closest('button[data-match], [data-club], #eplu-team, #eplu-clear')) clearPicked();
  });
  if(typeof ResizeObserver!=='undefined') {
    new ResizeObserver(()=>{
      const w=Math.round(pointsSvg.clientWidth);
      if(season && team && w>0 && w!==lastWidth)makePointsPlot();
    }).observe(pointsSvg);
  }
  fetch(root.dataset.source,{cache:'no-cache'})
    .then(r=>{if(!r.ok)throw Error('HTTP '+r.status);return r.json()})
    .then(json=>{
      season=prepareSeason(json);
      const attribution = root.querySelector('#eplu-data-source');
      if (attribution) {
        const provider = json.meta.source === 'https://www.football-data.org/'
          ? 'football-data.org' : json.meta.source === 'https://www.football-data.co.uk/mmz4281/2627/E0.csv'
            ? 'Football-Data.co.uk' : 'unverified source';
        attribution.textContent = 'Source: ' + provider + ' · 2026–27 completed results only';
      }
      picker.replaceChildren();
      season.teams.forEach(club=>{
        const option=create('option','',club.name);
        option.value=club.name;
        picker.appendChild(option);
      });
      setTeam('Arsenal');
    })
    .catch(error=>{
      status.textContent='Could not load the verified season dataset ('+error.message+').';
      totalsBody.replaceChildren();
      const tr=create('tr'),td=create('td','',status.textContent);
      td.colSpan=9;tr.appendChild(td);totalsBody.appendChild(tr);
    });
})();
