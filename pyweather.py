import requests
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
apiKey=os.getenv('apiKey')

from tkinter import *
root = Tk()
root.geometry("400x400")


title = Label(root, text='pyweather').grid(row=0)
ready = 0

def readyPressed():
    ready=1


Label(root, text='City: ').grid(row=1)
userInputCity = Entry(root)
userInputCity.grid(row=1, column=1)

userInputSystem = IntVar()
requestMeasurementSystem = "imperial"
Radiobutton(root, text='Imperial', variable=userInputSystem, value=1).grid(row=2,column=1)
Radiobutton(root,text='Metric', variable=userInputSystem, value=2).grid(row=2,column=2)
if userInputSystem == 1:
    requestMeasurementSystem = "imperial"
elif userInputSystem == 2:
    requestMeasurementSystem = "metric"

print(userInputCity)
print(userInputSystem)

goButton=Button(root, text="OK", width = 5, command=readyPressed).grid(row=3)

if(ready==1):
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

    Label(root, text=f'Weather for {userInputCity} ({longitude}, {latitude}):').grid(row=4,column=1)
    Label(root, text=f'Condition: {weather}').grid(row=4,column=2)
    Label(root, text=f'Temperature: {temperature}').grid(row=5,column=1)
    Label(root, text=f'Sunrise: {sunriseAdjusted}').grid(row=6,column=1)
    Label(root, text=f'Sunset: {sunsetAdjusted}').grid(row=6,column=2)
mainloop()





