#!/usr/bin/env python3
"""Christendom's divisions, 325–1806 — a flow diagram for Week 3 (Declaration & Address).

One river at the top that keeps forking. No trunk: at every split both sides bend away.
Ribbon widths are illustrative only (rough present-day size, with a floor so small bodies stay visible).
Each fork is labeled with the instrument of unity that caused it. Only church-vs-church divisions.

    python3 decks/src/elements/christendom-divisions.py   →   decks/elements/christendom-divisions.html
"""
from pathlib import Path

W, H = 2000, 1300
OUT = Path(__file__).resolve().parents[2] / "elements" / "christendom-divisions.html"
MARGIN, GAP, DROP = 70, 26, 56
TOP, END, LEAF_Y = 150, 1140, 1168

# rows (ordinal, not linear)
Y = {325: 230, 431: 310, 451: 390, 482: 445, 519: 500, 1054: 570, 1517: 650, 1527: 715, 1529: 775,
     1646: 860, 1690: 920, 1733: 975, 1747: 1030, 1799: 1080, 1806: 1095}

# ---- the tree -------------------------------------------------------------------
# leaves: key -> (label lines, width weight)
LEAF = {
    "arian":       ("Arians", 1.0),
    "east":        ("Church of|the East", 1.0),
    "oriental":    ("Oriental|Orthodox", 1.5),
    "orthodox":    ("Eastern|Orthodox", 2.4),
    "catholic":    ("Roman|Catholic", 4.6),
    "lutheran":    ("Lutheran", 1.6),
    "anglican":    ("Church of|England", 1.6),
    "independent": ("Independents", 1.0),
    "reformed":    ("Continental|Reformed", 1.5),
    "covenanter":  ("Covenanters", 1.0),
    "scotland":    ("Church of|Scotland", 1.3),
    "burgher_old": ("Burgher|Old Light", 1.0),
    "burgher_new": ("Burgher|New Light", 1.0),
    "antib_old":   ("Anti-Burgher|Old Light", 1.0),
    "antib_new":   ("Anti-Burgher|New Light", 1.0),
    "anabaptist":  ("Anabaptists", 1.0),
}
# internal nodes: key -> (split year, children in left-to-right order, label title, label sub)
NODE = {
    "root":  (325,  ["arian", "n431"],                 "Nicaea · the Nicene Creed",              "the Arians go · war for 56 more years"),
    "n431":  (431,  ["east", "n451"],                  "Ephesus · Canon 7, no new creed, ever",  "the Church of the East goes"),
    "n451":  (451,  ["oriental", "n1054"],             "Chalcedon · the Definition, “not a new creed”", "Egypt, Armenia, Ethiopia, Syria go"),
    "n1054": (1054, ["orthodox", "n1517"],             "the Filioque · the creed itself",        "East and West: which wording, who decides"),
    "n1517": (1517, ["catholic", "n1527"],             "the Reformation",                        "same creed, same filioque"),
    "n1527": (1527, ["n1529", "anabaptist"],           "Zurich · Felix Manz drowned",            "the Anabaptists go"),
    "n1529": (1529, ["lutheran", "n1646"],             "Marburg · agreed on 14 articles, not the Supper", "“you have a different spirit”"),
    "n1646": (1646, ["anglican", "independent", "reformed", "n1690"], "Westminster · one confession for three kingdoms", "England never adopts it · 1662, two thousand ejected"),
    "n1690": (1690, ["covenanter", "n1733"],           "the Revolution Settlement",              "the Covenanters go"),
    "n1733": (1733, ["scotland", "n1747"],             "the Secession · Erskine",                "over patronage"),
    "n1747": (1747, ["n1799", "n1806"],                "the Burgess Oath",                       "Burgher and Anti-Burgher"),
    "n1799": (1799, ["burgher_old", "burgher_new"],    "Old Light · New Light, 1799 and 1806",   "each Seceder body splits again · Thomas Campbell’s synod, the year before he sailed"),
    "n1806": (1806, ["antib_old", "antib_new"],        None,                                     None),
}
DIES = {"arian": 560}   # leaf -> y where the ribbon fades out

# label placement overrides: key -> (dx, dy, anchor)
LAB = {
    "root": (0, -14, "middle"), "n431": (0, -14, "middle"), "n451": (0, -14, "middle"),
    "n1054": (0, -14, "middle"), "n1517": (0, -14, "middle"),
    "n1527": (0, -14, "middle"), "n1529": (0, -14, "middle"),
    "n1646": (0, -14, "middle"), "n1690": (0, -14, "middle"), "n1733": (0, -14, "middle"),
    "n1747": (0, -14, "middle"), "n1799": (-14, -12, "end"), "n1806": None,
}

# ---- layout (bottom-up) ------------------------------------------------------------
order = []
def walk(k):
    if k in LEAF: order.append(k); return
    for c in NODE[k][1]: walk(c)
walk("root")

total_w = sum(LEAF[k][1] for k in order)
unit = (W - 2 * MARGIN - GAP * (len(order) - 1)) / total_w
span = {}      # key -> (x0, x1) own ribbon extent
x = MARGIN
for k in order:
    w = LEAF[k][1] * unit
    span[k] = (x, x + w); x += w + GAP

width = {}     # key -> ribbon width (sum of children, no gaps)
def measure(k):
    if k in LEAF:
        width[k] = span[k][1] - span[k][0]; return width[k]
    width[k] = sum(measure(c) for c in NODE[k][1]); return width[k]
measure("root")

def place(k):
    """Internal node's own extent: centered over its children's span."""
    if k in LEAF: return
    kids = NODE[k][1]
    for c in kids: place(c)
    lo = span[kids[0]][0]; hi = span[kids[-1]][1]
    cx = (lo + hi) / 2
    span[k] = (cx - width[k] / 2, cx + width[k] / 2)
place("root")

# ---- draw -------------------------------------------------------------------------
svg = []
def add(s): svg.append(s)

def ribbon(k, y0, sx0, sx1, y1, dies=None):
    x0, x1 = span[k]
    d = DROP
    if dies:
        add(f'<path class="rib dying" d="M{sx0:.1f},{y0} C{sx0:.1f},{y0+d/2} {x0:.1f},{y0+d/2} {x0:.1f},{y0+d} L{x0:.1f},{dies} L{x1:.1f},{dies} L{x1:.1f},{y0+d} C{x1:.1f},{y0+d/2} {sx1:.1f},{y0+d/2} {sx1:.1f},{y0} Z"/>')
        return
    add(f'<path class="rib" d="M{sx0:.1f},{y0} C{sx0:.1f},{y0+d/2} {x0:.1f},{y0+d/2} {x0:.1f},{y0+d} L{x0:.1f},{y1} L{x1:.1f},{y1} L{x1:.1f},{y0+d} C{x1:.1f},{y0+d/2} {sx1:.1f},{y0+d/2} {sx1:.1f},{y0} Z"/>')

def draw(k, y0, sx0, sx1):
    """Draw k's ribbon starting at its parent's fork (y0, segment sx0..sx1), then recurse."""
    if k in LEAF:
        ribbon(k, y0, sx0, sx1, END, DIES.get(k)); return
    yr, kids, _, _ = NODE[k]
    y1 = Y[yr]
    ribbon(k, y0, sx0, sx1, y1)
    # divide this node's ribbon at its fork among the children, contiguous, in order
    x0, _ = span[k]
    cur = x0
    for c in kids:
        w = width[c]
        draw(c, y1, cur, cur + w)
        cur += w

# root: a straight river from TOP to its fork
rx0, rx1 = span["root"]
add(f'<path class="rib" d="M{rx0:.1f},{TOP} L{rx0:.1f},{Y[325]} L{rx1:.1f},{Y[325]} L{rx1:.1f},{TOP} Z"/>')
x0, _ = span["root"]; cur = x0
for c in NODE["root"][1]:
    draw(c, Y[325], cur, cur + width[c]); cur += width[c]

# the Henotikon: a lens-shaped breach in the East+West river between 482 and 519, healed
hx0, hx1 = span["n1054"]; hc = (hx0 + hx1) / 2; hw = (hx1 - hx0) * 0.22
add(f'<path class="breach" d="M{hc:.1f},{Y[482]} C{hc+hw:.1f},{Y[482]+18} {hc+hw:.1f},{Y[519]-18} {hc:.1f},{Y[519]} C{hc-hw:.1f},{Y[519]-18} {hc-hw:.1f},{Y[482]+18} {hc:.1f},{Y[482]} Z"/>')
add(f'<circle class="node heal" cx="{hc:.1f}" cy="{Y[482]}" r="5"/><circle class="node heal" cx="{hc:.1f}" cy="{Y[519]}" r="5"/>')
add(f'<text class="lab" x="{hc-hw-16:.1f}" y="{Y[482]+14}" text-anchor="end"><tspan class="yr">482</tspan> <tspan class="ttl">the Henotikon · “instrument of union”</tspan>'
    f'<tspan class="sub" x="{hc-hw-16:.1f}" dy="20">Rome and Constantinople out of communion 484–519 · healed</tspan></text>')

# fork markers + labels
for k, (yr, kids, title, sub) in NODE.items():
    x0, x1 = span[k]; cx = (x0 + x1) / 2; y = Y[yr]
    add(f'<line class="fork" x1="{x0:.1f}" y1="{y}" x2="{x1:.1f}" y2="{y}"/>')
    if LAB.get(k) is None or title is None: continue
    dx, dy, anchor = LAB[k]
    lx = cx if anchor == "middle" else ((x1 + dx) if anchor == "start" else (x0 + dx))
    t = f'<tspan class="yr">{yr}</tspan> <tspan class="ttl">{title}</tspan>'
    if sub: t += f'<tspan class="sub" x="{lx:.1f}" dy="20">{sub}</tspan>'
    add(f'<text class="lab" x="{lx:.1f}" y="{y+dy}" text-anchor="{anchor}">{t}</text>')

# leaves
for i, k in enumerate(order):
    x0, x1 = span[k]; cx = (x0 + x1) / 2
    lines = LEAF[k][0].split("|")
    if k in DIES:
        add(f'<text class="x" x="{cx:.1f}" y="{DIES[k]+26}" text-anchor="middle">×</text>')
        add(f'<text class="leaf dim" x="{cx:.1f}" y="{DIES[k]+48}" text-anchor="middle"><tspan x="{cx:.1f}">Arians</tspan><tspan x="{cx:.1f}" dy="17">gone by c. 650</tspan></text>')
        continue
    stagger = 0 if i % 2 == 0 else 20
    t = "".join(f'<tspan x="{cx:.1f}" dy="{0 if j==0 else 17}">{l}</tspan>' for j, l in enumerate(lines))
    add(f'<text class="leaf" x="{cx:.1f}" y="{LEAF_Y+stagger}" text-anchor="middle">{t}</text>')

add(f'<text class="trunk" x="{(rx0+rx1)/2:.1f}" y="{TOP-16}" text-anchor="middle">the one Church</text>')

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Christendom’s Divisions</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">
<style>
  /* Same visual world as the Week 0 deck: night field, bone paper, candle gold. */
  :root{{
    --ground:#100d0a; --ground-lift:#181310; --panel:#1d1712;
    --bone:#ede4d3; --bone-dim:#b3a68e; --smoke:#7a6e5c;
    --gold:#c89b3c; --gold-dim:#8a6d2c; --ink-brown:#5c4a33;
  }}
  *{{margin:0;padding:0;box-sizing:border-box}}
  html,body{{background:var(--ground);color:var(--bone);height:100%}}
  body{{font-family:'Spectral',Georgia,serif;font-weight:300;display:flex;flex-direction:column;align-items:center;padding:3vmin 2vmin}}
  header{{width:min(96vw,2000px);margin-bottom:.6vmin}}
  .eyebrow{{font-family:'IM Fell English SC',Georgia,serif;font-size:clamp(11px,1.4vmin,15px);letter-spacing:.26em;color:var(--smoke)}}
  h1{{font-family:'IM Fell English',Georgia,serif;font-weight:400;font-size:clamp(22px,3.6vmin,40px);line-height:1.1;color:var(--bone)}}
  h1 em{{font-style:italic;color:var(--gold)}}
  svg{{width:min(96vw,2000px);height:auto;display:block}}
  .rib{{fill:rgba(237,228,211,.13);stroke:rgba(237,228,211,.55);stroke-width:1.2;stroke-linejoin:round}}
  .rib.dying{{fill:url(#fade);stroke:none}}
  .breach{{fill:var(--ground);stroke:var(--gold-dim);stroke-width:1.5;stroke-dasharray:4 5}}
  .fork{{stroke:var(--gold);stroke-width:2.5;stroke-linecap:round}}
  .node{{fill:var(--ground);stroke:var(--gold);stroke-width:2.5}}
  .node.heal{{fill:var(--gold-dim);stroke:var(--gold-dim)}}
  .x{{font-family:'IM Fell English',Georgia,serif;font-size:24px;fill:var(--smoke)}}
  .lab{{font-size:16px;fill:var(--bone-dim);paint-order:stroke;stroke:var(--ground);stroke-width:7px;stroke-linejoin:round}}
  .lab .yr{{font-family:'IM Fell English SC',Georgia,serif;font-size:17px;letter-spacing:.14em;fill:var(--gold)}}
  .lab .ttl{{font-family:'IM Fell English',Georgia,serif;font-style:italic;font-size:22px;fill:var(--bone)}}
  .lab .sub{{font-family:'Spectral',Georgia,serif;font-size:15px;fill:var(--bone-dim)}}
  .leaf{{font-family:'IM Fell English',Georgia,serif;font-size:16px;fill:var(--bone)}}
  .leaf.dim{{fill:var(--smoke);font-style:italic;font-size:15px}}
  .trunk{{font-family:'IM Fell English SC',Georgia,serif;font-size:15px;letter-spacing:.18em;fill:var(--smoke)}}
  footer{{width:min(96vw,2000px);margin-top:.8vmin;font-family:'IM Fell English',Georgia,serif;font-style:italic;font-size:clamp(11px,1.5vmin,16px);color:var(--smoke)}}
</style>
</head>
<body>
<header>
  <div class="eyebrow">Christendom’s search for unity · 325–1806</div>
  <h1>Every instrument of unity drew a <em>border</em></h1>
</header>
<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A flow diagram: one river of the Church at the top, forking again and again from Nicaea in 325 to the Seceder splits of 1806, each fork labeled with the creed, council, or oath that caused it.">
<defs><linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ede4d3" stop-opacity=".13"/><stop offset="1" stop-color="#ede4d3" stop-opacity="0"/></linearGradient></defs>
{chr(10).join(svg)}
</svg>
<footer>Each gold bar is a creed, council, or oath offered as a term of unity. Every stream below it is a church that still exists; widths are suggestive, not to scale. The faded stream died out; the dotted lens is the one breach that healed.</footer>
</body>
</html>
"""
OUT.write_text(html)
print(f"wrote {OUT} ({len(html):,} bytes)")
