# DSC 510
# Week 11
# Programming Assignment 11.FINAL
# Author Doug Nolan
# 11/23/2025

import requests



def get_user_input():
    while True:
        """ get user input location - Check user input for zip codes """
        user_location = input("Please enter a ZIP code or city name: ").strip()
        #check if input is digits -> then is zip code location
        if user_location.isdigit():
            if len(user_location) == 5:
                lookup_type = 1  #declaring as lookup type 1 for use later
                print(f"You entered ZIP code: {user_location}")
                return user_location, lookup_type
            else:
                print("Invalid ZIP code. Please enter exactly 5 digits.\n")
                continue

        else:
            """ask for state if city name was entered"""
            state = input(f"Enter the state abbreviation for {user_location}: ").strip().upper()
            if len(state) == 2 and state.isalpha():
                lookup_type = 2  #declaring as lookup type 2 for use later
                print(f"You entered city: {user_location}, state: {state}")
                return f"{user_location},{state}", lookup_type
            else:
                print("Invalid state. Please enter exactly 2 letters.\n")
                continue


def get_coordinates(query, api_key, lookup_type):
    """Use OpenWeather's geocoding API to get latitude and longitude."""
    if lookup_type == 2:
        query = f"{query},US"
    #url for city state
        location_url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            "q": query,
            "appid": api_key
        }
    else:
        query = f"{query},US"
    #url for zip lookup
        location_url = "http://api.openweathermap.org/geo/1.0/zip"
        params = {
            "zip": query,
            "appid": api_key
        }

    try:
        response = requests.get(location_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        # zip return object
        if lookup_type == 1:
            lat = data["lat"]
            lon = data["lon"]
            name = data["name"]
            country = data["country"]
            print(f"\nLocation Found: {name}, {country}")
            return  lat, lon
        # City Return list
        if not data:
            print("No Location found. Please try again.\n")
            return None, None

        location = data[0]
        lat = location["lat"]
        lon = location["lon"]

        # Display the found location
        name = location.get("name", "")
        state = location.get("state", "")
        country = location.get("country", "")
        print(f"\nLocation Found: {name}, {state} {country}")

        return lat, lon

    except requests.RequestException as error:
        print(f"Geocoding request failed: {error}")
        return None, None



def get_weather(lat, lon, api_key):
    """Fetch current weather using Openweather"""
    if lat is None or lon is None:
        print("Invalid coordinates. Skipping weather lookup.")
        return
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "imperial"  #nobody understand Kelvin units
    }

    try:
        response = requests.get(weather_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        main_data = data.get("main", {})
        clouds_data = data.get("clouds", {})
        weather_desc = data.get("weather", [{}])[0].get("description", "No data")

        print(f"\nCurrent temperature: {main_data.get('temp', 'No data')}°F")
        print(f"High temperature: {main_data.get('temp_max', 'No data')}°F")
        print(f"Low temperature: {main_data.get('temp_min', 'No data')}°F")
        print(f"Pressure: {main_data.get('pressure', 'No data')} hPa")
        print(f"Humidity: {main_data.get('humidity', 'No data')}%")
        print(f"Cloud coverage: {clouds_data.get('all', 'No data')}%")
        print(f"Weather: {weather_desc.capitalize()}")

    except requests.RequestException as error:
        print(f"Weather lookup failed: {error}")

def ask_to_continue():
    """Allow user to look up multiple locations"""
    while True:
        user_choice = input("\nLook up another location? (y/n): ").strip().lower()
        if user_choice in ("y", "n"):
            return user_choice == "y"
        else:
            print("Invalid entry. Please enter 'y' or 'n'.")

def main():
    """main function entry point"""
    # print welcome message
    print("\nWelcome to the Doug's Dazzling Weather Forecaster!")
    print("-" * 50)
    print(" " * 30)

    api_key = 'fc104f5a81be102c15c215d8140f84e2'
    lookup_type = 0
    while True:
        query, lookup_type = get_user_input()
        lat, lon = get_coordinates(query, api_key, lookup_type)
        if lat and lon:
            print(f"\nWeather report:")
            get_weather(lat, lon, api_key)

        if not ask_to_continue():
            break

if __name__ == "__main__":
    main()


