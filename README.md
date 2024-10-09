# Weather Forecast App

## Overview
This project is a weather forecast application that retrieves current weather data from the OpenWeatherMap API. The app provides users with accurate and up-to-date weather information for their location.

## Features
- Displays current weather data such as temperature, humidity, and wind speed.
- Supports multiple locations.
- User-friendly interface for easy interaction.

## Project Structure
- `accounts/`: Manages user accounts and authentication.
- `weather.py`: Main application logic for fetching and displaying weather data.
- `OpenWeatherMapAPI/`: Handles requests to the OpenWeatherMap API.
  
## Installation

1. Clone this repository:
    ```bash
    git clone git@github.com:J0nesycat/forecast.git
    ```
2. Navigate to the project directory:
    ```bash
    cd weather_forecast
    ```
3. Set up the virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
2. Run the application:
    ```bash
    python weather.py
    ```

## Contributions
Feel free to submit issues, fork the project, or contribute via pull requests.

## License
[MIT License](LICENSE)

