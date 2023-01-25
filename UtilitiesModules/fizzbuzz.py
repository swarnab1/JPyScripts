def fizzbuzz():
    print(
        "\nThis is the FizzBuzz Test!\n"
        "FizzBuzz is a test that outputs Fizz when divisible by a certain number, Buzz when divisible by another "
        "number and FizzBuzz when divisible by both.\nThis is not the best FizzBuzz test created in Python, "
        "but it does the deed.\nUser has to enter Fizz-Buzz conditions and the number range.\n"
        "Code by: @Joshboi || GitHub: github.com/swarnab1 || swarnab1.github.io\n")

    while True:
        fizz = input("FizzBuzz >>> Fizz (divisor1) = ")
        if fizz == "" or fizz.isdigit() is False:
            print("Enter a valid number")
            continue
        elif fizz == "0":
            print("Can't use Zero as a divisor")
            continue
        else:
            fizz = int(fizz)
        buzz = input("FizzBuzz >>> Buzz (divisor2) = ")
        if buzz == "" or buzz.isdigit() is False:
            print("Enter a valid number")
            continue
        elif buzz == "0":
            print("Can't use Zero as divisor")
            continue
        elif fizz == int(buzz):
            print("Can't use the same number for both divisors")
            continue
        else:
            buzz = int(buzz)
        userRangeInput = input(
            "FizzBuzz >>> Enter your desired range (Outputs FizzBuzz within the range): ")
        if userRangeInput == "" or userRangeInput.isdigit() is False:
            print("Enter a valid number")
            continue
        elif int(userRangeInput) < 2:
            print("Use a value greater than 1")
            continue
        else:
            userRangeInput = int(userRangeInput)

        for i in range(1, userRangeInput + 1):
            if i % fizz == 0 and i % buzz == 0:
                print("FizzBuzz")
                continue
            elif i % buzz == 0:
                print("Buzz")
                continue
            elif i % fizz == 0:
                print("Fizz")
                continue

            print(i)

        print("And that's Fizzbuzz!\nTo rerun, press Enter. To exit, type anything and press Enter.")
        if input("FizzBuzz >>> ") == "":
            continue
        else:
            return
