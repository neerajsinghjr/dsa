# Program: Print nth number of fibonacci series;

try:
    first = 0
    second = 1
    number = int(input("Fibonacci Series Starting From 0,1 To Your Limit (Limit greater than 2): "))
    # Raise error for uncertainity;
    if number < 3:
        raise ValueError
    # Default one;
    print(first, "|-->", end=" ")
    print(second, "|-->", end=" ")
    # Making Fibonacci Series;
    for x in range(0, number):
        second = first + second
        first = second - first
        print(second, "|-->", end=" ")

except ValueError:
    print("Exception occured invalid value ...")

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")
