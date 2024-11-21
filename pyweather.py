import requests
from dotenv import load_dotenv
from datetime import datetime
import os

import tkinter as tkinter
from tkinter import *
root = Tk()
root.geometry("600x400")

load_dotenv()
apiKey=os.getenv('apiKey')


def runWeatherGet():
    print("button pressed")
    userBlankInput = userInputCity.get()
    userButtonInput = userInputSystem.get()
    userComplexityVar = userComplexity.get()
    
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
    
    #Clear any existing text on screen to solve text artifacting.
    simpleConditionLabel=tkinter.Label(root, text=f'                                                               ')
    simpleConditionLabel.place(x=5,y=100)
    simpleTemperatureLabel=tkinter.Label(root, text=f'                                                               ')
    simpleTemperatureLabel.place(x=5,y=125)
    
    advancedConditionLabel=tkinter.Label(root, text=f'                                                                                                                        ')
    advancedConditionLabel.place(x=5,y=100)
    advancedWeatherLabel=tkinter.Label(root, text=f'                                                               ')
    advancedWeatherLabel.place(x=5,y=125)
    advancedTempLabel=tkinter.Label(root, text=f'                                                               ')
    advancedTempLabel.place(x=5,y=150)
    advancedFeelsLikeTempLabel=tkinter.Label(root, text=f'                                                               ')
    advancedFeelsLikeTempLabel.place(x=5,y=175)
    advancedMinTempLabel=tkinter.Label(root, text=f'                                                               ')
    advancedMinTempLabel.place(x=5,y=200)
    advancedMaxTempLabel=tkinter.Label(root, text=f'                                                               ')
    advancedMaxTempLabel.place(x=5,y=225)
    advancedVisibilityLabel=tkinter.Label(root, text=f'                                                               ')
    advancedVisibilityLabel.place(x=5,y=250)
    advancedSunriseLabel=tkinter.Label(root, text=f'                                                               ')
    advancedSunriseLabel.place(x=5,y=275)
    advancedSunsetLabel=tkinter.Label(root, text=f'                                                               ')
    advancedSunsetLabel.place(x=5,y=300)
    
    

    
    if(errorCode==200):
        print('code200')

        locName = (getWeatherData.json()['name'])

        weather = (getWeatherData.json()['weather'][0]['main'])
        weatherAdvanced = (getWeatherData.json()['weather'][0]['description'])

        temperature = round(getWeatherData.json()['main']['temp'], 2)
        feelsLikeTemp = round(getWeatherData.json()['main']['feels_like'], 2)
        minTemp = round(getWeatherData.json()['main']['temp_min'], 2)
        maxTemp = round(getWeatherData.json()['main']['temp_max'], 2)

        visibility = (getWeatherData.json()['visibility'])


        longitude = round(getWeatherData.json()['coord']['lon'], 5)
        latitude = round(getWeatherData.json()['coord']['lat'], 5)

        sunrise = int(getWeatherData.json()['sys']['sunrise'])
        sunset = int(getWeatherData.json()['sys']['sunset'])
        timezone = int(getWeatherData.json()['timezone'])
        sunriseAdjusted = datetime.utcfromtimestamp(sunrise+timezone).strftime('%H:%M')
        sunsetAdjusted = datetime.utcfromtimestamp(sunset+timezone).strftime('%H:%M')
        
        iconFile = (getWeatherData.json()['weather'][0]['description'])
      
        iconInter = f"{iconFile}.png"
        image=PhotoImage(file=iconInter)
        print(iconInter)
        
        

    
        if(userComplexityVar==1):
            print('selectedSimple')
            #locName, weather, temperature.
            simpleConditionLabel=tkinter.Label(root, text=f'Current weather in {locName}: {weather}')
            simpleConditionLabel.place(x=5,y=100)
            simpleTemperatureLabel=tkinter.Label(root, text=f'Temperature: {temperature}')
            simpleTemperatureLabel.place(x=5,y=125)
            image2=tkinter.PhotoImage(file=iconInter)
            imageLabel=tkinter.Label(root,image=image2)
            imageLabel.place(x=300,y=100)
            imageLabel.Pack()
        elif(userComplexityVar==2):
            print('selectedAdvanced')
            #locName, longitude, latitude, weather, weatherAdvanced, temperature, feelsLikeTemp, minTemp, maxTemp, visibility, sunrise adjusted, sunset adjusted.
            advancedConditionLabel=tkinter.Label(root, text=f'Current weather in {locName} ({longitude}, {latitude}): {weather}')
            advancedConditionLabel.place(x=5,y=100)
            advancedWeatherLabel=tkinter.Label(root, text=f'Condition: {weatherAdvanced}')
            advancedWeatherLabel.place(x=5,y=125)
            advancedTempLabel=tkinter.Label(root, text=f'Temperature: {temperature}')
            advancedTempLabel.place(x=5,y=150)
            advancedFeelsLikeTempLabel=tkinter.Label(root, text=f'Feels like: {feelsLikeTemp}')
            advancedFeelsLikeTempLabel.place(x=5,y=175)
            advancedMinTempLabel=tkinter.Label(root, text=f'Minimum temperature today: {minTemp}')
            advancedMinTempLabel.place(x=5,y=200)
            advancedMaxTempLabel=tkinter.Label(root, text=f'Maximum temperature today: {maxTemp}')
            advancedMaxTempLabel.place(x=5,y=225)
            advancedVisibilityLabel=tkinter.Label(root, text=f'Visibility: {visibility}')
            advancedVisibilityLabel.place(x=5,y=250)
            advancedSunriseLabel=tkinter.Label(root, text=f'Sunrise: {sunriseAdjusted} local time')
            advancedSunriseLabel.place(x=5,y=275)
            advancedSunsetLabel=tkinter.Label(root, text=f'Sunset: {sunsetAdjusted} local time')
            advancedSunsetLabel.place(x=5,y=300)
            image2=tkinter.PhotoImage(file=iconInter)
            imageLabel=tkinter.Label(root,image=image2)
            imageLabel.place(x=300,y=100)
            imageLabel.Pack()
            
            
    
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
Radiobutton(root, text='°F', variable=userInputSystem, value=1).grid(row=1,column=2)
Radiobutton(root,text='°C', variable=userInputSystem, value=2).grid(row=1,column=3)

userComplexity = IntVar()
Radiobutton(root,text='Simple', variable=userComplexity, value=1).grid(row=2,column=1)
Radiobutton(root,text='Advanced',variable=userComplexity, value=2).grid(row=2,column=2)


print(userInputCity)
print(requestMeasurementSystem)

goButton=Button(root, text="OK", command=runWeatherGet, width = 5).grid(row=1, column=7)


mainloop()
