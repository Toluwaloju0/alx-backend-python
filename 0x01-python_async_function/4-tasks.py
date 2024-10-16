#!/usr/bin/env python3
"""A module to use a task to run a function"""

import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """A functon touse tasks and run async code"""

    task_list = []
    for _ in range(n):
        task_list.append(await task_wait_random(max_delay))

    return task_list
