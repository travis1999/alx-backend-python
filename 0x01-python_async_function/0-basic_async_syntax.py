#!/usr/bin/env python3
"""Async io basic syntax"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    """wait random"""

    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
