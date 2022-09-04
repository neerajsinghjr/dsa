## Program: Given Two Sring S1, S2 then make new string by
## adding second string in the mid of first string;

try:
    firstStr = input("First string: ")
    secondStr = input("Second string: ")

    # trimming the strings;
    midFirstString = len(firstStr) // 2

    newString = firstStr[:midFirstString] + " " + secondStr + " " + firstStr[midFirstString:]

    print(newString)

except ValueError:
    print("Exception occured: Insufficient String should be greater than 7 and odd in length")

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")