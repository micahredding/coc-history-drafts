# -*- coding: utf-8 -*-
import re
# Oct 11 deck — Chapter 2 continued (Alexander) + Chapter 3 part 1 (the Declaration's claim). Spec: class folder, AI Notes/202610041900.
# The Alexander section is copied from decks/src/week2/slides.py (its slides 61–74, as of 2026-10-04).
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
def C(name, note):   # chapter card: the name only
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (name, note))
def Q(quote, cite='', eyebrow='', cls='slide', sub=''):   # a quotation alone
    e = '<div class=eyebrow>%s</div>' % eyebrow if eyebrow else ''
    c = '<div class=cite>%s</div>' % cite if cite else ''
    n = len(re.sub(r'<[^>]+>|&[a-z]+;', 'x', quote))   # visible length, entities as one char
    size = ' xlong' if n > 260 else ' long' if n > 150 else ''
    return '<section class="%s">%s<p class="bigquote%s"><span class=q>%s</span></p>%s%s' % (cls, e, size, quote, sub, c)

def N(*bul):   # speaker notes as bullets, closing the section
    return '<aside class=notes>' + '<br>'.join('&bull; '+x for x in bul) + '</aside></section>'

S = []
A = S.append

# ---------- 0 OPEN ----------
A('<section class="slide" style="padding-bottom:10vmin"><div class="eyebrow quiet" style="font-size:clamp(16px,3vmin,36px)">Otter Creek &middot; Fall 2026</div>'
  '<h1 style="font-size:min(19vmin,11.5vw);line-height:1.02;max-width:none">Our Wild<br>Democracy</h1>'
  '<p class=sub style="font-size:min(5vmin,3.6vw);max-width:none;margin-top:2vmin">The Story, Promise, and Future<br>of the Churches of Christ</p>'
  '<aside class=notes>Open. Under a minute: where we left Thomas, then straight into Alexander.</aside></section>')

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 2, continued &middot; Chapter 3</div>'
  '<h1>Alexander and the Declaration</h1><div class=table-line></div>'
  '<div class=sub>Glasgow 1808 &mdash; Washington, Pennsylvania 1809</div>'
  '<aside class=notes>The plan: Alexander (about 20 minutes), then why anyone would write this document, then what it says. The full discussion of the Declaration is next week.</aside></section>')

A('<section class="slide"><div class=eyebrow>Where we left him</div>'
  '<h2>Censured. Out of the synod. Preaching in a grove.</h2>'
  '<div class="sub frag">And his family was still in Ireland.</div>'
  + N('February 1808: the presbytery found the charges proved. May: he appealed to the synod and was rebuked.',
      'September 1808: his letter to the Chartiers Presbytery renounced their authority.',
      'Since then, farmhouses and a maple grove.',
      'He had left Alexander, eighteen, in charge of the family in Ireland.',
      '&rarr; While the father was on trial, the son was getting on a ship.'))

# ---------- I ALEXANDER AND THE SEA (from Chapter 2) ----------
A(C('Alexander and the Sea', 'The son&rsquo;s story, while the father&rsquo;s is still open. Three points, each a charge the room just judged.'))

A('<section class="slide"><h2 style="max-width:none">October 1808 &mdash; His family sailed</h2>'
  '<div class=days>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Sep 20</span><span>The family sets out for Londonderry. The <i>Hibernia</i> is not ready; they wait eight days.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 1</span><span>The <i>Hibernia</i> sails, firing her ten cannon in farewell.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 2</span><span>Out into the Atlantic &mdash; then anchored again off Inishowen.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 3</span><span>Contrary winds off Malin Head. They run before the gale all night.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 4</span><span>The coast of Scotland. They anchor in Loch Indaal, on Islay, and wait for wind.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 7</span><span style="color:var(--gold)">Evening. Alexander wakes from a dream.</span></div>'
  '</div>'
  + N('Click each date in. Keep it brisk until the last one.',
      'Thomas had left Alexander, eighteen, in charge of the family in Ireland. Now they sail to join him.',
      'Oct 7: Alexander dozes while reading to his sister Dorothea. He wakes alarmed &mdash; he dreamed the ship struck a rock and the water rushed in.',
      'He tells the family: &ldquo;I will not undress to-night. I will lay my shoes within my reach, and be ready to rise at a moment&rsquo;s warning.&rdquo;',
      'Then stop. Let the dream sit before you click.',
      'Source: Richardson 1:94&ndash;99.'))

A('<section class="slide bleed"><div class=bg><div class="bgimg wreckbg"></div></div>'
  '<div class=credit>Philippe Jacques de Loutherbourg, <i>A Shipwreck off a Rocky Coast</i><br>Not the <i>Hibernia</i>, and not Islay</div>'
  '<h2>That night, a gale blew in.</h2>'
  + N('About ten o&rsquo;clock that night the gale turns into the bay. The ship drags her anchors onto a sunken rock.',
      'Source: Richardson 1:99.',
      'Meanwhile his father has been tried and condemned. Alexander does not know.'))

A(Q('&ldquo;He thought of his father&rsquo;s noble life&hellip; and resolved that, if saved from the present peril, <b>he would certainly spend his entire life in the ministry of the gospel</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:101&ndash;02', 'The shipwreck &middot; on the broken mast', 'slide',
    '<div class="sub frag">Everyone survived. Stranded ten months, Alexander spent the winter at the <b>University of Glasgow</b>.</div>') +
  N('Night, the storm still on, no help in sight.',
    'Alexander sits on the stump of the broken mast, expecting to die.',
    'He thinks of his father&rsquo;s life &mdash; and vows: if he lives, he will give his whole life to the ministry.',
    '&rarr; His calling is born out of admiring his father. Within months, his conscience leads him away from his father&rsquo;s church.',
    'Click: everyone survives. Stuck in Scotland ten months; the winter at the University of Glasgow.',
    '&rarr; In Glasgow, the son runs into the same questions his father was charged with &mdash; one after another.'))

# --- 1 · occasional hearing (Article 4)
A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">1 &middot; Article 4</span> &middot; Glasgow, winter 1808&ndash;09</div>'
  '<h2>He went to hear other preachers.</h2>'
  '<div class="sub frag">Above all <b>Greville Ewing</b> &mdash; fifteen hundred people in a converted circus.</div>'
  '<div class="sub frag">The very thing his father was convicted for: <b>&ldquo;occasional hearing.&rdquo;</b></div>'
  + N('Article 4: his father was condemned for saying our people may hear ministers outside our church.',
      'In Glasgow, Alexander found the Seceder minister &ldquo;a prosy speaker.&rdquo;',
      'So every chance he got, he went to hear others. Favorite: Greville Ewing, preaching to 1,500 in a converted circus building (the Tabernacle).',
      'Richardson: it freed him from the denominational habits of his upbringing &mdash; easier with his father &ldquo;separated from him by the wide Atlantic.&rdquo;',
      '&rarr; The son is doing every week what the father was convicted for.',
      'Source: Richardson 1:188.'))

# --- 2 · the Haldanes (root of Articles 2 and 3)
A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">2 &middot; Articles 2 &amp; 3</span> &middot; at Ewing&rsquo;s house</div>'
  '<h2>Ewing told him the story of the Haldanes.</h2>'
  '<div class="sub frag">Two Scottish <b>laymen</b> who began preaching the gospel without ordination.</div>'
  '<div class="sub frag">James Haldane was <b>arrested at the instigation of the clergy</b>.</div>'
  + N('Alexander was often at Ewing&rsquo;s house. Ewing told him about the Haldanes &mdash; Robert and James, wealthy ex-navy laymen. James preached for years before he was ordained; Robert funded the movement.',
      'Ewing himself: left the Church of Scotland in 1798 to join them; ran their Glasgow Tabernacle and seminary; started weekly communion there. Their 1799 church was founded to avoid &ldquo;that contracted spirit which would exclude from the pulpit, or from occasional communion, any faithful preacher of the gospel or sincere lover of Christ&rdquo; (1:166) &mdash; Conemaugh, eight years early.',
      'Article 3 echo: his father was condemned for letting elders &mdash; non-ministers &mdash; pray and exhort.',
      '<b>Foreign missions.</b> Robert Haldane sold his estate, Airthrey, to fund a mission to Bengal; the East India Company &ldquo;positively and unexpectedly refused&rdquo; permission, and he had already sold it (1797). When the General Assembly debated &ldquo;That it is the duty of Christians to send the gospel to the heathen world,&rdquo; it voted it down &ldquo;by a large majority&rdquo; &mdash; plenty of unbelief at home, they said. James was in the room and took them at their word: he went and preached at home (1:152&ndash;54).',
      '<b>What the church tolerated.</b> In 1786 Dr. McGill, a minister at Ayr, published a book teaching that Christ &ldquo;was not God, equal with the Father&rdquo; and explaining away the atonement. It circulated for years with no action by presbytery, synod or General Assembly; when a complaint came in 1789 it was &ldquo;hushed up&rdquo; on &ldquo;vague explanations,&rdquo; and he kept his pulpit (1:153, note).',
      '&rarr; A minister could deny Christ&rsquo;s divinity and keep his pulpit. Laymen preaching Christ in the open air were the danger.',
      '<b>What the church fought.</b> The 1798 preaching tours met &ldquo;much opposition on the part of the clergy and the magistrates&rdquo; (1:161). Ewing&rsquo;s 1797 sermon defending field-preaching &ldquo;served still more to alarm the Moderates&rdquo; (1:162).',
      '<b>The arrest.</b> June 1800, Kintyre: James Haldane and his companion John Campbell (no relation to our Campbells), preaching every day in the open air, were &ldquo;held for some time under arrest by the Highland chiefs, at the instigation of the clergy&rdquo; (1:168&ndash;69).',
      'What struck Alexander (1:188&ndash;89): the clergy&rsquo;s &ldquo;persistent opposition&hellip; to every overture for reformation,&rdquo; their &ldquo;unscrupulous methods,&rdquo; and power used &ldquo;in an arbitrary manner.&rdquo;',
      'Richardson says this story, more than anything, is what changed Alexander&rsquo;s mind.',
      'Source: Richardson 1:152&ndash;69, 188&ndash;89.'))

A(Q('&ldquo;&hellip;an entire emancipation from the control of <b>domineering Synods and General Assemblies</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:189', 'What Alexander came to want') +
  N('He came to believe a congregation should be free of these church courts &mdash; &ldquo;more accordant with primitive usage.&rdquo;',
    'Article 2 echo: who sets the terms of the church &mdash; a synod&rsquo;s standards, or Scripture?',
    '&rarr; The son only heard these stories. The father was living them: church courts shut down his Irish reunion; a presbytery and a synod condemned him.'))

# --- 3 · the table
A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">3 &middot; The table</span> &middot; Glasgow, spring 1809</div>'
  '<h2>The communion season came. He was examined, and given the token.</h2>'
  '<div class="sub frag">Eight hundred communicants. Eight or nine tables. <b>He waited for the last one.</b></div>'
  + N('The Seceder church in Glasgow held its spring communion season.',
      'He still felt it was his duty to commune. But he no longer believed in the system.',
      'No letter from his church in Ireland, so the elders examined him &mdash; and gave him the token, his ticket to the table.',
      'About 800 communicants, eight or nine sittings. He waited for the last, hoping his doubts would settle.',
      'Source: Richardson 1:189&ndash;90.'))

A(Q('&ldquo;His conscientious misgivings as to the propriety of sanctioning any longer, by participation, a religious system which he disapproved, and, on the other hand, his sincere desire to comply with all his religious obligations, <b>created a serious conflict in his mind, from which he found it impossible to escape</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:189', 'Why he hesitated') +
  N('Both pulls at once: taking part would put his stamp of approval on the system &mdash; but he still felt bound to every duty of that church.',
    'What he would be leaving: &ldquo;the Seceder Church to which <b>his father and the family belonged</b>&rdquo; (1:189).',
    'He waited for the last table &ldquo;in hopes of being able to overcome his scruples.&rdquo; He wanted to stay.',
    '&rarr; Participation is sanction. The father: you may not make this table a test. The son: I will not let this table make me a witness.',
    'Read only the gold phrase. Hit the word <b>sanctioning</b> hard.'))

A(Q('&ldquo;&hellip;the ring of the token, falling upon the plate, announced the instant at which he renounced Presbyterianism for ever &mdash; <b>the leaden voucher becoming thus a token not of communion but of separation</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:190', '', 'slide hard') +
  N('His doubts did not settle. Call back the mast: the boy who vowed his life to his father&rsquo;s ministry.',
    'When the plate came around, he dropped his token on it.',
    'When the bread and wine came down the table, he &ldquo;declined to partake.&rdquo;',
    'He told no one. Collected his certificate of good standing on the way out.',
    '<b>&rarr; Through-line: who sets the terms of the table?</b> Third time.',
    'Then silence. Do not explain it.'))

A(C('Family Reunion', ''))

A('<section class="slide"><div class=eyebrow>19 October 1809 &middot; the road into Washington, Pennsylvania</div>'
  '<h2>Thomas rode out to meet them.</h2>'
  '<div class="sub frag">On the ride back he told his son everything: the trial, the rebuke &mdash; and that <b>he had left the Seceders</b>.</div>'
  + N('October 1809: the family finally lands. Thomas rides out to meet them. Apart two and a half years.',
      'On the ride back, Thomas tells it all: the trial, the rebuke, and that he has left the Seceders.',
      'Why: he &ldquo;could no longer feel justified in <b>sanctioning</b> their proceedings by remaining with them.&rdquo;',
      '&rarr; Same word the son used about the table: sanctioning.',
      'Source: Richardson 1:219&ndash;20.'))

A(Q('&ldquo;&hellip;instead of <b>fearing opposition from him</b> to the views to which he had himself been definitely brought while in Glasgow, he found him already, though by a somewhat different method, <b>led practically to the very same conclusions</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:220', 'On the road') +
  N('Read only the gold phrases.',
    'Six months he had carried it alone: &ldquo;as yet confined to his own heart&rdquo; (1:190).',
    'He expected his father to oppose him.',
    'Instead: by different roads, the same place.',
    'The father&rsquo;s side mirrors it: &ldquo;compelled suddenly to turn away&hellip; from the religious body which he had <b>loved and espoused</b>&rdquo; (1:221). Neither left lightly.'))

A('<section class="slide hard"><h2>The father opened the table to people who had no token.</h2>'
  '<div class="sub frag">The son held a valid token, and would not use it.</div>'
  '<div class="sub frag"><b>Neither knew.</b></div>'
  + N('Say it plain and stop. Let the silence sit before you click.'))

# ---------- II THE PROOF-SHEETS ----------
A('<section class="slide"><div class=eyebrow>Washington, Pennsylvania &middot; autumn 1809</div>'
  '<h2>Three weeks off the ship, Alexander read the proof-sheets.</h2>'
  '<div class="sub frag">His father&rsquo;s <b>Declaration and Address</b>, as it came from the press.</div>'
  + N('Richardson: Alexander was soon &ldquo;examining the proof-sheets of the &lsquo;Declaration and Address.&rsquo;&rdquo;',
      'The Christian Association of Washington approved it on 7 September 1809 and ordered it printed. It was at the printer when the family landed.',
      'Next week: how the Association came to be, and the rule it argued over. Tonight: what the document says.',
      '&rarr; Read it over his shoulder.',
      'Source: Richardson 1:250; Foster, <i>A Life of Alexander Campbell</i>, ch. 3, p. 43.'))

A('<section class="slide breath"><h2>Why would a man write this?</h2>'
  '<div class="sub frag">Because of what he had seen.</div>'
  + N('&rarr; Eighteen hundred years of Christians trying to be one.',
      'Tell the next part charitably. Every one of these was a serious attempt by faithful people.'))

# ---------- III EVERY LINE DREW ANOTHER LINE ----------
A(C('Every Line Drew Another Line', 'About ten minutes. One beat per slide: the date, what they reached for, what it divided. Credit every one of them.'))

A('<section class="slide"><div class=eyebrow>325 &middot; Nicaea</div>'
  '<h2>A creed, to settle who Christ is.</h2>'
  '<div class="sub frag">The quarrel went on for most of the century.</div>'
  + N('Constantine called the council over Arianism: was the Son fully God, or the first and highest creature?',
      'The creed said the Son is <i>homoousios</i>, of one substance with the Father.',
      'Arianism was official orthodoxy in the East again within decades. It was not settled until Constantinople, 381.',
      '&rarr; The first great creed was written to make the church one. Fifty years of fighting followed.',
      'Source: <i>Encyclop&aelig;dia Britannica</i>, &ldquo;First Council of Nicaea&rdquo;; &ldquo;Arianism.&rdquo;'))

A('<section class="slide"><div class=eyebrow>451 &middot; Chalcedon</div>'
  '<h2>A definition: one Christ, two natures.</h2>'
  '<div class="sub frag">The Coptic, Syriac, Armenian and Ethiopian churches could not accept it.</div>'
  '<div class="sub frag">They are still separate today.</div>'
  + N('Chalcedon defined Christ as one person in two natures, divine and human.',
      'The Egyptian (Coptic) and Syrian churches rejected it; the Ethiopian and Armenian churches soon joined them. Today: the Oriental Orthodox.',
      'One of the earliest lasting splits. (The Church of the East had already drifted apart after Ephesus, 431.)',
      '&rarr; A formula written to unite drew a line that has held for 1,500 years.',
      'Source: <i>Encyclop&aelig;dia Britannica</i>, &ldquo;Christianity: Theological controversies of the 4th and 5th centuries&rdquo;; &ldquo;Nestorius.&rdquo;'))

A('<section class="slide"><div class=eyebrow>1054 &middot; East and West</div>'
  '<h2>Rome and Constantinople excommunicated each other.</h2>'
  '<div class="sub frag">Over who holds authority, and one phrase in the creed.</div>'
  + N('16 July 1054: Cardinal Humbert laid a bull of excommunication on the altar of Hagia Sophia against Patriarch Michael Cerularius, who answered in kind.',
      'The issues: papal authority, and the <i>filioque</i> (&ldquo;and the Son&rdquo;) added to the creed in the West.',
      '<b>Hopeful note:</b> on 7 December 1965 Pope Paul VI and Ecumenical Patriarch Athenagoras I lifted the excommunications.',
      '&rarr; It took nine hundred years to take back one afternoon.',
      'Source: <i>Encyclop&aelig;dia Britannica</i>, &ldquo;East-West Schism&rdquo;; Joint Catholic-Orthodox Declaration, 7 December 1965 (vatican.va).'))

A('<section class="slide"><div class=eyebrow>1529 &middot; Marburg</div>'
  '<h2>Luther and Zwingli agreed on fourteen articles out of fifteen.</h2>'
  '<div class="sub frag">The fifteenth was the Lord&rsquo;s Supper.</div>'
  '<div class="sub frag"><b>The Reformation divided at the table.</b></div>'
  + N('A colloquy called to unite the German and Swiss reformers against Rome.',
      'They agreed on 14 of 15 articles. On the 15th they agreed on much, but not on whether Christ&rsquo;s body is present in the bread.',
      'The story is told that Luther chalked <i>Hoc est corpus meum</i>, &ldquo;This is my body,&rdquo; on the table.',
      '&rarr; Chapter 1: a table opened. Chapter 2: a man tried for opening one. Here the whole Reformation splits at it.',
      'Source: <i>Encyclop&aelig;dia Britannica</i>, &ldquo;Colloquy of Marburg&rdquo;; <i>New Catholic Encyclopedia</i>, &ldquo;Marburg, Colloquy of&rdquo; (14 of 15).'))

A('<section class="slide"><div class=eyebrow>1530 &middot; 1563 &middot; 1646</div>'
  '<h2>Augsburg. Heidelberg. Westminster.</h2>'
  '<div class="sub frag">Each a careful statement of the faith.</div>'
  '<div class="sub frag">Each one a border.</div>'
  + N('Augsburg Confession, 1530 (Lutheran). Heidelberg Catechism, 1563 (Reformed). Westminster Confession, finished 1646 and adopted by the Church of Scotland in 1647.',
      'Thomas Campbell&rsquo;s Seceder church held to Westminster.',
      '&rarr; These are beautiful documents. They also told you which church you could not take communion in.',
      'Source: <i>Encyclop&aelig;dia Britannica</i>, &ldquo;Augsburg Confession,&rdquo; &ldquo;Heidelberg Catechism,&rdquo; &ldquo;Westminster Confession.&rdquo;'))

A('<section class="slide"><div class=eyebrow>Scotland &middot; 1733 &rarr; 1747 &rarr; 1806</div>'
  '<h2>Seceder. Anti-Burgher. Old Light.</h2>'
  '<div class="sub frag">His own name tag, from Chapter 2.</div>'
  + N('1733: Ebenezer Erskine and others secede from the Church of Scotland over patronage.',
      '1747: the Secession splits over the Burgess Oath into Burghers and Anti-Burghers.',
      'Then Old Light and New Light: the Burghers in 1799, the Anti-Burghers in 1806.',
      '&rarr; Each split was over a real principle. Each produced a smaller church, sure it was the faithful one.',
      'Source: <i>Encyclop&aelig;dia Britannica</i> (1911), &ldquo;Erskine, Ebenezer&rdquo;; for 1806, R. M. Smith in <i>Scottish Church History</i> 36 (2006), via Wikipedia, &ldquo;Anti-Burgher.&rdquo;'))

A('<section class="slide"><div class=eyebrow>And us</div>'
  '<h2>The unity movement divided too.</h2>'
  '<div class="sub frag">In 1906 the census first counted Churches of Christ and Disciples of Christ separately.</div>'
  '<div class="sub frag">There have been more lines since.</div>'
  + N('The 1890 census still counted them as one body. By 1906 the separation was largely complete; the census recorded it rather than caused it.',
      '&rarr; This beat has to stay. It makes the history a confession we share, not a verdict on anyone in the room.',
      'Callback to the quiz: Christians only, but not the only Christians.',
      'Source: U.S. Bureau of the Census, <i>Religious Bodies: 1906</i> (1910); Douglas Foster, &ldquo;What really happened in 1906,&rdquo; <i>Christian Chronicle</i>, 1 April 2006.'))


A('<section class="slide hard"><h2>Every fence built to keep the church together became a wall that divided it.</h2>'
  + N('Say it once and stop.',
      '&rarr; Not because the people were bad. Because the method was: unity by drawing a line.'))

A(Q('&hellip;if, for instance, <b>Arians, Socinians, Arminians, Calvinists, Antinomians</b>, etc., might not all subscribe the Westminster Confession, the Athanasian Creed, or the doctrinal articles of the Church of England.', '<i>Declaration and Address</i>, 1809 &middot; Appendix', 'Campbell saw it',
    'slide', '<div class="sub frag">Signing the same paper had never made them one.</div>') +
  N('He is answering the objection that without a creed, anyone could claim the Bible. His reply: they already sign the creeds.',
    'The first two are heresies by the creeds&rsquo; own standards; the last three were the great Protestant quarrels. All could sign the same document.',
    'He goes on to mock the idea that Athanasius had to finish what the apostles left &ldquo;in such a rude and unfinished state.&rdquo; Keep the sarcasm in the notes.',
    '&rarr; Agreement on paper is not unity.'))

# ---------- IV WHAT IT SAYS ----------
A(C('What It Says', 'The Declaration&rsquo;s own words from here on. Let it speak.'))

A(Q('&ldquo;&hellip;tired and sick of the <b>bitter jarrings and janglings</b> of a party spirit, we would desire to be at rest&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809 &middot; the Declaration') +
  N('The opening section. Before any argument, a man who is worn out.',
    '&rarr; This is not a theory of unity. It is exhaustion.'))

A(Q('&ldquo;This desirable rest, however, we utterly despair either to find for ourselves&hellip; amid the diversity and rancor of party contentions, the veering uncertainty and <b>clashings of human opinions</b>&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809 &middot; the Declaration', '', 'slide',
    '<div class="sub frag">&ldquo;&hellip;nor, indeed, can we reasonably expect to find it anywhere but in <b>Christ and his simple word</b>.&rdquo;</div>') +
  N('Read the first part, then click.',
    '&rarr; Where rest is not. Then where it is.',
    'This is the hinge of the evening: the only unity to be had is Christ.'))

A(Q('&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ and obedience to him in all things according to the Scriptures, and that manifest the same by their tempers and conduct&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809 &middot; Proposition 1', 'The first proposition, whole') +
  N('They have heard the first clause twice. This is the whole sentence.',
    'Essentially: by its nature. Intentionally: by Christ&rsquo;s design. Constitutionally: by its founding.',
    'The sentence goes on: &ldquo;&hellip;and of none else; as none else can be truly and properly called Christians.&rdquo; Leave that off the screen unless asked.',
    '&rarr; Not &ldquo;ought to be one.&rdquo; Is one.'))

A('<section class="slide idea room"><div class="eyebrow quiet">The claim</div>'
  '<h2>Unity is <span style="color:var(--gold)">given</span>, not constructed.</h2>'
  '<div class="sub frag">The church is already one. The divisions are the innovation.</div>'
  + N('Chapter 3, Idea 1.',
      '&rarr; Every line in the history was an attempt to build unity. Campbell says it was never ours to build.'))

A('<section class="slide"><div class=eyebrow>Proposition 10</div>'
  '<h2>&ldquo;Division among the Christians is a horrid evil&hellip;&rdquo;</h2>'
  '<div class=litany>'
  '<div class=frag>antichristian</div>'
  '<div class="frag dim">it destroys the visible unity of the body of Christ</div>'
  '<div class=frag>antiscriptural</div>'
  '<div class="frag dim">a direct violation of his express command</div>'
  '<div class=frag>antinatural</div>'
  '<div class="frag dim">it excites Christians to contemn, to hate, and oppose one another</div>'
  '</div>'
  + N('Build it one word at a time.',
      'Antichristian: &ldquo;as if he were divided against himself, excluding and excommunicating a part of himself.&rdquo;',
      'Antinatural: Christians &ldquo;bound by the highest and most endearing obligations to love each other as brethren.&rdquo;',
      'Source: <i>Declaration and Address</i>, Proposition 10.'))

A(Q('&ldquo;With you all we desire to unite in the bonds of an entire Christian unity &mdash; <b>Christ alone being the head, the center</b>, his word the rule&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809 &middot; the Address', '', 'slide',
    '<div class="sub frag">&ldquo;More than this, you will not require of us; and less we can not require of you.&rdquo;</div>') +
  N('Addressed to &ldquo;our brethren of all denominations.&rdquo;',
    '&rarr; Christ alone: the center. Everything else is circumference.'))

A(Q('&ldquo;&lsquo;Union in Truth&rsquo; is our motto.&rdquo;', '<i>Declaration and Address</i>, 1809 &middot; the Address') +
  N('Optional. Cut it if time is short.',
    'In full: &ldquo;Union in truth has been, and ever must be, the desire and prayer of all such; &lsquo;Union in Truth&rsquo; is our motto. The Divine word is our standard.&rdquo;'))

# ---------- V CLOSE ----------
A('<section class="slide room"><div class=eyebrow>&#9670; for discussion</div>'
  '<h2>Is it true that the only unity to be had is Christ?</h2>'
  + N('Ten minutes at most. The full discussion of the Declaration is next week.',
      'If it stalls: what would we have to give up to believe it?'))

# Cliffhanger: Micah is choosing it. Candidates are in the spec.
