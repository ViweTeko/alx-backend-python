#!/usr/bin/env python3
"""Add type annotations to function"""
from typing import Union, TypeVar, Any, Mapping

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
