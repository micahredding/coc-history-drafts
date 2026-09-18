# -*- coding: utf-8 -*-
# Week 2 deck content. S = list of (html) slides.
def C(name, gloss, note):   # chapter card
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<div class="sub nt">%s</div><aside class=notes>%s</aside></section>' % (name, gloss, note))

S = []
A = S.append

# ---------- 1 THE CAVALRY (cold open) ----------
A('<section class="slide"><h2 class=nt>Ireland. The summer of 1798.</h2>'
  '<div class="sub frag nt">A rebellion had just failed &mdash; and it was not the rebellion you would expect.</div>'
  '<aside class=notes><b>Black screen. No title, no date card, no preamble.</b> Put us in the room first.'
  '<span class=narr>[MR &mdash; the opening line. Job: put us inside a church service in Ireland in the summer of 1798 before anyone knows whose church it is.]</span></aside></section>')

A('<section class="slide"><div class="eyebrow quiet">The United Irishmen</div>'
  '<h2>Catholics, Anglicans and Presbyterians &mdash; <span style="color:var(--gold)">together</span>.</h2>'
  '<div class="sub frag">Against British rule. It failed, and the reprisals were running.</div>'
  '<div class="small frag">Which is why a Presbyterian meeting house was under suspicion: <b>a great many Presbyterians had been in it.</b></div>'
  '<aside class=notes><b>This is the correction to the page.</b> The site currently frames the Irish violence as Catholic-vs-Protestant gangs. That is the <i>Armagh</i> conflict &mdash; Peep O&rsquo;Day Boys and Defenders &mdash; and it is a different story. Keep it for the addendum.'
  '<span class=narr>[MR &mdash; two sentences. The rising was cross-confessional; the reprisal was British; his congregation was suspect <i>because</i> Presbyterians had joined it.]</span></aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Probably Ahorey &middot; eight miles from Armagh</div>'
  '<h2>A troop of Welsh cavalry surrounded the building.</h2>'
  '<div class="sub frag">Notorious, Foster says, for indiscriminate execution of old men, boys and women.</div>'
  '<div class="sub frag">The captain dismounted and walked in <b>alone</b>.</div>'
  '<aside class=notes>Stationed at Newry. He comes in by himself &mdash; that is what makes it frightening rather than chaotic.'
  '<span class=narr>[MR &mdash; the arrival, and the captain walking up the aisle &ldquo;casting fierce glances upon all sides.&rdquo;]</span></aside></section>')

A('<section class="slide"><p class=bigquote><span class=q>&ldquo;Pray, sir!&rdquo;</span></p>'
  '<div class=cite>a venerable elder, sitting near Mr. Campbell<span class=loc>Richardson, <i>Memoirs</i> 1:44</span></div>'
  '<aside class=notes>&#9733; <b>The best detail in the scene, and the page does not have it.</b> Campbell does not think of it himself. An elder tells him to pray.<br>'
  'It is also the first time in this class that <b>a layman decides what happens in a room</b> &mdash; which is the whole argument of the twelve weeks.'
  '<span class=narr>[MR &mdash; one line setting up the elder, then let the two words stand.]</span></aside></section>')

A('<section class="slide"><div class="eyebrow quiet">He began in the language of the forty-sixth Psalm</div>'
  '<p class=bigquote><span class=q>&ldquo;Thou, O God, art our refuge and strength, a very present help in trouble.</span></p>'
  '<p class="bigquote frag"><span class=q>Therefore will not we fear, though the earth be removed and though the mountains be carried into the midst of the sea.&rdquo;</span></p>'
  '<aside class=notes>&ldquo;in a deep, unfaltering voice.&rdquo; Let the whole thing be read; do not summarise it.</aside></section>')

A('<section class="slide"><h2>The captain paused, bent his head, and listened to the close.</h2>'
  '<div class="sub frag">Then he bowed, retraced his steps, mounted his horse, <b>and dashed away with the entire troop.</b></div>'
  '<div class="small frag nt">Foster gives the whole scene &ldquo;according to the story.&rdquo; It is family tradition, not a document. Say so in a clause and move.</div>'
  '<aside class=notes><b>The hedging clause is not optional</b> &mdash; this is the least-evidenced scene in the hour and it is first, in a class that has taught the room to expect counted evidence. One clause. The addendum carries the rest.'
  '<span class=narr>[MR &mdash; the landing line. Job: <i>nothing was taken from him that day.</i>]</span></aside></section>')

# ---------- TITLE (after the cold open) ----------
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Week 2</div>'
  '<h1>Thomas Campbell&rsquo;s Break</h1><div class=table-line></div>'
  '<div class=sub>Ireland 1798 &mdash; Pennsylvania 1810</div>'
  '<aside class=notes><b>The title comes up only now, after the cavalry has ridden off.</b> Cold open done; say the class name once and go to the next card.'
  '<span class=cast><i>EVERYONE QUOTED IN THIS DECK</i><br>'
  '<i>Thomas Campbell</i> &mdash; 44 in 1807. The defendant.<br>'
  '<i>William Wilson</i> &mdash; the younger minister assigned to assist him; the complainant.<br>'
  '<i>John Anderson</i> (1748&ndash;1830) &mdash; senior minister, professor of theology, Wilson&rsquo;s old teacher; the prosecutor.<br>'
  '<i>Robert Richardson</i> &mdash; Alexander Campbell&rsquo;s biographer, 1868. The family&rsquo;s account.<br>'
  '<i>W. H. Hanna</i> &mdash; 1935; transcribed the Chartiers Presbytery minute book.<br>'
  '<i>James P. Miller</i> &mdash; 1839; Anderson&rsquo;s own student, writing his memoir.</span>'
  'Budget: ~43 min. Three room turns at <b>~7</b>, <b>~22</b>, <b>~43</b>. The reunion is the climax and now has ~7 min; beats 1&ndash;3 and the trial gave it the time.</aside></section>')

# ---------- 2 DIVISION AFTER DIVISION ----------
A(C('Division After Division','Who this man was, in four words.',
    '&#9733; <b>Perform a subtraction. Do not teach Scottish church history.</b><br>Say the whole designation once, then peel one word at a time &mdash; and after each peel, <b>name who can no longer eat with whom</b>. Ninety seconds. It should feel like watching a room empty.'))

A('<section class="slide"><div class="eyebrow quiet">His full designation in 1807</div>'
  '<h2 class=litany>Old Light &middot; Anti-Burgher &middot; Seceder &middot; Presbyterian<br>'
  '<span class=dim>of the Associate Synod of North America</span></h2>'
  '<div class="sub frag">Every one of those words is a division from other Christians.</div>'
  '<aside class=notes>Say it whole, once, at speed. Then take it apart &mdash; Seceder, Anti-Burgher, and one clause for <b>Old Light</b>: the Anti-Burghers split <i>again</i> in 1806 over whether magistrates may suppress heresy, and Campbell landed on the conservative side, Foster says, &ldquo;not so much because of strong convictions&hellip; but because of personal relationships.&rdquo; One clause; no slide.'
  '<span class=narr>[MR &mdash; &ldquo;each of those terms designating a division from another group of Christians&rdquo; is already your sentence on the site. Use it here.]</span></aside></section>')

A('<section class="slide"><div class=eyebrow>Seceder &middot; 1733</div>'
  '<h2>They left over <span style="color:var(--gold)">patronage</span>.</h2>'
  '<div class=body>Lay patrons appointing ministers over congregations that had not called them. Parliament stripped the presbyteries of the right to overrule a patron; the General Assembly backed the patrons; the dissenting presbyteries walked out.</div>'
  '<div class="sub frag" style="color:var(--gold)">His tradition began as a protest against imposed authority.</div>'
  '<aside class=notes>&#9733; <b>Plant this and leave it.</b> The whole hour collects on it: the body that was founded to resist imposed authority is about to impose it on him.</aside></section>')

A('<section class="slide"><div class=eyebrow>Anti-Burgher &middot; 1747</div>'
  '<h2>They split over an oath.</h2>'
  '<div class=body>After the 1745 rising, city officials in <b>Glasgow, Edinburgh and Perth</b> had to swear they held &ldquo;the true religion presently professed within this realm, and authorized by the laws thereof.&rdquo;</div>'
  '<div class="sub frag">Burghers: that only means <i>not Catholic</i>.</div>'
  '<div class="sub frag">Anti-Burghers: that endorses the church we just left.</div>'
  '<aside class=notes>Three cities. That is the entire geographic reach of the quarrel.</aside></section>')

A('<section class="slide hard"><h2>Two years later the Anti-Burghers <span style="color:var(--brick)">excommunicated every Burgher minister.</span></h2>'
  '<div class="sub frag">&ldquo;Mutual condemnation and <b>mutual forbidding of intermingling</b>.&rdquo;</div>'
  '<div class="small frag nt">Hold that phrase. In seventy pages of this story it is the reason a family goes years without the Lord&rsquo;s Supper.</div>'
  '<aside class=notes>&#9733; <b>This is the rule that beat 7 breaks.</b> Plant it now and Conemaugh costs nothing to set up.</aside></section>')

A('<section class="slide hard"><h2 class=nt>And the oath?</h2>'
  '<p class=bigquote><span class=q>It applied in three Scottish cities.</span></p>'
  '<div class="sub frag" style="color:var(--gold)">It had never been required in Ireland at all.</div>'
  '<aside class=notes>&#9733; <b>The punchline of the beat.</b> His congregation was divided over an oath not one of them would ever be asked to take.'
  '<span class=narr>[MR &mdash; your site sentence says the dispute was &ldquo;a whole country away.&rdquo; It is stronger than that: it did not apply to them.]</span></aside></section>')

# ---------- 3 THE ELDERS ----------
A(C('The Elders','Seated and disciplined in the same sitting.',
    'The contrast the cold open was built for. <b>Nobody here is his enemy.</b>'))

A('<section class="slide"><div class="eyebrow quiet">Four courts &mdash; say them once, plainly</div>'
  '<div class=body style="text-align:left;max-width:46em">'
  '<b>General Associate Synod</b> (Scotland) &mdash; supreme court over every Anti-Burgher church anywhere.<br><br>'
  '<b>Anti-Burgher Seceder Synod of Ulster</b> &mdash; the Irish synod. Subordinate to Scotland.<br><br>'
  '<b>Associate Presbytery of Markethill</b> &mdash; his presbytery. <b>It ordained him in 1798.</b><br><br>'
  '<b>Ahorey</b> &mdash; his congregation.</div>'
  '<aside class=notes>Licensed to preach 1791; ordained and installed at Ahorey 1798.<br>'
  '<b>Do not linger.</b> The room needs this only so that the next two beats are legible &mdash; the presbytery ordains, the synod seats, Scotland overrules.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Why his ordination was not reported for a year</div>'
  '<p class=bigquote><span class=q>&ldquo;prevented from meeting&hellip; by the <b>ever memorable and melancholy disturbances of the country</b>, particularly in the place of meeting.&rdquo;</span></p>'
  '<div class=cite>Minutes of the Anti-Burgher Synod of Ulster, 1799</div>'
  '<aside class=notes>&#9733; <b>The join between beats 1 and 3.</b> The same rising that put Welsh cavalry in his church stopped his synod from sitting. Say that out loud &mdash; it is the only place the two halves of 1798 touch.</aside></section>')

A('<section class="slide"><div class=eyebrow>October 1798</div>'
  '<h2>He helped found the Evangelical Society of Ulster.</h2>'
  '<div class=body>Cross-denominational. Supporting Reformed missionaries <b>&ldquo;regardless of their denomination.&rdquo;</b> Tied to the London Missionary Society.</div>'
  '<aside class=notes>Three sentences maximum. What it was is enough; do not narrate Irish church politics.</aside></section>')

A('<section class="slide"><div class=eyebrow>30 July &ndash; 1 August 1799</div>'
  '<h2>At the synod meeting that admitted him&hellip;</h2>'
  '<p class="bigquote frag"><span class=q>&ldquo;Mr. Campble was added to the list and took his seat accordingly.&rdquo;</span></p>'
  '<p class="bigquote frag"><span class=q>&ldquo;Is the Evangelical Society of Ulster constituted on principles consistent with the Secession Testimony?&rdquo;</span></p>'
  '<div class="sub frag">The synod voted no.</div>'
  '<aside class=notes>&#9733; <b>Seated and disciplined in one sitting.</b> Both quotations are from the same minutes, the same meeting. That is the whole point of the slide &mdash; do not let them land as two separate events.</aside></section>')

A('<section class="slide hard"><h2>Three elders were sent to ask whether he would submit.</h2>'
  '<p class="bigquote frag"><span class=q>He agreed to &ldquo;try to see eye to eye&rdquo; with the synod.</span></p>'
  '<div class="sub frag nt">He gave up his leadership role. He was out of the society by 1800.</div>'
  '<div class="small frag nt" style="color:var(--gold)">Strike one. Nobody accused him. A body enforced its own boundary.</div>'
  '<aside class=notes>&#9733; <b>The foil closes here.</b> Name the pattern <i>as a pattern</i> &mdash; we watch him do this twice more. In Ireland the opposition is institutional; in America it becomes personal.<br> Cavalry surrounded the building and he did not move. Thirteen months later three of his own elders asked a question and he agreed to see eye to eye.'
  '<span class=narr>[MR &mdash; the line that pays off the cold open. Job: <i>the one that could destroy him was never the one with the horses.</i>]</span></aside></section>')

A('<section class="slide room"><div class=eyebrow>&#9670; the room</div>'
  '<h2>Who here grew up in another tradition?</h2>'
  '<div class="sub frag">Hands.</div>'
  '<aside class=notes><b>~minute 7. Stop talking.</b><br>'
  'Then the Idea 1 move, said now instead of saved for the end: <i>in a sense, so did this movement.</i><br><br>'
  '&#9733; This is also where the co-teacher&rsquo;s Week 1 question gets answered &mdash; Church of Christ people getting itchy at the word <i>tradition</i>, with people from other traditions in the room. Better handled at minute 7 than left to build to minute 33.</aside></section>')


# ---------- 4 THE UNION PROPOSAL ----------
A(C('The Union Proposal','They let him argue. They would not let it come to a vote.',
    'Strike two &mdash; and now it is the higher court overruling his own.'))

A('<section class="slide"><div class=eyebrow>October 1804 &middot; Rich Hill</div>'
  '<h2>He tried to put the two halves back together.</h2>'
  '<div class=body>A formal proposal to reunite Burghers and Anti-Burghers <b>in Ireland</b> &mdash; on the ground that the oath had never applied there. The Synod of Ulster, meeting at Belfast, <b>&ldquo;favorably received&rdquo;</b> it.</div>'
  '<div class="sub frag">Then Scotland heard about it.</div>'
  '<aside class=notes>The Irish body was willing. This is the closest the Secession came to healing itself in his lifetime.</aside></section>')

A('<section class="slide hard"><div class="eyebrow quiet">Sent to Glasgow to ask that the Irish churches decide for themselves</div>'
  '<p class=bigquote><span class=q>The synod &ldquo;allowed him to argue his case but <b>refused to allow the proposition to come to a vote</b>.&rdquo;</span></p>'
  '<div class=cite>Foster, on the General Associate Synod</div>'
  '<aside class=notes>&#9733; <b>Land on this.</b> Not defeated &mdash; never permitted to be decided. He is heard and then the question is taken away from him.<br>'
  'Strike two.'
  '<span class=narr>[MR &mdash; one sentence naming the pattern: twice now he has tried, and twice a court has closed it.]</span></aside></section>')

# ---------- 5 SEA VOYAGE & ALEXANDER ----------
A(C('Sea Voyage &amp; Alexander','A physician&rsquo;s prescription.',
    'Keep this short. It exists to move him across the Atlantic and to <b>plant Alexander</b>.'))

A('<section class="slide plateslide tight"><div class=eyebrow>8 April 1807 &middot; Londonderry</div>'
  '<figure class="plate short"><img src="IMG_TCAMPBELL" alt="" style="max-height:40vh"><figcaption>Thomas Campbell, 1763&ndash;1854</figcaption></figure>'
  '<h2>His doctor told him the only remedy was to get out from under it.</h2>'
  '<div class=body>Teaching, pastoring Ahorey, and synod work had produced a debilitating illness. The prescription was <b>a sea voyage</b>. He sailed on the <i>Brutus</i>; thirty-five days; Philadelphia in May.</div>'
  '<div class="sub frag nt">He is also leaving because he lost both campaigns.</div>'
  '<aside class=notes>He travelled with a young charge, Hannah Acheson, whom he left at Washington with her uncle. Colour only &mdash; cut if time is short.</aside></section>')

A('<section class="slide"><h2>He left his eighteen-year-old son in charge of the family and the school.</h2>'
  '<div class="sub frag">His name was Alexander.</div>'
  '<div class="small frag nt">One clause here. Everything in the last beat depends on it being planted now.</div>'
  '<aside class=notes>&#9733; <b>Do not spend more than a clause.</b> This is a seed, not a subplot. It germinates in beat 10.</aside></section>')

# ---------- 6 AMERICAN APPOINTMENTS ----------
A(C('American Appointments','A country where the quarrel was already dead.',
    'The payoff of beat 2, collected as a callback.'))

A('<section class="slide"><div class="eyebrow quiet">He landed to find his own synod in session</div>'
  '<h2>Assigned, at his own request, to the Presbytery of Chartiers.</h2>'
  '<div class=body>Western Pennsylvania, where old neighbours from Ireland had already settled. He made his way across the mountains and settled near the <b>town of Washington</b> &mdash; about thirty miles <b>south-west</b> of Pittsburgh.</div>'
  '<div class="sub frag">The July presbytery gave him preaching stations in <b>four counties</b>: Beaver, Allegheny, Indiana &mdash; and his own, Washington.</div>'
  '<aside class=notes>The four counties matter. They are why, in six weeks, he is seventy miles from home.</aside></section>')

A('<section class="slide hard"><div class="eyebrow quiet">And the quarrel in his sect&rsquo;s name?</div>'
  '<p class=bigquote><span class=q>The Associate Synod of North America <b>had already merged the Burghers and the Anti-Burghers.</b></span></p>'
  '<div class="sub frag">There was no burgess oath in America. There were no burgesses.</div>'
  '<div class="sub frag" style="color:var(--gold)">The fences of a dead quarrel were about to prosecute him anyway.</div>'
  '<aside class=notes>&#9733; <b>This is why the name got its own beat.</b> If you unpack &ldquo;Anti-Burgher&rdquo; here, this is just information. Unpacked twenty minutes ago, it is a callback and it lands.</aside></section>')

A('<section class="slide"><p class=bigquote><span class=q>&ldquo;&hellip;the various fragments of religious parties, which, having floated off from the Old World upon the tide of emigration, had been thrown together in <b>the circling eddies of these new settlements</b>.&rdquo;</span></p>'
  '<div class=cite>Robert Richardson<span class=loc><i>Memoirs</i> 1:224</span></div>'
  '<aside class=notes>The best scene-setting sentence in the week. Let it sit; do not gloss it.</aside></section>')

# ---------- 7 COMMUNION AT CONEMAUGH ----------
A(C('Communion at Conemaugh','August 1807. Seventy miles from home.',
    '&#9733; The Week 1 restatement lives at the top of this beat now &mdash; <b>two minutes before the fence is broken instead of forty.</b>'))

A('<section class="slide plateslide tokenslide"><div class=eyebrow>You remember what a Scottish communion was</div>'
  '<figure class="plate short"><img src="IMG_TOKEN" alt=""><figcaption>A Scottish communion token, 1750</figcaption></figure>'
  '<div class=body>The multi-day season. The fencing sermon. And the <b>token</b> &mdash; you were examined beforehand, and if you passed you were handed a small lead ticket to surrender at the table.</div>'
  '<aside class=notes><b>Re-run the Week 1 slide deliberately.</b> Same object, same image. Running it again <i>is</i> the recap &mdash; it costs no exposition.<br>'
  'And now add beat 2&rsquo;s rule to it: <b>mutual forbidding of intermingling.</b>'
  '<span class=narr>[MR &mdash; one sentence tying the token to the rule: this is the machinery, and this is who it kept out.]</span></aside></section>')

A('<section class="slide"><h2 class=nt>Faithful Presbyterians who had not received communion in years.</h2>'
  '<div class="sub frag">Not for lack of a minister.</div>'
  '<div class="sub frag" style="color:var(--gold)">For lack of a minister <b>of their own sub-sect</b>.</div>'
  '<aside class=notes>This is your sentence from the site, verbatim. It now lands as the <i>consequence</i> of the rule you planted in beat 2, instead of as an opening fact the room has no frame for.</aside></section>')

A('<section class="slide plateslide tight"><div class=eyebrow>Seventy miles from home</div>'
  '<figure class="plate wide"><img src="IMG_MAP" alt=""><figcaption>Reading Howell, <i>A Map of the State of Pennsylvania</i>, 1792 &middot; Library of Congress. The ring on the right marks the district, not a building &mdash; on this sheet it is still Westmoreland.</figcaption></figure>'
  '<div class="sub frag"><b>Washington</b>, his home, south-west of Pittsburgh. <b>Conemaugh</b>, the other way &mdash; the far edge of a four-county circuit.</div>'
  '<aside class=notes>Cannamaugh Church, Conemaugh Township, an Associate congregation founded 1798; Hanna finds it spelled <b>Cannamagh, Cannamaugh and Conemaugh</b> in one minute book, which is why two published histories put it in two different places. Ten seconds on that if you like &mdash; it shows the room how the record behaves.'
  '<br>&#9733; The point of the slide: <b>the open table was not his home ground.</b> It happened once, on a trip.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">The minister sent to assist him</div>'
  '<h2>William Wilson.</h2>'
  '<div class=body>Younger. Glasgow-educated. And already, Foster says, <b>&ldquo;upset by some of the religious views Campbell had formed in Ireland&rdquo;</b> &mdash; his opposition to subscription to creeds, and his openness to Christians outside the body.</div>'
  '<div class="sub frag" style="color:var(--gold)">He was troubled before the table. Not by it.</div>'
  '<aside class=notes>This matters for fairness: Wilson is not scandalised by one act of hospitality. He had been uneasy for the whole journey.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Fencing the table, he declined to do the usual thing</div>'
  '<h2>He &ldquo;would not go over the commands.&rdquo;</h2>'
  '<div class=body>He offered terms of communion <b>generally</b> &mdash; not particularly. Because to require assent to them <i>particularly</i>, he said, would be to demand&hellip;</div>'
  '<p class="bigquote frag"><span class=q>&ldquo;implicit faith.&rdquo;</span></p>'
  '<aside class=notes>&#9733; <b>The sharpest idea in the file.</b> <i>Implicit faith</i> is the Protestant term of abuse for Roman submission to the church&rsquo;s teaching without personal understanding.<br>'
  'He is standing in front of a room of Seceders telling them <b>their fence is functionally Roman.</b> Say that.<br>'
  '<i>Source: Wilson&rsquo;s own deposition, in the trial record.</i></aside></section>')

A('<section class="slide"><div class="eyebrow quiet">And then the invitation</div>'
  '<p class=bigquote><span class=q>&hellip;that all his pious hearers, &ldquo;who felt so disposed and duly prepared, should, <b>without respect to party differences</b>, enjoy the benefits of the communion season then providentially afforded them.&rdquo;</span></p>'
  '<div class=cite>Richardson, <i>Memoirs</i> 1:224</div>'
  '<aside class=notes>The act itself, in the only words we have for it. Nine words are doing the work: <i>without respect to party differences.</i></aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Two years later he wrote down why it mattered</div>'
  '<p class=bigquote><span class=q>&ldquo;&hellip;the dispensations of the Lord&rsquo;s Supper, <b>that great ordinance of unity and love</b>.&rdquo;</span></p>'
  '<div class="sub frag">&ldquo;&hellip;the great fundamental law of unity and love ought not to be violated to make way for <b>exalting human opinions to an equality with express revelation, by making them articles of faith and terms of communion</b>.&rdquo;</div>'
  '<div class=cite><i>Declaration and Address</i>, 1809</div>'
  '<aside class=notes>&#9888; <b>Say &ldquo;two years later he put it this way.&rdquo;</b> These are 1809, not 1807. Do not let the room hear them as what he said at the table.'
  '<br>But they are the best statement he ever made of why a table was worth this, and the beat needs his own voice, not a summary.</aside></section>')

A('<section class="slide"><h2 class=nt>It was well received.</h2>'
  '<div class="sub frag">He was heartened about the possibilities for the growth of Christian brotherhood.</div>'
  '<div class="sub frag" style="color:var(--brick)">But back in Pittsburgh, things did not go so well.</div>'
  '<aside class=notes>Your sentences, verbatim from the site.<br><b>Nobody objected in the room.</b> The complaint travels afterward &mdash; and that is the difference from Cane Ridge, where the objection came first and Stone answered it on the spot.</aside></section>')

# ---------- 8 THE TRIAL ----------
A(C('The Trial','The fence fights back.',
    'Micah&rsquo;s own phrase for this beat. ~12 minutes, of which <b>six belong to the room</b>.'))

A('<section class="slide"><h2 class=nt>Before any of it starts, hold one question.</h2>'
  '<p class="bigquote frag"><span class=q>What can they actually take from him?</span></p>'
  '<div class="small frag nt">Ask it. Do not answer it. It gets answered in the next chapter, on a black screen.</div>'
  '<aside class=notes>&#9733; <b>The withheld question.</b> Week 1 held &ldquo;what were they converging on?&rdquo; for thirty-seven slides. This is the Week 2 equivalent and it is much shorter-range &mdash; plant here, re-ask at the end of the beat, answer in beat 9.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Wilson reported it &mdash; to his own old schoolmaster</div>'
  '<h2>John Anderson, 1748&ndash;1830.</h2>'
  '<div class=body>He taught Wilson at his log seminary and was professor of theology for the churches of the Chartiers Presbytery. He refused to keep a preaching appointment with Campbell at Buffaloe.</div>'
  '<div class="sub frag">His stated reason: doctrines <b>&ldquo;inconsistent with some articles of our testimony.&rdquo;</b></div>'
  '<aside class=notes>&#9733; <b>The mechanism, and it is not a conspiracy.</b> Wilson complained to the man who trained him. The investigating committee was Anderson plus <b>three of his own former students</b> &mdash; Wilson, Allison, Ramsay &mdash; and an elder.<br>'
  'A small frontier seminary&rsquo;s alumni network, sitting as a court.<br>'
  'The only portrait in circulation is unsourced and shows a man of about thirty; Anderson was fifty-nine. It is not in the deck. His title page, a few slides on, is the authenticated image of him.</aside></section>')

A('<section class="slide hard"><div class=eyebrow>October 1807 &middot; the minutes</div>'
  '<p class=bigquote><span class=q>&ldquo;Mr. Campbel gave in a verbal protest and having said that <b>he would not sit any longer in this Presbytery</b>, he withdrew.&rdquo;</span></p>'
  '<aside class=notes>&#9888; <b>Use this, not &ldquo;he stormed out.&rdquo;</b> Foster&rsquo;s phrase is a characterisation; this is the clerk&rsquo;s.<br>'
  'And it is better: not a man losing his temper, and not a victim either. He states a reason, enters a protest, and leaves.<br>'
  'They had suspended his appointments &mdash; and with them his income.</aside></section>')

A('<section class="slide room"><div class=eyebrow>&#9670; the room</div>'
  '<h2>You are the court.</h2>'
  '<div class=body>Three of the seven charges, read exactly as they were written. No commentary.</div>'
  '<div class="sub frag">Then: guilty, or not guilty?</div>'
  '<aside class=notes><b>~minute 24. Six minutes. Hand it over.</b><br>'
  'Co-teacher reads the charges, or takes the vote &mdash; this works far better with two voices.<br>'
  'Read Articles 1, 2 and 4. Do not gloss. Do not signal the answer.</aside></section>')

A('<section class="slide"><div class=eyebrow>Article 1</div>'
  '<p class=bigquote><span class=q>&ldquo;It is erroneous&hellip; to teach that a person&rsquo;s appropriation of Christ to himself as his own Savior <b>does not belong to the essence of Saving Faith</b>; but only to a high degree of it.&rdquo;</span></p>'
  '<aside class=notes>In plain terms: <i>you can be saved without feeling certain that you are.</i></aside></section>')

A('<section class="slide"><div class=eyebrow>Article 2</div>'
  '<p class=bigquote><span class=q>&ldquo;It is erroneous&hellip; to assert that a church has <b>no divine warrant for holding Confessions of Faith as terms of communion</b>.&rdquo;</span></p>'
  '<aside class=notes>&#9888; Note for you, not the room: <i>terms of communion</i> here means terms of church fellowship, which is broader than admission to the Supper. The table is the right hinge, but do not say the charge is about the Supper &mdash; they are looking at the words.</aside></section>')

A('<section class="slide"><div class=eyebrow>Article 4</div>'
  '<p class=bigquote><span class=q>&ldquo;It is erroneous&hellip; to assert that it is warrantable for the people of our communion to <b>hear ministers that are in a stated opposition to our testimony</b>.&rdquo;</span></p>'
  '<div class="sub frag nt">Remember this one.</div>'
  '<aside class=notes>&#9733; <b>&ldquo;Occasional hearing.&rdquo;</b> Flag it lightly now. In the last beat his own son will be doing it every week in Glasgow.<br><br>'
  '<b>NOW TAKE THE VOTE.</b></aside></section>')

A('<section class="slide hard"><h2>Which of the seven charges is about the communion table?</h2>'
  '<div class="sub frag">Saving faith &middot; confessions &middot; ruling elders &middot; occasional hearing &middot; Christ under the precept &middot; sinless perfection &middot; preaching in another man&rsquo;s bounds</div>'
  '<p class="bigquote frag"><span class=q>None of them.</span></p>'
  '<aside class=notes>&#9733; <b>Let them look for it.</b> Give it real silence.<br>'
  'Articles 1 and 2 are recorded as taught &ldquo;at Conemaugh&rdquo; &mdash; but no article charges him with communing non-Seceders.'
  '<span class=narr>[MR &mdash; the line that lands the turn. Job: <i>they never indicted the thing he did. They indicted the beliefs that made him do it.</i>]</span></aside></section>')

A('<section class="slide plateslide"><div class=eyebrow>And Article 1 prosecutes the thesis of the prosecutor&rsquo;s own book</div>'
  '<figure class="plate short"><img src="IMG_ANDERSONTITLE" alt=""><figcaption>John Anderson, <i>The Scripture Doctrine of the Appropriation which is in the Nature of Saving Faith</i><br>Philadelphia, 1793 &middot; 1797 Edinburgh reprint shown</figcaption></figure>'
  '<div class="small frag">Its epigraph is <b>Acts 15:11</b> &mdash; one of the proof-texts cited in Article 1.</div>'
  '<aside class=notes>&#9733; <b>No commentary needed. Put it up and wait.</b><br>'
  'The title page also identifies him without a caption: &ldquo;Minister of the Gospel, in the Associate Congregations of Mill-Creek, Kings-Creek, and Racoon, <b>near Pittsburgh</b>.&rdquo;<br>'
  'And there is a second: <b>Article 4 is the subject of his 1794 <i>Sermon on Occasional Hearing</i>.</b> Two of the seven charges sit on this one man&rsquo;s published theology.<br>'
  '&#9888; The scan on hand is the 1797 Edinburgh reprint &mdash; which says &ldquo;Philadelphia, printed&rdquo; on its face. Caption it honestly if the date shows.</aside></section>')

A('<section class="slide"><div class=eyebrow>12 February 1808 &middot; the verdict</div>'
  '<p class=bigquote><span class=q>&ldquo;&hellip;judged the <b>1 &amp; 2 clearly proved</b>&rdquo;</span></p>'
  '<div class="sub frag">3, 4 and 7 &mdash; <b>&ldquo;acknowledged&hellip; and still adhered to by him.&rdquo;</b> He admitted them and would not back down.</div>'
  '<div class="sub frag">6 approved &mdash; <b>except a quibble over &ldquo;or&rdquo; versus &ldquo;and.&rdquo;</b></div>'
  '<aside class=notes>Read it as a scoreboard, fast.<br>&#9733; <b>The &ldquo;or/and&rdquo; line is the whole institution in four words. Do not explain it. Let it sit.</b><br>If asked about the court: Article 7 charges him with preaching in <b>Ramsay&rsquo;s</b> bounds, and Ramsay sat on the committee that drafted it; the minute book has a page cut out at p. 129 and the February minutes rewritten on sewn-in pages &mdash; Hanna: &ldquo;a mysterious transaction, which will probably never be revealed.&rdquo; Say what is there; do not overclaim.</aside></section>')

A('<section class="slide hard"><div class=eyebrow>11 March 1808</div>'
  '<h2>Three men reconvened after the meeting had closed.</h2>'
  '<div class=body>Anderson, Wilson and Allison &mdash; after Campbell had left and the presbytery had adjourned &mdash; &ldquo;continue the suspension <b><i>sine die</i></b>, which he was laid under at the last meeting.&rdquo;</div>'
  '<div class="sub frag" style="color:var(--brick)">Indefinitely. With no date to return.</div>'
  '<aside class=notes>This is the act that actually ended his ministry, and it was done by three people in an empty room.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Then two years, in one line</div>'
  '<div class=days>'
  '<div class="d"><span class=dn>Aug 1807</span> the table</div>'
  '<div class="d"><span class=dn>Oct 1807</span> he walks out of presbytery</div>'
  '<div class="d"><span class=dn>Jan 1808</span> the libel &middot; seven charges</div>'
  '<div class="d"><span class=dn>Feb 1808</span> censure, suspension</div>'
  '<div class="d now"><span class=dn>May 1808</span> the appeal, Philadelphia</div>'
  '<div class="d"><span class=dn>Sept 1808</span> he declines their authority</div>'
  '<div class="d"><span class=dn>May 1809</span> the last letter</div>'
  '</div>'
  '<aside class=notes>&#9733; <b>The compression fix. Sixty seconds. Do not narrate it beat by beat.</b><br>'
  'The room already understands the pattern from beats 2&ndash;4; it does not need the procedure. Then stop on exactly two moments and nothing else.</aside></section>')

A('<section class="slide"><div class=eyebrow>May 1808 &middot; read aloud, standing, to the Synod at Philadelphia</div>'
  '<div class="small nt">&ldquo;Honored Brethren: Before you come to a final issue in the present business, let me entreat you to <b>pause a moment</b>&hellip;&rdquo;</div>'
  '<p class=bigquote><span class=q>&ldquo;It is, therefore, because I have <b>no confidence, either in my own infallibility or in that of others</b>, that I absolutely refuse, as inadmissible and schismatic, the introduction of human opinions and human inventions into the faith and worship of the Church.&rdquo;</span></p>'
  '<div class=cite>Richardson, <i>Memoirs</i> 1:227</div>'
  '<aside class=notes>Dwell one. He opened by asking them to <i>pause a moment</i>; then this.<br>&#9888; <b>The next slide is a separate sentence, two pages later in the appeal.</b> The site page currently splices them with ellipses. Do not stage them as one.</aside></section>')

A('<section class="slide"><p class=bigquote><span class=q>&ldquo;For what error or immorality ought I to be rejected, except it be that I refuse to acknowledge as obligatory upon myself, or to impose upon others, anything as of Divine obligation for which I cannot produce a <b>&lsquo;Thus saith the Lord?&rsquo;</b>&rdquo;</span></p>'
  '<div class=cite>Richardson, <i>Memoirs</i> 1:227</div>'
  '<aside class=notes>The rule he will live by, stated to the court that is about to censure him for it.</aside></section>')

A('<section class="slide hard"><div class=eyebrow>Dwell two &middot; what the Synod did with it</div>'
  '<div class=body>It found <b>&ldquo;such informalities in the proceedings of the Presbytery&rdquo;</b> as to set their judgment aside, and lifted the suspension.</div>'
  '<div class="sub frag">Then a committee found his answers <b>&ldquo;so evasive and unsatisfactory, and highly equivocal&hellip; sufficient grounds to infer censure.&rdquo;</b></div>'
  '<div class="sub frag" style="color:var(--gold)">Overturned on procedure. Re-censured on substance.</div>'
  '<aside class=notes>Everyone in this room has been in a meeting that ended this way. Say so &mdash; it is the moment the story stops being about 1808.</aside></section>')

A('<section class="slide hard"><p class=bigquote><span class=q>&ldquo;he was accordingly <b>rebuked and admonished by the Mod&rsquo;r</b>&rdquo;</span></p>'
  '<div class="sub frag">He submitted &mdash; under a signed declaration that his submission meant <b>&ldquo;no more&hellip; than an act of deference to the judgment of the court.&rdquo;</b></div>'
  '<div class="small frag nt">Deference. Not agreement. <span style="color:var(--gold)">Strike three.</span></div>'
  '<aside class=notes>&#9733; <b>To his face, in front of the assembled Synod.</b> This beat used to end on the paperwork; it should end on the humiliation.<br><br>'
  'One more fact, and hold it: <i>at that same meeting he offered a letter declining their authority &mdash; and then withdrew it.</i></aside></section>')

A('<section class="slide"><h2 class=nt>So &mdash; what could they actually take from him?</h2>'
  '<aside class=notes>Re-ask the withheld question. Then go straight to the chapter card.</aside></section>')

# ---------- 9 THE GROVE ----------
A(C('The Grove','They took everything they had the authority to take.',''))

A('<section class="slide"><div class=eyebrow>13&ndash;14 September 1808 &middot; Burgettstown</div>'
  '<h2>He sent the same letter again. This time he did not withdraw it.</h2>'
  '<p class=bigquote><span class=q>&ldquo;&hellip;not being able to point out a single error in the former, and declaring themselves satisfied with the latter&hellip; <b>yet proceeded to find me guilty of evasion and equivocation</b>&hellip;&rdquo;</span></p>'
  '<div class="sub frag nt">&ldquo;&hellip;their manifest breach of faith and avowed dissimulation, (<b>I might add treachery</b>,) can not be innocent and unrebukable conduct.&rdquo;</div>'
  '<div class="sub frag" style="color:var(--gold)">&ldquo;Of the justness and propriety of this, <b>let the world judge</b>.&rdquo;</div>'
  '<aside class=notes>Hanna, from the minutes: &ldquo;in his own name and in the name of all who adhered to him, he <b>declined the authority of this Presbytery&hellip; and all further communion with them</b>.&rdquo; He had offered this in May and retracted it; by September he &ldquo;had seen cause to adhere to it.&rdquo; &#9888; <b>September 1808 is the break</b> &mdash; the sources confuse this with a later paper.<br>&#9733; He is <b>angry</b>, and the site narration does not show it. Printed by Alexander in the 1861 <i>Memoirs of Elder Thomas Campbell</i>.</aside></section>')

A('<section class="slide"><p class=bigquote><span class=q>&ldquo;It is with <b>sincere reluctance</b>&hellip; that I find myself in duty bound to refuse submission to their decision as unjust and partial; and also finally to decline their authority.&rdquo;</span></p>'
  '<div class="sub frag">&ldquo;And I hereby do <b>decline all ministerial connection with, or subjection to, the Associate Synod of North America</b>&hellip; and do henceforth hold myself <b>altogether unaffected by their decisions</b>.&rdquo;</div>'
  '<aside class=notes><i>Sincere reluctance.</i> He did not want to go.<br>'
  '&#9888; <b>Correction to the site page:</b> he did not resign &ldquo;from the Association.&rdquo; It was the <b>Associate Synod</b>. The <i>Association</i> is the Christian Association of Washington, which he founds in August 1809 &mdash; next week&rsquo;s chapter.</aside></section>')

A('<section class="slide breath"><h1 style="font-size:clamp(28px,5.4vmin,64px);line-height:1.25">&ldquo;And then Campbell discovered that this meant very little.&rdquo;</h1>'
  '<aside class=notes>&#9733;&#9733; <b>THE REVEAL. Black screen, this sentence, nothing else. Give it a full breath.</b><br>'
  'This is your sentence and it currently sits mid-paragraph on the site. It is Week 2&rsquo;s &ldquo;this was a communion service.&rdquo;</aside></section>')

A('<section class="slide"><p class=bigquote><span class=q>&ldquo;Sometimes the deep shade of a <b>maple grove</b> sheltered the assembly from the summer sun. Generally, however, the houses of his old Irish neighbors&hellip; were the places where he had his appointments for preaching, and where he discoursed weekly to <b>all who chose to assemble</b>.&rdquo;</span></p>'
  '<div class=cite>Richardson, <i>Memoirs</i> 1:231</div>'
  '<aside class=notes>No pulpit, no salary, no standing &mdash; and no interruption.'
  '<span class=narr>[MR &mdash; your line: an association, then a church, then a movement.]</span></aside></section>')

A('<section class="slide hard breath"><h2>And now the honest part.</h2>'
  '<div class="sub nt">They had a case. And the man who prosecuted him was not a villain.</div>'
  '<aside class=notes>&#9733; <b>Bracket this block at both ends in your own words</b>, the way Week 1 bracketed &ldquo;It wasn&rsquo;t perfect&rdquo; &rarr; &ldquo;It was a start.&rdquo;</aside></section>')

A('<section class="slide"><div class=body style="text-align:left;max-width:46em">'
  '<b>They had a real case.</b> He had broken rules he was ordained under. Some of his answers <i>were</i> equivocal &mdash; his written answer on confessions threads a very fine needle. The Synod accepted two of them.<br><br>'
  '<b>And it was live ground, not settled law.</b> The Seceders were at that moment revising their own <i>Narrative and Testimony</i> on exactly these questions.<br><br>'
  '<b>Richardson is the family&rsquo;s account.</b> The &ldquo;envy&hellip; in clerical bosoms&rdquo; is his; so are the spies.</div>'
  '<aside class=notes>The collision-of-goods framing is now a documented claim, not a charitable one.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">What Anderson&rsquo;s own student wrote about him, nine years after he died</div>'
  '<p class=bigquote><span class=q>&ldquo;As to his Christian graces, <b>meekness and humility</b> might be said to predominate. He was also most conscientiously and scrupulously <b>tender of the feelings of all, even to the very least</b>&hellip;&rdquo;</span></p>'
  '<div class=cite>James P. Miller, 1839<span class=loc>Anderson&rsquo;s pastor-and-pupil relation, in his own words</span></div>'
  '<aside class=notes>&#9888; Wrather&rsquo;s biography clips this man down to &ldquo;irascible&rdquo; and &ldquo;impatient of contradiction.&rdquo; <b>Two independent sources say meekness and humility.</b> Use the whole thing or none of it.</aside></section>')

A('<section class="slide hard"><div class="eyebrow quiet">And the gift his student praised him for</div>'
  '<p class=bigquote><span class=q>&ldquo;&hellip;the ear of the adept in music was not more quick to discern a discordant note, than was his <b>to detect a sentiment that accorded not with the oracles of God, or even an expression that varied</b>&hellip;&rdquo;</span></p>'
  '<div class="sub frag" style="color:var(--gold)">Campbell was convicted of being <b>equivocal</b>.</div>'
  '<aside class=notes>&#9733;&#9733; <b>This is the honest block finished, and it is better than &ldquo;envy.&rdquo;</b><br>'
  'The faculty that produced the verdict is the same faculty his own student celebrates. Not malice &mdash; <b>a praised virtue, turned on a colleague.</b>'
  '<span class=narr>[MR &mdash; the closing bracket of the honest block.]</span></aside></section>')

# ---------- 10 FAMILY REUNION ----------
A(C('Family Reunion','Two men on a road, each having walked away from the same table.',''))

A('<section class="slide bleed"><div class=bg><div class="bgimg wreckbg"></div></div>'
  '<div class=credit>Philippe Jacques de Loutherbourg (1740&ndash;1812), <i>A Shipwreck off a Rocky Coast</i><br>Not the <i>Hibernia</i>, and not Islay</div>'
  '<h2 class=nt>Three weeks after he broke, his family sailed.</h2>'
  '<div class="sub frag">1 October 1808. Jane and seven children &mdash; Alexander at twenty, down to two-year-old Alicia.</div>'
  '<aside class=notes>&#9888; Caption honestly: a period image of what the event looked like, not the event.'
  '<span class=narr>[MR &mdash; the sailing. Note the order: <b>he had already broken.</b> This is not a man deciding under pressure; it is a man who has decided, about to be given every reason to reconsider.]</span></aside></section>')

A('<section class="slide bleed"><div class=bg><div class="bgimg indaalbg"></div></div>'
  '<div class=credit>The shore of Loch Indaal, Isle of Islay &middot; CC BY-SA 2.0, geograph.org.uk</div>'
  '<h2>They were wrecked off Islay.</h2>'
  '<div class="sub frag">Everyone survived. They were stranded in Scotland for <b>ten months</b>.</div>'
  '<aside class=notes>Loch Indaal, on the south-west of the island. Alexander spent days pulling his father&rsquo;s books out of the water and drying them; some were rebound and ended up in his library in America.</aside></section>')

A('<section class="slide"><h2 class=nt>He found out. And he did not walk anything back.</h2>'
  '<div class="sub frag">Richardson: he &ldquo;received intelligence of the shipwreck, and the consequent delay of the family at Glasgow,&rdquo; and wrote them a letter <b>&ldquo;full of affectionate solicitude and consolation.&rdquo;</b></div>'
  '<div class="sub frag">In May he sent the Synod a formal notice &mdash; and four days later, <b>a letter enclosing a fifty-dollar note</b>, refunding the sum they had advanced him on his arrival.</div>'
  '<aside class=notes>&#9733; No income. No standing. Wife and seven children three thousand miles away after nearly drowning.<br><b>He sent the money back.</b><br>'
  'Fifty dollars &mdash; at four dollars for a Sabbath, about twelve Sundays&rsquo; preaching.</aside></section>')

A('<section class="slide"><div class=eyebrow>Meanwhile, in Glasgow</div>'
  '<h2>Alexander was going to church twice on Sunday.</h2>'
  '<div class=body>The Seceder church in the morning, under a minister he found <b>&ldquo;a prosy speaker&rdquo;</b> &mdash; whose delivery he sat there taking critical notes on.</div>'
  '<div class="sub frag">And in the evening, Greville Ewing&rsquo;s Tabernacle. Fifteen hundred people. <b>In a building that had been a circus.</b></div>'
  '<aside class=notes>Ewing: former establishment minister, co-worker of the Haldanes, had Alexander to dinner and tea repeatedly. Congregationalism &mdash; &ldquo;an entire emancipation from the control of domineering Synods and General Assemblies.&rdquo;</aside></section>')

A('<section class="slide hard"><div class="eyebrow quiet">Richardson&rsquo;s word for what Alexander was doing, in his own quotation marks</div>'
  '<p class=bigquote><span class=q>&ldquo;occasional hearing&rdquo;</span></p>'
  '<div class="sub frag" style="color:var(--gold)">That is Article 4 of the libel against his father.</div>'
  '<div class="small frag">Ewing, Mitchel at Anderston, Balford at George&rsquo;s Square, Wall at the Salt Market. <b>Every week.</b></div>'
  '<aside class=notes>&#9733;&#9733; <b>Nobody has put these two facts next to each other.</b> Thomas is on trial in Pennsylvania partly for saying occasional hearing is permissible. Alexander is in Glasgow doing it, weekly, while it happens.</aside></section>')

A('<section class="slide"><p class=bigquote><span class=q>&ldquo;&hellip;an effect which was, doubtless, facilitated by the fact that <b>his revered father, to whose religious sentiments he was accustomed to pay the utmost deference, was now separated from him by the wide Atlantic</b>.&rdquo;</span></p>'
  '<div class=cite>Richardson, on why Alexander changed</div>'
  '<aside class=notes>&#9733; The son drifts partly <i>because the father is not there</i> &mdash; while the father, unknown to him, is breaking too.<br>This is the emotional engine of the last beat. Do not rush it.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Then the communion season came round</div>'
  '<div class=body style="text-align:left;max-width:46em">He could not decide. He had no letter from Ahorey, so the session <b>examined him &mdash; and gave him the token.</b><br><br>'
  'The hour of the Supper <b>&ldquo;found him still undecided.&rdquo;</b> Eight hundred communicants; eight or nine tables served in turn.<br><br>'
  'He <b>waited for the last table</b>, &ldquo;in hopes of being able to overcome his scruples.&rdquo;</div>'
  '<aside class=notes>&#9733; <b>He nearly went through with it.</b> That is what makes this a scene instead of a gesture &mdash; he is not staging a protest, he is failing to talk himself into it.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Why he could not</div>'
  '<p class=bigquote><span class=q>&ldquo;&hellip;conscientious misgivings as to the propriety of <b>sanctioning any longer, by participation, a religious system which he disapproved</b>.&rdquo;</span></p>'
  '<div class="sub frag">Against a church &ldquo;<b>to which his father and the family belonged</b>, and in which he had thought it his duty to be a regular communicant.&rdquo;</div>'
  '<aside class=notes>&#9733;&#9733; <b>This is the answer: participation is sanction.</b><br>'
  'And it is the mirror of his father. Thomas: <i>you may not make this table a test of fellowship.</i> Alexander: <i>I will not let this table make me a witness for you.</i></aside></section>')

A('<section class="slide hard"><p class=bigquote><span class=q>&ldquo;&hellip;the ring of the token, falling upon the plate, announced the instant at which he renounced Presbyterianism for ever &mdash; <b>the leaden voucher becoming thus a token not of communion but of separation</b>.&rdquo;</span></p>'
  '<div class=cite>Richardson, <i>Memoirs</i> 1:190</div>'
  '<aside class=notes>He dropped the token and passed the bread and wine.<br><br>'
  '&#9888; <b>Do not reach for Luther and the church door.</b> Wrather raises that parallel and kills it: &ldquo;Young Campbell himself certainly saw nothing heroic in his action.&rdquo; He was twenty, he told no one, and &mdash; having complied with every rule &mdash; he collected <b>the usual certificate of good standing</b> on his way out. <b>The understatement is the power of it.</b></aside></section>')

A('<section class="slide"><div class=eyebrow>19 October 1809 &middot; the road into Washington, Pennsylvania</div>'
  '<h2>He rode out to meet them.</h2>'
  '<div class=body>Two and a half years. Riding back together, Thomas told his son what had happened &mdash; the contumely, the slanders circulated, the unjust proceedings of the Presbytery and the Synod.</div>'
  '<aside class=notes>Foster: Thomas got word of their arrival a few days after they landed and immediately left with a friend to meet them on the road.</aside></section>')

A('<section class="slide hard"><p class=bigquote><span class=q>&ldquo;&hellip;had they possessed the power, he would have suffered martyrdom at their hands, or, as he expressed it, that <b>&lsquo;nothing but the law of the land had kept his head upon his shoulders.&rsquo;</b>&rdquo;</span></p>'
  '<div class=cite>Richardson, <i>Memoirs</i> 1:219&ndash;220<span class=loc>reported speech &mdash; what his son remembered him saying</span></div>'
  '<aside class=notes>&#9733;&#9733; <b>The strongest line in the week.</b> Keep Richardson&rsquo;s qualifier &mdash; <i>had they possessed the power</i> &mdash; it is what keeps it honest, and it is also what makes it land.</aside></section>')

A('<section class="slide"><p class=bigquote><span class=q>&ldquo;Alexander could not but feel indignant at this recital&hellip; <b>He was greatly surprised, however, when informed by his father that the latter had actually dissolved his connection with the Seceders.</b>&rdquo;</span></p>'
  '<aside class=notes>&#9733; <b>He learned it on the road.</b> And Thomas did not know what his son had done in Glasgow.'
  '<span class=narr>[MR &mdash; the close. Job: the father invited people who had no token; the son held a valid one and would not use it. Neither knew.]</span></aside></section>')

# ---------- IDEAS ----------
A('<section class="slide ideasmap"><div class=eyebrow>What this week touched</div>'
  '<div class=wmap><div class="r ms-christ"><span class="th key">CHRIST ALONE</span></div>'
  '<div class="r ms-pri"><span class="th key">UNITY</span><span class="th on">PRIESTHOOD</span><span class="th on">FUTURE</span></div>'
  '<div class="r ms-sec"><span class="th on">HOMECOMING</span><span class="th on">SELF-SACRIFICE</span><span class="th key">FREEDOM OF CONSCIENCE</span><span class=th>SCIENCE &amp; REASON</span><span class="th on">MINIMALISM</span></div>'
  '<div class="r ms-pra"><span class="th key">the Table</span><span class=th>Baptism</span><span class="th on">Scripture</span><span class=th>Singing</span><span class="th on">Congregation</span></div></div>'
  '<div class=small>Bright: the spine of this week. Dim: touched in passing. Unlit: still ahead of us.</div>'
  '<aside class=notes>Same board as Week 1, lit for this week. Running it weekly is what makes twelve stories feel like one argument accumulating.<br>New light since last week: <b>Freedom of Conscience</b> and <b>Christ Alone</b> move to the spine; <b>Priesthood</b> (the elder who said &ldquo;Pray, sir&rdquo;) and <b>Minimalism</b> (&ldquo;Thus saith the Lord&rdquo;) come on dim.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 1 of 3</div>'
  '<h2>Non-creedalism is <span style="color:var(--gold)">a protective move.</span></h2>'
  '<div class="body nt">No human formulation as a test of fellowship &mdash; because no one&rsquo;s interpretation is infallible, and the simplest believer must be able to confess Christ and belong. <i>No confidence, either in my own infallibility or in that of others.</i></div>'
  '<aside class=notes>Not scepticism. A fence-removal justified by humility about our own readings.<br>The two ideas that used to precede this &mdash; <i>the unity movement did not begin in America</i>, and <i>they divided over hospitality, not doctrine</i> &mdash; were already said aloud at minute 7 and found by the room in the vote. Collect them in a sentence here if you want them; do not re-argue.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 2 of 3</div>'
  '<h2>Why a table was worth all this.</h2>'
  '<div class="body nt" style="color:var(--gold)">[MR &mdash; this one is yours and it is the one the class most needs.]</div>'
  '<aside class=notes>&#9733;&#9733; <b>UNWRITTEN. This is the spine&rsquo;s step 3.</b><br>'
  'Week 1 established the table as the age to come arriving early. Without that claim here, Week 2 argues for tolerance &mdash; rather than arguing that someone put a gate in front of God&rsquo;s future.<br>'
  'The spine lists it as a claim-note still to be authored. Nothing is drafted for you here on purpose.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 3 of 3</div>'
  '<h2>It cost him everything they could reach &mdash; <span style="color:var(--gold)">and he did not want to leave.</span></h2>'
  '<div class="body nt">Two years. Three courts. His appointments, his income, his standing. A rebuke to his face. Fifty dollars sent back. He appealed, he submitted, he deferred, and he spent two years trying to stay. The break was the last thing he tried, not the first.</div>'
  '<aside class=notes>This is what makes the grove cost something.</aside></section>')

A('<section class="slide room"><div class=eyebrow>&#9670; for discussion</div>'
  '<h2>What is beautiful here? What do we carry forward?</h2>'
  '<div class="sub frag">What &ldquo;testimonies&rdquo; &mdash; written or unwritten &mdash; do we treat as terms of fellowship today?</div>'
  '<div class="sub frag">What does conviction-without-coercion look like in practice?</div>'
  '<div class="sub frag" style="color:var(--gold)">Who around us has gone years without being invited to the table?</div>'
  '<aside class=notes><b>~minute 43.</b> These are already drafted in the HTML comments on week2.md &mdash; this promotes them to the screen.</aside></section>')

# ---------- 11 TEASER ----------
A('<section class="slide"><div class="eyebrow quiet">That fall they asked him to write down what they stood for</div>'
  '<p class=bigquote><span class=q>&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ&hellip;&rdquo;</span></p>'
  '<div class="sub frag">Next week: <b>the Declaration and Address</b> &mdash; the document they asked him to write, and the sentence it opens with.</div>'
  '<aside class=notes>Keep the handoff short. Optional sting, if you want it: <b>the presbytery formally deposed him on 18 April 1810</b> &mdash; seven months after that document was published.</aside></section>')

A('<section class="slide siteslide"><div class=eyebrow>Online</div><h2>stone-campbell.micahredding.com</h2>'
  '<div class=sub>Timeline &middot; Exhibits &middot; People</div><aside class=notes>Standing furniture.</aside></section>')
