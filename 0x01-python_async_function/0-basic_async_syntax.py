#!/usr/bin/env python3
"""contains wait_random function"""
from typing import Union
import asyncio
import random


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """waits for a random delay between 0 and max_delay
       (included and float value) seconds and returns it.
    """
    val: Union[int, float] = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
