#!/usr/bin/env python3
""" Element length """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples of each element and its length """
    return [(i, len(i)) for i in lst]
