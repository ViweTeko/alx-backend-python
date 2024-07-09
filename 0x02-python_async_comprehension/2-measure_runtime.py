#!/usr/bin/python3
""" Continuation of previous script"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for a in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
