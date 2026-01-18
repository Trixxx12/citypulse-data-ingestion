from .config import OPENWEATHER_API_KEY, DEFAULT_CITY, WEATHER_DIR, RUN_LOG_PATH
from .http_client import get_json
from .utils import save_json
from .logger import write_run_log


def fetch_openweather(city: str) -> dict:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }
    return get_json(url, params=params)


def main():
    city = DEFAULT_CITY
    print(f"[weather] fetching city={city}")

    try:
        payload = fetch_openweather(city)

        saved_path = save_json(
            WEATHER_DIR,
            prefix="weather",
            payload=payload,
            suffix=city,
        )

        write_run_log(
            log_path=RUN_LOG_PATH,
            source="weather",
            status="success",
            output_file=str(saved_path),
            records=1,
            message=f"city={city}",
        )

        print(f"[weather] saved -> {saved_path}")

    except Exception as e:
        write_run_log(
            log_path=RUN_LOG_PATH,
            source="weather",
            status="failed",
            message=str(e),
        )
        print(f"[weather] failed: {e}")
        return  # important: stop here so we don't continue


if __name__ == "__main__":
    main()
