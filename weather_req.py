import requests as req
import os
os.system("clear")

api_key = "fb12afe2efc8992de27da4156f22f05a"
city = "Chennai"
country = "IN"

url_w=f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"

print()
print(url_w)
print()

weather_req = req.get(url = url_w)
weather_data = weather_req.json()

climate = weather_data['weather'][0]['main']
humidity = weather_data['main']['humidity']
pressure = weather_data['main']['pressure']
temperature = weather_data['main']['temp']
temperature_min = weather_data['main']['temp_min']
temperature_max = weather_data['main']['temp_max']
temperature_feel = weather_data['main']['feels_like']

print()
print("Weather Data :")
print()
print(weather_data)
print()

print(f"Climate = {climate}")
print(f"Humidity = {humidity}")
print(f"Pressure = {pressure}")
print(f"Temperature = {temperature} C")
print(f"Temperature Min = {temperature_min} C")
print(f"Temperature Max = {temperature_max} C")
print(f"Temperature Feel = {temperature_feel} C")
print()