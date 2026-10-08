# Trading Lab: human + AI crypto trading, documented

A 14-day exercise (started 2026-10-08) that produces the material for a demo
course on schologic.org, delivered on the Schologic.com LMS.

Goal: an easy-to-understand approach to trading built on human and AI
collaboration, learned in the open by a first-time trader with AI help.
Everything is documented as it happens, including mistakes.

## Ground rules

- **Real money stays small.** Only an amount we are fully prepared to lose.
  Each trade is approved by a person before it is placed. The AI never places
  orders on its own.
- **Predictions are scored.** Every forecast is written down before the
  outcome is known, with a range and a confidence, and checked afterwards.
  The track record is the lesson, not any single call.
- **No API key with withdrawal rights** is ever used.

## Data sources

| Source | What it gives | Status |
|---|---|---|
| Binance.US public API | Prices, candles back to 2024+, 24h stats | Working, no key needed |
| Binance.US private API | Balances, orders | Blocked: key returns `-2015` (see `../CLAUDE.md`) |
| Cryptowisser news (MCP) | Headlines, coin-specific news | Working |

## Plan (14 days)

| Days | Work | Course output |
|---|---|---|
| 1–2 | Screen for high-deviation assets, pick 5, write baseline profiles | Lesson 1: what volatility is and how to measure it |
| 3–7 | Forecast each asset at 6h / 12h / 24h, twice a day; score every forecast | Lesson 2: forecasts as ranges, and keeping score |
| 6–9 | Fix API access; paper-trade the rules that scored best | Lesson 3: turning a view into a trade plan (entry, stop, size) |
| 9–12 | A few small real trades, each approved and journaled | Lesson 4: the first real trades, unedited |
| 12–14 | Review results, write up, build the course in the LMS | Lesson 5: what worked, what didn't, what's next |

## Files

- `screen.py`: ranks liquid Binance.US pairs by volatility and deviation.
- `data/`: dated screen outputs (CSV).
- `journal.md`: running log of decisions, forecasts and results.
