import os
import mysql.connector

def init():
    try:
        # Setting the Database;
        connection = mysql.connector.connect(
            host='localhost',
            database='python',
            user='root',
            password='fuckingInsane@9'
        )

        # Connection;
        if connection.is_connected():
            return connection

    except Exception as e:
        print("Error while connecting to MySQL", e)
        return False


##--- Main Execution ---##
print(" ---------------------")
print("|DATABASE Connectivity|")
print(" ---------------------")

flag = True
# DB Checkpoint;
connection = init()
if connection != False:

    while (flag):
        value = input("Please Enter a Package Name: ")
        cursor = connection.cursor()
        sql = "SELECT package_name, package_version FROM packages WHERE package_name = %s"
        val = (value,)
        cursor.execute(sql, val)
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record[0] ," : ", record[1])
        else:
            print("Sorry no records found ")

        flag = input("Want to continue further (yes/no): ")
        if flag in ["yes", "Yes", "YES", "y", "Y"]:
            flag = True
            os.system("clear")
        else:
            flag = False
            os.system("clear")
            print("Thank you \nby Neeraj")

else:
    print("Sorry, Exception Occured from Database")



    

