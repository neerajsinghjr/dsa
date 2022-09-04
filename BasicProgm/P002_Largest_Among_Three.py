## Program: Find the largest among three;
try:
    num = 0
    myList = []
    for x in range(0, 3):
        temp = int(input("Enter number: "))
        myList.append(temp)
    print(max(myList))

except ValueError:
    print("Something went wrong ...")
