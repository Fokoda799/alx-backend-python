#!/usr/bin/env python3
""" Complex types - tuple """
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple """
    return (k, v ** 2)
