

# DSC 510
# Week 11
# Programming Assignment 11.FINAL
# Author: Doug Nolan
# Date: 11/23/2025

import requests


def get_user_input():
    """Get a valid ZIP code or city + state from the user (US only)."""
    while True:
        print("\nWelcome to Doug's Dazzling Weather Forecaster!")
        print("-" * 50)

        user_location = input("Please enter a ZIP code or city name: ").strip()

        # ZIP code branch
        if user_location.isdigit():
            if len(user_location) == 5:
                print(f"You entered ZIP code: {user_location}")
                return user_location  # we'll append ,US later for API call
            else:
                print("Invalid ZIP code. Please enter exactly 5 digits.\n")
                continue

        # City + State branch
        else:
            state = input(f"Enter the 2-letter state abbreviation for {user_location}: ").strip()
            if len(state) == 2 and state.isalpha():
                city_state = f"{user_location}, {state}"
                print(f"You entered city: {city_state}")
                return city_state
            else:
                print("Invalid state. Please enter exactly 2 letters.\n")
                continue


def get_coordinates(query, api_key):
    """
    Use OpenWeather's geocoding API to get latitude and longitude.
    Ensures query targets the United States.
    """

    # If the query looks like a 5-digit ZIP, append ",US".
    if query.isdigit() and len(query) == 5:
        q_param = f"{query},US"
    else:
        # Append country for city,state entries if not already present
        # If user already included country, we won't append twice.
        q_param = f"{query}, US" if ", US" not in query and ",US" not in query else query

    location_url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": q_param,       # supports ZIP or "city, state, US"
        "limit": 1,
        "appid": api_key
    }

    try:
        response = requests.get(location_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data:
            print("Location not found. Please try again.\n")
            return None, None

        location = data[0]
        lat = location.get("lat")
        lon = location.get("lon")

        # Safety check
        if lat is None or lon is None:
            print("Geocoding returned no coordinates. Raw response:")
            print(data)
            return None, None

        print("\nLocation Found: "
              f"{location.get('name', '')}, {location.get('state', '')} {location.get('country', '')}")
        return lat, lon

    except requests.HTTPError as http_err:
        # API returned an HTTP error (401 = invalid API key, 429 = rate limited, etc.)
        status = getattr(http_err.response, "status_code", "unknown")
        print(f"Geocoding HTTP error ({status}): {http_err}")
        # optionally show returned JSON for debugging when not 401
        try:
            print("Response:", http_err.response.json())
        except Exception:
            pass
        return None, None
    except requests.RequestException as req_err:
        print(f"Geocoding request failed: {req_err}")
        return None, None


def get_weather(lat, lon, api_key):
    """Fetch and display current weather from OpenWeather."""
    if lat is None or lon is None:
        print("Invalid coordinates. Skipping weather lookup.")
        return

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "imperial"   # Fahrenheit; change to "metric" for Celsius
    }

    try:
        response = requests.get(weather_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        main_data = data.get("main", {})
        clouds_data = data.get("clouds", {})
        weather_desc = data.get("weather", [{}])[0].get("description", "No data")

        # Print a neat, user-friendly summary
        print("\n--- Current Weather Summary ---")
        location_name = data.get("name", "Unknown location")
        print(f"Location: {location_name}")
        print(f"Current temperature: {main_data.get('temp', 'No data')}°F")
        print(f"High temperature: {main_data.get('temp_max', 'No data')}°F")
        print(f"Low temperature: {main_data.get('temp_min', 'No data')}°F")
        print(f"Pressure: {main_data.get('pressure', 'No data')} hPa")
        print(f"Humidity: {main_data.get('humidity', 'No data')}%")
        print(f"Cloud coverage: {clouds_data.get('all', 'No data')}%")
        print(f"Weather: {weather_desc.capitalize()}")
        print("-------------------------------")

    except requests.HTTPError as http_err:
        status = getattr(http_err.response, "status_code", "unknown")
        print(f"Weather HTTP error ({status}): {http_err}")
        try:
            print("Response:", http_err.response.json())
        except Exception:
            pass
    except requests.RequestException as req_err:
        print(f"Weather lookup failed: {req_err}")


def main():
    """Main program loop."""
    # >>> Replace with your OpenWeather API key if needed
    api_key = "fc104f5a81be102c15c215d8140f84e2"

    # Basic quick checks
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("ERROR: You must set a valid OpenWeather API key in the script.")
        return

    while True:
        query = get_user_input()
        lat, lon = get_coordinates(query, api_key)
        get_weather(lat, lon, api_key)

        again = input("\nLook up another location? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using Doug's Dazzling Weather Forecaster!")
            break


if __name__ == "__main__":
    main()
