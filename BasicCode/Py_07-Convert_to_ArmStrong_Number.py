## Program: To check when the given number is an Armstrong;
def convertToArmstrong(number):
    myList = []
    temp = number
    # Breaking the digits;
    while temp != 0:
        rem = temp % 10
        myList.append(rem)
        temp = temp // 10
    # Check sum of cubes;
    for x in myList:
        temp += x ** 3
    return temp


# Check If Armstrong is there ...
def checkIfArmstrong(number):
    convertedNumber = convertToArmstrong(number)
    if number == convertedNumber:
        return True
    # return to main
    return False


# Main Program Execution;
try:
    number = int(input("Your number: "))
    if checkIfArmstrong(number):
        print("Armstrong Test Successfull...")
    else:
        print("Armstring Test Un-Successfull")

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting")
