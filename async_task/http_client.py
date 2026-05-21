__author__ = "Саргсян Татев"

import asyncio
import httpx

def sync_fetch(urls: list[str]) -> list[int]:
    """Последовательные HTTP GET через единственный httpx.Client."""
    statuses: list[int] = []
    with httpx.Client(timeout=30) as client:
        for url in urls:
            response = client.get(url)
            print(response)
            statuses.append(response.status_code)
    return statuses


async def async_fetch(urls: list[str]) -> list[int]:
    """Параллельные HTTP GET через asyncio + httpx.AsyncClient."""
    limits = httpx.Limits(max_connections=200, max_keepalive_connections=100)
    async with httpx.AsyncClient(timeout=30, limits=limits) as client:

        async def fetch_one(url: str) -> int:
            response = await client.get(url)
            print("ASYNC", response)
            return response.status_code

        tasks = [asyncio.create_task(fetch_one(url)) for url in urls]
        statuses: list[int] = await asyncio.gather(*tasks)
    return list(statuses)