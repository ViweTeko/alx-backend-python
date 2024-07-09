#!/usr/bin/env python3
""" Write a coroutine that takes no args"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The generator"""
    for a in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
