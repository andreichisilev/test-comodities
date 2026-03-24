"""Fetch commodity news headlines via Google News RSS."""

from datetime import datetime, timedelta, timezone

import feedparser


def fetch_news(keywords: list[str], max_items: int = 5) -> list[dict]:
    """Fetch recent news headlines for given keywords.

    Returns list of dicts with keys: title, source, published, url
    """
    all_entries = []

    for keyword in keywords:
        query = keyword.replace(" ", "+")
        url = f"https://news.google.com/rss/search?q={query}&hl=en&gl=US&ceid=US:en"

        try:
            feed = feedparser.parse(url)
            cutoff = datetime.now(timezone.utc) - timedelta(days=2)

            for entry in feed.entries[:10]:
                published = None
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)

                if published and published < cutoff:
                    continue

                all_entries.append({
                    "title": entry.get("title", ""),
                    "source": entry.get("source", {}).get("title", "Unknown"),
                    "published": published,
                    "url": entry.get("link", ""),
                })
        except Exception as e:
            print(f"[WARN] Failed to fetch news for '{keyword}': {e}")

    # Deduplicate by title
    seen = set()
    unique = []
    for entry in all_entries:
        if entry["title"] not in seen:
            seen.add(entry["title"])
            unique.append(entry)

    # Sort by date (most recent first)
    unique.sort(key=lambda x: x["published"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)

    return unique[:max_items]
