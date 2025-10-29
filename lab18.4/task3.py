import requests
def display_weather_summary():
    city = input("Enter city name: ")
    api_key = "fb4a7548f821a83678bea7c37449ee4e"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        data = response.json()
        if data["cod"] == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            print(f"City: {city_name}")
            print(f"Temperature: {int(round(temp))}°C")
            print(f"Humidity: {humidity}%")
            print(f"      Weather: {description.capitalize()}")
        else:
            print(f"City '{city}' not found. Please check the spelling or try again.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the weather service: {e}")
    except KeyError:
        print("Unexpected response structure. Please check your API key or city name.")
if __name__ == "__main__":
    display_weather_summary()
