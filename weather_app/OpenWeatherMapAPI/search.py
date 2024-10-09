import requests
from OpenWeatherMapAPI.APIkey import key


def Geocoding(city_name, key):

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data:  # Ensure there's at least one result in the list
            city_data = data[0]  # Get the first result in the list
            city = city_data["name"]
            lat = city_data["lat"]
            lon = city_data["lon"]
            country = city_data["country"]

            print(f"City: {city}")
            print(f"Latitude: {lat}")
            print(f"Longitude: {lon}")
            print(f"Country: {country}")
        else:
            print(f"No results found for city: {city_name}")
    else:
        print(f"Request failed with status code: {response.status_code}")





city_name = input("Enter the city name: ")
Geocoding(city_name, key)
decision=input("Would you like to get weather forecast? y/n: ")
if decision == "y":
    from OpenWeatherMapAPI import forecast
else:
    exit()
