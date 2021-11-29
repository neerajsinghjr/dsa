# Program: Search for a given number inside a list of 10 numbers;
import os

try:
    number = 0
    myList = []

    # Creating list;
    for x in range(0, 10):
        number = int(input("Enter Value at Index %d: " % (x + 1)))
        myList.append(number)

    os.system("cls || clear")

    # Searching in list;
    number = int(input("Search for anything: "))
    count = myList.count(number)

    # Printing Result;
    print("Search Success") if count != 0 else print("Search Failed !");

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")

