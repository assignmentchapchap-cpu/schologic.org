"""Make and score 6h / 12h / 24h price forecasts, using Binance.US public data.

Make:   python3 trading-lab/forecast.py make '{"ZECUSDT": [50, 50, 50], ...}' [run_id]
        The numbers are our chance (%) that price is HIGHER than now after 6h, 12h, 24h.
Score:  python3 trading-lab/forecast.py score
        Fills in outcomes for any forecast whose time has passed.

Method (kept simple on purpose, so beginners can follow it):
- Centre = today's price. Over hours, crypto is close to a coin flip, so we don't pretend
  to know the direction; any view goes into the "chance higher" number instead.
- Ranges come from how much the coin normally moves: hourly volatility over the last
  30 days, scaled by the square root of the hours ahead. The 68% range is +/-1 of these
  "typical moves", the 90% range is +/-1.645. If the method is honest, the price should
  land inside the 68% range about 2 times in 3, and inside the 90% range 9 times in 10.
"""
import csv
import datetime as dt
import json
import math
import os
import statistics
import sys
import urllib.request

BASE = "https://api.binance.us/api/v3"
FILE = "trading-lab/forecasts.csv"
HORIZONS = (6, 12, 24)
FIELDS = [
    "run_id", "symbol", "made_at_utc", "horizon_h", "due_at_utc", "price_at_forecast",
    "typical_move_pct", "range68_low", "range68_high", "range90_low", "range90_high",
    "chance_higher_pct", "price_at_due", "change_pct", "in_68", "in_90",
    "direction_right", "brier",
]


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=20) as r:
        return json.load(r)


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, newline="") as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def fmt(x):
    return f"{x:.6g}"


def make(leans, run_id):
    now = dt.datetime.now(dt.timezone.utc).replace(second=0, microsecond=0)
    rows = load()
    for sym, chances in leans.items():
        k = get(f"/klines?symbol={sym}&interval=1h&limit=720")
        closes = [float(c[4]) for c in k]
        vol_h = statistics.pstdev(math.log(b / a) for a, b in zip(closes, closes[1:]))
        price = float(get(f"/ticker/price?symbol={sym}")["price"])
        for h, chance in zip(HORIZONS, chances):
            s = vol_h * math.sqrt(h)
            rows.append({
                "run_id": run_id, "symbol": sym, "made_at_utc": now.isoformat(),
                "horizon_h": h, "due_at_utc": (now + dt.timedelta(hours=h)).isoformat(),
                "price_at_forecast": fmt(price), "typical_move_pct": f"{s * 100:.2f}",
                "range68_low": fmt(price * math.exp(-s)), "range68_high": fmt(price * math.exp(s)),
                "range90_low": fmt(price * math.exp(-1.645 * s)),
                "range90_high": fmt(price * math.exp(1.645 * s)),
                "chance_higher_pct": chance,
            })
    save(rows)
    for r in rows:
        if r["run_id"] == run_id:
            print({k: r[k] for k in FIELDS[1:12]})


def score():
    now = dt.datetime.now(dt.timezone.utc)
    rows = load()
    for r in rows:
        due = dt.datetime.fromisoformat(r["due_at_utc"])
        if r.get("price_at_due") or due > now:
            continue
        # close of the 1-minute candle that starts at the due time
        ms = int(due.timestamp() * 1000)
        k = get(f"/klines?symbol={r['symbol']}&interval=1m&startTime={ms}&limit=1")
        if not k:
            continue
        p0, p = float(r["price_at_forecast"]), float(k[0][4])
        up = p > p0
        q = float(r["chance_higher_pct"]) / 100
        r.update({
            "price_at_due": fmt(p), "change_pct": f"{(p / p0 - 1) * 100:+.2f}",
            "in_68": float(r["range68_low"]) <= p <= float(r["range68_high"]),
            "in_90": float(r["range90_low"]) <= p <= float(r["range90_high"]),
            # a 50% forecast takes no side, so it is neither right nor wrong
            "direction_right": "" if q == 0.5 else (q > 0.5) == up,
            # Brier score: 0 is perfect, 0.25 is what a coin flip earns
            "brier": f"{(q - up) ** 2:.3f}",
        })
    save(rows)
    done = [r for r in rows if r.get("price_at_due")]
    print(f"{len(done)} of {len(rows)} forecasts scored")
    for r in done:
        print(r["run_id"], r["symbol"], f"{r['horizon_h']}h", r["change_pct"],
              "in68" if r["in_68"] == "True" or r["in_68"] is True else "out68",
              "dir:", r["direction_right"] or "no call", "brier:", r["brier"])


if __name__ == "__main__":
    if sys.argv[1] == "make":
        make(json.loads(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else "run")
    else:
        score()
