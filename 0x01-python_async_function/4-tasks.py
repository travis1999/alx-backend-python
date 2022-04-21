#!/usr/bin/env python3
"""Asyncio concurrent coroutines"""


from typing import List
import asyncio


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Schedule and run async tasks"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await x for x in asyncio.as_completed(tasks)]
