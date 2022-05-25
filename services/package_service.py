from typing import List


def package_count() -> int:
    return 240789


def release_count() -> int:
    return 170667


def latest_packages(limit: int = 5) -> List:
    return [
            {"id": "fastAPI", "summary": "A great web framework"},
            {"id": "uvicorn", "summary": "A great ASGI server"},
            {"id": "httpx", "summary": "Requests used in a async way"},
        ][:limit]