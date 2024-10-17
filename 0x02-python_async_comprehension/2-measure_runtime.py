#!/usr/bin/env python3
"""A module to measure the runtime of a async function"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """A function to measure the runtime of an async function"""

    async_list = [async_comprehension() for _ in range(4)]

    time1: float = time.perf_counter()
    await asyncio.gather(*async_list)
    time_2: float = time.perf_counter() - time1
    return time_2
