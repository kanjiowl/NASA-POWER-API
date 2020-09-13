# Simple API for accesing NASA Power database

# Reference: https://power.larc.nasa.gov/docs/services/api/v1/temporal/daily/

import requests 
import json

# request url 
req_query  = {
        'request': 'execute', 
        'tempAverage': 'DAILY',
        'parameters': 'ALLSKY_SFC_SW_DWN,T2M,PS,WS10M',
        'userCommunity': 'AG',
        'identifier': 'SinglePoint',
        'lat' : '0', 
        'lon' : '0',
        'startDate': '20170101', 
        'endDate' : '20170201', 
        'outputList' : 'CSV', 
        'user' : 'DOCUMENTATION' 
        }

req_url  = 'https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py' 

resp = requests.get(req_url, params=req_query)
print(resp.url)
print()

# parse data s
parsed = json.loads(resp.content)
insolation_data = parsed['features'][0]['properties']['parameter']['ALLSKY_SFC_SW_DWN']

# values
insolation_data_dates = list(map(int, insolation_data.keys()))
insolation_data_vals = list(map(float, insolation_data.values()))

# print values
print(insolation_data_dates)
print(insolation_data_vals)
