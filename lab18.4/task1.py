import requests
import json

def display_weather_details():
    # Ask the user for the city name
    city = input("Enter city name: ")
    api_key = "fb4a7548f821a83678bea7c37449ee4e"  # replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Send the API request
        response = requests.get(base_url)
        data = response.json()

        # Check if the request was successful
        if data["cod"] == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]

            # Display results
            print("\n--- Weather Details ---")
            print(f"City: {city_name}, {country}")
            print(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_desc.capitalize()}")
            print("------------------------")

        else:
            print(f"\nCity '{city}' not found. Please check the spelling or try again.")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the weather service: {e}")
    except KeyError:
        print("Unexpected response structure. Please check your API key or city name.")

# Run the function
if __name__ == "__main__":
    display_weather_details()
