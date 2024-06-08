import json
from typing import Any, Optional

from aiohttp import web


def json_response(data: Any, status: int = 200):
    headers = {'asdasdsd': 'asdadas'}
    return web.Response(text=json.dumps(data), content_type='application/json', status=status, headers=headers)
