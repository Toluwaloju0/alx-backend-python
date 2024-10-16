#!/usr/bin/env python3
"""A module to create a task"""


import asyncio
from typing import Any
wait_random: Any = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function to create a task and return it"""

    return asyncio.create_task(wait_random(max_delay))
