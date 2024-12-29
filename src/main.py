from surf_forecast import get_surf_forecast
from flight_alerts import get_flight_prices
from notifier import send_alert
import schedule
import time

# Constants for flights (Fort Lauderdale to BQN)
FLIGHT_SOURCE = 'Fort Lauderdale'  # FLL airport
FLIGHT_DESTINATION = 'BQN'  # Rafael Hernández Airport (BQN)
FLIGHT_DATES = ['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01', '2025-06-01', '2025-07-01', '2025-08-01', '2025-09-01', '2025-10-01', '2025-11-01', '2025-12-01']  # Add dates for all of 2025

def check_conditions():
    """Check surf conditions and flight prices."""
    # Get surf data
    surf_data = get_surf_forecast()
    
    if surf_data:
        # Extract the swell height (from the first hour data)
        swell_height = surf_data.get('hours', [])[0].get('swellHeight', {}).get('icon', 0)
        swell_height_in_feet = swell_height * 3.28084  # Convert meters to feet
        
        print(f"Swell Height: {swell_height_in_feet:.2f} ft")

        # Check if swell height is above 5 feet (1.52 meters)
        if swell_height_in_feet > 5:
            # Check flight prices for each date in 2025
            for date in FLIGHT_DATES:
                flight_price = get_flight_prices(FLIGHT_SOURCE, FLIGHT_DESTINATION, date)
                
                if flight_price and flight_price < 250:
                    message = f"Good surf conditions with swell height of {swell_height_in_feet:.2f} feet! Roundtrip flight to BQN for {date} is under $250. Book now!"
                    send_alert(message)
                else:
                    print(f"Flight for {date} is not under $250.")
        else:
            print("Surf conditions are not good.")
    else:
        print("Unable to fetch surf data.")

# Run the check every hour
schedule.every(1).hour.do(check_conditions)

while True:
    schedule.run_pending()
    time.sleep(1)
