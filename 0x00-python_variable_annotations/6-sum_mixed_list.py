#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """ Returns the sum of a list of integers and floats """
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
