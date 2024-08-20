#!/usr/bin/env python3
"""contains the async_comprehension coroutine"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """gets 10 random numbers using an async comprehension,
       then return the 10 random numbers.
    """
    return [n async for n in async_generator()]
