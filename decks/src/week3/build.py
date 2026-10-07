import re, sys
sys.path.insert(0,'decks/src/week3')
from slides import S

body='\n\n'.join(S)
css=open('decks/src/week3/engine.css').read()
css+= ('\n  /* ---- Week 3 type scale (inherited from Week 2) ---- */\n'
       '  #deck .slide h1{font-size:clamp(52px,11vmin,140px);line-height:1.05}\n'
       '  #deck .slide h2{font-size:clamp(36px,7vmin,90px);line-height:1.12;max-width:22ch}\n'
       '  #deck .slide.sect h2{font-size:clamp(52px,11vmin,130px)}\n'
       '  #deck .slide .sub{font-size:clamp(22px,3.6vmin,44px);max-width:34ch;line-height:1.35}\n'
       '  #deck .slide .eyebrow{font-size:clamp(16px,2.6vmin,30px)}\n'
       '  /* ---- the division slides: issue / attempt / fork ---- */\n'
       '  #deck .divslide{justify-content:flex-start;padding-top:7vmin;gap:0}\n'
       '  #deck .divslide h2{font-size:clamp(30px,5.6vmin,72px);max-width:26ch;min-height:2.3em}\n'
       '  #deck .divslide .attempt{margin-top:2.4vmin;font-family:Spectral,Georgia,serif;font-style:italic;font-size:clamp(20px,3.2vmin,40px);line-height:1.35;max-width:40ch;color:var(--bone-dim)}\n'
       '  #deck .divslide .attempt .k{display:block;font-family:"IM Fell English SC","IM Fell English",Georgia,serif;font-style:normal;letter-spacing:.24em;font-size:.62em;color:var(--gold);margin-bottom:.5vmin}\n'
       '  #deck .divslide .failure{margin-top:1.6vmin;display:flex;flex-direction:column;align-items:center;width:100%}\n'
       '  #deck .divslide .forkfig{width:min(70vmin,72vw);height:auto;display:block}\n'
       '  #deck .divslide .cap{font-family:"IM Fell English",Georgia,serif;font-size:clamp(20px,3.4vmin,42px);line-height:1.3;max-width:34ch;color:var(--bone);margin-top:.8vmin}\n'
       '  .forkfig .rib{fill:rgba(237,228,211,.13);stroke:rgba(237,228,211,.6);stroke-width:1.6;stroke-linejoin:round}\n'
       '  .forkfig .rib.dying{fill:url(#forkfade);stroke:none}\n'
       '  .forkfig .rib.heal{stroke-dasharray:5 6;stroke:var(--gold-dim)}\n'
       '  .forkfig .bar{stroke:var(--gold);stroke-width:5;stroke-linecap:round}\n'
       '  .forkfig .bar.heal{stroke:var(--gold-dim)}\n'
       '  .forkfig .rlab{font-family:"IM Fell English",Georgia,serif;font-size:30px;fill:var(--bone)}\n'
       '  .forkfig .rlab.dim{fill:var(--smoke);font-style:italic}\n'
       '  .forkfig .blab{font-family:"IM Fell English SC","IM Fell English",Georgia,serif;font-size:24px;letter-spacing:.14em;fill:var(--gold);paint-order:stroke;stroke:var(--ground);stroke-width:8px;stroke-linejoin:round}\n'
       '  .forkfig .xx{font-family:"IM Fell English",Georgia,serif;font-size:40px;fill:var(--smoke)}\n'
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
body = body.replace('<svg class="forkfig"', '<svg class="forkfig"', 1)
defs = '<defs><linearGradient id="forkfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ede4d3" stop-opacity=".13"/><stop offset="1" stop-color="#ede4d3" stop-opacity="0"/></linearGradient></defs>'
body = body.replace('xmlns="http://www.w3.org/2000/svg"><path class="rib"', 'xmlns="http://www.w3.org/2000/svg">' + defs + '<path class="rib"')

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
 + css + '</style></head>\n<body>\n<div id=deck>\n\n' + body +
 '\n\n</div>\n<div id=bar></div><div id=count></div>'
 '<div id=hint>&rarr; / space / click &middot; f fullscreen &middot; n read/present &middot; p presenter window &middot; s notes on THIS screen</div>'
 '<div id=mode></div><div id=strip></div><div id=pres></div>\n' + js + '</html>')

out='decks/week3-declaration-address.html'
open(out,'w').write(html)
print("wrote", out)
print("bytes:", len(html), "=", round(len(html)/1048576,2), "MB")
print("sections:", html.count('<section'))
print("frags:", html.count('class="attempt frag')+html.count('class="failure frag')+html.count('class="sub frag'))
