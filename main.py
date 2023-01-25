# Start of code for JPyScripts Main
# Import modules
import os
import requests
import platform

# Import utilities modules from JPyScripts\UtilitiesModules
from UtilitiesModules import simplecalc as splclc, TempConvert as tmpcvt, fizzbuzz as fzbz, \
    SearchQuery as searchQ, hasher, rndnumprank as rnp, divcheck as divchk, PasswordGenerator as passgen

print(
    "\u001b[32mWelcome to the JPyScripts!\nThis is a collection of scripts/utilities I made in Python.\n"
    "Type 'help' for more info\n"
    "Code by: @Joshboi || GitHub: github.com/swarnab1 || swarnab1.github.io\n")

if __name__ == "__main__":

    while True:  # Main loop
        userMainInput = input("JPyScripts >>> ")
        match userMainInput.casefold():
            case "":
                continue

            # Utilities commands
            case "fizzbuzz":
                fzbz.fizzbuzz()
            case "rndnumprank":
                rnp.rndnumprank()
            case "simplecalc":
                splclc.simplecalc()
            case "divcheck":
                divchk.divCheck()
            case "myip":
                try:
                    tryConnection = requests.get("https://1.1.1.1")
                except requests.exceptions.ConnectionError:
                    print("Error: Unable to fetch IP data. Please check your internet connection.")
                    continue
                else:
                    print("\nYour Public IP address is:", requests.get('http://ip-api.com/json').json()['query'])
                    print("Your country is:", requests.get('http://ip-api.com/json').json()['country'])
                    print("Your city is:", requests.get('http://ip-api.com/json').json()['city'])
                    print("Your ISP is:", requests.get('http://ip-api.com/json').json()['isp'])
                    print("Your timezone is:", requests.get('http://ip-api.com/json').json()['timezone'])
                    print("[These information are visible to everybody because of your public IP address]\n")
                    continue
            case "search":
                searchQ.SearchQuery()
            case "passgen":
                passgen.PasswordGenerator()
            case "tempconvert":
                tmpcvt.TempConvert()
            case "hasher":
                hasher.hasher()

            # Other commands
            case "exit":
                exit()
            case "cls":
                os.system('cls')
                continue
            case "pyversion":
                print("Python version:", platform.python_version())
                continue
            case "about":
                print(
                    "\nWelcome to the JPyScripts!\n"
                    "This is a collection of scripts/utilities I made in Python.\n"
                    "Type 'help' for more info\n"
                    "This program is open-source and is available on GitHub.\n"
                    "Warning: This program is not optimized well and may not work on some systems.\n"
                    "Code by: "
                    "@Joshboi || GitHub: github.com/swarnab1 || swarnab1.github.io\n")
                continue

            # Help command starts here
            case "help":
                print(
                    "\n"
                    "Utilities commands:\n"
                    "fizzbuzz - FizzBuzz Test\n"
                    "rndnumprank - Random Number Prank\n"
                    "simplecalc - Simple Calculator\n"
                    "divcheck - Divisibility Check Program\n"
                    "myip - Returns your Public IP Address\n"
                    "search - Search using Google, Bing or DuckDuckGo\n"
                    "passgen - A simple password generator\n"
                    "tempconvert - Temperature Converter (Between Celsius and Fahrenheit)\n"
                    "hasher - String to MD5, SHA1, SHA256, SHA512 converter\n"
                    "\n"
                    "Other commands:\n"
                    "exit - Exit the program\n"
                    "cls - Clear Screen\n"
                    "help - Commands info and list\n"
                    "pyversion - Returns your Python version\n"
                    "getos - Returns your Operating System info\n"
                    "about - About the program\n")
                # print("\n" + open("help.txt", "r").read() + "\n")
                continue
            # Help command ends here

            case "getos":
                print("Your OS is:", platform.system(), platform.release())
                print("Your OS architecture is:", platform.architecture())
                continue
            case otherwise:
                print("\'" + userMainInput + "\'" " is not a valid command. Type help for a list of commands")
                continue
# End of code
