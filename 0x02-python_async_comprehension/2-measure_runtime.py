#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime of async_comprehension """
    start = time()
    await asyncio.gather(* [async_comprehension() for i in range(4)])
    end = time()
    return end - start
