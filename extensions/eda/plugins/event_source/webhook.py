#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""DDN webhook event source for EDA."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import asyncio
from aiohttp import web


async def webhook_handler(request):
    """Handle webhook requests."""
    data = await request.json()
    return web.Response(text="OK")


async def main(queue, args):
    """Main event source loop."""
    port = args.get("port", 5000)
    
    app = web.Application()
    app.router.add_post("/webhook", webhook_handler)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    
    await site.start()
    
    try:
        await asyncio.sleep(float("inf"))
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    pass
