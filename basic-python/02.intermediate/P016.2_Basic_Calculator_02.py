## Program: sum all the numbers in a list of 10 elements input by the user;

try:
    sum = 0
    temp = 0
    list = []
    for x in range(0, 10):
        temp = int(input("Your Number %d: " % (x + 1)))
        list.append(temp)
        sum += temp
    print("Your List: ", list)
    print("Sum: ", sum)

except Exception as error:
    print("Exception Occured. ", error)

