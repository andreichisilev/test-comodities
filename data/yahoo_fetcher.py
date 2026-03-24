"""Fetch commodity price data from Yahoo Finance via yfinance, with fallback."""

import time

try:
    import yfinance as yf
    HAS_YFINANCE = True
except ImportError:
    HAS_YFINANCE = False


def fetch_commodity_data(ticker: str) -> dict | None:
    """Fetch current and historical price data for a commodity.

    Returns dict with keys:
        current_price, yesterday_high, yesterday_low, yesterday_close,
        today_open, history_20d (DataFrame)
    Or None on failure.
    """
    if not HAS_YFINANCE:
        return None

    try:
        tk = yf.Ticker(ticker)
        hist = tk.history(period="1mo", interval="1d")

        if hist.empty or len(hist) < 2:
            return None

        yesterday = hist.iloc[-2]
        today = hist.iloc[-1]

        current_price = today["Close"]
        today_open = today["Open"]

        return {
            "current_price": round(float(current_price), 2),
            "yesterday_high": round(float(yesterday["High"]), 2),
            "yesterday_low": round(float(yesterday["Low"]), 2),
            "yesterday_close": round(float(yesterday["Close"]), 2),
            "today_open": round(float(today_open), 2),
            "history_20d": hist,
        }
    except Exception as e:
        print(f"[WARN] Failed to fetch data for {ticker}: {e}")
        return None


def fetch_all_commodities(commodities: dict) -> dict:
    """Fetch data for all commodities with a small delay between requests."""
    results = {}
    for key, cfg in commodities.items():
        data = fetch_commodity_data(cfg["ticker"])
        results[key] = data
        time.sleep(0.5)
    return results
