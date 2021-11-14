## Program: To Print even length words in the string;

try:
    string = input("Enter String To Find Even Length Word: ")
    strList = string.split(" ")

    # Printing Even Words
    for str in strList:
        strLength = len(str)
        if strLength % 2 == 0:
            print("String Word: '%s' || Length: %d" %(str, strLength))

except ValueError:
    print("Exception occured invalid value ...")

except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")
