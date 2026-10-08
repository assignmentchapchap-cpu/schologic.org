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

**Candidate five (to confirm on Day 2):** PUMP, NEAR, ZEC, SUI, ALGO.
ADA is the alternate. ZEC has by far the most volume, so its signals are the
most trustworthy; ALGO has the least.

**Next:** news check per coin, baseline profile for each, first 6h / 12h /
24h forecasts.
