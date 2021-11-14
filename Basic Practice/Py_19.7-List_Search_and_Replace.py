## Program: Find value 20 inside a list and replace it with 200 but the first occurrence only.

import os

try:
    temp = 0
    numberList = []
    size = int(input("Enter the number of elements for List: "))

    # List creation;
    for x in range(0, size):
        temp = int(input("List Iteration %d: " %(x+1)))
        numberList.append(temp)

    os.system("clear || cls")

    find = int(input("Number For Search: "))
    findIndex = numberList.index(find)

    # checking if find there to replace;
    if find not in numberList:
        print(find, " Not Found !")
    else:
        numberList[findIndex] = 200
        print(numberList)

except Exception as error:
    print("Exception traced.", error)

else:
     print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")

