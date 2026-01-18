from src.config import NEWS_DIR, RUN_LOG_PATH, ALERTS_LOG_PATH
from src.http_client import get_json
from src.utils import save_json
from src.logger import write_run_log, write_alert


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

    try:
        payload = fetch_gdelt_articles(query=query, timespan=timespan, maxrecords=25)

        count = 0
        if isinstance(payload, dict) and "articles" in payload and isinstance(payload["articles"], list):
            count = len(payload["articles"])

        saved_path = save_json(NEWS_DIR, prefix="news", payload=payload, suffix=query)

        write_run_log(
            log_path=RUN_LOG_PATH,
            source="news",
            status="success",
            output_file=str(saved_path),
            records=count,
            message=f"query={query} timespan={timespan}",
        )

    except Exception as e:
        write_run_log(
            log_path=RUN_LOG_PATH,
            source="news",
            status="failed",
            message=str(e),
        )
        write_alert(
            alert_path=ALERTS_LOG_PATH,
            source="weather",
            message=str(e),
        )
        raise  # optional: remove if you don't want the runner to stop


if __name__ == "__main__":
    main()
