#!/usr/bin/python3
""" This script continues previous task"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers and return them"""
    return [a async a in async_generator()][:10]
