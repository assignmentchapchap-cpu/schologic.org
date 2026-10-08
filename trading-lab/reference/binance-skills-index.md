# Binance Skills Hub: index

Source: `assignmentchapchap-cpu/binance-skills-hub` (a copy of `binance/binance-skills-hub`),
read 2026-10-08 at commit `9960c67`. In a session, clone it read-only to
`/home/user/assignmentchapchap-cpu/binance-skills-hub`; paths below are relative to its `skills/`.

## Read this first

- **These skills target Binance.com and Binance Web3 (on-chain), not Binance.US.** Our
  credentials are for `api.binance.us`, so none of the account or trading skills apply to
  our real trades.
- **Blocked from this cloud environment (tested 2026-10-08).** Every data host returned
  `403 Host not in allowlist`: `www.binance.com`, `web3.binance.com`,
  `dquery.sintral.io` (kline candles), `api.binance.com`. To use the read-only research
  skills, add those hosts to the environment's network allowlist.
- **"Web3" skills cover on-chain tokens** on BSC (`56`), Solana (`CT_501`), Base (`8453`),
  Ethereum (`1`). They are looked up by contract address, not by exchange ticker. Of our
  five coins, only PUMP (a Solana token) is a natural fit.
- Most CLIs run with `node <skill-dir>/scripts/cli.mjs <command> '<json>'` (Node 22 is
  installed). Skills marked **baw** need the `@binance/agentic-wallet` npm CLI and a
  Binance Web3 wallet login.

## Quick lookup: "I want to…"

| I want to… | Skill | Usable for Trading Lab? |
|---|---|---|
| Check if a token contract is a scam / honeypot | `query-token-audit` | Yes, for PUMP, once the host is allowed |
| Get a token's price, holders, liquidity, candles (on-chain) | `query-token-info` | Yes for PUMP; the rest use Binance.US data |
| See trending / most-hyped / smart-money-inflow tokens | `crypto-market-rank` | Yes, as market context |
| See what "smart money" wallets just bought or sold | `trading-signal` | Context only; mostly meme tokens |
| Explain a concept for beginners (gas, staking, volatility…) | `academy-skill` | **Yes, best fit for the course** |
| Place spot, futures or convert trades on Binance.com | `binance` | No (wrong exchange) |
| Copy-trade wallets automatically | `binance-onchain-copy-trader` | No (too risky for beginners; borrow its discipline) |
| Rank or score trader wallets | `binance-leaderboard` | No; its scoring model is useful as a teaching idea |
| Track wallets, accumulation/distribution patterns | `binance-wallet-tracker` | No |
| On-chain wallet: swaps, limit orders, DeFi, prediction markets | `binance-agentic-wallet` | No |
| Meme launchpad feed (Pump.fun etc.), AI hot topics | `meme-rush` | No (high-risk content) |
| World Cup match predictions + betting | `binance-sports-ai-analyzer` | No |
| Tokenized US stocks (Ondo) | `binance-tokenized-securities-info` | No |
| A wallet address's token holdings | `query-address-info` | No |
| Fiat on-ramp methods, prices by country | `fiat` | No (excludes US; Binance.com only) |
| Buy crypto and send it on-chain (partner API) | `onchain-pay` | No (merchant API) |
| Pay / receive with Binance Pay QR codes | `payment` | No |
| P2P ads and prices, P2P orders | `p2p` | No |
| Post to Binance Square | `square-post` | Maybe later, for course marketing (needs a Square API key) |

## Skills in detail

### Exchange account and trading (`binance/`)

**`binance/binance`**: Binance.com via `binance-cli` (installer script from GitHub). Covers
spot, futures (USDS-M, COIN-M), options, margin, convert, earn, staking, loans, copy
trading, sub-accounts, wallet, plus a generic `binance-cli request` escape hatch. Needs a
Binance.com API key. Rule: prod transactions require the user to type `CONFIRM`. Per-command
docs are in `references/<command>.md`.

**`binance/fiat`**: public fiat APIs at `www.binance.com/bapi/fiat/v1/public/fiatpayment/agent`:
`get-capabilities`, `get-buy-and-sell-payment-methods`,
`get-deposit-and-withdraw-payment-methods`, `get-price`. Authenticated history is in
`references/sapi-endpoints.md`. Hard rule: **never** use `US` as the country (unsupported).

**`binance/p2p`**: P2P/C2C. Public quotes and ad search (no auth); personal orders, appeals
and ad publishing (SAPI key). Note: SAPI signing keeps parameter **insertion order** rather
than sorting.

**`binance/payment`**: Binance Pay send (QR / PIX) and receive (payment links).
`python3 payment_skill.py --action …`. Never use the clipboard without explicit consent.

**`binance/onchain-pay`**: partner (merchant) on-ramp API at `api.commonservice.io` with RSA
signing: payment methods, quotes, pre-orders, order status, networks.

**`binance/square-post`**: publish text, image, article or video posts to Binance Square.
Key: `BINANCE_SQUARE_OPENAPI_KEY`. Limit: 100 posts per day.

**`binance/academy-skill`**: Binance Academy content (glossary, courses, Learn & Earn,
articles) via `www.binance.com/bapi/bigdata`. Four intents: Q&A, risk education, learning
plans, Learn & Earn. Run with
`ACADEMY_SKILL_DIR=<dir> node scripts/academy-api.mjs prod searchAll '{"query":"…","lang":"en","limit":3}'`;
`getLearningPlan` takes a clean topic noun. Outputs must cite Academy URLs and never give
investment advice. Risk answers end with a mandatory disclaimer. **Most relevant skill for
writing beginner course material.**

### On-chain research, read-only (`binance-web3/`)

**`query-token-info`**: `search` (keyword/symbol/contract), `meta` (socials, creator),
`dynamic` (price, volume, holders, liquidity), `kline` (intervals `1s`…`1m`; each candle is
`[o,h,l,c,v,ts,count]`). Numbers arrive as strings.

**`query-token-audit`**: `POST web3.binance.com/.../security/token/audit` with
`binanceChainId`, `contractAddress` and a UUID `requestId`. Risk levels: 0–1 LOW (still not
"safe"), 2–3 MEDIUM, 4 HIGH (avoid), 5 block. Taxes: >10% critical, 5–10% warning. Only
trust results when `hasResult` and `isSupported` are both true. Ends with a "not investment
advice" disclaimer.

**`crypto-market-rank`**: `social-hype`, `token-rank` (rankType 10 = Trending, 11 = Top
Search, 20 = Alpha, 40 = Stock; period 50 = 24h), `smart-money-inflow`, `meme-rank` (BSC
only), `address-pnl-rank`.

**`trading-signal`**: smart-money buy/sell events (BSC, Solana), with trigger price, max gain
and exit rate. More smart-money addresses = stronger signal; exit rate ≥70% = smart money
already left.

**`meme-rush`**: launchpad feed (New / Finalizing / Migrated) and AI "topic rush"
narratives.

**`query-address-info`**: a wallet's holdings (`positions`, `offset` required).

**`binance-tokenized-securities-info`**: Ondo tokenized US stocks: list, metadata, market
status, corporate actions, price, klines. One token can equal several shares
(`multiplier`).

**`binance-sports-ai-analyzer`**: World Cup match AI probabilities and prediction-market
handoff.

### On-chain wallet and automation (`binance-web3/`, need `baw`)

**`binance-agentic-wallet`**: full Web3 wallet: auth, balances, send, market and limit
orders, approvals, DeFi, prediction markets, x402 payments, gas. Rules worth reusing:
confirm every state-changing action; a conditional instruction ("sell at $X") must be a
limit order and is **never** silently executed at market instead; never invent contract
addresses.

**`binance-trading-signal`**: smart-money signals plus user-built meme/fomo strategies with
backtests. Useful ideas (in `SKILL.md` and `knowledge.md`):
- "Can I still buy?" checklist: pullback from peak <30% may still have room, >50% means
  momentum is gone; exclude liquidity < $5K; flag signals older than 2h as stale.
- Time-to-peak buckets: snipe <1m, quick flip 1–5m, swing 5–60m, hold 1–24h, moon >24h.
- Conservative / balanced / aggressive parameter presets.

**`binance-leaderboard`**: top traders by PnL, win rate, volume; wallet scoring out of 100
(win rate 25, stability 20, drawdown 20, tags 15, PnL 10, follow-friendly 10) plus a ±10 AI
adjustment. Details in `references/scoring.md`.

**`binance-wallet-tracker`**: wallet groups, consensus/pioneer tokens, nine replay analyses
(accumulation/distribution, sector rotation, anomaly orders, round-trips, first-mover,
wake-up, bot-like), WebSocket push. Details in `references/analytics.md`.

**`binance-onchain-copy-trader`**: scaffold that wires the skills above into a copy-trading
pipeline with strategy hooks; it ships **no** strategy. Its advice transfers well to our
course: run a long `dry-run` first, build your own baseline from your own logged events,
go live only with money you can afford to lose entirely, and treat every parameter as a
suggestion, not a guarantee.

## What this means for the Trading Lab

1. Real trades stay on **Binance.US**, through its own API. These skills don't change that.
2. Worth unlocking (network allowlist): `www.binance.com` for `academy-skill` (beginner
   explanations with citable links) and `web3.binance.com` for `query-token-audit`,
   `query-token-info` and `crypto-market-rank` (market context, and a PUMP safety check).
3. Ideas to borrow for the course, with attribution: the copy-trader's "dry-run before
   live" sequence (our paper-trade phase), the agentic wallet's "never turn a conditional
   order into an immediate one", the audit risk-level table, and the "can I still buy"
   pullback rule as a discussion example.
