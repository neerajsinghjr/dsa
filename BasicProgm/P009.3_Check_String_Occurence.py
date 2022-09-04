## Program: Inspect all occurrences of "USA" in given string;
try:
    string = input("Your String: ").lower()
    list = ["u", "s", "a"]
    print("Given String: %s" %(string))
    for x in list:
        print("Length of %c: %d" %(x, string.count(x)))

except Exception as error:
    print("Exception catched ", error)

finally:
    print("Thank You!")