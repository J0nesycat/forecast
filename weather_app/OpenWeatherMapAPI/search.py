import requests
import logging
from weather_app.OpenWeatherMapAPI.APIkey import key


def Geocoding():
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
        logging.error(f"Request to OpenWeather API failed with status code: {response.status_code}")
        print(f"Request failed with status code: {response.status_code}")









