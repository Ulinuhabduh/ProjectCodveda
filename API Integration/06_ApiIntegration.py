import requests
from api_key import API_KEY

lat = -8.366583
lon = 114.146301

# Get location (Nominatim API)
nominatim_url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"

response_geo = requests.get(nominatim_url, headers={"User-Agent": "my-weather-app"})
if response_geo.status_code == 200:
    geo_data = response_geo.json()
    location_name = geo_data.get('display_name', 'Unknown location')
else:
    location_name = 'Location fetch failed'

#  Get weather data (OpenWeatherMap API)
api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    
    # Extract the weather data
    zone = data['timezone']
    temperature = data['current']['temp']
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_speed']
    wheater = data['current']['weather'][0]['main']
    summary = data['daily'][0]['summary']

    # Print the weather + location data
    print(f"Location: {location_name}")
    print(f"Timezone: {zone}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather: {wheater}")
    print(f"Summary: {summary}")
else:
    print("Failed to fetch weather data.")
