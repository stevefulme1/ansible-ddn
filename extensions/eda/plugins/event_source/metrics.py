#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""DDN metrics polling event source for EDA."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import asyncio
import aiohttp


async def main(queue, args):
    """Poll DDN metrics."""
    host = args["host"]
    username = args.get("username")
    password = args.get("password")
    interval = args.get("interval", 60)
    
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://{host}/api/v1/metrics"
                async with session.get(url, auth=aiohttp.BasicAuth(username, password)) as resp:
                    metrics = await resp.json()
                    await queue.put({"metrics": metrics})
        except Exception as e:
            await queue.put({"error": str(e)})
        
        await asyncio.sleep(interval)


if __name__ == "__main__":
    pass
