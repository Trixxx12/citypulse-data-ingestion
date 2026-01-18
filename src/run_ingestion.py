import os
from pathlib import Path

print("[runner] CWD:", os.getcwd())
print("[runner] FILE:", Path(__file__).resolve())
# src/run_ingestion.py
from src.fetch_weather import main as weather_main
from src.fetch_news import main as news_main


def main():
    print("[runner] starting ingestion run...")

    print("[runner] weather...")
    weather_main()

    print("[runner] news...")
    news_main()

    print("[runner] done.")
    

if __name__ == "__main__":
    main()
