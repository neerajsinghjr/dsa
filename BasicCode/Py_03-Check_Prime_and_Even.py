## Program: Print 'Yes', if number is prime and even else 'no'
def checkPrime(number):
    if number > 1:
        for x in range(2, number // 2):
            if number % x == 0:
                return False
            else:
                return True
    else:
        return False

def checkEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

try:
    number = int(input("Your number: "))
    if checkPrime(number) and checkEven(number):
        print("Yes it is even and also a prime")
    else:
        print("Result...")
        print("Prime True") if checkPrime(number) else print("Prime False")
        print("Even True") if checkEven(number) else print("Even False")

except ValueError:
    print("Something unexcepected occur ...")

finally:
    print("Thank you !")
