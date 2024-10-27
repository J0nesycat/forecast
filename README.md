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
    cd forecast
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
5.  Requirements
    ```bash
    - **Docker**: This project requires Docker for building and running containers.
    - Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
    - Ensure Docker is running and accessible in your command line interface.
     ```
## Usage

1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

## Setting Up the API Key

1. **Run the container in interactive mode**:
   To run the container and get a terminal inside it, users should execute:
   ```bash
   docker run -it -p 5000:5000 jonesycat/weather_forecast:fixed /bin/bash

2. Navigate to the directory: Once inside the container, they can navigate to the directory where APIkey.py is located:
cd /app/weather_app/OpenWeatherMapAPI/

3. Open the file for editing:
nano APIkey.py

key = "YOUR_API_KEY_HERE"  # Replace this with your actual API key

4. Run the application:
    ```bash
    python weather.py
    ```


## Contributions
Feel free to submit issues, fork the project, or contribute via pull requests.

## License
[MIT License](LICENSE)

