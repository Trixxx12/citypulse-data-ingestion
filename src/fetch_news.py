# src/fetch_news.py
from src.config import NEWS_DIR
from src.http_client import get_json
from src.utils import save_json


def fetch_gdelt_articles(query: str = "Manila", timespan: str = "1d", maxrecords: int = 25) -> dict:
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": query,
        "mode": "ArtList",
        "format": "json",
        "sort": "DateDesc",
        "timespan": timespan,
        "maxrecords": maxrecords,
    }
    return get_json(url, params=params)


def main():
    query = "Manila"
    timespan = "1d"

    print(f"[news] fetching gdelt query={query} timespan={timespan}")

    try:
        payload = fetch_gdelt_articles(query=query, timespan=timespan, maxrecords=25)
        saved_path = save_json(NEWS_DIR, prefix="news", payload=payload, suffix=query)
        print(f"[news] saved -> {saved_path}")
    except Exception as e:
        print(f"[news] failed: {e}")


if __name__ == "__main__":
    main()
