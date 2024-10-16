#!?usr/bin/env python3
"""A module to create a task"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """A function to create a task and return it"""

    return asyncio.create_task(wait_random(max_delay))
