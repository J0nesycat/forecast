
from .usersDB import users_db, save_users


def register_user() -> object:

    username = input("Please enter username: ")
    password = input("please enter password: ")


    if username in users_db:
        message= "Registration failed: Username already exists"
        print(message)
        return message


    users_db[username] = {"password": password}
    save_users(users_db)
    message = f"Registration successful: {username} added"
    print(message)
    return message




