#!/usr/bin/env python3
""" Write a function which takes list of ints and floats and returns sum"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """This function returns the sum as float"""
    return sum(mxd_list)
