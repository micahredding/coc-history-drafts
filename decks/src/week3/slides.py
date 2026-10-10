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

def Q(quote, cite='', eyebrow='', cls='slide', sub=''):   # a quotation alone
    e = '<div class=eyebrow>%s</div>' % eyebrow if eyebrow else ''
    c = '<div class=cite>%s</div>' % cite if cite else ''
    n = len(re.sub(r'<[^>]+>|&[a-z]+;', 'x', quote))
    size = ' xlong' if n > 260 else ' long' if n > 150 else ''
    return '<section class="%s">%s<p class="bigquote%s"><span class=q>%s</span></p>%s%s' % (cls, e, size, quote, sub, c)
def N(*bul):
    return '<aside class=notes>' + '<br>'.join('&bull; ' + x for x in bul) + '</aside></section>'
DA = 'Declaration and Address, 1809'

S = []
A = S.append
_D = __file__.rsplit('/', 1)[0]

# ---------- CLASS TITLE (as in the Chapter 2 deck) ----------
A('<section class="slide" style="padding-bottom:10vmin"><div class="eyebrow quiet" style="font-size:clamp(16px,3vmin,36px)">Otter Creek &middot; Fall 2026</div>'
  '<h1 style="font-size:min(19vmin,11.5vw);line-height:1.02;max-width:none">Our Wild<br>Democracy</h1>'
  '<p class=sub style="font-size:min(5vmin,3.6vw);max-width:none;margin-top:2vmin">The Story, Promise, and Future<br>of the Churches of Christ</p>'
  '<aside class=notes>The class title, as every week. Then the chapter.</aside></section>')

# ---------- RECAP: Chapter 2 in pictures (images from decks/src/week2) ----------
A('<section class="slide recapslide"><div class="eyebrow quiet">Last week &middot; Thomas Campbell&rsquo;s Heresy Trial</div>'
  '<div class=shots style="gap:3vmin">'
  '<figure class="shot frag" style="--r:-1.5deg"><img src="IMG_TCAMPBELL" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>Ireland.</b> Twice he works to unite the Seceders; twice his church courts shut it down.</figcaption></figure>'
  '<figure class="shot frag" style="--r:1.2deg"><img src="IMG_SHIP" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>April 1807.</b> He sails for America.</figcaption></figure>'
  '<figure class="shot frag" style="--r:-1deg"><img src="IMG_MAP" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>Western Pennsylvania.</b> Presbyterians who had not received communion in years.</figcaption></figure>'
  '<figure class="shot frag" style="--r:1.8deg"><img src="IMG_TOKEN" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>Conemaugh, August 1807.</b> He opens the table. He is tried and censured for it.</figcaption></figure>'
  '</div>'
  '<div class="sub frag" style="max-width:none;margin-top:3vmin">Put out, he preaches in a grove. That autumn they ask him to write down what they stand for.</div>'
  '<aside class=notes>Five clicks, about two minutes: the story so far in four pictures. Thomas Campbell (portrait); the ship (Robert Salmon, 1809, a ship of the kind, not the <i>Brutus</i>); Howell&rsquo;s 1792 map of Pennsylvania; a Scottish communion token, 1750, the fence at the table. Last week ended on the first sentence of what he wrote: the church of Christ upon earth is essentially, intentionally, and constitutionally one.</aside></section>')

# ---------- TITLE ----------
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 3</div>'
  '<h1>The Declaration<br>and Address</h1><div class=table-line></div>'
  '<div class=sub>Washington, Pennsylvania &middot; 1809</div>'
  '<aside class=notes>Title up. &rarr; &ldquo;Last week we ended on one sentence: the church of Christ upon earth is essentially, intentionally, and constitutionally one. Today: why anyone would need to write it.&rdquo; Then the Design of Religion. The hour: Design 4 &middot; Evils and proposition 10 6 &middot; Christendom 10 &middot; the sword 2 &middot; Preamble 3 &middot; conscience 6 &middot; the solution 3 &middot; Propositions 10 &middot; our table 8 &middot; reception and proof-sheets 5.</aside></section>')

# ---------- 1 THE DESIGN OF RELIGION ----------
A('<section class="slide breath sect"><div class=eyebrow>The Address</div><h2>The Design of Religion</h2><div class=table-line></div>'
  '<aside class=notes>Start here. The Address is the long part, to &ldquo;all that love our Lord Jesus Christ, in sincerity, throughout all the Churches.&rdquo; Its first paragraph is the premise under everything that follows.</aside></section>')

A(Q('&ldquo;That it is the grand design and native tendency of our holy religion <b>to reconcile and unite men to God, and to each other, in truth and love</b>, to the glory of God, and their own present and eternal good&hellip;&rdquo;', DA, 'The Design of Religion') +
  N('Stop before &ldquo;will not, we presume, be denied.&rdquo; Stand one, asked lightly: is unity what Christianity is <i>for</i>? If yes, every century of division is the religion failing its own purpose.', '&ldquo;In truth and love&rdquo;: both sides, from the first sentence. The motto later is &ldquo;Union in Truth.&rdquo;'))

A(Q('&ldquo;&hellip;the first and foundation truth of our Christianity is <b>union with him</b>, and the very next to it in order, <b>union with each other in him</b>.&rdquo;', DA, 'The Design of Religion') +
  N('The design sentence again, in its own order: unite men &ldquo;to God, and to each other&rdquo; becomes union with him first, and union with each other in him next. Unity is not a project beside the faith; it follows from it. From later in the Address, the same sentence, just before: the &ldquo;bewildered Church has, for hundreds of years past, been rending and dividing herself into factions, for Christ&rsquo;s sake, and for the truth&rsquo;s sake.&rdquo; That is the egg in his words.', 'Order matters: union with each other is not built beside union with Christ; it follows from it. That is proposition 1 in a sentence: given, not constructed.'))

A(Q('&ldquo;The nativity of its Divine author was announced from heaven, by a host of angels, with high acclamations of <b>&lsquo;Glory to God in the highest, and on earth peace and good-will toward men.&rsquo;</b>&rdquo;', DA, 'The Design of Religion') +
  N('Back to the first paragraph. The proof he offers is Luke 2: the religion was announced as peace.'))

A(Q('&ldquo;In so far, then, as this holy unity and unanimity in faith and love is attained, <b>just in the same degree</b> is the glory of God and the happiness of men promoted and secured.&rdquo;', DA, 'The Design of Religion') +
  N('&ldquo;Just in the same degree.&rdquo; Unity is not a bonus on top of the religion; it is the measure of it. Then: what does division cost?'))

# ---------- 2 THE EVILS OF DIVISION ----------
A('<section class="slide breath sect"><div class=eyebrow>The Address</div><h2>The Evils of Division</h2><div class=table-line></div>'
  '<aside class=notes>What division costs. Practical, not doctrinal. Build the list one line at a time and let the room map each one onto now.</aside></section>')

A('<section class="slide"><div class=eyebrow>&ldquo;What awful and distressing effects have those sad divisions produced!&rdquo;</div>'
  '<div class=litany>'
  '<div class="no frag">&ldquo;congregations <b>broken to pieces</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;large settlements and tracts of country&hellip; <b>entirely destitute of a Gospel ministry</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;How seldom do many&hellip; enjoy the dispensations of the Lord&rsquo;s Supper, <b>that great ordinance of unity and love</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;the tone of discipline relaxed&hellip; lest their people should leave them, and&hellip; <b>find refuge in the bosom of another party</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;the weak stumbled, the graceless and profane hardened, <b>the mouths of infidels opened</b> to blaspheme religion&rdquo;</div>'
  '</div><div class=cite>' + DA + '</div>'
  '<aside class=notes>Five clicks. All verbatim from the Evils of Division. The Supper line ties to the Table arc of the whole class. The last two land hardest in 2026: members who can leave for the church down the road, and the mouths of infidels. (Dropped from the list: &ldquo;Several&hellip; who live at the door of a preached Gospel, dare not in conscience go to hear it&rdquo;: people within reach of preaching, but of another party, whose scruples keep them from it, so they are as cut off as if among heathens. Restore if useful.)</aside></section>')

A(Q('&ldquo;Say, dear brethren, <b>are not these things so?</b>&rdquo;', DA, 'The Evils of Division') +
  N('His own question, to the room. Let them answer.', '&rarr; Then his verdict on all of it.'))

A('<section class="slide"><div class=eyebrow>Proposition 10</div>'
  '<h2>&ldquo;Division among the Christians is a horrid evil, fraught with many evils.&rdquo;</h2>'
  '<div class=litany>'
  '<div class="no frag">&ldquo;It is <b>antichristian</b>, as it destroys the visible unity of the body of Christ; as if he were divided against himself&hellip;&rdquo;</div>'
  '<div class="no frag">&ldquo;It is <b>antiscriptural</b>, as being strictly prohibited by his sovereign authority&hellip;&rdquo;</div>'
  '<div class="no frag">&ldquo;It is <b>antinatural</b>, as it excites Christians to contemn, to hate, and oppose one another, who are bound&hellip; to love each other as brethren&hellip;&rdquo;</div>'
  '</div><div class=cite>' + DA + '</div>'
  '<aside class=notes>Three clicks, verbatim. The Evils list was what division costs; this is what division <i>is</i>. Against Christ, against Scripture, against nature: a body excommunicating part of itself. Elided from the first: &ldquo;excluding and excommunicating a part of himself.&rdquo; From the second: &ldquo;a direct violation of his express command.&rdquo; Last clause: &ldquo;In a word, it is productive of confusion and of every evil work.&rdquo;<br>'
  '&rarr; Then: it was not for want of trying. Here is fifteen hundred years of trying.</aside></section>')

# ---------- 4 CHRISTENDOM'S SEARCH FOR UNITY (the egg) ----------
S += christendom_slides()


# ---------- 5 THE PREAMBLE: REST, AND DESPAIR ----------
A('<section class="slide breath sect"><div class=eyebrow>The Declaration</div><h2>Preamble</h2><div class=table-line></div>'
  '<div class=sub>The sentiments of the people of the grove.</div>'
  '<aside class=notes>Summer 1809. The people following Thomas Campbell from farmhouse to maple grove have become something, and they need to say what. The Declaration is the short part, written for them. After the egg: this is what the people of the grove wanted, and why they despaired of getting it the old way.</aside></section>')

A(Q('&ldquo;&hellip;tired and sick of the bitter jarrings and janglings of a party spirit, <b>we would desire to be at rest</b>; and, were it possible, we would also desire to adopt and recommend such measures as would give rest to our brethren throughout all the churches&hellip;&rdquo;', DA, 'Preamble') +
  N('The line everyone remembers. Say it slowly. &ldquo;Rest&rdquo; is the word they chose, not &ldquo;victory.&rdquo;'))

A(Q('&ldquo;This desirable rest, however, <b>we utterly despair</b> either to find for ourselves, or to be able to recommend to our brethren, by continuing amid the diversity and rancor of party contentions, the veering uncertainty and clashings of human opinions&hellip;&rdquo;', DA, 'Preamble') +
  N('Stop here. Do not read the next clause yet.', '&rarr; Before the answer, name the issue underneath all of it. Why can none of those instruments work?'))


# ---------- 6 THE ISSUE: FREEDOM OF CONSCIENCE ----------
A(C('Why did every instrument fail?', 'Card. Fifteen hundred years of creeds, councils and swords, and a document that despairs of the old way. The next slide names the reason underneath.'))

A('<section class="slide bleed" style="padding-bottom:5vmin"><div class=bg><div class="bgimg lutherbg"></div></div>'
  '<div class=credit>Anton von Werner, <i>Luther at the Diet of Worms</i>, 1877 &middot; public domain</div>'
  '<div class=eyebrow>Worms, 1521</div>'
  '<h2 style="font-size:clamp(56px,13vmin,170px);line-height:1.02;max-width:none">Conscience cannot<br>be compelled.</h2>'
  '<aside class=notes>Worms, April 1521. Asked to recant, Luther: &ldquo;my conscience is captive to the Word of God. I cannot and will not recant anything, since it is neither safe nor right to go against conscience.&rdquo; (&ldquo;Here I stand, I can do no other&rdquo; is the famous form; the earliest printed accounts add it, the transcript does not. Say &ldquo;as the story goes.&rdquo;) Protestantism begins with that sentence, and it is the reason none of the instruments on the egg could work: a creed can name who agrees, and a sword can make people say it, but neither can make anyone believe. The consequence comes a few slides on.</aside></section>')

A(Q('&ldquo;&hellip;my conscience is captive to the Word of God. I cannot and will not recant anything, since <b>it is neither safe nor right to go against conscience</b>.&rdquo;', 'Martin Luther at Worms, 18 April 1521', 'Here I stand') +
  N('The line everyone remembers. Say it slowly. (&ldquo;Here I stand, I can do no other&rdquo; is the famous form; the earliest printed accounts add it, the transcript does not.)', '&rarr; Then the whole sentence it ends.'))

A(Q('&ldquo;<b style="font-size:1.18em">Unless I am convinced by the testimony of the Scriptures or by clear reason</b><span style="font-size:.78em">&hellip; I am bound by the Scriptures I have quoted and my conscience is captive to the Word of God. I cannot and will not recant anything, since <b>it is neither safe nor right to go against conscience</b>. May God help me. Amen.</span>&rdquo;', 'Martin Luther at Worms, 18 April 1521', 'Worms, 18 April 1521', 'slide wormsfull') +
  N('The sentence, with its parenthesis trimmed on screen: &ldquo;(for I do not trust either in the pope or in councils alone, since it is well known that they have often erred and contradicted themselves)&rdquo;. Councils have erred: the egg, in his words. Look at how it starts: &ldquo;Unless I am convinced.&rdquo; He holds his own reading open. Show him from Scripture or clear reason that he is wrong, and he must change. That is the opposite of &ldquo;I can do what I want.&rdquo;', 'Translations vary (&ldquo;testimonies of the Holy Scriptures or evident reason&rdquo;); this is the common English form.'))

A('<section class="slide breath"><h2 style="max-width:none">Conscience is not &ldquo;I can do what I want.&rdquo;</h2>'
  '<div class="sub frag punch">It is &ldquo;I must.&rdquo;</div>'
  '<aside class=notes>One click. His word is <i>captive</i>: bound, not free. Conscience here is not a preference but an obligation before God. &ldquo;Neither safe nor right to go against conscience&rdquo;: not safe, because he must answer to God for it.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">Captive to the Word of God.</h2>'
  '<div class=litany style="align-items:center">'
  '<div class="no frag">Not to the pope&rsquo;s reading of it.</div>'
  '<div class="no frag">Not to a council&rsquo;s.</div>'
  '<div class="no frag">Not even to his own.</div>'
  '<div class="no frag">Not to what he thinks it says.</div>'
  '<div class="no frag" style="color:var(--gold)">To the Word of God itself.</div>'
  '</div>'
  '<aside class=notes>Five clicks; slow down on &ldquo;not even to his own.&rdquo; The proof is the first clause of the sentence: &ldquo;Unless I am convinced by the testimony of the Scriptures or by clear reason.&rdquo; He can still be corrected by the Word, so he is not treating his own reading as the Word. What binds him is the Word itself, and his conscience is where he answers to God for how faithfully he reads it. That is why no council can do it for him: an obligation cannot be handed to someone else.</aside></section>')

A('<section class="slide breath"><div class=eyebrow>Luther did not invent this</div>'
  '<h2 style="max-width:none">Even a mistaken conscience binds.</h2>'
  '<div class=sub style="max-width:none;margin-top:1.4vmin">Thomas Aquinas, <i>Summa Theologiae</i>, c. 1270 &middot; paraphrased</div>'
  '<div class="sub frag punch" style="margin-top:4vmin">A council can say it. A council cannot make you believe it.</div>'
  '<aside class=notes>One click. Aquinas, two and a half centuries before Worms, in the article on &ldquo;whether an erring conscience binds&rdquo; (<i>Summa Theologiae</i> I-II q.19 a.5): &ldquo;every will at variance with reason, whether right or erring, is always evil.&rdquo; His example: to believe in Christ is &ldquo;good in itself, and necessary for salvation,&rdquo; yet to will it while one&rsquo;s reason proposes it as evil is to will evil. &rarr; Say it: even faith in Christ cannot rightly be forced against conscience. So unity cannot be compelled: you can compel conformity; you cannot compel communion.<br><br>Point back at the egg: every council on it found this out. Nicaea named the Arians; it did not convert them. The settlement of 1662 ejected two thousand ministers; it did not persuade them. Luther only said out loud what had been true since the first council. Campbell, on a General Council: &ldquo;It is not the voice of the multitude, but the voice of truth, that has power with the conscience&rdquo;; &ldquo;a conscience that awaits the decision of the multitude, that hangs in suspense for the casting vote of the majority, is a fit subject for the man of sin.&rdquo;<br><b>The Catholic witness</b> (it was always true, on both sides of Worms):<br>&bull; Aquinas, <i>Summa Theologiae</i> I-II q.19 a.5, on &ldquo;whether an erring conscience binds&rdquo;: &ldquo;every will at variance with reason, whether right or erring, is always evil.&rdquo; His own example: to believe in Christ is &ldquo;good in itself, and necessary for salvation,&rdquo; yet to will it while one&rsquo;s reason proposes it as evil is to will evil. Even an erring conscience binds.<br>&bull; Newman, <i>Letter to the Duke of Norfolk</i> (1875): &ldquo;I shall drink&mdash;to the Pope, if you please,&mdash;still, to Conscience first, and to the Pope afterwards.&rdquo;<br>&bull; The gap: the dignity of conscience is not yet freedom from coercion. Gregory XVI, <i>Mirari Vos</i> (1832) &sect;14: &ldquo;that absurd and erroneous proposition which claims that liberty of conscience must be maintained for everyone.&rdquo; Vatican II, <i>Dignitatis Humanae</i> (1965) &sect;3: &ldquo;he is not to be forced to act in a manner contrary to his conscience&hellip; No merely human power can either command or prohibit acts of this kind.&rdquo;<br>&rarr; Rome reached Campbell&rsquo;s conclusion in 1965, 156 years after the Declaration and Address.<br>(Avoid the often-quoted Aquinas line about dying excommunicated rather than violating conscience, <i>Sentences</i> IV d.38: its meaning is disputed.)<br><br><b>Unity cannot be compelled:</b> Why: the unity of the church is not everyone saying the same words. It is a communion of believers, each standing before God and joined to the others in Christ. Compel the words and you get conformity: the same sentence in divided hearts, which comes apart the moment a conscience stands up. That is the egg, every time.</aside></section>')

A('<section class="slide bleed"><div class=bg><div class="bgimg marburgbg"></div></div>'
  '<div class=credit>August Noack, <i>Religionsgespr&auml;ch zu Marburg 1529</i> (detail), 1867&ndash;69 &middot; public domain</div>'
  '<div class=eyebrow>Marburg &middot; October 1529</div>'
  '<h2>Luther and Zwingli.</h2>'
  '<div class="sub frag">He could not share the Lord&rsquo;s table with a brother who read the Lord&rsquo;s table differently.</div>'
  '<aside class=notes>The painting (detail): Luther, left in the fur collar, holds Zwingli off with both hands; Zwingli points upward. In the full canvas Luther&rsquo;s other hand is on the word <i>est</i> chalked on the table (&ldquo;this <i>is</i> my body&rdquo;). Fourteen articles agreed, and on the fifteenth agreement on everything but the bodily presence. Luther to the Swiss: &ldquo;You have a different spirit.&rdquo; As the accounts have it, Zwingli offered his hand at the end and Luther would not take it as a brother&rsquo;s.<br>&rarr; Two men, both captive to the same Word, reading it as faithfully as they could. Only one of them would grant the other that.</aside></section>')

A('<section class="slide"><div class=eyebrow>Worms, 1521 &middot; Washington, Pennsylvania, 1809</div>'
  '<div class=litany style="display:grid;grid-template-columns:1fr 1fr;column-gap:5vmin;row-gap:2.4vmin;text-align:left;max-width:92vw">'
  '<div class=eyebrow style="margin:0">Luther</div><div class=eyebrow style="margin:0">The Declaration and Address</div>'
  '<div class="no frag">&ldquo;my conscience is <b>captive to the Word of God</b>&rdquo;</div><div class="no frag">&ldquo;to this alone we feel ourselves <b>Divinely bound</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;I do not trust either in the pope or <b>in councils alone</b>&rdquo;</div><div class="no frag">&ldquo;not <b>the voice of the multitude</b>, but the voice of truth&rdquo;</div>'
  '<div class="no frag">&ldquo;<b>unless I am convinced</b> by the testimony of the Scriptures or by clear reason&rdquo;</div><div class="no frag">&ldquo;not formally binding&hellip; <b>farther than they perceive the connection</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;neither safe nor right <b>to go against conscience</b>&rdquo;</div><div class="no frag">&ldquo;<b>no man can judge for his brother</b>&rdquo;</div>'
  '</div>'
  '<aside class=notes>Eight clicks, left then right on each row. Every line on the right is already on the left. The right column: the Preamble; the Address on a General Council; proposition 6; the Preamble again. Only the last row moves: Luther says <i>I</i> may not go against my conscience; Campbell says <i>no one</i> may go against his brother&rsquo;s.<br>That last row is exactly where Luther stopped, at Marburg (the slide before; also the 1529 slide on the egg): fourteen articles agreed, and on the fifteenth agreement on everything but the bodily presence. Luther to the Swiss: &ldquo;Ihr habt einen andern Geist&rdquo; &mdash; &ldquo;You have a different spirit.&rdquo; As the accounts have it, Zwingli offered his hand at the end and Luther would not take it as a brother&rsquo;s.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">Luther claimed conscience for himself.<br><span style="color:var(--gold)">Campbell claimed it for his brother.</span></h2>'
  '<aside class=notes>Say it once and stop. Not a new principle: the same principle, extended to the brother. Luther is not the villain here: the man of Worms and the man of Marburg were equally sincere. That is the point: conscience claimed for yourself is only half a sentence, and Campbell finishes it. This is the chapter in one line.</aside></section>')

A(Q('&ldquo;&hellip;as no man can be judged for his brother, so <b>no man can judge for his brother</b>; every man must be allowed to judge for himself, as every man must bear his own judgment&mdash;must give account of himself to God.&rdquo;', DA, 'Preamble') +
  N('The Preamble&rsquo;s second sentence: the half Luther could not say at Marburg. Not a right claimed but an impossibility stated: you cannot believe for someone else. Zurich and 1806 on the egg were the magistrate trying. The first sentence, just before it: &ldquo;it is high time for us not only to think, but also to act, for ourselves&hellip; to this alone we feel ourselves Divinely bound to be conformed, as by this alone, we must be judged.&rdquo;'))

# ---------- WHY CAMPBELL COULD GO FURTHER: THE SWORD, AND THIS COUNTRY ----------
A('<section class="slide breath"><h2 style="max-width:none">If my brother is as bound to the Word as I am,</h2>'
  '<div class="sub frag punch" style="color:var(--bone)">my reading cannot be his door to the table.</div>'
  '<div class="sub frag punch">The table has to be open.</div>'
  '<aside class=notes>Two clicks. Three things in one line: freedom of conscience, why unity cannot be compelled, and the open table. This is Chapter 2 from the inside: Campbell was tried for opening the table to Presbyterians who read differently. Proposition 6 will make it rule: inferences are &ldquo;not formally binding upon the consciences of Christians farther than they perceive the connection.&rdquo; The Preamble&rsquo;s word for the opposite: to judge your brother is &ldquo;a daring usurpation of his throne, and a gross intrusion upon the rights and liberties of his subjects.&rdquo;</aside></section>')

A('<section class="slide"><h2>What can Christians unite on?</h2>'
  '<div class="sub frag">&ldquo;That they all may be one&hellip; that the world may believe that thou hast sent me.&rdquo;<br><span style="font-size:.7em;color:var(--bone-dim)">John 17:21</span></div>'
  '<aside class=notes>The question, now that the reason is named. Then the prayer: a prayer, not a command, and for the sake of the world&rsquo;s belief. Pause on it before the answer.</aside></section>')

# ---------- 7 THE SOLUTION ----------

A(Q('&ldquo;&hellip;nor, indeed, can we reasonably expect to find it anywhere but in <b>Christ and his simple word</b>, which is the same yesterday, to-day, and forever.&rdquo;', DA, 'Preamble, continued') +
  N('The clause you stopped before. Now it has fifteen hundred years behind it.', '&rarr; Thomas Campbell saw only one answer: given a people called to follow their conscience, given that no council could forever bind it, the only thing Christians could unite on was Christ himself.'))

A(Q('&ldquo;&hellip;taking the Divine word alone for our rule; the Holy Spirit for our teacher and guide, to lead us into all truth; and <b>Christ alone, as exhibited in the word</b>, for our salvation&hellip;&rdquo;', DA, 'Preamble, continued') +
  N('Guard: it is not creedless. &ldquo;Christ alone, <i>as exhibited in the word</i>.&rdquo; The fence is what Scripture expressly says, and nothing else. The propositions say how.'))

A('<section class="slide breath"><h2 style="max-width:32ch">Every time we hand a creed, a council, or a magistrate<br><span style="color:var(--gold)">a job only Christ can do</span>, it fails.</h2>'
  '<aside class=notes>The chapter&rsquo;s thesis, right after Campbell&rsquo;s answer (&ldquo;anywhere but in Christ&rdquo;). Point back at the egg: every one of those was a good instrument given the wrong job. Campbell names the job in the Address: creeds were &ldquo;designed and embraced for the purpose of promoting and securing that desirable unity and purity which the Bible alone, without those helps, would be insufficient to maintain and secure.&rdquo; That is the job description, and no document can do it.<br>'
  '&rarr; Which is not to say creeds are bad.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">There is nothing wrong with a creed.</h2>'
  '<div class="sub frag" style="max-width:none">But a creed cannot make us one.</div>'
  '<div class="sub frag punch">Only Christ can do that.</div>'
  '<aside class=notes>Two clicks. Not anti-creed: Nicaea is true, and the room says it. The fault on the egg was never the creed; it was the job the creed was given.</aside></section>')

A(Q('&ldquo;&hellip;doctrinal exhibitions of the great system of Divine truths&hellip; <b>be highly expedient, and the more full and explicit they be for those purposes, the better</b>; yet&hellip; they ought not to be made terms of Christian communion&hellip;&rdquo;', DA, 'Proposition 7') +
  N('Campbell says it himself: write the fullest confession you can. Just do not make it the door. Elided: &ldquo;and defensive testimonies in opposition to prevailing errors&rdquo;; &ldquo;as these must be in a great measure the effect of human reasoning, and of course must contain many inferential truths.&rdquo;',
    'The sentence ends: &ldquo;the Church from the beginning did, and ever will, consist of little children and young men, as well as fathers.&rdquo;'))

# ---------- 6 THE PROPOSITIONS ----------
A('<section class="slide breath sect"><div class=eyebrow>The Address</div><h2>The Thirteen Propositions</h2><div class=table-line></div>'
  '<div class=sub>Five of them.</div>'
  '<aside class=notes>Offered, the Address says just before them, not &ldquo;as an overture toward a new creed or standard for the Church, or as in any wise designed to be made a term of communion.&rdquo; Remember Chalcedon said the same. Read 1, 3, 6, 8, 9; the gold clause is the one to say twice.</aside></section>')

A(Q('&ldquo;That the Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ and obedience to him in all things according to the Scriptures, and that manifest the same by their tempers and conduct, and of none else&hellip;&rdquo;', DA, 'Proposition 1') +
  N('The class has heard the opening clause twice; now the whole sentence. Stand two: do you believe unity is given rather than built? If so, the sects are the innovation.'))

A(Q('&ldquo;That in order to do this, <b>nothing ought to be inculcated upon Christians as articles of faith; nor required of them as terms of communion, but what is expressly taught and enjoined upon them in the word of God</b>&hellip;&rdquo;', DA, 'Proposition 3') +
  N('The method. &ldquo;Expressly.&rdquo; This is the whole wager: strip terms of communion to what Scripture expressly says, and Christians will find they already agree on enough to live together.'))

A(Q('&ldquo;That although inferences and deductions from Scripture premises, when fairly inferred, may be truly called the doctrine of God&rsquo;s holy word, yet are they <b>not formally binding upon the consciences of Christians farther than they perceive the connection</b>&hellip; Therefore, no such deductions can be made terms of communion&hellip;&rdquo;', DA, 'Proposition 6') +
  N('Conscience again, now as polity. You cannot believe what you do not see, so you cannot be made to. Every council on the egg was an inference made a term of communion.'))

A(Q('&ldquo;That as it is not necessary that persons should have a particular knowledge or distinct apprehension of all Divinely revealed truths in order to entitle them to a place in the Church; <b>neither should they, for this purpose, be required to make a profession more extensive than their knowledge</b>&hellip;&rdquo;', DA, 'Proposition 8') +
  N('The one that answers Chalcedon directly: no term that excludes those who cannot understand it. The rest of the sentence: &ldquo;a profession of their faith in and obedience to him, in all things, according to his word, is all that is absolutely necessary to qualify them for admission into his Church.&rdquo;'))

A(Q('&ldquo;That all that are enabled through grace to make such a profession&hellip; should consider each other as the precious saints of God, should <b>love each other as brethren</b>, children of the same family and Father, temples of the same Spirit, members of the same body&hellip; Whom God hath thus joined together no man should dare to put asunder.&rdquo;', DA, 'Proposition 9') +
  N('The marriage line. Stand four: who are we not treating as brethren, and on what term?'))

# ---------- 7 OUR TABLE ----------
A('<section class="slide room"><div class=eyebrow>Our table</div>'
  '<h2>What do we require of someone before they sit at our table?</h2>'
  '<div class="sub frag">&ldquo;&hellip;a profession more extensive than their knowledge.&rdquo;</div>'
  '<aside class=notes>Discussion, eight minutes. Have them list what we actually require. Then proposition 8 against the list: which of these is a profession more extensive than their knowledge? Every room has its Munro item; ours is not infant baptism. Leave it open. Set it against the Evils list: division already costs that; what would unity cost?</aside></section>')

# ---------- 8 THE RECEPTION ----------
A(Q('&ldquo;That this Society <b>by no means considers itself a Church</b>, nor does at all assume to itself the powers peculiar to such a society&hellip; but merely as voluntary advocates for Church reformation&hellip;&rdquo;', DA, 'Resolution IV') +
  N('The one resolution to keep: voluntary advocates for reform, not a new church.'))

A('<section class="slide"><div class=eyebrow>The reception</div>'
  '<div class=litany>'
  '<div class="no frag">October 1810 &middot; the Synod of Pittsburgh refuses Christian and ministerial communion. <b>Nobody joins.</b></div>'
  '</div>' +
  N('Candor beat, one click. A unity plea addressed to every party and joined, in the event, by almost no one; the synod&rsquo;s refusal is Week 5&rsquo;s opening.', '&rarr; And the movement it started? We know what happened next.'))

A('<section class="slide room"><div class=eyebrow>The Churches of Christ</div>'
  '<h2>We have kept dividing.</h2>'
  '<div class="sub frag">We have all lived it.</div>'
  '<div class="sub frag punch">Does that mean Thomas Campbell was wrong?</div>'
  '<aside class=notes>Two clicks. Let the first one sit: everyone in the room has a story of a split, a congregation, a family. Look back at the tree: one cup, non-class, non-institutional, instrumental, premillennial. Then ask the question and let them answer before the next slide.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">No. It means he was right.</h2>'
  '<div class="sub frag" style="max-width:none">Every division since has come from someone<br>offering another answer than Christ.</div>'
  '<div class="sub frag punch">There is no other answer. There never will be.</div>'
  '<aside class=notes>Two clicks. Campbell diagnosed the problem correctly; the divisions are what it looks like when his point is not taken as deeply as it merits. Cups, classes, institutions, instruments, the millennium: every one was made a term of communion, asked to do the job only Christ can do. It did what every instrument on the egg did.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">Make anything else a term of communion,<br><span style="color:var(--gold)">and it will not make us one.<br>It will divide us again.</span></h2>'
  '<aside class=notes>The thesis card, brought home: the egg was not only their history. It is ours. Proposition 3 was the remedy: nothing required as terms of communion &ldquo;but what is expressly taught and enjoined upon them in the word of God.&rdquo;</aside></section>')

# ---------- 9 THE PROOF-SHEETS ----------
A('<section class="slide"><div class=eyebrow>October 1809</div>'
  '<h2>Alexander, twenty-one, three weeks off the ship, reads the proof-sheets as they come from the printer.</h2>'
  '<aside class=notes>Two sentences of Glasgow: the family wrecked off Islay, ten months in Glasgow, and the son refusing the Seceder communion token on his own, an ocean away from his father&rsquo;s break. On the road from Philadelphia they find out they have each broken with the same fence, through the same table. Then the proof-sheets.</aside></section>')

A(Q('&ldquo;Sir&hellip; these words, however plausible in appearance, are not sound. For if you follow these out, <b>you must become a Baptist</b>.&rdquo;', 'Rev. Riddle, a neighboring Presbyterian minister, to Alexander &middot; Richardson, <i>Memoirs</i> 1:251', 'The warning') +
  N('Alexander presses the question on his father: will these principles not mean giving up infant baptism? He buys every pro-infant-baptism treatise in Andrew Munro&rsquo;s own bookshop to find out.'))

A(Q('&ldquo;We make our appeal to the law and to the testimony. <b>Whatever is not found therein we must of course abandon.</b>&rdquo;', 'Thomas Campbell to his son, every time &middot; Richardson 1:252', 'The answer') +
  N('The father&rsquo;s answer committed the next generation before anyone knew where it led. Within three years the logic runs its course; that is a later week.'))

A('<section class="slide"><h2>Next week: the rise and fall of the Springfield Presbytery.</h2>'
  '<div class="sub frag">Five years before this was printed, the men of Cane Ridge had already tried to live it.</div>'
  '<aside class=notes>Close. They built something, watched it succeed, and then did something almost without precedent in church history: they wrote a will for it. Chapter 4, October 18.</aside></section>')

A('<section class="slide"><aside class=notes>Black.</aside></section>')

# ---------- ADDENDUM (reference; not part of the telling) ----------
A(C('Addendum', 'Reference material; not part of the telling.'))

A('<section class="slide breath sect"><h2>Priesthood of all believers</h2><div class=table-line></div>'
  '<div class="sub frag">Every believer: the Spirit within, united with Christ, answering to God directly.</div>'
  '<aside class=notes>Card, one click. The ground under Worms: why conscience is an obligation and not a preference. No one can stand before God in your place, so no one can read the Word in your place either. Then Luther&rsquo;s own line, a year before Worms.</aside></section>')

A(Q('&ldquo;&hellip;whoever comes out of the water of baptism can boast that he is already <b>a consecrated priest, bishop, and pope</b>&hellip;&rdquo;', 'Martin Luther, <i>To the Christian Nobility of the German Nation</i>, 1520 &middot; <i>Luther&rsquo;s Works</i> 44', 'Luther, a year before Worms', sub='<div class="sub frag" style="max-width:none">No one can stand before God in your place.<br>So no one can read the Word in your place.</div>') +
  N('One click. Why conscience is an obligation and not a preference. A year before Worms: &ldquo;we are all consecrated priests through baptism, as St. Peter says in I Peter 2[:9].&rdquo; Every baptized Christian has the Spirit within, is united with Christ, and stands before God directly.', 'The sentence continues: &ldquo;although of course it is not seemly that just anybody should exercise such office.&rdquo; Older translation (C. M. Jacobs, 1915): &ldquo;For whoever comes out of the water of baptism can boast that he is already consecrated priest, bishop and pope, though it is not seemly that every one should exercise the office.&rdquo;'))

A('<section class="slide"><div class=eyebrow>What every one of them had in common</div>'
  '<h2>Every one had a sword behind it.</h2>'
  '<div class=litany>'
  '<div class="no frag">Constantine &middot; Theodosius &middot; Marcian &middot; Zeno &middot; the papal legates</div>'
  '<div class="no frag">Charles V &middot; the council of Zurich &middot; Philip of Hesse &middot; Parliament &middot; William and Mary</div>'
  '<div class="no frag">the patrons &middot; the burgess oath &middot; <b>the magistrate</b></div>'
  '</div>'
  '<aside class=notes>Three clicks, back across the egg: who stood behind each instrument. Emperors convened Nicaea (Constantine), Ephesus (Theodosius II) and Chalcedon (Marcian), and issued the Henotikon (Zeno); legates carried Rome&rsquo;s bull in 1054; Charles V received Augsburg; Zurich&rsquo;s council ruled and drowned; Philip of Hesse called Marburg; Parliament imposed Westminster; the crown settled 1690; Parliament&rsquo;s Patronage Act made the Secession; a civic oath made the Burgher split; and the last split was over whether the magistrate may enforce religion at all.<br>'
  '&rarr; Back to the egg for a moment: every instrument on it could be enforced. Luther lived under the same swords: Charles V at Worms, Philip of Hesse calling Marburg. Campbell did not, which is why he could take Worms further.</aside></section>')

A(Q('&ldquo;What dreary effects of those accursed divisions are to be seen, even in this highly favored country, <b>where the sword of the civil magistrate has not as yet learned to serve at the altar</b>.&rdquo;', DA, 'The Address &middot; why 1809, why here') +
  N('From the Evils of Division paragraph, just before &ldquo;congregations broken to pieces.&rdquo; The Address says it outright later: &ldquo;A country happily exempted from the baneful influence of a civil establishment of any peculiar form of Christianity.&rdquo;',
    'The First Amendment was eighteen years old; Pennsylvania had never had an established church. For the first time in the story, nobody could enforce a creed. So unity could not be imposed here. It would have to be found.',
    'A few decades after one Declaration of Independence, another.'))
