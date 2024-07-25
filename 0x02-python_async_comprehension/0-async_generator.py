#!/usr/bin/env python3
""" Async Generator """

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randrange(0, 10) / 5.9
