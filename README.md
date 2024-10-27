# Weather Forecast App

## Overview
This project is a weather forecast application that retrieves current weather data from the OpenWeatherMap API. It provides users with up-to-date weather details for selected locations.

## Features
- Displays current weather data: 
  - Temperature
  - Humidity *(planned for v1.2)*
  - Wind Speed *(planned for v1.3)*
- Supports multiple locations.
- Error handling for invalid inputs and API failures.
- Secure API key management, prompting users for API key input and storing it securely.
- User-friendly interface for straightforward interaction.
.

## Project Structure
- `accounts/`: Manages user accounts and authentication.
- `weather.py`: Main application logic for fetching and displaying weather data.
- `OpenWeatherMapAPI/`: Handles requests to the OpenWeatherMap API.
  
## Prerequisites
- **Python 3.x**: Ensure Python is installed on your machine.
- **Docker**: Install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).

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
5. Ensure Docker is installed and running.

## Usage

1. **API Key Setup**:
   On the first run, the app will prompt you to enter your OpenWeatherMap API key. You can obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

2. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

3. **Run the container in interactive mode**:
   To run the container and get a terminal inside it:
   ```bash
   docker run -it -p 5000:5000 jonesycat/weather_forecast 
