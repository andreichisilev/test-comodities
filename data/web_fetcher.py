"""Fetch commodity data by scraping publicly available financial pages."""

import json
import re

import requests
from bs4 import BeautifulSoup

# User agent to avoid basic bot blocks
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

# TradingEconomics commodity pages
COMMODITY_URLS = {
    "XAU-USD": "https://tradingeconomics.com/commodity/gold",
    "XAG-USD": "https://tradingeconomics.com/commodity/silver",
    "PALLADIUM": "https://tradingeconomics.com/commodity/palladium",
    "CRUDE-OIL": "https://tradingeconomics.com/commodity/crude-oil",
    "NATURAL-GAS": "https://tradingeconomics.com/commodity/natural-gas",
}


def scrape_commodity_data(commodity_key: str) -> dict | None:
    """Scrape commodity price data from TradingEconomics.

    Returns dict with keys:
        current_price, yesterday_high, yesterday_low, yesterday_close, today_open
    Or None on failure.
    """
    url = COMMODITY_URLS.get(commodity_key)
    if not url:
        return None

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Try to extract price from the page
        price_elem = soup.find("div", {"id": "ctl00_ContentPlaceHolder1_ctl02_pnlLast"})
        if price_elem:
            price_text = price_elem.get_text(strip=True)
            current_price = float(re.sub(r"[^\d.]", "", price_text))
        else:
            return None

        return {
            "current_price": current_price,
        }
    except Exception as e:
        print(f"[WARN] Failed to scrape {commodity_key} from {url}: {e}")
        return None


def scrape_all_commodities(commodities: dict) -> dict:
    """Scrape data for all commodities."""
    results = {}
    for key in commodities:
        data = scrape_commodity_data(key)
        results[key] = data
    return results
