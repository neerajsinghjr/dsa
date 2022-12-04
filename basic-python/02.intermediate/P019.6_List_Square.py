# Program: Make a square list from a existing numerical list.
try:
    numberList = []
    squareList = []
    square = lambda x: x ** 2
    count = int(input("Enter the number of elements inside the list: "))

    # Makeing numerical list;
    for x in range(0, count):
        temp = int(input("Element at index %d " % (x + 1)))
        numberList.append(temp)
        temp = square(temp)
        squareList.append(temp)

    # Makeing Square List;
    print("Number List: ", numberList)
    print("Sqaure List: ", squareList)

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")