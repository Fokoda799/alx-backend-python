#!/usr/bin/env python3
""" Complex types - functions """
from typing import callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    return lambda x: x * multiplier
