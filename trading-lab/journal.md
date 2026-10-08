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
