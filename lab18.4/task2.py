import requests
import json

def get_and_display_weather_json():
    city = input("Enter city name: ")
    api_key = "fb4a7548f821a83678bea7c37449ee4e"  # Use your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data.get("cod") == 200:
            print(json.dumps(data, indent=4))
        else:
            print(f"Error: {data.get('message', 'Unknown error occurred')}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as ex:
        print(f"Unexpected Error: {ex}")

if __name__ == "__main__":
    get_and_display_weather_json()
