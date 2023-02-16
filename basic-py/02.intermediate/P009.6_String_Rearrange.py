## Program: Arrange string characters such that lowercase letter comes first then any other characters;

try:
    string = input("Enter Your String:  ")
    printThemFirst = ""
    printThemLater = ""

    # Filter out the string;
    for x in string:
        if x.islower():
            printThemFirst = printThemFirst + x
        else:
            printThemLater = printThemLater + x

    # Formatting Output
    print("Lowercase: ", printThemFirst)
    print("Other: ", printThemLater)

except ValueError:
    print("Exception occured: Insufficient String should be greater than 7 and odd in length")

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")