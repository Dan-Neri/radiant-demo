from zeep import Client
import os
from dotenv import load_dotenv

load_dotenv()

WSDL_ADDRESS = os.environ['WSDL_ADDRESS']
SOAP_ADDRESS = os.environ['SOAP_ADDRESS']


client = Client(WSDL_ADDRESS)
for key, value in client.wsdl.bindings.items():
    print(f"name: {key}\naddress: {value}")

# service = client.create_service(
#     client.wsdl.bindings.keys(),
#     SOAP_ADDRESS
# )

# response = service.NDFDgen(
#     latitude="38.99",
#     longitude="-77.01",
#     product="time-series",
#     XMLformat="TSML",
#     startTime="2004-01-01T00:00:00",
#     endTime="2012-02-12T00:00:00",
#     Unit="e",
#     weatherParameters={
#         "maxt": True,
#         "mint": False,
#         "temp": False,
#         "dew": False,
#         "pop12": False,
#         "qpf": False,
#         "sky": False,
#         "snow": False,
#         "wspd": False,
#         "wdir": False,
#         "wx": False,
#         "waveh": False,
#         "icons": False,
#         "rh": False,
#         "appt": False,
#         "incw34": False,
#         "incw50": False,
#         "incw64": False,
#         "cumw34": False,
#         "cumw50": False,
#         "cumw64": False,
#         "critfireo": False,
#         "dryfireo": False,
#         "conhazo": False,
#         "ptornado": False,
#         "phail": False,
#         "ptstmwinds": False,
#         "pxtornado": False,
#         "pxhail": False,
#         "pxtstmwinds": False,
#         "ptotsvrtstm": False,
#         "pxtotsvrtstm": False,
#         "tmpabv14d": False,
#         "tmpblw14d": False,
#         "tmpabv30d": False,
#         "tmpblw30d": False,
#         "tmpabv90d": False,
#         "tmpblw90d": False,
#         "prcpabv14d": False,
#         "prcpblw14d": False,
#         "prcpabv30d": False,
#         "prcpblw30d": False,
#         "prcpabv90d": False,
#         "prcpblw90d": False,
#         "wwa": False,
#         "wgust": False,
#         "iceaccum": False,
#         "maxrh": False,
#         "minrh": False,
#         "evp24": False,
#         "evpdep24": False,
#         "evp168": False,
#         "tcsurge": False,
#         "tcrain": False,
#         "tcwind": False,
#         "tctornado": False,
#         "ppi": False,
#         "probtsrwe24": False,
#         "snowlvl": False,
#         "snow24e10": False,
#         "snow24e90": False,
#         "snow48e10": False,
#         "snow48e90": False,
#         "snow72e10": False,
#         "snow72e90": False,
#         "wbgt": False,
#         "snowratio": False,
#         "ceil": False,
#         "vis": False,
#         "llwsdist": False,
#         "llwswindspd": False,
#         "llwswinddir": False,
#         "heatrisk": False
#     }
# )

# print(f"response: {response}")