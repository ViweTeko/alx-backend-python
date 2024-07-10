#!/usr/bin/env python3
""" Continuation of previous script"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start = time.perf_counter()
    task = [async_comprehension() for a in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return (end - start)
