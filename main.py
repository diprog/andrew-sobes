import asyncio

import core.main
from webserver import webserver
from webserver.classes.city_weather import CityWeather


async def idle():
    while True:
        await asyncio.sleep(1)


async def main():
    asyncio.create_task(webserver.run())
    asyncio.create_task(core.main.main())
    await idle()


asyncio.run(main())
