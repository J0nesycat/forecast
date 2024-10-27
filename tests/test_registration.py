import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weather_app.accounts.registration import register_user

class TestRegisterUserFunction(unittest.TestCase):

    @patch('weather_app.accounts.registration.users_db', {'test_existing_user': {'password': 'correct_password'}})
    @patch('builtins.input', side_effect=['test_existing_user', 'some_password'])
    def test_user_name_exists(self, mock_input):
        result = register_user()
        self.assertEqual(result, 'Registration failed: Username already exists')

    @patch('weather_app.accounts.registration.users_db', {})
    @patch('builtins.input', side_effect=['new_user', 'new_password'])
    @patch('weather_app.accounts.registration.save_users')
    def test_successful_registration(self, mock_save_users, mock_input):
        result = register_user()
        self.assertEqual(result, 'Registration successful: new_user added')
        mock_save_users.assert_called_once()

if __name__ == '__main__':
    unittest.main()
