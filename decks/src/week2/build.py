import base64, re, sys, os
sys.path.insert(0,'decks/src/week2')
from slides import S

def b64(p):
    with open(p,'rb') as f: return 'data:image/jpeg;base64,'+base64.b64encode(f.read()).decode()

IMG='decks/src/week2/'
imgs={'IMG_TOKEN':'token.jpg','IMG_MAP':'map_marked.jpg','IMG_ANDERSON':'anderson_face.jpg',
      'IMG_ANDERSONTITLE':'anderson_title.jpg','IMG_TCAMPBELL':'tcampbell.jpg'}
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
 '<title>Our Wild Democracy &middot; Week 2</title>'
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
