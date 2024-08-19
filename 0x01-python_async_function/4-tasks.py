#!/usr/bin/env python3
"""contains task_wait_n async function"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times and returns list of all the delays"""
    delays: list = []
    for i in range(n):
        delay: float = await wait_random(max_delay)
        if not delays:
            delays.append(delay)
        else:
            j: int = 0
            while j < len(delays) and delays[j] < delay:
                j += 1
            delays.insert(j, delay)
    return delays
