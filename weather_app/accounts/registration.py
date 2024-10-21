import logging
from .usersDB import users_db, save_users


def register_user() -> object:
    logging.debug("Starting user registration process")

    username = input("Please enter username: ")
    password = input("Please enter password: ")
    logging.debug(f"Attempting to register user: {username}")

    if username in users_db:
        message = "Registration failed: Username already exists"
        logging.warning(f"Registration failed for {username}: Username already exists")
        print(message)
        return message

    users_db[username] = {"password": password}
    save_users(users_db)
    message = f"Registration successful: {username} added"
    logging.info(f"User {username} successfully registered")
    print(message)
    return message



