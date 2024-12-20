import requests
import logging


def Geocoding(key):
    city_name = input("Enter the city name: ")
    logging.debug(f"User input for city: {city_name}")

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={key}"
    logging.debug(f"Requesting geographical data from URL: {url}")

    response = requests.get(url)

    if response.status_code == 200:
        logging.info("Geocoding data successfully retrieved.")
        data = response.json()

        if data:  # Ensure there's at least one result in the list
            city_data = data[0]  # Get the first result in the list
            city = city_data["name"]
            lat = city_data["lat"]
            lon = city_data["lon"]
            country = city_data["country"]

            logging.debug(f"City: {city}, Latitude: {lat}, Longitude: {lon}, Country: {country}")

            print(f"City: {city}")
            print(f"Latitude: {lat}")
            print(f"Longitude: {lon}")
            print(f"Country: {country}")
        else:
            logging.warning(f"No results found for city: {city_name}")
            print(f"No results found for city: {city_name}")
    else:
        # Attempt to retrieve an error message from the API response JSON
        try:
            error_message = response.json().get("message", "No detailed error message provided.")
        except ValueError:
            error_message = "No detailed error message provided (invalid JSON response)."

        logging.error(f"Request to OpenWeather API failed with status code: {response.status_code} - {error_message}")
        print(f"Request failed with status code: {response.status_code}")
        print(f"Error message: {error_message}")
