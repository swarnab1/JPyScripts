import string
import random


def PasswordGenerator():

    print("This program will generate a random password for you.")

    while True:
        userPasswordLength = input("PasswordGenerator >>> Enter the length of the password: ")
        if userPasswordLength == "" or userPasswordLength.isdigit() is False:
            print("Enter a valid number")
            continue
        elif int(userPasswordLength) < 8 or int(userPasswordLength) > 32:
            print("Password must be at least 8 characters long and at most 32 characters long")
            continue
        else:
            userPasswordLength = int(userPasswordLength)
        userPassword = ''.join(
            random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(userPasswordLength))
        print("\nYour password is:", userPassword)

        print("To generate another password, press Enter. To exit, type anything and press Enter.")
        if input("PasswordGenerator >>> ") == "":
            continue
        else:
            return
