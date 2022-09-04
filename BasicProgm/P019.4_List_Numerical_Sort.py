## Program: Program to sort a numerical list in Python

try:
    temp = 0
    myList = []
    count = int(input("Enter the number of items to sort: "))
    # Creating List;
    for x in range(0, count):
        temp = int(input("Enter Value at Index %d: " % (x + 1)))
        myList.append(temp)

    # Printing result;
    print("User's List", myList)
    myList.sort()
    print("Sorted List: ", myList)

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")


