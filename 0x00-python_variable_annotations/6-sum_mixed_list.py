#!/usr/bin/env python3
"""Complex annotations"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns a sum of elements in mxd_lst"""
    return sum(mxd_lst)
