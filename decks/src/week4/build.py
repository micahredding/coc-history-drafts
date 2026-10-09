import re, sys, base64
sys.path.insert(0,'decks/src/week4')
from slides import S

D='decks/src/week4/'
def b64(p):
    with open(p,'rb') as f: return 'data:image/jpeg;base64,'+base64.b64encode(f.read()).decode()

body='\n\n'.join(S).replace('IMG_STONE', b64(D+'stone.jpg'))
css=open(D+'engine.css').read()
css+= ('\n  /* ---- Week 4 type scale (inherited from Weeks 2-3) ---- */\n'
       '  #deck .slide h1{font-size:clamp(52px,11vmin,140px);line-height:1.05}\n'
       '  #deck .slide h2{font-size:clamp(36px,7vmin,90px);line-height:1.12;max-width:22ch}\n'
       '  #deck .slide.sect h2{font-size:clamp(52px,11vmin,130px)}\n'
       '  #deck .slide .sub{font-size:clamp(22px,3.6vmin,44px);max-width:34ch;line-height:1.35}\n'
       '  #deck .slide .eyebrow{font-size:clamp(16px,2.6vmin,30px);max-width:70ch;line-height:1.4}\n'
       '  #deck .slide .litany{gap:2.2vmin;margin-top:2vmin;max-width:90vw}\n'
       '  #deck .slide .litany .no{font-family:"IM Fell English",Georgia,serif;font-size:clamp(24px,4.3vmin,54px);line-height:1.28;color:var(--bone)}\n'
       '  #deck .slide .litany .no b{color:var(--gold);font-weight:400}\n'
       '  .slide.bleed .frag.sub{color:var(--bone)}\n')
css += '  .bgimg.househbg{background-image:url("%s");background-position:center 40%%;filter:sepia(.35) brightness(.75)}\n' % b64(D+'meetinghouse.jpg')

js=open(D+'engine.js').read()
for k in ('cur','mode','strip','presenter'):
    js=js.replace("'w1%s'" % k, "'w4%s'" % k)
js=js.replace("||'read')","||'present')")

html=('<!doctype html><html><head><meta charset=utf8>'
 '<meta name=viewport content="width=device-width,initial-scale=1">'
 '<title>Our Wild Democracy &middot; Chapter 4 &middot; The Last Will and Testament</title>'
 '<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">'
 '<style>\n/* ============================================================\n'
 '   THE LAST WILL AND TESTAMENT — Week 4 deck\n'
 '   Engine, palette and type inherited from the Week 2-3 decks.\n'
 '   ============================================================ */\n'
 + css + '</style></head>\n<body>\n<div id=deck>\n\n' + body +
 '\n\n</div>\n<div id=bar></div><div id=count></div>'
 '<div id=hint>&rarr; / space / click &middot; f fullscreen &middot; n read/present &middot; p presenter window &middot; s notes on THIS screen</div>'
 '<div id=mode></div><div id=strip></div><div id=pres></div>\n' + js + '</html>')

out='decks/week4-last-will.html'
open(out,'w').write(html)
print("wrote", out, round(len(html)/1048576,2), "MB;", html.count('<section'), "sections")
