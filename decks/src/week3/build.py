import re, sys, base64
sys.path.insert(0,'decks/src/week3')
from slides import S, PATDEFS, CHRISTENDOM_CSS

body='\n\n'.join(S)
css=open('decks/src/week3/engine.css').read()
css+= ('\n  /* ---- Week 3 type scale (inherited from Week 2) ---- */\n'
       '  #deck .slide h1{font-size:clamp(52px,11vmin,140px);line-height:1.05}\n'
       '  #deck .slide h2{font-size:clamp(36px,7vmin,90px);line-height:1.12;max-width:22ch}\n'
       '  #deck .slide.sect h2{font-size:clamp(52px,11vmin,130px)}\n'
       '  #deck .slide .sub{font-size:clamp(22px,3.6vmin,44px);max-width:34ch;line-height:1.35}\n'
       '  #deck .slide .eyebrow{font-size:clamp(16px,2.6vmin,30px)}\n'
       + CHRISTENDOM_CSS +
       '  /* ---- the full flow diagram slide ---- */\n'
       '  #deck .flowslide{padding:2vmin 3vmin 6vmin;justify-content:center}#deck .flowslide .eyebrow{margin-bottom:1vmin}\n'
       '  #deck .flowslide svg{width:min(96vw,145vh);height:auto;display:block}\n'
       '  .flowslide .rib{fill:rgba(237,228,211,.13);stroke:rgba(237,228,211,.55);stroke-width:1.2;stroke-linejoin:round}\n'
       '  .flowslide .rib.dying{fill:url(#fade);stroke:none}\n'
       '  .flowslide .breach{fill:var(--ground);stroke:var(--gold-dim);stroke-width:1.5;stroke-dasharray:4 5}\n'
       '  .flowslide .fork{stroke:var(--gold);stroke-width:2.5;stroke-linecap:round}\n'
       '  .flowslide .node{fill:var(--ground);stroke:var(--gold);stroke-width:2.5}.flowslide .node.heal{fill:var(--gold-dim);stroke:var(--gold-dim)}\n'
       '  .flowslide .fx{font-family:"IM Fell English",Georgia,serif;font-size:28px;fill:var(--smoke)}\n'
       '  .flowslide .flab{font-size:19px;fill:var(--bone-dim);paint-order:stroke;stroke:var(--ground);stroke-width:8px;stroke-linejoin:round}\n'
       '  .flowslide .flab .yr{font-family:"IM Fell English SC",Georgia,serif;font-size:21px;letter-spacing:.14em;fill:var(--gold)}\n'
       '  .flowslide .flab .ttl{font-family:"IM Fell English",Georgia,serif;font-style:italic;font-size:27px;fill:var(--bone)}\n'
       '  .flowslide .flab .fsub{font-family:Spectral,Georgia,serif;font-size:19px;fill:var(--bone-dim)}\n'
       '  .flowslide .leaf{font-family:"IM Fell English",Georgia,serif;font-size:18px;fill:var(--bone)}.flowslide .leaf.dim{fill:var(--smoke);font-style:italic;font-size:17px}\n'
       '  .flowslide .trunk{font-family:"IM Fell English SC",Georgia,serif;font-size:19px;letter-spacing:.18em;fill:var(--smoke)}\n')

# one shared gradient for the dying fork ribbons
defs = '<defs><linearGradient id="forkfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ede4d3" stop-opacity=".13"/><stop offset="1" stop-color="#ede4d3" stop-opacity="0"/></linearGradient></defs>'
body = body.replace('xmlns="http://www.w3.org/2000/svg"><path class="rib"', 'xmlns="http://www.w3.org/2000/svg">' + defs + '<path class="rib"')

css += ('\n  /* ---- quote litanies (evils, reception) ---- */\n'
        '  #deck .slide .litany{gap:2.2vmin;margin-top:2vmin;max-width:90vw}\n'
        '  #deck .slide .litany .no{font-family:"IM Fell English",Georgia,serif;font-size:clamp(24px,4.3vmin,54px);line-height:1.28;color:var(--bone)}\n'
        '  #deck .slide .litany .no b{color:var(--gold);font-weight:400}\n'
        '  #deck .slide .eyebrow{max-width:70ch;line-height:1.4}\n')

def b64(p):
    with open(p,'rb') as f: return 'data:image/jpeg;base64,'+base64.b64encode(f.read()).decode()
css += '\n  .bgimg.lutherbg{background-image:url("%s");background-position:center 30%%}\n' % b64('decks/src/week3/luther.jpg')
css += '  .slide.bleed .frag.sub{color:var(--bone)}\n'
import os
if os.path.exists('decks/src/week3/marburg.jpg'):
    css += '  .bgimg.marburgbg{background-image:url("%s");background-position:center 20%%}\n' % b64('decks/src/week3/marburg.jpg')
    css += '  #deck .slide:has(.marburgbg) .credit{background:rgba(14,11,9,.72);padding:.35em .6em;border-radius:.3em}\n'
else:
    css += '  #deck .slide:has(.marburgbg) .credit{display:none}\n'
    print('note: decks/src/week3/marburg.jpg missing; the Marburg slide builds without its painting')

js=open('decks/src/week3/engine.js').read()
js=js.replace("'w1cur'","'w3cur'").replace("'w1mode'","'w3mode'").replace("'w1strip'","'w3strip'")
js=js.replace("'w1presenter'","'w3presenter'")
js=js.replace("||'read')","||'present')")

html=('<!doctype html><html><head><meta charset=utf8>'
 '<meta name=viewport content="width=device-width,initial-scale=1">'
 '<title>Our Wild Democracy &middot; Chapter 3 &middot; The Declaration and Address</title>'
 '<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">'
 '<style>\n/* ============================================================\n'
 '   THE DECLARATION AND ADDRESS — Week 3 deck\n'
 '   Engine, palette and type inherited from the Week 2 deck.\n'
 '   Started 2026-10-06 with the Christendom sequence (issue / attempt / fork).\n'
 '   ============================================================ */\n'
 + css + '</style></head>\n<body>\n<svg width=0 height=0 style="position:absolute;visibility:visible" aria-hidden=true>' + PATDEFS + '</svg>\n<div id=deck>\n\n' + body +
 '\n\n</div>\n<div id=bar></div><div id=count></div>'
 '<div id=hint>&rarr; / space / click &middot; f fullscreen &middot; n read/present &middot; p presenter window &middot; s notes on THIS screen</div>'
 '<div id=mode></div><div id=strip></div><div id=pres></div>\n' + js + '</html>')

out='decks/week3-declaration-address.html'
open(out,'w').write(html)
print("wrote", out)
print("bytes:", len(html), "=", round(len(html)/1048576,2), "MB")
print("sections:", html.count('<section'))
print("frags:", html.count('class="failure frag')+html.count('class="frag healer')+html.count('class="sub frag'))
