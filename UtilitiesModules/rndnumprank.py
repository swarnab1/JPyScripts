import webbrowser
import random


def rndnumprank():
    list69 = ["Really?", "Come on", "You donkey", "Internet degenerate", "OMG FUNNY NUMBER"]
    list420 = ["Stop you degenerate", "Smoke weed everyday", "Dude what", "Reddit user",
               "Get some help"]

    while True:
        userInput = input("RndNumPrank >>> Enter a number: ")
        if userInput == "":
            print("You didn't enter anything")
            continue
        elif userInput.isdigit() is False:
            print("Please enter a valid number")
            continue
        elif int(userInput) == 69:
            print(random.choice(list69))
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0,
                            autoraise=True)
        elif int(userInput) == 420:
            print(random.choice(list420))
            webbrowser.open("https://www.youtube.com/watch?v=fC7oUOUEEi4", new=0,
                            autoraise=True)
        else:
            print("The number is:", userInput)

        print("To rerun, press Enter. To exit, type anything and press Enter.")
        if input("RndNumPrank >>> ") == "":
            continue
        else:
            return
