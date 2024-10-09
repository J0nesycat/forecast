
from accounts.authorization import authorize



def main():
    username=input("hello friend! please enter your username: ")
    password=input("please enter password: ")
    login=authorize(username,password)


    # Check if login is authorized
    if login[0]:
        print(login[1])
        print("Proceeding to the software...")
        decision=input("Would you like to get geographical coordinates first? y/n: ")
        if decision == "y":
            from OpenWeatherMapAPI import search
        else:
            from OpenWeatherMapAPI import forecast

    else:
        print(login[1])
        decision=input("Would you like to sign up? y/n: ")
        if decision == "y":
            print("Redirecting to registration...")
            from accounts.registration import register_user
            main()
        else:
            print("Please try again: ")
            main()

if __name__ == "__main__":
    main()






