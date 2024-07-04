#!/usr/bin/env python3
""" Write a function that takes str and int or float and return tuple"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function returns tuple as str and float"""
    return (k, float(v**2))
