print("#------------------ CODE BEGINS ------------------#")

from enum import Enum
from copy import copy, deepcopy

class TestV1(Enum):
	t20 = 20
	odi = 50
	test = 90

member = TestV1.test
# print(member)
# print(member.name)
# print(member.value)


class TestV2:
	first = 'Neeraj'
	middle = 'Singh'
	last = 'junior'


testMember = TestV2.last
# print(testMember)


def enumFunc():
	# grocery = ['bread', 'milk', 'butter']
	# enumerateGrocery = enumerate(grocery)
	# print(type(enumerateGrocery))

	# # converting to list
	# print(list(enumerateGrocery))

	# # changing the default counter
	# enumerateGrocery = enumerate(grocery, 10)
	# print(list(enumerateGrocery))

	# With Generator;;
	grocery = ['bread', 'milk', 'butter']
	obj = enumerate(grocery)
	print(next(obj))


def square(num):
	if not(num > 0):
		return 0
	return num*num


def positiveSqr(num):
	if not(num > 0):
		return False
	return Trues


def mapping():
	nums = [1,2,3,4,5,0,-10]
	res = map(square, nums)
	res2 = filter(positiveSqr, nums)
	for r in res:
		print(f"map: {r}")
	for r2 in res2:
		print(f"filter: {r2}")


def deepAndShallowCopy(n1):
	n2 = copy(n1)
	n2[2] = 10000

	print(f"n1: {n1}")
	print(f"n2: {n2}")
	print(f"n1: {n1}")

	print(id(n1))
	print(id(n2))

	# initializing list 1
	li1 = n1
	li1 = [1, 2, [3,5], 4]
	  
	# using copy to shallow copy
	li2 = copy(li1)
	  
	# original elements of list
	print ("The original elements before shallow copying")
	for i in range(0,len(li1)):
	    print (li1[i],end=" ")
	  
	print("\r")
	  
	# adding and element to new list
	li2[2][0] = 7
	li2.append(14)
	  
	# checking if change is reflected
	print ("The original elements after shallow copying")
	for i in range(0,len( li1)):
	    print (li1[i],end=" ")

	print('\r')

	for i in range(0,len(li2)):
		print(li2[i], end=" ")

	print('\r')
	print(f"li1: {id(li1)}")
	print(f"li2: {id(li2)}")


def main():
	enumFunc()
	# mapping()
	# deepAndShallowCopy(n1=[1,2,3,4,5,6,7,8,9,10])



if __name__ == "__main__":
	main()

print("#------------------ CODE ENDS ------------------#")