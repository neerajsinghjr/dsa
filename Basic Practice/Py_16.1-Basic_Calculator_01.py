## Program: To Perform Addition, Subtraction, Multiply, Divide, Exit;

import os

try:
    # Printing menu board;
    def printMenu():
        print(" ___________________________")
        print("|______ 1. Addition ________|")
        print("|______ 2. Subtraction _____|")
        print("|______ 3. Multiplication___|")
        print("|______ 4. Divide __________|")
        print("|______ 5. Exit ____________|")
        print("|___________________________|")
        choice = int(input("Your Choice: "))
        return choice


    # Calculating output;
    def calculate(first, second, choice):
        if choice == 1:
            return first + second
        elif choice == 2:
            return first - second
        elif choice == 3:
            return first * second
        else:
            if second != 0:
                return first / second
            else:
                return False


    # main program calls;
    choice = printMenu()
    while choice < 6:
        if choice > 0 and choice < 5:
            first = int(input("Your First Number: "))
            second = int(input("Your Second Number: "))
            result = calculate(first, second, choice)
            if result is not False:
                print("Result: %f" % (result))
                choice = input("Continue or Exit (y/n)")
                if choice == 'y' or choice == 'Y' or choice == 'Yes' or choice == "YES":
                    os.system("cls||clear")
                    choice = printMenu()
                else:
                    print("Thank You, Successfully Ends ....")
                    break
            else:
                print("Result is reach Unsuccessfull")
                print("Check your entered input")

        else:
            print("Thank You !")
            break


except Exception as error:
    print("Exception Occured. ", error)