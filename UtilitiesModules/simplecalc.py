def simplecalc():
    def add(num1, num2):
        print(num1 + num2)
        return

    def subtract(num1, num2):
        print(num1 - num2)
        return

    def multiply(num1, num2):
        print(num1 * num2)
        return

    def divide(num1, num2):
        roundedResult = round(num1 / num2, 3)
        if roundedResult == 0.0:
            print(num1 / num2)
        elif num1 / num2 == roundedResult:
            print(num1 / num2)
        else:
            print(num1 / num2, "|| Rounded:", roundedResult)
        return

    while True:
        userFunction = input(
            "SimpleCalc >>> type add, sub, mult, div.\nNote: for division, Num1 is the dividend and Num2 is the divisor\nfor subtraction, Num1 is the minuend and Num2 is the subtrahend: ")
        if userFunction == "":
            print("You didn't enter anything")
            continue
        elif userFunction != "add" and userFunction != "sub" and userFunction != "mult" and userFunction != "div":
            print("You didn't enter a valid function")
            continue
        num1 = input("SimpleCalc >>> Enter Num1: ")
        if num1 == "" or num1.isalpha() is True:
            print(
                "Enter a number")
            continue
        else:
            num1 = float(num1)
        num2 = input("SimpleCalc >>> Enter Num2: ")
        if num2 == "" or num2.isalpha() is True:
            print("Enter a number")
            continue
        elif userFunction == "div" and num2 == 0:
            print("You can't divide by 0")
            continue
        else:
            num2 = float(num2)

        if userFunction == "add":
            add(num1, num2)
        elif userFunction == "sub":
            subtract(num1, num2)
        elif userFunction == "mult":
            multiply(num1, num2)
        elif userFunction == "div":
            divide(num1, num2)

        print(
            "Thanks for using my calculator!\nPress enter to continue or type anything to exit")
        if input("SimpleCalc >>> ") == "":
            continue
        else:
            return
