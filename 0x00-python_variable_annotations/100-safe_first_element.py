#!/usr/bin/env python3
"""Complex annotations"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """anotate this"""
    if lst:
        return lst[0]
    else:
        return None
