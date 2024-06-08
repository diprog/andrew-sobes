from typing import Literal

import aiohttp

ENDPOINT = 'http://127.0.0.1:8080'


class WeatherClientBase:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def request(self, method: str, path: str, json: dict = None):
        url = ENDPOINT + path
        r = await self.session.request(method, url, json=json)
        return await r.json()

    async def get(self, path: str):
        return await self.request('GET', path)

    async def post(self, path: str, json: dict = None):
        return await self.request('POST', path, json=json)

    async def put(self, path: str, json: dict = None):
        return await self.request('PUT', path, json=json)

    async def delete(self, path: str):
        return await self.request('DELETE', path)


class WeatherClient(WeatherClientBase):
    def __init__(self):
        super().__init__()

    async def get_temperature(self, city: str) -> float:
        return await self.get(f'/temperature/{city}')

    async def post_temperature(self, city: str, data: dict) -> float:
        data['city'] = city
        return await self.post('/temperature', data)

    async def put_temperature(self, city: str, data: dict) -> float:
        return await self.put(f'/temperature/{city}', data)

    async def delete_temperature(self, city: str) -> float:
        return await self.delete(f'/temperature/{city}')
