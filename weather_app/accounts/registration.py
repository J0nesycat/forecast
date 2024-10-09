
from accounts.usersDB import users_db, save_users


def register_user(username,password):

    if username in users_db:
        return print("Registration failed: Username already exists")


    users_db[username] = {"password": password}
    save_users(users_db)
    return print(f"Registration successful: {username} added")



username=input("Please enter username: ")
password=input("please enter password: ")
register_user(username, password)
