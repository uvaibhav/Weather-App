
# IMPORT REQUIRED MODULES

from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests


# EXTRACT KEY FROM THE WEATHER FILE
api_file="weather.key"
file_a=ConfigParser()
file_a.read(api_file)
api_key = file_a["api_key"]["key"]
url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# EXPLICIT FUNCTION TO GET WEATHER DETAILS

def weather_result(city):
    final=requests.get(url_api.format(city,api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        kelvin_temperature = json_file['main']['temp']
        celcius_temperature = kelvin_temperature - 273.15
        f_temperature = (kelvin_temperature-273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        humidity_display=json_file['main']['humidity']
        
        result = (city,country_name,celcius_temperature,f_temperature,weather_display,humidity_display)
        
        return result
    else:
        print("No content found") 

# EXPLICIT FUNCTION TO SEARCH CITY

def print_weather():
    city = search_city.get()
    weather = weather_result(city)
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0],weather[1])
        temperature_entry['text']='{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        weather_entry['text'] = weather[4]
        humidity_entry['text']=weather[5]
       
        
    else:
        messagebox.showerror('Error','Please enter a valid city name. Cannot find this city.')

# DRIVER CODE

# CREATE OBJECT
root = Tk()

# ADD TITLE
root.title("Weather App")
root.config(background="black")

# ADD WINDOW SIZE
root.geometry("700x400")

# ADD LABELS,BUTTONS AND TEXT
search_city = StringVar()
enter_city = Entry(root, textvariable=search_city, fg="blue",font={"Arial",30,"bold"})
enter_city.pack()


search_button = Button(root, text="SEARCH WEATHER ! ", width=20,bg="red",fg="white",font={"Arial",25,"bold"},command=print_weather)
search_button.pack()

location_entry = Label(root, text="Location",font={"Arial",35,"bold"},bg="lightblue")
location_entry.pack()

temperature_entry = Label(root, text="temperature",font={"Arial",35,"bold"},bg="lightpink")
temperature_entry.pack()

weather_entry = Label(root,text="weather_clouds",font={"Arial",35,"bold"},bg="lightgreen")
weather_entry.pack()

humidity_entry= Label(root,text="Humidity Level",font={"Aria",35,"bold"},bg="lightblue")
humidity_entry.pack()


root.mainloop()


