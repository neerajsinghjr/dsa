##--- Zip function;
l1 = [1, 2, 3, 4, ]
l2 = [11, 12, 13, 14, 15]

for x in zip(l1, l2):
    print(x, "First Value = ", x[0], "Second Value: ", x[1], end="\n")


#--- List comprehension;
l1= [1,2,3,4,5,6]
result = []

result.append(x**2 for x in l1 if x % 2 == 0)
print(result, end=" ")

##--- Formatting
x = 34
print ("decimal number : %2d " % (x))
print ("decimal number : %2d " % (712121212))
print ("Float number : %5.2f" % ( 209090909093.11111111))

##--- Docstring
"""
Doc string should be first line after defining in class, method, module
can be accessed using __doc__ like classname.__doc__ etc
"""

class Jungle:
    """
    Jungle is class which needs animals
    -- King of the jungle, Lion;
    """

    name = ''
    type = ''

    def __init__(self):
        print("executed...")



def func1():
    """
    Multi line comment
    by docstring
    """
    print("Hello, func1", end="\n")


print(func1.__doc__)
j1 = Jungle
print(j1.__doc__)

# Data types
num = 9
complex = num
a = [1,2,3,4,5,6]

print(list[::-1])
print(a.reverse())
#create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

#reverse the order of list elements
prime_numbers.reverse()

print(help(list))

ls  = ["apple", "a", 100, 20.78]
print(dict().__doc__)
"".title()

dick = {
    'a': ['b','c','d'],
    'aa' : ['sd','sd','sd','sd']
}

for key, value in dick.items():
    print("Key: ", key, "value: ", value)


print('Reversed List:', prime_numbers)

#Output: Reversed List: [7, 5, 3, 2]