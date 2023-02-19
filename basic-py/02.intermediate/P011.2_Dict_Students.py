## Program: Generate a Dictionary to hold student roll with subjects.
import os

try:
    student = {}
    subjects = []
    roll = None
    temp = None
    print("Welcome to Student Maintenance System ...")
    for x in range(0, 2):
        tempList = []
        roll = input("Student %d Roll No: " %(x+1))
        count = int(input("Total No Of Subjects: "))
        for y in range(0, count):
            temp = input("Subject %d: " %(y+1))
            tempList.append(temp)
        subjects.append(tempList)
        student[roll] = subjects[x]
        subjects.clear()
        os.system("cls||clear")
    #Display Data;
    print(student)

except Exception as error:
    print("Unhandled Exception occured.", error)