# OkPo design system

The product design system for OkPo: the brand console, the earner app and the earner page.

- `index.html` is the showcase. Every specimen on it is the real component.
- `DESIGN.md` is the brief for AI coding agents. Point Claude Code, Cursor or any agent at it before they build OkPo UI.
- `tokens.css` holds every colour, type, radius and motion token, light and dark, plus the core components.
- `prototypes/` holds four working prototypes. Short links on the live site:
  - `/console`: the brand console
  - `/earner`: the earner app, with a follower's page beside it
  - `/audience`: the same file, opened on the follower's page
  - `/lobby`: okpo.com for visitors and signed-in earners (campaigns, posts that passed, Earn with OkPo)
  - `/connected`: all three sharing one state
  - `/setup` (also `/onboard`): brand setup, the fast path: one input, a few answer cards, live

It is plain static HTML. No build step.

## Run it

Open `index.html` in a browser, or serve the folder:

```
npx serve .
```

## Use it in your own project

1. Copy `tokens.css` into your app and load the three Google Fonts it names.
2. Add `DESIGN.md` to your repo (or your agent's context) so generated UI follows the rules.
3. Build with the classes in `tokens.css`: `.glass`, `.btn`, `.ghost`, `.chip`, `.rid`, `.band`, `.label`, `.wordmark`.

## Status

Settled and open decisions are marked in `DESIGN.md`. Open items keep their current default until decided.
