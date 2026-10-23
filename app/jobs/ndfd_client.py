"""SOAP client for communicating with the NDFD.

The client is created from the WSDL using zeep. It fetches forecast data using
the appropriate server functions provided by the NDFD. The response is returned
directly without validation, which is handled by the ingest service.
"""

from zeep import Client
import os
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

_WSDL_ADDRESS = os.environ['WSDL_ADDRESS']
_SOAP_ADDRESS = os.environ['SOAP_ADDRESS']
_WEATHER_PARAMS = {
    "maxt": False,
    "mint": False,
    "temp": False,
    "dew": False,
    "pop12": False,
    "qpf": False,
    "sky": False,
    "snow": False,
    "wspd": False,
    "wdir": False,
    "wx": False,
    "waveh": False,
    "icons": False,
    "rh": False,
    "appt": False,
    "incw34": False,
    "incw50": False,
    "incw64": False,
    "cumw34": False,
    "cumw50": False,
    "cumw64": False,
    "critfireo": False,
    "dryfireo": False,
    "conhazo": False,
    "ptornado": False,
    "phail": False,
    "ptstmwinds": False,
    "pxtornado": False,
    "pxhail": False,
    "pxtstmwinds": False,
    "ptotsvrtstm": False,
    "pxtotsvrtstm": False,
    "tmpabv14d": False,
    "tmpblw14d": False,
    "tmpabv30d": False,
    "tmpblw30d": False,
    "tmpabv90d": False,
    "tmpblw90d": False,
    "prcpabv14d": False,
    "prcpblw14d": False,
    "prcpabv30d": False,
    "prcpblw30d": False,
    "prcpabv90d": False,
    "prcpblw90d": False,
    "wwa": False,
    "wgust": False,
    "iceaccum": False,
    "maxrh": False,
    "minrh": False,
    "evp24": False,
    "evpdep24": False,
    "evp168": False,
    "tcsurge": False,
    "tcrain": False,
    "tcwind": False,
    "tctornado": False,
    "ppi": False,
    "probtsrwe24": False,
    "snowlvl": False,
    "snow24e10": False,
    "snow24e90": False,
    "snow48e10": False,
    "snow48e90": False,
    "snow72e10": False,
    "snow72e90": False,
    "wbgt": False,
    "snowratio": False,
    "ceil": False,
    "vis": False,
    "llwsdist": False,
    "llwswindspd": False,
    "llwswinddir": False,
    "heatrisk": False
}

class NdfdClient:
    def __init__(self, timeout: int = 30):
        self._client = Client(_WSDL_ADDRESS)

        #The WSDL defines a SOAP address that relies on localhost. This must be
        #overwritten with the remote server address obatined from the
        #weather.gov site.
        self._service = self._client.create_service(
            #Retrieve the first binding name
            next(iter(self._client.wsdl.bindings)).name,
            #Overwrite the address with the remote server
            _SOAP_ADDRESS
        )

    def get_point_forecast(
        self, 
        lat: float, 
        lon: float, 
        start_time: datetime,
        end_time: datetime,
        *params: str 
    ) -> str:
        #Copy the default parameters dictionary to avoid overwriting it 
        weather_parameters = _WEATHER_PARAMS.copy()
        for param in params:
            weather_parameters[param] = True

        #Make the request to the server with the NDFDgen function
        response: str = self._service.NDFDgen(
            latitude = lat,
            longitude = lon,
            product = "time-series",
            XMLformat = "DWSML",
            startTime = start_time.isoformat(),
            endTime = end_time.isoformat(), 
            Unit = "e",
            weatherParameters = weather_parameters
        )

        return(response)

    def get_list_forecast(
        self, 
        lat_lon_list: list[tuple[float, float]], 
        start_time: datetime,
        end_time: datetime,
        *params: str 
    ) -> str:
        #Convert the list of tuples to a string accepted by the server
        lat_lon_str = ""
        for lat, lon in lat_lon_list:
            lat_lon_str += f"{lat},{lon},\n"

        #Copy the default parameters dictionary to avoid overwriting it 
        weather_parameters = _WEATHER_PARAMS.copy()
        for param in params:
            weather_parameters[param] = True

        #Make the request to the server with the NDFDgenLatLonList function
        response: str = self._service.NDFDgenLatLonList(
            listLatLon  = lat_lon_str,
            product = "time-series",
            XMLformat = "DWSML",
            startTime = start_time.isoformat(),
            endTime = end_time.isoformat(), 
            Unit = "e",
            weatherParameters = weather_parameters
        )

        return(response)
        