"""Builds onboard-byteplus.html from onboard.html: the same nine-step intake, with BytePlus
as the brand being read. Its last step opens console-byteplus.html, so the demo stays on
one brand from intake to console to earner.
Sourced (byteplus.com/en/product/modelark, read 5 Oct 2026): new accounts get 500,000 free
tokens per language model and 2,000,000 per vision model; Seedance makes 30-second clips.
Invented for the demo: the audience splits, the voice lines a and c, the rules and page numbers.
Run: python3 tools/make-byteplus-onboard.py  (from prototypes/)"""
import re
src = open('onboard.html').read()

WHO = '''const WHO = [["savers", "Video creators and small studios", "Seedance sign-ups grew most in this group", "BYTEPLUS.COM/MODELARK"], ["sellers", "Developers and startups", "Your docs pages talk to them most", "DOCS.BYTEPLUS.COM"], ["ofw", "Marketing teams at small businesses", "Solution pages, but not much recent content", "BYTEPLUS.COM/SOLUTIONS"], ["students", "Students learning to code", "Builder posts do well with them", "LINKEDIN, 40 POSTS"]];'''
VOICES = '''const VOICES = [["a", "“Isang prompt, 30 seconds. Ito yung ginawa ko!”", "Show-and-tell Taglish", "FROM YOUR LINKEDIN POSTS"], ["b", "“Powering your AI, from dev to growth.”", "Clear and direct", "FROM BYTEPLUS.COM"], ["c", "“Kaya mo ’yan! Your first clip is one prompt away.”", "Cheerful coach", "FROM THE SEEDANCE LAUNCH"]];'''
RULES = '''const RULES = [["r3", "Never", "#ff8787", "Say the free tokens never run out", "COMPLIANCE MEMO, P.2"], ["r4", "Never", "#ff8787", "Use real faces or famous characters without permission", "BRAND BOOK 2026, P.31"], ["r9", "Careful", "#ffd43b", "Comparing models: only numbers BytePlus published", "COMPLIANCE MEMO, P.3"], ["r12", "Always", "#8f8a80", "Say it’s paid: “Paid partnership with BytePlus”", "BRAND BOOK 2026, P.34"], ["r13", "Always", "#8f8a80", "Write BytePlus as one word, never “Byte Plus”", "BRAND BOOK 2026, P.4"], ["r14", "Never", "#ff8787", "Show real API keys or account IDs", "GUESS FROM YOUR POSTS"]];'''
BLENDS = '''    const blends = { 'a': '“Isang prompt, 30 seconds. Ito yung ginawa ko!”', 'b': '“Powering your AI, from dev to growth.”', 'c': '“Kaya mo ’yan! Your first clip is one prompt away.”',
      'a,b': '“Isang prompt, 30 seconds. From dev to growth, iisang account.”', 'a,c': '“Isang prompt, 30 seconds. Kaya mo ’yan, try mo na!”', 'b,c': '“From dev to growth. Kaya mo ’yan, one prompt away!”' };'''

lines = src.split('\n')
def setline(prefix, new, n=1):
    i = next(k for k, l in enumerate(lines) if l.lstrip().startswith(prefix))
    lines[i:i+n] = new.split('\n')
setline('const WHO =', WHO)
setline('const VOICES =', VOICES)
setline('const RULES =', RULES)
setline('const blends =', BLENDS, 2)
src = '\n'.join(lines)

R = [
 ('<title>OkPo Onboarding</title>', '<title>OkPo Onboarding · BytePlus</title>'),
 ('console.html#first', 'console-byteplus.html#first'),
 # step 2: sources
 ('>Reading gcash.com<', '>Reading byteplus.com<'),
 ('>gcash.com<', '>byteplus.com<'),
 ('>gcash.com/gsave<', '>byteplus.com/en/product/modelark<'),
 ('>gcash.com/gcredit<', '>docs.byteplus.com<'),
 ('>Facebook page, last 40 posts<', '>LinkedIn page, last 40 posts<'),
 ('>App Store listing<', '>Discord announcements<'),
 # the book
 ('An e-wallet for sending, paying and saving, from your phone.', 'An AI cloud: models for video, images and code, from one account.'),
 ('An e-wallet for sending, paying and saving. More first-time savers, please.', 'An AI cloud for video, images and code. More video creators, please.'),
 ('>Send money, pay bills, save, cash in<', '>Seedance video, Seedream images, Seed models for code<'),
 ('Sari-sari store owners, then first-time users', 'Video creators and small studios, then developers'),
 ('>“Libre lang mag-join, mga 5 minuto.”<', '>“Isang prompt, 30 seconds.”<'),
 ('>Blue and white, real people, bright daylight<', '>Real outputs on screen, the console, no stock footage<'),
 ('>No approval promises, no fee comparisons, don’t lead with loans<', '>No endless-free claims, no borrowed faces, only our own numbers<'),
 # check 3: the sensitive fact
 ('I won’t say anything about credit until someone confirms it.', 'I won’t say anything about free tokens until someone confirms it.'),
 ('>Anyone 21 and up with a verified account can apply for GCredit.<', '>New accounts get 500,000 free tokens per language model and 2,000,000 per vision model.<'),
 ('FOUND ON GCASH.COM/GCREDIT · READ TODAY', 'FOUND ON BYTEPLUS.COM/EN/PRODUCT/MODELARK · READ TODAY'),
 # step 5: sample post
 ('>ana.ipon<', '>ana.posts<'),
 ('>Nag-start ako mag-ipon sa GSave, ₱50 lang muna. Libre lang mag-join, mga 5 minuto. Kaya mo ’yan! Tara, ipon tayo. <',
  '>Isang prompt, 30 seconds na clip. Ito yung ginawa ko sa Seedance. May free tokens pag bago ang account mo, kaya mo ’yan! <'),
 ('value="gcash.com"', 'value="byteplus.com"'),
 ('>#GCash<', '>#SeedanceCreators<'),
 ('GSave, first-time savers', 'Seedance, video creators'),
 # live console preview (the book card)
 ('>Warm Taglish, short lines. A friend who’s good with money, never preachy.<', '>Taglish, short lines. A friend showing what they made, never hype.<'),
 ('>No loan promises, no fee fights, credit never first. Always say it’s paid.<', '>No endless-free claims, no borrowed faces, our numbers only. Always say it’s paid.<'),
 ('>GSave: savings with partner banks<', '>Seedance: a 30-second clip from one prompt<'),
 ('>First-time savers, small sellers<', '>Video creators, developers<'),
 ('>Credit<', '>Free tokens<'),
 ('>GCredit for verified users 21 and up<', '>For new accounts, per model<'),
 ('>Fees and verification times. I stay quiet until someone confirms.<', '>Pricing after the free tokens, and which regions. I stay quiet until someone confirms.<'),
 # voice
 ('Talk like a friend helping, not a bank announcing.', 'Talk like a friend showing what they made, not a vendor announcing.'),
 ('Cheer the saving habit; never lecture about money.', 'Cheer the first try; never lecture about AI.'),
 ('“Secure your financial future with best-in-class solutions.”', '“Unlock next-generation AI with best-in-class solutions.”'),
 ('SOUNDS LIKE GCASH', 'SOUNDS LIKE BYTEPLUS'),
 # rules page
 ('>Promise approval, loan amounts or dates<', '>Say the free tokens never run out<'),
 ('>✕ “Approved ka agad!”<', '>✕ “Unlimited free tokens!”<'),
 ('>Compare fees with other wallets<', '>Use real faces or famous characters<'),
 ('>✕ “Mas mura kaysa sa iba”<', '>✕ A celebrity’s face in the clip<'),
 ('>Show real balances or QR codes<', '>Show real API keys<'),
 ('>Loans and credit<', '>Comparing models<'),
 ('>Only after the main message, never in the hook.<', '>Only with numbers BytePlus published.<'),
 ('>Write GCash in full<', '>Write BytePlus as one word<'),
 ('>Never “G-Cash” or “Gcash”.<', '>Never “Byte Plus” or “Byteplus”.<'),
]
missing = []
for o, n in R:
    if o not in src: missing.append(o)
    src = src.replace(o, n)
# the brand tile and every remaining brand name
src = re.sub(r'(>)G(</span>)', r'\1B\2', src)
src = src.replace('GCash', 'BytePlus')
left = re.findall(r'.{0,50}(?:GCash|gcash|GCASH|GSave|GCredit|Ipon|ipon|e-wallet|loan).{0,50}', src)
open('onboard-byteplus.html', 'w').write(src)
print('missing:', len(missing)); [print('  -', m[:90]) for m in missing]
print('left:', len(left)); [print('  ·', l) for l in left]
