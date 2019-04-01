#! /usr/code/env python3
# -*- coding: UTF-8 -*-

__author__ = 'Mark Yang'

import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime
from aiohttp import web

def index(request):
    # must has  content_type = 'text/html' or headers = {'content-type':'text/html'}
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})
    # return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

async def init(loop):
    # create web server instance app
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)

    # use event_loop.create_server() create TCP service\

    # execute OK 001
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)

    # execute OK 002
    app_runner = web.AppRunner(app)
    # srv = await loop.create_server(app_runner.app.make_handler(), '127.0.0.1', 9000)

    # cant show the page
    # srv = await loop.create_server(web.AppRunner(app), '127.0.0.1', 9000)
    # srv = await loop.create_server(app_runner.server, '127.0.0.1', 9000)

    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
