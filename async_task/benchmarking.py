__author__ = "Саргсян Татев"

import asyncio
import time
import statistics
from async_task.http_client import sync_fetch, async_fetch

def run_sync(urls: list[str]) -> float:
    """Запустить sync_fetch, вернуть затраченное время в секундах."""
    start = time.perf_counter()
    sync_fetch(urls)
    return time.perf_counter() - start


def run_async(urls: list[str]) -> float:
    """Запустить async_fetch в event loop, вернуть затраченное время."""
    start = time.perf_counter()
    asyncio.run(async_fetch(urls))
    return time.perf_counter() - start


def benchmark(urls: list[str], runs: int = 3) -> dict:
    """Запустить оба варианта runs раз, вернуть статистику."""
    sync_times: list[float] = []
    async_times: list[float] = []

    for i in range(1, runs + 1):
        print(f"  Прогон {i}/{runs}: ", flush=True)

        t_sync = run_sync(urls)
        sync_times.append(t_sync)
        print(f"sync={t_sync:.2f}s  ", flush=True)

        t_async = run_async(urls)
        async_times.append(t_async)
        print(f"async={t_async:.2f}s", flush=True)

    return {
        "sync_times":   sync_times,
        "async_times":  async_times,
        "sync_mean":    statistics.mean(sync_times),
        "async_mean":   statistics.mean(async_times),
        "sync_median":  statistics.median(sync_times),
        "async_median": statistics.median(async_times),
    }