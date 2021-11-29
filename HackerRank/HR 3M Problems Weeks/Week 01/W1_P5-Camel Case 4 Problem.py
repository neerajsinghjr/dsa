'''
Problem:
Camel Case is a naming style common in many programming languages. 
In Java, method and variable names typically start with a lowercase letter,
with all subsequent words starting with a capital letter (example: startThread). 
Names of classes follow the same pattern, except that they start with a capital letter 
(example: BlueCar).

Your task is to write a program that creates or splits Camel Case variable, method, and class names.

Input Format
1) Each line of the input file will begin with an operation (S or C) followed by a semi-colon 
followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
2) The operation will either be S (split) or C (combine)
3) M indicates method, C indicates class, and V indicates variable
4) In the case of a split operation, the words will be a camel case method, class or variable 
name that you need to split into a space-delimited list of words starting with a lowercase letter.
5) In the case of a combine operation, the words will be a space-delimited list of words starting 
with lowercase letters that you need to combine into the appropriate camel case String. 
Methods should end with an empty set of parentheses to differentiate them from variable names.

Sample Input
    S;M;plasticCup()
    C;V;mobile phone
    C;C;coffee machine
    S;C;LargeSoftwareBook
    C;M;white sheet of paper
    S;V;pictureFrame

Sample Output
    plastic cup
    mobilePhone
    CoffeeMachine
    large software book
    whiteSheetOfPaper()
    picture frame
'''

#!/bin/python3


import math
import os
import random
import re
import sys

## Main Working Function
def getCaseString(opr, key, main):
    if opr == "S":                                  ## Split;
        if key == "V":
            
        if (key == "C"):
            pass
        if(key == "M"):
            pass
    else:                                           ## Combine;
        pass  
def getCaseString(s):
    while True:
        try:
            s = input().rstrip()    
            sc, mcv, op = s.split(";")
            if sc == "S":
                if mcv == "M":
                    cap = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', op[:-2])
                    ans = " ".join(m.group(0).lower() for m in cap)
                    print(ans.rstrip())
                    
                if mcv == "C":
                    cap = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', op)
                    ans = " ".join(i.lower() for i in cap)
                    print(ans.rstrip())
                    
                if mcv == "V":
                    cap = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', op)
                    ans = " ".join(m.group(0).lower() for m in cap)
                    print(ans.rstrip())
                    
            if sc == "C":
                if mcv == "M":
                    lst = op.split(" ")
                    res = []
                    for i in range(len(lst)):
                        if i == 0:
                            res.append(lst[i].lower())
                        else:
                            res.append(lst[i].capitalize())
                    ans = "".join(i for i in res)
                    ans = ans.rstrip() + "()"
                    print(ans.rstrip())
                if mcv == "C":
                    lst = op.split(" ")
                    ans = "".join(i.capitalize() for i in lst)
                    print(ans.rstrip())
                if mcv == "V":
                    lst = op.split(" ")
                    res = []
                    for i in range(len(lst)):
                        if i == 0:
                            res.append(lst[i].lower())
                        else:
                            res.append(lst[i].capitalize())
                    ans = "".join(i for i in res)
                    print(ans.rstrip())
            
        except EOFError:
            break


def getCamelCase(strings):
    newStr = None
    result = []
    for str in strings:
        getCamelCase(str)
    #     opr, key, main = str.split(";")
    #     newStr = getCaseString(opr,key,main)
    #     print(str,"=>",newStr)
    #     result.append(newStr)
    # return result


def main():
    strings = [
        "S;M;plasticCup()",
        "C;V;mobile phone",
        "C;C;coffee machine",
        "S;C;LargeSoftwareBook",
        "C;M;white sheet of paper",
        "S;V;pictureFrame"
    ]
    res = getCamelCase(strings)
    print(res) if res else print("Empty!")
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    