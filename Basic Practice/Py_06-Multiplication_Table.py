## Program: Multiplication Table;
try:
    number = int(input("Your number: "))
    for x in range(1, 11):
        print("%d x %d = %d"%(number, x, number*x))

except Exception as error:
    print("Something went wrong. ", error)