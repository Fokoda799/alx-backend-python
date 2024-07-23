#!/usr/bin/env python3
""" Sum List """


def sum_list(input_list: list[float]) -> float:
    """ Sum list """
    sum = 0
    for num in input_list:
        sum += num
    return sum
