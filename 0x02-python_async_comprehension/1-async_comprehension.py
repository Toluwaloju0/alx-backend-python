#!/usr/bin/env python3
"""A module to get the yielded number"""

import asyncio
# from typing import
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """A function to print yielded values"""

    async_list = [i async for i in async_generator()]

    return async_list
