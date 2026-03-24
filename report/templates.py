"""Romanian report templates matching the user's template format."""

REPORT_HEADER = """======================================================
   RAPORT ZILNIC COMMODITIES - {date}
======================================================
Surse: https://www.investing.com/ https://www.marketwatch.com/
       https://www.bloomberg.com/europe https://www.reuters.com/
"""

COMMODITY_SECTION = """
------------------------------------------------------
   {commodity_name}
------------------------------------------------------

- {commodity_name} se afla in momentul de fata la valoarea de {current_price} $

Pe parcursul zilei de ieri s-a tranzactionat intre {yesterday_low} si {yesterday_high}, \
inregistrand pe parcursul sesiunii de tranzactionare o {direction_session} de \
{session_change_usd} $, procentual {session_change_pct} %

De la inceputul zilei (ora 00), avem o miscare de {daily_change_usd} $, \
astfel {name_short} are in momentul de fata un {direction_daily} de {daily_change_abs}$

Ca zone de interes, avem un suport la valoarea de {support} $ si o rezistenta \
la valoarea de {resistance} $
"""

NEWS_HEADER = """
Stiri si informatii relevante:
"""

NEWS_ITEM = "  - {text}"

TOPICS_HEADER = """
Teme de interes zilnic:
"""

TOPIC_ITEM = "  + {text}"

REPORT_FOOTER = """
======================================================
   Sfarsit raport - {date}
======================================================
"""
