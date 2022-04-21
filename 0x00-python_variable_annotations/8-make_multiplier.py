#!/usr/bin/env python3
"""Complex annotations"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make multiplier"""
    def multiply(num: float) -> float:
        "the multiplier"
        return num * multiplier
    return multiply
