## Program: Find the middle three chars of the odd length given string;

try:
    string = input("Enter String of Odd Length: ")
    midStr = "";
    length = len(string)
    # Cross check string length;
    if length%2 != 0 :
        count = 0
        mid = length // 2
        for x in range(mid, length):
            if count != 3:
                midStr += string[x]
            else:
                break
        print("Given String: %s" %(string))
        print("Middle String: %s" %(midStr))
    else:
        print("Sorry, Program require string length of odd length, eg, India")

except Exception as error:
    print("Exception catched ", error)

finally:
    print("Thank You!")
