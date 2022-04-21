#!/usr/bin/env python3
"""Async generator"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """Generate random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
