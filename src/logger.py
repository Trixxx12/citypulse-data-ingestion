# src/logger.py
import csv
from datetime import datetime, timezone
from pathlib import Path


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def write_run_log(
    log_path: Path,
    source: str,
    status: str,
    output_file: str = "",
    records: int | None = None,
    message: str = "",
    ) -> None:
    """
    Append one row to a CSV run log.
    """
    log_path.parent.mkdir(parents=True, exist_ok=True)

    file_exists = log_path.exists()
    headers = ["ts_utc", "source", "status", "records", "output_file", "message"]

    row = {
        "ts_utc": utc_now_iso(),
        "source": source,
        "status": status,
        "records": "" if records is None else str(records),
        "output_file": output_file,
        "message": message,
    }

    with log_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
        
def write_alert(alert_path: Path, source: str, message: str) -> None:
    alert_path.parent.mkdir(parents=True, exist_ok=True)
    line = f"{utc_now_iso()} | ALERT | {source} | {message}\n"
    with alert_path.open("a", encoding="utf-8") as f:
        f.write(line)

