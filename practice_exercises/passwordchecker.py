# password reqs: 8 characters, letters, numbers, $%#@
import re


def checkPassword(password):
    pattern = r"(^[a-zA-Z0-9@#$%]{8,}$)"
    return re.match(pattern, password)


print("Passwords should be 8 characters long, contain numbers and/or letters and/or @, #, $, %")
print("-"*15)
while True:
    password = input("Please enter your password (enter q to quit): ")
    if checkPassword(password):
        print("That password meets the criteria!")
    elif password == "q":
        print("Bye!")
        break
    else:
        print("That password does not meet the criteria, try again.")
