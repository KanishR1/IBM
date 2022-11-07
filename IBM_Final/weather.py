import requests as req
import json
import os
import ibmiotf.application
import ibmiotf.device
import time
import sys

# Weather Details 
api_key = "fb12afe2efc8992de27da4156f22f05a"
city = "Chennai"
country = "IN"
url_w=f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"

#Cloud Details
org_id = "nbl97v"
device_type = "weather"
device_id = "weather_id_1"
auth_method = "token"
auth_token = "Kanish@2002"




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
