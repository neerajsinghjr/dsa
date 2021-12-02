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
def splitString(s, t):    
    # split at upper case, convert to lower case and sep by blank:
    s = ''.join(' '+c.lower() if c.isupper() else c for c in s)
    # special treatment of classes and methods:
    if t=='C':
        s= s.capitalize().strip()
    elif t=='M':
        s = s[:-2]
        
    return s
    
    
def combineString(s, t):    
        if t=='C':
            s = ''.join(x.capitalize() for x in s)             
        elif t=='M':                        
            s = s[0] + ''.join(x.capitalize() for x in s[1:]) 
            s = s + '()'             
        elif t=='V':            
            s= s[0] + ''.join(x.capitalize() for x in s[1:]) 
            
        return s

        
def processCase(arr):
    if arr[0]=='S':        
        s = splitString(arr[-1],arr[1])    
        print(s)

    elif arr[0]=='C':        
        # split by blank:
        s = arr[-1].split(' ')
        # process
        s = combineString(s,arr[1])            
        print(s)
    

def main():
    strings = [
        "S;M;plasticCup()",
        "C;V;mobile phone",
        "C;C;coffee machine",
        "S;C;LargeSoftwareBook",
        "C;M;white sheet of paper",
        "S;V;pictureFrame"
    ]
    for str in strings:
        arr = str.rstrip().split(';')
        processCase(arr)
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    