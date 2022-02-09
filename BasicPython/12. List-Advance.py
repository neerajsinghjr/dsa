print("-----------------------------------CODE BEGINS ---------------------------------------")

arr1 = [10,12,31,22,34,66,67,88,22,10,33,45]
arr2 = [100,200,300,400,500,600,700,800]

# print(arr1[:, 0])
# print(f"arr1: {arr1}, len: {len(arr1)}")
# arr1[:] = arr2

# print(f"arr1[:]: {arr1}, len: {len(arr1)}")

a = [0]      
b = a                   # a and b pointing to the same location;
print("b", b)   
a[:] = [1]              # changes the a 
print("b", b)
print("a", a)
a = [2]      
print("b", b)
print("a", a)


print("-----------------------------------CODE ENDS ---------------------------------------")