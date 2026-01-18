
from .config import (
    OPEN_WEATHER_API_KEY,
    DEFAULT_CITY,
    WEATHER_DIR,
)
from .http_client import get_json
from .utils import save_json


def fetch_current_weather(city: str) -> dict:
    if not OPEN_WEATHER_API_KEY:
        raise ValueError("OPEN_WEATHER_API_KEY is missing. Put it in .env")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPEN_WEATHER_API_KEY, "units": "metric"}
    return get_json(url, params=params)


def main():
    city = DEFAULT_CITY
    print(f"[weather] fetching city={city}")

    try:
        payload = fetch_current_weather(city)
        saved_path = save_json(WEATHER_DIR, prefix="weather", payload=payload, suffix=city)
        print(f"[weather] saved -> {saved_path}")
    except Exception as e:
        print(f"[weather] failed: {e}")


if __name__ == "__main__":
    main()
