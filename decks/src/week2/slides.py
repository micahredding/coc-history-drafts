# -*- coding: utf-8 -*-
# Week 2 deck content — minimal cut, 2026-09-18. One idea per slide. S = list of slide html.
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
def C(name, note):   # chapter card: the name only
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (name, note))
def Q(quote, cite='', eyebrow='', cls='slide', sub=''):   # a quotation alone
    e = '<div class=eyebrow>%s</div>' % eyebrow if eyebrow else ''
    c = '<div class=cite>%s</div>' % cite if cite else ''
    return '<section class="%s">%s<p class=bigquote><span class=q>%s</span></p>%s%s' % (cls, e, quote, sub, c)

S = []
A = S.append
_D = __file__.rsplit('/',1)[0]
W1_SITESLIDE = open(_D+'/w1_siteslide.html').read()
RECAP_VT = open(_D+'/recap_vt.html').read()
RECAP_VO = open(_D+'/recap_vo.html').read()

# ---------- 1 THE CAVALRY (cold open) ----------
# ---------- 0 RECAP — the class, then last week ----------
# ---------- 0 RECAP ----------
A('<section class="slide"><div class="eyebrow quiet">Otter Creek Church of Christ &nbsp;&middot;&nbsp; Fall 2026</div>'
  '<h1>Our Wild<br>Democracy</h1>'
  '<p class=sub>The Story, Promise, and Future<br>of the Churches of Christ</p>'
  '<aside class=notes>Recap, five minutes: the class, then last week. Same slides as Week 0 where possible.</aside></section>')

A('<section class="slide"><div class=eyebrow>How each week works</div>'
  '<div class=shape><span class=step>Story</span><span class=sep>&rarr;</span><span class=step>Idea</span><span class=sep>&rarr;</span><span class=step>Future</span></div>'
  '<aside class=notes>One of us tells a story from our history. Another cross-examines it. Then the questions are yours.</aside></section>')

A('<section class="slide"><p class=bigquote style="font-size:clamp(27px,5.15vmin,60px)"><span class=q>What is beautiful here?<br>What do we carry forward?</span></p>'
  '<aside class=notes>The class question. It closes every week.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">A movement with more than one name</div>'
  '<div class=litany><div class=frag>The Restoration Movement</div><div class=frag>The Stone&ndash;Campbell Movement</div><div class=frag>The Stone&ndash;Campbell Restoration Movement</div></div>'
  '<aside class=notes>Week 0&rsquo;s slide. Three names for one movement; we use them interchangeably.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">Where the movement lives today</div>'
  '<div class=selfname><span class=big>Churches of Christ</span><span class=gl>that&rsquo;s us</span></div>'
  '<div class=selfname><span class=big>Christian Churches</span><span class=gl>the independent congregations</span></div>'
  '<div class=selfname><span class=big>Disciples of Christ</span><span class=gl>the organized denomination</span></div>'
  '<aside class=notes>One movement, three families. This class is the family story, told from our branch.</aside></section>')

A(RECAP_VO)

A(C('Last week &middot; Cane Ridge, 1801', 'Four beats, one slide each.'))

A('<section class="slide"><h2>Tens of thousands gathered.</h2>'
  '<div class=sub>One man counted 12,000. Military men on the ground guessed twenty to thirty thousand.</div>'
  '<aside class=notes>Patterson, counting, September 1801; the whole state held 220,955 people.</aside></section>')

A('<section class="slide"><div class=eyebrow>And they were not people of one church</div>'
  '<div class=litany><div class="no frag">Presbyterians. Methodists. <b>Baptists.</b></div>'
  '<div class="no frag">Folks both <b>black and white</b>.</div>'
  '<div class="no frag">Preachers who were formally <b>at odds</b> &mdash;</div>'
  '<div class="no frag">whose churches did not, as a rule,<br><b>commune at one another&rsquo;s tables.</b></div>'
  '<div class="coda frag">And here they were.</div></div>'
  '<aside class=notes>The Week 1 slide, verbatim. Seven preachers at once; a Black preacher at the fourth centre.</aside></section>')

A(Q('&ldquo;cordially united&hellip; of one mind and one soul&hellip; all engaged in singing the same songs of praise &mdash; all united in prayer &mdash; all preached the same things.&rdquo;', 'Barton W. Stone, of Cane Ridge, August 1801', 'They experienced a profound unity') +
  '<aside class=notes>Presbyterians, Methodists, Baptists; Black and white; seven preachers at once.</aside></section>')

A(Q('&ldquo;Many, very many fell down, <b>as men slain in battle</b>, and continued for hours together in an apparently breathless and motionless state.&rdquo;', 'Barton W. Stone', 'They witnessed the work of the Spirit') +
  '<aside class=notes>The falling &mdash; the part that made it famous, and made it suspect.</aside></section>')

A('<section class="slide"><div class=eyebrow>And they came together</div><h1>This was a<br><span style="color:var(--gold)">communion service.</span></h1>'
  '<aside class=notes>Methodists at a Presbyterian table. Stone dropped the doctrinal test at the door.</aside></section>')

A(Q('&ldquo;Together, in sweetest, holiest, symbolic communion, <b>they sat down at the one table of the one Lord</b>&hellip; many good people thought assuredly, <b>the millennium had begun to dawn upon the world.</b>&rdquo;', 'William Rogers, of Cane Ridge &middot; who was there', 'A foretaste of the future') +
  '<aside class=notes>The table as the age to come, arriving early. Hold this: today someone puts a gate in front of it.</aside></section>')

A(C('Open Communion', 'Before the story: the thing the story is about.'))

A('<section class="slide"><h2>What is <span style="color:var(--gold)">open communion</span>?</h2>'
  '<aside class=notes>Ask it. Let two or three people answer before the next slide.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">A working definition</div>'
  '<h2>The Lord&rsquo;s Supper offered to every believer present &mdash; with no church test at the door.</h2>'
  '<div class=sub>Its opposite is <i>close communion</i>: only members of that church, in good standing, may partake.</div>'
  '<aside class=notes>General definition, not a technical one. In the Scottish Presbyterian world of 1800 the test was the token; in Baptist churches it was immersion; in most churches it was membership.</aside></section>')

A('<section class="slide room"><h2>Did you know this was <span style="color:var(--gold)">part of our practice</span>?</h2>'
  '<aside class=notes>Hands. Then: Churches of Christ have practised it, and defended it in print, for a very long time.</aside></section>')

A('<section class="slide plateslide tight"><div class=eyebrow>1945</div>'
  '<figure class="plate short"><img src="IMG_BROWNLOW" alt="" style="max-height:56vh"><figcaption>Leroy Brownlow, <i>Why I Am a Member of the Church of Christ</i> &middot; Reason XXIII, &ldquo;Because of its scriptural teaching and observance of the Lord&rsquo;s Supper&rdquo;</figcaption></figure>'
  '<aside class=notes>The standard twentieth-century tract of the Churches of Christ; twenty-five reasons. Reason XXIII, section III: &ldquo;Who shall participate in the communion.&rdquo;</aside></section>')

A(Q('&ldquo;&hellip;no man or set of men has the right to judge who shall and shall not have the privilege of communion&hellip; The self-examination taught in this verse <b>condemns the doctrine of close communion</b>. Each is to examine himself; not somebody else.&rdquo;', 'Leroy Brownlow, <i>Why I Am a Member of the Church of Christ</i>, 1945, p. 178', 'On 1 Corinthians 11:28') +
  '<aside class=notes>His argument: it is the Lord&rsquo;s table, so the judgment belongs to Christ and to each communicant, not to the church. That is the position Thomas Campbell was tried for in 1808.</aside></section>')

A('<section class="slide"><div class=eyebrow>Three founders</div>'
  '<div class=faces>'
  '<div class=face><img src="IMG_STONE" alt=""><span class=nm>Barton W. Stone</span><span class=rl>Cane Ridge, Kentucky. Last week.</span></div>'
  '<div class=face><img src="IMG_TCAMPBELL" alt=""><span class=nm>Thomas Campbell</span><span class=rl>Ireland, then Pennsylvania. Today.</span></div>'
  '<div class=face><img src="IMG_ACAMPBELL" alt=""><span class=nm>Alexander Campbell</span><span class=rl>His son. Today, and most weeks after.</span></div>'
  '</div>'
  '<div class=facecred>Stone: memorial portrait at the Cane Ridge shrine, a later painting (photo Chris Light, CC BY-SA 4.0). Alexander Campbell at about 65.</div>'
  '<aside class=notes>Stone and the Campbells do not meet until 1824; their movements merge in 1832 (Week 7).</aside></section>')

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Week 2</div>'
  '<h1>Thomas Campbell&rsquo;s Heresy Trial</h1><div class=table-line></div>'
  '<div class=sub>Ireland 1798 &mdash; Pennsylvania 1810</div>'
  '<aside class=notes>Title up while people settle. Then black, and open cold on the cavalry. ~40 min; the room takes the court at ~20 and discussion at ~40.</aside></section>')

A('<section class="slide"><aside class=notes>Black. A breath after the title.</aside></section>')

A('<section class="slide breath"><h2>Ireland <span class=dim>&middot;</span> summer 1798</h2>'
  '<div class=sub>A Presbyterian meeting house near Armagh, during the Sunday service.</div>'
  '<aside class=notes>Probably Ahorey. The failed rising of 1798 (the United Irishmen &mdash; Presbyterians had joined it); reprisals running.<br>&rarr; Put us inside the service before anyone knows whose church it is.</aside></section>')

A('<section class="slide"><h2>A troop of cavalry surrounded the church.</h2>'
  '<aside class=notes>Welsh horse from Newry, feared for reprisals. The captain dismounted and walked in alone.<br>&rarr; The captain up the aisle.</aside></section>')

A(Q('&ldquo;Pray, sir!&rdquo;', 'a venerable elder, sitting near Mr. Campbell &middot; Richardson, <i>Memoirs</i> 1:44') +
  '<aside class=notes>An elder tells him to pray. He does not think of it himself.</aside></section>')

A(Q('&ldquo;Thou, O God, art our refuge and strength, a very present help in trouble. Therefore will not we fear, though the earth be removed and though the mountains be carried into the midst of the sea.&rdquo;', '', 'He began in the words of the forty-sixth Psalm') +
  '<aside class=notes>&ldquo;in a deep, unfaltering voice.&rdquo; Read the whole thing.</aside></section>')

A('<section class="slide"><h2>The captain listened to the end, bowed, and rode away with his troop.</h2>'
  '<aside class=notes>Family tradition, via Richardson &mdash; say &ldquo;as the story goes.&rdquo;<br>&rarr; Nothing was taken from him that day.</aside></section>')

A('<section class="slide plateslide tight"><figure class="plate short"><img src="IMG_TCAMPBELL" alt="" style="max-height:62vh"><figcaption>Thomas Campbell, 1763&ndash;1854</figcaption></figure>'
  '<aside class=notes>&rarr; Name him. One sentence.</aside></section>')

A('<section class="slide"><div class=eyebrow>His designation in Ireland</div>'
  '<div class=litany>'
  '<div class=frag>Old Light</div>'
  '<div class=frag>Anti-Burgher</div>'
  '<div class=frag>Seceder</div>'
  '<div class=frag>Presbyterian</div>'
  '<div class="frag dim">of the Anti-Burgher Synod of Ulster</div>'
  '<div class="frag dim">under the General Associate Synod in Scotland</div>'
  '</div>'
  '<aside class=notes>Every word is a division from other Christians. Build it one line at a time, then take it apart.</aside></section>')

A(C('Division After Division', 'Say the designation once, then peel it, outside in. Under three minutes for the section.'))

A('<section class="slide"><div class=eyebrow>Old Light &middot; 1806</div>'
  '<h2>Division over whether the <span style="color:var(--gold)">magistrate</span> may enforce religion.</h2>'
  '<aside class=notes>The Anti-Burghers split again the year before he sailed. He sided with the Old Lights by friendship more than conviction (Foster).</aside></section>')

A('<section class="slide"><div class=eyebrow>Anti-Burgher &middot; 1747</div>'
  '<h2>Division over an <span style="color:var(--gold)">oath</span>.</h2>'
  '<div class=sub>After it, Burghers and Anti-Burghers could no longer take communion together.</div>'
  '<aside class=notes>Whether a Seceder could swear to &ldquo;the true religion presently professed within this realm.&rdquo; Burghers: it only means not Catholic. Anti-Burghers: it blesses the church we left. Within two years, mutual excommunication &mdash; &ldquo;mutual forbidding of intermingling.&rdquo; The oath applied in three Scottish cities and had never been required in Ireland at all. This is the rule Conemaugh breaks.</aside></section>')

A('<section class="slide"><div class=eyebrow>Seceder &middot; 1733</div>'
  '<h2>Division over <span style="color:var(--gold)">who appoints the minister</span>.</h2>'
  '<div class=sub>They walked out of the Church of Scotland.</div>'
  '<aside class=notes>Lay patrons placing ministers over congregations that had not called them. His tradition began as a protest against imposed authority.</aside></section>')

A(C('Worked for Unity', 'Two tries, two slides.'))

A('<section class="slide"><div class=eyebrow>1798</div>'
  '<h2>He helped found a missionary society open to every denomination.</h2>'
  '<div class="sub frag">His synod voted it inconsistent with the Secession Testimony. He gave it up.</div>'
  '<aside class=notes>Evangelical Society of Ulster &mdash; &ldquo;regardless of their denomination.&rdquo; Synod of Ulster, Aug 1799: the vote came at the same meeting that seated him. Three elders asked whether he would submit; he agreed to &ldquo;try to see eye to eye.&rdquo;<br>&rarr; The one that could make him yield was never the one with the horses.</aside></section>')

A('<section class="slide"><div class=eyebrow>1804</div>'
  '<h2>He proposed reuniting Burghers and Anti-Burghers in Ireland.</h2>'
  '<div class="sub frag">Glasgow &ldquo;allowed him to argue his case but <b>refused to allow the proposition to come to a vote</b>.&rdquo;</div>'
  '<aside class=notes>The Irish synod received it favourably; the General Associate Synod in Scotland would not let it be decided (Foster). Twice he tried; twice a court above him closed it.</aside></section>')

A(C('Unity Failed', 'Card. Then the ship.'))

A('<section class="slide bleed sect"><div class=bg><div class="bgimg shipbg"></div></div>'
  '<div class=credit>Robert Salmon, <i>British Merchantman in the River Mersey off Liverpool</i>, 1809<br>A ship of the kind, not the <i>Brutus</i></div>'
  '<h2>Sea Voyage</h2><div class=table-line></div>'
  '<aside class=notes>Card.</aside></section>')

A('<section class="slide bleed"><div class=bg><div class="bgimg shipbg"></div></div>'
  '<div class=eyebrow>April 1807 &middot; Londonderry</div>'
  '<h2>His doctor prescribed a sea voyage.</h2>'
  '<div class=sub>He left his eighteen-year-old son, <b>Alexander</b>, in charge of the family and the school.</div>'
  '<aside class=notes>Illness from overwork; thirty-five days on the <i>Brutus</i>; Philadelphia in May. Assigned to the Presbytery of Chartiers, western Pennsylvania. Alexander: one clause; he returns in the last two chapters.</aside></section>')

A(C('Communion at Conemaugh', ''))

A('<section class="slide plateslide tight"><div class=eyebrow>August 1807 &middot; seventy miles from home</div>'
  '<figure class="plate wide"><img src="IMG_MAP" alt=""><figcaption>Reading Howell, <i>A Map of the State of Pennsylvania</i>, 1792 &middot; Library of Congress</figcaption></figure>'
  '<aside class=notes>Washington, his home, south-west of Pittsburgh. Conemaugh Township, later Indiana County, the far edge of a four-county circuit. Cannamaugh Church, an Associate congregation founded 1798.</aside></section>')

A('<section class="slide plateslide tokenslide"><div class=eyebrow>The token</div>'
  '<figure class="plate short"><img src="IMG_TOKEN" alt=""><figcaption>A Scottish communion token, 1750</figcaption></figure>'
  '<div class=sub>Examined beforehand. Handed a lead ticket. Surrendered at the table.</div>'
  '<aside class=notes>Same object as Week 1. The fence, in metal.</aside></section>')

A('<section class="slide"><h2>Faithful Presbyterians who had not received communion in years.</h2>'
  '<div class="sub frag">Not for lack of a minister. For lack of a minister <b>of their own sub-sect</b>.</div>'
  '<aside class=notes>Your sentence from the site.</aside></section>')

A(Q('&hellip;that all his pious hearers, &ldquo;who felt so disposed and duly prepared, should, <b>without respect to party differences</b>, enjoy the benefits of the communion season then providentially afforded them.&rdquo;', 'Richardson, <i>Memoirs</i> 1:224', 'He did not fence the table') +
  '<aside class=notes>Wilson&rsquo;s deposition: he &ldquo;would not go over the commands&rdquo; &mdash; to require assent to the terms particularly would be to demand &ldquo;implicit faith.&rdquo;</aside></section>')

A(Q('&ldquo;&hellip;the Lord&rsquo;s Supper, <b>that great ordinance of unity and love</b>.&rdquo;', '<i>Declaration and Address</i>, 1809', 'Two years later, in his own words') +
  '<aside class=notes>1809, not 1807 &mdash; say &ldquo;two years later he put it this way.&rdquo;</aside></section>')

A('<section class="slide"><h2>It was well received.</h2>'
  '<div class="sub frag">The young minister assisting him, <b>William Wilson</b>, reported it to the presbytery.</div>'
  '<aside class=notes>Nobody objected in the room. Wilson took it to his old teacher John Anderson, professor of theology; Anderson refused to keep a preaching appointment with Campbell.</aside></section>')

A(C('The Trial', 'Five minutes belong to the room.'))

A('<section class="slide"><h2>The Libel <span class=dim>&middot; January 1808</span></h2>'
  '<div class=days>'
  '<div class="d"><span class=dn>1</span><span>that appropriating Christ as one&rsquo;s own Savior does not belong to the essence of saving faith</span></div>'
  '<div class="d"><span class=dn>2</span><span>that a church has no divine warrant for holding Confessions of Faith as terms of communion</span></div>'
  '<div class="d"><span class=dn>3</span><span>that ruling elders may pray and exhort publicly in vacant congregations</span></div>'
  '<div class="d"><span class=dn>4</span><span>that our people may hear ministers in stated opposition to our testimony</span></div>'
  '<div class="d"><span class=dn>5</span><span>that Christ was not subject to the precept of the law, as well as its penalty, for his people</span></div>'
  '<div class="d"><span class=dn>6</span><span>that a man may live without sin in this life</span></div>'
  '<div class="d"><span class=dn>7</span><span>that he preached in another minister&rsquo;s bounds without appointment</span></div>'
  '</div>'
  '<aside class=notes>Hanna, ch. II, from the Chartiers minutes. Read them plain.</aside></section>')

A('<section class="slide room"><h2><span style="color:var(--gold)">YOU</span> are the court.</h2>'
  '<div class=sub>Guilty, or not guilty?</div>'
  '<aside class=notes>~minute 20. Hand it over. Co-teacher reads the charges.</aside></section>')

A('<section class="slide hard"><h2>The Verdict <span class=dim>&middot; February 1808</span></h2>'
  '<div class="days verdictlist">'
  '<div class="d"><span class=dn>1</span><span>that appropriating Christ as one&rsquo;s own Savior does not belong to the essence of saving faith</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>2</span><span>that a church has no divine warrant for holding Confessions of Faith as terms of communion</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>3</span><span>that ruling elders may pray and exhort publicly in vacant congregations</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>4</span><span>that our people may hear ministers in stated opposition to our testimony</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>7</span><span>that he preached in another minister&rsquo;s bounds without appointment</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '</div>'
  '<aside class=notes>Minutes, 12 Feb 1808: 1 and 2 &ldquo;clearly proved&rdquo;; 3, 4 and 7 &ldquo;acknowledged&hellip; and still adhered to by him.&rdquo; Charges 5 and 6 fell away: his answers were accepted (5 &ldquo;not sufficiently proved&rdquo;; 6 approved except &ldquo;or&rdquo; for &ldquo;and&rdquo;). Click through the five verdicts.</aside></section>')

A(C('The Appeal', 'May 1808. He appealed the presbytery&rsquo;s verdict to the Associate Synod at Philadelphia and read his appeal aloud before it.'))

A(Q('&ldquo;For what error or immorality ought I to be rejected, except it be that I refuse to acknowledge as obligatory upon myself, or to impose upon others, anything as of Divine obligation for which I cannot produce a <b>&lsquo;Thus saith the Lord?&rsquo;</b>&rdquo;', 'Richardson, <i>Memoirs</i> 1:227', 'May 1808 &middot; his appeal to the Synod at Philadelphia') +
  '<aside class=notes>A separate sentence, two pages on in the appeal.</aside></section>')

A(Q('&ldquo;It is, therefore, because I have <b>no confidence, either in my own infallibility or in that of others</b>, that I absolutely refuse, as inadmissible and schismatic, the introduction of human opinions and human inventions into the faith and worship of the Church.&rdquo;', 'Richardson, <i>Memoirs</i> 1:227', 'May 1808 &middot; his appeal to the Synod at Philadelphia') +
  '<aside class=notes>Richardson: &ldquo;he addressed an earnest appeal to the Synod when his case came up.&rdquo; The Synod minutes: his reasons of protest and appeal were read, and &ldquo;parties were heard.&rdquo; He opened by asking them to &ldquo;pause a moment.&rdquo;</aside></section>')

A(C('The Judgment', 'The Synod set the presbytery&rsquo;s judgment aside for &ldquo;informalities&rdquo; &mdash; then found his answers on the same articles &ldquo;so evasive and unsatisfactory, and highly equivocal&hellip; sufficient grounds to infer censure.&rdquo;'))

A(Q('&ldquo;It is erroneous&hellip; to assert that a church has <b>no divine warrant for holding Confessions of Faith as terms of communion</b>.&rdquo;', '', '<span style="color:var(--gold)">Communion</span> &middot; Article 2', 'slide hard') +
  '<aside class=notes>The question of the class. &ldquo;But you, the Rev&rsquo;d Thomas Campbell, taught this error at Conemaugh and Buffaloe.&rdquo;<br>&rarr; Who may come to the table, and on whose terms.</aside></section>')

A(Q('&ldquo;It is erroneous&hellip; to assert that it is <b>the duty of ruling elders to pray and exhort publickly</b> in vacant congregations.&rdquo;', '', '<span style="color:var(--gold)">Priesthood</span> &middot; Article 3', 'slide hard') +
  '<aside class=notes>Laymen leading worship where there is no minister. The first person to decide what happened in a room this hour was an elder: &ldquo;Pray, sir.&rdquo;</aside></section>')

A(Q('&ldquo;It is erroneous&hellip; to assert that it is warrantable for the people of our communion to <b>hear ministers that are in a stated opposition to our testimony</b>.&rdquo;', '', '<span style="color:var(--gold)">Freedom of Conscience</span> &middot; Article 4', 'slide hard') +
  '<aside class=notes>&ldquo;Occasional hearing.&rdquo; Hold it: his son will be doing this every week in Glasgow.</aside></section>')

A(Q('&ldquo;he was accordingly <b>rebuked and admonished by the Mod&rsquo;r</b>&rdquo;', 'Minutes of the Associate Synod, May 1808', 'The Synod&rsquo;s answer', 'slide hard',
    '<div class=sub>He submitted &mdash; as &ldquo;no more&hellip; than an act of deference to the judgment of the court.&rdquo;</div>') +
  '<aside class=notes>Presbytery&rsquo;s judgment set aside for &ldquo;informalities&rdquo;; his answers found &ldquo;so evasive and unsatisfactory, and highly equivocal&hellip; sufficient grounds to infer censure.&rdquo; Rebuked to his face before the assembled Synod.</aside></section>')

A(C('The Break', 'Accuracy: the break is September 1808, three weeks before his family sailed.'))

A(Q('&ldquo;It is with <b>sincere reluctance</b>&hellip; that I find myself in duty bound to refuse submission to their decision as unjust and partial&hellip; And I hereby do <b>decline all ministerial connection with, or subjection to, the Associate Synod of North America</b>.&rdquo;', 'Thomas Campbell, 13&ndash;14 September 1808 &middot; Chartiers Presbytery, Burgettstown', 'September 1808') +
  '<aside class=notes>He had offered this letter in May and withdrawn it. In September he sent it again. Printed by Alexander, 1861.</aside></section>')

A(Q('&ldquo;&hellip;had they possessed the power, he would have suffered martyrdom at their hands, or, as he expressed it, that <b>&lsquo;nothing but the law of the land had kept his head upon his shoulders.&rsquo;</b>&rdquo;', 'Richardson, <i>Memoirs</i> 1:219&ndash;220', '', 'slide hard') +
  '<aside class=notes>His own summary of the two years &mdash; said to Alexander on the road a year later, as Richardson reports it. Keep the qualifier: <i>had they possessed the power</i>.</aside></section>')

A(C('The Grove', ''))

A('<section class="slide breath"><h1 style="font-size:clamp(28px,5.4vmin,64px);line-height:1.25">And then Campbell discovered that this meant very little.</h1>'
  '<aside class=notes>Your sentence. Black screen; give it a breath.</aside></section>')

A(Q('&ldquo;Sometimes the deep shade of a <b>maple grove</b> sheltered the assembly from the summer sun. Generally, however, the houses of his old Irish neighbors&hellip; were the places where he had his appointments for preaching, and where he discoursed weekly to <b>all who chose to assemble</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:231') +
  '<aside class=notes>No pulpit, no salary, no standing &mdash; and no interruption.<br>&rarr; An association, then a church, then a movement.</aside></section>')

A(C('What did they stand for?', ''))

A(Q('&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809', 'That fall they asked him to write down what they stood for') +
  '<aside class=notes>Close his half of the hour on his own sentence. It returns at the end.</aside></section>')

A(C('Alexander and the Shipwreck', 'The son&rsquo;s story, while the father&rsquo;s is still open. He does not know what has happened in Pennsylvania.'))

A('<section class="slide bleed"><div class=bg><div class="bgimg wreckbg"></div></div>'
  '<div class=credit>Philippe Jacques de Loutherbourg, <i>A Shipwreck off a Rocky Coast</i><br>Not the <i>Hibernia</i>, and not Islay</div>'
  '<h2>October 1808. His family sailed &mdash; and were wrecked off Islay.</h2>'
  '<div class=sub>Everyone survived. They were stranded in Scotland for ten months.</div>'
  '<aside class=notes>1 October 1808, three weeks after the break. Jane and seven children; Alexander twenty. Loch Indaal. Alexander spent days drying his father&rsquo;s books.</aside></section>')

A('<section class="slide"><div class=eyebrow>Glasgow &middot; 1808&ndash;09</div>'
  '<h2>Every week, Alexander went to hear ministers outside his church.</h2>'
  '<div class="sub frag">Richardson&rsquo;s word for it: <b>&ldquo;occasional hearing.&rdquo;</b> Article 4.</div>'
  '<aside class=notes>Seceder church in the morning; Greville Ewing&rsquo;s Tabernacle in the evening &mdash; fifteen hundred people in a former circus &mdash; and others. His father is on trial in Pennsylvania partly for saying this is permissible.</aside></section>')

A(Q('&ldquo;&hellip;an effect which was, doubtless, facilitated by the fact that <b>his revered father, to whose religious sentiments he was accustomed to pay the utmost deference, was now separated from him by the wide Atlantic</b>.&rdquo;', 'Richardson, on why Alexander changed') +
  '<aside class=notes>The son drifts partly because the father is not there &mdash; while the father, unknown to him, is breaking too.</aside></section>')

A('<section class="slide"><div class=eyebrow>The communion season</div>'
  '<h2>He was examined, and given the token.</h2>'
  '<aside class=notes>No letter from Ahorey, so the session examined him. Eight hundred communicants, eight or nine tables. He waited for the last one, &ldquo;in hopes of being able to overcome his scruples.&rdquo;</aside></section>')

A(Q('&ldquo;&hellip;conscientious misgivings as to the propriety of <b>sanctioning any longer, by participation, a religious system which he disapproved</b>.&rdquo;', 'Richardson, <i>Memoirs</i>', 'Why he could not') +
  '<aside class=notes>Participation is sanction. The father: you may not make this table a test. The son: I will not let this table make me a witness.</aside></section>')

A(Q('&ldquo;&hellip;the ring of the token, falling upon the plate, announced the instant at which he renounced Presbyterianism for ever &mdash; <b>the leaden voucher becoming thus a token not of communion but of separation</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:190', '', 'slide hard') +
  '<aside class=notes>He dropped the token and passed the bread and wine. Told no one. Collected his certificate of good standing on the way out.</aside></section>')

A(C('Family Reunion', ''))

A('<section class="slide"><div class=eyebrow>19 October 1809 &middot; the road into Washington, Pennsylvania</div>'
  '<h2>He rode out to meet them.</h2>'
  '<div class=sub>Two and a half years.</div>'
  '<aside class=notes>Riding back together, Thomas told his son what had happened.</aside></section>')

A(Q('&ldquo;Alexander could not but feel indignant at this recital&hellip; <b>He was greatly surprised, however, when informed by his father that the latter had actually dissolved his connection with the Seceders.</b>&rdquo;', 'Richardson, <i>Memoirs</i>') +
  '<aside class=notes>He learned it on the road. Thomas did not know what his son had done in Glasgow.<br>&rarr; The father invited people who had no token; the son held a valid one and would not use it. Neither knew.</aside></section>')

A(Q('&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809', 'That fall they asked him to write down what they stood for', 'slide',
    '<div class="sub frag">Next week: <b>the Declaration and Address</b>.</div>') +
  '<aside class=notes>Optional sting: the presbytery formally deposed him on 18 April 1810 &mdash; seven months after this was published.</aside></section>')

A('<section class="slide ideasmap"><div class=eyebrow>What this week touched</div>'
  '<div class=wmap><div class="r ms-christ"><span class="th key">CHRIST ALONE</span></div>'
  '<div class="r ms-pri"><span class="th key">UNITY</span><span class="th key">PRIESTHOOD</span><span class="th on">FUTURE</span></div>'
  '<div class="r ms-sec"><span class="th on">HOMECOMING</span><span class="th on">SELF-SACRIFICE</span><span class="th key">FREEDOM OF CONSCIENCE</span><span class=th>SCIENCE &amp; REASON</span><span class="th on">MINIMALISM</span></div>'
  '<div class="r ms-pra"><span class="th key">the Table</span><span class=th>Baptism</span><span class="th on">Scripture</span><span class=th>Singing</span><span class="th on">Congregation</span></div></div>'
  '<div class=small>Bright: the spine of this week. Dim: touched in passing. Unlit: still ahead of us.</div>'
  '<aside class=notes>Same board as Week 1. New light: Priesthood, Freedom of Conscience, Christ Alone.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 1 of 4</div>'
  '<h2>The unity movement <span style="color:var(--gold)">did not begin in America.</span></h2>'
  '<aside class=notes>Thomas Campbell was already working for unity in a divided Ireland, and took that work with him across the Atlantic.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 2 of 4</div>'
  '<h2>They divided over <span style="color:var(--gold)">hospitality, not doctrine.</span></h2>'
  '<aside class=notes>He did not set out to found anything or to dispute a doctrine; he extended the Supper to believers the system had orphaned, holding the fences to be the thing without divine warrant.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 3 of 4</div>'
  '<h2>Non-creedalism is <span style="color:var(--gold)">a protective move.</span></h2>'
  '<aside class=notes>No human formulation as a test of fellowship &mdash; because no one&rsquo;s interpretation is infallible, and the simplest believer must be able to confess Christ and belong.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 4 of 4</div>'
  '<h2>They stood for <span style="color:var(--gold)">the universal church.</span></h2>'
  '<aside class=notes>That autumn the people following him from farmhouse to grove asked him to write down what they stood for, and the first sentence was that the church of Christ upon earth is essentially, intentionally, and constitutionally one.</aside></section>')

A('<section class="slide room"><div class=eyebrow>&#9670; for discussion</div>'
  '<h2>What is beautiful here? What do we carry forward?</h2>'
  '<div class="sub frag">What &ldquo;testimonies&rdquo; &mdash; written or unwritten &mdash; do we treat as terms of fellowship today?</div>'
  '<div class="sub frag">Who around us has gone years without being invited to the table?</div>'
  '<aside class=notes>~minute 40.</aside></section>')

A(W1_SITESLIDE)








A(C('Addendum', 'Reference material; not part of the telling.'))

A('<section class="slide ideasmap"><div class=eyebrow>The ideas</div>'
  '<div class="wmap all"><div class="r ms-christ"><span class="th key">CHRIST ALONE</span></div>'
  '<div class="r ms-pri"><span class=th>UNITY</span><span class=th>PRIESTHOOD</span><span class=th>FUTURE</span></div>'
  '<div class="r ms-sec"><span class=th>HOMECOMING</span><span class=th>SELF-SACRIFICE</span><span class=th>FREEDOM OF CONSCIENCE</span><span class=th>SCIENCE &amp; REASON</span><span class=th>MINIMALISM</span></div>'
  '<div class="r ms-pra"><span class=th>the Table</span><span class=th>Baptism</span><span class=th>Scripture</span><span class=th>Singing</span><span class=th>Congregation</span></div></div>'
  '<aside class=notes>The board from Week 0. Christ alone at the centre; three primary ideas; five secondary; five practices.</aside></section>')

A(RECAP_VT)
