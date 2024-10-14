#!/usr/bin/env python3
"""A module to create a asynchronous coroutine"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A async function to wait on a random number"""
    n: float = random.uniform(0, max_delay)
    await asyncio.sleep(n)

    return n
