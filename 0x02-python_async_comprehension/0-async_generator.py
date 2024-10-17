#!/usr/bin/env python3
"""A module to work on async comprehension"""

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """A function to create a generator number"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
