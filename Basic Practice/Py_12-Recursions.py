## Program: Recursion(), Call this func inside itself and break completion of 10 cycle;

try:
    def recursion(number, count):
        if count == 10:
            return number
        else:
            return (number + recursion(number + 1, count + 1))


    number = int(input("Your number: "))
    print(recursion(number, 0))

except Exception as error:
    print("Unhandled exception occurred.", error)
