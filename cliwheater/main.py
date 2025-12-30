import requests
import json

API_key="the key ..."
latitude=00000
longtude=00000
exclude_port="minutely,hourly"

url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
#openwheater#-https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longtude}&exclude={exclude_port}&appid={API_key}
response=requests.get(url)

if response.status_code==200:
    data=response.json()
    print(data)
else:
    print(f"Error: {response.status_code},{response.text}")