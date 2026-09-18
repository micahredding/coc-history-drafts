<script>
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  /* The addendum's plate gallery shows the SAME figures as the telling.
     Cloning the node keeps ONE copy of each base64 payload in the file — duplicating the
     markup would have added ~930 KB to a deck people open on a phone. */
  [].slice.call(document.querySelectorAll('[data-mirror]')).forEach(function(ph){
    var src=document.getElementById(ph.getAttribute('data-mirror'));
    if(!src){return}
    var c=src.cloneNode(true);
    c.removeAttribute('id');
    [].slice.call(c.querySelectorAll('[id]')).forEach(function(e){e.removeAttribute('id')});
    ph.parentNode.replaceChild(c,ph);
  });
  var bar=document.getElementById('bar'),count=document.getElementById('count'),hint=document.getElementById('hint');
  var strip=document.getElementById('strip'),modeEl=document.getElementById('mode'),pres=document.getElementById('pres');
  var q=new URLSearchParams(location.search);
  var LS={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
  var isPrev=q.has('preview'),isPres=q.has('presenter');
  if(isPrev||isPres)LS.set=function(){};  /* only the main window owns the shared state */
  var cur=0,interacted=false;
  function isPresent(){return document.body.classList.contains('present')}
  function fragsOf(i){var a=[].slice.call(slides[i].querySelectorAll('.frag')).filter(function(f){return !f.classList.contains('wp')&&!(isPresent()&&f.classList.contains('nt'))});a.sort(function(x,y){return (+(x.getAttribute('data-o')||0))-(+(y.getAttribute('data-o')||0))});return a}
  /* a .wp element (an attribution) is never its own step — it reveals with the frag above it */
  function syncWP(i){[].slice.call(slides[i].querySelectorAll('.wp')).forEach(function(w){
    var p=w.previousElementSibling,t=null;
    while(p){if(p.classList.contains('frag')&&!p.classList.contains('wp')&&!(isPresent()&&p.classList.contains('nt'))){t=p;break}p=p.previousElementSibling}
    w.classList.toggle('on',t?t.classList.contains('on'):true)})}
  function totalSteps(){return slides.reduce(function(t,s,i){return t+1+fragsOf(i).length},0)}
  function stepsBefore(i){var t=0;for(var k=0;k<i;k++)t+=1+fragsOf(k).length;return t}
  function shownFrags(i){return fragsOf(i).filter(function(f){return f.classList.contains('on')}).length}
  function notesOf(i){var a=slides[i].querySelector('aside.notes');return a?a.innerHTML:''}
  function titleOf(i){var e=slides[i].querySelector('h1,h2,h3,.eyebrow');return e?e.textContent.replace(/\s+/g,' ').trim():'—'}
  function render(){
    syncWP(cur);
    slides.forEach(function(s,i){s.classList.toggle('on',i===cur)});
    count.textContent=(cur+1)+' / '+slides.length;
    bar.style.width=((stepsBefore(cur)+1+shownFrags(cur))/totalSteps()*100)+'%';
    strip.innerHTML='<i>'+(cur+1)+'</i> &nbsp; '+notesOf(cur);
    LS.set('w1cur',String(cur));
    try{history.replaceState(null,'',location.search+'#'+(cur+1))}catch(e){}
  }
  function setMode(m){
    document.body.classList.toggle('present',m==='present');LS.set('w1mode',m);
    modeEl.textContent=(m==='present')?'present':'read';render();
  }
  function setStrip(on){document.body.classList.toggle('strip',!!on);LS.set('w1strip',on?'1':'0')}
  function next(){
    interacted||fadeHint();
    var fr=fragsOf(cur);
    for(var i=0;i<fr.length;i++){if(!fr[i].classList.contains('on')){fr[i].classList.add('on');render();return}}
    if(cur<slides.length-1){cur++;fragsOf(cur).forEach(function(f){f.classList.remove('on')});render()}
  }
  function prev(){
    interacted||fadeHint();
    var fr=fragsOf(cur);
    for(var i=fr.length-1;i>=0;i--){if(fr[i].classList.contains('on')){fr[i].classList.remove('on');render();return}}
    if(cur>0){cur--;fragsOf(cur).forEach(function(f){f.classList.add('on')});render()}
  }
  function goto(i,built){
    cur=Math.max(0,Math.min(slides.length-1,i));
    fragsOf(cur).forEach(function(f){f.classList.toggle('on',!!built)});render();
  }
  function fadeHint(){interacted=true;hint.classList.add('gone')}
  function openPresenter(){
    var base=location.href.split(/[?#]/)[0];
    window.open(base+'?presenter=1','w1presenter','width=960,height=640');
  }
  function sharedCur(){var c=parseInt(LS.get('w1cur')||'0',10);if(isNaN(c))c=0;return Math.max(0,Math.min(slides.length-1,c))}
  /* ---- preview pane (?preview=1): renders the NEXT slide, follows the main window ---- */
  if(isPrev){
    document.body.classList.add('preview');
    var pvS=-1,pvM='',pvPushed=false;
    function pvApply(c,m){
      var n=Math.min(slides.length-1,Math.max(0,c)+1);
      if(n!==pvS||m!==pvM){pvS=n;pvM=m;
        document.body.classList.toggle('present',m==='present');goto(n,true)}
    }
    /* the presenter window pushes state in: an embedded frame cannot rely on shared
       storage (Chrome partitions it for embedded documents), so this is the real channel */
    window.addEventListener('message',function(e){
      var d=e.data;if(d&&d.w1){pvPushed=true;pvApply(d.cur,d.mode||'read')}
    });
    function pvTick(){if(!pvPushed)pvApply(sharedCur(),LS.get('w1mode')||'read')}
    pvTick();setInterval(pvTick,200);window.addEventListener('storage',pvTick);
    return;
  }
  /* ---- presenter window (?presenter=1): notes + a live picture of the next slide ---- */
  if(isPres){
    document.body.classList.add('presenter');
    var pbase=location.href.split(/[?#]/)[0];
    pres.innerHTML='<div class=pcol><div class=pn id=ppn></div><div class=pt id=ppt></div>'+
      '<div class=pnotes id=ppnotes></div></div>'+
      '<div class=pside><div class=plabel id=pplabel>NEXT</div>'+
      '<div class=pwrap id=ppwrap><iframe id=ppif src="'+pbase+'?preview=1"></iframe></div>'+
      '<div class=pnexttitle id=ppnt></div>'+
      '<div class=pkeys>arrows / space advance the deck from here too</div></div>';
    var ppif=document.getElementById('ppif'),ppwrap=document.getElementById('ppwrap');
    function pfit(){ppif.style.transform='scale('+(ppwrap.clientWidth/1920)+')'}
    pfit();window.addEventListener('resize',pfit);setTimeout(pfit,300);
    function ppush(){try{ppif.contentWindow&&ppif.contentWindow.postMessage(
      {w1:1,cur:sharedCur(),mode:LS.get('w1mode')||'read'},'*')}catch(e){}}
    ppif.addEventListener('load',ppush);
    var last=-1;
    function tick(){
      var c=sharedCur();ppush();
      if(c!==last){last=c;
        var end=(c+1>=slides.length);
        document.getElementById('ppn').textContent=(c+1)+' / '+slides.length;
        document.getElementById('ppt').textContent=titleOf(c);
        document.getElementById('ppnotes').innerHTML=notesOf(c);
        document.getElementById('pplabel').textContent=end?'END OF DECK':'NEXT';
        ppwrap.style.visibility=end?'hidden':'visible';
        document.getElementById('ppnt').textContent=end?'':((c+2)+' · '+titleOf(c+1));
      }
    }
    tick();setInterval(tick,200);window.addEventListener('storage',tick);
    var seq=0;
    function cmd(d){seq++;try{localStorage.setItem('w1cmd',Date.now()+':'+seq+':'+d)}catch(e){}}
    document.addEventListener('keydown',function(e){
      if(e.metaKey||e.ctrlKey||e.altKey)return;
      switch(e.key){
        case 'ArrowRight':case 'ArrowDown':case ' ':case 'PageDown':e.preventDefault();cmd(1);break;
        case 'ArrowLeft':case 'ArrowUp':case 'Backspace':case 'PageUp':e.preventDefault();cmd(-1);break;
        case 'f':case 'F':
          if(document.fullscreenElement)document.exitFullscreen&&document.exitFullscreen();
          else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();
          break;
      }
    });
    return;
  }
  document.addEventListener('keydown',function(e){
    if(e.metaKey||e.ctrlKey||e.altKey)return;
    switch(e.key){
      case 'ArrowRight':case 'ArrowDown':case ' ':case 'PageDown':e.preventDefault();next();break;
      case 'ArrowLeft':case 'ArrowUp':case 'Backspace':case 'PageUp':e.preventDefault();prev();break;
      case 'Home':goto(0,false);break;
      case 'End':goto(slides.length-1,true);break;
      case 'n':case 'N':setMode(isPresent()?'read':'present');break;
      case 's':case 'S':setStrip(!document.body.classList.contains('strip'));break;
      case 'p':case 'P':openPresenter();break;
      case 'f':case 'F':
        if(document.fullscreenElement)document.exitFullscreen&&document.exitFullscreen();
        else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();
        break;
    }
  });
  document.addEventListener('click',function(e){if(e.target.closest('#strip'))return;(e.clientX<innerWidth/5)?prev():next()});
  var tx=null;
  document.addEventListener('touchstart',function(e){tx=e.touches[0].clientX},{passive:true});
  document.addEventListener('touchend',function(e){
    if(tx==null)return;var dx=e.changedTouches[0].clientX-tx;tx=null;
    if(dx<-40)next();else if(dx>40)prev();
  },{passive:true});
  var h=parseInt((location.hash||'').replace('#',''),10);
  if(h>=1&&h<=slides.length)cur=h-1;
  var lastCmd=LS.get('w1cmd')||'';
  setInterval(function(){
    var v=LS.get('w1cmd')||'';
    if(v&&v!==lastCmd){lastCmd=v;(v.slice(-2)==='-1')?prev():next()}
  },200);
  setStrip((LS.get('w1strip')||'0')==='1');
  setMode(q.get('mode')||LS.get('w1mode')||'read');
  fragsOf(cur).forEach(function(f){f.classList.remove('on')});render();
  setTimeout(fadeHint,8000);
})();
</script>
</body></html>
