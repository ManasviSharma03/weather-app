from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
print("API_KEY loaded:", API_KEY)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    try:
        # Build complete API URL
        params = {
            'q': city_name,
            'appid': API_KEY,
            'units': 'metric'  # To get temperature in Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check for error in response
        if response.status_code != 200:
            print(f"❌ Error: {data.get('message', 'Unable to fetch weather data')}")
            return None

        # Extract relevant data
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        # Return weather details
        return {
            'City': city,
            'Country': country,
            'Temperature (°C)': temp,
            'Humidity (%)': humidity,
            'Condition': description.title()
        }

    except Exception as e:
        print("❌ Exception occurred:", e)
        return None

def main():
    print("=== ☁️ Weather App ☀️ ===")
    city = input("Enter city name: ").strip()
    weather = get_weather(city)

    if weather:
        print("\n📍 Weather Details:")
        for key, value in weather.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
