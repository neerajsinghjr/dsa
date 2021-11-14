## Program: Program to Find Factorial of Number Using Recursion
try:
    def fact(number):
        if number == 1:
            return number
        else:
            return (number * fact(number - 1))


    number = int(input("Your Number: "))
    print(fact(number))

except Exception as error:
    print("Exception Occured. ", error)