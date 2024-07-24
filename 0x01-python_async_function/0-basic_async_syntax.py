#!/usr/bin/ev python3
""" The basics of async """
from typing import Union
from random import randrange
import asyncio


async def wait_random(max_delaiy: int=10) -> Union[int, float]:
    """ Wait random time """
    delaiy: Union[int, float] = randrange(0, max_delaiy + 1) / 10
    await asyncio.sleep(delaiy) 
    return delaiy 
