## Program : Print fibonacci series first 20, starting from 0 and 1;

# Main Program Execution;
try:
    count = 2
    first = 0
    second = 1
    # Default one;
    print(first, "|-->", end=" ")
    print(second, "|-->", end=" ")

    # Making Fibonacci Series;
    for x in range(0, 20):
        # Termination of Loop;
        if count == 20:
            break
        count += 1
        second = first + second
        first = second - first
        print(second, "|-->", end=" ")


except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting...")