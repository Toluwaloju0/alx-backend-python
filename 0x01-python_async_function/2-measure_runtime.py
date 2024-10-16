#!/usr/bin/env python3
"""A module to print the elasped time  function uses"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A function to get the time taken for a function to run"""

    time1: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_taken: float = time1 - time.time()

    return time_taken / n
