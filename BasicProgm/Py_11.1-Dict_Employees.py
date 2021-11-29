## Program: Enter 5 Employees - Names and Keys in Dictionary Structure;

import os

try:
    emp = {}
    empId = None
    empName = None
    print("Enter Details of New Employee ...")
    for x in range(0, 2):
        empId = input("Employee ID %d : " % (x + 1))
        empName = input("Employee Name %d: " % (x + 1))
        emp[empId] = empName
        os.system("cls||clear")

    ## Section: Access the empployee details using keys

    print("Search for Employees ...")
    searchId = input("Employee ID: ")
    if searchId in emp:
        print("Employee's Name: %s" % (emp[searchId]))
    else:
        print("Sorry, Employee is not found !")
        print("Exit ...")

except Exception as error:
    print("Exception occured. ", error)