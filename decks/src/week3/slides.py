# -*- coding: utf-8 -*-
# Week 3 deck content — The Declaration & Address.
# The Christendom sequence (325–1806, the egg) is a reusable element: decks/src/elements/christendom.py.
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
import re, math

def C(name, note=''):   # chapter card
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (name, note))

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'elements'))
from christendom import christendom_slides, PATDEFS, CHRISTENDOM_CSS

S = []
A = S.append
_D = __file__.rsplit('/', 1)[0]

S += christendom_slides()

A('<section class="slide"><h2>What can Christians unite on?</h2>'
  '<div class="sub frag">He prayed that they would be one. So it must be possible.</div>'
  '<aside class=notes>John 17:21, a prayer, not a command. Then back to the Preamble: &ldquo;nor, indeed, can we reasonably expect to find it anywhere but in Christ and his simple word.&rdquo;<br>&rarr; Your close is yours. The slide stops at the question.</aside></section>')

A('<section class="slide"><aside class=notes>Black. Then the Preamble&rsquo;s last sentence.</aside></section>')
