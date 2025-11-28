from dotenv import load_dotenv
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).parent.parent

load_dotenv(PROJECT_ROOT / '.env')

OPEN_WEATHER_API_KEY = os.getenv('a6e5c19164ddb2c8d22956854cb6aa15')
DEFAULT_CITY = os.getenv('DEFAULT_CITY', 'Manila')

DATA_DIR = PROJECT_ROOT / 'data'
RAW_DIR = DATA_DIR / 'raw'
WEATHER_DIR = RAW_DIR / 'weather'