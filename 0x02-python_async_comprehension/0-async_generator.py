#!/usr/bin/env python3
"""contains the async_generator coroutine"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """loop 10 times, each time asynchronously wait 1 second,
       then yield a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
