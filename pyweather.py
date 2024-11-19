import requests
from dotenv import load_dotenv
from datetime import datetime
import os

from tkinter import *
root = Tk()
root.geometry("400x400")

load_dotenv()
apiKey=os.getenv('apiKey')

def runWeatherGet():
    print("button pressed")
    userBlankInput = userInputCity.get()
    userButtonInput = userInputSystem.get()
    
    if userButtonInput == 1:
        requestMeasurementSystem = "imperial"
    elif userButtonInput == 2:
        requestMeasurementSystem = "metric"
        
    getWeatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userBlankInput}&units={requestMeasurementSystem}&APPID={apiKey}")
    print(getWeatherData.json())
    print(userBlankInput)
    print(userInputSystem)
    
    weather = (getWeatherData.json()['weather'][0]['main'])
    temperature = round(getWeatherData.json()['main']['temp'], 2)
    longitude = round(getWeatherData.json()['coord']['lon'], 5)
    latitude = round(getWeatherData.json()['coord']['lat'], 5)
    sunrise = int(getWeatherData.json()['sys']['sunrise'])
    sunset = int(getWeatherData.json()['sys']['sunset'])
    timezone = int(getWeatherData.json()['timezone'])
    sunriseAdjusted = datetime.utcfromtimestamp(sunrise+timezone).strftime('%H:%M')
    sunsetAdjusted = datetime.utcfromtimestamp(sunset+timezone).strftime('%H:%M')
    
    
    Label(root, text=f'Current condition in {userBlankInput}: {weather}').grid(row=4,column=1)
    Label(root, text=f'Temperature: {temperature}').grid(row=5,column=1)
    Label(root, text=f'Sunrise: {sunriseAdjusted}').grid(row=6,column=1)
    Label(root, text=f'Sunset: {sunsetAdjusted}').grid(row=6,column=2)


title = Label(root, text='pyweather').grid(row=0)

Label(root, text='City: ').grid(row=1)
userInputCity = Entry(root)
userInputCity.grid(row=1, column=1)


userInputSystem = IntVar()
requestMeasurementSystem = "imperial"
Radiobutton(root, text='Imperial', variable=userInputSystem, value=1).grid(row=2,column=1)
Radiobutton(root,text='Metric', variable=userInputSystem, value=2).grid(row=2,column=2)

print(userInputCity)
print(requestMeasurementSystem)

goButton=Button(root, text="OK", command=runWeatherGet, width = 5).grid(row=3)


mainloop()





