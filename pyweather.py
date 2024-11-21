import requests
from dotenv import load_dotenv
from datetime import datetime
import os
import tkinter as tkinter
from tkinter import *
root = Tk()
root.geometry("600x400")

load_dotenv()
API_KEY=os.getenv('API_KEY')


def runWeatherGet():
    print("button pressed")
    user_blank_input = user_input_city.get()
    user_button_input = user_input_system.get()
    user_complexity = user_input_complexity.get()
    
    if user_button_input == 1:
        measurement_system = "imperial"
    elif user_button_input == 2:
        measurement_system = "metric"
    
    access_weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_blank_input}&units={measurement_system}&APPID={API_KEY}")
    print(access_weather_data.json())
    print(user_blank_input)
    print(user_input_system)
    
    error_code = (access_weather_data.json()['cod'])
    print(error_code)
    
    #Clear any existing text on screen to solve text artifacting.
    simple_condition_label=tkinter.Label(root, text=f'                                                               ')
    simple_condition_label.place(x=5,y=100)
    simple_temperature_label=tkinter.Label(root, text=f'                                                               ')
    simple_temperature_label.place(x=5,y=125)
    
    advanced_condition_label=tkinter.Label(root, text=f'                                                                                                                        ')
    advanced_condition_label.place(x=5,y=100)
    advanced_weather_label=tkinter.Label(root, text=f'                                                               ')
    advanced_weather_label.place(x=5,y=125)
    advanced_temperature_label=tkinter.Label(root, text=f'                                                               ')
    advanced_temperature_label.place(x=5,y=150)
    advanced_feels_like_temp_label=tkinter.Label(root, text=f'                                                               ')
    advanced_feels_like_temp_label.place(x=5,y=175)
    advanced_min_temp_label=tkinter.Label(root, text=f'                                                               ')
    advanced_min_temp_label.place(x=5,y=200)
    advanced_max_temp_label=tkinter.Label(root, text=f'                                                               ')
    advanced_max_temp_label.place(x=5,y=225)
    advanced_vis_label=tkinter.Label(root, text=f'                                                               ')
    advanced_vis_label.place(x=5,y=250)
    advanced_sunrise_label=tkinter.Label(root, text=f'                                                               ')
    advanced_sunrise_label.place(x=5,y=275)
    advanced_sunset_label=tkinter.Label(root, text=f'                                                               ')
    advanced_sunset_label.place(x=5,y=300)
    
    

    
    if(error_code==200):
        print('code200')

        location_name = (access_weather_data.json()['name'])
        print(location_name)

        weather = (access_weather_data.json()['weather'][0]['main'])
        weather_advanced = (access_weather_data.json()['weather'][0]['description'])

        temperature = round(access_weather_data.json()['main']['temp'], 2)
        feels_like_temperature = round(access_weather_data.json()['main']['feels_like'], 2)
        min_temperature = round(access_weather_data.json()['main']['temp_min'], 2)
        max_temperature = round(access_weather_data.json()['main']['temp_max'], 2)

        visibility = (access_weather_data.json()['visibility'])


        longitude = round(access_weather_data.json()['coord']['lon'], 5)
        latitude = round(access_weather_data.json()['coord']['lat'], 5)

        sunrise = int(access_weather_data.json()['sys']['sunrise'])
        sunset = int(access_weather_data.json()['sys']['sunset'])
        timezone = int(access_weather_data.json()['timezone'])
        sunrise_adjusted = datetime.utcfromtimestamp(sunrise+timezone).strftime('%H:%M')
        sunset_adjusted = datetime.utcfromtimestamp(sunset+timezone).strftime('%H:%M')
        
        icon_file_identifier = (access_weather_data.json()['weather'][0]['description'])
      
        icon_filename = f"{icon_file_identifier}.png"
        print(icon_filename)
        
        

    
        if(user_complexity==1):
            print('selectedSimple')
            #locName, weather, temperature.
            simple_condition_label=tkinter.Label(root, text=f'Current weather in {location_name}: {weather}')
            simple_condition_label.place(x=5,y=100)
            simple_temperature_label=tkinter.Label(root, text=f'Temperature: {temperature}')
            simple_temperature_label.place(x=5,y=125)
            image_import=tkinter.PhotoImage(file=icon_filename)
            image_label=tkinter.Label(root,image=image_import)
            image_label.place(x=300,y=100)
            image_label.Pack()
        elif(user_complexity==2):
            print('selectedAdvanced')
            #locName, longitude, latitude, weather, weatherAdvanced, temperature, feelsLikeTemp, minTemp, maxTemp, visibility, sunrise adjusted, sunset adjusted.
            advanced_condition_label=tkinter.Label(root, text=f'Current weather in {location_name} ({longitude}, {latitude}): {weather}')
            advanced_condition_label.place(x=5,y=100)
            advanced_weather_label=tkinter.Label(root, text=f'Condition: {weather_advanced}')
            advanced_weather_label.place(x=5,y=125)
            advanced_temperature_label=tkinter.Label(root, text=f'Temperature: {temperature}')
            advanced_temperature_label.place(x=5,y=150)
            advanced_feels_like_temp_label=tkinter.Label(root, text=f'Feels like: {feels_like_temperature}')
            advanced_feels_like_temp_label.place(x=5,y=175)
            advanced_min_temp_label=tkinter.Label(root, text=f'Minimum temperature today: {min_temperature}')
            advanced_min_temp_label.place(x=5,y=200)
            advanced_max_temp_label=tkinter.Label(root, text=f'Maximum temperature today: {max_temperature}')
            advanced_max_temp_label.place(x=5,y=225)
            advanced_vis_label=tkinter.Label(root, text=f'Visibility: {visibility}')
            advanced_vis_label.place(x=5,y=250)
            advanced_sunrise_label=tkinter.Label(root, text=f'Sunrise: {sunrise_adjusted} local time')
            advanced_sunrise_label.place(x=5,y=275)
            advanced_sunset_label=tkinter.Label(root, text=f'Sunset: {sunset_adjusted} local time')
            advanced_sunset_label.place(x=5,y=300)
            image_import=tkinter.PhotoImage(file=icon_filename)
            image_label=tkinter.Label(root,image=image_import)
            image_label.place(x=300,y=100)
            image_label.Pack()
            
            
    
    elif(error_code==401):
        Label(root, text=f'401: Authentication Error').place(x=5,y=100)
        print('code401')
    elif(error_code==404):
        Label(root, text=f'404: Invalid City Entered').place(x=5,y=100)
        print('code404')
    elif(error_code==400):
        Label(root, text=f'400: Invalid City Entered').place(x=5,y=100)
        print('code400')
    else:
        Label(root, text=f'Unknown Error').place(x=5,y=100)
        print('error')

title = Label(root, text='pyweather').grid(row=0)

Label(root, text='City: ').grid(row=1)
user_input_city = Entry(root)
user_input_city.grid(row=1, column=1)


user_input_system = IntVar()
measurement_system = "imperial"
Radiobutton(root, text='°F', variable=user_input_system, value=1).grid(row=1,column=2)
Radiobutton(root,text='°C', variable=user_input_system, value=2).grid(row=1,column=3)

user_input_complexity = IntVar()
Radiobutton(root,text='Simple', variable=user_input_complexity, value=1).grid(row=2,column=1)
Radiobutton(root,text='Advanced',variable=user_input_complexity, value=2).grid(row=2,column=2)


print(user_input_city)
print(measurement_system)

ok_button=Button(root, text="OK", command=runWeatherGet, width = 5).grid(row=1, column=7)


mainloop()
