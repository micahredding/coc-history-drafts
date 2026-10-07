# -*- coding: utf-8 -*-
# Week 3 deck content — The Declaration & Address. Started 2026-10-06 with the Christendom sequence.
# One division per slide, like a bullet: the year and the instrument as the headline, one line under it
# (need → result), then one click: the split, one body cleaving into two colors.
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
import re, math

def C(name, note=''):   # chapter card
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (name, note))

# ---------- the split illustration ----------
# One circle, cut into slices. A slide has a BEFORE state and an AFTER state, each a list of units;
# a unit = (slice indices, label, color, dying). Slices in the same unit sit flush and share a color,
# so they read as one body. The click moves every slice from its before-unit to its after-unit.
# Cumulative slides (325 → 431 → 451) open on the previous slide's after-state and split one unit again.
W_, H_, CX, CY, R = 1200, 560, 600, 200, 170
def eq(n):            # n equal vertical slices of the circle
    w = 2 * R / n
    return [(CX - R + i * w, CX - R + (i + 1) * w) for i in range(n)]
# the ancient church, carved cumulatively: East · Oriental · Chalcedonian | Arian
ANCIENT = [(CX - R, CX - R / 2), (CX - R / 2, CX - R / 4), (CX - R / 4, CX), (CX, CX + R)]

def _layout(slices, units, gap):
    """Lay units out left→right, centered; return per-slice dx, and per-unit (center x, width)."""
    widths = [sum(slices[i][1] - slices[i][0] for i in u[0]) for u in units]
    total = sum(widths) + gap * (len(units) - 1)
    x = CX - total / 2
    dx = {}; centers = []
    for (idx, lab, col, dying), w in zip(units, widths):
        off = 0
        for i in idx:
            dx[i] = x + off - slices[i][0]
            off += slices[i][1] - slices[i][0]
        centers.append((x + w / 2, w)); x += w + gap
    return dx, centers

def split(slices, pre, post, gap=60):
    dx0, c0 = _layout(slices, pre, gap)
    dx1, c1 = _layout(slices, post, gap)
    col0 = {}; col1 = {}; dy1 = {}
    for idx, lab, col, dying in pre:
        for i in idx: col0[i] = col
    for idx, lab, col, dying in post:
        for i in idx: col1[i] = col; dy1[i] = dying
    out = []
    for i, (xa, xb) in enumerate(slices):
        ya = math.sqrt(max(R * R - (xa - CX) ** 2, 0)); yb = math.sqrt(max(R * R - (xb - CX) ** 2, 0))
        d = ('M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f L%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f Z'
             % (xa, CY - ya, R, R, xb, CY - yb, xb, CY + yb, R, R, xa, CY + ya))
        k0 = 'bone-dim' if col0[i] == 'bone' else col0[i]; k1 = 'bone-dim' if col1[i] == 'bone' else col1[i]
        out.append('<g class="piece%s" style="--dx0:%.0fpx;--dx1:%.0fpx;--k0:var(--%s);--k1:var(--%s)"><path d="%s"/></g>'
                   % (' dying' if dy1[i] else '', dx0[i], dx1[i], k0, k1, d))
    # labels: a unit present in both states keeps its label; otherwise pre labels fade out, post labels fade in
    pre_keys = {tuple(u[0]): u for u in pre}; post_keys = {tuple(u[0]): u for u in post}
    def label(u, center, row, cls):
        idx, lab, col, dying = u
        if not lab: return ''
        x = center; y = CY + R + 52 + row * 44
        lines = lab.split('|')
        return '<text class="plab %s%s" x="%.0f" y="%d" text-anchor="middle">%s</text>' % (
            cls, ' dim' if dying else '', x, y,
            ''.join('<tspan x="%.0f" dy="%d">%s</tspan>' % (x, 0 if j == 0 else 34, l) for j, l in enumerate(lines)))
    st0 = 1 if min(w for _, w in c0) < 120 or len(pre) > 2 else 0     # stagger label rows only when pieces are narrow
    st1 = 1 if min(w for _, w in c1) < 120 or len(post) > 2 else 0
    for k, (u, (cx_, w)) in enumerate(zip(pre, c0)):
        if tuple(u[0]) not in post_keys: out.append(label(u, cx_, (k % 2) * st0, 'pre'))
    for k, (u, (cx_, w)) in enumerate(zip(post, c1)):
        out.append(label(u, cx_, (k % 2) * st1, 'keep' if tuple(u[0]) in pre_keys else 'post'))
    return '<svg class="splitfig" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (W_, H_, ''.join(out))

def two(a, b, ca='c1', cb='c2', dying_b=False):   # a fresh circle splitting in n
    kids = [a, b] if isinstance(a, str) else a
    cols = [ca, cb, 'c3', 'c4']
    sl = eq(len(kids))
    pre = [(list(range(len(kids))), '', 'bone', False)]
    post = [([i], k, cols[i], dying_b and i == len(kids) - 1) for i, k in enumerate(kids)]
    return sl, pre, post

def D(title, line, fig, notes, kind='', cut=False):
    """One division. Headline + line at once; click = the split (+ a second click to heal, if kind='heal')."""
    slices, pre, post = fig
    healer = '<div class="frag healer"></div>' if kind == 'heal' else ''
    return ('<section class="slide divslide%s"><h2>%s</h2>'
            '<div class=line>%s</div>'
            '<div class="failure frag">%s</div>%s'
            '<aside class=notes>%s</aside></section>' % (
                ' cuttable' if cut else '', title, line, split(slices, pre, post), healer, notes))

S = []
A = S.append
_D = __file__.rsplit('/', 1)[0]
FLOW_SVG = re.search(r'<svg.*?</svg>', open(_D + '/../../elements/christendom-divisions.html').read(), re.S).group(0)
# keep the element's class names clear of the deck engine's .sub / .lab / .x rules
FLOW_SVG = FLOW_SVG.replace('class="sub"', 'class="fsub"').replace('class="lab"', 'class="flab"').replace('class="x"', 'class="fx"')
NOTES = {
"325": "Constantine had just reunited the empire (324) and found the church at war over whether the Son is God. He convened the council himself, 325. The creed condemned Arius with the word <i>homoousios</i>.<br>'\n    'Failure: Constantine was baptized on his deathbed (337) by Eusebius of Nicomedia, an Arian sympathizer; his son Constantius pushed the empire Arian; Athanasius exiled five times; Jerome c. 360: &ldquo;the whole world groaned and found itself Arian.&rdquo; The creed people say today is the rewrite of 381. Goths, Vandals and Lombards stayed Arian into the 500s and 600s, then converted.<br>'\n    '&rarr; Say: the first creed written to unite the church did not unite the two sides; it named them.',",
"431": "Nestorius of Constantinople objected to <i>Theotokos</i>; Cyril of Alexandria pressed the council. Cyril&rsquo;s council opened before John of Antioch arrived; John&rsquo;s party held its own council and each deposed the other&rsquo;s leader; Theodosius II arrested both Cyril and Nestorius. A Formula of Reunion patched it in 433.<br>'\n    'Canon 7 of Ephesus: unlawful &ldquo;to bring forward, or to write, or to compose a different faith as a rival to that established by the holy Fathers assembled with the Holy Ghost in Nicaea.&rdquo; This is the ban the next council breaks, and the ban the East cites against the West in 1054.<br>'\n    'The Church of the East (Persia, outside the empire) had adopted Nicaea on its own at Seleucia-Ctesiphon in 410; it refused Ephesus and has been separate ever since. Today: the Assyrian Church of the East.<br>'\n    '&rarr; Plant the canon. &ldquo;We will come back to that.&rdquo;',",
"451": "Chalcedon reaffirmed Ephesus&rsquo;s ban on new creeds, then issued the Definition (&ldquo;in two natures&rdquo;) and said it was a definition, not a creed. The 381 creed is first read into the record here. Egypt, Armenia, Ethiopia, the Syriac churches refused it: the Oriental Orthodox, non-Chalcedonian to this day (Copts, Armenians, Ethiopians, Eritreans, Syriacs, Malankara).<br>'\n    '&rarr; The rhyme to plant: &ldquo;not a new creed.&rdquo; The thirteen propositions will say the same words.',",
"482": "Zeno&rsquo;s Henotikon (482), drafted with Patriarch Acacius, tried to reconcile Chalcedonians and non-Chalcedonians by affirming Nicaea, Ephesus and Cyril and passing over Chalcedon in silence. Pope Felix III excommunicated Acacius (484). Rome and Constantinople were out of communion until 519 (Emperor Justin, the Formula of Hormisdas). It did not win Egypt back either.<br>'\n    'Later imperial compromises did the same thing twice more: 553 (Three Chapters, split the West for 150 years), 638 (Monothelitism, condemned in 680). Not on slides; say it in a sentence if you want the pattern.<br>'\n    '&rarr; A document literally named &ldquo;instrument of union&rdquo; produced the first schism between Rome and Constantinople.',",
"1054": "The Filioque (&ldquo;and the Son&rdquo;) entered the creed in Spain (Toledo 589), spread through the Frankish church, and was adopted at Rome about 1014. The East objected to the content and to the unilateral change, citing Ephesus Canon 7. Cardinal Humbert&rsquo;s legation (1054) also contested leavened bread and papal primacy; on 16 July he laid the bull on the altar; Patriarch Cerularius anathematized the legates. The date is conventional; the estrangement was long and the 1204 sack sealed it. Mutual anathemas lifted 1965, communion not restored.<br>'\n    '&rarr; How do two churches with the same creed divide over the creed? Which version, and who decides.',",
"1530": "1517 the theses; 1521 Worms. The Augsburg Confession (25 June 1530, Melanchthon) was presented to Charles V at an imperial diet called to restore religious unity against the Turkish threat; its first articles affirm Nicaea. The Catholic theologians&rsquo; Confutation (3 August) rejected it; Charles gave the Protestants until April 1531 to submit. Trent (1545&ndash;63) anathematized the Protestant positions.<br>'\n    '&rarr; Shared creed, shared filioque, divided anyway. The creed was never the thing holding them together.',",
"1527": "Disputations January and November 1525; the council ordered infants baptized and rebaptizers banished, then (March 1526) drowned. Felix Manz drowned 5 January 1527, the first Protestant executed by Protestants. Schleitheim (February 1527, Michael Sattler) set out seven articles including believer&rsquo;s baptism and separation from the sword; Sattler burned at Rottenburg that May. Zwingli wrote against Schleitheim the same year.<br>'\n    'Out of order by three years with Augsburg on purpose: Augsburg is the Catholic/Protestant split, this is the first split inside Protestantism.<br>'\n    '&rarr; The first Protestant unity ruling was enforced with the river.',",
"1529": "Marburg Colloquy, 1&ndash;4 October 1529, called by Philip of Hesse to unite the Protestants politically and theologically. The Marburg Articles: agreement on fourteen, and on the fifteenth (the Supper) agreement on everything except whether Christ&rsquo;s body is bodily present. Luther&rsquo;s line to the Swiss: &ldquo;Ihr habt einen andern Geist.&rdquo; Lutheran and Reformed have been separate confessional families since. The Formula of Concord (1577) settled Lutheran infighting by excluding the Reformed.<br>'\n    '&rarr; Thomas Campbell will call the Supper &ldquo;that great ordinance of unity and love.&rdquo; It is the one thing they could not agree on.',",
"1646": "Solemn League and Covenant (1643): Scotland&rsquo;s price for joining Parliament&rsquo;s war was a common Presbyterian settlement for all three kingdoms. The Westminster Assembly (1643&ndash;49) produced the Confession (1646) and catechisms. The Independents (the &ldquo;Dissenting Brethren&rdquo;) argued against Presbyterian government inside the Assembly. Parliament never fully established it in England; the Restoration (1660) restored bishops; the Act of Uniformity (1662) ejected about two thousand ministers, the Great Ejection. Scotland adopted the Confession in 1647 and keeps it.<br>'\n    '&rarr; The confession Thomas Campbell was tried under was written to unite three kingdoms. It produced nonconformity.',",
"1690": "William and Mary&rsquo;s settlement (1690) abolished bishops and established Presbyterianism with the Westminster Confession, but without the Covenants, which the state did not renew. The Cameronians (Society People) refused to enter and became the Reformed Presbyterian Church (1743 as a presbytery). The Episcopalians went out the other side.<br>'\n    'Cuttable: the Secession slide carries the Scottish story on its own.',",
"1733": "The Patronage Act (1712) restored lay patrons&rsquo; right to present ministers. Erskine&rsquo;s synod sermon (October 1732) attacked it; the Assembly rebuked him (1733); he and three others (Wilson, Moncrieff, Fisher) protested, were suspended, and formed the Associate Presbytery (December 1733). Deposed 1740. The Seceders renewed the Covenants; the Week 2 litany note has this.<br>'\n    '&rarr; His tradition began as a protest against imposed authority.',",
"1747": "The oath, required of burgesses in Edinburgh, Glasgow and Perth: &ldquo;the true religion presently professed within this realm and authorized by the laws thereof.&rdquo; Burghers: it means only &ldquo;not Catholic.&rdquo; Anti-Burghers: it blesses the church we left. The synod split April 1747 (Associate Synod vs General Associate Synod); the Anti-Burghers excommunicated the Burghers (1748&ndash;49), and the two could not take communion together. Thomas Campbell was Anti-Burgher. The Week 2 litany note covers why it felt so large (the Testimony, the Covenants).<br>'\n    '&rarr; This is the rule Conemaugh broke, and the room already knows it.',",
"1799": "The Burghers split 1799 (Original Burghers, Old Light), the Anti-Burghers 1806 (Constitutional Associate Presbytery, Old Light) over whether the civil magistrate has power in religion (Westminster Confession ch. 23). Campbell sided with the Old Lights by friendship more than conviction (Foster; Week 2 note). He sailed April 1807.<br>'\n    'Cuttable: the Week 2 litany already told this. Keep if the room needs the landing.',"
}

# ---------- CHRISTENDOM'S SEARCH FOR UNITY ----------
A(C('Christendom&rsquo;s Search for Unity',
    'Card. Lands after the Preamble&rsquo;s despair (&ldquo;amid the diversity and rancor of party contentions&rdquo;) and before &ldquo;anywhere but in Christ.&rdquo; One click per slide. Eight to ten minutes with every slide; 1690 and 1799 are marked cuttable in their notes.'))

A(D('325 &middot; Council of Nicaea',
    'Arians against non-Arians. A creed, and fifty-six more years of war.',
    (ANCIENT, [([0, 1, 2, 3], '', 'bone', False)],
              [([0, 1, 2], 'Nicene', 'c1', False), ([3], 'Arian', 'c1', True)]), NOTES['325']))

A(D('431 &middot; Council of Ephesus',
    'Does Mary bear God? A canon forbidding new creeds, and the Church of the East gone.',
    (ANCIENT, [([0, 1, 2], 'Nicene', 'c1', False), ([3], 'Arian', 'c1', True)],
              [([0], 'Church of|the East', 'c3', False), ([1, 2], 'the imperial|Church', 'c1', False), ([3], 'Arian', 'c1', True)]), NOTES['431']))

A(D('451 &middot; Council of Chalcedon',
    'One nature or two? A Definition, &ldquo;not a new creed,&rdquo; and Egypt gone.',
    (ANCIENT, [([0], 'Church of|the East', 'c3', False), ([1, 2], 'the imperial|Church', 'c1', False), ([3], 'Arian', 'c1', True)],
              [([0], 'Church of|the East', 'c3', False), ([1], 'Oriental|Orthodox', 'c2', False), ([2], 'Chalcedonian', 'c1', False), ([3], 'Arian', 'c1', True)]), NOTES['451']))

A(D('482 &middot; The Henotikon',
    'Zeno needs Egypt back. An &ldquo;instrument of union,&rdquo; and thirty-five years of schism with Rome.',
    two('Rome', 'Constantinople'), NOTES['482'], kind='heal'))

A(D('1054 &middot; The Filioque',
    'One word added to the creed. Legates sent to settle it, and East and West apart.',
    two('Catholic West', 'Orthodox East'), NOTES['1054']))

A(D('1530 &middot; The Augsburg Confession',
    'Luther&rsquo;s protest. A confession offered as the basis for peace, and the West in two.',
    two('Catholic', 'Protestant'), NOTES['1530']))

A(D('1527 &middot; Zurich',
    'Infant baptism and the sword. A council ruling, and Felix Manz drowned.',
    two('Reformed', 'Anabaptists'), NOTES['1527']))

A(D('1529 &middot; The Marburg Colloquy',
    'The Lord&rsquo;s Supper. Fourteen articles agreed, and &ldquo;you have a different spirit.&rdquo;',
    two('Lutheran', 'Reformed'), NOTES['1529']))

A(D('1646 &middot; The Westminster Confession',
    'Three kingdoms at war. One confession for all three, and two thousand ministers ejected.',
    two(['Church of|England', 'Independents', 'Church of|Scotland'], None), NOTES['1646']))

A(D('1690 &middot; The Revolution Settlement',
    'Scotland after the Revolution. Presbytery restored, and the Covenanters outside.',
    two('Church of Scotland', 'Covenanters'), NOTES['1690'], cut=True))

A(D('1733 &middot; The Secession',
    'Patrons appoint ministers. Erskine rebuked, and four ministers walk out.',
    two('Church of Scotland', 'the Seceders'), NOTES['1733']))

A(D('1747 &middot; The Burgess Oath',
    'May a Seceder swear it? A synod vote, and mutual excommunication.',
    two('Burgher', 'Anti-Burgher'), NOTES['1747']))

A(D('1799 &middot; 1806 &middot; Old Light, New Light',
    'May the magistrate enforce religion? Revised Testimonies, and each synod in two.',
    two(['Old Light', 'New Light', 'Old Light', 'New Light'], None), NOTES['1799'], cut=True))

A('<section class="slide flowslide"><div class="eyebrow quiet">325&ndash;1806</div>' + FLOW_SVG +
  '<aside class=notes>The whole picture at once. One river, and every gold bar is a creed, council, oath or settlement offered as a term of unity. Widths are suggestive, not to scale. The faded stream is the Arians; the dotted lens is the Henotikon, the one breach that healed.<br>'
  '&rarr; All of these, as informative and enlightening as they are, did not produce unity. They could not produce it even among those who agreed on them.</aside></section>')

A('<section class="slide"><h2>What can Christians unite on?</h2>'
  '<div class="sub frag">He prayed that they would be one. So it must be possible.</div>'
  '<aside class=notes>John 17:21, a prayer, not a command. Then back to the Preamble: &ldquo;nor, indeed, can we reasonably expect to find it anywhere but in Christ and his simple word.&rdquo;<br>&rarr; Your close is yours. The slide stops at the question.</aside></section>')

A('<section class="slide"><aside class=notes>Black. Then the Preamble&rsquo;s last sentence.</aside></section>')
