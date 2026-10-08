"""Screen Binance.US USDT pairs for high deviation (volatility).

Public data only; no API keys needed. Run: python3 trading-lab/screen.py
Writes a dated CSV to trading-lab/data/.
"""
import csv
import datetime as dt
import json
import math
import os
import statistics
import urllib.request

BASE = "https://api.binance.us/api/v3"
MIN_QUOTE_VOLUME = 100_000  # USD traded in 24h; filters out illiquid coins
MIN_TRADES = 1_000  # trades in 24h; a flat 4000 count is a market-maker bot, not real activity
QUOTES = ("USDT", "USD")
STABLE = {"USDC", "USDT", "DAI", "FDUSD", "TUSD", "PYUSD", "USD1", "EUR", "BUSD"}


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=20) as r:
        return json.load(r)


def main():
    # Pairs in BREAK status are halted or being delisted: their wild swings are traps.
    info = {s["symbol"]: s for s in get("/exchangeInfo")["symbols"]}
    best = {}  # one pair per coin: the more liquid of its USD / USDT pairs
    for t in get("/ticker/24hr"):
        s = info.get(t["symbol"])
        if not s or s["status"] != "TRADING" or s["quoteAsset"] not in QUOTES:
            continue
        if s["baseAsset"] in STABLE or float(t["quoteVolume"]) < MIN_QUOTE_VOLUME:
            continue
        if t["count"] < MIN_TRADES or t["count"] == 4000:
            continue
        b = s["baseAsset"]
        if b not in best or float(t["quoteVolume"]) > float(best[b]["quoteVolume"]):
            best[b] = t
    tickers = list(best.values())
    rows = []
    for t in tickers:
        sym = t["symbol"]
        # 7 days of hourly candles
        k = get(f"/klines?symbol={sym}&interval=1h&limit=168")
        closes = [float(c[4]) for c in k]
        if len(closes) < 100:
            continue
        rets = [math.log(b / a) for a, b in zip(closes, closes[1:])]
        vol_h = statistics.pstdev(rets)
        last = closes[-1]
        mean_7d = statistics.fmean(closes)
        rows.append({
            "symbol": sym,
            "price": last,
            "chg_24h_pct": float(t["priceChangePercent"]),
            "vol_24h_usd": round(float(t["quoteVolume"])),
            # hourly volatility scaled to a day, in %
            "daily_vol_pct": round(vol_h * math.sqrt(24) * 100, 2),
            # how far price sits from its 7-day average, in %
            "dev_from_7d_mean_pct": round((last / mean_7d - 1) * 100, 2),
            "range_7d_pct": round((max(closes) / min(closes) - 1) * 100, 2),
        })
    rows.sort(key=lambda r: r["daily_vol_pct"], reverse=True)

    os.makedirs("trading-lab/data", exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H%MZ")
    out = f"trading-lab/data/screen-{stamp}.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} liquid pairs screened -> {out}")
    for r in rows[:15]:
        print(r)


if __name__ == "__main__":
    main()
