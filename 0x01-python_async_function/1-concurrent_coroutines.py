#!/usr/bin/env python3
"""Asyncio concurrent coroutines"""


from typing import List
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Schedule and run async tasks"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await x for x in asyncio.as_completed(tasks)]
