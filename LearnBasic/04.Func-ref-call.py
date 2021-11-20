print("-----------------------------------CODE BEGINS ---------------------------------------")

# # ## Call by Value;
# string = "Neeraj"
# def check(string):
#     print(id(string))
#     string = "Junior"
#     print(id(string))
# print(string)               ## global string;
# print(id(string))
# check(string)
# print(id(string))
# print(string)               ## global string;



# ## Call By References
# names = ["Neeraj", "Singh"]
# def check(fullname):
#     print("before func:",id(fullname))
#     names.append("Junior")
#     print("after func:",id(fullname))
# print(names)
# print(id(names))
# check(names)
# print(names)
# print(id(names))


# ## Checking by call reference by id;
# a = "Neeraj"
# b = "Neeraj"

# # Returns the actual location, where the variable is stored
# print(id(a))
# print(id(b))
 
# # Returns true if both the variables, are stored in same location
# print(a is b)


# ## Call By References
# names = ["Neeraj", "Singh"]
# def check(fullname):
#     print("before func:",id(fullname))
#     names.append("Junior")
#     print("after func:",id(fullname))
#     names[0] = "Adam"
# print(names)
# print(id(names))
# check(names)
# print(names)
# print(id(names))


## Call By References
# data = 7
# def check(data):
#     print("before func:",id(data))
#     data = 9
#     print("after func:",id(data))

# print(data)
# print(id(data))
# check(data)
# print(data)
# print(id(data))

print("-----------------------------------CODE ENDS ---------------------------------------")