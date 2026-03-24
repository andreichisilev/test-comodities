"""Market data management - fetches from multiple sources with manual fallback."""

from data.yahoo_fetcher import fetch_all_commodities


def get_market_data(commodities: dict) -> dict:
    """Try to fetch live data from yfinance. Returns dict keyed by commodity ID."""
    print("Se incearca descarcarea datelor live din Yahoo Finance...")
    data = fetch_all_commodities(commodities)

    # Check if we got any data
    has_data = any(v is not None for v in data.values())
    if has_data:
        print("Date live obtinute cu succes.")
        return data

    print("[INFO] Nu s-au putut obtine date live. Se folosesc datele manuale.")
    return data


def set_manual_data(commodity_key: str, current_price: float,
                    yesterday_high: float, yesterday_low: float,
                    yesterday_close: float, today_open: float) -> dict:
    """Create a manual data entry for a commodity."""
    return {
        "current_price": current_price,
        "yesterday_high": yesterday_high,
        "yesterday_low": yesterday_low,
        "yesterday_close": yesterday_close,
        "today_open": today_open,
        "history_20d": None,
    }
