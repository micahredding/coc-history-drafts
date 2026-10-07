# Build the Christendom sequence as a standalone element deck: decks/elements/christendom-divisions-sequence.html
# Run from the repo root:  python3 decks/src/elements/build_christendom.py
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from christendom import christendom_slides, PATDEFS, CHRISTENDOM_CSS

ENGINE = os.path.join(HERE, '..', 'week3')       # the shared deck engine (same as Weeks 1–3)
css = open(os.path.join(ENGINE, 'engine.css')).read()
css += ('\n  #deck .slide h2{font-size:clamp(36px,7vmin,90px);line-height:1.12;max-width:22ch}\n'
        '  #deck .slide.sect h2{font-size:clamp(52px,11vmin,130px)}\n'
        '  #deck .slide .sub{font-size:clamp(22px,3.6vmin,44px);max-width:34ch;line-height:1.35}\n'
        '  #deck .slide .eyebrow{font-size:clamp(16px,2.6vmin,30px)}\n') + CHRISTENDOM_CSS
js = open(os.path.join(ENGINE, 'engine.js')).read()
js = js.replace("'w1cur'", "'elcur'").replace("'w1mode'", "'elmode'").replace("'w1strip'", "'elstrip'").replace("'w1presenter'", "'elpresenter'")
js = js.replace("||'read')", "||'present')")

body = '\n\n'.join(christendom_slides())
html = ('<!doctype html><html><head><meta charset=utf8>'
 '<meta name=viewport content="width=device-width,initial-scale=1">'
 '<title>Christendom&rsquo;s Search for Unity &middot; element</title>'
 '<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">'
 '<style>\n/* Christendom\'s search for unity — reusable element. Source: decks/src/elements/christendom.py */\n'
 + css + '</style></head>\n<body>\n<svg width=0 height=0 style="position:absolute;visibility:visible" aria-hidden=true>' + PATDEFS + '</svg>\n<div id=deck>\n\n' + body +
 '\n\n</div>\n<div id=bar></div><div id=count></div>'
 '<div id=hint>&rarr; / space / click &middot; f fullscreen &middot; n read/present &middot; p presenter window &middot; s notes on THIS screen</div>'
 '<div id=mode></div><div id=strip></div><div id=pres></div>\n' + js + '</html>')
out = os.path.join(HERE, '..', '..', 'elements', 'christendom-divisions-sequence.html')
open(out, 'w').write(html)
print('wrote', os.path.relpath(out), len(html), 'bytes;', html.count('<section'), 'sections')
