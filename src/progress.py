from datetime import UTC, datetime


def log_step(step: int, total: int, title: str, message: str) -> None:
    print(f"{timestamp()} [{step}/{total}] {title} - {message}", flush=True)


def log_info(scope: str, message: str) -> None:
    print(f"{timestamp()} [{scope}] {message}", flush=True)


def timestamp() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")
