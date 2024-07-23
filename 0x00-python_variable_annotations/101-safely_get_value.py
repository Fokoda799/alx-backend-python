#!/usr/bin/env python3
""" More involved type annotations """
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
M = Mapping
A = Any
U = Union


def safely_get_value(dct: M, key: A, default: U[T, None] = None) -> U[A, T]:
    """ Returns the value of a key in a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default
