#!/usr/bin/env python3
""" Import wait_random from the previous Python file and create an async routine named wait_n. 
    It takes two integer arguments, max_delay and n. wait_n spawns wait_random n times with the specified max_delay. 
    It returns a list of delays (float values) in ascending order, ensuring concurrency. """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines concurrently using async """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
