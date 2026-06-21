import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
records=json.load(open(os.path.join(HERE,'records.json')))
hints={"Star Wars: The Themes (Episodes I–VI)":""}
for r in records:
    if r['title'] in hints: r['q']=hints[r['title']]
data=json.dumps(records,ensure_ascii=False,separators=(',',':'))

CSS = r'''
  :root{--espresso:#1e150d;--espresso2:#2a1d11;--wood:#3a2917;--cream:#f3e6cc;--paper:#efe0c2;
    --ink:#2a1c0c;--dim:#b69b6f;--gold:#e9a81f;--orange:#d8631a;--rust:#a83118;--teal:#2c9c8e;--avocado:#7e8d36;}
  *{box-sizing:border-box}
  html,body{overflow-x:hidden}
  body{margin:0;color:var(--cream);padding-bottom:96px;
    background:radial-gradient(120% 80% at 50% -10%, #4a3315 0%, var(--espresso2) 45%, var(--espresso) 100%);
    font-family:'Oswald','Arial Narrow',sans-serif;font-weight:300;letter-spacing:.2px;}
  a{color:var(--gold)}
  .hero{position:relative;overflow:hidden;border-bottom:4px solid var(--gold);background:#241808}
  .hero::before{content:"";position:absolute;inset:-60% -10%;z-index:0;
    background:repeating-conic-gradient(from 0deg at 50% 38%, rgba(216,99,26,.30) 0 7deg, rgba(233,168,31,.10) 7deg 14deg);
    -webkit-mask:radial-gradient(60% 60% at 50% 38%, #000 35%, transparent 72%);mask:radial-gradient(60% 60% at 50% 38%, #000 35%, transparent 72%)}
  .hero-inner{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:26px 20px 22px;display:flex;align-items:center;gap:22px;flex-wrap:wrap}
  .deck{width:96px;height:96px;flex:0 0 auto;border-radius:50%;position:relative;background:#120c06;box-shadow:0 0 0 5px #0c0804,0 8px 26px rgba(0,0,0,.6)}
  .deck::before{content:"";position:absolute;inset:0;border-radius:50%;background:repeating-radial-gradient(circle at 50% 50%, #161009 0 2px, #221708 2px 4px);animation:spin 3.2s linear infinite}
  .deck::after{content:"";position:absolute;top:50%;left:50%;width:38%;height:38%;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,#2a1a05 0 16%, var(--orange) 16% 55%, var(--gold) 55% 100%);box-shadow:0 0 0 2px rgba(0,0,0,.45)}
  @keyframes spin{to{transform:rotate(360deg)}}
  .titles{flex:1 1 auto;min-width:240px}
  h1{margin:0;font-family:'Monoton',cursive;font-weight:400;letter-spacing:2px;color:var(--gold);font-size:clamp(30px,6vw,54px);line-height:1;text-shadow:3px 3px 0 var(--rust),6px 6px 0 rgba(0,0,0,.35)}
  .tag{font-family:'Pacifico',cursive;color:var(--cream);font-size:clamp(15px,2.4vw,22px);margin-top:8px;opacity:.95}
  .onair{display:inline-flex;align-items:center;gap:8px;margin-top:10px;font-weight:600;letter-spacing:3px;text-transform:uppercase;font-size:12px;background:#160d05;color:#ffd98a;padding:6px 12px;border:2px solid var(--gold);border-radius:6px}
  .onair .led{width:11px;height:11px;border-radius:50%;background:#ff3b30;box-shadow:0 0 8px #ff3b30;animation:blink 1.4s ease-in-out infinite}
  @keyframes blink{50%{opacity:.25}}
  .wrap{max-width:1180px;margin:0 auto;padding:22px 20px 40px}
  .stats{display:flex;flex-wrap:wrap;gap:12px;margin:6px 0 22px}
  .stat{background:linear-gradient(180deg,#2c2012,#241809);border:2px solid var(--wood);border-top-color:#5a431f;border-radius:10px;padding:10px 16px;min-width:100px;box-shadow:inset 0 1px 0 rgba(255,220,150,.08)}
  .stat b{display:block;font-weight:700;font-size:24px;color:var(--gold);line-height:1}
  .stat span{color:var(--dim);font-size:11px;text-transform:uppercase;letter-spacing:1.5px}
  .controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:20px}
  input[type=search],select{font-family:'Oswald';font-weight:400;color:var(--ink);background:var(--cream);border:2px solid var(--wood);border-radius:8px;padding:10px 12px;font-size:15px}
  input[type=search]{flex:1 1 200px;min-width:170px}
  input[type=search]::placeholder{color:#9c855c}
  .toggle{display:flex;border:2px solid var(--gold);border-radius:8px;overflow:hidden}
  .toggle button{font-family:'Oswald';font-weight:600;letter-spacing:1px;text-transform:uppercase;background:#241809;color:var(--dim);border:0;padding:10px 15px;font-size:13px;cursor:pointer}
  .toggle button.on{background:var(--gold);color:#241809}
  .needlebtn{font-family:'Oswald';font-weight:600;text-transform:uppercase;letter-spacing:1px;background:var(--orange);color:#fff;border:2px solid var(--rust);border-radius:8px;padding:10px 16px;cursor:pointer}
  .needlebtn:hover{filter:brightness(1.08)}
  .needlebtn.alt{background:#241809;color:var(--gold);border-color:var(--gold)}
  .needlebtn.alt.on{background:var(--gold);color:#241809}
  .gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:20px}
  .card{position:relative;background:var(--paper);border-radius:8px;padding:9px 9px 11px;border:1px solid #c9b489;box-shadow:0 6px 16px rgba(0,0,0,.45);overflow:visible;transition:transform .25s ease}
  .card:hover{transform:translateY(-4px);z-index:20}
  .card.featured{animation:pop 1.6s ease}
  @keyframes pop{0%{box-shadow:0 0 0 0 var(--gold)}30%{box-shadow:0 0 0 6px rgba(233,168,31,.7)}100%{box-shadow:0 6px 16px rgba(0,0,0,.45)}}
  .cov{position:relative;aspect-ratio:1/1;perspective:900px;cursor:pointer}
  .flip3d{position:absolute;inset:0;transform-style:preserve-3d;transition:transform .6s}
  .card.flipped .flip3d{transform:rotateY(180deg)}
  .face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border-radius:4px}
  .face.front{overflow:visible}
  .disc{position:absolute;top:0;left:0;width:100%;height:100%;border-radius:50%;background:#120c06;z-index:1;transition:transform .4s cubic-bezier(.2,.7,.2,1);box-shadow:0 6px 14px rgba(0,0,0,.5)}
  .disc::before{content:"";position:absolute;inset:0;border-radius:50%;background:repeating-radial-gradient(circle at 50% 50%, #15100a 0 2px, #241809 2px 4px)}
  .disc::after{content:"";position:absolute;top:50%;left:50%;width:34%;height:34%;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,#241606 0 13%, var(--orange) 13% 58%, var(--gold) 58% 100%)}
  .card:hover:not(.flipped) .disc{transform:translateX(46%) rotate(18deg)}
  .cov img{position:relative;z-index:2;width:100%;height:100%;object-fit:cover;display:block;border-radius:3px;box-shadow:0 2px 8px rgba(0,0,0,.4)}
  .favbtn{position:absolute;right:7px;top:7px;z-index:4;background:#241809cc;border:1px solid var(--gold);color:#9b835a;border-radius:50%;width:27px;height:27px;cursor:pointer;font-size:14px;line-height:1;padding:0}
  .favbtn.on{color:var(--gold);background:#3a2a0f}
  .face.back{transform:rotateY(180deg);background:#241809;color:var(--cream);overflow:hidden;display:flex;flex-direction:column;border:1px solid var(--wood)}
  .backhead{display:flex;justify-content:space-between;align-items:center;padding:6px 8px;border-bottom:1px solid var(--wood)}
  .playall{background:var(--gold);color:#241809;border:0;border-radius:5px;font-family:'Oswald';font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:1px;padding:4px 9px;cursor:pointer}
  .flipback{background:none;border:0;color:var(--cream);font-size:18px;cursor:pointer;line-height:1}
  .tracks{flex:1;overflow-y:auto;padding:4px}
  .trk{display:flex;align-items:center;gap:7px;width:100%;text-align:left;background:none;border:0;border-bottom:1px solid #382814;color:var(--cream);padding:6px 5px;cursor:pointer;font-family:'Oswald';font-size:12.5px}
  .trk:hover{background:#33240f}
  .trk .tn{color:var(--dim);width:18px;font-size:11px;flex:0 0 auto}
  .trk .tnm{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .trk .tpv{color:var(--gold);flex:0 0 auto}
  .notrk{padding:14px;color:var(--dim);font-size:13px;text-align:center}
  .backfoot{border-top:1px solid var(--wood);padding:7px 9px;display:flex;align-items:center;gap:8px}
  .backfoot label{color:var(--dim);text-transform:uppercase;letter-spacing:1px;font-size:10px}
  .valinput{width:78px;background:#120c06;border:1px solid var(--wood);color:var(--gold);border-radius:5px;padding:4px 6px;font-family:'Oswald';font-size:13px}
  .src{position:absolute;left:7px;top:7px;z-index:3;font-size:9px;font-weight:600;letter-spacing:1px;text-transform:uppercase;padding:2px 7px;border-radius:3px;background:#241809cc;color:#ffd98a;border:1px solid var(--gold)}
  .meta{padding:9px 3px 1px;color:var(--ink)}
  .a{font-weight:600;font-size:14px;line-height:1.2;color:#1f1407}
  .t{font-weight:400;font-size:12.5px;color:#6a5430;margin-top:2px}
  .cond{color:var(--rust);font-weight:600;font-size:11px;margin-top:4px;text-transform:uppercase;letter-spacing:.5px}
  .rowline{display:flex;justify-content:space-between;align-items:center;margin-top:7px;gap:6px}
  .y{color:#7a6238;font-size:12px;font-weight:500;flex:1}
  .valtag{color:#5f7a1e;font-weight:600;font-size:12px}
  .playbtn{background:var(--orange);color:#fff;border:0;border-radius:50%;width:26px;height:26px;cursor:pointer;font-size:11px;flex:0 0 auto}
  .playbtn:hover{background:var(--rust)}
  .pill{display:inline-block;font-size:10px;font-weight:600;letter-spacing:1px;text-transform:uppercase;padding:3px 9px;border-radius:999px;border:2px solid}
  .s-identified{color:#1f3d13;background:#bfe08a;border-color:#7e8d36}
  .s-tentative{color:#3d2c05;background:#f1c862;border-color:#c79318}
  .s-unidentified{color:#fff;background:#c0492c;border-color:#7e2a16}
  table{width:100%;border-collapse:collapse;font-weight:300;background:var(--paper);border-radius:8px;overflow:hidden}
  thead th{font-weight:600;text-transform:uppercase;letter-spacing:1px;font-size:12px;color:#241809;background:var(--gold);text-align:left;padding:10px;cursor:pointer;user-select:none}
  tbody td{padding:9px 10px;border-bottom:1px solid #d8c39a;color:var(--ink);vertical-align:middle}
  tbody tr:hover{background:#e7d4ad}
  td.thumb{width:50px}
  td.thumb img{width:42px;height:42px;object-fit:cover;border-radius:3px;display:block;box-shadow:0 1px 4px rgba(0,0,0,.4)}
  .title-cell .note{display:block;color:#7a6238;font-size:12px;font-style:italic;margin-top:2px}
  .title-cell .note.cond{color:var(--rust);font-style:normal;font-weight:600}
  td .artist{font-weight:600}
  .statsView .panel{background:var(--paper);color:var(--ink);border-radius:10px;padding:16px 18px;margin-bottom:16px;border:1px solid #c9b489}
  .panel h3{margin:0 0 12px;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;font-size:14px;color:#3a2a10}
  .bar-row{display:flex;align-items:center;gap:10px;margin:7px 0}
  .bar-row .lab{width:96px;font-size:13px;color:#4a3a1f;text-align:right;flex:0 0 auto}
  .bar-row .barwrap{flex:1;background:#e0cda3;border-radius:4px;overflow:hidden;height:18px}
  .bar-row .bar{height:100%;background:linear-gradient(90deg,var(--orange),var(--gold))}
  .bar-row .cnt{width:26px;font-size:12px;color:#4a3a1f;flex:0 0 auto}
  .factgrid{display:flex;gap:12px;flex-wrap:wrap}
  .fact{background:#241809;color:var(--cream);border-radius:8px;padding:10px 14px;min-width:118px}
  .fact span{color:var(--dim);font-size:11px;text-transform:uppercase;letter-spacing:1px}
  .fact b{display:block;color:var(--gold);font-size:16px;margin-top:2px}
  .empty{color:var(--dim);padding:36px;text-align:center;font-size:18px;font-family:'Pacifico',cursive}
  footer{color:var(--dim);font-size:12.5px;margin-top:30px;border-top:2px solid var(--wood);padding-top:16px;line-height:1.7}
  footer b{color:var(--gold)}
  .np{position:fixed;left:0;right:0;bottom:0;z-index:100;display:flex;align-items:center;gap:12px;padding:10px 16px;background:linear-gradient(180deg,#2c2012,#1a1206);border-top:3px solid var(--gold);box-shadow:0 -6px 20px rgba(0,0,0,.5)}
  .np-deck{position:relative;width:46px;height:46px;border-radius:50%;background:#120c06;flex:0 0 auto;box-shadow:0 0 0 3px #0c0804}
  .np-deck::before{content:"";position:absolute;inset:0;border-radius:50%;background:repeating-radial-gradient(circle,#161009 0 2px,#241708 2px 4px)}
  .np.playing .np-deck::before{animation:spin 2.4s linear infinite}
  .np-deck::after{content:"";position:absolute;top:50%;left:50%;width:36%;height:36%;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,#241606 0 16%,var(--gold) 16% 100%)}
  .np-arm{position:absolute;top:-5px;right:-3px;width:4px;height:28px;background:#cdb27a;border-radius:3px;transform-origin:top right;transform:rotate(-34deg);transition:transform .5s;z-index:3}
  .np.playing .np-arm{transform:rotate(-6deg)}
  .np-art{width:46px;height:46px;border-radius:4px;object-fit:cover;flex:0 0 auto;background:#120c06}
  .np-info{flex:0 0 auto;min-width:110px;max-width:30vw}
  #np-title{font-weight:600;color:var(--cream);font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  #np-artist{color:var(--dim);font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .np-btn{background:#3a2917;color:var(--cream);border:0;border-radius:6px;width:34px;height:34px;cursor:pointer;font-size:13px;flex:0 0 auto}
  #np-toggle{background:var(--gold);color:#241809;font-weight:700}
  .np-bar{flex:1 1 auto;height:8px;background:#1a1206;border:1px solid var(--wood);border-radius:6px;overflow:hidden;min-width:40px}
  #np-prog{height:100%;width:0;background:linear-gradient(90deg,var(--orange),var(--gold))}
  .hidden{display:none !important}
'''

JS = r'''
const RECORDS = __DATA__;
const galleryEl=document.getElementById('gallery'),tableWrap=document.getElementById('tableWrap'),tbody=document.getElementById('rows'),statsView=document.getElementById('statsView');
const qEl=document.getElementById('q'),statusEl=document.getElementById('status'),genreEl=document.getElementById('genre'),emptyEl=document.getElementById('empty');
let sortKey='artist',sortDir=1,view='gallery',favesOnly=false;
const CACHEV='2';
if(localStorage.getItem('vinylCacheV')!==CACHEV){localStorage.removeItem('vinylArt');localStorage.removeItem('vinylIds');localStorage.setItem('vinylCacheV',CACHEV);}
const ART=JSON.parse(localStorage.getItem('vinylArt')||'{}');
const IDS=JSON.parse(localStorage.getItem('vinylIds')||'{}');
const FAVS=JSON.parse(localStorage.getItem('vinylFavs')||'{}');
const VALUES=JSON.parse(localStorage.getItem('vinylValues')||'{}');
const TRACKS={};
const audio=new Audio();
let QUEUE=[],QPOS=-1;
function money(n){return '$'+(Math.round((+n||0)*100)/100).toLocaleString();}
function totalValue(){return Object.values(VALUES).reduce((a,b)=>a+(+b||0),0);}

function artQuery(r){
  if(r.q!==undefined) return r.q;
  if(r.status==='unidentified'||r.artist==='Unknown') return '';
  if(r.title.trim().startsWith('(')) return '';
  let t=r.title.replace(/\(.*?\)/g,' ').replace(/[“”"…]/g,' ').split('—')[0];
  return (r.artist+' '+t).replace(/\s+/g,' ').trim();
}
function jsonp(url){return new Promise((res,rej)=>{
  const cb='itc_'+Math.random().toString(36).slice(2),s=document.createElement('script');
  const to=setTimeout(()=>{cleanup();rej();},9000);
  function cleanup(){delete window[cb];s.remove();clearTimeout(to);}
  window[cb]=d=>{cleanup();res(d);}; s.onerror=()=>{cleanup();rej();};
  s.src=url+(url.includes('?')?'&':'?')+'callback='+cb; document.body.appendChild(s);
});}
async function searchAlbum(q){
  try{const d=await jsonp('https://itunes.apple.com/search?term='+encodeURIComponent(q)+'&entity=album&limit=1');
    if(d&&d.results&&d.results[0]){const x=d.results[0];
      return {art:x.artworkUrl100?x.artworkUrl100.replace('100x100bb','500x500bb'):null,id:x.collectionId};}
  }catch(e){} return null;
}
async function fetchTracks(id){
  try{const d=await jsonp('https://itunes.apple.com/lookup?id='+id+'&entity=song&limit=60');
    if(d&&d.results) return d.results.filter(x=>x.wrapperType==='track'&&x.previewUrl);
  }catch(e){} return [];
}
async function ensureTracks(r){
  const q=artQuery(r); if(!q) return null;
  let id=IDS[q];
  if(!id){const s=await searchAlbum(q); if(s&&s.id){id=IDS[q]=s.id; localStorage.setItem('vinylIds',JSON.stringify(IDS)); if(s.art&&!ART[q]){ART[q]=s.art;localStorage.setItem('vinylArt',JSON.stringify(ART));applyArt(q,s.art);}}}
  if(!id) return null;
  if(TRACKS[id]) return TRACKS[id];
  return (TRACKS[id]=await fetchTracks(id));
}
function applyArt(q,url){document.querySelectorAll('img[data-q="'+CSS.escape(q)+'"]').forEach(img=>{img.src=url;const c=img.closest('.cov');const t=c&&c.querySelector('.src');if(t)t.remove();});}
async function hydrate(){
  const queries=[...new Set(RECORDS.map(artQuery).filter(Boolean))];
  for(const q of queries){ if(ART[q]) applyArt(q,ART[q]); }
  const todo=queries.filter(q=>!ART[q]||!IDS[q]); let i=0;
  async function worker(){ while(i<todo.length){ const q=todo[i++];
    const s=await searchAlbum(q);
    if(s){ if(s.art){ART[q]=s.art;localStorage.setItem('vinylArt',JSON.stringify(ART));applyArt(q,s.art);}
           if(s.id){IDS[q]=s.id;localStorage.setItem('vinylIds',JSON.stringify(IDS));} }
    await new Promise(r=>setTimeout(r,250)); } }
  await Promise.all(Array.from({length:4},worker));
}

/* ---- audio / queue / now playing ---- */
const np=document.getElementById('np'),npArt=document.getElementById('np-art'),npTitle=document.getElementById('np-title'),npArtist=document.getElementById('np-artist'),npToggle=document.getElementById('np-toggle'),npProg=document.getElementById('np-prog');
function playPreview(url,artist,title,art){
  if(!url)return; audio.src=url; audio.play().catch(()=>{});
  np.classList.remove('hidden'); np.classList.add('playing');
  npToggle.textContent='❚❚'; npTitle.textContent=title||''; npArtist.textContent=artist||''; if(art)npArt.src=art;
}
function playQueue(list,start,art,artist){
  QUEUE=list.map(t=>({url:t.previewUrl,title:t.trackName,artist:artist,art:art}));
  QPOS=Math.min(Math.max(0,start),QUEUE.length-1);
  if(QUEUE[QPOS]) playPreview(QUEUE[QPOS].url,QUEUE[QPOS].artist,QUEUE[QPOS].title,QUEUE[QPOS].art);
}
function advance(d){const n=QPOS+d; if(n<0||n>=QUEUE.length)return; QPOS=n; const it=QUEUE[QPOS]; playPreview(it.url,it.artist,it.title,it.art);}
audio.addEventListener('timeupdate',()=>{ if(audio.duration) npProg.style.width=(audio.currentTime/audio.duration*100)+'%';});
audio.addEventListener('ended',()=>{ if(QPOS>-1&&QPOS<QUEUE.length-1){advance(1);} else {np.classList.remove('playing');npToggle.textContent='▶';}});
npToggle.addEventListener('click',()=>{ if(audio.paused){audio.play();np.classList.add('playing');npToggle.textContent='❚❚';} else {audio.pause();np.classList.remove('playing');npToggle.textContent='▶';}});
document.getElementById('np-prev').addEventListener('click',()=>advance(-1));
document.getElementById('np-next').addEventListener('click',()=>advance(1));
document.getElementById('np-close').addEventListener('click',()=>{audio.pause();np.classList.add('hidden');np.classList.remove('playing');});

/* ---- render ---- */
[...new Set(RECORDS.map(r=>r.genre))].sort().forEach(g=>{const o=document.createElement('option');o.value=g;o.textContent=g;genreEl.appendChild(o);});
function stats(){const by=s=>RECORDS.filter(r=>r.status===s).length;
  document.getElementById('statbar').innerHTML=`
    <div class="stat"><b>${RECORDS.length}</b><span>Records</span></div>
    <div class="stat"><b>${new Set(RECORDS.map(r=>r.artist)).size}</b><span>Artists</span></div>
    <div class="stat"><b>${Object.keys(FAVS).length}</b><span>Faves</span></div>
    <div class="stat"><b>${money(totalValue())}</b><span>Est. value</span></div>`;}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function imgFor(r){const q=artQuery(r);const src=(q&&ART[q])?ART[q]:r.img;const dq=q?` data-q="${esc(q)}"`:'';const badge=((q&&!ART[q])||!q)?'<span class="src">photo</span>':'';return {src,dq,badge,q};}
function filtered(){const q=qEl.value.trim().toLowerCase(),fs=statusEl.value,fg=genreEl.value;
  return RECORDS.map((r,i)=>({...r,i})).filter(r=>{
    if(favesOnly&&!FAVS[r.i])return false;
    if(fs&&r.status!==fs)return false; if(fg&&r.genre!==fg)return false;
    if(q&&!(`${r.artist} ${r.title} ${r.genre}`.toLowerCase().includes(q)))return false; return true;});}
function sortRows(rows){return rows.sort((a,b)=>{let x=a[sortKey],y=b[sortKey];if(sortKey==='year'){x=x||0;y=y||0;return (x-y)*sortDir;}return String(x).localeCompare(String(y))*sortDir;});}
function render(){
  let rows=filtered(); emptyEl.classList.toggle('hidden',rows.length>0||view==='stats');
  if(view==='gallery'){
    rows.sort((a,b)=>String(a.artist).localeCompare(String(b.artist)));
    galleryEl.innerHTML=rows.map(r=>{const m=imgFor(r);const canPlay=!!m.q;const v=VALUES[r.i];return `
      <div class="card" data-i="${r.i}" title="${esc(r.note||'')}">
        <div class="cov">
          <div class="flip3d">
            <div class="face front"><button class="favbtn${FAVS[r.i]?' on':''}" data-fav="${r.i}">${FAVS[r.i]?'★':'☆'}</button><span class="disc"></span>${m.badge}<img loading="lazy"${m.dq} src="${m.src}" alt="${esc(r.artist+' – '+r.title)}"></div>
            <div class="face back">
              <div class="backhead">${canPlay?'<button class="playall">▶ Play all</button>':'<span></span>'}<button class="flipback" aria-label="flip back">↩</button></div>
              <div class="tracks">${canPlay?'<div class="notrk">Loading…</div>':'<div class="notrk">No digital preview for this pressing.</div>'}</div>
              <div class="backfoot"><label>Est. value</label><input class="valinput" type="number" min="0" step="1" inputmode="decimal" data-val="${r.i}" value="${v!=null?v:''}" placeholder="—"></div>
            </div>
          </div>
        </div>
        <div class="meta"><div class="a">${esc(r.artist)}</div><div class="t">${esc(r.title)}</div>
          ${r.condition?`<div class="cond">⚠ ${esc(r.condition)}</div>`:''}
          <div class="rowline"><span class="y">${r.year||'—'}</span><span class="valtag" data-vt="${r.i}">${v!=null?money(v):''}</span>${canPlay?'<button class="playbtn" title="Play album">▶</button>':''}<span class="pill s-${r.status}">${r.status}</span></div></div>
      </div>`;}).join('');
  }else if(view==='table'){
    sortRows(rows);
    tbody.innerHTML=rows.map(r=>{const m=imgFor(r);return `
      <tr title="${esc(r.note||'')}"><td class="thumb"><img loading="lazy"${m.dq} src="${m.src}" alt=""></td>
        <td class="artist">${esc(r.artist)}</td>
        <td class="title-cell">${esc(r.title)}${r.note?`<span class="note">${esc(r.note)}</span>`:''}${r.condition?`<span class="note cond">⚠ ${esc(r.condition)}</span>`:''}</td>
        <td>${r.year||'—'}</td><td>${esc(r.genre)}</td>
        <td><span class="pill s-${r.status}">${r.status}</span></td></tr>`;}).join('');
  }else{ renderStats(); }
}
function renderStats(){
  const yrs=RECORDS.filter(r=>r.year);
  const dec={};yrs.forEach(r=>{const d=Math.floor(r.year/10)*10;dec[d]=(dec[d]||0)+1;});
  const gen={};RECORDS.forEach(r=>gen[r.genre]=(gen[r.genre]||0)+1);
  const art={};RECORDS.forEach(r=>art[r.artist]=(art[r.artist]||0)+1);
  const top=Object.entries(art).sort((a,b)=>b[1]-a[1]).slice(0,5);
  const oldest=yrs.reduce((m,r)=>r.year<m.year?r:m),newest=yrs.reduce((m,r)=>r.year>m.year?r:m);
  function bars(obj,keys,w){const mx=Math.max(...keys.map(k=>obj[k]));return keys.map(k=>`<div class="bar-row"><div class="lab"${w?` style="width:${w}px"`:''}>${esc(String(k))}</div><div class="barwrap"><div class="bar" style="width:${obj[k]/mx*100}%"></div></div><div class="cnt">${obj[k]}</div></div>`).join('');}
  const decObj={};Object.keys(dec).forEach(d=>decObj[d+'s']=dec[d]);
  const decKeys=Object.keys(dec).sort((a,b)=>a-b).map(d=>d+'s');
  const genKeys=Object.keys(gen).sort((a,b)=>gen[b]-gen[a]);
  const topObj={};top.forEach(([a,c])=>topObj[a]=c);
  statsView.innerHTML=`
    <div class="panel"><h3>By decade</h3>${bars(decObj,decKeys)}</div>
    <div class="panel"><h3>By genre</h3>${bars(gen,genKeys)}</div>
    <div class="panel"><h3>Most collected</h3>${bars(topObj,top.map(t=>t[0]),150)}</div>
    <div class="panel"><h3>Crate facts</h3><div class="factgrid">
      <div class="fact"><span>Oldest</span><b>${oldest.year}</b>${esc(oldest.artist)}</div>
      <div class="fact"><span>Newest</span><b>${newest.year}</b>${esc(newest.artist)}</div>
      <div class="fact"><span>Est. value</span><b>${money(totalValue())}</b>${Object.keys(VALUES).length} priced</div>
      <div class="fact"><span>Favorites</span><b>${Object.keys(FAVS).length}</b>starred</div>
      <div class="fact"><span>Span</span><b>${newest.year-oldest.year} yrs</b>of music</div>
    </div></div>`;
}
function setView(v){view=v;
  document.getElementById('vGallery').classList.toggle('on',v==='gallery');
  document.getElementById('vTable').classList.toggle('on',v==='table');
  document.getElementById('vStats').classList.toggle('on',v==='stats');
  galleryEl.classList.toggle('hidden',v!=='gallery');
  tableWrap.classList.toggle('hidden',v!=='table');
  statsView.classList.toggle('hidden',v!=='stats');
  render();}

/* ---- card interactions ---- */
async function openCard(card,autoplay){
  const r=RECORDS[+card.dataset.i]; card.classList.add('flipped');
  const tEl=card.querySelector('.tracks');
  if(tEl&&!tEl.dataset.loaded&&artQuery(r)){tEl.dataset.loaded='1';
    const list=await ensureTracks(r);
    tEl.innerHTML=(list&&list.length)?list.map((t,n)=>`<button class="trk" data-idx="${n}"><span class="tn">${t.trackNumber||n+1}</span><span class="tnm">${esc(t.trackName)}</span><span class="tpv">▶</span></button>`).join(''):'<div class="notrk">No digital preview for this pressing.</div>';
  }
  if(autoplay){const list=await ensureTracks(r);const img=card.querySelector('.cov img');
    if(list&&list.length)playQueue(list,0,img&&img.src,r.artist);}
}
async function playRecord(card,from){const r=RECORDS[+card.dataset.i];const list=await ensureTracks(r);const img=card.querySelector('.cov img');
  if(list&&list.length)playQueue(list,from||0,img&&img.src,r.artist);}
galleryEl.addEventListener('click',e=>{
  const fav=e.target.closest('.favbtn'); if(fav){const i=+fav.dataset.fav; if(FAVS[i])delete FAVS[i];else FAVS[i]=1; localStorage.setItem('vinylFavs',JSON.stringify(FAVS)); fav.classList.toggle('on');fav.textContent=FAVS[i]?'★':'☆'; stats(); if(favesOnly)render(); return;}
  const back=e.target.closest('.flipback'); if(back){back.closest('.card').classList.remove('flipped');return;}
  const pa=e.target.closest('.playall'); if(pa){playRecord(pa.closest('.card'),0);return;}
  const trk=e.target.closest('.trk'); if(trk){playRecord(trk.closest('.card'),+trk.dataset.idx);return;}
  const pb=e.target.closest('.playbtn'); if(pb){playRecord(pb.closest('.card'),0);return;}
  if(e.target.closest('.backfoot'))return;
  const cov=e.target.closest('.cov'); if(cov){const card=cov.closest('.card'); if(!card.classList.contains('flipped'))openCard(card,false);}
});
galleryEl.addEventListener('input',e=>{const vi=e.target.closest('.valinput'); if(!vi)return;
  const i=+vi.dataset.val,v=parseFloat(vi.value);
  if(isNaN(v))delete VALUES[i];else VALUES[i]=v;
  localStorage.setItem('vinylValues',JSON.stringify(VALUES));
  const tag=document.querySelector('.valtag[data-vt="'+i+'"]'); if(tag)tag.textContent=isNaN(v)?'':money(v);
  stats();});
function dropNeedle(){
  const pool=filtered().filter(r=>artQuery(r)); if(!pool.length)return;
  if(view!=='gallery')setView('gallery');
  const r=pool[Math.floor(Math.random()*pool.length)];
  setTimeout(()=>{const card=galleryEl.querySelector('.card[data-i="'+r.i+'"]'); if(!card)return;
    card.scrollIntoView({behavior:'smooth',block:'center'});
    card.classList.add('featured');setTimeout(()=>card.classList.remove('featured'),1600);
    openCard(card,true);},80);
}
document.querySelectorAll('thead th').forEach(th=>{if(!th.dataset.k)return;th.addEventListener('click',()=>{const k=th.dataset.k;if(k===sortKey)sortDir*=-1;else{sortKey=k;sortDir=1;}render();});});
qEl.addEventListener('input',render);statusEl.addEventListener('change',render);genreEl.addEventListener('change',render);
document.getElementById('vGallery').addEventListener('click',()=>setView('gallery'));
document.getElementById('vTable').addEventListener('click',()=>setView('table'));
document.getElementById('vStats').addEventListener('click',()=>setView('stats'));
document.getElementById('needle').addEventListener('click',dropNeedle);
document.getElementById('faves').addEventListener('click',function(){favesOnly=!favesOnly;this.classList.toggle('on',favesOnly);render();});
stats();render();hydrate();
'''

HTML = '''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>The Wax Stacks — Vinyl Inventory</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Monoton&family=Pacifico&family=Oswald:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>'''+CSS+'''</style></head><body>
<header class="hero"><div class="hero-inner">
  <div class="deck" aria-hidden="true"></div>
  <div class="titles"><h1>The Wax Stacks</h1>
    <div class="tag">spinnin&rsquo; the whole collection &mdash; dusty grooves &amp; gold</div>
    <span class="onair"><span class="led"></span> On Air</span></div>
</div></header>
<div class="wrap">
  <div class="stats" id="statbar"></div>
  <div class="controls">
    <input type="search" id="q" placeholder="Search the crate&hellip;">
    <select id="status"><option value="">All statuses</option><option value="identified">Identified</option><option value="tentative">Tentative</option><option value="unidentified">Unidentified</option></select>
    <select id="genre"><option value="">All genres</option></select>
    <button id="faves" class="needlebtn alt">&#9733; Faves</button>
    <div class="toggle"><button id="vGallery" class="on">Sleeves</button><button id="vTable">List</button><button id="vStats">Stats</button></div>
    <button id="needle" class="needlebtn">&#127922; Drop the needle</button>
  </div>
  <div id="gallery" class="gallery"></div>
  <table id="tableWrap" class="hidden"><thead><tr><th></th><th data-k="artist">Artist</th><th data-k="title">Title</th><th data-k="year">Year</th><th data-k="genre">Genre</th><th data-k="status">Status</th></tr></thead><tbody id="rows"></tbody></table>
  <div id="statsView" class="statsView hidden"></div>
  <div class="empty hidden" id="empty">Nothin&rsquo; in this crate&hellip;</div>
  <footer><b>Liner notes:</b> click a sleeve to flip it for the tracklist, &#9658; / Play all to spin the whole side
  (auto-advances), &#9733; to favorite, and type an <em>Est. value</em> on the back to track worth. <b>Drop the needle</b>
  for a random spin. Art &amp; audio stream from the iTunes catalog; rare pressings ride on photo scans. Your faves,
  values &amp; cached art live in this browser only.</footer>
</div>
<div id="np" class="np hidden">
  <div class="np-deck"><span class="np-arm"></span></div>
  <img id="np-art" alt=""><div class="np-info"><div id="np-title"></div><div id="np-artist"></div></div>
  <button id="np-prev" class="np-btn">&#9198;</button>
  <button id="np-toggle" class="np-btn">&#9658;</button>
  <button id="np-next" class="np-btn">&#9197;</button>
  <div class="np-bar"><div id="np-prog"></div></div>
  <button id="np-close" class="np-btn">&#10005;</button>
</div>
<script>'''+JS.replace('__DATA__',data)+'''</script></body></html>'''

open(os.path.join(HERE,'..','vinyl-inventory.html'),'w').write(HTML)
print('ok bytes',len(HTML))
