import logging
from weather_app.accounts.authorization import authorize
from weather_app.OpenWeatherMapAPI.search import Geocoding
from weather_app.OpenWeatherMapAPI.forecast import weather_forecast
from weather_app.accounts.registration import register_user

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])

def get_validated_input(prompt, valid_options):
    """Prompt user until they enter a valid option."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
            logging.warning(f"Invalid input received: {user_input}")

def main():
    logging.info("Starting the application")

    username = input("hello friend! please enter your username: ")
    password = input("please enter password: ")
    logging.debug(f"User {username} is trying to log in.")
    login = authorize(username, password)

    # Check if login is authorized
    if login[0]:
        logging.info(f"User {username} authorized successfully.")
        print(login[1])
        print("Proceeding to the software...")
        decision = get_validated_input("Would you like to get geographical coordinates first? y/n: ", ["y", "n"])
        logging.debug(f"User decision to get coordinates: {decision}")

        if decision == "y":
            logging.info(f"User {username} opted to fetch geographical coordinates.")
            Geocoding()
            decision = get_validated_input("Would you like to get weather forecast? y/n: ", ["y", "n"])
            logging.debug(f"User decision to get weather forecast: {decision}")

            if decision == "y":
                logging.info(f"User {username} opted to get weather forecast.")
                weather_forecast()
            else:
                logging.info(f"User {username} chose to exit after Geocoding.")
                exit()
        else:
            logging.info(f"User {username} skipped Geocoding and opted for weather forecast.")
            weather_forecast()

    else:
        logging.warning(f"User {username} failed to log in: {login[1]}")
        print(login[1])
        decision = get_validated_input("Would you like to sign up? y/n: ", ["y", "n"])
        logging.debug(f"User decision to sign up: {decision}")

        if decision == "y":
            logging.info(f"User {username} chose to sign up.")
            print("Redirecting to registration...")
            register_user()
            main()  # Recursively call main after registration
        else:
            logging.info(f"User {username} chose not to sign up.")
            print("Please try again: ")
            main()

if __name__ == "__main__":
    main()
