# OkPo design system, for AI coders

Read this before you write any OkPo UI. It describes the system **as Luis decided it on 3 Oct 2026, with the 5 Oct review folded in**. The working prototypes (`prototypes/console.html`, `onboard.html`, `earner.html`, `lobby.html`, `connected.html`) are being brought in line; §12 lists what they still get wrong. If this file and a prototype disagree, this file wins, and the prototype is due a fix. **One exception:** the earner app and the follower page settled on 3 Oct (the “Earner keep and change” board) are the source for those two rooms. If this file disagrees with them, this file is due a fix, not the screens. If a screen you are asked to build breaks a rule here, follow this file and say so in your summary.

Status words:

- **Locked**: Luis decided it and it stays closed. Build it this way. Do not suggest alternatives, redesigns or "small improvements" to it, and do not raise it in reviews. It reopens only when Luis says so in so many words.
- **On trial**: in use and kept for now. Do not change it; Luis will call it.
- **Open**: build the current default, keep it easy to change, and do not invent a new answer.

### What changed on 3 Oct 2026

Luis reopened and re-locked these. Everything else from 2 Oct stands.

1. **Brand context is now the Playbook**, in three parts: Facts, Voice, Rules. Rules come in three kinds: Never, Careful, Always. The Playbook has editions. Campaigns live in Campaigns, not in the Playbook (§10).
2. **Shape map**: five shapes, five meanings, everything else ink (§6). The old one-tile-per-section table is retired, and so is the frame and coral trial.
3. **The earner's day is "Today's mission"**. "Brief" is a brand-side word only (§10, §11).
4. **Earner tab bar** uses tile-family symbols; Coach gets the speech tile (§6).
5. **Console nav is plain words**, no icons (§7).
6. **Nine principles** for every view (§1a).
7. **Liquid glass** for the Playbook book and its live moment (§3).

### Locked register

| Area | What is locked | Where |
|---|---|---|
| Principles | The nine principles | §1a |
| Registers | Marketing art is hand-drawn, marketing controls are crisp yellow; product is crisp glass with an ink main button | §2 |
| Tokens | Glazes, label shades, neutrals, status tints, type, glass, liquid glass, radius, light first | §3 |
| Wordmark | OkPo, four glazes, 20px minimum, all four letters or none | §4 |
| Backdrop | Three crisp tone tiles, fixed placement, never moves | §5 |
| Shape map | Five shapes, five meanings, everything else ink | §6 |
| Tab symbols | Today pin, Coach speech tile, Posts frame, Wallet quarter, My page lens | §6 |
| Layout | Console shell with a words-only nav, phone shell, Lobby wrap, screen header | §7 |
| Tab titles | `.big` 26px on every earner tab | §7 |
| Components | Everything in §8 | §8 |
| Motion | The five curves, the durations, the takeover, the banner, the console moments | §9 |
| Vocabulary | Playbook, Facts, Voice, Rules, Never, Careful, Always, Edition, Talking point, Today's mission | §10 |
| Playbook view | The book, one OkPo line, three part cards; detail one level down | §10 |
| Campaigns | Built on a Playbook edition, add only, clashes flagged | §10 |
| Fast onboarding | Trust levels, minimum to publish, answer cards, To check list, the glass live moment | §10 |
| Voice | Chrome in second person, OkPo's guide in first person, the AI in third person | §11 |
| Copy | Names from data, button and toast shapes, money format, no em dashes | §11 |

Open: the sensitive list (§10), the level names (§10).

The golden rule for new screens: **reuse a pattern that already exists in a prototype before inventing one.** No new icons, badges, marks or shortened wordmarks. Visuals come from the tiles and the line-icon set in §6, and the full wordmark.

---

## 1. What OkPo is

OkPo trains AI to train a brand's influencers. Three surfaces share one state:

| Surface | Who | Job | Prototype |
|---|---|---|---|
| **Brand console** | Brand marketing manager, OkPo team | Playbook, campaigns, recruiting, posts, leads, pool | `console.html` |
| **Earner app** | Influencers ("earners", e.g. Ana) | Today's mission, coach, posts, wallet, my page | `earner.html` (left phone) |
| **Earner page** | A follower of the earner | `okpo.com/<handle>`: sign up, ask the earner's AI | `earner.html` (right phone) |
| **Lobby** | Visitors and signed-in creators at okpo.com (the home page) | Campaigns to join, posts that passed, Earn with OkPo | `lobby.html` |
| **For brands** | Brand marketing managers at okpo.com/brands | The landing, with the masterline “Build a community that grows your revenue.” | `~/Projects/okpo/site` (`/brands` redirects to okpo-landing for now) |

New brands arrive through fast onboarding (`onboard.html`), which ends with their Playbook live.

First client: GCash. Campaign names are plain client names ("GCash Heroes", "GCash Ipon Challenge").

### How the parts feed each other

The Playbook is the source. Every campaign is built on one of its editions. The coach and Today's mission draw on the Playbook and the campaign. Every post is checked against the Rules. Posts that pass earn money from the campaign's pool. Followers who ask the earner's AI get answers from the Facts the AI may say.

---

## 1a. Principles (Locked 3 Oct)

They came from the Playbook redesign and apply to every view.

| # | Principle | In the console | Elsewhere |
|---|---|---|---|
| 1 | **Start with something they recognise** | The Playbook view opens on the book they saw in onboarding. | Today's mission looks like what they were promised at sign-up. |
| 2 | **One job per screen** | The first visit reassures. Upkeep lives one level down. | Today leads with the mission. The money and habit cards from the delight study stay under it (Earned today, streak, weekly bonus); claiming lives in Wallet. |
| 3 | **Say it once** | The contents already summarise the parts; cards don't repeat them. | The mission card doesn't repeat the campaign card. |
| 4 | **Detail one level at a time** | Book, then part, then line, then source. | Rule IDs, trust labels and dates are on tap, never upfront. |
| 5 | **Quiet until something needs you** | Healthy looks calm. "1 to check" appears only when due. | No always-on "needs you" strip; it appears when it has something. |
| 6 | **Few named groups, each with a shape** | Facts, Voice, Rules. Shape first, then word. | One shape per idea across every room, no collisions (§6). |
| 7 | **Plain words** | "1 to check", not "Sourced · R-03 · expired". | "Today's mission", not "brief v7". |
| 8 | **Fits one screen at rest** | If the first view scrolls, it is doing two jobs. | Earner Today opens on Today’s mission and the missions; Always true and the habit cards follow below, as settled 3 Oct. |
| 9 | **Show it working** | "See it in a post" beats a paragraph about a rule. | Show the earner's draft with the fix, not a rules list. |

---

## 2. Registers (Locked, one Open)

| | Marketing site (okpo.com landing) | Product (console, earner app, earner page, Lobby) |
|---|---|---|
| Edges | Art hand-drawn, 1.6 to 2.2px wobble; controls crisp with CSS radius | Crisp, CSS radius |
| Hand-drawn shapes | In the art (the tile wall, section tiles). Never on a control: buttons and fields are crisp in both registers. | **Only** inside reward moments (takeovers, the sign-up banner). Never on a control. |
| Main button | Yellow glaze, crisp: 14px corners, ink text, hover 8% darker, press .97 | **Ink** (`--btn`) |
| Surface | Cream and bisque, solid cards | Liquid glass over the tone-on-tone backdrop |

Marketing hero claim: "I need more ___" is one field, `#fff` (dark `#1b1b1b`), 1px `#d9d0bb` (dark `#3a3a3a`) edge, 18px corners, the yellow button inside it. Focus turns the edge ink with a soft blue ring. Sent empty: coral edge and "Tell us what you need more of." The other site buttons still use the drawn edge until Luis decides on them.

Never mix registers on one screen. **Locked 5 Oct:** the Lobby is okpo.com’s home page and stays in the product register; the landing moves to okpo.com/brands in the marketing register.

Diagrams and design boards are light only.

---

## 3. Tokens

`tokens.css` is the source. Every prototype should load it instead of redeclaring `:root` (§12).

### Glazes (Locked)

| Token | Hex | Meaning (§6) | Label shade on light |
|---|---|---|---|
| `--blue` | `#74C0FC` | Facts | `--l-blue #1971C2` |
| `--purple` | `#B197FC` | Voice | `--l-purple #6741D9` |
| `--coral` | `#FF8787` | Rules, and "needs a fix" | `--l-coral #C92A2A` |
| `--yellow` | `#FFD43B` | Missions | `--l-yellow #9C6500` |
| `--green` | `#69DB7C` | Money | `--l-green #237A36` |
| `--orange` | `#FFA94D` | None in the product. Kept for marketing art. | `--l-orange #C2410C` |

1. On light, a glaze is graphic only: tiles, fills, bars, tints. Never text, never a thin line or ring. Coloured text and rings on light use the label shade.
2. On dark, label shades switch to the glazes.
3. A full glaze block takes ink text.
4. The wordmark is the only place glazes colour letters on light.
5. In the product a glaze always means one of the five meanings in §6, or a status from the table below. Nothing is coloured for decoration.

### Chart series (Locked 5 Oct)

Charts never use glazes. Two series: `--s-gcash` ink for the number that bills (confirmed by the brand), `--s-okpo` a tone shade (`#C9BFA9`, dark `#55524B`) for OkPo’s count. Axis labels use the mono stack with a fallback.

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
| fix, fail, didn't count, Never | `rgba(255,135,135,.22)` | `--l-coral` |
| waiting, in review, to check, changed, Needs work, Careful | `--warn-bg rgba(255,212,59,.38)` (dark `.2`) | `--warn-ink #6B4E00` (dark `#FFD43B`) |
| paused, invite | `rgba(116,192,252,.24)` | `--l-blue` |
| neutral, draft, note, Good, Always | `--soft` | `--body` |

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

### Liquid glass (Locked 3 Oct, the book only)

The Playbook book and the "Your playbook is live" moment use a heavier glass that visibly bends what is behind it. Nothing else does.

```css
--liquid-blur: blur(22px) saturate(1.75);
--liquid-sheen: linear-gradient(135deg,rgba(255,255,255,.58) 0%,rgba(255,255,255,.09) 36%,rgba(255,255,255,0) 58%,rgba(255,255,255,.2) 100%);
--liquid-rim: inset 0 1px 0 rgba(255,255,255,.95),inset 0 -1px 0 rgba(255,255,255,.35),inset 1px 0 0 rgba(255,255,255,.55),inset -1px 0 0 rgba(255,255,255,.25);
```

- **Cover:** tinted in the brand's own colour (GCash `rgba(13,110,253,.78)` to `.58` at 160deg), white text, radius `22px 6px 6px 22px`, a 1px white spine on the right.
- **Contents page:** `rgba(255,255,255,.52)`, radius `6px 22px 22px 6px`, the sheen at .7.
- Both carry the sheen as an overlay and the rim as `box-shadow`.
- **Something to bend:** crisp Facts, Voice and Rules tiles sit behind the book, partly covered, so the glass has shapes to refract. This is the one place glazes sit behind glass, and only behind the book, never behind a screen.
- The live moment sits on a tone-on-tone ground in the brand tint with large crisp tone tiles in the corners.

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

### Theme (Locked)

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

Tone tiles carry no meaning; they are ground, not shapes in the §6 sense.

---

## 6. Iconography (Locked 3 Oct)

### The shape map

**Five shapes, five meanings. Everything else is ink.** Colour and shape are reserved for the five things people need to tell apart at a glance. Nothing else gets a coloured shape, so a shape never means two things.

| Meaning | Tile | Glaze | Covers |
|---|---|---|---|
| **Facts** | half (arch) | blue | What's true about the brand |
| **Voice** | petal (four petals) | purple | How the brand sounds |
| **Rules** | diamond | coral | Never, Careful, Always |
| **Missions** | pin (pinwheel) | yellow | Campaigns, Today's mission, talking points, streaks |
| **Money** | quarter | green | Pool, payouts, payday, a post that earned |

Tile paths, `viewBox="-5 -5 110 110"`, filled with their glaze or outlined `fill:none;stroke:<colour>;stroke-width:9`:

```html
half:    <path d="M0 100 A50 50 0 0 1 100 100 Z"/><rect width="100" height="22"/>
petal:   <path d="M50 50 Q50 2 98 2 Q98 50 50 50 Z M50 50 Q98 50 98 98 Q50 98 50 50 Z M50 50 Q50 98 2 98 Q2 50 50 50 Z M50 50 Q2 50 2 2 Q50 2 50 50 Z"/>
diamond: <path d="M50 0L100 50L50 100L0 50Z M50 28L72 50L50 72L28 50Z" fill-rule="evenodd"/>
pin:     <path d="M0 0 L50 0 L50 50 Z M100 0 L100 50 L50 50 Z M100 100 L50 100 L50 50 Z M0 100 L0 50 L50 50 Z"/>
quarter: <path d="M0 100 L0 0 A100 100 0 0 1 100 100 Z"/>
```

- A tile sits **beside the header** of the thing it names. The rows under it carry only the colour (a tint, a dot, a bar), not another tile.
- Shape first, then word: the part's tile comes before its name.

### Tab symbols (Locked 3 Oct)

Three more tiles from the same family. They are **ink only**, never coloured, because they are not meanings.

| Tab | Symbol | Active |
|---|---|---|
| Today | pin | yellow fill |
| Coach | speech tile (a tile with one sharp corner) | ink fill |
| Posts | frame (square in square) | ink fill |
| Wallet | quarter | green fill |
| My page | lens | ink fill |

```html
speech: <path d="M0 100 V30 Q0 0 30 0 H70 Q100 0 100 30 V70 Q100 100 70 100 Z"/>
frame:  <path d="M0 0H100V100H0Z M27 27V73H73V27Z" fill-rule="evenodd"/>
lens:   <path d="M0 50 Q50 -16 100 50 Q50 116 0 50 Z"/>
```

- Idle: outline in `--mute`, 20px. Active: filled, 22px, the label 600 ink.
- The pin is the exception to outlines: its four triangles meet at the centre, so a stroke crosses itself. Wherever the pin would be outlined (idle tab, an open mission, a future streak day) it is a soft fill instead: the outline colour at 42% opacity.
- The speech tile is also OkPo's Coach and AI mark wherever the AI speaks (chat, Ask AI). Always ink.

### Everything else is ink

1. **Line icons** for controls and for things that are not one of the five (people, leads, posts, settings): 24×24, `stroke-width:1.8`, round caps and joins, `currentColor`. Set: `x, check, back, arrow, chev, bell, send, copy, link, mic, up, play, lock, shield, grip, doc, spark, person, people`. Add to this set only by drawing in the same style.
2. **Text glyphs** allowed as icons: `↑ ↓` (reorder, with aria-labels), `→` (link text), `·` (separator).
3. **Avatars:** `.av` circle with 1 or 2 initials on `--soft`. Brand monogram `.bm` rounded square (radius 12) with initials.
4. Nothing else. No invented badges or marks.

### Retired on 3 Oct

| Was | Now |
|---|---|
| Frame, coral: Overview, Today, the streak | Overview has no tile; Today and the streak are the yellow pin |
| Half, yellow: Recruiting, My page, sign-up | Half is Facts (blue). Recruiting is a word; My page is the lens; sign-up is the yellow pin |
| Diamond, orange: Posts, missions, post passed | Diamond is Rules (coral). Posts is the frame; missions are the pin; a post that passed is the green quarter |
| Pin, blue: Leads, invites | Pin is Missions (yellow). Leads and invites are ink |
| Petal, purple: Brand context, Coach, Ask AI, publish | Petal is Voice. Coach and Ask AI are the speech tile |
| Quarter, green: talking points and the brief | Talking points are the yellow pin |

---

## 7. Layout

### Console (Locked)

```css
.app{display:grid;grid-template-columns:244px minmax(0,1fr);gap:16px;padding:16px}
.side{position:sticky;top:16px}          /* glass strong: wordmark 24px, brand switcher, nav, role box */
.topbar{padding:8px 10px 8px 16px}       /* glass strong: live chip, brand, day line, theme, reset */
.view{display:flex;flex-direction:column;gap:14px}
```

- **Nav (Locked 3 Oct): plain words, no icons.** Overview, Campaigns, Recruiting, Posts, Leads, Playbook, Pool and billing. Plex 500 15px, padding `11px 12px`, radius 12. Active is 600 with a soft ink fill `rgba(18,18,18,.07)` (dark `rgba(255,255,255,.08)`), never a colour, so colour stays for the five meanings. A `.cnt` may follow the word only when something is due.
- Rhythm: 14px between blocks, 12px inside cards, 10px between rows.
- Breakpoints: 1100, 860 (sidebar becomes a top scroller), 700 (one column), 560.
- **Screen header** is `head(eyebrow, title, sub, right)`:
  - eyebrow `.label`, written `Section · scope`. It leads with a tile only when the screen is one of the five meanings (a campaign: pin; Pool and billing: quarter; a Playbook part: its own tile).
  - h1 32px Bricolage
  - one or two sentence `.sub`
  - actions on the right

### Phone (Locked)

- Phone 390×800, radius 44.
- Screen padding `22px 18px 110px`, gap 14px.
- Floating tab bar: strong glass, 64px tall, radius 26px, 12px from the edges, five tabs (Today, Coach, Posts, Wallet, My page) with the §6 symbols. It slides away on pushed screens.
- Pushed screens open with a back icon button and a breadcrumb `.small`.
- Every tab title is `.big` 26px, Today included.
- Today fits the phone without scrolling at rest (principle 8).

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
| `.cnt` | Mono 11px count badge in nav and tabs, neutral or warn. Shown only when something is due. |
| `.seg` | Segmented control: soft track radius 12, pressed button strong glass |
| `.pill` | Filter toggle, radius 99, pressed is an ink fill |
| `.rid` | Rule or fact ID, mono 600 10px, radius 6, `--soft`. **Shown on tap or hover only**, with the line's source and trust. `.rid.tp` "Talking point" in yellow tint. `.rid.k` fact ID in blue tint. |
| `.band` | Quality band, Plex 600 11.5px, 7px dot + word: Strong (green), Good (neutral), Needs work (yellow). Never coral. |
| `.li` | List row, padding 11px 0, top rule except the first |
| `.mission` | Pin 22px (filled done, outline open, `--l-coral` outline needs a fix), title 600, one sub line, chip on the right |
| `.always` | "Always true for GCash" block under Today's mission: a `.label`, then 2 or 3 Playbook lines in plain words, each led by a 7px dot in its part's colour. No IDs. |
| `.book` | The Playbook book in liquid glass (§3): cover with brand monogram, name, one-line description, "Written by OkPo and GCash"; contents page with numbered chapters. An edition chip "Edition N · live" above it. |
| `.part` | Playbook part card: tile beside the header (Facts, Voice, Rules), one-line summary, a mono count ("14 FACTS"), and "1 to check" in warn only when due. Opens the part. |
| `.tbl` | Mono uppercase headers, 13.5px cells, clickable rows hover `--soft` and open on Enter |
| `.field` / `.txt` | 46px (phone) or 42px (console) input, radius 12, strong glass; `.bad` border `--l-coral` |
| `.otp` | 44×54 mono 22px boxes |
| `.opts` / `.plan` | Option cards, pressed is an ink border and inset ring |
| `.cbx` / `.switch` | Checkbox radius 6, switch 40×23. Both pop on with `--pop`. |
| `.drop-z` | Dashed 1.5px `--line`, radius 14, hover `--soft` |
| `.stepper` | Strong glass row: 26px numbered circles (ink when current, green when done), `.sline` progress bars between steps |
| `.outbar` | Publish bar, ink, no tile: "N changes ready for Edition N", ghost "See changes", the primary publish action |
| `.need` | A row that says what needs you: `N things verb`, `Review →`. No tile. Appears only when something is due, never as an always-on strip. |
| Toast | **Console:** bottom centre, strong glass, bold lead + consequence, 3.2s. A tile leads only when the toast is about one of the five meanings. **Phone:** top inside the phone, strong glass, drops in, 2.6s. |
| Drawer | Console right panel, `min(460px,100%)`, radius `22px 0 0 22px`, scrim |
| Modal | Centred, `min(480px, 100% - 32px)`, scrim |
| Sheet | Phone bottom sheet, radius 28 top, grab handle |
| Chat | `.bub.me` soft, `.bub.ai` speech tile (ink) + text, then `used` chips naming the part in plain words ("From Facts", "Rule: say it's paid"), each with its part's dot. IDs on tap. |
| Typing | `.dots`, three 7px dots, 1s loop |
| Empty state | One plain `.small` sentence that says what to do: "Nothing new. The AI checks again tomorrow." |

---

## 9. Moments and motion (Locked)

### Motion tokens

| Token | Curve | Use |
|---|---|---|
| `--ease` | `cubic-bezier(.2,.8,.2,1)` | Everything that settles |
| `--pop` | `cubic-bezier(.34,1.56,.64,1)` | Small things popping on: checks, tokens, switch knobs, counters |
| `--pop-soft` | `cubic-bezier(.34,1.45,.64,1)` | Big shapes and cards arriving: takeover shapes, AI-read cards, the book |
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

### Earner reward takeover (Locked; shapes remapped 3 Oct)

Everything from the delight study stays: the wash, the hand-drawn shapes, the count-ups, the holds, the queue. Only the shapes follow the §6 map.

| Moment | Shape | Wash |
|---|---|---|
| A post passed | quarter | green |
| Payday | quarter, deep | green |
| Streak | pin, deep | yellow |
| Mission done | pin | yellow |

The sequence:

1. The wash opens as a circle from the thing that earned it, 460ms.
2. The hand-drawn shape pops from the origin at scale .06, `--pop-soft`, 620ms.
3. The text rises 14px, 320ms, staggered 90ms per line.
4. Hold 1.5s (streak 1.7s, payday 1.9s). A tap skips.
5. The shape flies to its tab with `--exit` over 560ms while the wash closes into the tab.
6. The tab symbol fills and lands (scale 1.5 at 40%, `--pop`).

- Moments queue and never overlap: passed, then money, then streak.
- Light wash is the full glaze, with the shape in its deep or pale shade.
- Dark wash is a tinted dark ground (green `#0F1A12`, yellow `#1D1A0C`), with the shape in its glaze (62% on pale moments) and `#ECECEC` text.

### Things other people do (Locked)

These arrive as the **top banner** and never interrupt. A follower signing up wears the yellow pin.

1. Enters with `--pop-soft`.
2. A yellow sweep runs across it.
3. The shape pops.
4. The counter flips.
5. Hold 2.4s.
6. The shape flies to its tab with `--arc`.

The banner's dark version is still to build (§12).

### Console (Locked)

The console never takes over the screen. Its moments are local:

- **Publish an edition:** the book settles (scale .97 to 1, `--pop-soft`, 420ms), the edition chip flips to the new number with `--pop`, and the toast reads "**Edition 2 is out.** Earners get it in tomorrow's mission." Nothing flies.
- **AI reading:** each drafted card arrives from 14px below at scale .96 with `--pop-soft`, 420ms.
- **Checked:** the card flashes a `--l-green` ring over 0.7s.
- **Approve:** avatars arc into the Joined column with `--arc`, 700ms.

"One pulse per section per minute, then a counter" is specced but not built (§12).

### Onboarding live moment (Locked 3 Oct)

Publishing the first edition ends on one full-screen moment, the only one on the brand side: the book in liquid glass on the brand-tint ground, "Your playbook is live.", one line on what happens next, and "Open the console". The book rises 14px at .96 with `--pop-soft`, 520ms; the line follows after 90ms. Hold until the button.

### What moves on a screen (Locked)

- A step or screen change fades the main column once, 260ms. Inside a step only the part that changed moves.
- Text never animates word by word and never blurs in.
- Things are not thrown across the screen. The only flights are the earner's reward shapes and the banner shape. Confirmed items change in place.
- New things join the end of a list, so nothing below them jumps.

### Reduced motion

Everything becomes a short fade with the **same hold times**. Demo delays stay the same length; only the movement goes.

---

## 10. The Playbook, campaigns and missions

### Vocabulary (Locked 3 Oct)

| Word | Means | Who sees it |
|---|---|---|
| **Playbook** | Everything a brand's AI works from: Facts, Voice, Rules | Brand, OkPo |
| **Facts** | What's true. The AI only says what a fact allows (trust, below). | Brand, OkPo |
| **Voice** | How the brand sounds | Brand, OkPo |
| **Rules** | What every post must or must not do: **Never**, **Careful**, **Always** | Brand, OkPo; earners see the lines in plain words |
| **Edition** | A published version of the Playbook: Edition 1, Edition 2 | Brand, OkPo |
| **Campaign** | Built on an edition; adds talking points, goal and ending | Everyone |
| **Talking point** | A campaign's message to get across | Everyone |
| **Brief** | The brand-side word for what earners get each day | Brand only |
| **Today's mission** | What the earner does today | Earner |

Retired: "Brand context", "Know", "Aim", "Direction", "Who we are", "Guardrails", "Your [brand] AI", "angle", and the severities "Fail", "Needs a fix" and "Note" as rule types. ("Needs a fix" stays as a post status.)

### Rules

| Kind | Means | A slip |
|---|---|---|
| **Never** | A post that does this comes back. | The post doesn't count until fixed. |
| **Careful** | Allowed, with a condition. | Needs a fix. |
| **Always** | Every post, every campaign. | Needs a fix. |

- Each rule line shows its words and, under it, one example in quotes. Its ID (`R-03`), source and trust are on tap or hover.
- OkPo's four rules are the same for every brand and locked. The part ends with "Plus OkPo's 4 rules for every brand."
- The paid-post label reads "Paid partnership with GCash". It is an Always rule.
- Rule and money changes go to the brand for approval. The second tap reads "Send to GCash for approval", then "Approve and publish Edition N".
- Feedback to an earner names the rule in plain words ("Say it's paid"), never the ID.

### Trust (Locked)

Every fact carries one of three levels:

- **Confirmed** (the brand picked it on a card or checked it): the AI says it freely.
- **Sourced** (found word for word on the brand's own page): the AI may say it, close to the source, and names the source.
- **Guess** (inferred): the AI never says it until confirmed.

**Sensitive facts are never spoken at Sourced, only Confirmed.** List (Open, to revisit): money, eligibility, dates and deadlines, legal, health and safety.

Trust is shown on tap, never as a chip on every line (principle 4).

### Freshness (Locked)

- Each part has an owner and a "verified until" date, shown on tap.
- A fact not re-checked for 30 days is **paused until someone re-confirms it**; everything else keeps working.
- The part card shows "1 to check" only when something is due. Healthy parts show nothing extra.

### The Playbook view in the console (Locked 3 Oct)

The view opens on the same book the brand saw in onboarding, with the three parts under it.

1. **First visit:** the edition chip, the book, one first-person OkPo line ("Your playbook is live. Earners get their first brief from it tomorrow at 9:00."), "Try it" on the right, then three closed `.part` cards: Facts, Voice, Rules. Nothing else. It fits one screen.
2. **Returning:** the same, with the OkPo line saying what is due ("One thing to check in Voice. Everything else is current.") and "1 to check" on that part.
3. **A part opened:** breadcrumb "Playbook / Facts · Voice · Rules" to switch parts, the part's tile and one-line summary, "See it in a post" and "Add a rule" (or fact, or trait). Rules are grouped Never, Careful, Always, each group with a one-line meaning. Each line's ID, source, trust and Edit sit one level down.

Detail goes one level at a time: book, part, line, source.

The book’s contents are the same everywhere it appears (onboarding, the live moment, the console, the showcase): 01 What you sell, 02 Who buys (Facts), 03 How you sound, 04 How you look (Voice), 05 Rules. “How you look” is its own chapter (settled 5 Oct, reopened by Luis): five chapters, still three parts. Its lines live in the Voice part under a “How you look” heading, after “How you sound”, so the shape map needs no new shape. Tapping chapter 04 opens Voice at that heading.

### Campaigns (Locked 3 Oct)

Campaigns live in Campaigns. The Playbook never holds campaign facts or rules.

- A campaign is **built on a Playbook edition**, named on the campaign ("Built on Edition 1").
- It adds talking points, a goal and an ending. It can add rules or tighten them, never loosen.
- When a new edition is published, OkPo re-checks every live campaign against it and flags anything that now clashes on that campaign, in plain words, with a fix.
- Campaigns wear the yellow pin, beside the campaign name on every card.
- **Pools are per campaign (Locked 5 Oct).** A campaign’s posts are paid from its own pool. Pool and billing lists one pool per campaign and one invoice for the brand.
- **Overview is brand-wide (Locked 5 Oct):** the one OkPo line, then a row per campaign (progress and pool left), then the chart and recent posts.

### Today's mission (Locked 3 Oct)

- The earner's Today tab headline is **"Today's mission"**, one mission card, then the `.always` block "Always true for GCash" with 2 or 3 Playbook lines.
- The mission card's Do and Don't become Never, Careful, Always in plain words. No rule IDs.
- The Coach answers from the Playbook and cites the part in plain words.
- The earner page's Ask AI follows the trust rules: never a Guess, never a sensitive fact below Confirmed.

### Fast onboarding (Locked, `prototypes/onboard.html`)

The first visit is a fast path. Completeness is not the goal; the brand or OkPo finishes the rest later.

- **One input:** a website or brand name. OkPo reads public web only: the brand's site, app store pages, public socials, news. Sources it can't read show "Couldn't read".
- **Optional files and links:** under the website, "Add more" (marked optional) takes dropped files (brand book, decks, FAQs, price lists) and pasted links (Drive, Notion, socials, landing pages). Each added item says what OkPo will use it for. A private link shows "Needs sharing" and is skipped until shared. Facts from a file name the file as their source.
- **Read shows the work:** sources land one by one; facts enter the draft book as they are found.
- **Draft book:** the brand sees its Playbook as a book before any question.
- **Answer cards:** a question, 2 to 4 options OkPo derived, "Something else" to type, "Skip for now". Each option carries its source and trust. Number keys answer; one click moves on. "Who do you want more of" takes up to 3; Voice is a blend of up to 2.
- **Sensitive conflicts must be answered to publish.** "Don't mention it yet" counts as an answer; the AI stays quiet and the item goes to To check. Continue stays locked until it is answered.
- **Rules:** pre-ticked toggles grouped Never, Careful, Always.
- **Minimum to publish Edition 1:** who they want more of, voice, at least 1 rule, every sensitive conflict answered.
- **Test and publish**, then the liquid-glass live moment (§9): "**Your playbook is live.**", then "Open the console", which lands on the real console (`console.html#first`) on Edition 1’s first visit. Onboarding has 9 screens and no console of its own. In the demo, “Skip to day 12” jumps to Edition 7 with two campaigns live; Edition 7 grew out of Edition 1’s facts and rules.
- **To check:** one shared list inside the Playbook of skipped, Guess and unconfirmed sensitive items. The brand and OkPo both have full access; whoever gets there first confirms it.
- Steps in the `.stepper`: Sources, Read, Check, Rules, Test and publish. Under 900px it becomes "2 of 5 · Read".

### How well I know the brand (Locked)

An expectation setter: what the AI can do with what it has been given.

- **Four levels:** Just met, Learning, Knows you, Knows you well. Names are Open; the four-level shape is Locked.
  - Just met: website read, not published. Drafts only. "0 of 4 to publish".
  - Learning: the minimum to publish is in. Writes daily briefs; sensitive questions go to the brand's team.
  - Knows you: To check cleared, none older than 7 days; fees and eligibility Confirmed; at least 1 file from the brand.
  - Knows you well: a finished campaign with results fed back; earner questions answered within 2 days.
- **Never an accuracy %.** The level says what OkPo can and can't do.
- **Moves only on what the brand adds,** never on time spent or days live.
- **Can drop a level** when a promo ends or a fact passes 30 days without a re-check.
- **Meter:** 4 segments in ink (purple now means Voice); the current level name with "n of 4". After a drop, the lost segment stays as an outline and the label reads "from Knows you".
- It lives one level down from the book (principle 5), and comes forward in the OkPo line only when it moves.

---

## 11. Copy (Locked)

- **The person who posts (Locked 5 Oct):** brand screens (console, /brands) say **influencers**, the word the buyer uses. Everywhere else (Lobby, earner app, earner page) says **creators**, or just “you”. “Earner” stays the internal word in this file and in code.
- **Chrome is English**, short, second person. Taglish lives in data, AI answers, earner greetings and follower-facing lines. Use "po" when the other person uses it.
- **Three voices, never mixed:**
  - **Chrome** (headings, buttons, labels, toasts): second person. "Is this right?", "Check the rest later".
  - **OkPo's guide** (onboarding, the Playbook's one line, other guided spots): first person, plain, one or two sentences. "I drafted 8 facts. Nothing is used until you check it." It sits in a `.say` block: `--soft` ground, radius 14, a mono "OkPo" label above the text, no avatar, no mark. It rises once, 10px over 320ms, in one piece, and only when its words change. Never word by word.
  - **The brand's AI** as described in the console: third person. "The AI drafts cards. Nothing is used until someone checks it." When the AI answers in a chat it speaks for itself, with the speech tile and its `used` chips.
- **Plain words before system words.** "1 to check", not "Sourced · R-03 · expired". "Today's mission", not "brief v7". IDs, trust and dates are one level down.
- **Names come from data, never from templates.** A brand or person name appears where the screen is about that account: the brand switcher, eyebrow scope ("Playbook · GCash"), buttons that send to them ("Send to GCash"), "Always true for GCash", the earner's own greeting. Flow headings and questions stay general ("Is this true about your brand?"), because the same flow serves every brand.
- Titles: plain nouns ("Campaigns", "Pool and billing") or one clear claim ("Your numbers, next to ours").
- Subtitles: one or two sentences that explain who decides or pays.
- Buttons: verb first, naming the object or the recipient ("Send to GCash for approval", "Claim to GCash").
- Toasts: a bold lead, then the consequence. "**Edition 2 is out.** Earners get it in tomorrow's mission."
- Money `₱40`, tabular numerals. Unknown values `[₱X]`. Example data flagged "Example numbers."
- No em dashes. Middle dot `·` as the separator.

---

## 12. Known drift to fix in the prototypes

**Review of 5 Oct, fixed the same day.** Every room was opened and checked. The review page lists every screen with its status.

- **Console:** charts in ink and a tone shade; switches and sliders ink; the brief preview uses dots with IDs on hover; campaign cards wear the pin; the new-campaign flow names its edition and asks “What should this campaign get you?”; Leads says “How a sign-up counts” and pays from the pool; the Playbook first visit drops Add a brand (it lives in the brand switcher) and the updated-by line; the book has five lines; Facts show their group once; Voice has Add a trait; Posts show the campaign; Overview has a row per campaign; Pool and billing has a pool per campaign; Edition 1 first visit (`#first`) with “Skip to day 12”; the Playbook parts use the breadcrumb.
- **Onboarding:** 9 screens; the draft book says Draft; OkPo’s guide line carries a mono “OkPo” label, no mark; briefs at 7:00; “Open the console” opens `console.html#first`.
- **Connected:** Ana’s phone has the five tabs; no edition on the earner side; the brief uses dots.
- **Lobby:** home page hero is the creator line; For brands opens /brands; Never, Careful, Always copy.
- **Earner:** sources on tap say “GCash Playbook”, no edition. Nothing else changed: the 3 Oct screens are the source.

Still open:

1. The console’s in-product new-brand flow still uses its own five steps; the brand switcher’s “Add a brand” opens `/onboard`.
2. “One pulse per section per minute, then a counter” is specced but not built.
3. The landing’s move to okpo.com/brands happens in `~/Projects/okpo/site`; until then `/brands` redirects to okpo-landing.
4. Not yet opened in the review: the earner app’s campaigns, invite and notifications screens, and Ask AI on the earner page.

**Retired 4 Oct:** the Brand Setup artifact, `/setup-v1`, and the GU, SU, BC2 and Ctx2 boards on the product canvas. Keep them as archive; do not build from them.

---

## 13. Do not

- Put hand-drawn edges on product controls.
- Use a glaze as a screen background, a text colour on light, or a thin line on light.
- Colour anything that is not one of the five meanings or a status.
- Give one shape two meanings, or put a tile on every row (tile beside the header, colour below).
- Put icons in the console nav.
- Invent icons, badges or partial wordmarks.
- Show rule IDs, trust labels or dates upfront. They are one tap down.
- Show an always-on "needs you" strip.
- Put campaign facts, rules or talking points in the Playbook.
- Call the earner's day a "brief" in the earner app.
- Put a brand's name in a flow's headings.
- Show the earner their quality number.
- Write "Brand context", "angle", "Know", "Aim", "Direction", "Who we are", "Guardrails" or "Your [brand] AI".
- Reopen, restyle or offer alternatives to anything Locked.
- Animate text word by word, or throw confirmed items across the screen.
- Add a full-screen moment to the brand console. The onboarding live moment is the one brand-side exception.
- Use liquid glass on anything but the book and its live moment.
- Blur or animate the backdrop tiles.
- Use any easing other than the five motion tokens.
