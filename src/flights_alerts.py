# flight_alerts.py

import requests
from config import FLIGHT_API_KEY

def get_flight_prices(source, destination, date):
    """Fetches roundtrip flight prices from the specified departure airport to the destination."""
    url = f"https://api.flightapi.com/roundtrip"
    params = {
        "source": source,
        "destination": destination,
        "date": date,
        "apiKey": FLIGHT_API_KEY
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Assuming the API returns price in 'price' field
        price = data.get('price', 0)
        if price < 250:
            return price  # Return price if under $250
    else:
        print(f"Error fetching flight data: {response.status_code}")
    return None
