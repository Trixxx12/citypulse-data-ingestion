
from pathlib import Path
import os
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


OPENWEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Manila")


DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
WEATHER_DIR = RAW_DIR / "weather"
NEWS_DIR = RAW_DIR / "news"
LOGS_DIR = PROJECT_ROOT / "logs"
RUN_LOG_PATH = LOGS_DIR / "ingestion_runs.csv"
ALERTS_LOG_PATH = LOGS_DIR / "alerts.log"

HTTP_RETRY_ATTEMPTS = 3
HTTP_RETRY_BACKOFF_SECONDS = 2

HTTP_TIMEOUT_SECONDS = 10


