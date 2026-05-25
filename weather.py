# Weather App by Jaiakash
# Project 2 — API calls + JSON
# JJ College of Engineering, Trichy

from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = "1edc71b096f4c272b21de7b99be70071"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ---- FETCH WEATHER FROM API ----
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# ---- DISPLAY WEATHER NICELY ----
def show_weather(data):
    if data["cod"] != 200:
        print("City not found. Check spelling.\n")
        return

    city     = data["name"]
    country  = data["sys"]["country"]
    temp     = data["main"]["temp"]
    feels    = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    desc     = data["weather"][0]["description"]
    wind     = data["wind"]["speed"]

    print(f"\n{'='*35}")
    print(f"  Weather in {city}, {country}")
    print(f"{'='*35}")
    print(f"  Temperature  : {temp}°C")
    print(f"  Feels like   : {feels}°C")
    print(f"  Humidity     : {humidity}%")
    print(f"  Condition    : {desc.title()}")
    print(f"  Wind speed   : {wind} m/s")
    print(f"{'='*35}\n")

# ---- MAIN PROGRAM ----
print("=== Weather App ===")
print("Type a city name. Type quit to exit.\n")

while True:
    city = input("Enter city: ").strip()
    if city.lower() == "quit":
        print("Bye!")
        break
    data = get_weather(city)
    show_weather(data)