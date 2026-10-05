"""Builds console-byteplus.html from console.html: the same brand console, with BytePlus as
the brand and two campaigns that match the earner copy (earner-byteplus.html):
  heroes -> BytePlus Seedance Creators (short Seedance), paid per sign-up that makes a first clip
  save   -> BytePlus ModelArk Builders (short Builders), paid per first API call
Earner payouts still say GCash (that is OkPo's payout rail, not the brand).
Sourced (byteplus.com/en/product/modelark, read 5 Oct 2026): free tokens for new accounts,
500,000 per language model and 2,000,000 per vision model; Seedance 2.5 makes a clip up to
30 seconds, takes up to 50 reference files, works in more than 10 languages.
Invented for the demo: the launch promo, sign-up requirements, audiences, rules, page numbers.
Run: python3 tools/make-byteplus-console.py  (from prototypes/)"""
import re
src = open('console.html').read()

def block(pattern, new):
    global src
    n = len(re.findall(pattern, src, flags=re.S))
    if n != 1: print('BLOCK', n, pattern[:60])
    src = re.sub(pattern, lambda m: new, src, count=1, flags=re.S)

# ---------- FRESH state ----------
block(r"wiz:\{step:0,name:'GCash Heroes · Wave 2'.*?hook:'[^']*'\}",
 "wiz:{step:0,name:'BytePlus Seedance Creators · Wave 2',goal:3000,post:40,act:12,pool:50000,cap:120,reviewer:'ai',ends:'2026-11-30',hook:'Free tokens for new accounts. Your first clip from one prompt.'}")
block(r"followers:\[[^\]]*\],topics:\[[^\]]*\],nos:\[[^\]]*\]",
 "followers:['Video creators','Small studios','Students learning to code','Developers','Metro Manila'],topics:['AI edits','Short video','Tech'],nos:['Active deal with another AI brand','Deepfakes of real people','Under 18']")
KNOW = """know:[{g:'Campaign facts',t:'Joining BytePlus Seedance Creators is free. No fees to sign up or to stay in.',src:'Seedance deck, slide 4',st:'ok',n:'Checked by Marga, 28 Sep'},{g:'Campaign facts',t:'Seedance launch promo: double free tokens for new accounts.',src:'Seedance deck, slide 9',st:'exp',n:'Ends 31 Oct. The AI stops saying it after.'},{g:'Compliance',t:'[Approved wording for pricing after the free tokens. To confirm with BytePlus legal.]',src:'Waiting on legal',st:'need',n:'Needs a check before publishing'},{g:'Products and offers',t:'Sign-up needs an email and a phone number. Takes about 5 minutes.',src:'docs.byteplus.com',st:'ok',n:'Checked by Marga, 28 Sep'},{g:'Audience',t:'First target: video creators and small studios in Metro Manila, 18 to 30.',src:'Seedance deck, slide 2',st:'need',n:'The deck says 18 to 26'},{g:'Voice',t:'Show-and-tell, short, Taglish. Two or three sentences. Say “po” when the other person does.',src:'Voice guide, p.2',st:'ok',n:'Checked by Marga, 28 Sep'},{g:'Don’t say',t:'Never say the free tokens never run out.',src:'Voice guide, p.6',st:'ok',n:'Checked by Marga, 28 Sep'},{g:'Don’t say',t:'Don’t compare with other AI models, except with numbers BytePlus published.',src:'Voice guide, p.6',st:'need',n:'Needs a check'},{g:'Products and offers',t:'Seedream makes images from a prompt. [Resolution wording to confirm.]',src:'byteplus.com',st:'need',n:'Needs a check'},
  {g:'Company',t:'An AI cloud: models for video, images and code, from one account.',src:'byteplus.com',st:'ok',n:'Confirmed at onboarding'},
  {g:'Products and offers',t:'Seedance 2.5 makes a single clip up to 30 seconds long.',src:'byteplus.com/en/product/modelark',st:'ok',n:'Sourced, read at onboarding'},
  {g:'Products and offers',t:'Seedance takes up to 50 reference files and works in more than 10 languages.',src:'byteplus.com/en/product/modelark',st:'ok',n:'Sourced, read at onboarding'},
  {g:'Products and offers',t:'ModelArk: many models from one account, through one API.',src:'byteplus.com/en/product/modelark',st:'ok',n:'Sourced, read at onboarding'},
  {g:'Products and offers',t:'Free tokens for new accounts: 500,000 per language model, 2,000,000 per vision model.',src:'byteplus.com/en/product/modelark',st:'ok',n:'Confirmed at onboarding (sensitive)'},
  {g:'Products and offers',t:'Seed models for code, through the same API.',src:'docs.byteplus.com',st:'ok',n:'Sourced, read at onboarding'},
  {g:'Audience',t:'Who buys: video creators and small studios, then developers.',src:'byteplus.com',st:'ok',n:'Confirmed at onboarding'},
  {g:'Audience',t:'Who we want more of: video creators and developers.',src:'Picked at onboarding',st:'ok',n:'Confirmed at onboarding'},
  {g:'Company',t:'Docs and API reference at docs.byteplus.com.',src:'docs.byteplus.com',st:'ok',n:'Sourced, read at onboarding'},
  {g:'Company',t:'Launches are announced on Discord first.',src:'Discord announcements',st:'ok',n:'Sourced, read at onboarding'}],"""
block(r"know:\[\{g:'Campaign facts'.*?\}\],\n", KNOW + "\n")
block(r"angles:\[\{n:'Free to join'.*?\}\],",
 "angles:[{n:'Free tokens to start',d:'Leads with “free tokens”, for new accounts',p:45},{n:'A 30-second clip, one prompt',d:'Show the clip being made on screen',p:30},{n:'Show what you made',d:'Your clip and the prompt behind it',p:25}],")
block(r"gaps:\[\{q:.*?\}\],",
 "gaps:[{q:'Pwede ba sa Facebook Reels?',n:34,w:'influencers'},{q:'Kailan lalabas ang bayad?',n:21,w:'influencers'},{q:'Kailangan ba ng credit card?',n:18,w:'followers'},{q:'May student discount ba?',n:9,w:'followers'}],")

# ---------- ensureDir and saved defaults ----------
R = [
 ("okpo-console5", "okpo-console5-byteplus"),
 ('<title>OkPo Brand Console</title>', '<title>OkPo Brand Console · BytePlus</title>'),
 ('<span class="gdot">G</span>', '<span class="gdot">B</span>'),
 ('font-size:11px">G</span>', 'font-size:11px">B</span>'),
 ("const CAMPS={heroes:{name:'GCash Heroes',short:'Heroes'},save:{name:'GCash Ipon Challenge',short:'Ipon Challenge'}};",
  "const CAMPS={heroes:{name:'BytePlus Seedance Creators',short:'Seedance'},save:{name:'BytePlus ModelArk Builders',short:'Builders'}};"),
 ("n:'Point people to the app',t:'Every post ends in the GCash app sign-up, not the website.'", "n:'Point people to the sign-up',t:'Every post ends on the BytePlus sign-up page, through your own link.'"),
 ("t:'Record the actual app. No slides or stock video.'", "t:'Record the actual Seedance or ModelArk page. No slides or stock video.'"),
 ("guards:['Never lead with loans or credit.','Never compare fees with other wallets.',", "guards:['Never say the free tokens never run out.','Never compare with other AI models, except with numbers BytePlus published.',"),
 ("[{n:'Start with ₱50',d:'Show a first deposit, start to finish',p:50},{n:'Goals for students',d:'Saving for a phone, a trip or tuition',p:30},{n:'Watch it grow',d:'Open the app a week later',p:20}]",
  "[{n:'Your first API call',d:'Show the key, the call and the answer, start to finish',p:50},{n:'Build for school',d:'A study helper, a chat bot or a small app',p:30},{n:'Build it all free',d:'A whole app on the free tokens',p:20}]"),
 ("save:{d3:'₱25 per passed post, ₱10 per first deposit of ₱50 or more.'}", "save:{d3:'₱25 per passed post, ₱10 per first API call from a new account.'}"),
 ("t:'Warm Taglish, short lines',d:'Two or three sentences. Say “po” when the other person does.',ex:'“Libre lang mag-join, mga 5 minuto.”'",
  "t:'Show-and-tell Taglish, short lines',d:'Two or three sentences. Say “po” when the other person does.',ex:'“Isang prompt, 30 seconds.”'"),
 ("t:'A friend who’s good with money',d:'Practical and kind. Never preachy, no jargon.',ex:'“Ganito ako nag-iipon, sana makatulong.”'",
  "t:'A friend showing what they made',d:'Practical and excited. Never hype, no jargon.',ex:'“Ito yung prompt ko, try mo rin.”'"),
 ("d:'The actual app on screen, real people, daylight.',ex:'A screen recording, not a slide.',src:'gcash.com/about · read by OkPo'",
  "d:'The actual console on screen, real outputs, real people.',ex:'A screen recording, not a slide.',src:'byteplus.com · read by OkPo'"),
 ("t:'Blue and white, bright daylight',d:'GCash blue on white. Shot outside or by a window, never in a dark room.',ex:'A Reel filmed at a sari-sari store counter at noon.'",
  "t:'Real outputs, no stock footage',d:'The clip or the answer you made, shown in full. Never stock video or a mock screen.',ex:'A Reel that cuts from the prompt to the finished clip.'"),
 ("/GCash Heroes|welcome credit/", "/Seedance Creators|launch promo/"),
 ("t:'Ipon Challenge: a first deposit of ₱50 or more into GSave counts. No minimum after that.',src:'Ipon brief, p.1'",
  "t:'ModelArk Builders: a first API call from a new account counts. One per account.',src:'Builders brief, p.1'"),
 # rules
 ("{id:'R-03',k:'never',t:'Promise approval, loan amounts or dates',ty:'Must not',sev:'fail',sc:'brand',look:'Spoken words, caption, on-screen text',ap:'Posts, coach, Ask AI',src:'Voice guide, p.6',pass:'“Libre mag-join, mga 5 minuto lang.”',fail:'“Sure approval ’to, promise!”'",
  "{id:'R-03',k:'never',t:'Say the free tokens never run out',ty:'Must not',sev:'fail',sc:'brand',look:'Spoken words, caption, on-screen text',ap:'Posts, coach, Ask AI',src:'Voice guide, p.6',pass:'“May free tokens pag bago ang account mo.”',fail:'“Unlimited free tokens, forever!”'"),
 ("{id:'R-04',k:'never',t:'Compare fees with other wallets',ty:'Must not',sev:'fail',sc:'brand',look:'Spoken words, caption',ap:'Posts, coach, Ask AI',src:'Voice guide, p.6',pass:'“Send to any bank from the app.”',fail:'“Mas mura pa kaysa sa iba!”'",
  "{id:'R-04',k:'never',t:'Use a real person’s face or a famous character without permission',ty:'Must not',sev:'fail',sc:'brand',look:'On screen',ap:'Posts, coach, Ask AI',src:'Voice guide, p.6',pass:'An original character, or your own face.',fail:'A celebrity’s face in the clip.'"),
 ("t:'Show the real GCash app, not slides or screenshots'", "t:'Show the real BytePlus console, not slides or screenshots'"),
 ("pass:'Screen recording of the app.'", "pass:'Screen recording of the console.'"),
 ("t:'Say it’s free to join',ty:'Must',sev:'fix',sc:'heroes',look:'Spoken words, caption',ap:'Posts',src:'Heroes deck, slide 4',pass:'“Libre lang mag-join.”',fail:'No mention of cost.'",
  "t:'Say the free tokens are for new accounts',ty:'Must',sev:'fix',sc:'heroes',look:'Spoken words, caption',ap:'Posts',src:'Heroes deck, slide 4',pass:'“Free tokens pag bago ang account.”',fail:'No mention of who gets them.'"),
 ("t:'End on the app sign-up, not the website'", "t:'End on the sign-up page, through your link'"),
 ("pass:'Ends on the sign-up screen.',fail:'Sends people to gcash.com.'", "pass:'Ends on the sign-up page.',fail:'Ends on the clip, no sign-up.'"),
 ("t:'Loans and credit: only after the main message, never in the hook',ty:'Must not',sev:'fail',sc:'brand',look:'Spoken words, caption',ap:'Posts, coach, Ask AI',src:'Compliance memo, p.2',pass:'Leads with joining; GLoan comes later.',fail:'Opens on GLoan.'",
  "t:'Comparing with other AI models: only with numbers BytePlus published',ty:'Must not',sev:'fail',sc:'brand',look:'Spoken words, caption',ap:'Posts, coach, Ask AI',src:'Compliance memo, p.2',pass:'Quotes a number from byteplus.com.',fail:'“Mas magaling pa sa lahat ng model!”'"),
 ("pass:'gcash.com/heroes?ref=ana',fail:'A plain gcash.com link.'", "pass:'byteplus.com/seedance?ref=ana',fail:'A plain byteplus.com link.'"),
 ("t:'The ₱50 welcome credit: only until 31 Oct'", "t:'The launch promo: only until 31 Oct'"),
 ("pass:'Before 31 Oct: “₱50 welcome credit.”'", "pass:'Before 31 Oct: “Double free tokens sa Seedance.”'"),
 ("t:'Show real account balances or QR codes',ty:'Must not',sev:'fail',sc:'brand',look:'On screen',ap:'Posts',src:'Read from your posts, confirmed at onboarding',pass:'A sample screen or a blurred balance.',fail:'A real balance on screen.'",
  "t:'Show real API keys or account IDs',ty:'Must not',sev:'fail',sc:'brand',look:'On screen',ap:'Posts',src:'Read from your posts, confirmed at onboarding',pass:'A blurred key or a sample screen.',fail:'A real API key on screen.'"),
 ("t:'Write GCash in full',ty:'Must',sev:'fix',sc:'brand',look:'Caption, on-screen text',ap:'Posts, coach, Ask AI',src:'Brand book 2026, p.4',pass:'“GCash”',fail:'“G-Cash” or “Gcash”.'",
  "t:'Write BytePlus as one word',ty:'Must',sev:'fix',sc:'brand',look:'Caption, on-screen text',ap:'Posts, coach, Ask AI',src:'Brand book 2026, p.4',pass:'“BytePlus”',fail:'“Byte Plus” or “Byteplus”.'"),
 ("t:'Shows a screenshot, not the live app.'", "t:'Shows a screenshot, not the live console.'"),
 ("/loan|credit|utang|borrow/i", "/never run out|unlimited|forever|walang limit/i"),
 ("/cheaper than|compare|vs\\.?\\s|than maya|other wallets/i", "/better than|compare|vs\\.?\\s|than gpt|other models/i"),
 # posts and recruiting
 ("'Shows the sign-up in 14 seconds','Says it’s free to join'", "'Shows the clip being made in 14 seconds','Says the free tokens are for new accounts'"),
 ("'Says “sure approval” (not allowed)'", "'Says “unlimited free tokens” (not allowed)'"),
 ("'Shows the sign-up','Says it’s free to join'", "'Shows the clip being made','Says the free tokens are for new accounts'"),
 ("'Shows the sign-up','Tags present'", "'Shows the clip being made','Tags present'"),
 ("t:'Food and budget · QC'", "t:'AI edits and food · QC'"),
 ("t:'Student food · Cebu'", "t:'Student tech · Cebu'"),
 ("{h:'@rhea.budget',av:'RB',s:'Open call',t:'Ipon tips · Davao'", "{h:'@rhea.builds',av:'RB',s:'Open call',t:'AI side projects · Davao'"),
 ("@rhea.budget", "@rhea.builds"),
 ("t:'Crypto and loans',m:41,pick:false,flag:'Hard no: loan promos'", "t:'Face-swap videos',m:41,pick:false,flag:'Hard no: deepfakes'"),
 ("t:'Budget · Bacolod'", "t:'Short video · Bacolod'"),
 ("{h:'@ivy.ipon',av:'II',s:'Open call',t:'Ipon challenges · Iloilo'", "{h:'@ivy.builds',av:'IB',s:'Open call',t:'Coding for school · Iloilo'"),
 ("t:'Tipid tips · Cebu'", "t:'AI tools on a budget · Cebu'"),
 ("'Followers mostly in Visayas'", "'Followers mostly in Metro Manila'"),
 ("'No active e-wallet or loan deals'", "'No active deals with other AI brands'"),
 # leads
 ("d:'Already had GCash'", "d:'Already had a BytePlus account'"),
 ("'Duplicate: already had GCash'", "'Duplicate: already had a BytePlus account'"),
 ("['ID not verified',27,", "['Email not verified',27,"),
 (". Most of the gap is people who already had GCash.", ". Most of the gap is people who already had a BytePlus account."),
 ("'Wed 1 Oct · first deposit ₱50'", "'Wed 1 Oct · first API call'"),
 ("'Wed 1 Oct · new customer, ID verified'", "'Wed 1 Oct · new account, email verified'"),
 ("'Thu 2 Oct · first transaction'", "'Thu 2 Oct · first clip made'"),
 # overview
 ("I answer fees and eligibility on my own now.", "I answer free tokens and sign-up on my own now."),
 # the book
 ("'Send money, pay bills, save, cash in'", "'Seedance video, Seedream images, Seed models for code'"),
 ("'Sari-sari store owners, then first-time users'", "'Video creators and small studios, then developers'"),
 ("'“Libre lang mag-join, mga 5 minuto.”','voice'", "'“Isang prompt, 30 seconds.”','voice'"),
 ("'Blue and white, real people, bright daylight'", "'Real outputs on screen, the console, no stock footage'"),
 ("'No approval promises, no fee comparisons, loans never first'", "'No endless-free claims, no borrowed faces, only our own numbers'"),
 ("An e-wallet for sending, paying and saving, from your phone.", "An AI cloud: models for video, images and code, from one account."),
 ("An e-wallet for sending, paying and saving. More first-time savers, please.", "An AI cloud for video, images and code. More video creators, please."),
 ("Warm Taglish, short lines, the real app in daylight. A friend who’s good with money, never preachy.", "Taglish, short lines, real outputs on screen. A friend showing what they made, never hype."),
 ("No approval promises, no fee fights, loans never first. Always say it’s paid.", "No endless-free claims, no borrowed faces, our numbers only. Always say it’s paid."),
 ("“Libre lang mag-join, mga 5 minuto. Ito yung ginawa ko.”", "“Isang prompt, 30 seconds. Ito yung ginawa ko.”"),
 # brief lines
 ("['Say it’s free to join. No promises on amounts.',", "['Say the free tokens are for new accounts. No promises on amounts.',"),
 ("['Show the Heroes sign-up in under 20 seconds.',", "['Show the clip being made in under 20 seconds.',"),
 ("['Talk about sending money home to family.',", "['Show the clip you made and the prompt behind it.',"),
 ("['End on the app sign-up, not the website.',", "['End on the sign-up page, through your link.',"),
 ("['Don’t promise approval, amounts or dates.',", "['Don’t say the free tokens never run out.',"),
 # try it
 ("Ask about the ₱50 welcome credit in both to see the difference.", "Ask about the launch promo in both to see the difference."),
 ("['Pwede bang sabihing sure approval?','May welcome credit ba?','Ilan ang minimum na deposit?']", "['Pwede bang sabihing unlimited ang free tokens?','May launch promo ba?','Ano ang first API call?']"),
 ("['May bayad ba mag-sign up?','May ₱50 promo ba?','Paano kung wala akong ID?']", "['May bayad ba mag-sign up?','May promo ba sa Seedance?','Kailangan ba ng credit card?']"),
 ("if(/welcome|credit|promo|₱50/.test(q)){const c=okCard(/welcome credit/),o=other(/welcome credit/);", "if(/promo|launch|double/.test(q)){const c=okCard(/launch promo/),o=other(/launch promo/);"),
 ("{t:'Opo! New verified users get a ₱50 welcome credit, until 31 Oct.',used:['Facts · Heroes only','Voice'],why:['Fact in scope: GCash Heroes only',",
  "{t:'Opo! Sa bagong account po, double free tokens sa Seedance hanggang 31 Oct.',used:['Facts · Seedance only','Voice'],why:['Fact in scope: Seedance Creators only',"),
 ("const ip=okCard(/first deposit/);return{t:ip?'Sa Ipon Challenge po, ang nagbibilang ay ang first deposit na ₱50 o higit pa sa GSave. Wala pong welcome credit dito.'",
  "const ip=okCard(/first API call/);return{t:ip?'Sa ModelArk Builders po, ang nabibilang ay ang first API call gamit ang bagong account. Walang launch promo dito.'"),
 ("used:ip?['Facts · Ipon only']", "used:ip?['Facts · Builders only']"),
 ("'Skipped a GCash Heroes fact: the welcome credit isn’t part of Ipon Challenge'", "'Skipped a Seedance Creators fact: the launch promo isn’t part of ModelArk Builders'"),
 ("'Answered from Ipon’s own fact instead'", "'Answered from Builders’ own fact instead'"),
 ("if(/ipon|deposit|gsave|ilan|minimum/.test(q)){const c=okCard(/first deposit/);if(c)return{t:'Mag-deposit ka lang po ng ₱50 o higit pa sa GSave. Yun ang first deposit na nabibilang.',used:['Facts · Ipon only'],why:['Fact in scope: Ipon Challenge only','Fact: ₱50 or more into GSave',",
  "if(/api|call|modelark|minimum|key/.test(q)){const c=okCard(/first API call/);if(c)return{t:'Gumawa ka lang po ng API key at mag-send ng unang request. Yun ang first API call na nabibilang.',used:['Facts · Builders only'],why:['Fact in scope: ModelArk Builders only','Fact: a first API call from a new account',"),
 ("{t:'Wala pa po akong sagot dito para sa GCash Heroes. Ipapasa ko sa team.',used:['Voice'],why:['Skipped an Ipon Challenge fact: it isn’t part of GCash Heroes',",
  "{t:'Wala pa po akong sagot dito para sa Seedance Creators. Ipapasa ko sa team.',used:['Voice'],why:['Skipped a ModelArk Builders fact: it isn’t part of Seedance Creators',"),
 ("if(/sure|approval|guarantee/.test(q))return{t:'Hindi po natin puwedeng sabihin yan. Puwede mong sabihin: “Libre mag-join, at mabilis ang sign-up.”'",
  "if(/unlimited|forever|sure|guarantee/.test(q))return{t:'Hindi po natin puwedeng sabihin yan. Puwede mong sabihin: “May free tokens pag bago ang account mo.”'"),
 ("why:['Rule: never promise approval','Fact: joining is free',", "why:['Rule: never say the free tokens never run out','Fact: free tokens are for new accounts',"),
 ("if(/bayad|magkano|fee/.test(q))return{t:'Libre po ang pag-join. Kailangan mo lang ng mobile number at isang valid ID, mga 5 minuto.',used:['Facts','Facts'],why:['Rules: nothing to flag','Fact: free, mobile number and one ID',",
  "if(/bayad|magkano|fee|libre|free/.test(q))return{t:'Libre po mag-sign up. Sa bagong account, 500,000 free tokens sa bawat language model at 2,000,000 sa bawat vision model.',used:['Facts','Rules · Always'],why:['Rule: say the free tokens are for new accounts','Fact: free tokens per model, new accounts',"),
 ("if(/id/.test(q))return{t:'Kailangan po ng isang valid ID para ma-verify. Pwede mong simulan ngayon at tapusin pag may ID ka na.',used:['Facts'],why:['Rules: nothing to flag','Fact: one valid ID needed','Voice: warm, “po”','Talking point: keep them in the sign-up']};",
  "if(/card|credit/.test(q))return{t:'Hindi ko pa po alam yan, kaya hindi ako manghuhula. Ipapasa ko sa BytePlus team.',used:['Voice'],why:['Not in the Playbook, so it won’t guess','Fact: none on cards yet','Voice: honest hand-off','Logged to Suggestions as a question']};"),
 # actions: draft rule, campaign rule, clash
 ("t:'Promise returns or interest on savings'", "t:'Promise what the free tokens will build'"),
 ("pass:'“Start with ₱50 and watch it add up.”',fail:'“Kikita ka ng 5% agad!”'", "pass:'“Start free, then see what it costs.”',fail:'“Buong app, libre lahat!”'"),
 ("'Rules: never promise returns or interest'", "'Rules: never promise what free tokens build'"),
 ("'Show the ₱50 going into GSave on screen'", "'Show the first API call and its answer on screen'"),
 ("'The deposit screen is shown.'", "'The call and its answer are shown.'"),
 ("'Show the sign-up within 20 seconds'", "'Show the clip being made within 20 seconds'"),
 ("'Sign-up appears at 0:40.'", "'The clip appears at 0:40.'"),
 ("Talking point “Watch it grow” leans on interest earned.", "Talking point “Build it all free” says the free tokens cover a whole app."),
 ("never promise returns or interest on savings", "never promise what the free tokens will build"),
 ("'Reword it: “Open the app a week later and see your savings”',to:'Open the app a week later and see your savings'",
  "'Reword it: “Start free, then see what it costs”',to:'Start free, then see what it costs'"),
 ("Watch it grow", "Build it all free"),
 ("'Pause “Send money home” for students'", "'Pause “Show what you made” for developers'"),
 ("'Lowest activation for 18 to 22. Keep it for first-jobbers.'", "'Lowest activation with developers. Keep it for video creators.'"),
 ("a.d='For first-jobbers only'", "a.d='For video creators only'"),
 ("“Send money home” is for first-jobbers only.", "“Show what you made” is for video creators only."),
 # angle names, everywhere (match the earner copy)
 ("Free to join", "Free tokens to start"),
 ("Five-minute sign-up", "A 30-second clip, one prompt"),
 ("Send money home", "Show what you made"),
 # kinds and money words
 ("'first deposits'", "'first API calls'"),
 ("first deposit", "first API call"),
 ("activated GCash accounts", "activated BytePlus accounts"),
 ("welcome credit", "launch promo"),
]
missing = []
for o, n in R:
    if o not in src: missing.append(o)
    src = src.replace(o, n)

# payouts go to the earner's GCash wallet: keep those, rename the brand everywhere else
KEEP = ['paid Fridays to GCash', ' · to GCash<']
for i, k in enumerate(KEEP): src = src.replace(k, f'@@KEEP{i}@@')
for o, n in [('#GCashHeroes', '#SeedanceCreators'), ('#IponChallenge', '#ModelArkBuilders'),
             ('GCash Heroes', 'BytePlus Seedance Creators'), ('GCash Ipon Challenge', 'BytePlus ModelArk Builders'),
             ('Ipon Challenge', 'ModelArk Builders'), ('Ipon', 'Builders'), ('Heroes', 'Seedance'),
             ('GCash', 'BytePlus'), ('gcash.com', 'byteplus.com')]:
    src = src.replace(o, n)
for i, k in enumerate(KEEP): src = src.replace(f'@@KEEP{i}@@', k)

left = [m for m in re.findall(r".{0,50}(?:GCash|GSave|GCredit|GLoan|ipon|e-wallet|loan|deposit|sari-sari|₱50).{0,50}", src)
        if not any(k in m for k in KEEP)]
open('console-byteplus.html', 'w').write(src)
print('missing:', len(missing)); [print('  -', m[:100]) for m in missing]
print('left:', len(left)); [print('  ·', l) for l in left]
