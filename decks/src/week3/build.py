import re, sys
sys.path.insert(0,'decks/src/week3')
from slides import S, PATDEFS

body='\n\n'.join(S)
css=open('decks/src/week3/engine.css').read()
css+= ('\n  /* ---- Week 3 type scale (inherited from Week 2) ---- */\n'
       '  #deck .slide h1{font-size:clamp(52px,11vmin,140px);line-height:1.05}\n'
       '  #deck .slide h2{font-size:clamp(36px,7vmin,90px);line-height:1.12;max-width:22ch}\n'
       '  #deck .slide.sect h2{font-size:clamp(52px,11vmin,130px)}\n'
       '  #deck .slide .sub{font-size:clamp(22px,3.6vmin,44px);max-width:34ch;line-height:1.35}\n'
       '  #deck .slide .eyebrow{font-size:clamp(16px,2.6vmin,30px)}\n'
       '  /* ---- the division slides: headline / line / split ---- */\n'
       '  :root{--c1:#c89b3c;--c2:#a84a33;--c3:#5f8aa3;--c4:#6f9a6a;--bone:#ede4d3}\n'
       '  #deck .divslide{justify-content:flex-start;padding-top:5vmin;gap:0}\n'
       '  #deck .divslide h2{font-size:clamp(36px,6.8vmin,86px);max-width:none}\n'
       '  #deck .divslide .line{margin-top:1vmin;font-family:Spectral,Georgia,serif;font-style:italic;font-size:clamp(18px,3vmin,38px);line-height:1.35;max-width:44ch;color:var(--bone-dim)}\n'
       '  #deck .divslide .failure{margin-top:1vmin;width:100%;display:flex;justify-content:center}\n'
       '  #deck .divslide .splitfig{height:min(68vh,76vmin);width:auto;max-width:96vw;display:block}\n'
       '  /* the figure is on screen before the click as the before-state; the click moves it to the after-state */\n'
       '  #deck .divslide .failure.frag{opacity:1;transform:none}\n'
       '  .splitfig .piece path{d:var(--d0);fill:var(--k0);stroke:var(--s0);stroke-width:1.5;transition:d .9s cubic-bezier(.6,0,.3,1),fill .7s ease .25s,stroke .3s ease,opacity .7s ease .25s}\n'
       '  .splitfig .piece.gone0 path{opacity:0}.failure.on .piece.gone1 path{opacity:0!important}\n'
       '  .splitfig .piece.dying0 path{opacity:.35}.failure.on .piece path{opacity:1}.failure.on .piece.dying1 path{opacity:.35}\n'
       '  .failure.on .piece path{d:var(--d1);fill:var(--k1);stroke:var(--s1)}\n'
       '  .splitfig .seam{d:var(--d0);fill:none;stroke:var(--ground);stroke-width:5;stroke-linejoin:round;opacity:0;transition:d .9s cubic-bezier(.6,0,.3,1),opacity .5s ease}\n'
       '  .splitfig .seam.on0{opacity:1}.failure.on .seam{d:var(--d1);opacity:0}.failure.on .seam.on1{opacity:1}\n'
       '  #deck .divslide:has(.healer.on) .failure.on .seam{d:var(--d2);opacity:0}#deck .divslide:has(.healer.on) .failure.on .seam.on2{opacity:1}\n'
       '  #deck .shatterslide .shards{height:min(70vh,78vmin);width:auto;max-width:96vw;display:block}\n'
       '  .shards .shardlab{font-family:"IM Fell English",Georgia,serif;fill:var(--bone);paint-order:stroke;stroke:var(--ground);stroke-width:3px;stroke-linejoin:round;pointer-events:none}\n'
       '  .splitfig .plab{font-family:"IM Fell English",Georgia,serif;font-size:32px;fill:var(--bone);transition:opacity .6s ease}\n'
       '  .splitfig .plab.post{opacity:0;transition-delay:.6s}.failure.on .plab.post{opacity:1}\n'
       '  .splitfig .plab.pre{opacity:1}.failure.on .plab.pre{opacity:0;transition-delay:0s}\n'
       '  .splitfig .plab.dim{fill:var(--smoke);font-style:italic}\n'
       '  /* the Henotikon: a second click closes the gap again, leaving a gold seam */\n'
       '  .healer{height:0}\n'
       '  #deck .divslide:has(.healer.on) .failure.on .piece path{d:var(--d2)}\n'
       '  \n'
       '  \n'
       '  /* ---- the tree of divisions ---- */\n'
       '  #deck .treeslide2{padding:2vmin 3vmin 4vmin;justify-content:center}#deck .treeslide2 .eyebrow{margin-bottom:.6vmin}\n'
       '  #deck .treeslide2 .tree2{height:min(84vh,88vmin);width:auto;max-width:96vw;display:block}\n'
       '  .tree2 .tb{stroke-width:1.6;fill:none;stroke-linecap:round}.tree2 .leafline{opacity:.45}\n'
       '  .tree2 .tn{stroke:var(--ground);stroke-width:2}\n'
       '  .tree2 .tl{font-family:"IM Fell English",Georgia,serif;fill:var(--bone);paint-order:stroke;stroke:var(--ground);stroke-width:5px;stroke-linejoin:round}\n'
       '  .tree2 .tl .yr{font-family:"IM Fell English SC",Georgia,serif;fill:var(--gold);font-size:.8em;letter-spacing:.08em}\n'
       '  .tree2 .lf{font-family:Spectral,Georgia,serif;fill:var(--bone-dim)}.tree2 .lf.dead{fill:var(--smoke);font-style:italic}\n'
       '  .tree2 .tick{stroke:var(--ink-brown);stroke-width:1;stroke-dasharray:2 6}.tree2 .tk{font-family:"IM Fell English SC",Georgia,serif;font-size:13px;letter-spacing:.14em;fill:var(--smoke)}\n'
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
