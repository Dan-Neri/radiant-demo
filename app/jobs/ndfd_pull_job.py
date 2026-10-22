"""NDFD pull job.

This module is used to pull data from the NDFD which can be easily scheduled
separately from the API. It first loads the locations from the CSV file
located at `app/data/state_capitals.csv` into a dictionary keyed by strings
in the form `city, state_code`.

TODO: Passes the dictionary to the ingest service which will handle data
validation and loading.
"""
import csv
from pathlib import Path
#from .ndfd_client import NdfdClient
from .types.city import CityRecord

_LOCATIONS_PATH = (Path(__file__).resolve().parents[1] / "data" / 
    "state_capitals.csv")

def load_locations() -> dict[str, CityRecord]:
    cities: dict[str, CityRecord] = {}
    with open(_LOCATIONS_PATH, 'r', newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            key = f"{line['city']}, {line['state_code']}"
            cities[key] = {
                "state_code": line["state_code"],
                "state": line["state"],
                "city": line["city"],
                "latitude": float(line["latitude"]),
                "longitude": float(line["longitude"]),
                "timezone": line["timezone"]
            }

    return cities


if __name__ == "__main__":
    try:
        print(load_locations())
    except OSError as e:
        raise RuntimeError(f"Failed to open {_LOCATIONS_PATH}") from e
    