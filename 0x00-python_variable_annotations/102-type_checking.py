#!/usr/bin/env python3
"""contains safely_get_value function"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """returns a list containing each element in the argument tuple
       according to the number passed as factor which defaults to two
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
