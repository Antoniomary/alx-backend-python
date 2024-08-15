#!/usr/bin/env python3
"""contains to_kv function"""
from typing import Tuple


def to_kv(k: str, v: [int, float]) -> Tuple[str, float]:
    """a function that returns a tuple"""
    return (k, v ** 2)
