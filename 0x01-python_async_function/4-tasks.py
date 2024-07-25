#!/usr/bin/env python3
""" Tasks """

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values).
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))

    return sorted(delays)
