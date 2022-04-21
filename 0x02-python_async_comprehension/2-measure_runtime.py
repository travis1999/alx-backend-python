#!/usr/bin/env python3
"""measure runtime"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    start = time()
    await asyncio.gather(*tasks)
    stop = time()
    return stop - start
