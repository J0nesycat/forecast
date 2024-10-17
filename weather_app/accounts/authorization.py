
from .usersDB import users_db


def authorize(username, password):

    if username not in users_db:
        return False,"Unauthorized: User not found"
    user_info = users_db[username]
    if user_info["password"] !=password:
        return False,"Unauthorized: Incorrect password"

    return True,"Authorized: Access granted"
