#!/usr/bin/env python3
"""Asyncio concurrent coroutines"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function that measures the 
    runtime of wait_n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    return (stop - start) / n
