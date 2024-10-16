#!/usr/bin/env python3
"""A module to run concurrent async functions"""

import asyncio
from typing import List, Callable, Any
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function to run a async code multiple times"""

    run_list: List[float]

    tasks: List[Any] = [wait_random(max_delay) for _ in range(n)]

    run_list = await asyncio.gather(*tasks)

    return run_list
