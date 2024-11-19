import requests
from dotenv import load_dotenv
from datetime import datetime
import os

from tkinter import *
root = Tk()
root.geometry("600x400")

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
    
    errorCode = (getWeatherData.json()['cod'])
    print(errorCode)
    
    if(errorCode==200):
        print('code201')
        weather = (getWeatherData.json()['weather'][0]['main'])
        temperature = round(getWeatherData.json()['main']['temp'], 2)
        longitude = round(getWeatherData.json()['coord']['lon'], 5)
        latitude = round(getWeatherData.json()['coord']['lat'], 5)
        sunrise = int(getWeatherData.json()['sys']['sunrise'])
        sunset = int(getWeatherData.json()['sys']['sunset'])
        timezone = int(getWeatherData.json()['timezone'])
        sunriseAdjusted = datetime.utcfromtimestamp(sunrise+timezone).strftime('%H:%M')
        sunsetAdjusted = datetime.utcfromtimestamp(sunset+timezone).strftime('%H:%M')
    
        if(userComplexity==1):
            print('selectedComplex')
            #placeholder until testing
        elif(userComplexity==2):
            print('selectedAdvanced')
            #placeholder until testing
        Label(root, text=f'Current condition in {userBlankInput}: {weather}').place(x=5,y=100)
        Label(root, text=f'Temperature: {temperature}').place(x=5,y=125)
        Label(root, text=f'Sunrise: {sunriseAdjusted} local time').place(x=5,y=150)
        Label(root, text=f'Sunset: {sunsetAdjusted} local time').place(x=5,y=175)
    elif(errorCode==401):
        Label(root, text=f'401: Authentication Error').place(x=5,y=100)
        print('code401')
    elif(errorCode==404):
        Label(root, text=f'404: Invalid City Entered').place(x=5,y=100)
        print('code404')
    elif(errorCode==400):
        Label(root, text=f'400: Invalid City Entered').place(x=5,y=100)
        print('code400')
    else:
        Label(root, text=f'Unknown Error').place(x=5,y=100)
        print('error')


title = Label(root, text='pyweather').grid(row=0)

Label(root, text='City: ').grid(row=1)
userInputCity = Entry(root)
userInputCity.grid(row=1, column=1)


userInputSystem = IntVar()
requestMeasurementSystem = "imperial"
Radiobutton(root, text='°F', variable=userInputSystem, value=1).place(x=50,y=5)
Radiobutton(root,text='°C', variable=userInputSystem, value=2).place(x=75,y=5)

userComplexity = IntVar()
userComplexity = 1
Radiobutton(root,text='Simple', variable=userComplexity, value=1).place(x=5,y=5)
Radiobutton(root,text='Advanced',variable=userComplexity, value=2).place(x=25,y=5)


print(userInputCity)
print(requestMeasurementSystem)

goButton=Button(root, text="OK", command=runWeatherGet, width = 5).grid(row=1, column=6)


mainloop()





