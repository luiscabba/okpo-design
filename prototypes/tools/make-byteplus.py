"""Builds earner-byteplus.html from earner.html: the same earner app and follower page,
with BytePlus as the brand instead of GCash. Payouts still go to the earner's GCash wallet
(that is OkPo's payout rail, not the brand), so "Claim to GCash" and the like stay.
Facts used, from byteplus.com/en/product/modelark (read 5 Oct 2026): new accounts get
500,000 free tokens per language model and 2,000,000 per vision model; Seedance 2.5 makes
a single 30-second clip, takes up to 50 reference files and works in more than 10 languages.
Run: python3 tools/make-byteplus.py  (from prototypes/)"""
import re, sys
src = open('earner.html').read()

R = [
 # page title and storage, so the two demos never share state
 ('<title>OkPo Earner and Page</title>', '<title>OkPo Earner and Page · BytePlus</title>'),
 ("okpo-ep5", "okpo-ep5-byteplus"),
 # control strip
 ('Follower taps Heroes Reel', 'Follower taps Seedance Reel'),
 ('Taps Ipon Story', 'Taps Builders Story'),
 ('GCash confirms sign-ups', 'BytePlus confirms sign-ups'),
 # missions and talking points
 ("tp:'Free to join'", "tp:'Free tokens to start'"),
 ("tp:'Five-minute sign-up'", "tp:'A 30-second clip, one prompt'"),
 ("tp:'Send money home'", "tp:'Show what you made'"),
 ("t:'Reel on today’s talking point'", "t:'Reel: make a clip live'"),
 ("t:'Story with your sign-up link'", "t:'Story with your sign-up link'"),
 ("tp:'Save for one goal'", "tp:'Your first API call'"),
 ("t:'Story: your first ₱50 deposit'", "t:'Story: your first API call'"),
 # campaigns
 ("{id:'heroes',name:'GCash Heroes',short:'Heroes',brand:'GCash',", "{id:'heroes',name:'BytePlus Seedance Creators',short:'Seedance',brand:'BytePlus',"),
 ("deal:'₱40 per passed post · ₱12 per activated sign-up'", "deal:'₱40 per passed post · ₱12 per sign-up that makes a first clip'"),
 ("per:'Plus ₱12 for every sign-up from your page that activates.'", "per:'Plus ₱12 for every sign-up from your page that makes a first clip.'"),
 ("{id:'ipon',name:'GCash Ipon Challenge',short:'Ipon',brand:'GCash',", "{id:'ipon',name:'BytePlus ModelArk Builders',short:'Builders',brand:'BytePlus',"),
 ("per:'Plus ₱10 for every first deposit from your page.'", "per:'Plus ₱10 for every first API call from your page.'"),
 ("why:'Picked for you because your followers are students in Iloilo.'", "why:'Picked for you because your followers are students learning to code.'"),
 ("ask:'Two Reels a week about saving for a goal. Missions arrive in Today, tagged Ipon.'", "ask:'Two Reels a week building something small with ModelArk. Missions arrive in Today.'"),
 # past posts and tips
 ("{t:'Reel · GCash Heroes',when:'Fri',state:'passed',r:40,tp:'Free to join'", "{t:'Reel · Seedance Creators',when:'Fri',state:'passed',r:40,tp:'Free tokens to start'"),
 ("Your hook said “libre” in the first two seconds. Keep opening like that.", "Your hook said “free tokens” in the first two seconds. Keep opening like that."),
 ("Hold the sign-up screen a beat longer at the end.", "Hold the finished clip a beat longer at the end."),
 ("{t:'Story · GCash Heroes',when:'Fri',state:'passed',r:15,tp:'Five-minute sign-up'", "{t:'Story · Seedance Creators',when:'Fri',state:'passed',r:15,tp:'A 30-second clip, one prompt'"),
 ("Say “mga 5 minuto lang” out loud, not only in the caption.", "Read your prompt out loud, not only in the caption."),
 ("Show the real app. The second frame was a screenshot.", "Show the real console. The second frame was a screenshot."),
 ("{t:'Reel · GCash Heroes',when:'Wed',state:'passed',r:40,tp:'Send money home'", "{t:'Reel · Seedance Creators',when:'Wed',state:'passed',r:40,tp:'Show what you made'"),
 ("Name who you send money to. It was the talking point, and the Reel never got there.", "Show the clip you made. It was the talking point, and the Reel never got there."),
 # notifications
 ("{t:'GCash invited you to Ipon Challenge',b:'A better deal: ₱30 per passed post instead of ₱25. Reply within 72 hours.'", "{t:'BytePlus invited you to ModelArk Builders',b:'A better deal: ₱30 per passed post instead of ₱25. Reply within 72 hours.'"),
 ("3 missions for GCash Heroes. The first takes about 2 minutes.", "3 missions for Seedance Creators. The first takes about 2 minutes."),
 ("Heroes replies drop to ₱8 on Sat 4 Oct", "Seedance replies drop to ₱8 on Sat 4 Oct"),
 # pass tips
 ("You opened on “libre”. That is today’s talking point, done right.", "You opened on “free tokens”. That is today’s talking point, done right."),
 ("End on the app sign-up screen, not your face.", "End on the finished clip, not your face."),
 ("Say “mga 5 minuto lang” out loud.", "Show the prompt, then the clip."),
 ("Your reply named who you send money to. Keep it that specific.", "Your reply showed the clip you made. Keep it that specific."),
 ("Show the deposit screen for two seconds, not one.", "Show the API response for two seconds, not one."),
 ("Name the goal in the first line of the caption.", "Name what you built in the first line of the caption."),
 # mission detail: rules
 ("plus ₱10 for every first deposit", "plus ₱10 for every first API call"),
 ("more for every activated sign-up", "more for every sign-up that makes a first clip"),
 ("{never:[['Promise approval, amounts or returns.','R-03 · GCash Playbook']],careful:[['Loans or credit: never in the hook, only after the main message.','R-09 · GCash Playbook']],always:[['Show your own first ₱50 going into GSave, in the real app.','R-05 · Ipon Challenge'],['Tag #IponChallenge.','R-12 · Ipon Challenge'],",
  "{never:[['Say the free tokens never run out.','R-03 · BytePlus Playbook']],careful:[['Comparing with other AI models: only with numbers BytePlus published.','R-09 · BytePlus Playbook']],always:[['Show your own first API call, in the real console.','R-05 · ModelArk Builders'],['Tag #ModelArkBuilders.','R-12 · ModelArk Builders'],"),
 ("{never:[['Promise approval, amounts or dates.','R-03 · GCash Playbook'],['Compare fees with other wallets.','R-04 · GCash Playbook']],careful:[['Loans or credit: never in the hook, only after the main message.','R-09 · GCash Playbook']],always:[['Show the Heroes sign-up in the real app, under 20 seconds.','R-05 · GCash Heroes'],['Say it’s free to join.','R-06 · GCash Heroes'],['Tag #GCashHeroes.','R-13 · GCash Heroes'],",
  "{never:[['Say the free tokens never run out.','R-03 · BytePlus Playbook'],['Use a real person’s face or a famous character without permission.','R-04 · BytePlus Playbook']],careful:[['Comparing with other AI models: only with numbers BytePlus published.','R-09 · BytePlus Playbook']],always:[['Show the clip being made in the real Seedance page, under 20 seconds.','R-05 · Seedance Creators'],['Say the free tokens are for new accounts.','R-06 · Seedance Creators'],['Tag #SeedanceCreators.','R-13 · Seedance Creators'],"),
 ("['End on the app sign-up, not the website.','R-08 · GCash Heroes']", "['Label the clip as made with AI.','R-08 · Seedance Creators']"),
 ("data-copy=\"${ip?'gcash.com/ipon?ref=ana':'gcash.com/heroes?ref=ana'}\"", "data-copy=\"${ip?'byteplus.com/modelark?ref=ana':'byteplus.com/seedance?ref=ana'}\""),
 ("'Una kong ₱50 sa ipon! #IponChallenge':'Libre mag-join sa GCash Heroes! #GCashHeroes'", "'First API call ko sa ModelArk! #ModelArkBuilders':'30 seconds, isang prompt. Free tokens para sa bagong account. #SeedanceCreators'"),
 ("Other ${ip?'savers':'Heroes'} get other talking points today", "Other ${ip?'builders':'creators'} get other talking points today"),
 # Always true on the campaign screen and Today
 ("['rules','Say it’s a paid partnership.'],['rules','Never promise approval, amounts or dates.'],['voice','Warm Taglish, short lines.']", "['rules','Say it’s a paid partnership.'],['rules','Free tokens are for new accounts. Never say they don’t run out.'],['voice','Plain words, show the thing you made.']"),
 # wallet and receipts (payout stays GCash; campaign names change)
 ("'All campaigns':'GCash Heroes'", "'All campaigns':'Seedance Creators'"),
 ("Confirming · GCash checks the account is active", "Confirming · BytePlus checks the account made a first clip"),
 ("GCash couldn’t verify the account · removed Tue", "BytePlus couldn’t verify the account · removed Tue"),
 ("<span>GCash Heroes · week 2</span>", "<span>Seedance Creators · week 2</span>"),
 ("'Paano kung wala pa akong GCash?','Ano ang makukuha ko?'", "'Kailangan ba ng credit card?','Ano ang makukuha ko?'"),
 # onboarding
 ("You tapped her GCash Heroes Reel", "You tapped her Seedance Creators Reel"),
 ("<b class=\"grow\">GCash Heroes</b><span class=\"chip wait\">Trial · 0 of 3</span>", "<b class=\"grow\">Seedance Creators</b><span class=\"chip wait\">Trial · 0 of 3</span>"),
 ("₱40 per passed post · ₱12 per activated sign-up", "₱40 per passed post · ₱12 per sign-up that makes a first clip"),
 # banners and takeovers
 ("'Ipon Challenge sign-up':'A follower signed up'", "'A follower made a first API call':'A follower signed up'"),
 ("+₱12 once GCash confirms", "+₱12 once BytePlus confirms"),
 ("'1 first deposit · Ipon Challenge':'1 sign-up · GCash Heroes'", "'1 first API call · ModelArk Builders':'1 sign-up · Seedance Creators'"),
 ("'A follower started the Ipon Challenge':'A follower signed up'", "'A follower made a first API call':'A follower signed up'"),
 ("${ip?'Ipon Challenge':'GCash Heroes'}", "${ip?'ModelArk Builders':'Seedance Creators'}"),
 ("+₱${amt} once GCash confirms.", "+₱${amt} once BytePlus confirms."),
 ("Nothing is waiting on GCash right now.", "Nothing is waiting on BytePlus right now."),
 ("'GCash confirmed your sign-ups. It’s ready to claim.'", "'BytePlus confirmed your sign-ups. It’s ready to claim.'"),
 # follower page
 ("GCash confirms it, then Ana gets credit", "BytePlus confirms it, then Ana gets credit"),
 ("Reel · GCash Heroes", "Reel · Seedance Creators"),
 ("Story · GCash Heroes", "Story · Seedance Creators"),
 ("heroes:{k:'pin',t:'Join GCash Heroes',d:'Libre mag-join. About 5 minutes on the GCash app.',b:'Sign up on GCash',src:'Reel'},ipon:{k:'pin',t:'Start the Ipon Challenge',d:'Ipon ng ₱50 sa GSave. Libre at mga 3 minuto.',b:'Start saving on GCash',src:'Story'}",
  "heroes:{k:'pin',t:'Try Seedance on BytePlus',d:'Free tokens for new accounts. Make a 30-second clip from one prompt.',b:'Sign up on BytePlus',src:'Reel'},ipon:{k:'pin',t:'Build with ModelArk',d:'Free tokens for every model when you start. Get an API key in a few minutes.',b:'Get an API key',src:'Story'}"),
 ("@ana.posts · food and budget tips, QC", "@ana.posts · AI edits and food vlogs, QC"),
 ("Paid partnership with GCash", "Paid partnership with BytePlus"),
 ("'Opens GCash. Ana gets credit when GCash confirms it.'", "'Opens BytePlus. Ana gets credit when BytePlus confirms it.'"),
 ("['Heroes sign-up in 14s','₱500 grocery run','Budget ulam','Paano mag-GCash','Baon hacks','Week of meals']", "['30-sec clip, 1 prompt','₱500 grocery run','Budget ulam','My first AI ad','Baon hacks','Week of meals']"),
 ("A.via==='ipon'?'the Ipon Challenge':'GCash Heroes'", "A.via==='ipon'?'ModelArk Builders':'Seedance Creators'"),
 ("Answers from GCash’s Playbook</span>", "Answers from BytePlus’s Playbook</span>"),
 ("Answers come from GCash’s Playbook. It only says what GCash has confirmed.", "Answers come from BytePlus’s Playbook. It only says what BytePlus has confirmed."),
 ("['Magkano ang kailangan?','May ₱50 welcome credit ba?','Paano kung wala pa akong GCash?']:['May bayad ba mag-sign up?','May ₱50 welcome credit ba?','Paano kung wala pa akong GCash?']",
  "['Ilang free tokens ang makukuha ko?','Pwede ba sa ibang model?','Kailangan ba ng credit card?']:['May bayad ba mag-sign up?','Gaano kahaba ang video?','Kailangan ba ng credit card?']"),
 ("A.via==='ipon'?'Start saving on GCash':'Sign up on GCash'", "A.via==='ipon'?'Get an API key':'Sign up on BytePlus'"),
 ('aria-label="Leaving for GCash"', 'aria-label="Leaving for BytePlus"'),
 ("<b style=\"font-size:20px\">Opening GCash</b><span class=\"sub\">You’ll finish in the GCash app.", "<b style=\"font-size:20px\">Opening BytePlus</b><span class=\"sub\">You’ll finish on byteplus.com."),
 ("A.via==='ipon'?'GCash Ipon Challenge':'GCash Heroes'", "A.via==='ipon'?'BytePlus ModelArk Builders':'BytePlus Seedance Creators'"),
 ("Continue to GCash</button>", "Continue to BytePlus</button>"),
 # follower AI answers
 ("if(/welcome|credit|promo/.test(q))return inIpon?{t:'Wala pong welcome credit sa Ipon Challenge. Ang kailangan lang ay first deposit na ₱50 o higit pa sa GSave.',used:[['Ipon Challenge','pin']]}:{t:'Opo! New verified users get a ₱50 welcome credit, until 31 Oct.',used:[['Facts','half'],['Rules: say the end date','diamond']]};",
  "if(/credit card|card/.test(q))return{t:'Hindi ko pa po alam yan, kaya hindi ako manghuhula. Ipapasa ko sa BytePlus team.',used:[['Voice','petal']]};\n if(/free token|ilang|tokens/.test(q))return{t:'Sa bagong account po: 500,000 free tokens sa bawat language model, at 2,000,000 sa bawat vision model.',used:[['Facts','half'],['Rules: for new accounts only','diamond']]};"),
 ("if(inIpon&&/magkano|kailangan|minimum|deposit/.test(q))return{t:'₱50 lang po ang first deposit sa GSave. Pwede mo nang dagdagan kahit kailan.',used:[['Ipon Challenge','pin']]};",
  "if(/gaano|haba|long|seconds|video/.test(q))return{t:'Hanggang 30 seconds po bawat clip sa Seedance 2.5, at kaya nito ang higit 10 na wika.',used:[['Facts','half']]};\n if(inIpon&&/model|ibang/.test(q))return{t:'Opo. Iisang account lang po para sa mga model sa ModelArk, at may free tokens ang bawat isa pag bago ka.',used:[['Facts','half']]};"),
 ("Puwede mong sabihin: “Libre mag-join, at mabilis ang sign-up.”", "Puwede mong sabihin: “May free tokens ang bagong account, at isang prompt lang ang 30-second clip.”"),
 ("{t:'Libre po ang pag-join. Walang bayad.',used:[['Facts','half']]}", "{t:'Libre po ang sign-up, at may free tokens ang bagong account. Pag naubos, bayad ka lang sa ginagamit mo.',used:[['Facts','half']]}"),
 ("used:[['GCash Heroes','pin']]};\n if(/tiktok", "used:[['Seedance Creators','pin']]};\n if(/tiktok"),
 ("I-tag ang #GCashHeroes at i-on ang Paid partnership.',used:[['Rules: say it’s paid, tag it','diamond'],['GCash Heroes','pin']]}", "I-tag ang #SeedanceCreators, i-label na AI-made, at i-on ang Paid partnership.',used:[['Rules: say it’s paid, tag it','diamond'],['Seedance Creators','pin']]}"),
 ("if(/gcash|wala|app|paano|how/.test(q))return{t:'I-download ang GCash app, i-verify ang number mo, tapos sundan ang link. Mga 5 minuto lang po.',used:[['GCash Heroes','pin']]};",
  "if(/wala|app|paano|how/.test(q))return{t:'Sundan ang link ni Ana, gumawa ng BytePlus account, tapos buksan ang Seedance. Isang prompt lang po para sa unang clip.',used:[['Seedance Creators','pin']]};"),
 ("{t:'Makakagamit ka ng GCash para magbayad, mag-ipon at magpadala. Libre ang sign-up.',used:[['GCash Heroes','pin']]}", "{t:'Free tokens sa bawat model para makagawa ng video, image at app gamit ang AI. Libre ang sign-up.',used:[['Facts','half']]}"),
 ("Ipapasa ko ito sa GCash team para masagot nang tama.", "Ipapasa ko ito sa BytePlus team para masagot nang tama."),
 # accept invite
 ("c.deal=`${peso(c.rate)} per passed post · ${peso(c.dep)} per first deposit`", "c.deal=`${peso(c.rate)} per passed post · ${peso(c.dep)} per first API call`"),
 ("{t:'You joined GCash Ipon Challenge',", "{t:'You joined BytePlus ModelArk Builders',"),
 ("<b>Joined.</b> Ipon is in Your campaigns.", "<b>Joined.</b> ModelArk Builders is in Your campaigns."),
 ("A.creditName=A.via==='ipon'?'GCash Ipon Challenge':'GCash Heroes'", "A.creditName=A.via==='ipon'?'BytePlus ModelArk Builders':'BytePlus Seedance Creators'"),
 ("x==='ipon'?'Ipon Story':'Heroes Reel'", "x==='ipon'?'Builders Story':'Seedance Reel'"),
 ("Ana hasn’t joined Ipon yet.", "Ana hasn’t joined ModelArk Builders yet."),
 # invite page and the per-first-deposit labels
 ("· ${peso(c.dep)} per first deposit", "· ${peso(c.dep)} per first API call"),
 ("<span>Per first deposit</span>", "<span>Per first API call</span>"),
 ("Help students start saving with ₱50. ${esc(c.why)}", "Help new builders make their first API call. ${esc(c.why)}"),
 ("You stay in GCash Heroes too.", "You stay in Seedance Creators too."),
 # coach and posts headers
 ("Answers from GCash’s Playbook and your campaigns.", "Answers from BytePlus’s Playbook and your campaigns."),
 ("Answers come from GCash’s Playbook, and each one says which part it used.", "Answers come from BytePlus’s Playbook, and each one says which part it used."),
 ("Every post is checked against GCash’s Playbook", "Every post is checked against BytePlus’s Playbook"),
 ("Always true for GCash", "Always true for BytePlus"),
]
missing=[]
for o,n in R:
    if o not in src: missing.append(o)
    src=src.replace(o,n)
# what's left that names the brand, other than the payout wallet
left=[m for m in re.findall(r".{0,40}(?:GCash|Ipon|GSave|Heroes).{0,40}",src) if not re.search(r"Claim to GCash|your GCash|GCash · 0917|in your GCash|to your GCash|GCash on Friday",m)]
open('earner-byteplus.html','w').write(src)
print('missing:',len(missing)); [print('  -',m[:90]) for m in missing]
print('left:',len(left)); [print('  ·',l) for l in left]
