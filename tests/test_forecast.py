import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weather_app.OpenWeatherMapAPI.forecast import weather_forecast

class TestWeatherForecast(unittest.TestCase):

    @patch('weather_app.OpenWeatherMapAPI.api_key.api_key', return_value='test_key')  # Mock API key function
    @patch('builtins.input', side_effect=['45', '-93'])
    @patch('weather_app.OpenWeatherMapAPI.forecast.requests.get')
    def test_weather_forecast_success(self, mock_get, mock_input, mock_api_key):
        # Mock response object for a successful API call
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "city": {"name": "North Saint Paul", "coord": {"lat": 45, "lon": -93}},
            "list": [
                {"main": {"temp": 8.47, "feels_like": 5.06}, "weather": [{"description": "clear sky"}], "dt_txt": "2024-10-17 15:00:00"},
                {"main": {"temp": 15.5, "feels_like": 13.76}, "weather": [{"description": "clear sky"}], "dt_txt": "2024-10-18 15:00:00"},
                {"main": {"temp": 17.46, "feels_like": 16.04}, "weather": [{"description": "broken clouds"}], "dt_txt": "2024-10-19 15:00:00"},
                {"main": {"temp": 19.44, "feels_like": 18.59}, "weather": [{"description": "clear sky"}], "dt_txt": "2024-10-20 15:00:00"},
                {"main": {"temp": 18.89, "feels_like": 17.54}, "weather": [{"description": "scattered clouds"}], "dt_txt": "2024-10-21 15:00:00"},
                *[{"main": {"temp": 0, "feels_like": 0}, "weather": [{"description": "n/a"}], "dt_txt": "n/a"} for _ in range(35)]
            ]
        }
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mocked_print:
            weather_forecast('test_key')  # Pass the test key directly

        mock_get.assert_called_once_with(
            'http://api.openweathermap.org/data/2.5/forecast?lat=45&lon=-93&appid=test_key&units=metric'
        )

        # Check for specific prints
        mocked_print.assert_any_call("Temperature: 8.47°C")
        mocked_print.assert_any_call("Feels Like: 5.06°C")
        mocked_print.assert_any_call("Weather: clear sky")

    @patch('weather_app.OpenWeatherMapAPI.api_key.api_key', return_value='test_key')  # Mock API key function
    @patch('builtins.input', side_effect=['45', '-93'])
    @patch('weather_app.OpenWeatherMapAPI.forecast.requests.get')
    def test_weather_forecast_failure(self, mock_get, mock_input, mock_api_key):
        # Mock response object for a failed API call
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"message": "city not found"}
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mocked_print:
            weather_forecast('test_key')  # Pass the test key directly

        mock_get.assert_called_once_with(
            'http://api.openweathermap.org/data/2.5/forecast?lat=45&lon=-93&appid=test_key&units=metric'
        )

        # Check that the failure message is printed
        mocked_print.assert_any_call("Request failed with status code: 404")
        mocked_print.assert_any_call("Error message: city not found")


if __name__ == '__main__':
    unittest.main()
