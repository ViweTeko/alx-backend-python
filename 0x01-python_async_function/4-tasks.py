#!/usr/bin/env python3
""" Task number 4"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays"""
    delays = [task_wait_random(max_delay) for a in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
