from typing import TypedDict

class CityRecord(TypedDict):
    sate_code: str
    state: str
    city: str
    lat: float
    lon: float
    timezone: str