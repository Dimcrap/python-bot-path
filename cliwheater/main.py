import requests
import json
import numpy as np
import pandas as pd

API_key="the key ..."
latitude=00000
longtude=00000
exclude_port="minutely,hourly"


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 32,
	"longitude": 53,
	"daily": ["apparent_temperature_max", "snowfall_sum", "sunrise", "sunset"],
	"hourly": ["temperature_2m", "apparent_temperature", "cloud_cover", "temperature_80m", "snow_depth", "visibility", "rain", "weather_code"],
	"past_days": 5,
}

'''url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly
=temperature_2m"#openwheater#-https://api.openweathermap.org/data/3.0/onecall?
lat={latitude}&lon={longtude}&exclude={exclude_port}&appid={API_key}
'''
response=requests.get(url,params=params)

if response.status_code==200:
    data=response.json()
    #print(data)
else:
    print(f"Error: {response.status_code},{response.text}")

input("press enter to continue . . .")

print(f"Coordinates:{data['latitude']}°N {data['longitude']}°E")
print(f"Elevation:{data['elevation']} m asl")
print(f"Timezone difference to GMT+0:{data['utc_offset_seconds']}s")


'''
hourly=data['date]
hourly_temperature_2m = np.array(hourly['temperature_2m'])
hourly_apparent_temperature = np.array(hourly['apparent_temperature'])
hourly_cloud_cover = np.array(hourly['cloud_cover'])
hourly_temperature_80m = np.array(hourly['temperature_80m'])
hourly_snow_depth = np.array(hourly['snow_depth'])
hourly_visibility = np.array(hourly['visibility'])
hourly_rain = np.array(hourly['rain'])
hourly_weather_code = np.array(hourly['weather_code'])
'''
hourly ={
"date":pd.to_datetime(data['hourly']['time']),    
"hourly_temperature_2m": data['hourly']['temperature_2m'],
"hourly_apparent_temperature" :  data['hourly']['apparent_temperature'],
"hourly_cloud_cover"  : data['hourly']['cloud_cover'],
"hourly_temperature_80m"  :  data['hourly']['temperature_80m'],
"hourly_snow_depth"  :  data['hourly']['snow_depth'],
"hourly_visibility"  :  data['hourly']['visibility'],
"hourly_rain"  :  data['hourly']['rain'],
"hourly_weather_code"  :  data['hourly']['weather_code']
}

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',50)
pd.set_option('display.width',1000)

df=pd.DataFrame(hourly)

print(df)