import unittest
from unittest.mock import patch, Mock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weather_app.OpenWeatherMapAPI.search import Geocoding
from weather_app.OpenWeatherMapAPI.APIkey import key

class TestGeocodingFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['London'])
    @patch('weather_app.OpenWeatherMapAPI.search.requests.get')
    def test_geocoding_success(self, mock_get, mock_input):
        # Mock successful API response for geocoding
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{
            "name": "London",
            "lat": 51.5073219,
            "lon": -0.1276474,
            "country": "GB"
        }]
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mocked_print:
            Geocoding()

        # Assert that the API call was made with the correct URL
        mock_get.assert_called_once_with(
            f'http://api.openweathermap.org/geo/1.0/direct?q=London&appid={key}'
        )

        # Assert the correct print statements were called
        mocked_print.assert_any_call("City: London")
        mocked_print.assert_any_call("Latitude: 51.5073219")
        mocked_print.assert_any_call("Longitude: -0.1276474")
        mocked_print.assert_any_call("Country: GB")

    @patch('builtins.input', side_effect=['Unknown City'])
    @patch('weather_app.OpenWeatherMapAPI.search.requests.get')
    def test_geocoding_no_results(self, mock_get, mock_input):
        # Mock API response with no results
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []  # No results found
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mocked_print:
            Geocoding()

        # Assert that the API call was made with the correct URL
        mock_get.assert_called_once_with(
            f'http://api.openweathermap.org/geo/1.0/direct?q=Unknown City&appid={key}'
        )

        # Assert the "no results" message is printed
        mocked_print.assert_any_call("No results found for city: Unknown City")

    @patch('builtins.input', side_effect=['London'])
    @patch('weather_app.OpenWeatherMapAPI.search.requests.get')
    def test_geocoding_api_failure(self, mock_get, mock_input):
        # Mock failed API response
        mock_response = Mock()
        mock_response.status_code = 404  # Simulating a failed request
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mocked_print:
            Geocoding()

        # Assert that the API call was made with the correct URL
        mock_get.assert_called_once_with(
            f'http://api.openweathermap.org/geo/1.0/direct?q=London&appid={key}'
        )

        # Assert the failure message is printed
        mocked_print.assert_any_call("Request failed with status code: 404")


if __name__ == '__main__':
    unittest.main()
