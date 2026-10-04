# -*- coding: utf-8 -*-
import re
# Week 2 deck content — minimal cut, 2026-09-18. One idea per slide. S = list of slide html.
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
_D = __file__.rsplit('/',1)[0]
W1_SITESLIDE = open(_D+'/w1_siteslide.html').read()
RECAP_VT = open(_D+'/recap_vt.html').read()
RECAP_VO = open(_D+'/recap_vo.html').read()

# ---------- 1 THE CAVALRY (cold open) ----------
# ---------- 0 RECAP — the class, then last week ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
# ---------- 0 RECAP ----------
A('<section class="slide" style="padding-bottom:10vmin"><div class="eyebrow quiet" style="font-size:clamp(16px,3vmin,36px)">Otter Creek &middot; Fall 2026</div>'
  '<h1 style="font-size:min(19vmin,11.5vw);line-height:1.02;max-width:none">Our Wild<br>Democracy</h1>'
  '<p class=sub style="font-size:min(5vmin,3.6vw);max-width:none;margin-top:2vmin">The Story, Promise, and Future<br>of the Churches of Christ</p>'
  '<aside class=notes>Recap, about four minutes: the class title, the movement, then last week at Cane Ridge.</aside></section>')

A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2>We are Christians only&hellip;</h2>'
  '<div class="sub frag">&hellip;but not the only Christians.</div></section>')

A('<section class="slide treeslide"><div class="eyebrow quiet">One movement</div>'
  '<svg class=tree viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><clipPath id="c250"><circle cx="250" cy="95" r="68"/></clipPath><clipPath id="c500"><circle cx="500" cy="95" r="68"/></clipPath><clipPath id="c750"><circle cx="750" cy="95" r="68"/></clipPath></defs><line x1="60" y1="60" x2="60" y2="540" stroke="#5a4a2e" stroke-width="2"/><polygon points="54,540 66,540 60,556" fill="#5a4a2e"/><text x="60" y="44" text-anchor="middle" font-family="IM Fell English SC","IM Fell English",Georgia,serif font-size="18" letter-spacing="2" fill="#8e8272">1800s</text><text x="60" y="582" text-anchor="middle" font-family="IM Fell English SC","IM Fell English",Georgia,serif font-size="18" letter-spacing="2" fill="#8e8272">today</text><image href="IMG_STONE" x="182" y="27" width="136" height="136" preserveAspectRatio="xMidYMid slice" clip-path="url(#c250)"/><circle cx="250" cy="95" r="68" fill="none" stroke="#c89b3c" stroke-width="2"/><text x="250" y="192" text-anchor="middle" font-family="IM Fell English SC","IM Fell English",Georgia,serif font-size="19" letter-spacing="1.5" fill="#ede4d3">Barton W. Stone</text><text x="250" y="216" text-anchor="middle" font-family=Spectral,Georgia,serif font-style="italic" font-size="17" fill="#8e8272">Kentucky · 1801</text><image href="IMG_TCAMPBELL" x="432" y="27" width="136" height="136" preserveAspectRatio="xMidYMid slice" clip-path="url(#c500)"/><circle cx="500" cy="95" r="68" fill="none" stroke="#c89b3c" stroke-width="2"/><text x="500" y="192" text-anchor="middle" font-family="IM Fell English SC","IM Fell English",Georgia,serif font-size="19" letter-spacing="1.5" fill="#ede4d3">Thomas Campbell</text><text x="500" y="216" text-anchor="middle" font-family=Spectral,Georgia,serif font-style="italic" font-size="17" fill="#8e8272">Pennsylvania · 1809</text><image href="IMG_ACAMPBELL" x="682" y="27" width="136" height="136" preserveAspectRatio="xMidYMid slice" clip-path="url(#c750)"/><circle cx="750" cy="95" r="68" fill="none" stroke="#c89b3c" stroke-width="2"/><text x="750" y="192" text-anchor="middle" font-family="IM Fell English SC","IM Fell English",Georgia,serif font-size="19" letter-spacing="1.5" fill="#ede4d3">Alexander Campbell</text><text x="750" y="216" text-anchor="middle" font-family=Spectral,Georgia,serif font-style="italic" font-size="17" fill="#8e8272">his son</text><path d="M250,226 C250,270 460,268 500,290 M500,226 L500,290 M750,226 C750,270 540,268 500,290" fill="none" stroke="#c89b3c" stroke-width="2.5"/><text x="500" y="345" text-anchor="middle" font-family="IM Fell English",Georgia,serif font-size="46" fill="#c89b3c">The Stone&#8211;Campbell Restoration Movement</text><text x="500" y="376" text-anchor="middle" font-family=Spectral,Georgia,serif font-style="italic" font-size="20" fill="#8e8272">one movement, many congregations &#183; merged 1832</text><path d="M500,392 C500,430 185,430 165,465 M500,392 L500,465 M500,392 C500,430 815,430 835,465" fill="none" stroke="#c89b3c" stroke-width="2.5"/><text x="165" y="500" text-anchor="middle" font-family="IM Fell English",Georgia,serif font-size="34" fill="#c89b3c">Churches of Christ</text><text x="165" y="530" text-anchor="middle" font-family=Spectral,Georgia,serif font-style="italic" font-size="19" fill="#c89b3c">that&#8217;s us</text><text x="500" y="500" text-anchor="middle" font-family="IM Fell English",Georgia,serif font-size="34" fill="#ede4d3">Christian Churches</text><text x="500" y="530" text-anchor="middle" font-family=Spectral,Georgia,serif font-style="italic" font-size="19" fill="#8e8272">the independent congregations</text><text x="835" y="500" text-anchor="middle" font-family="IM Fell English",Georgia,serif font-size="34" fill="#ede4d3">Disciples of Christ</text><text x="835" y="530" text-anchor="middle" font-family=Spectral,Georgia,serif font-style="italic" font-size="19" fill="#8e8272">the organized denomination</text></svg>'
  '<aside class=notes>Three founders, one movement, three families. Stone and the Campbells merge in 1832 (Chapter 7); the three families separate in the twentieth century. We are the branch on the left.</aside></section>')

A('<section class="slide"><div class=eyebrow>Three Instigators</div>'
  '<div class=faces>'
  '<div class=face><img src="IMG_STONE" alt=""><span class=nm>Barton W. Stone</span><span class=rl>Cane Ridge, Kentucky. Last week.</span></div>'
  '<div class=face><img src="IMG_TCAMPBELL" alt=""><span class=nm>Thomas Campbell</span><span class=rl>Ireland, then Pennsylvania. Today.</span></div>'
  '<div class=face><img src="IMG_ACAMPBELL" alt=""><span class=nm>Alexander Campbell</span><span class=rl>His son. Today, and most weeks after.</span></div>'
  '</div>'
  '<div class=facecred>Stone: memorial portrait at the Cane Ridge shrine, a later painting (photo Chris Light, CC BY-SA 4.0). Alexander Campbell at about 65.</div>'
  '<aside class=notes>Name them once. Stone&rsquo;s story was last week; the Campbells are today. They meet in 1824 and their movements merge in 1832 (Chapter 7).</aside></section>')


A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 2</div>'
  '<h1>Thomas Campbell&rsquo;s Heresy Trial</h1><div class=table-line></div>'
  '<div class=sub>Ireland 1798 &mdash; Pennsylvania 1810</div>'
  '<aside class=notes>Title up. Then black, and the cold open. ~40 min for the story; the room takes the court at about minute 20 and discussion at about 40.</aside></section>')

A('<section class="slide"><aside class=notes>Black. A breath after the title.</aside></section>')

A('<section class="slide breath"><h2>Ireland <span class=dim>&middot;</span> summer 1798</h2>'
  '<div class=sub>A Presbyterian meeting house near <b>Richhill, County Armagh</b> &mdash; probably his own at <b>Ahorey</b> &mdash; during the Sunday service.</div>'
  '<aside class=notes>Probably Ahorey, his congregation eight miles from Armagh; he had been its minister since 1798, licensed 1791. Summer 1798 is the failed rising of the United Irishmen &mdash; Presbyterians had joined it in great numbers &mdash; and the reprisals were under way. A Presbyterian meeting house was, to a soldier, a possible rebel meeting.<br>&rarr; Put us inside the service before anyone knows whose church it is.</aside></section>')

A('<section class="slide"><aside class=notes>Black. A breath before the cavalry.</aside></section>')

A('<section class="slide"><h2>A troop of cavalry surrounded the church.</h2>'
  '<aside class=notes>Richardson 1:44: &ldquo;a troop of Welsh horse, notorious for their severities and outrages upon those they conceived to be rebels.&rdquo; Stationed at Newry. The captain, &ldquo;conceiving that in this remote place he had come upon a meeting of rebels, dismounted and in a threatening manner marched into the church.&rdquo; He came in alone.<br>&rarr; The captain up the aisle, &ldquo;casting fierce glances upon all sides.&rdquo;</aside></section>')

A(Q('&ldquo;Pray, sir!&rdquo;', 'a venerable elder, sitting near Mr. Campbell &middot; Richardson, <i>Memoirs</i> 1:44') +
  '<aside class=notes>A venerable elder sitting near him &ldquo;called to him solemnly.&rdquo; Campbell does not think of it; a layman tells the minister what to do.</aside></section>')

A(Q('&ldquo;Thou, O God, art our refuge and strength, a very present help in trouble. Therefore will not we fear, though the earth be removed and though the mountains be carried into the midst of the sea.&rdquo;', '', 'He began in the words of the forty-sixth Psalm') +
  '<aside class=notes>&ldquo;in a deep, unfaltering voice.&rdquo; Read the whole verse; do not summarise it.</aside></section>')

A('<section class="slide"><h2>The captain listened to the end, bowed, and rode away with his troop.</h2>'
  '<aside class=notes>Richardson: &ldquo;No sooner was the first verse uttered than the captain paused, and, apparently impressed, bent his head, listened to the close, then bowed, and retracing his steps, mounted his horse and dashed away with the entire troop.&rdquo; Family tradition, written down seventy years later &mdash; say &ldquo;as the story goes.&rdquo;<br>&rarr; Nothing was taken from him that day.</aside></section>')

A('<section class="slide"><div class=eyebrow>Armagh &middot; the 1790s</div>'
  '<h2>Ireland was tearing itself apart.</h2>'
  '<div class=sub>Orangemen and Defenders by night. The United Irishmen by secret oath. Most of his own people had joined.</div>'
  '<aside class=notes>Richardson 1:41&ndash;42, the fullest account. The <b>Orange society</b> formed in County Armagh in 1795 &ldquo;to drive by threats and nocturnal outrages the entire Catholic peasantry from the country&rdquo;; Catholic <b>Defenders</b> and Protestant <b>Peep-o&rsquo;-Day Boys</b> fought across Ulster; houses were searched for arms by night and robbers used the cover. Then the <b>United Irishmen</b> &mdash; a secret, oath-bound society aiming at an independent republic. Catholics joined for protection from the Orangemen; Presbyterians for parliamentary reform &mdash; and &ldquo;the greater portion of the Presbyterians became connected with this secret organization,&rdquo; its &ldquo;chief moral strength.&rdquo; In the six northern counties they were much of the population. That is his congregation.</aside></section>')

A('<section class="slide">'
  '<h2>Thomas Campbell was asked to preach on Oaths and Secret Societies.</h2>'
  '<aside class=notes>Richardson 1:42. In the heat of it, his congregation &mdash; many of them sworn United Irishmen &mdash; asked him to preach on the lawfulness of oaths and secret societies.<br>&rarr; Let the room guess what he said before you click.</aside></section>')

A(Q('&ldquo;&hellip;he presented so candidly and earnestly his views in condemnation of them that <b>a large portion of the audience became excited and exasperated</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:42', 'Asked to preach on the lawfulness of oaths and secret societies') +
  '<aside class=notes>Richardson 1:42. Campbell&rsquo;s &ldquo;utter refusal to take any part in the movement, and his conscientious opposition to secret associations,&rdquo; brought him &ldquo;into disfavor with his people.&rdquo; Asked, in the heat of it, to preach on oaths and secret societies, he condemned both &mdash; the United Irishmen and, by the same principle, the Orange Order. Foster: he &ldquo;had consistently spoken against membership in any society that might encourage rebellion and violence.&rdquo; He would take neither side, and said so from his own pulpit to a room that had largely taken one.</aside></section>')

A('<section class="slide"><h2>He had to be <span style="color:var(--gold)">escorted</span> through the crowd.</h2>'
  '<aside class=notes>Richardson: &ldquo;a prominent member, fearing lest he should be insulted, courteously took him by the arm and conducted him safely through the crowd.&rdquo; Through the whole rebellion he &ldquo;remained entirely unmolested, retaining the confidence of the community.&rdquo; Lord Gosford, governor of the county &mdash; who had himself tried to check the persecution of Catholics &mdash; was impressed enough to offer him a post as tutor to his family, a large salary and a house on the estate; Campbell declined it. When the rising failed and the reprisals came, Richardson says, &ldquo;the unhappy results of the rebellion vindicated the correctness of his principles.&rdquo;<br>&rarr; His first act for unity: in a country choosing sides, he refused to choose one for his people.</aside></section>')

A('<section class="slide plateslide tight"><figure class="plate short"><img src="IMG_TCAMPBELL" alt="" style="max-height:74vh"><figcaption>Thomas Campbell, 1763&ndash;1854</figcaption></figure>'
  '<aside class=notes>&rarr; Name him. Born County Down 1763; schoolmaster, then Seceder minister; forty-four when this story crosses the Atlantic. The engraving is later.</aside></section>')

A('<section class="slide"><div class=eyebrow>His designation in Ireland</div>'
  '<div class=litany>'
  '<div class=frag>Old Light</div>'
  '<div class=frag>Anti-Burgher</div>'
  '<div class=frag>Seceder</div>'
  '<div class=frag>Presbyterian</div>'
  '<div class="frag dim">of the Anti-Burgher Synod of Ulster</div>'
  '<div class="frag dim">under the General Associate Synod in Scotland</div>'
  '</div>'
  '<aside class=notes>Every word is a division from other Christians. Build it one line at a time, then take it apart, outside in.<br><br>Peel the four words, outside in &mdash; under two minutes, from these notes.<br><br><b>Old Light &middot; 1806 &mdash; division over whether the magistrate may enforce religion.</b> The Anti-Burghers split again the year before he sailed; he sided with the Old Lights by friendship more than conviction (Foster).<br><br><b>Anti-Burgher &middot; 1747 &mdash; division over an oath.</b> Whether a Seceder could swear to &ldquo;the true religion presently professed within this realm.&rdquo; Burghers: it only means not Catholic. Anti-Burghers: it blesses the church we left. Within two years, mutual excommunication &mdash; &ldquo;mutual forbidding of intermingling&rdquo;: Burghers and Anti-Burghers could no longer take communion together. The oath applied in three Scottish cities and had never been required in Ireland at all. This is the rule Conemaugh breaks.<br>Why it felt so big: the Seceders existed as a sworn &ldquo;Testimony&rdquo; against a corrupt national church. Swearing loyalty to that church&rsquo;s religion betrayed the reason they existed. Behind it stand the <b>Covenants</b> &mdash; the National Covenant (1638) and the Solemn League and Covenant (1643), oaths binding Scotland (and Ulster) to Reformed religion; the Westminster Confession was written to fulfil the second. The 1690 church never renewed them; the Seceders did.<br><br><b>Seceder &middot; 1733 &mdash; division over who appoints the minister.</b> Lay patrons placing ministers over congregations that had not called them; the dissenting presbyteries walked out of the Church of Scotland. His tradition began as a protest against imposed authority.</aside></section>')

A(C('Division After Division', ''))

A('<section class="slide"><div class=eyebrow>1798</div>'
  '<h2>He helped found a missionary society open to every denomination.</h2>'
  '<div class="sub frag">His synod voted it inconsistent with the Secession Testimony. He gave it up.</div>'
  '<aside class=notes>The Evangelical Society of Ulster, October 1798 &mdash; cross-denominational, supporting missionaries &ldquo;regardless of their denomination,&rdquo; tied to the London Missionary Society. His synod took it up at the very meeting that seated him (Synod of Ulster, 30 July&ndash;1 August 1799): &ldquo;Is the Evangelical Society of Ulster constituted on principles consistent with the Secession Testimony?&rdquo; Voted no. Three elders were sent to ask whether he would submit; he agreed to &ldquo;try to see eye to eye,&rdquo; gave up his role, and was out of the society by 1800.<br>&rarr; The one that could make him yield was never the one with the horses.</aside></section>')

A('<section class="slide"><div class=eyebrow>1804</div>'
  '<h2>He proposed reuniting Burghers and Anti-Burghers in Ireland.</h2>'
  '<div class="sub frag">Glasgow &ldquo;allowed him to argue his case but <b>refused to allow the proposition to come to a vote</b>.&rdquo;</div>'
  '<aside class=notes>October 1804, a consultation at Rich Hill drafted a formal proposal to reunite Burghers and Anti-Burghers in Ireland, on the ground that the burgess oath had never applied there. The Synod of Ulster at Belfast &ldquo;favorably received&rdquo; it. The General Associate Synod in Scotland moved to block it; the Irish sent Campbell to Glasgow to ask that the Irish churches decide for themselves. Glasgow &ldquo;allowed him to argue his case but refused to allow the proposition to come to a vote&rdquo; (Foster). Twice he tried; twice a court above him closed it.</aside></section>')

A('<section class="slide breath sect"><h2>Unity vs Authority</h2><div class=table-line></div>'
  '<div class=sub>Unity failed.</div>'
  '<aside class=notes>Card. Two tries in Ireland, both closed by his own church courts. Then the ship.<br>Running long? The missionary-society and reunion slides can be one sentence: &ldquo;Twice he tried to bring Christians together; twice his own church courts shut it down.&rdquo; Protect the court at minute 20.</aside></section>')

A('<section class="slide bleed"><div class=bg><div class="bgimg shipbg"></div></div>'
  '<div class=eyebrow>April 1807 &middot; Londonderry</div>'
  '<h2>His doctor prescribed a sea voyage.</h2>'
  '<div class=sub>He left his eighteen-year-old son, <b>Alexander</b>, in charge of the family and the school.</div>'
  '<aside class=notes>Teaching, pastoring Ahorey and synod work had produced a debilitating illness; his physician said the only remedy was to get out from under it and prescribed a sea voyage. He sailed 8 April 1807 on the <i>Brutus</i> out of Londonderry, thirty-five days, with a young charge, Hannah Acheson, whom he left with her uncle at Washington. He landed at Philadelphia in May to find the <b>Associate Synod of North America in session</b>, presented his letters from Markethill and Ahorey, and was seated. At his own request he was assigned to the <b>Presbytery of Chartiers</b>, western Pennsylvania, where old neighbours from Ireland had settled. He crossed the mountains and settled near the town of <b>Washington</b>, thirty miles south-west of Pittsburgh. Alexander, eighteen, stayed behind in charge of the family and the school; his story is the section after the site slide, if there is time.</aside></section>')

A('<section class="slide bleed sect"><div class=bg><div class="bgimg shipbg"></div></div>'
  '<div class=credit>Robert Salmon, <i>British Merchantman in the River Mersey off Liverpool</i>, 1809<br>A ship of the kind, not the <i>Brutus</i></div>'
  '<h2>Voyage to America</h2><div class=table-line></div>'
  '<aside class=notes>Card. He sails from Londonderry, 8 April 1807, on the <i>Brutus</i>.</aside></section>')

A('<section class="slide plateslide tight"><div class=eyebrow>August 1807 &middot; seventy miles from home</div>'
  '<figure class="plate wide"><img src="IMG_MAP" alt=""><figcaption>Reading Howell, <i>A Map of the State of Pennsylvania</i>, 1792 &middot; Library of Congress</figcaption></figure>'
  '<aside class=notes>Howell&rsquo;s 1792 map, the standard sheet of his lifetime. <b>Washington</b>, his base, is south-west of Pittsburgh. The presbytery met at the Harmony meeting-house on 30 June&ndash;1 July 1807 and gave him a circuit of appointments through <b>four counties</b> &mdash; Buffaloe, Mt. Pleasant, Pittsburgh, Squire McKee&rsquo;s, then <b>Cannamaugh on the third and fourth Sabbaths of August</b> (16 and 23 August 1807), then Squire Smith&rsquo;s, Templeton&rsquo;s, Upper Piney Creek, Mercer&rsquo;s, Hammel&rsquo;s, Breakneck, and back to Buffaloe in October (Chartiers minutes p. 122, in Hanna). Cannamaugh Church: an Associate congregation founded 1798 in Conemaugh Township, seventy miles east-north-east, in what had just become Indiana County; Ebenezer was the post office; Richardson calls it &ldquo;up the Allegheny.&rdquo; The ring marks the district, not a building. The point: the open table was not his home ground. It happened once, on a trip, on the far edge of his circuit.</aside></section>')

A(Q('&ldquo;This part of the country was then <b>thinly settled</b>, and it was seldom that ministerial services were enjoyed by the various <b>fragments of religious parties</b>, which, having <b>floated off from the Old World</b> upon the tide of emigration, had been <b>thrown together in the circling eddies of these new settlements</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:224', 'Who was out there') +
  '<aside class=notes>Richardson&rsquo;s description of the people Campbell had been sent up the Alleghany to serve. Not a congregation &mdash; wreckage: pieces of every Old World party, washed into the same eddy, and rarely a minister of any of them. The word is <b>fragments</b>, not dregs; the image is flotsam, not sediment.<br>&rarr; This is who is sitting in front of him at Conemaugh.<br><br>A two-Sabbath sacramental occasion, 16&ndash;23 August 1807, two months after he landed. The presbytery had assigned a younger minister, <b>William Wilson</b> &mdash; Glasgow-educated, in America since about 1791, John Anderson&rsquo;s first pupil &mdash; to assist, and the two travelled there together. Wrather: Campbell, &ldquo;perceiving that members from other branches of the Presbyterian Church were mingled with the seceders in his audience,&rdquo; took it as the moment to put his ideas into practice. Foster: Wilson was already &ldquo;upset by some of the religious views Campbell had formed in Ireland.&rdquo; Troubled before the table, not by it.</aside></section>')

A('<section class="slide"><h2>Faithful Presbyterians who had not received communion in years.</h2>'
  '<div class="sub frag">Not for lack of a minister. For lack of a minister <b>of their own sub-sect</b>.</div>'
  '<aside class=notes>Your sentence from the site. On the frontier the sub-sects were thin on the ground; a family could go years between a minister of exactly their own kind. Richardson 1:224 describes the settlers as fragments &ldquo;thrown together in the circling eddies of these new settlements.&rdquo;</aside></section>')

A('<section class="slide plateslide tokenslide"><div class=eyebrow>The token</div>'
  '<figure class="plate short"><img src="IMG_TOKEN" alt=""><figcaption>A Scottish communion token, 1750</figcaption></figure>'
  '<div class=sub>Examined beforehand. Handed a lead ticket. Surrendered at the table.</div>'
  '<aside class=notes>The Chapter 1 object. The Scottish communion season: days of preparation, the fencing sermon, the examination, and the lead token you surrendered at the table. The fence, in metal. And since 1747 Burghers and Anti-Burghers had been forbidden each other&rsquo;s tables.<br><b>&rarr; Through-line: who sets the terms of the table?</b> Say it here for the first time.</aside></section>')

A(Q('&hellip;that all his pious hearers, &ldquo;who felt so disposed and duly prepared, should, <b>without respect to party differences</b>, enjoy the benefits of the communion season then providentially afforded them.&rdquo;', 'Richardson, <i>Memoirs</i> 1:224', 'He did not fence the table') +
  '<aside class=notes>Richardson 1:224: he invited &ldquo;all his pious hearers, who felt so disposed and duly prepared,&rdquo; to the table &ldquo;without respect to party differences.&rdquo; Wilson&rsquo;s deposition gives the fencing itself: Scripture first, &ldquo;that he who runs might read&rdquo;; the Confession and the Testimony only &ldquo;generally,&rdquo; since to require them particularly &ldquo;would be to require an implicit faith.&rdquo; Asked why he did not fence the table, Wilson said Campbell gave as his reason &ldquo;the care that was taken by the session in not admitting such gross characters&rdquo; &mdash; the session had already examined the communicants; he would not add a doctrinal gate on top.</aside></section>')

A(Q('&ldquo;&hellip;the Lord&rsquo;s Supper, <b>that great ordinance of unity and love</b>.&rdquo;', '<i>Declaration and Address</i>, 1809', 'Two years later, in his own words') +
  '<aside class=notes>1809, not 1807 &mdash; say &ldquo;two years later he put it this way.&rdquo; From the <i>Declaration and Address</i>.</aside></section>')

A('<section class="slide"><h2>It was well received.</h2>'
  '<h2 class=frag style="color:var(--brick)">But not by everyone.</h2>'
  '<div class="sub frag">The young minister assisting him, <b>William Wilson</b>, reported it to the presbytery.</div>'
  '<aside class=notes>Your sentences from the site. Nobody objected in the room. On the Monday of the season he told them he would &ldquo;now come nearer home&rdquo;: the church maintained many things &ldquo;for which they had only human authority,&rdquo; a Confession and a Testimony among them; those who lacked them and did the same things &ldquo;were nothing the worse,&rdquo; and &ldquo;we are nothing the better&rdquo;; he could join Lutherans if they let him keep his own principles; Luther and Calvin should never have separated over &ldquo;a mere opinion&rdquo;; ministers &ldquo;had done more hurt to the church by their opinions than ever they did good&rdquo;; and the Burgher oath deserved &ldquo;a decent burial&rdquo; (Wilson&rsquo;s deposition). Wilson carried it to <b>John Anderson</b>, professor of theology, who then refused a joint appointment with Campbell at Buffaloe. At the October presbytery Wilson testified; a committee of Anderson and three of his former students was appointed; Campbell&rsquo;s appointments were suspended; he protested and withdrew. The libel followed in January.</aside></section>')

A(C('The Trial', 'Five minutes belong to the room.'))

A('<section class="slide libelposter" id=libel><h2 style="max-width:none;white-space:nowrap;font-size:clamp(34px,6.4vmin,80px)">The Libel <span class=dim>&middot; January 1808</span></h2>'
  '<div class=days>'
  '<div class="d"><span class=dn>1</span><span>that appropriating Christ as one&rsquo;s own Savior does not belong to the essence of saving faith</span></div>'
  '<div class="d"><span class=dn>2</span><span>that a church has no divine warrant for holding Confessions of Faith as terms of communion</span></div>'
  '<div class="d"><span class=dn>3</span><span>that ruling elders may pray and exhort publicly in vacant congregations</span></div>'
  '<div class="d"><span class=dn>4</span><span>that our people may hear ministers in stated opposition to our testimony</span></div>'
  '<div class="d"><span class=dn>5</span><span>that Christ was not subject to the precept of the law, as well as its penalty, for his people</span></div>'
  '<div class="d"><span class=dn>6</span><span>that a man may live without sin in this life</span></div>'
  '<div class="d"><span class=dn>7</span><span>that he preached in another minister&rsquo;s bounds without appointment</span></div>'
  '</div>'
  '<aside class=notes>Hanna, ch. II, from the Chartiers minutes. Read them plain.<br>Charge 1 is a Glas-and-Sandeman question: Sandeman taught faith is simple belief of the testimony, against Hervey&rsquo;s &ldquo;appropriating&rdquo; faith. His accusers heard Sandeman in him.<br>The verdict slide words 1 and 7 in plain English &mdash; say &ldquo;in plain words&rdquo; when it comes up.</aside></section>')

A('<section class="slide room"><h2 style="font-size:clamp(48px,9.6vmin,126px)"><span style="color:var(--gold)">YOU</span> are the court.</h2>'
  '<div class=sub style="font-size:clamp(30px,5.2vmin,64px)">Guilty, or not guilty?</div>'
  '<aside class=notes>~minute 20. Hand it over. Co-teacher reads the charges.</aside></section>')

A('<section class="slide hard" id=verdict><h2 style="max-width:none;white-space:nowrap;font-size:clamp(34px,6.4vmin,80px)">The Verdict <span class=dim>&middot; February 1808</span></h2>'
  '<div class="days verdictlist">'
  '<div class="d"><span class=dn>1</span><span>that one may have doubts even in the midst of saving faith</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>2</span><span>that a church has no divine warrant for holding Confessions of Faith as terms of communion</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>3</span><span>that ruling elders may pray and exhort publicly in vacant congregations</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>4</span><span>that our people may hear ministers in stated opposition to our testimony</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '<div class="d"><span class=dn>7</span><span>that a divine calling, ordination, and the invitation of the people is sufficient warrant to preach, without authorization of church authorities</span><span class="verdict frag v-red" data-o=1>guilty!</span></div>'
  '</div>'
  '<aside class=notes>Minutes, 12 Feb 1808: 1 and 2 &ldquo;clearly proved&rdquo;; 3, 4 and 7 &ldquo;acknowledged&hellip; and still adhered to by him.&rdquo; Charges 5 and 6 fell away: his answers were accepted (5 &ldquo;not sufficiently proved&rdquo;; 6 approved except &ldquo;or&rdquo; for &ldquo;and&rdquo;). One more fact for the room if it asks: Campbell objected that &ldquo;there might be witnesses found in Conemaugh who would prove the contrary of what Mr. Wilson had deposed.&rdquo; The presbytery would not wait for them, and the Synod&rsquo;s dissenters later conceded the point &mdash; he was condemned &ldquo;by witnesses from elsewhere.&rdquo; No one who sat in that congregation was ever heard. Click through the five verdicts.<br>Charges 1 and 7 are paraphrased here; same charges as the libel.<br><b>&rarr; Through-line: who sets the terms of the table?</b> Second time.</aside></section>')

A(C('The Appeal', 'May 1808. He appealed the presbytery&rsquo;s verdict to the Associate Synod at Philadelphia and read his appeal aloud before it.'))

A(Q('&ldquo;For what error or immorality ought I to be rejected, except it be that I refuse to acknowledge as obligatory upon myself, or to impose upon others, anything as of Divine obligation for which I cannot produce a <b>&lsquo;Thus saith the Lord?&rsquo;</b>&rdquo;', 'Richardson, <i>Memoirs</i> 1:227', 'May 1808 &middot; his appeal to the Synod at Philadelphia') +
  '<aside class=notes>May 1808. He appealed the presbytery&rsquo;s verdict to the Associate Synod at Philadelphia. Richardson: &ldquo;he addressed an earnest appeal to the Synod when his case came up.&rdquo; The Synod read his reasons of protest and appeal on 20 May, and &ldquo;parties were heard.&rdquo;<br>Date check: the text itself carries no date. Two sources fix it to May 1808 &mdash; the Synod minutes (20 May 1808: &ldquo;Read his reasons of protest and appeal&rdquo;; Hanna ch. IV) and Alexander&rsquo;s <i>Memoirs of Elder Thomas Campbell</i> (1861), pp. 12&ndash;15, which prints it in full as the &ldquo;Protest and Appeal&rdquo; to the Associate Synod. Richardson copied it from Alexander. &ldquo;My written declaration&rdquo; in it means his written answers to the libel, which the Synod also read that day.</aside></section>')

A(Q('&ldquo;As to the expediency of such, <b>I leave every man to his own judgment</b>&hellip; a matter on which&hellip; the Scriptures are silent&hellip;&rdquo;', 'Thomas Campbell, Protest and Appeal &middot; A. Campbell, <i>Memoirs of Elder Thomas Campbell</i> (1861), p. 14', 'May 1808 &middot; his appeal to the Synod &middot; on creeds and confessions') +
  N('&ldquo;Such&rdquo; = human standards: creeds, confessions, the Testimony.',
    'Full sentence: &ldquo;As to the expediency of such, I leave every man to his own judgment, while I claim the same privilege for myself. This, I presume, I may justly do about a matter on which, <b>according to the learned doctor</b>, the Scriptures are silent.&rdquo; The doctor is Philip Doddridge, whom he has just quoted: had creeds been necessary, &ldquo;the sacred oracles would have presented them.&rdquo;',
    'What he will not allow: a creed &ldquo;made a positive article of sin or duty, or a term of communion &mdash; in which cases I dare neither acquiesce nor be silent.&rdquo;',
    '&rarr; Where Scripture is silent, each person is free. The fence is the thing he refuses.',
    'Richardson cut this passage (his asterisks at 1:227); Alexander&rsquo;s 1861 text keeps it.'))

A(Q('&ldquo;It is, therefore, because I have <b>no confidence, either in my own infallibility or in that of others</b>, that I absolutely refuse, as inadmissible and schismatic, the introduction of human opinions and human inventions into the faith and worship of the Church.&rdquo;', 'Richardson, <i>Memoirs</i> 1:227', 'May 1808 &middot; his appeal to the Synod at Philadelphia') +
  '<aside class=notes>Same appeal, a few lines before the &ldquo;Thus saith the Lord&rdquo; sentence (Richardson 1:226&ndash;27).<br>The Westminster Confession says it too: &ldquo;All synods or councils since the apostles&rsquo; times&hellip; may err, and many have erred&rdquo; (31.4). He is holding the church to its own disclaimer.<br>He had opened it: &ldquo;Honored Brethren: before you come to a final issue in the present business, let me entreat you to pause a moment.&rdquo;</aside></section>')

A(C('The Judgment', 'The Synod set the presbytery&rsquo;s judgment aside for &ldquo;informalities&rdquo; &mdash; then found his answers on the same articles &ldquo;so evasive and unsatisfactory, and highly equivocal&hellip; sufficient grounds to infer censure.&rdquo;'))

A(Q('&ldquo;It is erroneous&hellip; to assert that a church has <b>no divine warrant for holding Confessions of Faith as terms of communion</b>.&rdquo;', '', '<span style="color:var(--gold)">Communion</span> &middot; Article 2', 'slide hard') +
  '<aside class=notes>The question of the class. &ldquo;But you, the Rev&rsquo;d Thomas Campbell, taught this error at Conemaugh and Buffaloe.&rdquo;<br>&rarr; Who may come to the table, and on whose terms.</aside></section>')

A(Q('&ldquo;It is erroneous&hellip; to assert that it is <b>the duty of ruling elders to pray and exhort publickly</b> in vacant congregations.&rdquo;', '', '<span style="color:var(--gold)">Priesthood</span> &middot; Article 3', 'slide hard') +
  '<aside class=notes>Laymen leading worship where there is no minister. The first person to decide what happened in a room this hour was an elder: &ldquo;Pray, sir.&rdquo;</aside></section>')

A(Q('&ldquo;It is erroneous&hellip; to assert that it is warrantable for the people of our communion to <b>hear ministers that are in a stated opposition to our testimony</b>.&rdquo;', '', '<span style="color:var(--gold)">Freedom of Conscience</span> &middot; Article 4', 'slide hard') +
  '<aside class=notes>&ldquo;Occasional hearing&rdquo; &mdash; going to hear ministers outside your own church. (His son Alexander was doing exactly this every week in Glasgow at the same time; that story is the section after the site slide.)</aside></section>')

A(Q('&ldquo;he was accordingly <b>rebuked and admonished by the Mod&rsquo;r</b>&rdquo;', 'Minutes of the Associate Synod, May 1808', 'The Synod&rsquo;s answer', 'slide hard',
    '<div class=sub>He submitted &mdash; as &ldquo;no more&hellip; than an act of deference to the judgment of the court.&rdquo;</div>') +
  '<aside class=notes>Presbytery&rsquo;s judgment set aside for &ldquo;informalities&rdquo;; his answers found &ldquo;so evasive and unsatisfactory, and highly equivocal&hellip; sufficient grounds to infer censure.&rdquo; Rebuked to his face before the assembled Synod.</aside></section>')

A(Q('&ldquo;&hellip;had they possessed the power, he would have suffered martyrdom at their hands, or, as he expressed it, that <b>&lsquo;nothing but the law of the land had kept his head upon his shoulders.&rsquo;</b>&rdquo;', 'Richardson, <i>Memoirs</i> 1:219&ndash;220', '', 'slide hard') +
  '<aside class=notes>His own summary of the two years &mdash; said to Alexander on the road a year later, as Richardson reports it. Keep the qualifier: <i>had they possessed the power</i>.</aside></section>')

A(C('The Break', 'Accuracy: the break is September 1808, three weeks before his family sailed.'))

A(Q('&ldquo;It is with <b>sincere reluctance</b>&hellip; that I find myself in duty bound to refuse submission to their decision as unjust and partial&hellip; And I hereby do <b>decline all ministerial connection with, or subjection to, the Associate Synod of North America</b>.&rdquo;', 'Thomas Campbell, 13&ndash;14 September 1808 &middot; Chartiers Presbytery, Burgettstown', 'September 1808') +
  '<aside class=notes>He had offered this letter in May and withdrawn it. In September he sent it again. Printed by Alexander, 1861.<br>Read only the gold phrase; say the rest in your own words.</aside></section>')

A(C('The Grove', ''))

A(Q('&ldquo;Sometimes the deep shade of a <b>maple grove</b> sheltered the assembly from the summer sun. Generally, however, the houses of his old Irish neighbors&hellip; were the places where he had his appointments for preaching, and where he discoursed weekly to <b>all who chose to assemble</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:231') +
  '<aside class=notes>No pulpit, no salary, no standing &mdash; and no interruption.<br>&rarr; An association, then a church, then a movement.</aside></section>')

A(C('What did they stand for?', ''))

A(Q('&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809', 'That fall they asked him to write down what they stood for', 'slide',
    '<div class="sub frag">Next week: <b>the Declaration and Address</b>.</div>') +
  '<aside class=notes>Close his half of the hour on his own sentence. It returns at the end.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 1 of 6</div>'
  '<h2>The unity movement <span style="color:var(--gold)">did not begin in America.</span></h2>'
  '<aside class=notes>He was working for unity in a divided Ireland &mdash; the missionary society, the Burgher reunion &mdash; years before America. He brought that work with him.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 2 of 6</div>'
  '<h2>They divided over <span style="color:var(--gold)">hospitality, not doctrine.</span></h2>'
  '<aside class=notes>He did not set out to found anything or to dispute a doctrine; he extended the Supper to believers the system had orphaned, holding the fences to be the thing without divine warrant.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 3 of 6</div>'
  '<h2>Unity rose from below; <span style="color:var(--gold)">division was enforced from above.</span></h2>'
  '<aside class=notes>The people kept moving toward each other. What stopped them was the authority structure that bound them to other people&rsquo;s fights.<br>&bull; The Burgher oath: a 1747 quarrel over an oath sworn by burgesses of Scottish towns. It never applied in Ireland &mdash; yet it divided Irish Seceders, and then American ones.<br>&bull; 1799: a missionary society open to every denomination. His synod voted it &ldquo;inconsistent with the Secession Testimony.&rdquo;<br>&bull; 1804: the Irish synod at Belfast &ldquo;favorably received&rdquo; the Burgher reunion. Glasgow would not let it come to a vote.<br>&bull; Conemaugh, 1807: the frontier settlers were &ldquo;fragments of religious parties&rdquo; carried over on the tide of emigration, still bound to Old World divisions. The open table was well received in the room. A colleague reported it; no one from Conemaugh was ever heard as a witness.<br>&rarr; Slide 26 set this up: Unity vs Authority.<br>Caveat, if the room romanticizes &ldquo;the people&rdquo;: in 1798 his own congregation turned on him over secret societies. He told the crowd no, too.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 4 of 6</div>'
  '<h2>He trusted ordinary believers with <span style="color:var(--gold)">the table, the pulpit, and their own ears.</span></h2>'
  + N('Look at what the charges that held have in common. Four of the five move power from the church court to ordinary believers:',
      '<b>The table</b> (charge 2): no confession as the gate. Each examines himself &mdash; Brownlow&rsquo;s 1 Cor 11:28 (now in the Addendum).',
      '<b>The pulpit</b> (charge 3): ruling elders &mdash; laymen &mdash; may pray and exhort where there is no minister. Callback: &ldquo;Pray, sir!&rdquo;',
      '<b>Their own ears</b> (charge 4): the people may go and hear whom they choose.',
      '<b>The call</b> (charge 7): the libel allowed only two regular calls &mdash; sent by a presbytery, or ordained to a congregation. His answer: he had &ldquo;the call of some of the most regular and respectable people of that vicinity.&rdquo; The people&rsquo;s invitation counted.',
      'And the people answered: petitions from Buffaloe, Chartiers, Mt. Pleasant and Burgettstown went to the Synod in his favor (May 1808).',
      '&rarr; Recognizing more than empowering: the people already had faith, judgment, and a voice. He refused to treat them as needing a court&rsquo;s permission.',
      'Honest caveat: the witnesses against him were lay people too (Buffaloe). He was still a Presbyterian minister, not a democrat. Governance is Chapter 12.',
      'Sources: Hanna ch. II (libel), ch. III (his answer to art. 7), ch. IV (petitions).'))

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 5 of 6</div>'
  '<h2>&ldquo;Thus saith the Lord&rdquo; was a check on <span style="color:var(--gold)">new boundaries</span> &mdash; not a test for other people&rsquo;s worship.</h2>'
  '<aside class=notes>Slide 41: he refuses &ldquo;to acknowledge as obligatory upon myself, <b>or to impose upon others</b>, anything as of Divine obligation&rdquo; without a &ldquo;Thus saith the Lord.&rdquo; The setting is a man being &ldquo;thrust out from communion.&rdquo; The target is schism.<br>&bull; Same appeal: &ldquo;all this <b>without any intention on my part to judge or despise my Christian brethren who may not see with my eyes</b>&rdquo; (1:227).<br>&bull; Honest caveat: he did want worship conformed to Scripture &mdash; &ldquo;the introduction of human opinions and human inventions into the faith and worship of the Church&rdquo; (slide 43), and he calls it &ldquo;schismatic.&rdquo; But he bound himself with it, and refused to make it a fence for anyone else.<br>&rarr; Later generations turned the same words into a fence &mdash; dividing over practices in worship. That inverts what he used them for.<br>&bull; The lines Richardson cut (Alexander&rsquo;s 1861 <i>Memoirs of Elder Thomas Campbell</i>, p. 14) make the point outright. On human standards (creeds, confessions), quoting Dr. Doddridge first: &ldquo;As to the expediency of such, I leave every man to his own judgment, while I claim the same privilege for myself. This, I presume, I may justly do about a matter on which, according to the learned doctor, <b>the Scriptures are silent</b>.&rdquo; But when one is &ldquo;made a positive article of sin or duty, or a term of communion &mdash; in which cases I dare neither acquiesce nor be silent&rdquo; &mdash; he protests &ldquo;against making sins and duties which his word has nowhere pointed out.&rdquo;<br>&rarr; In 1808, where Scripture is silent, each person is free. The fence is what he refuses.<br>Sources: Richardson 1:226&ndash;27; A. Campbell, <i>Memoirs of Elder Thomas Campbell</i> (1861), pp. 13&ndash;15.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 6 of 6</div>'
  '<h2>They stood for <span style="color:var(--gold)">the universal church.</span></h2>'
  '<aside class=notes>That autumn the people following him from farmhouse to grove asked him to write down what they stood for, and the first sentence was that the church of Christ upon earth is essentially, intentionally, and constitutionally one.</aside></section>')

A('<section class="slide room"><div class=eyebrow>&#9670; for discussion</div>'
  '<h2>What is beautiful here? What do we carry forward?</h2>'
  '<aside class=notes>~minute 40.<br>Backup prompts (off the slide): What &ldquo;testimonies&rdquo; &mdash; written or unwritten &mdash; do we treat as terms of fellowship today? Who around us has gone years without being invited to the table?<br>If the room is slow: &ldquo;Have you ever stayed at a table you no longer believed in &mdash; or left one?&rdquo;<br>Optional close (Brownlow is now in the Addendum): his 1945 sentence &mdash; &ldquo;no man or set of men has the right to judge&rdquo; &mdash; is where this trial ends up. Our own church&rsquo;s tract.</aside></section>')

A(W1_SITESLIDE)








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
  '<div class="sub frag">The church courts fought them at every turn.</div>'
  + N('Alexander was often at Ewing&rsquo;s house. Ewing told him about the Haldanes &mdash; Robert and James, wealthy ex-navy laymen. James preached for years before he was ordained; Robert funded the movement.',
      'Ewing himself: left the Church of Scotland in 1798 to join them; ran their Glasgow Tabernacle and seminary; started weekly communion there. Their 1799 church was founded to avoid &ldquo;that contracted spirit which would exclude from the pulpit, or from occasional communion, any faithful preacher of the gospel or sincere lover of Christ&rdquo; (1:166) &mdash; Conemaugh, eight years early.',
      'Article 3 echo: his father was condemned for letting elders &mdash; non-ministers &mdash; pray and exhort.',
      'The established clergy opposed them at every turn. Richardson: &ldquo;unscrupulous methods,&rdquo; power used &ldquo;in an arbitrary manner.&rdquo;',
      'Richardson says this story, more than anything, is what changed Alexander&rsquo;s mind.',
      'Source: Richardson 1:188&ndash;89.'))

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

A(Q('&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ&hellip;&rdquo;', '<i>Declaration and Address</i>, 1809', 'That fall they asked him to write down what they stood for', 'slide',
    '<div class="sub frag">Next week: <b>the Declaration and Address</b>.</div>') +
  '<aside class=notes>Optional sting: the presbytery formally deposed him on 18 April 1810 &mdash; seven months after this was published.</aside></section>')

A(C('Addendum', 'Reference material; not part of the telling.'))

A(C('Open Communion', ''))

A('<section class="slide"><h2 style="font-size:clamp(46px,9vmin,118px)">What is <span style="color:var(--gold)">open communion</span>?</h2>'
  '<aside class=notes>Ask it. Let two or three people answer before you give the working definition.</aside></section>')

A('<section class="slide"><div class="eyebrow quiet">A working definition</div>'
  '<h2>The Lord&rsquo;s Supper offered to every believer present &mdash; with no church test at the door.</h2>'
  '<div class=sub>Its opposite is <i>close communion</i>: only members of that church, in good standing, may partake.</div>'
  '<aside class=notes>General definition, not a technical one. In the Scottish Presbyterian world of 1800 the test was the token; in Baptist churches it was immersion; in most churches it was membership.</aside></section>')

A('<section class="slide room"><h2>Did you know this was <span style="color:var(--gold)">part of our practice</span>?</h2>'
  '<aside class=notes>Hands. Then: Churches of Christ have practised it, and defended it in print, for a very long time.</aside></section>')

A('<section class="slide plateslide tight"><div class=eyebrow>1945</div>'
  '<figure class="plate short"><img src="IMG_BROWNLOW" alt="" style="max-height:72vh"><figcaption>Leroy Brownlow, <i>Why I Am a Member of the Church of Christ</i> &middot; Reason XXIII, &ldquo;Because of its scriptural teaching and observance of the Lord&rsquo;s Supper&rdquo;</figcaption></figure>'
  '<aside class=notes>The standard twentieth-century tract of the Churches of Christ; twenty-five reasons. Reason XXIII, section III: &ldquo;Who shall participate in the communion.&rdquo;</aside></section>')

A(Q('&ldquo;&hellip;no man or set of men has the right to judge who shall and shall not have the privilege of communion&hellip; The self-examination taught in this verse <b>condemns the doctrine of close communion</b>. Each is to examine himself; not somebody else.&rdquo;', 'Leroy Brownlow, <i>Why I Am a Member of the Church of Christ</i>, 1945, p. 178', 'On 1 Corinthians 11:28') +
  '<aside class=notes>His argument: it is the Lord&rsquo;s table, so the judgment belongs to Christ and to each communicant, not to the church. That is the position Thomas Campbell was tried for in 1808.</aside></section>')

A(RECAP_VO)

A('<section class="slide ideasmap"><div class=eyebrow>What this week touched</div>'
  '<div class=wmap><div class="r ms-christ"><span class="th key">CHRIST ALONE</span></div>'
  '<div class="r ms-pri"><span class="th key">UNITY</span><span class="th key">PRIESTHOOD</span><span class="th on">FUTURE</span></div>'
  '<div class="r ms-sec"><span class="th on">HOMECOMING</span><span class="th on">SELF-SACRIFICE</span><span class="th key">FREEDOM OF CONSCIENCE</span><span class=th>SCIENCE &amp; REASON</span><span class="th on">MINIMALISM</span></div>'
  '<div class="r ms-pra"><span class="th key">the Table</span><span class=th>Baptism</span><span class="th on">Scripture</span><span class=th>Singing</span><span class="th on">Congregation</span></div></div>'
  '<div class=small>Bright: the spine of this week. Dim: touched in passing. Unlit: still ahead of us.</div>'
  '<aside class=notes>Same board as Chapter 1. New light: Priesthood, Freedom of Conscience, Christ Alone.</aside></section>')

A('<section class="slide"><div class=eyebrow>How each week works</div>'
  '<div class=shape><span class=step>Story</span><span class=sep>&rarr;</span><span class=step>Idea</span><span class=sep>&rarr;</span><span class=step>Future</span></div>'
  '<aside class=notes>One of us tells a story from our history. Another cross-examines it. Then the questions are yours.</aside></section>')

A('<section class="slide"><p class=bigquote style="font-size:clamp(36px,7.4vmin,92px)"><span class=q>What is beautiful here?<br>What do we carry forward?</span></p>'
  '<aside class=notes>The class question. It closes every week.</aside></section>')






