import requests
from weather_app.OpenWeatherMapAPI.APIkey import key
from weather_app.OpenWeatherMapAPI.forecast import  weather_forecast

def Geocoding():

    city_name = input("Enter the city name: ")
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









