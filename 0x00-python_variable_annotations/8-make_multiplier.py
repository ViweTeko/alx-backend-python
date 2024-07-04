#!/usr/bin/env python3
""" Write a function that takes a float as arg and return float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function returns function that multiplies"""
    def floating(x: float) -> float:
        return multiplier * x
    
    return floating
