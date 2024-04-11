## Program: to convert a list of characters into a string.
try:
    charList = ['a' , 'e', 'i', 'o', 'u']
    print("Character List \n", charList)
    print("Type of Character List \n", type(charList))
    strList = str(charList)
    print("String Character List \n", strList)
    print("Type of String Character List \n", type(strList))

except Exception as error:
    print("Exception catched !")
    print("Error: ", error)

finally:
    print("Thank You!")