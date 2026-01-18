
from pathlib import Path
import os
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Manila")


DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
WEATHER_DIR = RAW_DIR / "weather"
NEWS_DIR = RAW_DIR / "news"


HTTP_TIMEOUT_SECONDS = 10


