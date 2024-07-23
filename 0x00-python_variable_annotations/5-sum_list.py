#!/usr/bin/env python3
""" Sum List """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sum list """
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
