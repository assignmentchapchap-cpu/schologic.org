# Journal

## 2026-10-08, Day 1: first screen

**Market context.** Broad sell-off. Bitcoin fell below $83,000 as Brent
crude topped $102 and US Treasury yields rose to 5.31%; $80,000 is being
watched as the next BTC downside level (Cryptowisser, "Bitcoin Slips Below
$83,000 as Oil Surge Fuels $80,000 Fears", 2026-10-08). Every coin in the
screen trades below its 7-day average.

**Lesson learned on the first run.** The raw screen was topped by coins
down 70–99% in a day (UST, LOOM, VITE, REN). On checking, these pairs were in
`BREAK` status, which means halted or being delisted. Their "volatility" was
a collapse, not an opportunity. Fix: keep only pairs that are actively
trading, with at least $100k of volume and 1,000 real trades a day. That
left 13 coins. Teaching point: always check *why* something is moving.

**Screen result** (`data/screen-2026-10-08T2329Z.csv`), ranked by daily
volatility:

| Coin | Price | 24h | Daily vol | vs 7-day avg |
|---|---|---|---|---|
| PUMP | 0.00564 | -9.6% | 8.8% | -7.8% |
| NEAR | 4.544 | -15.2% | 7.7% | -8.6% |
| ALGO | 0.1181 | -0.4% | 6.6% | -6.5% |
| ZEC | 1190.08 | -11.0% | 5.6% | -9.6% |
| SUI | 1.0513 | -6.8% | 5.6% | -9.9% |
| ADA | 0.2346 | -8.0% | 5.1% | -8.0% |
| BTC (reference) | 81,861.78 | -1.8% | 1.8% | -3.4% |

**Selection rationale.** The course is for beginners with a low risk
appetite, and the real-trade budget is $10–$50 in total. So the five are
chosen for two jobs: *study* (they must move enough to be worth forecasting)
and *safety* (they must be easy to buy and sell at a fair price).

Selection rules:
1. Actively trading on Binance.US (not halted or delisting).
2. Real liquidity: at least $100k traded today *and* on a normal day. A coin
   that only looks busy today can be hard to sell tomorrow.
3. High volatility: these are the ones that teach the most about forecasting.
4. Mixed types, so the course can compare a meme coin, platform coins and a
   privacy coin, instead of five versions of the same thing.

90-day profile (Binance.US daily candles):

| Coin | 90d change | 30d change | Typical daily swing | Avg daily volume (30d) | From 90d high |
|---|---|---|---|---|---|
| PUMP | +304% | +31% | 7.5% | $173k | -14% |
| NEAR | +143% | +96% | 5.7% | $294k | -16% |
| ZEC | +135% | +1% | 6.4% | $2.0M | -28% |
| SUI | +44% | +30% | 4.4% | $358k | -17% |
| ADA | +41% | +7% | 3.9% | $163k | -13% |
| ALGO (dropped) | +38% | +18% | 3.8% | $27k | -13% |

**Final five: PUMP, NEAR, ZEC, SUI, ADA.**

- **ZEC (Zcash)**, privacy coin. By far the most liquid alt here, so its
  price signals are the most trustworthy. It has stalled (+1% in 30 days,
  28% off its high) after a big run, which makes it a clean "what happens
  after a rally" case study.
- **NEAR**, smart-contract platform. It nearly doubled in 30 days and then
  fell 15% today, the sharpest drop in the group. Momentum versus pullback.
- **SUI**, smart-contract platform. Strong trend (+30% in 30 days),
  furthest below its 7-day average today. Tests whether a dip in an uptrend
  recovers.
- **PUMP**, meme / launchpad token. The most volatile coin that still
  trades properly. Included **for study, not as a trade candidate for
  beginners**: it shows what high risk looks like in practice.
- **ADA (Cardano)**, large established coin. Calmer than the rest, so it is
  the closest to a "beginner-appropriate" volatile asset, and a useful
  contrast.
- **ALGO was dropped.** Today's volume was a spike; on a normal day only
  about $27k trades. Thin markets mean wider spreads and harder exits, the
  wrong lesson for beginners.

**Budget and position sizing ($10–$50).** Binance.US accepts orders from
$1, so the budget is workable. At this size, trading fees and the buy/sell
spread are a meaningful share of any gain, so few, deliberate trades beat
many small ones. Working rules: no more than $10 in any single trade, a
written exit plan (target and stop) before buying, and BTC/ETH remain the
default "safer" choice the course compares everything against.

**Next:** check the current Binance.US fee tier, news check per coin, baseline profile for each, first 6h / 12h /
24h forecasts.

## 2026-10-09 00:00 UTC, Day 2: news check and first forecasts (run F001)

### Market backdrop
A broad sell-off on 2026-10-08: Bitcoin dipped to about $80,400 as oil topped $102 and
US 10-year yields hit 5.31%; $80,000 is the level traders are watching (Cryptowisser,
[Bitcoin Slips Below $83,000](https://www.cryptowisser.com/news/bitcoin-slips-below-83000-as-oil-surge-fuels-80000-fears/)).
In the last 6 hours every coin bounced 2–5% off its low. On hourly charts all six
(including BTC) are still below their 20-, 50- and 200-hour averages, which is a
short-term downtrend. None is "oversold" yet (RSI 33–41; below 30 usually counts).

### News, coin by coin (Cryptowisser, 24 Sep – 8 Oct)

| Coin | Recent news | What it shows |
|---|---|---|
| ZEC | Winklevoss filed for a spot Zcash ETF (7 Oct); NU7 upgrade on testnet, blocks 75s→25s (5 Oct); Fortitude's $100M miner deal (7 Oct); Bitget hacker moved $3.9M into Zcash's private pool (1 Oct) | Strong positive headlines, **yet the price fell 10.6% in 24h**. Good news doesn't guarantee a rising price when the whole market is selling. |
| NEAR | Robinhood Chain live on Near.com (8 Oct); Bitwise spot NEAR ETF launched (30 Sep); NEAR Intents **$3.8M exploit**, trading halted, refund promised (2 Oct) | Mixed. The 16% drop is the largest of the group and came the same day as positive news, so the market is the more likely driver. |
| SUI | Google Cloud partnership on AI-agent proof layer (7 Oct); 6M TPS record attempt (7 Oct); USDsui stablecoin on Kraken (6 Oct) | Steady positive flow, no red flags. |
| ADA | Cardano Foundation spins off Veridian (8 Oct); CIP-0113 token standard with freeze/seize powers (7 Oct); +11% rally on 5 Oct | Gave back its 5 Oct rally. |
| PUMP | No Cryptowisser coverage | Moves are driven by sentiment and the wider market alone. Lack of news is itself a risk signal. |

Links: [Zcash ETF](https://www.cryptowisser.com/news/winklevoss-twins-file-for-a-spot-zcash-etf-on-nasdaq/),
[NEAR exploit](https://www.cryptowisser.com/news/near-intents-halts-trading-after-38m-exploit-vows-full-refund/),
[Robinhood Chain on NEAR](https://www.cryptowisser.com/news/robinhood-chain-goes-live-linking-users-to-180-assets-via-near/),
[Sui + Google Cloud](https://www.cryptowisser.com/news/google-cloud-and-sui-build-a-proof-layer-for-ai-agent-actions/),
[Cardano Veridian](https://www.cryptowisser.com/news/cardano-foundation-spins-off-veridian-to-verify-ai-agents-identity/).

**Cost check:** NEAR's buy/sell spread on Binance.US is 0.56% (ZEC 0.04%, SUI 0.01%, ADA
0.05%, PUMP 0.06%). On a $10 trade that's ~6 cents lost on entry alone, before fees.

### How the forecasts work (`forecast.py`)
- **Centre = current price.** Over hours, crypto is close to a coin flip. Any view goes
  into a separate "chance it ends higher" number, rather than into a fake price target.
- **Ranges** come from each coin's normal hourly movement over the last 30 days, scaled
  to 6, 12 and 24 hours. The 68% range should catch the price about 2 times in 3, and
  the 90% range 9 times in 10. Scoring will show whether that holds; crypto often
  jumps more than "normal" maths expects.
- **Scoring:** whether the price landed in each range, whether the direction lean was
  right, and a Brier score (0 = perfect, 0.25 = coin flip, higher = worse than guessing).

### Our reasoning for the leans
- **6h: 50% for all (no call).** The bounce could continue, but the trend is down.
  These two forces cancel out.
- **12h–24h: slight lean lower (45–47%)** for NEAR, SUI, ADA and BTC: price is below every
  hourly average and the macro pressure (oil, yields) hasn't eased. This is a *weak* view.
- **ZEC: 50% throughout.** The ETF filing and upgrade news may cushion it; trend and news
  pull in opposite directions.
- **PUMP: leaning lowest (42% at 24h).** It has the highest volatility, no news support,
  and meme tokens tend to fall hardest in risk-off markets.

**What would change the view:** BTC holding above $80,000 and reclaiming its 20-hour
average (~$82,100) would weaken the "lower" lean. BTC breaking below $80,000 would
strengthen it, and each coin's 24h low (ZEC 1,113 / NEAR 4.30 / SUI 0.999 / ADA 0.224 /
PUMP 0.00528) becomes the next line to watch.

### F001 forecasts (made 2026-10-09 00:00 UTC)

| Coin | Price | Chance higher 6h / 12h / 24h | 24h typical move | 24h 68% range | 24h 90% range |
|---|---|---|---|---|---|
| ZEC | 1,186.1 | 50 / 50 / 50 | ±6.1% | 1,115.7 – 1,261.0 | 1,072.5 – 1,311.7 |
| NEAR | 4.483 | 50 / 47 / 45 | ±8.6% | 4.116 – 4.883 | 3.895 – 5.160 |
| SUI | 1.0409 | 50 / 47 / 45 | ±5.7% | 0.983 – 1.102 | 0.948 – 1.143 |
| ADA | 0.23462 | 50 / 47 / 45 | ±4.6% | 0.2240 – 0.2457 | 0.2175 – 0.2531 |
| PUMP | 0.0055432 | 50 / 45 / 42 | ±8.0% | 0.00512 – 0.00601 | 0.00486 – 0.00633 |
| BTC (reference) | 81,754 | 50 / 48 / 47 | ±1.8% | 80,269 – 83,268 | 79,325 – 84,259 |

6h and 12h ranges are in `forecasts.csv`. Scoring is due at 06:00 UTC, 12:00 UTC and
00:00 UTC on 10 Oct.

*Educational information, not personalized financial advice. Crypto assets can lose
substantial value.*
