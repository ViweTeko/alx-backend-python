#!/usr/bin/env python3
""" This script executes multiple coroutines simultaneously"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays"""
    delays = [wait_random(max_delay) for a in range(n)]

    return [await delay for delay in asyncio.as_completed(delays)]