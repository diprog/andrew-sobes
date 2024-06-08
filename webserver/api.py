import json
from datetime import datetime

from aiohttp import web
from .utils import json_response

api_routes = web.RouteTableDef()

data_store = {}


@api_routes.get('/temperature/{city}')
async def get_temperature(request: web.Request):
    city = request.match_info.get('city', "Unknown")
    return json_response({
        "city": city,
        "temperature": 25,
        "timestamp": datetime.now().isoformat()
    })


@api_routes.post('/temperature')
async def post_temperature(request):
    data = await request.json()
    city = data['city']
    data_store[city] = data
    return json_response({"status": "success"})


@api_routes.put('/temperature/{city}')
async def put_temperature(request):
    data = await request.json()
    city = request.match_info.get('city')
    data_store[city] = data
    return json_response({"status": "updated"})


@api_routes.delete('/temperature/{city}')
async def delete_temperature(request):
    city = request.match_info.get('city')
    if city in data_store:
        del data_store[city]
        return json_response({"status": "deleted"})
    else:
        return json_response({"status": "not found"}, 404)
