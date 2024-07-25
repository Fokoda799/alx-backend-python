#!/usr/bin/env python3
"""  Let's execute multiple coroutines
at the same time with async """
from typing import List
import asyncio
File: str = '0-basic_async_syntax'
wait_random = __import__(File).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values).
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
