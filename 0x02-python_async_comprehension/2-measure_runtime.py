#!/usr/bin/env python3
"""
Concurrency of four Asynchronous Comprehension operations
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Collects 10 random numbers using an async comprehensing,
    then returns 10 random numbers.
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.perf_counter()
    return (end - start)
