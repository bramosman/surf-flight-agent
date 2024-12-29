# surf_forecast.py

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the Stormglass API key from environment variables
STORMGLASS_API_KEY = os.getenv("STORMGLASS_API_KEY")

BASE_URL = 'https://api.stormglass.io/v2/weather/point'

# Coordinates for the beach (18°29'01.6"N 67°10'00.2"W)
LAT = 18.483778  # Latitude: 18°29'01.6"N
LON = -67.166722  # Longitude: 67°10'00.2"W

print("surf_forecast module loaded")

def get_surf_forecast():
    # Fetch the surf forecast data from the Stormglass API
    headers = {'Authorization': STORMGLASS_API_KEY}
    params = {
        'lat': LAT,
        'lng': LON,
        'params': 'swellHeight,swellDirection,swellPeriod,windSpeed'
    }
    
    response = requests.get(BASE_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()  # Return data as JSON
    else:
        print("Error:", response.status_code)
        return None
