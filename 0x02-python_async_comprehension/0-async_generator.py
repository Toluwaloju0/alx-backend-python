#!/usr/bin/env python3
"""A module to work on async comprehension"""

import asyncio
from typing import AsyncGenerator
from random import uniform


async def async_generator() -> AsyncGenerator[float, None]:
    """A function to create a generator number"""

    await asyncio.sleep(1)

    for _ in range(10):
        yield uniform(0, 10)
