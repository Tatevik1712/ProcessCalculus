__author__ = "Саргсян Татев"

BASE_URLS: list[str] = [
    "https://httpbin.org/get?id=1",
    "https://httpbin.org/get?id=2",
    "https://httpbin.org/get?id=3",
    "https://httpbin.org/ip",
    "https://httpbin.org/user-agent",
    "https://httpbin.org/headers",
    "https://httpbin.org/uuid",
    "https://httpbin.org/robots.txt",
    "https://httpbin.org/html",
]

def get_urls(n: int) -> list[str]:
    """Вернуть список из n URL (циклически из BASE_URLS)."""
    return [BASE_URLS[i % len(BASE_URLS)] for i in range(n)]