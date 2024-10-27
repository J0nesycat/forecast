import unittest
from unittest.mock import patch, mock_open
import os
import json
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weather_app.accounts.usersDB import load_users, save_users


class TestUsersDBFunctions(unittest.TestCase):

    @patch('weather_app.accounts.usersDB.USERS_FILE', '/fake/path/users_db.json')
    @patch('os.path.exists', return_value=False)
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('weather_app.accounts.usersDB.save_users')
    def test_load_users_file_not_exists(self, mock_save_users, mock_open, mock_makedirs, mock_exists):
        # Test case when the users file doesn't exist and a new one is created
        result = load_users()
        self.assertEqual(result, {})  # Since default_users is an empty dict
        mock_save_users.assert_called_once_with({})  # Ensure save_users is called to create the file

    @patch('weather_app.accounts.usersDB.USERS_FILE', '/fake/path/users_db.json')
    @patch('os.path.exists', return_value=True)
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_load_users_file_exists(self, mock_open, mock_makedirs, mock_exists):
        # Test case when the users file exists and is successfully loaded
        result = load_users()
        self.assertEqual(result, {})  # Expecting an empty dictionary loaded from the file

    @patch('weather_app.accounts.usersDB.USERS_FILE', '/fake/path/users_db.json')
    @patch('os.path.exists', return_value=True)
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open, read_data='invalid json')
    def test_load_users_invalid_json(self, mock_open, mock_makedirs, mock_exists):
        # Test case when the JSON file is corrupted and can't be decoded
        result = load_users()
        self.assertEqual(result, {})  # Expecting an empty dictionary when JSON decoding fails

    @patch('weather_app.accounts.usersDB.USERS_FILE', '/fake/path/users_db.json')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_users(self, mock_open, mock_makedirs):
        users_data = {'user1': {'password': 'password123'}}
        save_users(users_data)

        # Check that the file was opened for writing
        mock_open.assert_called_once_with('/fake/path/users_db.json', 'w')

        # Check that write was called multiple times (since json.dump writes in chunks)
        written_data = ''.join(call[0][0] for call in mock_open().write.call_args_list)

        # Check if the correct JSON data was written to the file
        expected_data = json.dumps(users_data, indent=4)
        self.assertEqual(written_data, expected_data)


if __name__ == '__main__':
    unittest.main()
