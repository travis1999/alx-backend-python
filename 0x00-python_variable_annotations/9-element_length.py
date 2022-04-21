#!/usr/bin/env python3
"""Complex annotations"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """get element length"""
    return [(i, len(i)) for i in lst]
