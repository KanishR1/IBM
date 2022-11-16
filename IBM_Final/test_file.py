import requests as req
import json
import os
import ibmiotf.application
import ibmiotf.device
import time
import sys

# Weather Details 
api_key = "ae3304d1ae3a8c4dc28ddc816b07b1a9"
city = "Chennai"
country = "IN"
url_w=f"https://api.openweathermap.org/data/2.5/weather?q=Chennai,IN&appid=ae3304d1ae3a8c4dc28ddc816b07b1a9&units=metric"

#Cloud Details
org_id = "ml58t7"
device_type = "Smart_Farmer"
device_id = "Weather_field"
auth_method = "token"
auth_token = "Karan@2001"




def get_weather_details():    
    weather_req = req.get(url = url_w)
    weather_data = weather_req.json()

    climate = weather_data['weather'][0]['main']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    temperature = weather_data['main']['temp']
    temperature_min = weather_data['main']['temp_min']
    temperature_max = weather_data['main']['temp_max']
    temperature_feel = weather_data['main']['feels_like']
    temperature_average = (temperature_max+ temperature_min)/2
    data = {"climate":climate,"humidity":humidity,"temperature_average":temperature_average}
    return data

def myonpublishcallback(data):
    print(f"Published Temperature  = { data['temperature_average'] }, Humidity = {data['humidity']}, Climate = {data['climate']}")

try:
    deviceOptions = {"org" : org_id, 
                     "type" : device_type,
                     "id" : device_id,
                     "auth-method" : auth_method,
                     "auth-token" : auth_token
                    }
    deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print(f"Caught exception connecting device {str(e)}")
    sys.exit()
deviceCli.connect()
while True:
    data = get_weather_details()
    success = deviceCli.publishEvent("Current Weather","json",data,qos=1,on_publish = myonpublishcallback(data))
    if not success:
        time.sleep(1)