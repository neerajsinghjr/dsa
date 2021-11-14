## Program: Merge two list using + operator;

try:
    even = []
    odd = []
    list = []
    for x in range(0, 20):
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    list = even + odd

    print("Even: ", even)
    print("Odd: ", odd)
    print("List: ", list)

except Exception as error:
    print("Exception Occured. ", error)


## Program: List of rainbow colours, remove 1, 3, last;

try:
    temp = 0
    name = "RAINBOW"
    rainbow = {}
    print("RAINBOW Colours List ...")
    for x in name:
        temp = input("%s means: " % (x))
        rainbow[x] = temp
        # rainbow.append(temp)

    # Display full;
    print(rainbow)
    # Deleting Elements;
    rainbow.pop('R')
    rainbow.pop('A')
    rainbow.pop('W')
    print(rainbow)

except Exception as error:
    print("Exception Occured. ", error)


# Program: Insert given string X into 2nd position in list Y
list = [10 ,20 ,30 ,50]
print("Before Insertion: ", list)
list.insert(2, 10000)
print("After Insertion: ", list)


## Program: To get the largest number from a list.
try:
    temp = 0
    myList = []
    items = int(input("How many items are there: "))
    for x in range(0, items):
        temp = input("List [%d]: " %(x+1))
        myList.append(temp)
    print("Max Element: %s" %(max(myList)))

except Exception as error:
    print("Exception catched !")
    print("Error: ", error)

finally:
    print("Thank You!")


## Program: to multiplies all the items in a list.
try:
    list = [12, 13, 15, 16, 20]
    newList = list * 2
    print("Original List: ", list)
    print("Mulitiplied List: ", newList)

except Exception as error:
    print("Exception catched !")
    print("Error: ", error)

finally:
    print("Thank You!")


## Program: to remove duplicates from a list.
try:
    duplicatedList = [12, 13, 15, 16, 20, 12, 13, 15, 16, 20]
    print("Original Duplicated List ... \n", duplicatedList)
    # Remove duplicacy;
    filteredSet = set(duplicatedList)
    # Converting to list;
    filteredList = list(filteredSet)
    print("Filter List ... \n ", filteredList)

except Exception as error:
    print("Exception catched !")
    print("Error: ", error)

finally:
    print("Thank You!")