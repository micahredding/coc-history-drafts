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

# ---------- TITLE ----------
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 3</div>'
  '<h1>The Declaration<br>and Address</h1><div class=table-line></div>'
  '<div class=sub>Washington, Pennsylvania &middot; 1809</div>'
  '<aside class=notes>Title up. Then the Design of Religion. The hour: Design 4 &middot; Evils 5 &middot; Christendom 10 &middot; Preamble 3 &middot; the issue, conscience 5 &middot; the solution 2 &middot; Propositions 10 &middot; our table 8 &middot; reception and proof-sheets 5.</aside></section>')

# ---------- 1 THE DESIGN OF RELIGION ----------
A('<section class="slide breath sect"><div class=eyebrow>The Address</div><h2>The Design of Religion</h2><div class=table-line></div>'
  '<aside class=notes>Start here. The Address is the long part, to &ldquo;all that love our Lord Jesus Christ, in sincerity, throughout all the Churches.&rdquo; Its first paragraph is the premise under everything that follows.</aside></section>')

A(Q('&ldquo;That it is the grand design and native tendency of our holy religion <b>to reconcile and unite men to God, and to each other, in truth and love</b>, to the glory of God, and their own present and eternal good&hellip;&rdquo;', DA, 'The Design of Religion') +
  N('Stop before &ldquo;will not, we presume, be denied.&rdquo; Stand one, asked lightly: is unity what Christianity is <i>for</i>? If yes, every century of division is the religion failing its own purpose.', '&ldquo;In truth and love&rdquo;: both sides, from the first sentence. The motto later is &ldquo;Union in Truth.&rdquo;'))

A(Q('&ldquo;The nativity of its Divine author was announced from heaven, by a host of angels, with high acclamations of <b>&lsquo;Glory to God in the highest, and on earth peace and good-will toward men.&rsquo;</b>&rdquo;', DA, 'The Design of Religion') +
  N('Same paragraph. The proof he offers is Luke 2: the religion was announced as peace.'))

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
  N('His own question, to the room. Let them answer.', '&rarr; Then: it was not for want of trying. Here is fifteen hundred years of trying.'))

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
A('<section class="slide bleed"><div class=bg><div class="bgimg lutherbg"></div></div>'
  '<div class=credit>Anton von Werner, <i>Luther at the Diet of Worms</i>, 1877 &middot; public domain</div>'
  '<div class=eyebrow>What&rsquo;s the issue?</div>'
  '<h2>Freedom of conscience.</h2>'
  '<div class="sub frag">If conscience cannot be compelled, then unity cannot be compelled either.</div>'
  '<aside class=notes>Worms, April 1521. Asked to recant, Luther: &ldquo;my conscience is captive to the Word of God. I cannot and will not recant anything, since it is neither safe nor right to go against conscience.&rdquo; (&ldquo;Here I stand, I can do no other&rdquo; is the famous form; the earliest printed accounts add it, the transcript does not. Say &ldquo;as the story goes.&rdquo;) Protestantism begins with that sentence, and it is the reason none of the instruments on the egg could work: a creed can name who agrees, but it cannot make anyone believe. Click for the consequence.</aside></section>')

A(Q('&ldquo;&hellip;my conscience is captive to the Word of God. I cannot and will not recant anything, since <b>it is neither safe nor right to go against conscience</b>.&rdquo;', 'Martin Luther at Worms, 18 April 1521', 'Here I stand') +
  N('The documented words. The Declaration opens by saying the same thing, three centuries later, in Pennsylvania.'))

A(Q('&ldquo;&hellip;it is high time for us not only to think, but also to <b>act, for ourselves</b>; to see with our own eyes, and to take all our measures directly and immediately from the Divine standard&hellip;&rdquo;', DA, 'Preamble') +
  N('The Preamble&rsquo;s first sentence. The first word of the movement is a verb.'))

A(Q('&ldquo;&hellip;as no man can be judged for his brother, so <b>no man can judge for his brother</b>; every man must be allowed to judge for himself, as every man must bear his own judgment&mdash;must give account of himself to God.&rdquo;', DA, 'Preamble') +
  N('Its second sentence. Not a right claimed but an impossibility stated: you cannot believe for someone else. Zurich and 1806 on the egg were the magistrate trying.'))

A(Q('&ldquo;It is not the voice of the multitude, but the voice of truth, that has power with the conscience; that can produce rational conviction and acceptable obedience. <b>A conscience that awaits the decision of the multitude</b>&hellip;&rdquo;', DA, 'The Address') +
  N('The Address says it of a General Council by name. Every council on the egg was a multitude deciding for a conscience.', '&rarr; So: given a people who must follow their conscience, given that no council can forever bind it, what is left to unite on?'))

A('<section class="slide"><h2>What can Christians unite on?</h2>'
  '<div class="sub frag">He prayed that they would be one. So it must be possible.</div>'
  '<aside class=notes>John 17:21, a prayer, not a command. The question, now that the issue is named. Pause on it before the answer.</aside></section>')

# ---------- 7 THE SOLUTION ----------

A(Q('&ldquo;&hellip;nor, indeed, can we reasonably expect to find it anywhere but in <b>Christ and his simple word</b>, which is the same yesterday, to-day, and forever.&rdquo;', DA, 'Preamble, continued') +
  N('The clause you stopped before. Now it has fifteen hundred years behind it.', '&rarr; Thomas Campbell saw only one answer: given a people called to follow their conscience, given that no council could forever bind it, the only thing Christians could unite on was Christ himself.'))

A(Q('&ldquo;&hellip;taking the Divine word alone for our rule; the Holy Spirit for our teacher and guide, to lead us into all truth; and <b>Christ alone, as exhibited in the word</b>, for our salvation&hellip;&rdquo;', DA, 'Preamble, continued') +
  N('Guard: it is not creedless. &ldquo;Christ alone, <i>as exhibited in the word</i>.&rdquo; The fence is what Scripture expressly says, and nothing else. The propositions say how.'))

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
  N('The one resolution to keep. It is the fuse.'))

A('<section class="slide"><div class=eyebrow>The reception</div>'
  '<div class=litany>'
  '<div class="no frag">October 1810 &middot; the Synod of Pittsburgh refuses Christian and ministerial communion. <b>Nobody joins.</b></div>'
  '<div class="no frag">May 1811 &middot; the Society that was &ldquo;by no means a Church&rdquo; <b>becomes one.</b></div>'
  '<div class="no frag">Thirteen propositions offered &ldquo;not as a new creed&rdquo; are, by the heirs, <b>treated as one.</b></div>'
  '</div>' +
  N('Candor beat, three clicks. A unity plea addressed to every party and joined, in the event, by almost no one; the synod&rsquo;s refusal is Week 5&rsquo;s opening. The second line is Brush Run, two weeks from now. The third is the long fuse: the document warned against its own later use, and its heirs did it anyway. That detonates in Chapter 12.', '&rarr; Chalcedon said &ldquo;not a new creed&rdquo; too. Honoring this document means keeping it a plea, not a pattern.'))

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

