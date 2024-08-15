#!/usr/bin/env python3
"""contains safely_get_value function"""
from typing import Any, Mapping, Optional, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """a function that returns the value of a key in a dictionary if key is
       present else returns the value in default which defaults to None
    """
    if key in dct:
        return dct[key]
    else:
        return default
