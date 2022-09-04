# Program: Create empty dictionary and then add multiple elements.
# Program: Add to add key to a dictionary and print all the values

try:
    temp="";
    student={}
    count=int(input("Enter number of student: "))
    for x in range(0, count):
        temp=input("Student Name [%d]: " %(x+1))
        student[x]=temp
    print("Keys: ", student.keys())
    print("Values: ", student.values())
    print("Dictionary: ", student)


except Exception as error:
    print("Exception catch.", error);



# Program: Add dict2 elements into dict1 and print it , use update
dict1 = {1: "one", 2: "three"}
dict2 = {2: "two"}
dict1.update(dict2)
print