import requests
import logging
from weather_app.OpenWeatherMapAPI.APIkey import key


def weather_forecast():
    lat = input("Please insert the latitude: ")
    lon = input("Please insert the longitude: ")
    logging.debug(f"User input for latitude: {lat}, longitude: {lon}")

    print("You will receive the weather forecast for the upcoming 5 days.")

    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&units=metric"
    logging.debug(f"Requesting weather data from URL: {url}")

    response = requests.get(url)

    if response.status_code == 200:
        logging.info("Weather data successfully retrieved from OpenWeather API.")
        data = response.json()

        city = data["city"]["name"]
        lat = data["city"]["coord"]["lat"]
        lon = data["city"]["coord"]["lon"]

        logging.debug(f"City: {city}, Latitude: {lat}, Longitude: {lon}")

        print(f"City: {city}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")

        # Loop through the 5-day forecast, getting an entry every 8th index (which is every day)
        for day in range(0, 40, 8):  # There are 40 entries (data every 3 hours), so 8 per day
            temp = data["list"][day]["main"]["temp"]
            feels_like = data["list"][day]["main"]["feels_like"]
            weather = data["list"][day]["weather"][0]["description"]

            date = data["list"][day]["dt_txt"]

            logging.debug(f"Forecast for {date}: Temp: {temp}°C, Feels Like: {feels_like}°C, Weather: {weather}")

            print(f"\nDate: {date}")
            print(f"Temperature: {temp}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Weather: {weather}")

        print("Weather data provided by OpenWeather https://openweathermap.org/")
    else:
        logging.error(f"Request to OpenWeather API failed with status code: {response.status_code}")
        print(f"Request failed with status code: {response.status_code}")




