import time
from typing import Optional

from webserver.classes.base import JSONable


class CityWeather(JSONable):
    def __init__(self, city: str, temperature: int, timestamp: Optional[float] = None):
        self.city = city
        self.temperature = temperature
        self.timestamp = timestamp or time.time()