def TempConvert():
    print("This program will convert temperatures between Celsius and Fahrenheit.")
    while True:
        userTemp = input("TempConvert >>> Enter the temperature: ")
        if userTemp == "" or userTemp.isalpha() is True:
            print("Enter a valid number")
            continue
        else:
            userTemp = float(userTemp)
        userTempType = input("TempConvert >>> Enter the temperature type (C or F): ")
        if userTempType == "":
            print("Enter a temperature type")
            continue
        elif userTempType.casefold() != "c" and userTempType.casefold() != "f":
            print("Enter a valid temperature type")
            continue
        elif userTempType.casefold() == "c":
            print("Temperature in Fahrenheit:", round(((userTemp * 1.8) + 32), 2))
        elif userTempType.casefold() == "f":
            print("Temperature in Celsius:", round(((userTemp - 32) / 1.8), 2))

        print("To convert another temperature, press Enter. To exit, type anything and press Enter.")
        if input() == "":
            continue
        else:
            return
