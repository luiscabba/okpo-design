# OkPo design system, for AI coders

Read this before you write any OkPo UI. It describes the system **as the working prototypes build it** (`prototypes/console.html`, `setup.html`, `earner.html`, `lobby.html`, `connected.html`), audited on 2 Oct 2026. If this file and a prototype disagree, this file wins, and the prototype is due a fix. If a screen you are asked to build breaks a rule here, follow this file and say so in your summary.

Status words:

- **Locked**: Luis decided it and it stays closed. Build it this way. Do not suggest alternatives, redesigns or "small improvements" to it, and do not raise it in reviews. It reopens only when Luis says so in so many words. Everything that was Settled became Locked on 2 Oct 2026.
- **On trial**: in use and kept for now. Do not change it; Luis will call it.
- **Open**: build the current default, keep it easy to change, and do not invent a new answer.

### Locked register (2 Oct 2026)

Review time goes to flow and usability, not to these:

| Area | What is locked | Where |
|---|---|---|
| Registers | Marketing art is hand-drawn, marketing controls are crisp yellow; product is crisp glass with an ink main button | §2 |
| Tokens | Glazes, label shades, neutrals, status tints, type, glass, radius, light first | §3 |
| Wordmark | OkPo, four glazes, 20px minimum, all four letters or none | §4 |
| Backdrop | Three crisp tone tiles, fixed placement, never moves | §5 |
| Icons | Six tiles, the line-icon set, avatars and monograms, nothing invented | §6 |
| Section tiles | One tile per section and tab | §6 |
| Layout | Console shell, phone shell, Lobby wrap, screen header | §7 |
| Tab titles | `.big` 26px on every earner tab | §7 |
| Components | Everything in §8 | §8 |
| Motion | The five curves, the durations, the takeover, the banner, the console moments | §9 |
| Vocabulary | Fact, Voice, Rule, Talking point, Brand context | §10 |
| Brand setup | The console's new-brand flow, full screen, one question per screen | §10 |
| Voice | Chrome in second person, OkPo's guide in first person, the AI in third person | §11 |
| Copy | Names from data, button and toast shapes, money format, no em dashes | §11 |

On trial: frame and coral for Overview and Today (§6). Open: the Lobby's register (§2), Luis to review.

The golden rule for new screens: **reuse a pattern that already exists in a prototype before inventing one.** No new icons, badges, marks or shortened wordmarks. Visuals come from the six tiles, the line-icon set in §6, and the full wordmark.

---

## 1. What OkPo is

OkPo trains AI to train a brand's influencers. Three surfaces share one state:

| Surface | Who | Job | Prototype |
|---|---|---|---|
| **Brand console** | Brand marketing manager, OkPo team | Brand context, campaigns, recruiting, posts, leads, pool | `console.html` |
| **Earner app** | Influencers ("earners", e.g. Ana) | Today's brief, missions, coach, posts, wallet, my page | `earner.html` (left phone) |
| **Earner page** | A follower of the earner | `okpo.com/<handle>`: sign up, ask the earner's AI | `earner.html` (right phone) |
| **Lobby** | Visitors and signed-in earners on okpo.com | Campaigns to join, posts that passed, Earn with OkPo | `lobby.html` |

First client: GCash. Campaign names are plain client names ("GCash Heroes", "GCash Ipon Challenge").

---

## 2. Registers (Locked, one Open)

| | Marketing site (okpo.com landing) | Product (console, earner app, earner page, Lobby) |
|---|---|---|
| Edges | Art hand-drawn, 1.6 to 2.2px wobble; controls crisp with CSS radius | Crisp, CSS radius |
| Hand-drawn shapes | In the art (the tile wall, section tiles). Never on a control: buttons and fields are crisp in both registers. | **Only** inside reward moments (takeovers, the sign-up banner). Never on a control. |
| Main button | Yellow glaze, crisp: 14px corners, ink text, hover 8% darker, press .97 (Locked 2 Oct, direction A) | **Ink** (`--btn`) |
| Surface | Cream and bisque, solid cards | Liquid glass over the tone-on-tone backdrop |

Marketing hero claim (Locked 2 Oct, direction A): "I need more ___" is one field, `#fff` (dark `#1b1b1b`), 1px `#d9d0bb` (dark `#3a3a3a`) edge, 18px corners, the yellow button inside it. Focus turns the edge ink with a soft blue ring. Sent empty: coral edge and "Tell us what you need more of." The other site buttons still use the drawn edge until Luis decides on them.

Never mix registers on one screen. **Open, Luis to review:** the Lobby lives on okpo.com but is built in the product register. Keep it that way until he decides.

---

## 3. Tokens

`tokens.css` is the source. Every prototype should load it instead of redeclaring `:root` (today each one redeclares, with small drift; §12 lists it).

### Glazes (Locked)

| Token | Hex | Tile | Label shade on light |
|---|---|---|---|
| `--coral` | `#FF8787` | Frame (square in square) | `--l-coral #C92A2A` |
| `--yellow` | `#FFD43B` | Half disc and bar | `--l-yellow #9C6500` |
| `--orange` | `#FFA94D` | Cut diamond | `--l-orange #C2410C` |
| `--green` | `#69DB7C` | Quarter disc | `--l-green #237A36` |
| `--blue` | `#74C0FC` | Pinwheel | `--l-blue #1971C2` |
| `--purple` | `#B197FC` | Four petals | `--l-purple #6741D9` |

1. On light, a glaze is graphic only: tiles, fills, bars, tints. Never text, never a thin line or ring. Coloured text and rings on light use the label shade.
2. On dark, label shades switch to the glazes.
3. A full glaze block takes ink text.
4. The wordmark is the only place glazes colour letters on light.

### Neutrals (Locked)

| Token | Light | Dark |
|---|---|---|
| `--ground` | `#F6F1E4` | `#0F0F0F` |
| `--tone` | `#EBE2CC` | `#1C1B19` |
| `--ink` | `#121212` | `#ECECEC` |
| `--body` | `#4A4640` | `#B9BCC0` |
| `--mute` | `#6A655C` | `#8F949A` |
| `--line` | `rgba(18,18,18,.12)` | `rgba(255,255,255,.12)` |
| `--soft` | `rgba(18,18,18,.06)` | `rgba(255,255,255,.07)` |
| `--scrim` | `rgba(18,18,18,.28)` | `rgba(0,0,0,.55)` |
| `--btn` / `--on-btn` | `#121212` / `#F6F1E4` | `#ECECEC` / `#121212` |

### Status tints (Locked)

| Meaning | Background | Text |
|---|---|---|
| ok, live, passed, confirmed, Strong | `rgba(105,219,124,.24)` | `--l-green` |
| fix, fail, didn't count | `rgba(255,135,135,.22)` | `--l-coral` |
| waiting, in review, check me, changed, Needs work | `--warn-bg rgba(255,212,59,.38)` (dark `.2`) | `--warn-ink #6B4E00` (dark `#FFD43B`) |
| paused, invite, campaign scope | `rgba(116,192,252,.24)` | `--l-blue` |
| neutral, draft, note, Good | `--soft` | `--body` |

**"Needs a fix" is coral everywhere** (posts, rules, missions). Yellow means "waiting or needs a look", never "fix".

### Type (Locked)

| Role | Face | Size |
|---|---|---|
| Display: titles, numbers | Bricolage Grotesque **800 only**, `-0.03em` | Console h1 32px (26px under 560px). Phone headline `.big` 30px. Money 46 to 54px. Reward numbers 44 to 112px. |
| Reading, nav, buttons | IBM Plex Sans 400/500/600 | Body 14px/1.45 in apps, 15px/1.55 on the Lobby |
| Labels, IDs, receipts | IBM Plex Mono 600, uppercase, `0.12em` | 10.5px |
| Small text | Plex Sans | 12.5px, `--mute` |

Never Inter, Roboto or Arial. Do not load Bricolage 700.

### Glass (Locked, values from the built prototypes)

```css
--glass-a: rgba(255,255,255,.66);  --glass-b: rgba(255,255,255,.44);
--glass-edge: rgba(255,255,255,.95); --glass-strong: rgba(255,255,255,.82);
--glass-shadow: 0 16px 36px rgba(18,18,18,.10);
/* dark */
--glass-a: rgba(40,40,40,.7); --glass-b: rgba(18,18,18,.6);
--glass-edge: rgba(255,255,255,.18); --glass-strong: rgba(32,32,32,.88);
--glass-shadow: 0 16px 36px rgba(0,0,0,.5);
.glass{background:linear-gradient(160deg,var(--glass-a),var(--glass-b));backdrop-filter:blur(14px) saturate(1.5);border:1px solid var(--glass-edge);box-shadow:inset 0 1px 0 var(--glass-edge),var(--glass-shadow);border-radius:20px}
.glass.strong{background:var(--glass-strong)}
```

Strong glass is for things that float (tab bar, sheets, drawers, modals, toasts, the topbar and sidebar) **and** for the one hero card in a group that must read first (Earned today, Ready to claim, the sign-up card, the main table).

### Radius (Locked)

| Token | Value | Use |
|---|---|---|
| `--r-card` | 20px | glass cards |
| `--r-btn` | 14px | buttons |
| `--r-field` | 12px | inputs, ghost buttons, option cards |
| `--r-row` | 14px | list cards, drag rows |
| `--r-sheet` | 28px top | phone sheets |
| `--r-drawer` | 22px left | console drawer |
| `--r-tabbar` | 26px | phone tab bar |
| `--r-id` | 6px | rule IDs, tags |
| `--r-pill` | 99px | chips, pills, bands |

### Theme (Locked 1 Oct)

Light first. **The OS dark setting is ignored**; dark applies only when the person picks it (`data-theme="dark"`). Build both.

---

## 4. Wordmark (Locked)

`OkPo`: Bricolage 800, `-0.035em`, letters coral, yellow, green, blue. Minimum 20px; below that write OkPo in the text face. All four letters or none: never two letters, never a badge, avatar or app icon made from it, never built from tiles.

---

## 5. Backdrop (Locked)

Three crisp `--tone` tiles behind every product screen, no blur, never a glaze behind a screen.

- Desktop (console, Lobby): quarter top left (`-260px,-360px`, 900px), petal top right (`45vw,-260px`, 640px), half bottom right (`48vw,58vh`, 820px).
- Phone: quarter `-120,-120` 420px, petal `180,140` 300px, half `120,520` 380px.
- The backdrop does not move.

---

## 6. Iconography (Locked)

1. **Tiles.** Six shapes, `viewBox="-5 -5 110 110"`. Filled with their glaze, or outlined `fill:none;stroke:<colour>;stroke-width:9`.
   - Nav and tab icons: outline in `--mute` when idle (14 to 21px), filled glaze when active (15 to 22px).
2. **Line icons** for controls only: 24×24, `stroke-width:1.8`, round caps and joins, `currentColor`. Set: `x, check, back, arrow, chev, bell, send, copy, link, mic, up, play, lock, shield, grip, doc, spark`. Add to this set only by drawing in the same style.
3. **Text glyphs** allowed as icons: `↑ ↓` (reorder, with aria-labels), `→` (link text), `·` (separator).
4. **Avatars:** `.av` circle with 1 or 2 initials on `--soft`. Brand monogram `.bm` rounded square (radius 12) with initials.
5. Nothing else. No invented badges or marks.

### Section tiles (Locked)

Each console section and each earner tab wears one tile.

| Where | Tile | Glaze |
|---|---|---|
| Console Overview, earner Today, the streak | frame | coral |
| Campaigns, Pool and billing, Wallet, money | quarter | green |
| Recruiting, earner My page, follower sign-up | half | yellow |
| Posts, missions, post passed | diamond | orange |
| Leads, invites | pin | blue |
| Brand context, Coach, Ask AI, publish | petal | purple |
| Talking points and the brief | quarter | green |

**On trial (2 Oct):** frame and coral stay on Overview and Today. Do not change them; Luis will call it.

---

## 7. Layout

### Console (Locked)

```css
.app{display:grid;grid-template-columns:244px minmax(0,1fr);gap:16px;padding:16px}
.side{position:sticky;top:16px}          /* glass strong: wordmark 24px, brand switcher, nav, role box */
.topbar{padding:8px 10px 8px 16px}       /* glass strong: live chip, brand, day line, theme, reset */
.view{display:flex;flex-direction:column;gap:14px}
```

- Rhythm: 14px between blocks, 12px inside cards, 10px between rows.
- Breakpoints: 1100, 860 (sidebar becomes a top scroller), 700 (one column), 560.
- **Screen header** is `head(eyebrow, title, sub, right)`:
  - eyebrow `.label` led by the section tile, written `Section · scope`
  - h1 32px Bricolage
  - one or two sentence `.sub`
  - actions on the right

### Phone (Locked)

- Phone 390×800, radius 44.
- Screen padding `22px 18px 110px`, gap 14px.
- Floating tab bar: strong glass, 64px tall, radius 26px, 12px from the edges, five tabs (Today, Coach, Posts, Wallet, My page). It slides away on pushed screens.
- Pushed screens open with a back icon button and a breadcrumb `.small`.
- **Locked (2 Oct):** every tab title is `.big` 26px, Today included. Coach, Posts, Wallet and My page still use a 17px Plex title in the prototype; see §12.

### Lobby (Locked)

`.wrap` max 1180px, gap 56px. Site nav glass strong, current link underlined in ink.

---

## 8. Components (Locked unless marked)

| Component | Spec |
|---|---|
| `.btn` | Ink, `--on-btn` text, 600, radius 14, padding `12px 16px`, press scale .97 over 120ms |
| `.btn.sm` | Radius 12, padding `9px 14px`, for dense console rows |
| `.ghost` | 1px `--line`, transparent, radius 10 to 12, 500 13 to 14px, hover `--soft` |
| `.link` | Underlined text button, offset 3px |
| `.iconbtn` | 40px circle, glass or `--soft`, line icon 16 to 18px, needs `aria-label` |
| `.chip` | Mono 600 10.5px, `.08em`, radius 99, padding `4px 9px`, variants `ok fix warn n info`. Uppercase in the console. Amounts (`+₱40`) and names stay as written. |
| `.chip.go` | Ink pill, Plex 600 13px: the "Start" on a mission row |
| `.st` | Campaign status with a 7px dot: Draft, Waiting for GCash, Live, Paused, Ended |
| `.cnt` | Mono 11px count badge in nav and tabs, neutral or warn |
| `.seg` | Segmented control: soft track radius 12, pressed button strong glass |
| `.pill` | Filter toggle, radius 99, pressed is an ink fill |
| `.rid` | Rule ID, mono 600 10px, radius 6, `--soft`. `.rid.tp` "Talking point" in yellow tint. `.rid.k` fact ID in purple tint. |
| `.band` | Quality band, Plex 600 11.5px, 7px dot + word: Strong (green), Good (neutral), Needs work (yellow). Never coral. |
| `.li` | List row, padding 11px 0, top rule except the first |
| `.mission` | Diamond 22px (filled passed, outline open, coral outline fix), title 600, one sub line, chip on the right |
| `.tbl` | Mono uppercase headers, 13.5px cells, clickable rows hover `--soft` and open on Enter |
| `.field` / `.txt` | 46px (phone) or 42px (console) input, radius 12, strong glass; `.bad` border `--l-coral` |
| `.otp` | 44×54 mono 22px boxes |
| `.opts` / `.plan` | Option cards, pressed is an ink border and inset ring |
| `.cbx` / `.switch` | Checkbox radius 6, switch 40×23. Both pop on with `--pop`. |
| `.drop-z` | Dashed 1.5px `--line`, radius 14, hover `--soft` |
| `.stepper` | Strong glass row: 26px numbered circles (ink when current, green when done), `.sline` progress bars between steps |
| `.outbar` | Publish bar: petal, "N changes ready for vX", ghost "See changes", the primary publish action |
| `.need` | Overview "needs you" tile: tile, `N things verb`, `Review →` |
| Toast | **Console:** bottom centre, strong glass, tile + bold lead + consequence, 3.2s. **Phone:** top inside the phone, strong glass, drops in, 2.6s. |
| Drawer | Console right panel, `min(460px,100%)`, radius `22px 0 0 22px`, scrim |
| Modal | Centred, `min(480px, 100% - 32px)`, scrim |
| Sheet | Phone bottom sheet, radius 28 top, grab handle |
| Chat | `.bub.me` soft, `.bub.ai` petal avatar + text, then `used` chips naming the fact or rule (`K1`, `R-03`) |
| Typing | `.dots`, three 7px dots, 1s loop |
| Empty state | One plain `.small` sentence that says what to do: "Nothing new. The AI checks again tomorrow." |

---

## 9. Moments and motion (Locked, from the built engines)

### Motion tokens

| Token | Curve | Use |
|---|---|---|
| `--ease` | `cubic-bezier(.2,.8,.2,1)` | Everything that settles |
| `--pop` | `cubic-bezier(.34,1.56,.64,1)` | Small things popping on: checks, tokens, switch knobs, counters |
| `--pop-soft` | `cubic-bezier(.34,1.45,.64,1)` | Big shapes and cards arriving: takeover shapes, AI-read cards |
| `--exit` | `cubic-bezier(.6,0,.3,1)` | Leaving: shapes flying to a tab, the wash closing |
| `--arc` | `cubic-bezier(.5,0,.3,1)` | A clone flying along a curve: banner shape, recruit avatars |

### Durations

- Press 120ms.
- Screen push 320ms: the new screen comes in from the right, the old one moves 28% left at .4 opacity.
- Tab or view change: fade up 260ms in, 160ms out.
- Rows, bubbles and cards arriving: rise 8 to 12px, 300 to 350ms.
- Stagger 60 to 90ms.
- Count-up 900ms, ease-out cubic.
- Meters and bars grow 800ms.
- Overlays: drawer 360ms, modal 280ms, sheet 340ms, close 220 to 260ms.

### Earner reward takeover (Locked)

The shape and its colour come from §6. The sequence:

1. The wash opens as a circle from the thing that earned it, 460ms.
2. The hand-drawn shape pops from the origin at scale .06, `--pop-soft`, 620ms.
3. The text rises 14px, 320ms, staggered 90ms per line.
4. Hold 1.5s (streak 1.7s, payday 1.9s). A tap skips.
5. The shape flies to its tab with `--exit` over 560ms while the wash closes into the tab.
6. The tab icon fills and lands (scale 1.5 at 40%, `--pop`).

- Moments queue and never overlap: passed, then money, then streak.
- Light wash is the full glaze, with the shape in its deep or pale shade.
- Dark wash is a tinted dark ground (`#1D150C`, `#0F1A12`, `#1D1010`, `#1D1A0C`), with the shape in its glaze (62% on pale moments) and `#ECECEC` text.

### Things other people do (Locked)

These arrive as the **top banner** and never interrupt:

1. Enters with `--pop-soft`.
2. A yellow sweep runs across it.
3. The shape pops.
4. The counter flips.
5. Hold 2.4s.
6. The shape flies to its tab with `--arc`.

The banner's dark version is still to build (§12).

### Console (Locked)

The console never takes over the screen. Its moments are local:

- **Publish:** a petal pops at the button, then flies to the brand switcher over 1.3s with `--exit`. The live card pops and the switcher pulses.
- **AI reading:** each drafted card arrives from 14px below at scale .96 with `--pop-soft`, 420ms.
- **Checked:** the card flashes a green-tint ring over 0.7s. (Fix: today it uses the green glaze, which is a thin glaze line; use `--l-green`.)
- **Approve:** avatars arc into the Joined column with `--arc`, 700ms.

"One pulse per section per minute, then a counter" is specced but not built (§12).

### What moves on a screen (Locked 2 Oct)

- A step or screen change fades the main column once, 260ms. Inside a step only the part that changed moves.
- Text never animates word by word and never blurs in.
- Things are not thrown across the screen. The only flights are the publish petal (console and setup) and the earner's reward shapes. Confirmed items change in place.
- New things join the end of a list, so nothing below them jumps.

### Reduced motion

Everything becomes a short fade with the **same hold times**. Demo delays stay the same length; only the movement goes.

---

## 10. Brand context, rules, facts, talking points

Vocabulary used in UI copy (Locked): **Brand context**, **Fact** (`K1`), **Voice**, **Rule** (`R-01`), **Talking point**. Never "angle".

- Rule severities: **Fail** (post doesn't count), **Needs a fix** (fix and resubmit), **Note** (lowers quality only).
- Every Do and Don't line carries its rule ID chip, or a yellow "Talking point" chip.
- Every fix names its rule: "Needs a fix · R-01".
- The paid-post label on the earner page reads "Paid partnership with GCash".
- Rule and money changes go to the brand for approval. The second tap reads "Send to GCash for approval", then "Approve and publish vN".

### Brand context (Locked 2 Oct)

Brand context is one thing with one name everywhere: the checked facts, the voice and the rules a brand's AI works from. Earlier names are retired: "Know", "Aim", "Direction", "Who we are", "Guardrails" and "Your [brand] AI".

| Part | IDs | What it holds |
|---|---|---|
| Facts | `K1` | What's true. The AI only states what a checked fact says. |
| Voice | `Voice` | How the brand sounds. |
| Rules | `R-01` | What stops a post. OkPo's four (`R-01`, `R-02`, `R-11`, `R-14`) are the same for every brand and locked. |
| Campaign brief | | Talking points, goal and ending. Lives in Campaigns, written after a campaign is created, sits on top, can add or tighten, never loosen. Never part of setup. |

### Brand setup (Locked 2 Oct, `prototypes/setup.html`)

Setup **is** the console's new-brand flow, run full screen. Same five steps, same components, same motion; only the layout changes.

- Top bar (strong glass): wordmark, brand switcher, the console's `.stepper` (Sources, Read, Check facts, Rules, Test and publish), "Save and exit". Under 900px the stepper becomes "2 of 5 · Read".
- One question per screen, in this order: brand name · sources · three quick questions (optional) · read · facts in pages of five · the conflict picker · voice · questions nothing answered (optional) · rules · test · "Ready to go live?" · live.
- **Brand context panel** on the right (regular glass, sticky). Title "Brand context". The brand's name appears only in its eyebrow ("GCash · v1"), with a Draft or Live chip. Sections: Facts, Voice, Rules, then Campaign brief as the last line, empty. Only checked items enter it. On a phone it is a strong-glass bar ("Brand context · 9 facts · 4 rules") that opens a sheet.
- Read: the console's read engine. Each card rises 14px at .96 into the bottom of its column (Facts, Voice, Rules) with `--pop-soft` over 420ms; the count ticks up; scans turn into checks in place. No re-render at the end.
- Check: "Keep these 5" ticks each card in place with the green flash ring (0.7s, 60ms stagger), and its chip pops into the panel. Cards never leave the screen. Then only the list fades (160ms out, 260ms in); the heading stays. "Check the rest later" saves the rest as drafts the AI does not use.
- Test: the console's test chat. Every answer names the fact or rule it used, and that row flashes in the panel.
- Publish: the console's moment. A petal pops at the button and flies to the brand switcher over 1.3s, the switcher pulses, the live card pops, and the toast reads "**GCash brand context v1 is live.** The coach, daily briefs and every OkPo page use it now."
- Live ends on the campaign brief as the next layer, with "Start the first campaign", which opens the console's new campaign.

---

## 11. Copy (Locked)

- **Chrome is English**, short, second person. Taglish lives in data, AI answers, earner greetings and follower-facing lines. Use "po" when the other person uses it.
- **Three voices, never mixed (Locked 2 Oct):**
  - **Chrome** (headings, buttons, labels, toasts): second person. "Is this right?", "Check the rest later".
  - **OkPo's guide** (setup and other guided flows only): first person, plain, one or two sentences. "I drafted 8 facts. Nothing is used until you check it." It sits in a `.say` block: `--soft` ground, radius 14, a mono "OkPo" label above the text, no avatar, no mark. It rises once, 10px over 320ms, in one piece, and only when its words change. Never word by word.
  - **The brand's AI** as described in the console: third person. "The AI drafts cards. Nothing is used until someone checks it." When the AI answers in a chat it speaks for itself, with the petal and its `used` chips.
- **Names come from data, never from templates.** A brand or person name appears where the screen is about that account: the brand switcher, eyebrow scope ("Brand context · GCash"), buttons that send to them ("Send to GCash"), the earner's own greeting. Flow headings and questions stay general ("Is this true about your brand?" not "Is this true about GCash?"), because the same flow serves every brand.
- Titles: plain nouns ("Campaigns", "Pool and billing") or one clear claim ("Your numbers, next to ours").
- Subtitles: one or two sentences that explain who decides or pays.
- Buttons: verb first, naming the object or the recipient ("Send to GCash for approval", "Claim to GCash").
- Toasts: a bold lead, then the consequence. "**v8 published.** Earners see it in tomorrow's 7:00 AM brief."
- Money `₱40`, tabular numerals. Unknown values `[₱X]`. Example data flagged "Example numbers."
- No em dashes. Middle dot `·` as the separator.

---

## 12. Known drift to fix in the prototypes

1. Every prototype except `setup.html` redeclares `:root` instead of loading `tokens.css`. The values drift: glass saturate, strong-glass alpha, dark edge.
2. Focus rings use `var(--blue)`. Change to `2px solid var(--l-blue)`.
3. Glaze rings on light: the console's green check flash, the yellow example ring and the coral verdict border. Change them to label shades or tints.
4. "Needs a fix" is yellow in the console rules. Change to coral.
5. Talking-point card on the earner mission uses the blue pin. Change to the green quarter.
6. Quality band in the console is plain text, and connected uses chips. Change both to `.band`.
7. The connected prototype's takeover is a text-only linear fade. Replace with the earner engine.
8. Console copy still says Know, Aim and Direction.
9. The follower page wordmark is 15px, under the 20px minimum. Write "OkPo" in the text face instead.
10. Coral appears on the notification badge and the invite dot. Frame and coral on Overview and Today stay while on trial.
11. Earner tabs Coach, Posts, Wallet and My page still use the 17px Plex title. Change to `.big` 26px.
12. The "other people" banner is hard-coded light. Build its strong-glass and dark version.
13. "One pulse per section per minute, then a counter" is specced for the console but not built.
14. The console's own new-brand view still says Know, Aim and Direction, and still asks for starter talking points in Rules. Setup is the reference; bring the console view in line.

---

## 13. Do not

- Put hand-drawn edges on product controls.
- Use a glaze as a screen background, a text colour on light, or a thin line on light.
- Invent icons, badges or partial wordmarks.
- Put a brand's name in a flow's headings.
- Show the earner their quality number.
- Write "angle", "Know", "Aim", "Direction", "Who we are", "Guardrails" or "Your [brand] AI".
- Reopen, restyle or offer alternatives to anything Locked.
- Animate text word by word, or throw confirmed items across the screen.
- Add a full-screen moment to the brand console.
- Blur or animate the backdrop tiles.
- Use any easing other than the five motion tokens.
