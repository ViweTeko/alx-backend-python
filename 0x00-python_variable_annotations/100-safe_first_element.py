#!/usr/bin/env python3
""" Argument the following code with correct duck-typed annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Putting correct duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
