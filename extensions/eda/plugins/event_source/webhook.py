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
    host = args.get("host", "127.0.0.1")
    port = args.get("port", 5000)
    max_payload_size = int(args.get("max_payload_size", 1048576))  # 1 MB

    app = web.Application(client_max_size=max_payload_size)
    app.router.add_post("/webhook", webhook_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)

    await site.start()

    try:
        await asyncio.sleep(float("inf"))
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    pass
