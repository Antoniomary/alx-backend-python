#!/usr/bin/env python3
"""contains safe_first_element function"""
from typing import Any, Optional, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """returns the 1st element of an iterable if any is passed or None"""
    if lst:
        return lst[0]
    else:
        return None
