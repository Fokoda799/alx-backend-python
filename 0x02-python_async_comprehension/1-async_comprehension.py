#!/usr/bin/env python3
""" Async Comprehensions """

from typing import List
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async Comprehensions """
    return [i async for i in async_generator()]
