from aiohttp import web
import json
from datetime import datetime
from .api import api_routes
from aiohttp.web import _run_app

app = web.Application()
app.add_routes(api_routes)


async def run():
    await _run_app(
        app,
    )
