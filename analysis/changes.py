"""Calculate session and daily price changes."""


def compute_changes(current_price: float, yesterday_close: float, today_open: float) -> dict:
    """Compute session and daily changes with Romanian direction labels.

    Returns dict with keys:
        session_change_usd, session_change_pct, direction_session,
        daily_change_usd, direction_daily, daily_change_abs
    """
    session_change = current_price - yesterday_close
    session_change_pct = (session_change / yesterday_close) * 100 if yesterday_close else 0

    daily_change = current_price - today_open

    return {
        "session_change_usd": round(session_change, 2),
        "session_change_pct": round(session_change_pct, 2),
        "direction_session": "crestere" if session_change >= 0 else "scadere",
        "daily_change_usd": round(daily_change, 2),
        "direction_daily": "+" if daily_change >= 0 else "-",
        "daily_change_abs": round(abs(daily_change), 2),
    }
