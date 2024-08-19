#!/usr/bin/env python3
"""contains measure_time async function"""
from typing import List
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay), and
       returns total_time / n as a float.
    """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - start_time
    return total_time / n
