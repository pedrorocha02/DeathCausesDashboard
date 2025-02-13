import requests
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

def get_weather(api_key, country):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": country,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

api_key = os.getenv("WEATHER_KEY") 
country = "Portugal"
weather_data = get_weather(api_key, country)
if weather_data:
    print(weather_data)

else:
    print("Failed to retrieve weather data")
