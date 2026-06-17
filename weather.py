
import requests

# 1. Taking city name from the user
city = input("Enter City Name (e.g., Anantapur, Hyderabad, New York): ").strip()

# 2. Using a free Open-Meteo API (No API Key Required! It is 100% Free & Live)
# First, we get the Latitude and Longitude of the city
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"

try:
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()
    
    if "results" in geo_data:
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        display_name = geo_data["results"][0]["name"]
        country = geo_data["results"][0].get("country", "")

        # Now, we fetch the actual real-world live weather using coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        current = weather_data["current"]
        temp = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind = current["wind_speed_10m"]
        
        print(f"\n--- Live Weather Details ---")
        print(f"Location: {display_name}, {country}")
        print(f"Current Temperature: {temp}°C")
        print(f"Wind Speed: {wind} km/h")
        print(f"Humidity: {humidity}%")
        print("----------------------------")
    else:
        print("\nError: City not found! Please check the spelling.")

except Exception as e:
    print("\nError: Please check your internet connection.")
