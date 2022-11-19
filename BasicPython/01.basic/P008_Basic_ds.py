print("-----------------------------------CODE BEGINS -------------------------------------")

name = "neeraj"
print(f"my name is {name}")
name += " singh"
print(f"my name is {name}")

## fString are in v3.6
# first = "neeraj"
# second = "singh"
# last = "junior"

# print(f"name: {first} {second} {last}")
# print("{} {} {}".format(first,second,last))
# print("{2} {0} {1}".format(first,second,last))


nums = [12,12313453,45,3,53,654,675673,52,515345,365,456]
"""
insert(index, value) ~ take value for index;
pop(index:optional)  ~ remove index value or remove last
remove(value) ~ remove value;
append(value) ~ append at last
list([1,2,3]) ~ constructor method;
nums = []     ~ popular
"""
# print(nums)
# nums.insert(5,9876)
# print(nums)
# sortedNums = sorted(nums,reverse=True)
# print(sortedNums)
# nums.sort(reverse=True)
# print(nums)
# nums.append(9999)
# print(nums)
# popped = nums.pop(5)              # ~index;
# print(popped)             
# print(nums)
# print(nums.remove(52))            # ~value; 
# print(nums)


"""
can't add or delete values from tuple
tuple()
tup = (x,)      ## comma need to considered as tuple otherwise type x
"""
# nums = (1,4,5,2,3,5,6,7)
# del nums[9]         ## error: single deletion doesnt support
# del nums            ## delete as a whole list;
# print(nums if nums else print("None"))

# print(nums,"type:",type(nums))
# nums[1] = 10            # ~ assignment not possible

# case 1:
# data1 = 1
# print(type(data1),":",data1)          ## type: int
# data2 = 2,
# print(type(data2),":",data2)          ## type: tuple
# data3 = (3)
# print(type(data3),":",data3)          ## type: int
# data4 = (4,)
# print(type(data4),":",data4)          ## type: tuple


"""
set contains uniques list but unordered;
add(value) ~ add 'value' to set;
pop() ~ takes no arguments
remove(value) ~ value to delete
"""
# nums = {9,1,2,6,42,7,65,4}
# nums.add(99)
# print(nums)
# nums.add(98)
# print(nums)
# nums.add(98)
# print(nums)

# nums.remove(98)
# print(nums)
# popped = nums.pop()
# print(nums, "popped:",popped)
# popped = nums.pop()
# print(nums, "popped:",popped)
# popped = nums.pop()
# print(nums, "popped:",popped)
# popped = nums.pop()
# print(nums, "popped:",popped)

"""
dict() ~ construct
dict = {}   ~ using, keywords
"""
# data = [
#     {
#         "id": 1,
#         "first":"neeraj",
#         "middle": "singh",
#         "last": "junior",
#     }, {
#         "id": 2,
#         "first":"rohit",
#         "middle": "singh",
#         "last": "junior"
#     }
# ]

# print(type(data))

## --- check codes
# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# k = int(first_multiple_input[1])
# ar = list(map(int, input().rstrip().split()))
# result = divisibleSumPairs(n, k, ar)
# fptr.write(str(result) + '\n')
# fptr.close()



print("-----------------------------------CODE ENDS ---------------------------------------")
