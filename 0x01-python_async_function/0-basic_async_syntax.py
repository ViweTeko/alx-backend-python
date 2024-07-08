#!/usr/bin/env python3
""" This script writes an async coroutine that waits for a random delay"""
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This waits for random delay"""
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay