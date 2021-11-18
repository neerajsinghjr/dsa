# ## String Manipulations
#
# ## Program: Replace all 'a' with 'e' in string;
# str_a = "Train"
# str_b = "Program"
#
# print(str_a.replace('a', 'e'))
# print(str_b.replace('a', 'e'))
#
# ## Program: find length of string "Refrigerator"
# try:
#     string = "Refrigerator"
#     print("Length of %s: %d"  %(string, len(string)))
#
# except Exception as error:
#     print("Error: ", error)
#
#
# ## Question No: 3
#
# ## Program: Print each character of name in new line;
# try:
#     string = input("Your String: ")
#     for x in string:
#         print(x)
#
# except Exception as error:
#     print("Error: ", error)
#
#
# ## Program: Split string from'.' In "Very.Easy.Assignments"
# try:
#     string = 'Very.Easy.Assignments'
#     print(string.split('.'))
#     print(string.split('.', 0))
#     print(string.split('.', 1))
#
# except Exception as error:
#     print("Exception: ", error)
#
#
# ## Program: Print every character in new line of loop
# try:
#     count = 1
#     string = input("Your String: ")
#     for x in string:
#         print("Line %d: %s" % (count, x))
#         count = count + 1
#
# except Exception as error:
#     print("Exception occured.", error)
#
#
# ## Program: Take full name and convert to this pattern, For e.g, R.B.Roser.
# try:
#     first = input("first: ")
#     mid = input("middle: ")
#     last = input("last: ")
#     name = first[0].upper()+"." + mid[0].upper() + "." + last.title()
#     print("Hi, %s" %(name))
#
# except Exception as error:
#     print("Unhandled Exception Occured.", error)
#
#
# ## Program: Generate a string and make a new one by deleting consonants;
# try:
#     newString = ""
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     oldString = input("Your String: ")
#     for x in oldString:
#         if x in vowels or x == " ":
#             newString += x
#         else:
#             continue
#     print(newString)
#
# except Exception as error:
#     print("Unhandled Exception Occured.", error)
#
#
# ## Program: Check if 'orange' is in 'orange juice'
# try:
#     search = 'orange'
#     string = 'orange juice'
#     if search in string:
#         print("Search '%s' is Found in '%s'" % (search, string))
#     else:
#         print("Search '%s' not Found" % (search))
#
# except Exception as error:
#     print("Exception occured.", error)
#
# ## Program: Python program to count the number of characters (character frequency) in a string
# ## Sample String : 'google.com'
# ## Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
#
# try:
#     strDic = {}
#     string = input("Your String: ")
#     for x in string:
#         len = string.count(x)
#         strDic[x] = len
#
#     # Displaying data;
#     print(strDic)
#
# except Exception as error:
#     print("Unhandled Exception.", error)
#
#
# ## Program: Calculate length of a String without using len() function
# try:
#     len = 0
#     string = input("Your String: ")
#     for x in string:
#         len += 1
#     print("Length of %s is %d" %(string, len))
#
# except Exception as error:
#     print("Unhandled Exception.", error)
#
#
# ## Program: Check if a given number is in range , Take Number, And range as input from user
# try:
#     number = int(input("Your Number: "))
#     lower = int(input("Lower Range: "))
#     upper = int(input("Upper Range: "))
#     print("Found, Successfull !") if number in range(lower, upper) else print("Not Found !")
#
# except Exception as error:
#     print("Unhandled Exception.", error)
#
#
# ## Program: String inbuilt 5 functions;
# try:
#     string = input("Your String: ")
#     print("1. Convert To Lowercase: %s" %(string.lower()))
#     print("2. Convert To Uppercase: %s" %(string.upper()))
#     print("3. String Split Func: %s" %(string.split(" ")))
#     print("4. Check if Lowercase: %s" %(string.islower()))
#     print("5. Check if uppercase: %s" %(string.isupper()))
#
# except Exception as error:
#     print("Exception Occured.", error)


# Program: Change the first and last character of the string;
try:
    newString = ""
    string = input("Enter String: ")
    first = input("Enter first Character: ")
    last = input("Enter last Character: ")
    for x in range(0, len(string)):
        if x == 0:
            newString += first
        elif x == len(string) - 1:
            newString += last
        else:
            newString += string[x]

    print("Your String: %s" % newString)

finally:
    print("End Reached!")


## Program: Input from the user and displays that input back in upper and lower cases;

try:
    string = input("Enter String: ")
    print("Uppercase: %s" %(string.upper()))
    print("Lowercase: %s" %(string.lower()))

except Exception as error:
    print("Exception catch !", error)



## Program: Remove the characters which have odd index values of a given string

try:
    strOdd= ""
    string = input("Your String: ")
    for x in range(0, len(string)):
        if x%2 != 0:
            strOdd += string[x]
    print("String Without Odd Index: %s" %(strOdd))

except Exception as error:
    print("Exception catch !", error)
