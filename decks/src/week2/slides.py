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
W1_SITESLIDE = open(__file__.rsplit('/',1)[0]+'/w1_siteslide.html').read()

# ---------- 1 THE CAVALRY (cold open) ----------
A('<section class="slide"><aside class=notes>Black. No title, no date.<br>&rarr; Put us inside a church service in Ireland, summer 1798, before anyone knows whose church it is.</aside></section>')

A('<section class="slide"><div class=eyebrow>Ireland &middot; summer 1798</div>'
  '<h2>A troop of cavalry surrounded the church.</h2>'
  '<aside class=notes>Probably Ahorey, near Armagh. Welsh horse from Newry, feared for reprisals after the failed rising (the United Irishmen &mdash; Presbyterians had joined it). The captain dismounted and walked in alone.<br>&rarr; The captain up the aisle.</aside></section>')

A(Q('&ldquo;Pray, sir!&rdquo;', 'a venerable elder, sitting near Mr. Campbell &middot; Richardson, <i>Memoirs</i> 1:44') +
  '<aside class=notes>An elder tells him to pray. He does not think of it himself.</aside></section>')

A(Q('&ldquo;Thou, O God, art our refuge and strength, a very present help in trouble. Therefore will not we fear, though the earth be removed and though the mountains be carried into the midst of the sea.&rdquo;', '', 'He began in the words of the forty-sixth Psalm') +
  '<aside class=notes>&ldquo;in a deep, unfaltering voice.&rdquo; Read the whole thing.</aside></section>')

A('<section class="slide"><h2>The captain listened to the end, bowed, and rode away with his troop.</h2>'
  '<aside class=notes>Family tradition, via Richardson &mdash; say &ldquo;as the story goes.&rdquo;<br>&rarr; Nothing was taken from him that day.</aside></section>')

A('<section class="slide plateslide tight"><figure class="plate short"><img src="IMG_TCAMPBELL" alt="" style="max-height:62vh"><figcaption>Thomas Campbell, 1763&ndash;1854</figcaption></figure>'
  '<aside class=notes>&rarr; Name him. One sentence.</aside></section>')

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Week 2</div>'
  '<h1>Thomas Campbell&rsquo;s Break</h1><div class=table-line></div>'
  '<div class=sub>Ireland 1798 &mdash; Pennsylvania 1810</div>'
  '<aside class=notes>Say the title once and go. ~40 min; the room takes the court at ~20 and discussion at ~40.</aside></section>')

# ---------- 2 DIVISION AFTER DIVISION ----------
A(C('Division After Division', 'Say the designation once, then peel it, outside in. Under three minutes for the section.'))

A('<section class="slide"><div class=eyebrow>His designation in Ireland</div>'
  '<h2 class=litany>Old Light &middot; Anti-Burgher &middot; Seceder &middot; Presbyterian<br>'
  '<span class=dim>of the Anti-Burgher Synod of Ulster &mdash; under the General Associate Synod in Scotland</span></h2>'
  '<aside class=notes>Every word is a division from other Christians. Say it whole, then take it apart.</aside></section>')

A('<section class="slide"><div class=eyebrow>Old Light &middot; 1806</div>'
  '<h2>Division over whether the <span style="color:var(--gold)">magistrate</span> may enforce religion.</h2>'
  '<aside class=notes>The Anti-Burghers split again the year before he sailed. He sided with the Old Lights by friendship more than conviction (Foster).</aside></section>')

A('<section class="slide"><div class=eyebrow>Anti-Burgher &middot; 1747</div>'
  '<h2>Division over an <span style="color:var(--gold)">oath</span>.</h2>'
  '<div class=sub>After it, Burghers and Anti-Burghers could no longer take communion together.</div>'
  '<aside class=notes>Whether a Seceder could swear to &ldquo;the true religion presently professed within this realm.&rdquo; Burghers: it only means not Catholic. Anti-Burghers: it blesses the church we left. Within two years, mutual excommunication &mdash; &ldquo;mutual forbidding of intermingling.&rdquo; This is the rule Conemaugh breaks.</aside></section>')

A('<section class="slide"><div class=eyebrow>Seceder &middot; 1733</div>'
  '<h2>Division over <span style="color:var(--gold)">who appoints the minister</span>.</h2>'
  '<div class=sub>They walked out of the Church of Scotland.</div>'
  '<aside class=notes>Lay patrons placing ministers over congregations that had not called them. His tradition began as a protest against imposed authority.</aside></section>')

A('<section class="slide hard"><h2>The oath applied in three Scottish cities. <span style="color:var(--gold)">It had never been required in Ireland.</span></h2>'
  '<aside class=notes>Glasgow, Edinburgh, Perth. His congregation was divided over an oath none of them would ever be asked to take.</aside></section>')

A('<section class="slide"><div class=eyebrow>1798</div>'
  '<h2>He helped found a missionary society open to every denomination.</h2>'
  '<div class="sub frag">His synod voted it inconsistent with the Secession Testimony. He gave it up.</div>'
  '<aside class=notes>Evangelical Society of Ulster &mdash; &ldquo;regardless of their denomination.&rdquo; Synod of Ulster, Aug 1799: the vote came at the same meeting that seated him. Three elders asked whether he would submit; he agreed to &ldquo;try to see eye to eye.&rdquo;<br>&rarr; The one that could make him yield was never the one with the horses.</aside></section>')

A('<section class="slide"><div class=eyebrow>1804</div>'
  '<h2>He proposed reuniting Burghers and Anti-Burghers in Ireland.</h2>'
  '<div class="sub frag">Glasgow &ldquo;allowed him to argue his case but <b>refused to allow the proposition to come to a vote</b>.&rdquo;</div>'
  '<aside class=notes>The Irish synod received it favourably; the General Associate Synod in Scotland would not let it be decided (Foster). Twice he tried; twice a court above him closed it.</aside></section>')

# ---------- 3 SEA VOYAGE → COMMUNION AT CONEMAUGH ----------
A('<section class="slide bleed sect"><div class=bg><div class="bgimg shipbg"></div></div>'
  '<div class=credit>Robert Salmon, <i>British Merchantman in the River Mersey off Liverpool</i>, 1809<br>A ship of the kind, not the <i>Brutus</i></div>'
  '<h2>Sea Voyage</h2><div class=table-line></div>'
  '<aside class=notes>Card.</aside></section>')

A('<section class="slide"><div class=eyebrow>April 1807 &middot; Londonderry</div>'
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

# ---------- 4 THE TRIAL ----------
A(C('The Trial', 'Five minutes belong to the room.'))

A('<section class="slide room"><h2>You are the court.</h2>'
  '<div class=sub>Seven charges. Then: guilty, or not guilty?</div>'
  '<aside class=notes>~minute 20. Hand it over. Co-teacher reads the charges.</aside></section>')

A('<section class="slide"><h2>The Libel <span class=dim>&middot; January 1808</span></h2>'
  '<div class=days>'
  '<div class="d frag"><span class=dn>1</span><span>that appropriating Christ as one&rsquo;s own Savior does not belong to the essence of saving faith</span></div>'
  '<div class="d frag"><span class=dn>2</span><span>that a church has no divine warrant for holding Confessions of Faith as terms of communion</span></div>'
  '<div class="d frag"><span class=dn>3</span><span>that ruling elders may pray and exhort publicly in vacant congregations</span></div>'
  '<div class="d frag"><span class=dn>4</span><span>that our people may hear ministers in stated opposition to our testimony</span></div>'
  '<div class="d frag"><span class=dn>5</span><span>that Christ was not subject to the precept of the law, as well as its penalty, for his people</span></div>'
  '<div class="d frag"><span class=dn>6</span><span>that a man may live without sin in this life</span></div>'
  '<div class="d frag"><span class=dn>7</span><span>that he preached in another minister&rsquo;s bounds without appointment</span></div>'
  '</div>'
  '<aside class=notes>Hanna, ch. II, from the Chartiers minutes. Read them plain. <b>Then take the vote.</b></aside></section>')

A('<section class="slide hard"><h2>The Verdict <span class=dim>&middot; February 1808</span></h2>'
  '<div class=days>'
  '<div class="d"><span class=dn>1</span><span>that appropriating Christ as one&rsquo;s own Savior does not belong to the essence of saving faith</span><span class="verdict frag v-red" data-o=1>guilty</span></div>'
  '<div class="d"><span class=dn>2</span><span>that a church has no divine warrant for holding Confessions of Faith as terms of communion</span><span class="verdict frag v-red" data-o=1>guilty</span></div>'
  '<div class="d"><span class=dn>3</span><span>that ruling elders may pray and exhort publicly in vacant congregations</span><span class="verdict frag v-red" data-o=1>guilty</span></div>'
  '<div class="d"><span class=dn>4</span><span>that our people may hear ministers in stated opposition to our testimony</span><span class="verdict frag v-red" data-o=1>guilty</span></div>'
  '<div class="d"><span class=dn>7</span><span>that he preached in another minister&rsquo;s bounds without appointment</span><span class="verdict frag v-red" data-o=1>guilty</span></div>'
  '</div>'
  '<aside class=notes>Minutes, 12 Feb 1808: 1 and 2 &ldquo;clearly proved&rdquo;; 3, 4 and 7 &ldquo;acknowledged&hellip; and still adhered to by him.&rdquo; Charges 5 and 6 fell away: his answers were accepted (5 &ldquo;not sufficiently proved&rdquo;; 6 approved except &ldquo;or&rdquo; for &ldquo;and&rdquo;). Click through the five verdicts.</aside></section>')

A(Q('&ldquo;It is, therefore, because I have <b>no confidence, either in my own infallibility or in that of others</b>, that I absolutely refuse, as inadmissible and schismatic, the introduction of human opinions and human inventions into the faith and worship of the Church.&rdquo;', 'Richardson, <i>Memoirs</i> 1:227', 'May 1808 &middot; his appeal, read standing before the Synod') +
  '<aside class=notes>He opened by asking them to &ldquo;pause a moment.&rdquo;</aside></section>')

A(Q('&ldquo;For what error or immorality ought I to be rejected, except it be that I refuse to acknowledge as obligatory upon myself, or to impose upon others, anything as of Divine obligation for which I cannot produce a <b>&lsquo;Thus saith the Lord?&rsquo;</b>&rdquo;', 'Richardson, <i>Memoirs</i> 1:227') +
  '<aside class=notes>A separate sentence, two pages on in the appeal.</aside></section>')

A(Q('&ldquo;It is erroneous&hellip; to assert that a church has <b>no divine warrant for holding Confessions of Faith as terms of communion</b>.&rdquo;', '', '<span style="color:var(--gold)">Communion</span> &middot; Article 2', 'slide hard') +
  '<aside class=notes>The question of the class. &ldquo;But you, the Rev&rsquo;d Thomas Campbell, taught this error at Conemaugh and Buffaloe.&rdquo;<br>&rarr; Who may come to the table, and on whose terms.</aside></section>')

A(Q('&ldquo;It is erroneous&hellip; to assert that it is <b>the duty of ruling elders to pray and exhort publickly</b> in vacant congregations.&rdquo;', '', '<span style="color:var(--gold)">Priesthood</span> &middot; Article 3', 'slide hard') +
  '<aside class=notes>Laymen leading worship where there is no minister. The first person to decide what happened in a room this hour was an elder: &ldquo;Pray, sir.&rdquo;</aside></section>')

A(Q('&ldquo;It is erroneous&hellip; to assert that it is warrantable for the people of our communion to <b>hear ministers that are in a stated opposition to our testimony</b>.&rdquo;', '', '<span style="color:var(--gold)">Freedom of Conscience</span> &middot; Article 4', 'slide hard') +
  '<aside class=notes>&ldquo;Occasional hearing.&rdquo; Hold it: his son will be doing this every week in Glasgow.</aside></section>')

A(Q('&ldquo;he was accordingly <b>rebuked and admonished by the Mod&rsquo;r</b>&rdquo;', 'Minutes of the Associate Synod, May 1808', 'The Synod&rsquo;s answer', 'slide hard',
    '<div class=sub>He submitted &mdash; as &ldquo;no more&hellip; than an act of deference to the judgment of the court.&rdquo;</div>') +
  '<aside class=notes>Presbytery&rsquo;s judgment set aside for &ldquo;informalities&rdquo;; his answers found &ldquo;so evasive and unsatisfactory, and highly equivocal&hellip; sufficient grounds to infer censure.&rdquo; Rebuked to his face before the assembled Synod.</aside></section>')

# ---------- 5 THE BREAK ----------
A(C('The Break', 'Accuracy: the break is September 1808, three weeks before his family sailed.'))

A(Q('&ldquo;It is with <b>sincere reluctance</b>&hellip; that I find myself in duty bound to refuse submission to their decision as unjust and partial&hellip; And I hereby do <b>decline all ministerial connection with, or subjection to, the Associate Synod of North America</b>.&rdquo;', 'Thomas Campbell, 13&ndash;14 September 1808 &middot; Chartiers Presbytery, Burgettstown', 'September 1808') +
  '<aside class=notes>He had offered this letter in May and withdrawn it. In September he sent it again. Printed by Alexander, 1861.</aside></section>')

# ---------- 6 THE GROVE ----------
A(C('The Grove', ''))

A('<section class="slide breath"><h1 style="font-size:clamp(28px,5.4vmin,64px);line-height:1.25">&ldquo;And then Campbell discovered that this meant very little.&rdquo;</h1>'
  '<aside class=notes>Your sentence. Black screen; give it a breath.</aside></section>')

A(Q('&ldquo;Sometimes the deep shade of a <b>maple grove</b> sheltered the assembly from the summer sun. Generally, however, the houses of his old Irish neighbors&hellip; were the places where he had his appointments for preaching, and where he discoursed weekly to <b>all who chose to assemble</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:231') +
  '<aside class=notes>No pulpit, no salary, no standing &mdash; and no interruption.<br>&rarr; An association, then a church, then a movement.</aside></section>')

A(Q('&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809', 'That fall they asked him to write down what they stood for') +
  '<aside class=notes>Close his half of the hour on his own sentence. It returns at the end.</aside></section>')

# ---------- 7 ALEXANDER AND THE SHIPWRECK ----------
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

# ---------- 8 FAMILY REUNION ----------
A(C('Family Reunion', ''))

A('<section class="slide"><div class=eyebrow>19 October 1809 &middot; the road into Washington, Pennsylvania</div>'
  '<h2>He rode out to meet them.</h2>'
  '<div class=sub>Two and a half years.</div>'
  '<aside class=notes>Riding back together, Thomas told his son what had happened.</aside></section>')

A(Q('&ldquo;&hellip;had they possessed the power, he would have suffered martyrdom at their hands, or, as he expressed it, that <b>&lsquo;nothing but the law of the land had kept his head upon his shoulders.&rsquo;</b>&rdquo;', 'Richardson, <i>Memoirs</i> 1:219&ndash;220', '', 'slide hard') +
  '<aside class=notes>Reported speech &mdash; what his son remembered him saying. Keep Richardson&rsquo;s qualifier.</aside></section>')

A(Q('&ldquo;Alexander could not but feel indignant at this recital&hellip; <b>He was greatly surprised, however, when informed by his father that the latter had actually dissolved his connection with the Seceders.</b>&rdquo;', 'Richardson, <i>Memoirs</i>') +
  '<aside class=notes>He learned it on the road. Thomas did not know what his son had done in Glasgow.<br>&rarr; The father invited people who had no token; the son held a valid one and would not use it. Neither knew.</aside></section>')

# ---------- 9 CLOSE ----------
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

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 1 of 3</div>'
  '<h2>Non-creedalism is <span style="color:var(--gold)">a protective move.</span></h2>'
  '<aside class=notes>No human formulation as a test of fellowship, because no one&rsquo;s reading is infallible and the simplest believer must be able to confess Christ and belong. His words: <i>no confidence, either in my own infallibility or in that of others.</i></aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 2 of 3</div>'
  '<h2>Why a table was worth all this.</h2>'
  '<aside class=notes>&rarr; Yours. The spine&rsquo;s step 3: Week 1 made the table the age to come arriving early; here someone put a gate in front of it. Unwritten on purpose.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 3 of 3</div>'
  '<h2>It cost him everything they could reach &mdash; <span style="color:var(--gold)">and he did not want to leave.</span></h2>'
  '<aside class=notes>Two years, three courts, his income and standing, a rebuke to his face. He appealed, submitted, deferred. The break was the last thing he tried.</aside></section>')

A('<section class="slide room"><div class=eyebrow>&#9670; for discussion</div>'
  '<h2>What is beautiful here? What do we carry forward?</h2>'
  '<div class="sub frag">What &ldquo;testimonies&rdquo; &mdash; written or unwritten &mdash; do we treat as terms of fellowship today?</div>'
  '<div class="sub frag">Who around us has gone years without being invited to the table?</div>'
  '<aside class=notes>~minute 40.</aside></section>')

A(W1_SITESLIDE)

