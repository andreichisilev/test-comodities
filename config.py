"""Commodity definitions, tickers, and news configuration."""

COMMODITIES = {
    "XAU-USD": {
        "ticker": "GC=F",
        "name_ro": "XAU - USD (Gold)",
        "name_short": "XAU - USD",
        "news_keywords": ["gold price", "central bank gold reserves", "gold mining"],
        "news_topics_ro": [
            "Stire despre Gold, rezerve bancare ale bancilor centrale, companii care extrag. "
            "PBoC a extins achizitiile de aur pentru a 15-a luna consecutiva in ianuarie. "
            "Banca Nationala a Poloniei a fost cel mai mare cumparator in 2025, adaugand 102 tone",
            "Bancile centrale detin acum mai multe rezerve in aur decat in obligatiuni "
            "ale Trezoreriei SUA (conform WisdomTree). Cererea ramane ridicata pe fondul "
            "tensiunilor geopolitice din Orientul Mijlociu",
            "Pretul aurului a depasit $5,000/uncie in ianuarie 2026, atingand un maxim "
            "istoric de $5,589.38. J.P. Morgan prognozeaza $5,055/uncie pana la sfarsitul lui 2026"
        ],
    },
    "XAG-USD": {
        "ticker": "SI=F",
        "name_ro": "XAG - USD (Silver)",
        "name_short": "XAG - USD",
        "news_keywords": ["silver price", "silver mining", "silver industrial demand"],
        "news_topics_ro": [
            "Stire despre Silver, rezerve bancare ale bancilor centrale, companii care extrag. "
            "Argintul a scazut cu aproape 50% de la maximele din februarie si cu peste 27% "
            "doar in martie, pe fondul cresterii randamentelor obligatiunilor",
            "Pretul argintului a revenit la $70 dupa declaratiile lui Trump privind "
            "\"discutii bune si productive\" cu Iranul, stabilizand pietele",
            "Indicatorii tehnici arata un semnal \"Strong Sell\" pe termen scurt. "
            "Perspectiva ramane incerta, influentata de piata energiei"
        ],
    },
    "PALLADIUM": {
        "ticker": "PA=F",
        "name_ro": "Palladium",
        "name_short": "Palladium",
        "news_keywords": ["palladium price", "palladium catalyst", "palladium supply"],
        "news_topics_ro": [
            "Stire despre Palladium, rezerve bancare ale bancilor centrale, companii care extrag. "
            "Paladiul a urcat peste $1,800/uncie in februarie, dupa o scadere la $1,573",
            "Ingrijorari pe partea de oferta din cauza revizuirii acordului comercial "
            "Canada-SUA-Mexic si amenintarilor tarifare de 50%, Canada fiind un furnizor "
            "cheie global de paladiu",
            "Dupa atingerea unui minim de 7 ani la $31.74/gram la inceputul lui 2025, "
            "paladiul a recuperat 74.48% pe parcursul anului 2025"
        ],
    },
    "CRUDE-OIL": {
        "ticker": "CL=F",
        "name_ro": "Crude Oil (WTI)",
        "name_short": "WTI",
        "news_keywords": ["crude oil price", "OPEC production", "US crude inventories"],
        "news_topics_ro": [
            "Stire despre conflicte in tarile arabe. Transporturile de petrol prin Stramtoarea "
            "Hormuz au scazut de la ~20 mb/zi la un fir, tarile din Golf reducand productia "
            "cu cel putin 10 mb/zi. Brent a atins $120/bbl inainte de a scadea la ~$92",
            "OPEC+ a decis pe 1 martie 2026 o crestere a productiei cu 206,000 barili/zi "
            "pentru aprilie. Arabia Saudita a crescut productia cu 640,000 b/zi - cea mai "
            "mare crestere din iunie. OPEC a pompat 29.52 milioane barili/zi",
            "In fiecare miercuri se publica inventarele de petrol ale SUA (Crude Oil Inventories). "
            "Ultima raportare (13 martie): stocuri +6.2 mil barili la 449.3 mil bbl, "
            "~1% sub media pe 5 ani. Urmatorul raport: 25 martie 2026",
            "Tarile IEA au decis eliberarea a 400 milioane barili din rezervele de urgenta "
            "pentru a atenua impactul intreruperilor de aprovizionare"
        ],
    },
    "NATURAL-GAS": {
        "ticker": "NG=F",
        "name_ro": "Nat Gas",
        "name_short": "Nat Gas",
        "news_keywords": ["natural gas price", "gas storage US", "LNG supply"],
        "news_topics_ro": [
            "Stire despre conflicte in tarile arabe. Rachetele iraniene au avariat Ras Laffan, "
            "cel mai mare hub LNG din lume (~20% din oferta globala). Pretul gazului TTF "
            "in Europa a crescut cu 32% peste noapte",
            "In fiecare JOI se publica inventarele de gaz ale SUA (US Natural Gas Storage). "
            "Ultima raportare (6 martie): stocuri la 1,848 Bcf, scadere de 38 Bcf. "
            "Nivelul este cu 141 Bcf peste anul trecut, dar cu 17 Bcf sub media pe 5 ani",
            "Productia de gaz natural in SUA este asteptata sa creasca la 118 Bcf/zi "
            "in 2026 si 121 Bcf/zi in 2027 (fata de 116 Bcf/zi in 2025). "
            "EIA prognozeaza pretul Henry Hub la ~$3.80/MMBtu in medie pentru 2026",
            "Preturile Henry Hub raman izolate de presiunile inflationiste globale "
            "cauzate de conflictul din Orientul Mijlociu, ramanand in jurul a $3/MMBtu"
        ],
    },
}
