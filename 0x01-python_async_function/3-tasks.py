#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax.
    Define a function named task_wait_random, using regular function syntax,
    which accepts an integer max_delay and returns an asyncio.Task. """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Generate an asyncio.Task """
    task = asyncio.create_task(wait_random(max_delay))
    return task
