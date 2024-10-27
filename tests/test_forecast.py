import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weather_app.OpenWeatherMapAPI.forecast import weather_forecast
from weather_app.OpenWeatherMapAPI.APIkey import key

class TestWeatherForecast(unittest.TestCase):

    @patch('builtins.input', side_effect=['45', '-93'])
    @patch('weather_app.OpenWeatherMapAPI.forecast.requests.get')
    def test_weather_forecast_success(self, mock_get, mock_input):
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
                # Add enough entries with 'feels_like' key to satisfy the 5-day forecast access pattern
                *[{"main": {"temp": 0, "feels_like": 0}, "weather": [{"description": "n/a"}], "dt_txt": "n/a"} for _ in range(35)]
            ]
        }
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mocked_print:
            weather_forecast()

        mock_get.assert_called_once_with(
            f'http://api.openweathermap.org/data/2.5/forecast?lat=45&lon=-93&appid={key}&units=metric'
        )

        mocked_print.assert_any_call("City: North Saint Paul")

    @patch('builtins.input', side_effect=['45', '-93'])
    @patch('weather_app.OpenWeatherMapAPI.forecast.requests.get')
    def test_weather_forecast_failure(self, mock_get, mock_input):
        # Mock response object for a failed API call
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mocked_print:
            weather_forecast()

        mock_get.assert_called_once_with(
            f'http://api.openweathermap.org/data/2.5/forecast?lat=45&lon=-93&appid={key}&units=metric'
        )

        # Check that the failure message is printed
        mocked_print.assert_any_call("Request failed with status code: 404")


if __name__ == '__main__':
    unittest.main()
