def divCheck():
    def divide(num1, num2):
        if num2 % num1 == 0:
            print(num2, "is divisible by", num1, "|| Quotient:", int(num2 / num1))
        else:
            print(num2, "is not divisible by", num1, "|| Remainder:", num2 % num1, "|| Float:", num2 / num1)
        return

    print(
        "This program will check if a number is divisible by another number.\nIf yes, it will return the quotient.\nIf not, it will return the remainder and the float value.\nCode by: @Joshboi || GitHub: github.com/swarnab1 || swarnab1.github.io\n")

    while True:
        userInputNum1 = input("Enter divisor: ")
        if userInputNum1 == "" or userInputNum1.isdigit() is False:
            print("Please enter a valid number")
            continue
        elif int(userInputNum1) == 0:
            print("Can't divide by 0")
            continue
        else:
            userInputNum1 = int(userInputNum1)
        userInputNum2 = input("Enter dividend: ")
        if userInputNum2 == "" or userInputNum2.isdigit() is False:
            print("Please enter a valid number")
            continue
        else:
            userInputNum2 = int(userInputNum2)

        divide(userInputNum1, userInputNum2)

        print("To rerun, press Enter. To exit, type anything and press Enter.")
        if input() == "":
            continue
        else:
            return
