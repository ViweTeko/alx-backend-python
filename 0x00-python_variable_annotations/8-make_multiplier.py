#!/usr/bin/env python3
""" Write a function that takes a float as arg and return float"""
from typing return Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function returns function that multiplies"""
    return lambda x: x * multiplier
