import base64, re, sys, os
sys.path.insert(0,'decks/src/week2')
from slides import S

def b64(p):
    with open(p,'rb') as f: return 'data:image/jpeg;base64,'+base64.b64encode(f.read()).decode()

IMG='decks/src/week2/'
imgs={'IMG_TOKEN':'token.jpg','IMG_MAP':'map_marked.jpg','IMG_ANDERSON':'anderson_face.jpg',
      'IMG_ANDERSONTITLE':'anderson_title.jpg','IMG_TCAMPBELL':'tcampbell.jpg','IMG_STONE':'stone.jpg','IMG_ACAMPBELL':'acampbell.jpg','IMG_BROWNLOW':'brownlow.jpg'}
body='\n\n'.join(S)
for k,v in sorted(imgs.items(), key=lambda kv:-len(kv[0])):  # longest key first: IMG_ANDERSON is a prefix of IMG_ANDERSONTITLE
    if k in body: body=body.replace(k, b64(IMG+v))

css=open('decks/src/week2/engine.css').read()
# week-2 bleed backgrounds
css+= ('\n  /* ---- Week 2 bleeds ---- */\n'
       '  .bgimg.wreckbg{background-image:url("%s")}\n'
       '  .bgimg.indaalbg{background-image:url("%s")}\n'
       '  .bgimg.shipbg{background-image:url("%s")}\n'
'  .days .d .verdict{margin-left:auto;padding-left:2vmin;font-family:"IM Fell English SC","IM Fell English",Georgia,serif;letter-spacing:.08em;white-space:nowrap}\n'
       '  .verdict.v-red{color:#d3573f}.verdict.v-green{color:#6db07a}.verdict.v-yellow{color:var(--gold)}\n'
'  .days.verdictlist{gap:2.6vmin;max-width:82vw;width:82vw}.days.verdictlist .d{font-size:clamp(20px,3.5vmin,40px);line-height:1.3;align-items:baseline}.days.verdictlist .d span:nth-child(2){flex:1}.days.verdictlist .dn{flex:0 0 3em}\n'
       '  .days.verdictlist .verdict{font-size:clamp(24px,4.4vmin,48px);letter-spacing:.1em}.verdictlist .verdict.v-red{color:#ff5a3c;text-shadow:0 0 1.2vmin rgba(255,90,60,.35)}\n'
       '  .litany .frag{display:block}.litany .dim{font-size:.62em;color:var(--bone-dim);margin-top:.4em}\n'
       '  .shape{display:flex;gap:4vmin;align-items:center;margin:4.5vmin 0;flex-wrap:wrap;justify-content:center}.shape .step{font-family:"IM Fell English",Georgia,serif;font-size:clamp(27px,5.6vmin,65px)}.shape .sep{color:var(--gold);font-size:clamp(22px,4.48vmin,52px)}\n'
       '  .selfname{display:flex;flex-direction:column;gap:.8vmin;margin-top:3.4vmin}.selfname .big{font-family:"IM Fell English",Georgia,serif;font-size:clamp(31px,6.05vmin,67px);line-height:1.1;color:var(--gold)}.selfname .gl{font-style:italic;color:var(--smoke);font-size:clamp(15px,2.24vmin,24px)}\n'
       '  .wmap.all .th{opacity:.85}\n'
       '  .vt:not(.vo) .vev:not(.cur) .pull{opacity:0}\n'
       '  /* ---- Week 2 type scale: everything up, quotes already right ---- */\n'
       '  #deck .slide h1{font-size:clamp(52px,11vmin,140px);line-height:1.05}\n'
       '  #deck .slide h2{font-size:clamp(36px,7vmin,90px);line-height:1.12;max-width:22ch}\n'
       '  #deck .slide.sect h2{font-size:clamp(52px,11vmin,130px)}\n'
       '  #deck .slide .sub{font-size:clamp(22px,3.6vmin,44px);max-width:34ch;line-height:1.35}\n'
       '  #deck .slide .body{font-size:clamp(22px,3.4vmin,40px);line-height:1.35}\n'
       '  #deck .slide .eyebrow{font-size:clamp(16px,2.6vmin,30px)}\n'
       '  #deck .slide .cite{font-size:clamp(14px,2.2vmin,24px)}\n'
       '  #deck .slide .small{font-size:clamp(16px,2.4vmin,26px)}\n'
       '  #deck .slide .litany{font-size:clamp(30px,5.6vmin,68px);line-height:1.45}\n'
       '  #deck .slide .litany .dim{font-size:.62em}\n'
       '  #deck .slide .litany .no,#deck .slide .litany .coda{font-size:1em}\n'
       '  #deck .slide .shape .step{font-size:clamp(42px,8.4vmin,104px)}#deck .slide .shape .sep{font-size:clamp(32px,6.4vmin,80px)}\n'
       '  #deck .slide .selfname .big{font-size:clamp(42px,8vmin,96px)}#deck .slide .selfname .gl{font-size:clamp(18px,2.9vmin,34px)}\n'
       '  #deck .slide .plate img,#deck .slide .plate.short img{max-height:70vh}#deck .slide .plate.wide img{max-height:72vh}\n'
       '  #deck .slide figcaption{font-size:clamp(14px,2vmin,24px);max-width:60ch}\n'
       '  #deck .slide .faces{display:flex;gap:3vw;justify-content:center;flex-wrap:nowrap}#deck .slide .faces .face{width:min(52vmin,27vw)}#deck .slide .faces .face img{max-height:52vh}\n'
       '  #deck .slide .face .nm{font-size:clamp(22px,3.4vmin,40px)}#deck .slide .face .rl{font-size:clamp(15px,2.3vmin,26px)}\n'
       '  #deck .slide .facecred,#deck .slide .credit{font-size:clamp(12px,1.7vmin,19px)}\n'
       '  #deck .slide .days{font-size:clamp(20px,3.5vmin,40px);line-height:1.35;max-width:82vw;width:82vw;gap:2.2vmin}#deck .slide .days .dn{flex:0 0 3em}#deck .slide .days .d span:nth-child(2){flex:1}\n'
       '  #deck .slide .wmap .ms-christ .th{font-size:clamp(22px,4vmin,48px)}#deck .slide .wmap .ms-pri .th{font-size:clamp(36px,7.4vmin,88px)}\n'
       '  #deck .slide .wmap .ms-sec .th,#deck .slide .wmap .ms-pra .th{font-size:clamp(16px,2.8vmin,32px)}#deck .slide .ideasmap .small{font-size:clamp(14px,2.1vmin,24px)}\n'
       '  #deck .slide .room .sub{font-size:clamp(26px,4.4vmin,54px)}\n'
       '  .treeslide{padding:2vmin 3vmin 6vmin}.treeslide .eyebrow{margin-bottom:1vmin}.tree{width:min(96vw,150vh);height:auto;display:block}\n'
       '  .litany{line-height:1.5;font-size:clamp(20px,3.6vmin,44px)}\n'
       '  .days{font-family:"IM Fell English SC","IM Fell English",Georgia,serif;'
       'font-size:clamp(13px,2.05vmin,21px);color:var(--bone-dim);line-height:2.1;max-width:52em;letter-spacing:.02em}\n'
       % (b64(IMG+'wreck.jpg'), b64(IMG+'indaal.jpg'), b64(IMG+'ship.jpg')))

js=open('decks/src/week2/engine.js').read()
js=js.replace("'w1cur'","'w2cur'").replace("'w1mode'","'w2mode'").replace("'w1strip'","'w2strip'")
js=js.replace("'w1presenter'","'w2presenter'")
js=js.replace("||'read')","||'present')")  # one deck: present mode by default

html=('<!doctype html><html><head><meta charset=utf8>'
 '<meta name=viewport content="width=device-width,initial-scale=1">'
 '<title>Our Wild Democracy &middot; Week 2 &middot; Thomas Campbell&rsquo;s Heresy Trial</title>'
 '<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">'
 '<style>\n/* ============================================================\n'
 '   THOMAS CAMPBELL\'S BREAK — Week 2 deck\n'
 '   Engine, palette and type inherited from the Week 1 Cane Ridge deck.\n'
 '   Content set from the eleven-beat outline (vault 202609180912).\n'
 '   ============================================================ */\n'
 + css + '</style></head>\n<body>\n<div id=deck>\n\n' + body +
 '\n\n</div>\n<div id=bar></div><div id=count></div>'
 '<div id=hint>&rarr; / space / click &middot; f fullscreen &middot; n read/present &middot; p presenter window &middot; s notes on THIS screen</div>'
 '<div id=mode></div><div id=strip></div><div id=pres></div>\n' + js + '</html>')

out='decks/week2-thomas-campbell.html'
open(out,'w').write(html)
print("wrote", out)
print("bytes:", len(html), "=", round(len(html)/1048576,2), "MB")
print("sections:", html.count('<section'))
print("frags:", html.count('class="sub frag')+html.count('class="bigquote frag')+html.count('class="small frag'))
print("unreplaced IMG_ placeholders:", len(re.findall(r'IMG_[A-Z]+', html)))
