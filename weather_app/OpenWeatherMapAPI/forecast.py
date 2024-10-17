import requests
from weather_app.OpenWeatherMapAPI.APIkey import key

def weather_forecast():


    lat = input("Please insert the latitude: ")
    lon = input("Please insert the longitude: ")
    print("You will receive the weather forecast for the upcoming 5 days.")

    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
            data = response.json()

            city = data["city"]["name"]
            lat = data["city"]["coord"]["lat"]
            lon = data["city"]["coord"]["lon"]

            print(f"City: {city}")
            print(f"Latitude: {lat}")
            print(f"Longitude: {lon}")

            # Loop through the 5-day forecast, getting an entry every 8th index (which is every day)
            for day in range(0, 40, 8):  # There are 40 entries (data every 3 hours), so 8 per day
                temp = data["list"][day]["main"]["temp"]
                feels_like = data["list"][day]["main"]["feels_like"]
                weather = data["list"][day]["weather"][0]["description"]

                date = data["list"][day]["dt_txt"]

                print(f"\nDate: {date}")
                print(f"Temperature: {temp}°C")
                print(f"Feels Like: {feels_like}°C")
                print(f"Weather: {weather}")
            print("Weather data provided by OpenWeather https://openweathermap.org/")
    else:
        print(f"Request failed with status code: {response.status_code}")




