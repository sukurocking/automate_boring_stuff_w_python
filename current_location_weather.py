#! python3
# current_location_weather.py - This programs gets the current location and browses the local weather

# import geocoder
# g = geocoder.ip("me")
# print(g.latlng)

import requests, webbrowser

def get_current_location():
    # Get public IP address
    ip_request = requests.get('https://api.ipify.org?format=json')
    ip_address = ip_request.json()['ip']

    # Get location information based on IP address
    location_request = requests.get(f'http://ip-api.com/json/{ip_address}')
    location_data = location_request.json()
    
    return (location_data['lat'], location_data['lon'])



if __name__ == "__main__":
    lat, long = get_current_location()
    webbrowser.open(f"https://weather.com/en-IN/weather/today/l/{lat},{long}")
    print(f"Current location coordinates: Latitude {lat}, Longitude {long}")


# My actual coordinates
# 20.2529093, 85.8030417