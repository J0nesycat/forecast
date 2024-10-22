import logging
from .usersDB import users_db


def authorize(username, password):
    logging.debug(f"Attempting to authorize user: {username}")

    if username not in users_db:
        logging.warning(f"Authorization failed for {username}: User not found")
        return False, "Unauthorized: User not found"

    user_info = users_db[username]
    if user_info["password"] != password:
        logging.warning(f"Authorization failed for {username}: Incorrect password")
        return False, "Unauthorized: Incorrect password"

    logging.info(f"Authorization successful for {username}")
    return True, "Authorized: Access granted"
