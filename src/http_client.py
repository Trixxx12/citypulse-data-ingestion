# src/http_client.py
import time
import requests
from requests import Response

from src.config import HTTP_TIMEOUT_SECONDS, HTTP_RETRY_ATTEMPTS, HTTP_RETRY_BACKOFF_SECONDS


_session = requests.Session()


def get_json(url: str, params: dict | None = None, headers: dict | None = None) -> dict:
    last_error: Exception | None = None

    for attempt in range(1, HTTP_RETRY_ATTEMPTS + 1):
        try:
            resp: Response = _session.get(url, params=params, headers=headers, timeout=HTTP_TIMEOUT_SECONDS)
            resp.raise_for_status()

            try:
                return resp.json()
            except Exception as e:
                raise ValueError(f"Response was not valid JSON. url={url}") from e

        except Exception as e:
            last_error = e

            # If this was the last attempt, break and raise
            if attempt == HTTP_RETRY_ATTEMPTS:
                break

            # Backoff: 2s, 4s, 8s...
            sleep_s = HTTP_RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1))
            time.sleep(sleep_s)

    raise RuntimeError(f"GET failed after {HTTP_RETRY_ATTEMPTS} attempts. url={url}") from last_error
