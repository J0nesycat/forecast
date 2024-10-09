import json
import os

# Define the absolute path to the users database JSON file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
USERS_FILE = os.path.join(BASE_DIR, 'users_db.json')


def load_users():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)

    # Check if the users_db.json file exists, if not create it with default data
    if not os.path.exists(USERS_FILE):
        print(f"File not found: {USERS_FILE}. Generating a new one...")
        default_users = {}  # Add default users here if needed
        save_users(default_users)  # Save default users to the file
        return default_users

    # If file exists, try to load users
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error decoding JSON. Returning empty user database.")
        return {}


def save_users(users_db):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    with open(USERS_FILE, 'w') as file:
        json.dump(users_db, file, indent=4)  # indent=4 makes the JSON file easier to read


# Load users at the beginning of the program
users_db = load_users()
