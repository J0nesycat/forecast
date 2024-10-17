
from weather_app.accounts.authorization import authorize
from weather_app.OpenWeatherMapAPI.search import Geocoding
from weather_app.OpenWeatherMapAPI.forecast import weather_forecast


def main():
    username=input("hello friend! please enter your username: ")
    password=input("please enter password: ")
    login=authorize(username,password)


    # Check if login is authorized
    if login[0]:
        print(login[1])
        print("Proceeding to the software...")
        decision=input("Would you like to get geographical coordinates first? y/n: ")
        if decision == "y":
            Geocoding()
        else:
            weather_forecast()

    else:
        print(login[1])
        decision=input("Would you like to sign up? y/n: ")
        if decision == "y":
            print("Redirecting to registration...")
            from accounts.registration import register_user
            main()
        else:
            print("Please try again: ")
            main()

if __name__ == "__main__":
    main()






