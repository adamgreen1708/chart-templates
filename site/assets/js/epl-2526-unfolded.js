/* Coffeetableviz: EPL 2025–26 Season Unfolded, Tableau-inspired dark seasonal results board.
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
  const monthKeys = ['2025-08','2025-09','2025-10','2025-11','2025-12','2026-01','2026-02','2026-03','2026-04','2026-05'];
  const monthLabels = ['AUG','SEP','OCT','NOV','DEC','JAN','FEB','MAR','APR','MAY'];
  const abbreviations = {
    'Arsenal':'ARS','Aston Villa':'AVL','Bournemouth':'BOU','Brentford':'BRE','Brighton':'BRI',
    'Burnley':'BUR','Chelsea':'CHE','Crystal Palace':'CRY','Everton':'EVE','Fulham':'FUL',
    'Leeds':'LEE','Liverpool':'LIV','Man City':'MCI','Man United':'MUN','Newcastle':'NEW',
    "Nott'm Forest":'NFO','Sunderland':'SUN','Tottenham':'TOT','West Ham':'WHU','Wolves':'WOL'
  };
  // Representative 2025–26 home-kit primary colours, not licensed brand hex specifications.
  // Black/white home kits intentionally stay black/white; visibility is provided by outline/contrast styling.
  const primaryByClub = Object.freeze({
    'Arsenal':'#EF0107', 'Aston Villa':'#670E36', 'Bournemouth':'#DA291C',
    'Brentford':'#E30613', 'Brighton':'#0057B8', 'Burnley':'#6C1D45',
    'Chelsea':'#034694', 'Crystal Palace':'#1B458F', 'Everton':'#003399',
    'Fulham':'#FFFFFF', 'Leeds':'#FFFFFF', 'Liverpool':'#C8102E',
    'Man City':'#6CABDD', 'Man United':'#DA291C', 'Newcastle':'#111111',
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
    const index = Math.min(38, Math.max(1, Number(matchNumber) || 38));
    const area = create('div','eplu-tip-trajectory');
    const head = create('div','eplu-tip-trajectory-title');
    head.appendChild(create('span','', 'CUMULATIVE POINTS'));
    head.appendChild(create('span','', '20 CLUBS'));
    area.appendChild(head);
    const focusValue = focusClub.games[index-1].points;
    const description = 'All 20 clubs, cumulative points by each club\'s match number 0 to 38. '+focusClub.name+' highlighted, at match '+index+' with '+focusValue+' points.';
    const mini = svgNode('svg',{
      viewBox:'0 0 270 142',class:'eplu-tip-mini','aria-label':description,role:'img',
      preserveAspectRatio:'xMidYMid meet'
    },area);
    const left=27,right=259,top=9,bottom=113;
    const x=n=>left+n/38*(right-left);
    const y=n=>bottom-n/90*(bottom-top);
    [0,45,90].forEach(value=>{
      const ypos=y(value);
      svgNode('line',{x1:left,x2:right,y1:ypos,y2:ypos,stroke:'#E4EAEE','stroke-width':.7,opacity:.3},mini);
      svgNode('text',{x:left-6,y:ypos+3,'text-anchor':'end',fill:'#E3E8EA','font-size':9,'font-family':'monospace'},mini,value);
    });
    [0,19,38].forEach(n=>{
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
    top.appendChild(create('span','',pinned?'● SELECTED':'MATCH '+game.number+'/38'));
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
    top.appendChild(create('span','','FINAL POSITION'));
    top.appendChild(create('span','','#'+club.rank+' OF 20'));
    tooltip.appendChild(top);
    tooltip.appendChild(create('div','eplu-tip-title',club.name));
    tooltip.appendChild(create('div','eplu-tip-sub','2025–26 Premier League'));
    tooltip.appendChild(create('div','eplu-tip-line'));
    const stats=create('div','eplu-tip-stats');
    [['POINTS',club.points],['GOAL DIFF.',(club.gd>0?'+':'')+club.gd]].forEach(([name,value])=>{
      const cell=create('div');
      cell.appendChild(create('small','',name));
      cell.appendChild(create('strong','',value));
      stats.appendChild(cell);
    });
    tooltip.appendChild(stats);
    addCumulativeTooltipChart(team,pickedMatch || 38);
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
  function clearPicked() {
    if(!pickedMatch) {tooltip.hidden=true;return;}
    pickedMatch=null;
    clear.disabled=true;
    calendar.querySelectorAll('.eplu-match').forEach(btn=>{
      btn.classList.remove('is-selected','is-muted');
      btn.setAttribute('aria-pressed','false');
    });
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
      column.setAttribute('aria-label',monthLabels[index]+' '+(index<5?'2025':'2026'));
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
          btn.setAttribute('aria-label',fullDate(game.date)+', '+homeName+' '+hg+' to '+ag+' '+awayName+', '+resultWord(game.result).toLowerCase()+', match '+game.number);
          btn.addEventListener('click',e=>{e.stopPropagation();selectMatch(game)});
          btn.addEventListener('pointerenter',e=>{if(e.pointerType==='touch')return;hovered=true;matchInfo(game,btn,game.number===pickedMatch)});
          btn.addEventListener('pointerleave',()=>hideOrRestore());
          btn.addEventListener('focus',()=>{if(!pickedMatch)matchInfo(game,btn,false)});
          btn.addEventListener('blur',()=>hideOrRestore());
          host.appendChild(btn);
        });
      }
      const name=create('div','eplu-month-name',monthLabels[index]);
      name.title=(index<5?'2025':'2026')+' '+monthLabels[index];
      column.append(home,name,away);
      calendar.appendChild(column);
    });
  }

  function setTeam(name) {
    const match=byName(name);
    if(!match)return;
    team=match;
    applyClubColour(team.name);
    clubName.textContent=team.name.toUpperCase();
    rank.textContent=String(team.rank);
    rank.setAttribute('aria-label','Final league position '+team.rank);
    picker.value=name;
    makeTotals();
    makeCalendar();
    makePointsPlot();
    status.textContent=team.name+' · '+team.points+' points · '+team.rank+(team.rank===1?'st':team.rank===2?'nd':team.rank===3?'rd':'th')+' place';
  }

  function makePointsPlot() {
    const W=Math.max(240,Math.round(pointsSvg.clientWidth||800));
    lastWidth=W;
    const mobile=W<580;
    const radius=mobile?13:15;
    const touch=mobile?18:20;
    const L=mobile?23:38,R=mobile?21:34;
    const plotWidth=W-L-R;
    const x=points=>L+(points/90)*plotWidth;
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
    [0,20,40,60,80,90].forEach(value=>{
      const cx=x(value);
      svgNode('line',{x1:cx,x2:cx,y1:baseline,y2:baseline+5,stroke:'#74787B'});
      svgNode('text',{x:cx,y:baseline+19,'text-anchor':'middle',fill:'#9FA4A9','font-size':mobile?10:12,'font-family':'IBM Plex Mono, monospace'},undefined,value);
    });
    const ordered=clubPositions.slice().sort((a,b)=>(a.club.name===team.name?1:0)-(b.club.name===team.name?1:0));
    ordered.forEach(entry=>{
      const club=entry.club,cx=entry.cx,cy=28+entry.lane*gap;
      const selected=club.name===team.name;
      svgNode('line',{x1:cx,x2:cx,y1:cy+radius+3,y2:baseline,stroke:selected?'#D6D8D9':'#555A5E',opacity:selected?.65:.3,'stroke-width':1,'pointer-events':'none'});
      const group=svgNode('g',{tabindex:0,role:'button','aria-label':club.name+', position '+club.rank+', '+club.points+' points; select club','aria-pressed':String(selected),'data-club':club.name,style:'cursor:pointer'});
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
    if(!json || json.meta?.matchCount!==380 || json.teams?.length!==20
      || json.teams.some(t=>t.games?.length!==38
        || t.games.some(g=>!monthKeys.includes(g.date.slice(0,7)))))
      throw Error('Expected the verified 380-fixture, 20-team Premier League season dataset');
    for(const club of json.teams) {
      const home=club.games.filter(g=>g.venue==='H'),away=club.games.filter(g=>g.venue==='A');
      if(home.length!==19||away.length!==19||home.length+away.length!==38)
        throw Error('Invalid home / away fixture counts for '+club.name);
      const computed=club.games.reduce((p,g)=>p+(g.result==='W'?3:g.result==='D'?1:0),0);
      if(computed!==club.points || club.games[37].points!==club.points)
        throw Error('Invalid cumulative points for '+club.name);
    }
    if(json.teams[0].name!=='Arsenal'||json.teams[0].points!==85)
      throw Error('Final points failed official league table crosscheck');
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
  fetch(root.dataset.source,{cache:'force-cache'})
    .then(r=>{if(!r.ok)throw Error('HTTP '+r.status);return r.json()})
    .then(json=>{
      season=prepareSeason(json);
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
