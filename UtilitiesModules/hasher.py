# Broken code
import hashlib


def hasher():

    print("\nThis program will convert a string to a hash.")

    while True:
        hashMain = input("HashER >>> Enter your string to convert to hash: ")

        if hashMain != "":

            while True:
                encodingMethod = input("HashER >>> Enter encoding method (md5, sha1, sha256, sha512): ")
                match encodingMethod.casefold():
                    case "md5":
                        print(encodingMethod.upper() + " hash is " + (hashlib.md5(hashMain.encode())).hexdigest())
                    case "sha1":
                        print(encodingMethod.upper() + " hash is " + (hashlib.sha1(hashMain.encode())).hexdigest())
                    case "sha256":
                        print(encodingMethod.upper() + " hash is " + (hashlib.sha256(hashMain.encode())).hexdigest())
                    case "sha512":
                        print(encodingMethod.upper() + " hash is " + (hashlib.sha512(hashMain.encode())).hexdigest())
                    case _:
                        print("Enter a valid method")
                        continue

                print("To generate another hash, press Enter. To exit, type anything and press Enter.")
                if input("HashER >>> ") == "":
                    break
                else:
                    return
        else:
            print("Enter a string")
            continue
