import getpass # getpass module allows for a hidden password prompt - a nice thing for a little extra security
from socket import gethostname
from os import system
from time import sleep

userChoice = 0 # initialise variable before global or pycharm screams at you


def menu():
    system("cls") # clears screen to stop output stacking on top of each other
    print("""[1] Login
[2] Register
[3] Exit\n""")
    global userChoice
    userChoice = int(input(f"{getpass.getuser()}@{gethostname()}:~$ ")) # linux style command line input because why not

    match userChoice:
        case 1:
            login()
        case 2:
            register()
        case 3:
            exit(0)
        case _:
            print("Error: Invalid Input.")
            sleep(1.5) # Could make it go back to start but it's rare someone can't read what they enter


def login():
    system("cls")
    username = input("Username: ")
    password = getpass.getpass("Password: ") # hidden password prompt

    with open("userData.txt", "r") as userData: #checking if the username/password combination is in userData.txt
        logins = userData.readlines()
        for user in logins:
            if user.find(f"{username}, {password}") != -1:
                print("Login Success.")
                input()
            else:
                print("Invalid Details.")
                input()


def register():
    system("cls")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    password2 = getpass.getpass("Repeat Password: ") # Double entry check for good validation

    while password2 != password:
        print("Passwords do not match, try again.")
        sleep(1.5)
        system("cls")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        password2 = getpass.getpass("Repeat Password: ")

    with open("userData.txt", "w") as userData:
        userData.write(f"{username}, {password}\n")

    print("Register Success.")
    sleep(1.5)

    menu()


if __name__ == "__main__":
    menu()
