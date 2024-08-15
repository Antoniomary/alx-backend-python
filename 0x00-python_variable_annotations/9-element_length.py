#!/usr/bin/env python3
"""contains element_length function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a function that returns a list of tuples.
       Each tuple in the list contains the element and length of the elements
       passed in the lst argument
    """
    return [(i, len(i)) for i in lst]
