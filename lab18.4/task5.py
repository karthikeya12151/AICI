import requests
import json
import os

def get_weather_and_save(city_name):
    api_key = "fb4a7548f821a83678bea7c37449ee4e"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data.get("cod") == 200:
            city = data.get("name")
            temp = data["main"].get("temp")
            humidity = data["main"].get("humidity")
            description = data["weather"][0].get("description")

            # Console output
            print(f"City: {city}")
            print(f"Temperature: {int(round(temp))}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description.capitalize()}")

            # Prepare to save result
            result_entry = {
                "city": city,
                "temp": int(round(temp)),
                "humidity": humidity,
                "weather": description.capitalize()
            }

            # Load existing data
            results_filename = "results.json"
            results = []
            if os.path.isfile(results_filename):
                try:
                    with open(results_filename, "r", encoding="utf-8") as f:
                        results = json.load(f)
                except Exception:
                    results = []

            # Append new entry and save back
            results.append(result_entry)
            with open(results_filename, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=4)

        else:
            print("Error: City not found. Please enter a valid city.")

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to the weather service. {e}")
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    user_input = input("Enter city name: ")
    get_weather_and_save(user_input)
