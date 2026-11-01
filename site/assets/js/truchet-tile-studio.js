
(()=>{
'use strict';
const $=id=>document.getElementById(id);
const canvas=$('art');
const ctx=canvas.getContext('2d',{alpha:false});
const modes={chequer:'Chequerboard',radial:'Radial rings',stripes:'Diagonal drift',pinwheel:'Pinwheel',random:'Beautiful mess',waves:'Waves'};
const palettes=[['#111111','#f7f7f5'],['#3d4950','#e9ecee'],['#1f8fa8','#f7f7f5'],['#bb504b','#f7f7f5']];
const state={n:16,mode:'radial',seed:93,palette:0,invert:false,grid:false,chaos:20,linked:true,tiles:[],linkedEdits:new Map(),singleEdits:new Map(),undo:[]};
const mod=(a,n)=>(a%n+n)%n;
const hash=(x,y,s)=>{let h=((x+51)*374761393+(y+37)*668265263+s*1442695041)|0;h=Math.imul(h^(h>>>13),1274126177);return (h^(h>>>16))>>>0};
const mirror=(a,h,v)=>{if(h)a=[1,0,3,2][a];if(v)a=[3,2,1,0][a];return a};
const ref=(x,y)=>({u:Math.min(x,state.n-1-x),v:Math.min(y,state.n-1-y),h:x>=state.n/2,w:y>=state.n/2});
const id=(x,y)=>y*state.n+x;
const pointKey=(x,y)=>x+','+y;
function pattern(x,y){
 const n=state.n,c=(n-1)/2,dx=x-c,dy=y-c,ring=Math.floor(Math.hypot(dx,dy));
 switch(state.mode){
 case 'chequer':return(x+y)%2;
 case 'radial':return mod(ring+Math.floor(ring/3),4);
 case 'stripes':return mod(x+2*y+Math.floor(y/3),4);
 case 'pinwheel':return mod(Math.floor((Math.atan2(dy,dx)+Math.PI)/(Math.PI/2))+Math.floor(Math.hypot(dx,dy)/3),4);
 case 'waves':return mod(Math.floor((x+3*Math.sin(y*.72))/2)+Math.floor((y+2*Math.sin(x*.7))/3),4);
 default:return hash(x,y,state.seed)%4;
 }
}
function noise(x,y){
 if(state.chaos===0)return 0;
 const p=hash(x,y,state.seed+701)%10000;
 return p<state.chaos*100 ? hash(x+129,y+17,state.seed+1903)%4 : 0;
}
function rebuild(){
 state.tiles=Array.from({length:state.n*state.n},(_,i)=>{
  const x=i%state.n,y=Math.floor(i/state.n),r=ref(x,y);
  const base=state.linkedEdits.has(pointKey(r.u,r.v))?state.linkedEdits.get(pointKey(r.u,r.v)):pattern(r.u,r.v);
  const a=mod(mirror(base,r.h,r.w)+noise(x,y),4);
  return state.singleEdits.has(i)?state.singleEdits.get(i):a;
 });
 paint();
}
function reset(){state.linkedEdits.clear();state.singleEdits.clear();state.undo=[];rebuild();}
function paint(){
 let [dark,light]=palettes[state.palette];if(state.invert)[dark,light]=[light,dark];
 const s=canvas.width/state.n;ctx.fillStyle=light;ctx.fillRect(0,0,canvas.width,canvas.height);ctx.fillStyle=dark;
 for(let y=0;y<state.n;y++)for(let x=0;x<state.n;x++){
  const a=state.tiles[id(x,y)],px=x*s,py=y*s;
  ctx.beginPath();switch(a){
  case 0:ctx.moveTo(px,py);ctx.lineTo(px+s,py);ctx.lineTo(px,py+s);break;
  case 1:ctx.moveTo(px+s,py);ctx.lineTo(px+s,py+s);ctx.lineTo(px,py);break;
  case 2:ctx.moveTo(px+s,py+s);ctx.lineTo(px,py+s);ctx.lineTo(px+s,py);break;
  default:ctx.moveTo(px,py+s);ctx.lineTo(px,py);ctx.lineTo(px+s,py+s);break;
  }ctx.closePath();ctx.fill();
 }
 if(state.grid){ctx.strokeStyle=state.palette===0?'#858585':'#66757b';ctx.lineWidth=1;ctx.beginPath();for(let j=1;j<state.n;j++){const t=j*s;ctx.moveTo(t,0);ctx.lineTo(t,canvas.height);ctx.moveTo(0,t);ctx.lineTo(canvas.width,t)}ctx.stroke()}
 $('pattern-name').textContent=modes[state.mode];$('count').textContent=`${state.n*state.n} tiles · ${state.chaos}% chaos`;
}
function updateUI(){
 document.querySelectorAll('[data-mode]').forEach(b=>{const a=b.dataset.mode===state.mode;b.classList.toggle('active',a);b.setAttribute('aria-pressed',a)});
 document.querySelectorAll('[data-palette]').forEach(b=>{const a=+b.dataset.palette===state.palette;b.classList.toggle('active',a);b.setAttribute('aria-pressed',a)});
 $('size').value=state.n;$('size-output').textContent=`${state.n} × ${state.n}`;
 $('chaos').value=state.chaos;$('chaos-output').textContent=`${state.chaos}% chaos`;
 $('grid').checked=state.grid;$('linked').checked=state.linked;
 $('edit-hint').textContent=state.linked?'Tap a square: its linked partners update too.':'Tap a square: rotate only that tile.';
}
function message(s){$('status').textContent=s;}
function snapshot(){state.undo.push({linkedEdits:new Map(state.linkedEdits),singleEdits:new Map(state.singleEdits)});if(state.undo.length>30)state.undo.shift()}
function rotate(x,y){
 snapshot();const i=id(x,y),next=mod(state.tiles[i]+1,4);
 if(state.linked){
  const r=ref(x,y);
  const canonical=mirror(mod(next-noise(x,y),4),r.h,r.w);
  state.linkedEdits.set(pointKey(r.u,r.v),canonical);
  const linkedIndices=[id(x,y),id(state.n-1-x,y),id(x,state.n-1-y),id(state.n-1-x,state.n-1-y)];
  for(const j of linkedIndices)state.singleEdits.delete(j);
  rebuild();message('Updated this tile and three linked positions.');
 }else{
  state.singleEdits.set(i,next);rebuild();message('Rotated one tile. Linked pattern unchanged.');
 }
}
function encode(){
 const d={v:2,n:state.n,mode:state.mode,seed:state.seed,palette:state.palette,invert:state.invert,grid:state.grid,chaos:state.chaos,linked:state.linked,linkedEdits:[...state.linkedEdits],singleEdits:[...state.singleEdits]};
 return '#design='+encodeURIComponent(btoa(JSON.stringify(d)));
}
function restore(){
 try{
  if(!location.hash.startsWith('#design='))return false;
  const decoded=atob(decodeURIComponent(location.hash.slice(8)));
  if(decoded.startsWith('{')){
   const d=JSON.parse(decoded);if(d.v!==2||![8,12,16,20,24,28,32].includes(d.n)||!modes[d.mode])return false;
   state.n=d.n;state.mode=d.mode;state.seed=Number.isSafeInteger(d.seed)?d.seed:93;
   state.palette=Number.isInteger(d.palette)&&d.palette>=0&&d.palette<palettes.length?d.palette:0;
   state.invert=Boolean(d.invert);state.grid=Boolean(d.grid);state.linked=Boolean(d.linked);
   state.chaos=Number.isInteger(d.chaos)?Math.min(100,Math.max(0,d.chaos)):20;
   state.linkedEdits=new Map(Array.isArray(d.linkedEdits)?d.linkedEdits.filter(e=>Array.isArray(e)&&/^\d+,\d+$/.test(e[0])&&Number.isInteger(e[1])&&e[1]>=0&&e[1]<4).slice(0,state.n*state.n):[]);
   state.singleEdits=new Map(Array.isArray(d.singleEdits)?d.singleEdits.filter(e=>Array.isArray(e)&&Number.isInteger(e[0])&&e[0]>=0&&e[0]<state.n*state.n&&Number.isInteger(e[1])&&e[1]>=0&&e[1]<4).slice(0,state.n*state.n):[]);
   state.undo=[];return true;
  }
  // Older prototype links retain their exact design and can be edited further.
  const a=decoded.split('~'),n=+a[0];if(![8,12,16,20,24,28,32].includes(n)||!modes[a[1]]||!a[5]||a[5].length!==n*n||/[^0-3]/.test(a[5]))return false;
  state.n=n;state.mode=a[1];state.seed=+a[2]||93;state.palette=+a[3]||0;state.invert=a[4]==='1';state.chaos=20;state.linked=false;
  state.singleEdits=new Map([...a[5]].map((v,i)=>[i,+v]));return true;
 }catch{return false;}
}
canvas.addEventListener('pointerdown',e=>{const r=canvas.getBoundingClientRect();const x=Math.min(state.n-1,Math.max(0,Math.floor((e.clientX-r.left)/r.width*state.n))),y=Math.min(state.n-1,Math.max(0,Math.floor((e.clientY-r.top)/r.height*state.n)));rotate(x,y)});
canvas.setAttribute('tabindex','0');canvas.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();rotate(Math.floor(state.n/2),Math.floor(state.n/2))}});
$('presets').addEventListener('click',e=>{const b=e.target.closest('button[data-mode]');if(!b)return;state.mode=b.dataset.mode;state.seed++;updateUI();reset();message(`New ${modes[state.mode].toLowerCase()} pattern. Manual edits cleared.`)});
$('size').addEventListener('input',e=>{state.n=+e.target.value;updateUI();reset();message(`Grid changed to ${state.n} × ${state.n}.`) });
$('chaos').addEventListener('input',e=>{state.chaos=+e.target.value;updateUI();rebuild();message(state.chaos===0?'Perfect four-way reflections.':state.chaos===100?'Maximum independent rotation.':`${state.chaos}% chaos: the pattern is gradually breaking symmetry.`)});
$('palettes').addEventListener('click',e=>{const b=e.target.closest('button[data-palette]');if(!b)return;state.palette=+b.dataset.palette;updateUI();paint();message('Colour palette changed.')});
$('grid').addEventListener('change',e=>{state.grid=e.target.checked;paint()});
$('linked').addEventListener('change',e=>{state.linked=e.target.checked;updateUI();message(state.linked?'Linked editing: four mirrored positions will respond.':'Free editing: only the tapped square will rotate.')});
$('reroll').addEventListener('click',()=>{state.seed++;reset();message('Fresh arrangement using the current rule and structure setting.')});
$('invert').addEventListener('click',()=>{state.invert=!state.invert;paint();message('Colours inverted.')});
$('clear-edits').addEventListener('click',()=>{reset();message('Manual edits cleared; rule and chaos setting retained.')});
$('undo').addEventListener('click',()=>{if(state.undo.length){const s=state.undo.pop();state.linkedEdits=s.linkedEdits;state.singleEdits=s.singleEdits;rebuild();message('Last tile edit undone.')}else message('No tile edits to undo yet.')});
$('save').addEventListener('click',()=>{const url=canvas.toDataURL('image/png');$('export-preview').src=url;$('export-link').href=url;$('export-link').download=`coffeetableviz-truchet-${state.n}x${state.n}.png`;$('export-panel').hidden=false;if(!/iPhone|iPad|iPod/i.test(navigator.userAgent))$('export-link').click();message('Your 1,024 × 1,024 PNG is ready. Save it using the link or preview below.')});
$('share').addEventListener('click',async()=>{const u=location.href.split('#')[0]+encode();try{await navigator.clipboard.writeText(u);message('Design link copied. Links work once this studio is hosted on coffeetableviz.com.')}catch{const t=document.createElement('textarea');t.value=u;document.body.append(t);t.select();document.execCommand('copy');t.remove();message('Design link prepared for copying.')}});
const restored=restore();updateUI();rebuild();if(restored)message('Shared design restored.');
})();
