#!/usr/bin/env python3
"""Complex annotations"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of string and float"""
    return (k, v)
