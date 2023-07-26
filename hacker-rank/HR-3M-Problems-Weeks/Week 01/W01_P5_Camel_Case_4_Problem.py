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
def split(txt):
    new = txt[0].lower()
    for char in txt[1:]:
        if char.isalpha():
            if char.islower():
                new += char
            else:
                new += " " + char.lower()
    return new


def combine(txt, opr):
    flag = txt[0:1].lower()
    if opr == "M":
        # print("txt:",txt,"flag",flag,"opr",opr)
        new = process(txt,flag, isMethod=True)
        # print("combine:",new)
    elif opr == "V":
        # print("txt:",txt,"flag",flag,"opr",opr)
        new = process(txt,flag)
    elif opr == "C":
        # print("txt:",txt,"flag",flag,"opr",opr)
        flag = flag.upper()
        new = process(txt,flag)
        # print("combine:",new)
    
    return new
    

def process(txt,flag,isMethod=False):
    new, space = flag, False
    for char in txt[1:]:
        if char == " ":
            space = True
            # print("space:",space)
            continue
        elif char.islower():
            if space:   
                # print("if-l-char:",char)
                new += char.upper()
                space = False
            else:
                # print("else-l-char:",char)
                new += char
        elif char.isupper():
            if not space:
                # print("if-u-char:",char)
                new += char.lower()
            else:
                # print("else-u-char:",char)
                new += char
                space = False
        
    if isMethod:
        # Adding Parenthesis for Methods;
        new += "()"
        
    return new
                

def main():
    try:
        strings = [
            "C;V;can of coke",
            "S;M;sweatTea()",
            "S;V;epsonPrinter",
            "C;M;santa claus",
            "C;C;mirror",
            "C;M;mouse pad",
            "S;M;plasticCup()",
            "C;V;mobile phone",
            "C;C;coffee machine",
            "S;C;LargeSoftwareBook",
            "C;M;white sheet of paper",
            "S;V;pictureFrame",
            "S;V;iPad",
            "C;C;code swarm",
            "S;C;OrangeHighlighter",
        ]
        for str in strings:
            if str[0] == "S":
                print(split(str[4:]))
            elif str[0] == "C":
                print(combine(str[4:],str[2:3]))
    
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    