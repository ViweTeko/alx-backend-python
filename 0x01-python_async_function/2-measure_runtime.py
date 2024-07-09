#!/usr/bin/env python3
""" This script measures runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures execution time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total = time.time() - start

    return total / n if n > 0 else 0
