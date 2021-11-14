## Program: Return middle 3 character of a string of odd length greater ## than 7.

try:
    count = 0
    string = input("Enter String of odd length (Greater than 7 of odd length): ")
    stripString = string.replace(" ", "_")
    strlen = len(string)

    if strlen < 7 and strlen % 2 == 0:
        raise ValueError
    else:
        for x in range(strlen // 2, strlen):
            if count == 3:
                break
            else:
                print("Character:", stripString[x])
                count = count + 1

except ValueError:
    print("Exception occured: Insufficient String should be greater than 7 and odd in length")

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting...")
