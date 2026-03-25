"""Generate HTML version of the commodity report for GitHub Pages."""

from datetime import datetime

from analysis.changes import compute_changes
from config import COMMODITIES
from data.market_data import get_market_data, set_manual_data
from data.news_fetcher import fetch_news


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raport Zilnic Commodities - {date}</title>
    <style>
        :root {{
            --bg: #1a1a2e;
            --card-bg: #16213e;
            --accent: #e94560;
            --gold: #ffd700;
            --silver: #c0c0c0;
            --green: #00b894;
            --red: #e74c3c;
            --text: #eee;
            --text-muted: #a0a0b0;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        header {{
            text-align: center;
            padding: 30px 0;
            border-bottom: 2px solid var(--accent);
            margin-bottom: 30px;
        }}
        header h1 {{ font-size: 2em; color: var(--gold); }}
        header .date {{ color: var(--text-muted); margin-top: 5px; font-size: 1.1em; }}
        header .sources {{
            color: var(--text-muted);
            font-size: 0.85em;
            margin-top: 10px;
        }}
        header .sources a {{ color: var(--accent); text-decoration: none; }}
        header .sources a:hover {{ text-decoration: underline; }}
        .commodity-card {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 25px;
            border-left: 4px solid var(--gold);
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}
        .commodity-card.silver {{ border-left-color: var(--silver); }}
        .commodity-card.palladium {{ border-left-color: #b8a9c9; }}
        .commodity-card.oil {{ border-left-color: #e67e22; }}
        .commodity-card.gas {{ border-left-color: #3498db; }}
        .commodity-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }}
        .commodity-name {{ font-size: 1.5em; font-weight: bold; }}
        .commodity-price {{
            font-size: 2em;
            font-weight: bold;
        }}
        .price-up {{ color: var(--green); }}
        .price-down {{ color: var(--red); }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }}
        .stat-box {{
            background: rgba(255,255,255,0.05);
            padding: 12px;
            border-radius: 8px;
        }}
        .stat-label {{ color: var(--text-muted); font-size: 0.85em; }}
        .stat-value {{ font-size: 1.2em; font-weight: bold; margin-top: 4px; }}
        .news-section {{ margin-top: 20px; }}
        .news-section h3 {{
            color: var(--accent);
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        .news-item {{
            background: rgba(255,255,255,0.03);
            padding: 10px 15px;
            border-radius: 6px;
            margin-bottom: 8px;
            font-size: 0.95em;
            border-left: 2px solid var(--accent);
        }}
        .topic-item {{
            padding: 8px 15px;
            margin-bottom: 6px;
            font-size: 0.9em;
            color: var(--text-muted);
            border-left: 2px solid var(--gold);
            background: rgba(255,215,0,0.03);
            border-radius: 0 6px 6px 0;
        }}
        footer {{
            text-align: center;
            padding: 30px 0;
            color: var(--text-muted);
            border-top: 1px solid rgba(255,255,255,0.1);
            margin-top: 20px;
            font-size: 0.9em;
        }}
        @media (max-width: 600px) {{
            .commodity-header {{ flex-direction: column; align-items: flex-start; }}
            .commodity-price {{ font-size: 1.5em; }}
            body {{ padding: 10px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>RAPORT ZILNIC COMMODITIES</h1>
            <div class="date">{date}</div>
            <div class="sources">
                Surse:
                <a href="https://www.investing.com/">Investing.com</a> |
                <a href="https://www.marketwatch.com/">MarketWatch</a> |
                <a href="https://www.bloomberg.com/europe">Bloomberg</a> |
                <a href="https://www.reuters.com/">Reuters</a>
            </div>
        </header>

        {commodity_sections}

        <footer>
            Raport generat automat - {date}<br>
            Datele sunt cu titlu informativ si nu constituie sfaturi de investitii.
        </footer>
    </div>
</body>
</html>"""

COMMODITY_CARD = """
        <div class="commodity-card {card_class}">
            <div class="commodity-header">
                <span class="commodity-name">{commodity_name}</span>
                <span class="commodity-price {price_class}">{current_price} $</span>
            </div>

            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-label">Range ieri</div>
                    <div class="stat-value">{yesterday_low} - {yesterday_high} $</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Schimbare sesiune</div>
                    <div class="stat-value {session_class}">{direction_symbol}{session_change_usd} $ ({session_change_pct}%)</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Schimbare zilnica (de la ora 00)</div>
                    <div class="stat-value {daily_class}">{direction_daily}{daily_change_abs} $</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Suport / Rezistenta</div>
                    <div class="stat-value">{support} $ / {resistance} $</div>
                </div>
            </div>

            {news_html}
            {topics_html}
        </div>"""


CARD_CLASSES = {
    "XAU-USD": "",
    "XAG-USD": "silver",
    "PALLADIUM": "palladium",
    "CRUDE-OIL": "oil",
    "NATURAL-GAS": "gas",
}


def generate_html_report() -> str:
    """Generate the full HTML commodity report."""
    today = datetime.now().strftime("%d.%m.%Y")

    all_data = get_market_data(COMMODITIES)
    manual_fallbacks = _get_manual_fallbacks()
    for key in COMMODITIES:
        if all_data.get(key) is None and key in manual_fallbacks:
            all_data[key] = manual_fallbacks[key]

    sections = []

    for key, cfg in COMMODITIES.items():
        print(f"Se proceseaza {cfg['name_ro']}...")
        data = all_data.get(key)
        if data is None:
            continue

        changes = compute_changes(
            data["current_price"],
            data["yesterday_close"],
            data["today_open"],
        )

        # Pivot point support/resistance
        h = data["yesterday_high"]
        l = data["yesterday_low"]
        c = data["yesterday_close"]
        pp = (h + l + c) / 3
        support = round(2 * pp - h, 2)
        resistance = round(2 * pp - l, 2)

        # News
        try:
            news = fetch_news(cfg["news_keywords"], max_items=3)
        except Exception:
            news = []

        news_html = ""
        if news:
            items = "".join(
                f'<div class="news-item">{item["title"]} ({item["source"]})</div>'
                for item in news
            )
            news_html = f'<div class="news-section"><h3>Stiri recente</h3>{items}</div>'

        topics_html = ""
        if cfg.get("news_topics_ro"):
            items = "".join(
                f'<div class="topic-item">{t}</div>'
                for t in cfg["news_topics_ro"]
            )
            topics_html = f'<div class="news-section"><h3>Teme de interes zilnic</h3>{items}</div>'

        session_dir = changes["direction_session"]
        price_class = "price-up" if changes["session_change_usd"] >= 0 else "price-down"
        session_class = "price-up" if changes["session_change_usd"] >= 0 else "price-down"
        daily_class = "price-up" if changes["daily_change_usd"] >= 0 else "price-down"
        direction_symbol = "+" if changes["session_change_usd"] >= 0 else "-"

        card = COMMODITY_CARD.format(
            card_class=CARD_CLASSES.get(key, ""),
            commodity_name=cfg["name_ro"],
            current_price=data["current_price"],
            price_class=price_class,
            yesterday_low=data["yesterday_low"],
            yesterday_high=data["yesterday_high"],
            session_change_usd=abs(changes["session_change_usd"]),
            session_change_pct=abs(changes["session_change_pct"]),
            session_class=session_class,
            direction_symbol=direction_symbol,
            daily_change_abs=changes["daily_change_abs"],
            daily_class=daily_class,
            direction_daily=changes["direction_daily"],
            support=support,
            resistance=resistance,
            news_html=news_html,
            topics_html=topics_html,
        )
        sections.append(card)

    return HTML_TEMPLATE.format(
        date=today,
        commodity_sections="\n".join(sections),
    )


def _get_manual_fallbacks() -> dict:
    """Manual fallback data from web research."""
    return {
        "XAU-USD": set_manual_data(
            commodity_key="XAU-USD",
            current_price=4388.19,
            yesterday_high=4536.46,
            yesterday_low=4099.55,
            yesterday_close=4491.15,
            today_open=4388.19,
        ),
        "XAG-USD": set_manual_data(
            commodity_key="XAG-USD",
            current_price=69.28,
            yesterday_high=70.76,
            yesterday_low=60.98,
            yesterday_close=67.79,
            today_open=69.15,
        ),
        "PALLADIUM": set_manual_data(
            commodity_key="PALLADIUM",
            current_price=1452.25,
            yesterday_high=1480.00,
            yesterday_low=1392.00,
            yesterday_close=1445.20,
            today_open=1445.20,
        ),
        "CRUDE-OIL": set_manual_data(
            commodity_key="CRUDE-OIL",
            current_price=88.67,
            yesterday_high=101.66,
            yesterday_low=84.59,
            yesterday_close=98.23,
            today_open=91.61,
        ),
        "NATURAL-GAS": set_manual_data(
            commodity_key="NATURAL-GAS",
            current_price=2.90,
            yesterday_high=3.07,
            yesterday_low=2.80,
            yesterday_close=3.07,
            today_open=2.90,
        ),
    }
