#!/usr/bin/env python3
"""contains make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that returns a multiplier function"""
    def f(n: float):
        """a function that multiplies a float by multiplier"""
        return n * multiplier
    return f
