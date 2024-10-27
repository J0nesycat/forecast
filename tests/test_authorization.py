import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from weather_app.accounts.authorization import authorize

class TestAuthorizeFunction(unittest.TestCase):

    @patch('weather_app.accounts.authorization.users_db', {'test_user': {'password': 'correct_password'}})
    def test_authorize_user_not_found(self):
        # Test when the username is not in users_db
        result = authorize('unknown_user', 'some_password')
        self.assertEqual(result, (False, 'Unauthorized: User not found'))

    @patch('weather_app.accounts.authorization.users_db', {'test_user': {'password': 'correct_password'}})
    def test_authorize_incorrect_password(self):
        # Test when the password is incorrect
        result = authorize('test_user', 'wrong_password')
        self.assertEqual(result, (False, 'Unauthorized: Incorrect password'))

    @patch('weather_app.accounts.authorization.users_db', {'test_user': {'password': 'correct_password'}})
    def test_authorize_success(self):
        # Test when the username and password are correct
        result = authorize('test_user', 'correct_password')
        self.assertEqual(result, (True, 'Authorized: Access granted'))

if __name__ == '__main__':
    unittest.main()