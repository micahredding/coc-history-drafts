#!/usr/bin/env python3
"""Christendom's divisions, 325–1806 — a branching timeline for Week 3 (Declaration & Address).

Generates decks/elements/christendom-divisions.html: a single SVG in the class's visual world
(night field, bone paper, candle gold). Each split names the instrument of unity that caused it.
Only church-vs-church divisions are drawn. Run from anywhere:

    python3 decks/src/elements/christendom-divisions.py
"""
from pathlib import Path

W, H = 1800, 1270
OUT = Path(__file__).resolve().parents[2] / "elements" / "christendom-divisions.html"

# ---- lanes (x) ------------------------------------------------------------
X = dict(
    arian=120, east=230, oriental=340, orthodox=450, rome=560,
    lutheran=690, anglican=810, independent=920, reformed=1030,
    covenanter=1140, scotland=1250, burgher_old=1350, burgher_new=1440,
    antib_old=1540, antib_new=1630, anabaptist=1740,
)
SEC = 1490   # Seceder trunk 1733–1747
BUR = 1395   # Burgher trunk 1747–1799
ANB = 1585   # Anti-Burgher trunk 1747–1806

# ---- rows (y), ordinal not linear ------------------------------------------
Y = dict(top=70, n325=170, n431=250, n451=330, n482=400, n519=460, n1054=545,
         n1517=650, n1527=705, n1529=765, n1646=845, n1690=905, n1733=955,
         n1747=1005, n1799=1055, n1806=1090, end=1150)
LEAF_Y = 1172

svg = []
def add(s): svg.append(s)

def line(x1, y1, x2, y2, cls="lane"):
    add(f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')

def branch(x0, y0, x1, drop=40, cls="lane"):
    """Curve from the parent at (x0,y0) to the child lane x1, landing drop px lower."""
    y1 = y0 + drop
    add(f'<path class="{cls}" d="M{x0},{y0} C{x0},{y0+drop*0.9} {x1},{y0+drop*0.1} {x1},{y1}"/>')
    return y1

def node(x, y, kind="split"):
    r = 7 if kind == "split" else 6
    add(f'<circle class="node {kind}" cx="{x}" cy="{y}" r="{r}"/>')

def label(x, y, year, title, sub=None, anchor="start", boxed=False):
    """Event label: year (small caps gold), instrument (italic), who it lost (small)."""
    lines = [f'<tspan class="yr">{year}</tspan> <tspan class="ttl">{title}</tspan>']
    if sub:
        for s in sub.split("|"):
            lines.append(f'<tspan class="sub" x="{x}" dy="19">{s.strip()}</tspan>')
    body = "".join(f'<tspan x="{x}" dy="{0 if i==0 else 0}">{l}</tspan>' if i == 0 else l for i, l in enumerate(lines))
    cls = "lab boxed" if boxed else "lab"
    add(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{body}</text>')

def leaf(key, name, stagger=0):
    x = X[key]
    parts = name.split("|")
    t = [f'<tspan x="{x}" dy="{0 if i==0 else 16}">{p.strip()}</tspan>' for i, p in enumerate(parts)]
    add(f'<text class="leaf" x="{x}" y="{LEAF_Y + stagger}" text-anchor="middle">{"".join(t)}</text>')

def trunklabel(x, y, text, anchor="start"):
    add(f'<text class="trunk" x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>')

# ============================================================================
# The one Church → Rome (x=560 runs top to bottom)
line(X["rome"], Y["top"], X["rome"], Y["end"], "lane main")
trunklabel(X["rome"] + 14, Y["top"] + 6, "the one Church")

# 325 Nicaea → Arians (dies out)
node(X["rome"], Y["n325"]); y = branch(X["rome"], Y["n325"], X["arian"])
line(X["arian"], y, X["arian"], 500, "lane dying")
add(f'<text class="x" x="{X["arian"]}" y="{512}" text-anchor="middle">×</text>')
label(X["rome"] + 22, Y["n325"] + 5, "325", "Nicaea — the Nicene Creed",
      "lost the Arians · war for 56 more years | Arian kingdoms persist until c. 650")

# 431 Ephesus → Church of the East
node(X["rome"], Y["n431"]); y = branch(X["rome"], Y["n431"], X["east"])
line(X["east"], y, X["east"], Y["end"])
label(X["rome"] + 22, Y["n431"] + 5, "431", "Ephesus — Canon 7: no new creed, ever",
      "lost the Church of the East (Persia)")

# 451 Chalcedon → Oriental Orthodox
node(X["rome"], Y["n451"]); y = branch(X["rome"], Y["n451"], X["oriental"])
line(X["oriental"], y, X["oriental"], Y["end"])
label(X["rome"] + 22, Y["n451"] + 5, "451", "Chalcedon — the Definition, “not a new creed”",
      "lost Egypt, Armenia, Ethiopia, Syria")

# 482 Henotikon → Acacian schism (healed 519): a dashed strand beside the trunk
node(X["rome"], Y["n482"], "heal")
add(f'<path class="lane schism" d="M{X["rome"]},{Y["n482"]} C{X["rome"]},{Y["n482"]+18} {X["rome"]+28},{Y["n482"]+10} {X["rome"]+28},{Y["n482"]+26} '
    f'L{X["rome"]+28},{Y["n519"]-26} C{X["rome"]+28},{Y["n519"]-10} {X["rome"]},{Y["n519"]-18} {X["rome"]},{Y["n519"]}"/>')
node(X["rome"], Y["n519"], "heal")
label(X["rome"] + 50, Y["n482"] + 5, "482", "the Henotikon — “instrument of union”",
      "Rome and Constantinople out of communion 484–519 · healed")

# 1054 Filioque → Orthodox
node(X["rome"], Y["n1054"]); y = branch(X["rome"], Y["n1054"], X["orthodox"])
line(X["orthodox"], y, X["orthodox"], Y["end"])
label(X["rome"] + 22, Y["n1054"] + 5, "1054", "the Filioque — the creed itself",
      "East and West: which wording, and who decides")
trunklabel(X["rome"] + 14, Y["n1054"] + 46, "Rome · the West")

# 1517 Reformation → Protestants (trunk moves to x=1030)
node(X["rome"], Y["n1517"]); y = branch(X["rome"], Y["n1517"], X["reformed"], drop=50)
line(X["reformed"], y, X["reformed"], Y["end"])
label(X["rome"] + 22, Y["n1517"] - 30, "1517", "the Reformation",
      "same creed, same filioque, divided anyway")
trunklabel(X["reformed"] + 14, Y["n1517"] + 62, "Protestants")

# 1527 Zurich → Anabaptists
node(X["reformed"], Y["n1527"]); y = branch(X["reformed"], Y["n1527"], X["anabaptist"], drop=45)
line(X["anabaptist"], y, X["anabaptist"], Y["end"])
label(X["reformed"] - 22, Y["n1527"] + 5, "1527", "Zurich — Felix Manz drowned",
      "lost the Anabaptists", anchor="end")

# 1529 Marburg → Lutheran | Reformed
node(X["reformed"], Y["n1529"]); y = branch(X["reformed"], Y["n1529"], X["lutheran"])
line(X["lutheran"], y, X["lutheran"], Y["end"])
label(X["reformed"] + 22, Y["n1529"] + 5, "1529", "Marburg — fourteen articles agreed, the Supper not",
      "Lutheran and Reformed part · “you have a different spirit”")
trunklabel(X["reformed"] + 14, Y["n1529"] + 62, "Reformed")

# 1646 Westminster → Church of England | Independents | Church of Scotland
node(X["reformed"], Y["n1646"])
y = branch(X["reformed"], Y["n1646"], X["anglican"]);    line(X["anglican"], y, X["anglican"], Y["end"])
y = branch(X["reformed"], Y["n1646"], X["independent"]); line(X["independent"], y, X["independent"], Y["end"])
y = branch(X["reformed"], Y["n1646"], X["scotland"]);    line(X["scotland"], y, X["scotland"], Y["end"])
label(X["scotland"] + 22, Y["n1646"] - 20, "1646", "Westminster — one confession for three kingdoms",
      "England never adopted it · the Independents dissented in the room | 1662: two thousand ministers ejected")

# 1690 Revolution settlement → Covenanters
node(X["scotland"], Y["n1690"]); y = branch(X["scotland"], Y["n1690"], X["covenanter"])
line(X["covenanter"], y, X["covenanter"], Y["end"])
label(X["scotland"] + 22, Y["n1690"] + 5, "1690", "the Revolution Settlement",
      "lost the Covenanters")

# 1733 Secession → Seceder trunk
node(X["scotland"], Y["n1733"]); y = branch(X["scotland"], Y["n1733"], SEC, drop=45)
line(SEC, y, SEC, Y["n1747"])
label(SEC + 22, Y["n1733"] + 5, "1733", "the Secession — Ebenezer Erskine",
      "over patronage")

# 1747 Burgess Oath → Burgher | Anti-Burgher
node(SEC, Y["n1747"])
y = branch(SEC, Y["n1747"], BUR, drop=35); line(BUR, y, BUR, Y["n1799"])
y = branch(SEC, Y["n1747"], ANB, drop=35); line(ANB, y, ANB, Y["n1806"])
label(ANB + 22, Y["n1747"] + 5, "1747", "the Burgess Oath", "Burgher and Anti-Burgher", boxed=True)
add(f'<text class="trunk tc" x="{ANB + 14}" y="{Y["n1747"] + 66}" text-anchor="start">Thomas Campbell’s synod</text>')

# 1799 / 1806 Old Light | New Light
node(BUR, Y["n1799"])
y = branch(BUR, Y["n1799"], X["burgher_old"], drop=30); line(X["burgher_old"], y, X["burgher_old"], Y["end"])
y = branch(BUR, Y["n1799"], X["burgher_new"], drop=30); line(X["burgher_new"], y, X["burgher_new"], Y["end"])
node(ANB, Y["n1806"])
y = branch(ANB, Y["n1806"], X["antib_old"], drop=30); line(X["antib_old"], y, X["antib_old"], Y["end"])
y = branch(ANB, Y["n1806"], X["antib_new"], drop=30); line(X["antib_new"], y, X["antib_new"], Y["end"])
label(BUR - 60, Y["n1799"] + 5, "1799 · 1806", "Old Light and New Light",
      "each Seceder body splits again | the year before he sailed", anchor="end", boxed=True)

# ---- leaves ---------------------------------------------------------------
leaf("east", "Church of|the East")
leaf("oriental", "Oriental|Orthodox", 18)
leaf("orthodox", "Eastern|Orthodox")
leaf("rome", "Roman|Catholic", 18)
leaf("lutheran", "Lutheran")
leaf("anglican", "Church of|England", 18)
leaf("independent", "Independents")
leaf("reformed", "Continental|Reformed", 18)
leaf("covenanter", "Covenanters")
leaf("scotland", "Church of|Scotland", 18)
leaf("burgher_old", "Burgher|Old Light")
leaf("burgher_new", "Burgher|New Light", 18)
leaf("antib_old", "Anti-Burgher|Old Light")
leaf("antib_new", "Anti-Burgher|New Light", 18)
leaf("anabaptist", "Anabaptists")

# ---- assemble --------------------------------------------------------------
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
  header{{width:min(96vw,1800px);margin-bottom:1.2vmin}}
  .eyebrow{{font-family:'IM Fell English SC',Georgia,serif;font-size:clamp(11px,1.4vmin,15px);letter-spacing:.26em;color:var(--smoke)}}
  h1{{font-family:'IM Fell English',Georgia,serif;font-weight:400;font-size:clamp(22px,3.6vmin,40px);line-height:1.1;color:var(--bone)}}
  h1 em{{font-style:italic;color:var(--gold)}}
  svg{{width:min(96vw,1800px);height:auto;display:block}}
  .lane{{fill:none;stroke:var(--bone-dim);stroke-width:2;stroke-linecap:round}}
  .lane.main{{stroke:var(--bone);stroke-width:3}}
  .lane.dying{{stroke:var(--smoke);stroke-dasharray:3 7}}
  .lane.schism{{stroke:var(--gold-dim);stroke-dasharray:4 6}}
  .node{{fill:var(--ground);stroke:var(--gold);stroke-width:2.5}}
  .node.heal{{fill:var(--gold-dim);stroke:var(--gold-dim)}}
  .x{{font-family:'IM Fell English',Georgia,serif;font-size:22px;fill:var(--smoke)}}
  .lab{{font-size:16px;fill:var(--bone-dim)}}
  .lab .yr{{font-family:'IM Fell English SC',Georgia,serif;font-size:16px;letter-spacing:.14em;fill:var(--gold)}}
  .lab .ttl{{font-family:'IM Fell English',Georgia,serif;font-style:italic;font-size:21px;fill:var(--bone)}}
  .lab .sub{{font-family:'Spectral',Georgia,serif;font-size:15px;fill:var(--bone-dim)}}
  .lab.boxed{{paint-order:stroke;stroke:var(--ground);stroke-width:9px;stroke-linejoin:round}}
  .lab.boxed .yr,.lab.boxed .ttl,.lab.boxed .sub{{paint-order:stroke;stroke:var(--ground);stroke-width:9px;stroke-linejoin:round}}
  .leaf{{font-family:'IM Fell English',Georgia,serif;font-size:15px;fill:var(--bone)}}
  .trunk{{font-family:'IM Fell English SC',Georgia,serif;font-size:13px;letter-spacing:.16em;fill:var(--smoke)}}
  .trunk.tc{{fill:var(--gold-dim);paint-order:stroke;stroke:var(--ground);stroke-width:8px;stroke-linejoin:round}}
  footer{{width:min(96vw,1800px);margin-top:1vmin;font-family:'IM Fell English',Georgia,serif;font-style:italic;font-size:clamp(11px,1.5vmin,16px);color:var(--smoke)}}
</style>
</head>
<body>
<header>
  <div class="eyebrow">Christendom’s search for unity · 325–1806</div>
  <h1>Every instrument of unity drew a <em>border</em></h1>
</header>
<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A branching timeline of church divisions from Nicaea in 325 to the Seceder splits of 1806, each labeled with the creed, council, or oath that caused it.">
{chr(10).join(svg)}
</svg>
<footer>Each dot is a creed, council, or oath offered as a term of unity. Each branch is a church that still exists. The dotted branch died out; the gold loop is the one breach that healed.</footer>
</body>
</html>
"""
OUT.write_text(html)
print(f"wrote {OUT} ({len(html):,} bytes)")
