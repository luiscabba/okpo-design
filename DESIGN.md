# OkPo design system, for AI coders

Read this before you write any OkPo UI. It is the short, binding version of the OkPo product system canvas and the brand book. If a screen you are asked to build breaks a rule here, follow this file and say so in your summary.

Status words used below:

- **Settled**: build it this way.
- **Open**: build the current default, keep it easy to change, and do not invent a new answer.

---

## 1. What OkPo is (so the UI makes sense)

OkPo trains AI to train a brand's influencers. Three surfaces share one state:

| Surface | Who | Job |
|---|---|---|
| **Brand console** | Brand marketing manager, OkPo team | Set brand context (rules, facts, talking points), run campaigns, read posts, leads and pool |
| **Earner app** | Influencers ("earners", e.g. Ana) | Daily brief, missions, coach, posts, wallet, their OkPo page |
| **Earner page** | A follower of the earner | `okpo.com/<handle>`: sign up for the campaign, ask the earner's AI |

First client: GCash. Campaign names are plain client names ("GCash Heroes", "GCash Ipon Challenge") with no mark of their own. Copy is Taglish; use "po" when the other person uses it.

---

## 2. Two registers: site vs product (Settled)

| | Marketing site (okpo.com landing) | Product (console, earner app, earner page) |
|---|---|---|
| Edges | Hand-drawn: buttons, cards, photo cuts wobble 1.6 to 2.2px. No CSS border radius. | Crisp. CSS radius allowed (cards 20px, buttons 12 to 14px, chips 99px). |
| Sloppy shapes | Everywhere tiles appear | **Only** inside reward moments (takeovers, banners). Never on a control. |
| Main button | Yellow glaze, drawn edge | **Ink** (`--btn`), crisp |
| Surface | Cream and bisque grounds, solid cards | Clear liquid glass over a tone-on-tone tile backdrop |

Never mix the two registers on one screen.

---

## 3. Tokens

Copy `tokens.css` from this repo. Values:

### Colour: the six glazes (Settled)

| Token | Hex | Tile it belongs to | Label shade on light |
|---|---|---|---|
| `--coral` | `#FF8787` | Square in square (frame) | `--l-coral` `#C92A2A` |
| `--yellow` | `#FFD43B` | Half disc and bar | `--l-yellow` `#9C6500` |
| `--orange` | `#FFA94D` | Cut diamond | `#C2410C` |
| `--green` | `#69DB7C` | Quarter disc | `--l-green` `#237A36` |
| `--blue` | `#74C0FC` | Pinwheel | `#1971C2` |
| `--purple` | `#B197FC` | Four petals | `--l-purple` `#6741D9` |

Rules:

1. On a light ground a glaze is graphic only: tiles, fills, bars. It never carries text or a thin line. Coloured text on light uses the label shade.
2. On dark, glazes can be text and lines.
3. A full glaze block takes ink text.
4. The wordmark is the only place glazes colour letters on light.

### Product neutrals (Settled)

| Token | Light | Dark |
|---|---|---|
| `--ground` | `#F6F1E4` | `#0F0F0F` |
| `--tone` (backdrop tiles) | `#EBE2CC` | `#1C1B19` |
| `--ink` | `#121212` | `#ECECEC` |
| `--body` | `#4A4640` | `#B9BCC0` |
| `--mute` | `#6A655C` | `#8F949A` |
| `--line` | `rgba(18,18,18,.12)` | `rgba(255,255,255,.12)` |
| `--soft` | `rgba(18,18,18,.06)` | `rgba(255,255,255,.07)` |
| `--btn` / `--on-btn` | `#121212` / `#F6F1E4` | `#ECECEC` / `#121212` |

Site neutrals: cream `#FFFDF6`, bisque `#F3EFE6`, rule `#E2DCCD`, panel dark `#1B1B1B`, rule dark `#2E2E2E`, paper `#E3E3E3`.

### Type (Settled)

| Role | Face | Size |
|---|---|---|
| Display, numbers, screen titles | Bricolage Grotesque 800, `-0.03em` | 26 to 30px titles, 44 to 112px reward numbers |
| Reading, nav, buttons | IBM Plex Sans 400/500/600 | 14 to 16px |
| Labels, IDs, receipts | IBM Plex Mono 600, uppercase, `0.12em` | 10.5 to 13px |

All three are free Google Fonts. Never use Inter, Roboto or Arial. Nothing lighter than 800 for display.

### Motion (Settled unless marked)

- Pop: `cubic-bezier(.34,1.56,.64,1)`. Ease: `cubic-bezier(.2,.8,.2,1)`. Exits: `cubic-bezier(.6,0,.3,1)`.
- Numbers count up over 0.8 to 0.9s, easing out.
- Screen push 320ms; fade 260ms.
- `prefers-reduced-motion`: everything still or a short fade, same hold times.

---

## 4. The wordmark (Settled)

`OkPo`: capital O and P, Bricolage Grotesque 800, `-0.035em`. Letters O coral, k yellow, P green, o blue, in that order on light and dark. Minimum 20px; below that write OkPo in the text face. Never build letters from tiles, never add an underline, plate or squiggle. In the nav: wordmark only, no four-tile mark.

---

## 5. Backdrop and surfaces (Settled)

- Every product screen sits on the tone-on-tone backdrop: three tiles a shade off the ground (`--tone`), crisp, no blur. On a phone: quarter off the top left, petal on the right, half rising from the bottom.
- Never put a glaze colour behind a screen.
- Clear glass for content cards; strong glass (`--glass-strong`) for anything that floats: tab bar, sheets, banners, toasts.

```css
.glass{background:linear-gradient(160deg,var(--glass-a),var(--glass-b));
  backdrop-filter:blur(14px) saturate(1.6);border:1px solid var(--glass-edge);
  box-shadow:inset 0 1px 0 var(--glass-edge),var(--glass-shadow);border-radius:20px}
.glass.strong{background:var(--glass-strong)}
```

---

## 6. Each moment owns a shape and a colour

| Moment | Shape | Colour | Lives in tab | Size | Shade |
|---|---|---|---|---|---|
| Post passed | Cut diamond | Orange | Posts | Takeover | Pale |
| Money landed | Quarter disc | Green | Wallet | Takeover | Pale |
| Streak ticked | Square in square | Coral | Today | Takeover | Deep |
| Payday | Four quarters | Green | Wallet | Takeover | Deep |
| Follower signed up | Half disc | Yellow | My page | Top banner | Pale |
| Coach | Petals | Purple | Coach | Never a reward | |

- Money is always green.
- Wins the earner makes happen take over the screen. Things other people do (a follower signs up) arrive as a top banner and never interrupt.
- Takeover path: wash opens from the thing that earned it, shape pops with overshoot, text rises, hold about 1.5s (tap skips), shape flies to its tab, the tab icon lands.
- Tab icons: outline in `--mute` when idle, filled glaze when active.
- Brand console (Settled 1 Oct, option B): each section wears its tile, the same as the earner app. Posts orange diamond, Leads blue pinwheel, Brand context purple petals, Talking points green quarter, Recruiting yellow half, Pool green quarter. Status colours keep their meaning everywhere.
- The console never takes over the screen. One pulse per section per minute, then a counter. No sound.
- **Open**: the takeover system as a whole, streak rules, claim-now fee, weekly bonus, dark-mode washes.

---

## 7. Brand context v2: rules, facts, talking points (Settled 1 Oct)

These words are product vocabulary. Use them exactly.

| Thing | What it answers | ID | Where it shows |
|---|---|---|---|
| **Rule** | What must a post never do? | `R-01`, `R-02` ... | Mission Do and Don't, fixes, verdicts, coach answers |
| **Fact** | What may the AI claim? | `K1`, `K2` ... | Coach and Ask AI "used" chips |
| **Talking point** | What is this post about? | `TALKING POINT 01` | Console order list, mission detail, post rows |

- Never write "angle" in UI copy. It is "talking point".
- Talking points live inside each campaign's brief only. Their order (and share) steers the mix; they never override a rule or a fact.
- Rule severities: **Fail** (post doesn't count), **Needs a fix** (fix and resubmit), **Note** (lowers quality only).
- Every Do and Don't line on a mission carries its rule ID as a mono chip. Lines that come from the talking point carry a yellow "Talking point" chip instead.
- Every fix names its rule: "Needs a fix · R-01".
- Rule changes go to the brand for approval before they are live. Money changes need a second tap ("Send to GCash", "Approve and publish").

```html
<li><span>Say it’s free to join.</span><span class="rid">R-06</span></li>
<li><span>Name one goal you’re saving for.</span><span class="rid tp">Talking point</span></li>
```

---

## 8. Quality score (Settled 1 Oct, parts open)

- Pass or fail decides pay. Quality sits beside it and **never changes pay**.
- Score 0 to 100 from four parts: Brief fit 35, Clear and true 25, Craft 20, Style notes 20. **Open**: the split, until production data.
- Bands: **Strong** 80 to 100, **Good** 60 to 79, **Needs work** below 60.
- Brand console shows the number and its four parts. The earner sees **the band and two tips, never the number**.
- Band colours: Strong green tint, Good neutral, Needs work yellow tint. Never coral: coral means "fix this", and a low band is not a failure.
- Each tip names its rule ID or "Talking point".
- Disputes are reviewed by the OkPo team.

```js
const qBand = n => n >= 80 ? 'Strong' : n >= 60 ? 'Good' : 'Needs work';
```

---

## 9. Components (product)

| Component | Spec |
|---|---|
| Button | Ink fill, `--on-btn` text, 600 weight, radius 12 to 14px, press scales to .97 |
| Ghost button | 1px `--line` border, transparent, radius 10px |
| Chip | Mono 600 10.5px, `0.08em`, radius 99px. `ok` green tint, `fix` coral tint, `wait` soft, `go` ink |
| Rule ID | Mono 600 10px, radius 6px, `--soft` ground. Talking point variant: yellow tint, `--l-yellow` text |
| Band | Plex Sans 600 11.5px, dot plus word, radius 99px |
| Mission row | Diamond icon (outline open, filled passed), title, one sub line ("Talking point: X · +₱40 when it passes"), chip on the right |
| Tab bar | Strong glass, 64px, radius 26px, floats 12px from the edges, five tabs: Today, Coach, Posts, Wallet, My page |
| Top banner | Strong glass, radius 22px, yellow sweep, shape pops, counter flips |
| Sheet | Strong glass, radius 28px top, grab handle |
| Daily cap | Three missions a day across all campaigns |

Accessibility: real `<button>`, `<a>`, `<label>`; icon-only buttons get `aria-label`; text 4.5:1; status never by colour alone (always a word).

---

## 10. Copy

- Taglish, short. "Libre mag-join. About 5 minutes on the GCash app."
- No em dashes. Use a full stop or a comma.
- Money as `₱40`, tabular numerals.
- Placeholders for unknown values: `[₱X]`, never an invented number.
- Name things by what the user does: "Claim to GCash", "Paste the link", "Submit for check".

---

## 11. Do not

- Put sloppy edges on product controls.
- Use a glaze as a screen background.
- Show the earner their quality number.
- Write "angle".
- Use coral for anything but a fix, a fail, the streak, or the wordmark's O.
- Add a full-screen moment to the brand console.
- Blur the backdrop tiles.
