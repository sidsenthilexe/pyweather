import requests
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

apiKey=os.getenv('apiKey')

userInputCity = input("Enter city: ")
userInputSystem = input("Enter your preferred system of measurements (I/M): ")
requestMeasurementSystem = "I"

if userInputSystem == "I":
    requestMeasurementSystem = "imperial"
elif userInputSystem == "M":
    requestMeasurementSystem = "metric"

getWeatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInputCity}&units={requestMeasurementSystem}&APPID={apiKey}")

print(getWeatherData.json())

weather = getWeatherData.json()['weather'][0]['main']
temperature = round(getWeatherData.json()['main']['temp'], 2)
longitude = round(getWeatherData.json()['coord']['lon'], 5)
latitude = round(getWeatherData.json()['coord']['lat'], 5)
sunrise = int(getWeatherData.json()['sys']['sunrise'])
sunset = int(getWeatherData.json()['sys']['sunset'])
timezone = int(getWeatherData.json()['timezone'])
sunriseAdjusted = sunrise+timezone
sunsetAdjusted = sunset+timezone

print(f"Weather for {userInputCity}:")
print(f"{longitude}, {latitude}")
print(f"Condition: {weather}")
print(f"Temperature: {temperature}")
print(datetime.utcfromtimestamp(sunriseAdjusted).strftime('%H:%M'))
print(datetime.utcfromtimestamp(sunsetAdjusted).strftime('%H:%M'))