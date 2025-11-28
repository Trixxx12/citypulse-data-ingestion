# src/fetch_weather.py

import json
from datetime import datetime, timezone
from pathlib import Path
import requests

from config import WEATHER_DIR

def fetch_current_weather(lat=14.5995, lon=120.9842):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def save_weather_json(data):
    WEATHER_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filename = f"weather_{timestamp}.json"
    filepath = WEATHER_DIR / filename

    with filepath.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return str(filepath)

def main():
    try:
        data = fetch_current_weather()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return

    saved_path = save_weather_json(data)
    print(f"Saved weather data to {saved_path}")

if __name__ == "__main__":
    main()
