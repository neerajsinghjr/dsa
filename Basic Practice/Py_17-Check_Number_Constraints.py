## Program: Print Numbers - 1. Positive 2. Negative 3. Even 4. Odd 5. Zero's - inside list of 5 numbers;

import os

# Check For Positive;
def checkIfPositive(number):
    if number > 0:
        return True
    return False


# Check For Negative;
def checkIfNegative(number):
    if number < 0:
        return True
    return False


# Check For Even;
def checkIfEven(number):
    if number == 0:
        return False
    elif number % 2 == 0:
        return True
    return False


# Check For Odd
def checkIfOdd(number):
    if number % 2 != 0:
        return True
    # return to main;
    return False


# Check if Zero
def checkIfZero(number):
    if number == 0:
        return True
    # returnt to main;
    return False


try:
    number = 0
    myList = []
    # Creating list;
    for x in range(0, 5):
        number = int(input("Enter Value at Index %d: " % (x + 1)))
        myList.append(number)

    os.system("cls || clear")

    # Checking List;
    for number in myList:
        # Check For Positive;
        if checkIfPositive(number):
            print("Positive:", number)
            # Check For Even and Odd;
            if checkIfEven(number):
                print("Even Number:", number)
            else:
                print("Odd Number:", number)
        # Check for Negative;
        elif checkIfNegative(number):
            print("Negative:", number)
        # Check For Zeros;
        elif checkIfZero(number):
            print("Zero:", number)
        else:
            print("Something unexpected occured !")

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")