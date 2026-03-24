"""Calculate support and resistance levels using pivot points."""

import pandas as pd


def calculate_support_resistance(history: pd.DataFrame) -> dict:
    """Calculate support and resistance using classic pivot points.

    Uses yesterday's High, Low, Close to compute:
        PP = (H + L + C) / 3
        S1 = 2 * PP - H  (support)
        R1 = 2 * PP - L  (resistance)

    Returns dict with keys: support, resistance
    """
    if history is None or len(history) < 2:
        return {"support": 0.0, "resistance": 0.0}

    yesterday = history.iloc[-2]
    h = float(yesterday["High"])
    l = float(yesterday["Low"])
    c = float(yesterday["Close"])

    pp = (h + l + c) / 3
    s1 = 2 * pp - h
    r1 = 2 * pp - l

    return {
        "support": round(s1, 2),
        "resistance": round(r1, 2),
    }
