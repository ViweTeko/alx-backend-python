#!/usr/bin/env python3
"""Annotate below function's parameters"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating the above funtion"""
    return [(i, len(i)) for i in lst]
