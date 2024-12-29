import requests
import json

# Define the API URL and parameters
API_KEY = '9371503e-c583-11ef-a0d5-0242ac130003-93715098-c583-11ef-a0d5-0242ac130003'  # Replace with your actual API key
API_URL = 'https://api.stormglass.io/v2/weather/point'

# Coordinates for Los Angeles (you can change these as needed)
latitude = 34.0522
longitude = -118.2437

# Parameters to request wave height data
params = 'waveHeight'

# Construct the API request headers
headers = {
    'Authorization': API_KEY
}

# Construct the API URL with parameters
url = f'{API_URL}?lat={latitude}&lng={longitude}&params={params}'

def get_surf_forecast():
    try:
        # Make the GET request to the StormGlass API
        response = requests.get(url, headers=headers)
        
        # Check for a successful response
        if response.status_code == 200:
            data = response.json()
            print("Surf Forecast Data:")
            for hour in data.get('hours', []):
                time = hour.get('time')
                wave_height = hour.get('waveHeight', {}).get('noaa', 'N/A')
                print(f"Time: {time} | Wave Height: {wave_height}m")
        else:
            print(f"Error: {response.status_code}")
            print("Error: Could not retrieve surf forecast.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_surf_forecast()
