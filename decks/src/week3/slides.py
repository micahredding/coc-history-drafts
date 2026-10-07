# -*- coding: utf-8 -*-
# Week 3 deck content — The Declaration & Address. Started 2026-10-06 with the Christendom sequence.
# One division per slide: the issue shows at once; click 1 = the attempt; click 2 = the fork.
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
import re

def N(*bul):   # speaker notes as bullets, closing the section
    return '<aside class=notes>' + '<br>'.join('&bull; '+x for x in bul) + '</aside></section>'

def C(name, note=''):   # chapter card
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (name, note))

# ---------- the fork illustration ----------
# A ribbon that divides: the same visual language as elements/christendom-divisions.html.
# kids = [(label, weight, kind)]  kind: '' | 'dies'.  kind='heal' on the fork: the two rejoin below.
def fork(parent, kids, bar='', kind=''):
    W, H = 1000, 400
    top, y, drop, end = 40, 170, 60, 330
    gap = 46
    tw = sum(k[1] for k in kids)
    pw = 560
    px0 = (W - pw) / 2; px1 = px0 + pw
    out = []
    out.append('<path class="rib" d="M%.0f,%d L%.0f,%d L%.0f,%d L%.0f,%d Z"/>' % (px0, top, px0, y, px1, y, px1, top))
    out.append('<text class="rlab" x="%d" y="%d" text-anchor="middle">%s</text>' % (W/2, (top + y)/2 + 10, parent))
    out.append('<line class="bar" x1="%.0f" y1="%d" x2="%.0f" y2="%d"/>' % (px0, y, px1, y))
    if bar:
        out.append('<text class="blab" x="%d" y="%d" text-anchor="middle">%s</text>' % (W/2, y - 12, bar))
    total_lane = pw + gap * (len(kids) - 1)
    lx = (W - total_lane) / 2
    sx = px0
    for i, (lab, wt, kk) in enumerate(kids):
        w = pw * wt / tw
        sx0, sx1 = sx, sx + w
        x0, x1 = lx, lx + w
        ye = end
        cls = 'rib' + (' dying' if kk == 'dies' else '')
        out.append('<path class="%s" d="M%.0f,%d C%.0f,%d %.0f,%d %.0f,%d L%.0f,%d L%.0f,%d L%.0f,%d C%.0f,%d %.0f,%d %.0f,%d Z"/>' % (
            cls, sx0, y, sx0, y + drop/2, x0, y + drop/2, x0, y + drop, x0, ye, x1, ye, x1, y + drop, x1, y + drop/2, sx1, y + drop/2, sx1, y))
        lines = lab.split('|')
        ty = (ye - 22) if kind == 'heal' else (ye + 34)
        out.append('<text class="rlab%s" x="%.0f" y="%d" text-anchor="middle">%s</text>' % (
            ' dim' if kk == 'dies' else '', (x0 + x1)/2, ty,
            ''.join('<tspan x="%.0f" dy="%d">%s</tspan>' % ((x0 + x1)/2, 0 if j == 0 else 30, l) for j, l in enumerate(lines))))
        if kk == 'dies':
            out.append('<text class="xx" x="%.0f" y="%d" text-anchor="middle">&times;</text>' % ((x0 + x1)/2, ye - 8))
        sx += w; lx += w + gap
    if kind == 'heal':
        l0 = (W - total_lane)/2; l1 = (W + total_lane)/2
        out.append('<path class="rib heal" d="M%.0f,%d C%.0f,%d %.0f,%d %.0f,%d L%.0f,%d C%.0f,%d %.0f,%d %.0f,%d Z"/>' % (
            l0, end, l0, end + 30, px0, end + 30, px0, end + 58, px1, end + 58, px1, end + 30, l1, end + 30, l1, end))
        out.append('<line class="bar heal" x1="%.0f" y1="%d" x2="%.0f" y2="%d"/>' % (px0, end + 58, px1, end + 58))
        out.append('<text class="blab" x="%d" y="%d" text-anchor="middle">519 &middot; healed</text>' % (W/2, end + 90))
    return ('<svg class="forkfig" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (W, H + (70 if kind == 'heal' else 0), ''.join(out)))

def D(eyebrow, issue, attempt, parent, kids, caption, notes, bar='', kind='', cut=False):
    """One division: issue at once; click = the attempt; click = the fork + caption."""
    return ('<section class="slide divslide%s"><div class=eyebrow>%s</div>'
            '<h2>%s</h2>'
            '<div class="attempt frag"><span class=k>The attempt</span>%s</div>'
            '<div class="failure frag">%s<div class=cap>%s</div></div>'
            '<aside class=notes>%s</aside></section>' % (
                ' cuttable' if cut else '', eyebrow, issue, attempt, fork(parent, kids, bar, kind), caption, notes))

S = []
A = S.append
_D = __file__.rsplit('/', 1)[0]
FLOW_SVG = re.search(r'<svg.*?</svg>', open(_D + '/../../elements/christendom-divisions.html').read(), re.S).group(0)
# keep the element's class names clear of the deck engine's .sub / .lab / .x rules
FLOW_SVG = FLOW_SVG.replace('class="sub"', 'class="fsub"').replace('class="lab"', 'class="flab"').replace('class="x"', 'class="fx"')

# ---------- CHRISTENDOM'S SEARCH FOR UNITY ----------
A(C('Christendom&rsquo;s Search for Unity',
    'Card. Lands after the Preamble&rsquo;s despair (&ldquo;amid the diversity and rancor of party contentions&rdquo;) and before &ldquo;anywhere but in Christ.&rdquo; Eight to twelve minutes if every slide is kept; the two marked cuttable in notes are 1690 and 1799.'))

A(D('325 &middot; Nicaea',
    'The empire is divided between Arians and non-Arians.',
    'Constantine calls every bishop to Nicaea. The first draft of the Nicene Creed.',
    'the Church', [('Nicene', 1.3, ''), ('Arian', 1, 'dies')],
    'Arius is condemned. The war goes on for fifty-six more years. Arian kingdoms last until about 650.',
    'Constantine had just reunited the empire (324) and found the church at war over whether the Son is God. He convened the council himself, 325. The creed condemned Arius with the word <i>homoousios</i>.<br>'
    'Failure: Constantine was baptized on his deathbed (337) by Eusebius of Nicomedia, an Arian sympathizer; his son Constantius pushed the empire Arian; Athanasius exiled five times; Jerome c. 360: &ldquo;the whole world groaned and found itself Arian.&rdquo; The creed people say today is the rewrite of 381. Goths, Vandals and Lombards stayed Arian into the 500s and 600s, then converted.<br>'
    '&rarr; Say: the first creed written to unite the church did not unite the two sides; it named them.',
    bar='the Nicene Creed'))

A(D('431 &middot; Ephesus',
    'Alexandria and Antioch are divided over whether Mary bore God.',
    'The Council of Ephesus. And a canon: no one may ever compose another creed.',
    'the Church', [('the imperial Church', 1.6, ''), ('the Church|of the East', 1, '')],
    'Two rival councils meet in the same city and excommunicate each other. The Church of the East walks away. It still exists.',
    'Nestorius of Constantinople objected to <i>Theotokos</i>; Cyril of Alexandria pressed the council. Cyril&rsquo;s council opened before John of Antioch arrived; John&rsquo;s party held its own council and each deposed the other&rsquo;s leader; Theodosius II arrested both Cyril and Nestorius. A Formula of Reunion patched it in 433.<br>'
    'Canon 7 of Ephesus: unlawful &ldquo;to bring forward, or to write, or to compose a different faith as a rival to that established by the holy Fathers assembled with the Holy Ghost in Nicaea.&rdquo; This is the ban the next council breaks, and the ban the East cites against the West in 1054.<br>'
    'The Church of the East (Persia, outside the empire) had adopted Nicaea on its own at Seleucia-Ctesiphon in 410; it refused Ephesus and has been separate ever since. Today: the Assyrian Church of the East.<br>'
    '&rarr; Plant the canon. &ldquo;We will come back to that.&rdquo;',
    bar='Canon 7: no new creed'))

A(D('451 &middot; Chalcedon',
    'One nature or two? Egypt against the capital.',
    'The Council of Chalcedon writes a Definition, insisting it is not a new creed.',
    'the Church', [('Chalcedonian', 1.6, ''), ('Oriental Orthodox|Egypt &middot; Armenia &middot; Ethiopia &middot; Syria', 1.2, '')],
    'The largest split yet. Still unhealed, fifteen centuries later.',
    'Chalcedon reaffirmed Ephesus&rsquo;s ban on new creeds, then issued the Definition (&ldquo;in two natures&rdquo;) and said it was a definition, not a creed. The 381 creed is first read into the record here. Egypt, Armenia, Ethiopia, the Syriac churches refused it: the Oriental Orthodox, non-Chalcedonian to this day (Copts, Armenians, Ethiopians, Eritreans, Syriacs, Malankara).<br>'
    '&rarr; The rhyme to plant: &ldquo;not a new creed.&rdquo; The thirteen propositions will say the same words.',
    bar='the Definition, &ldquo;not a new creed&rdquo;'))

A(D('482 &middot; Constantinople',
    'Emperor Zeno needs Egypt back.',
    'The Henotikon, the &ldquo;instrument of union&rdquo;: a formula of faith that does not mention Chalcedon.',
    'the Church', [('Rome', 1, ''), ('Constantinople', 1, '')],
    'Rome excommunicates the patriarch. The Acacian schism lasts thirty-five years. The one breach that heals.',
    'Zeno&rsquo;s Henotikon (482), drafted with Patriarch Acacius, tried to reconcile Chalcedonians and non-Chalcedonians by affirming Nicaea, Ephesus and Cyril and passing over Chalcedon in silence. Pope Felix III excommunicated Acacius (484). Rome and Constantinople were out of communion until 519 (Emperor Justin, the Formula of Hormisdas). It did not win Egypt back either.<br>'
    'Later imperial compromises did the same thing twice more: 553 (Three Chapters, split the West for 150 years), 638 (Monothelitism, condemned in 680). Not on slides; say it in a sentence if you want the pattern.<br>'
    '&rarr; A document literally named &ldquo;instrument of union&rdquo; produced the first schism between Rome and Constantinople.',
    bar='the Henotikon', kind='heal'))

A(D('1054 &middot; Constantinople',
    'East and West say the same creed, and the West has added a word.',
    'Pope Leo IX sends legates to Constantinople to settle the Filioque and the authority to add it.',
    'the Church', [('Catholic West', 1.4, ''), ('Orthodox East', 1, '')],
    'The legates lay a bull of excommunication on the altar of Hagia Sophia. Still separate.',
    'The Filioque (&ldquo;and the Son&rdquo;) entered the creed in Spain (Toledo 589), spread through the Frankish church, and was adopted at Rome about 1014. The East objected to the content and to the unilateral change, citing Ephesus Canon 7. Cardinal Humbert&rsquo;s legation (1054) also contested leavened bread and papal primacy; on 16 July he laid the bull on the altar; Patriarch Cerularius anathematized the legates. The date is conventional; the estrangement was long and the 1204 sack sealed it. Mutual anathemas lifted 1965, communion not restored.<br>'
    '&rarr; How do two churches with the same creed divide over the creed? Which version, and who decides.',
    bar='the Filioque'))

A(D('1530 &middot; Augsburg',
    'Luther&rsquo;s protest has spread. The Western church is dividing over the gospel itself.',
    'The Augsburg Confession: the Protestants present their faith to the Emperor as a basis for peace. Same creed, same filioque.',
    'the Western Church', [('Catholic', 1.5, ''), ('Protestant', 1.1, '')],
    'Rome answers with a Confutation. The Emperor orders submission. Trent closes the door.',
    '1517 the theses; 1521 Worms. The Augsburg Confession (25 June 1530, Melanchthon) was presented to Charles V at an imperial diet called to restore religious unity against the Turkish threat; its first articles affirm Nicaea. The Catholic theologians&rsquo; Confutation (3 August) rejected it; Charles gave the Protestants until April 1531 to submit. Trent (1545&ndash;63) anathematized the Protestant positions.<br>'
    '&rarr; Shared creed, shared filioque, divided anyway. The creed was never the thing holding them together.',
    bar='the Augsburg Confession'))

A(D('1527 &middot; Zurich',
    'Zurich&rsquo;s reformers divide over infant baptism and the sword.',
    'Public disputations before the city council, which rules for infant baptism. The dissenters answer with the Schleitheim Confession.',
    'Reformed Zurich', [('Reformed', 1.6, ''), ('Anabaptists', 1, '')],
    'Felix Manz is drowned in the Limmat, January 1527: a Protestant killed by Protestants.',
    'Disputations January and November 1525; the council ordered infants baptized and rebaptizers banished, then (March 1526) drowned. Felix Manz drowned 5 January 1527, the first Protestant executed by Protestants. Schleitheim (February 1527, Michael Sattler) set out seven articles including believer&rsquo;s baptism and separation from the sword; Sattler burned at Rottenburg that May. Zwingli wrote against Schleitheim the same year.<br>'
    'Out of order by three years with Augsburg on purpose: Augsburg is the Catholic/Protestant split, this is the first split inside Protestantism.<br>'
    '&rarr; The first Protestant unity ruling was enforced with the river.',
    bar='the council&rsquo;s ruling'))

A(D('1529 &middot; Marburg',
    'Lutherans and Swiss divided over the Lord&rsquo;s Supper.',
    'Philip of Hesse brings Luther and Zwingli to Marburg. They agree on fourteen articles of fifteen.',
    'Protestants', [('Lutheran', 1.2, ''), ('Reformed', 1.2, '')],
    'On the Supper, Luther: &ldquo;You have a different spirit.&rdquo; The ordinance of unity divides them.',
    'Marburg Colloquy, 1&ndash;4 October 1529, called by Philip of Hesse to unite the Protestants politically and theologically. The Marburg Articles: agreement on fourteen, and on the fifteenth (the Supper) agreement on everything except whether Christ&rsquo;s body is bodily present. Luther&rsquo;s line to the Swiss: &ldquo;Ihr habt einen andern Geist.&rdquo; Lutheran and Reformed have been separate confessional families since. The Formula of Concord (1577) settled Lutheran infighting by excluding the Reformed.<br>'
    '&rarr; Thomas Campbell will call the Supper &ldquo;that great ordinance of unity and love.&rdquo; It is the one thing they could not agree on.',
    bar='the Marburg Articles'))

A(D('1646 &middot; Westminster',
    'Three kingdoms, three church settlements, and a civil war.',
    'The Solemn League and Covenant, then the Westminster Confession: one confession for England, Scotland and Ireland.',
    'the Reformed churches of Britain', [('Church of|England', 1.3, ''), ('Independents', 1, ''), ('Church of|Scotland', 1.2, '')],
    'England never adopts it. The Independents dissent inside the Assembly. 1662: two thousand ministers ejected.',
    'Solemn League and Covenant (1643): Scotland&rsquo;s price for joining Parliament&rsquo;s war was a common Presbyterian settlement for all three kingdoms. The Westminster Assembly (1643&ndash;49) produced the Confession (1646) and catechisms. The Independents (the &ldquo;Dissenting Brethren&rdquo;) argued against Presbyterian government inside the Assembly. Parliament never fully established it in England; the Restoration (1660) restored bishops; the Act of Uniformity (1662) ejected about two thousand ministers, the Great Ejection. Scotland adopted the Confession in 1647 and keeps it.<br>'
    '&rarr; The confession Thomas Campbell was tried under was written to unite three kingdoms. It produced nonconformity.',
    bar='the Westminster Confession'))

A(D('1690 &middot; Scotland',
    'Scotland after the Revolution: Episcopalians, Presbyterians, Covenanters.',
    'The Revolution Settlement re-establishes the Presbyterian Church of Scotland on the Westminster Confession.',
    'Church of Scotland', [('Church of Scotland', 1.6, ''), ('Covenanters', 1, '')],
    'The Covenanters refuse a church that has not renewed the Covenants. Still separate.',
    'William and Mary&rsquo;s settlement (1690) abolished bishops and established Presbyterianism with the Westminster Confession, but without the Covenants, which the state did not renew. The Cameronians (Society People) refused to enter and became the Reformed Presbyterian Church (1743 as a presbytery). The Episcopalians went out the other side.<br>'
    'Cuttable: the Secession slide carries the Scottish story on its own.',
    bar='the Revolution Settlement', cut=True))

A(D('1733 &middot; Scotland',
    'Patrons appoint ministers that congregations never called.',
    'The General Assembly upholds patronage and rebukes Ebenezer Erskine for preaching against it.',
    'Church of Scotland', [('Church of Scotland', 1.6, ''), ('the Secession', 1, '')],
    'Four ministers walk out and form the Associate Presbytery. Thomas Campbell&rsquo;s tradition begins here.',
    'The Patronage Act (1712) restored lay patrons&rsquo; right to present ministers. Erskine&rsquo;s synod sermon (October 1732) attacked it; the Assembly rebuked him (1733); he and three others (Wilson, Moncrieff, Fisher) protested, were suspended, and formed the Associate Presbytery (December 1733). Deposed 1740. The Seceders renewed the Covenants; the Week 2 litany note has this.<br>'
    '&rarr; His tradition began as a protest against imposed authority.',
    bar='the Assembly&rsquo;s rebuke'))

A(D('1747 &middot; the Burgess Oath',
    'Burgesses in three cities must swear to &ldquo;the true religion presently professed within this realm.&rdquo;',
    'The Associate Synod votes on whether a Seceder may swear it.',
    'the Seceders', [('Burgher', 1, ''), ('Anti-Burgher', 1, '')],
    'Within two years, mutual excommunication. The oath was never required in Ireland.',
    'The oath, required of burgesses in Edinburgh, Glasgow and Perth: &ldquo;the true religion presently professed within this realm and authorized by the laws thereof.&rdquo; Burghers: it means only &ldquo;not Catholic.&rdquo; Anti-Burghers: it blesses the church we left. The synod split April 1747 (Associate Synod vs General Associate Synod); the Anti-Burghers excommunicated the Burghers (1748&ndash;49), and the two could not take communion together. Thomas Campbell was Anti-Burgher. The Week 2 litany note covers why it felt so large (the Testimony, the Covenants).<br>'
    '&rarr; This is the rule Conemaugh broke, and the room already knows it.',
    bar='the Burgess Oath'))

A(D('1799 &middot; 1806',
    'May the magistrate enforce religion? Each Seceder body divides over the Confession&rsquo;s own words.',
    'Each synod revises its Testimony: the &ldquo;New Light.&rdquo;',
    'Burgher &middot; Anti-Burgher', [('Old Light', 1, ''), ('New Light', 1, ''), ('Old Light', 1, ''), ('New Light', 1, '')],
    'Thomas Campbell&rsquo;s synod splits in 1806, the year before he sails.',
    'The Burghers split 1799 (Original Burghers, Old Light), the Anti-Burghers 1806 (Constitutional Associate Presbytery, Old Light) over whether the civil magistrate has power in religion (Westminster Confession ch. 23). Campbell sided with the Old Lights by friendship more than conviction (Foster; Week 2 note). He sailed April 1807.<br>'
    'Cuttable: the Week 2 litany already told this. Keep if the room needs the landing.',
    bar='the revised Testimony', cut=True))

A('<section class="slide flowslide"><div class="eyebrow quiet">325&ndash;1806</div>' + FLOW_SVG +
  '<aside class=notes>The whole picture at once. One river, and every gold bar is a creed, council, oath or settlement offered as a term of unity. Widths are suggestive, not to scale. The faded stream is the Arians; the dotted lens is the Henotikon, the one breach that healed.<br>'
  '&rarr; All of these, as informative and enlightening as they are, did not produce unity. They could not produce it even among those who agreed on them.</aside></section>')

A('<section class="slide"><h2>What can Christians unite on?</h2>'
  '<div class="sub frag">He prayed that they would be one. So it must be possible.</div>'
  '<aside class=notes>John 17:21, a prayer, not a command. Then back to the Preamble: &ldquo;nor, indeed, can we reasonably expect to find it anywhere but in Christ and his simple word.&rdquo;<br>&rarr; Your close is yours. The slide stops at the question.</aside></section>')

A('<section class="slide"><aside class=notes>Black. Then the Preamble&rsquo;s last sentence.</aside></section>')
