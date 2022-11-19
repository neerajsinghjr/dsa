'''
-------------------------------------------------------------------------------------
-> Title: PyNotes Diary
-> Author: Neeraj Singh Jr.
-> Status: Ongoing...
-> Created: 03.09.2022
-> Updated: 09.10.2022
-> Summary: Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Question 040 : Hashing vs Encryption;
-> Question 039 : Asyncio Module in Python;;
-> Question 038 : Arrays in Python;;
-> Question 037 : Method Overloading and Operator Overloading;;
-> Question 036 : Switch alternative in python;;
**** Question 035 : Disassember Package using DIS package;;
**** Question 034 : Access Python Source Code and Byte Code ;;
-> Question 033 : ABCMeta, AbstractClass, abstractmethod in ABC package;;
-> Question 032 : Variable arguments *args and **vargs in python;;
-> Question 031 : Finding and Installing Packages;;
**** Question 030 : Default Dict in Python;;
-> Question 029 : Explicit string type at definition of literals;;
-> Question 028 : Builtins Error and Exception;;
-> Question 027 : Mutable and Immutable data types;;
-> Question 026 : Explicit string type at definition of literals;;
-> Question 025 : Python first class objects;;
-> Question 024 : Python main() function;;
-> Question 023 : Identify bugs and performing static analysis in python;;
-> Question 022 : Global Interpreter Lock;;
-> Question 021 : Lambda function in Python;;
-> Question 020 : Module vs Packages in Python;;
-> Question 019 : Inheritance in Python;;t
-> Question 018 : Access Specifiers used in python;;
-> Question 017 : Access Parent Class using Child class;;
-> Question 016 : Python Pickling vs UnPickling;;
-> Question 015 : Class Compositon Vs Inheritance;;
**** Question 014 : Class Composition in Python;;
-> Question 013 : @classmethod() vs @staticmethod();;
-> Question 012 : Magic Method __str__() vs __repr__();;
-> Question 011 : Set Variable LowerBound and UpperBound;;
-> Question 010 : Create a Generator Class;;
-> Question 009 : Iterators Vs Iterables Vs Generators in python;;
-> Question 008 : Iterators in python;;
-> Question 007 : Generators in python;;
-> Question 006 : Type Hinting;;
-> Question 005 : Copy in python;;
-> Question 004 : Python arrays;;
-> Question 003 : LAMBDA in python;;
-> Question 002 : Comprehension in python;;
-> Question 001 : Decorators in python;;
-------------------------------------------------------------------------------------
'''

-------------------------------------------------------------------------------------
-> Question 040 : Encryption vs Hashing

ENCYRPTION : 

    - Encryption is a two-way function where data is passed in as plaintext and
      comes out as ciphertext, which is unreadable but the data can be decrypted
      so it is readable again
    - Encryption comes in two types: Asymmetric and Symmetric. 

        a) Asymmetric Encryption

            Encryption : Asymmetric encryption uses two different keys, a public
            and private key, for encryption and decryption. The private key is
            used to encrypt data, and is kept a secret from everyone but the
            person encrypting the data. The public key is available for anyone,
            and is used for decryption. Using asymmetric encryption, the
            authenticity of the data can be verified, because if the data was
            modified in transit, it would not be able to be re-encrypted with
            the private key

            Asymmetric Encryption Algorithms:

                1) Elliptic Curve Digital Signature Algorithm (ECDSA)
                2) Rivest-Shamir-Adleman (RSA)
                3) Diffie-Hellman
                4) Pretty Good Privacy (PGP)

        b) Symmetric Encryption : 
            
            Symmetric encryption uses the same key for both encryption and
            decryption. This type of encryption uses less processing power
            and is faster, but is less secure as only one key is used

            Symmetric Encryption Algorithms:

                1) Advanced Encryption Standard (AES)
                2) Blowfish
                3) Twofish
                4) Rivest Cipher (RC4)
                5) Data Encryption Standard (DES)

HASHING  :

    - Hashing, on the other hand, is one-way, meaning the plaintext is scrambled
      into a unique digest, through the use of a salt, that cannot be decrypted.

    -  Hashing Algorithms:

        1) Message Digest Algorithm (MD5)
        2) Secure Hashing Algorithm (SHA-1, SHA-2, SHA-3)
        3) WHIRLPOOL
        4) TIGER
        5) Cyclical Reduction Check (CRC32)

HASHING USE CASES :-

1)  One of the uses for hashing is to compare large amounts of data. Hash
values are much easier to compare than large chunks of data, as they are more
concise.

2) Hashing is also used for mapping data, as finding values using hashes is
quick, and good hashes do not overlap.

3) Hashes are used in digital signatures and to create random strings to avoid
duplication of data in databases too.

4) hashing is extremely infeasible to reverse, hashing algorithms are used on
passwords. This makes the password shorter and undiscoverable by attackers.

ENCRYPTION USE CASES :-

1)  Encryption tends to be used for encrypting data that is in transit. Data
being transmitted is data that needs to be read by the recipient only, thus
it must be sent so that an attacker cannot read it.

2) Encryption hides the data from anyone taking it in the middle of transit,
and allows only the decryption key owner to read the data

3) Encryption would be used over hashing is for storing and retrieving data in
databases, authentication methods, and other cases where data must be hidden
at rest, but retrieved later.


-------------------------------------------------------------------------------------
-> Question 039: Asyncio Module in Python;;

# Thread syncrhonization;

# 




-------------------------------------------------------------------------------------
-> Question 038: Arrays in Python;;

// Syntax of array module :-
arrayIdentifierName = array(typecode, [Initializers])

for eg, 
from array import Array

arr = array(paramter type, initialize values)
print(arr)

// Array Parameters Details :-
c : character of size 1 byte
u : unicode character of size 2 bytes
w : unicode character of size 4 bytes

b : signed integer of 1 byte
B : unsigned integer of 1 byte
h : signed integer of 2 bytes
H : unsigned integer of 2 bytes
i : signed integer of 2 bytes
I : unsigned integer of 2 bytes
l : signed integer of 4 bytes
L : unsigned integer of 4 bytes

f : floating point of 4 bytes
d : floating point of 8 bytes


for eg, // Array CRUD

from array import *

arr = array(i, [1,2,3])

// append values to array
arr.append(4)       # [1,2,3,4]

print(arr)

// print array
for i in arr:
    print(i)

// insert values at array
arr.insert(4,99)

// extends from list
c = [11,12,13]
arr.extends(c)
print(arr)

// more helpers...
arr.fromlist(opts=[11,22,33])
arr.count(3)
arr.tostring()              # convert to string
arr.tolist()                # convert to list


-------------------------------------------------------------------------------------
-> Question 037: Method Overloading and Operator Overloading;;




-------------------------------------------------------------------------------------
-> Question 036: Switch alternative in python;;

for eg,

# Case 1: Switch case using if-else;
def switch(value):
	if(value == 1):	return value*10
	elif(value == 2): return value*20
	elif(value == 3): return value*30
	else: return value

print(switch(value=3))	# switch function in python

# Case 2: Switch using dict;
switch = {
	1: lambda: 1*10,
	2: lambda: 2*20,
	3: lambda: 3*30,
	
	
}


-------------------------------------------------------------------------------------
-> Question 035: Disassember Package using DIS package;;




-------------------------------------------------------------------------------------
-> Question 034: Access Python Source Code and Byte Code ;;



-------------------------------------------------------------------------------------
-> Question 033: ABCMeta, AbstractClass, abstractmethod in ABC package;;

# BASIC USAGE OF ABSTRACT CLASS:-
Abstract classes are classes that are meant to be inherited but avoid 
implementing specific methods, leaving behind only method signatures that 
subclasses must implement.

Abstract classes are useful for defining and enforcing class abstractions 
at a high level, similar to the concept of interfaces in typed languages, 
without the need for method implementation.

One conceptual approach to defining an abstract class is to stub out the 
class methods, and then raise a NotImplementedError if accessed. This 
prevents children classes from accessing parent methods without overriding
them first. 

for eg, 

class Fruit:
    def check_ripeness(self):
        raise NotImplementedError("method not implemented!")

class Apple(Fruit):
    pass

a = Apple()
a.check_ripeness() # raises NotImplementedError


# ABSTRACT CLASS PACKAGE :-
Abstract base classes (ABCs) enforce what derived classes implement particular 
methods from the base class.

To understand how this works and why we should use it, let's take a look at 
an example that Van Rossum would enjoy. Let's say we have a Base class 
"MontyPython"with two methods (joke & punchline) that must be implemented by 
all derived classes.

for eg,
class MontyPython:
    def joke(self):
        raise NotImplementedError()

    def punchline(self):
        raise NotImplementedError()

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"
        
When we instantiate an object and call it's two methods, we'll get an error
(as expected) with the punchline() method.

 >>> sketch = ArgumentClinic() 
 >>> sketch.punchline() 
 >>> NotImplementedError 

However, this still allows us to instantiate an object of the ArgumentClinic 
class without getting an error. In fact we don't get an error until we look 
for the punchline().

This is avoided by using the Abstract Base Class (ABC) module. Let's see how
this works with the same example:

for eg,

from abc import ABCMeta, abstractmethod

class MontyPython(metaclass=ABCMeta):
    @abstractmethod
    def joke(self):
        pass

@abstractmethod
def punchline(self):
    pass

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"
        
This time when we try to instantiate an object from the incomplete class, we 
immediately get a TypeError!

>>> c = ArgumentClinic()
>>> TypeError: "Can't instantiate abstract class ArgumentClinic with abstract 
methods punchline"

In this case, it's easy to complete the class to avoid any TypeErrors:

for eg,
class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"

    def punchline(self):
        return "Send in the constable!"


-------------------------------------------------------------------------------------
-> Question 032: *args and **vargs in python;;

- args  : received tuple
- kargs : recieved dictionary 

# Usage 1:
The names args and kwargs are used by convention, they are not a part of the 
language specification. Thus, these are equivalent:

for eg, They both are same...

def func(*args, **kwargs):	# example 1
	print(args)
	print(kwargs)
	
def func(*a, **b):			# example 2
	print(a)
	print(b)


# Usage 2:-
You may not have more than one args or more than one kwargs parameters 
(however they are not required)

def func(*args1, *args2): #  example 1
	# File "<stdin>", line 1
	# def test(*args1, *args2):
	
	# SyntaxError: invalid syntax


def test(**kwargs1, **kwargs2):	# example 2
	# File "<stdin>", line 1
	# def test(**kwargs1, **kwargs2):
	
	# SyntaxError: invalid syntax


# Usage 3: 
If any positional argument follow *args , they are keyword-only arguments
that can only be passed by name. A single star may be used instead of 
*args to force values to be keyword arguments without providing a variadic
parameter list. Keyword-only parameter lists are only available in Pytohn3


def func(a, b, *args, x, y):	# Example 1
	print(a, b, args, x, y)
	
func(1, 2, 3, 4, x=5, y=6)
>>> Error : Missing param x,y

def func(a,b, *args, x, y):
	print(a, b, var, b, y)
	
func(1,2,3,4,6,x=8,y=9)


# Usage 4:
Keyworded argument should be at last of the function defination.

def func(**kwargs, *args):
# File "<stdin>", line 1
# def test(**kwargs, *args):
#
# SyntaxError: invalid syntax
	
	
### args when calling for function;

args uses tuple for sending and receiving the value;

when you are using *args for sending param value to a func() param
then argument gonna unpack while calling the method and the func()
recieved individual argument.

for eg,

def func(x,y):
	print(x,y)
	
a = [1,2]
func(*a)		# x = 1, y = 2 unpack a into two variables;

a.append(3)
func(*a)		# error func() expects two agrument but 3 were given;

### kwargs using in function;

Work approach is same as in the args but kwargs received key:value
pair instead of tuple as in args;

for eg,

def func(x,y):
	print(f"x: {x} // y:{y}")

x = {'a': 10, 'b': 20}
func(**x)


Note that the length of the starred argument need to be equal to the 
number of the function's arguments.

A common python idiom is to use the unpacking operator * with the zip 
function to reverse its effects.


-------------------------------------------------------------------------------------
-> Question 031: Finding and Installing Packages;

For indirect calling for the pip module if the pip module is not defined as 
inside the environment variable;

$ python -m pip install 

NOTE: for directly using pip, you need to defined it inside the environment
variable like you have done while install python;

$ pip search <query>
$ pip install <query>
$ pip uniinstall <query>
$ pip install [package_name]==x.x.x # specific version of the package
$ pip install '[package_name]>=x.x.x' # minimum version of the package

$ pip list --outdated # list outdated package;

$ pip install <package> --upgrade # Upgrading the installed packges;;

$ pip install -U pip	# upgrading pip module;;

-------------------------------------------------------------------------------------
-> Question 030: Deafult Dict in Python;;

A defaultdict is a dictionary with a default value for keys, so that keys for
which no value has been explicitly defined can be accessed without errors.
defaultdict is especially useful when the values in the dictionary are
collections (lists, dicts, etc) in the sense that it does not need to be
initialized every time when a new key is used.

A defaultdict will never raise a KeyError. Any key that does not exist gets
the default value returned.

for eg, 

from collection import defaultdict

list = [1,2,3]


-------------------------------------------------------------------------------------
-> Question 028: Builtins Error and Exception;;

Built in modules contains extra functionalities.For example to get square root
of a number we need to include math module.

>>> import math
>>> math.sqrt(16) # 4.0

To know all the functions in a module we can assign the functions list to a
variable, and then print the variable.

>>> import math
>>> dir(math)

['__doc__', '__name__', '__package__', 'acos', 'acosh',
'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign',
'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1',
'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma',
'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10',
'log1p', 'modf', 'pi', 'pow'

>>> dir(__builtins__)
[
    'ArithmeticError',
    'AssertionError',
    'AttributeError',
    'BaseException',
    'BufferError',
    'BytesWarning',
    'DeprecationWarning',
    'EOFError',
    'Ellipsis',
    'EnvironmentError',
    'Exception',
    'False',
    'FloatingPointError',
    'FutureWarning',
    'GeneratorExit',
    'IOError',
    'ImportError',
    'ImportWarning',
    'IndentationError',
    'IndexError',
    'KeyError',
    'KeyboardInterrupt',
    'LookupError',
    'MemoryError',
    'NameError',
    'None',
    'NotImplemented',
    'NotImplementedError',

    ...
]

-------------------------------------------------------------------------------------
-> Question 027: Mutable and Immutable data types;;

# Immutable:
int , long , float , complex
str
bytes
tuple
frozenset

# Mutable
list
set
dict
bytearray

-------------------------------------------------------------------------------------
-> Question 026: Explicit string type at definition of literals;;

With one letter labels just in front of the quotes you can tell what type of
string you want to define.

- b'foo bar' : results : bytes in Python 3, str in Python 2
- u'foo bar' : results : str in Python 3, unicode in Python 2
- 'foo bar'  : results : str
- r'foo bar' : results : so called raw string, where escaping special characters
  is not necessary, everything is taken verbatim as you typed 

for eg,
normal = 'foo\nbar'         # foo 
                            # bar
escaped = 'foo\\nbar'       # foo\nbar
raw = r'foo\nbar'           # foo\nbar


-------------------------------------------------------------------------------------
-> Question 025: Python first class objects;;

It means there are no restrictions on the object's use. It's the same as any
other object.

A first class object is an entity that can be dynamically created, destroyed,
passed to a function, returned as a value, and have all the rights as other
variables in the programming language have.

Depending on the language, this can imply:

- Being expressible as an anonymous literal value
- Being storable in variables
- Being storable in data structures
- Being having an intrinsic identity (independent of any given name)
- Being comparable for equality with other entities
- Being passable as a parameter to a procedure/function
- Being returnable as the result of a procedure/function
- Being constructible at runtime
- Being printable
- Being readable
- Being transmissible among distributed processes
- Being storable outside running processes


-------------------------------------------------------------------------------------
-> Question 024: Python main() function;;

In the world of programming languages, the main is considered as an entry
point of execution for a program. But in python, it is known that the
interpreter serially interprets the file line-by-line. This means that python
does not provide main() function explicitly. But this doesn't mean that we
cannot simulate the execution of main. This can be done by defining
user-defined main() function and by using the __name__ property of python
file. This __name__ variable is a special built-in variable that points to
the name of the current module. This can be done as shown below:


def main():
   print("Hi Interviewbit!")
if __name__=="__main__":
   main()


-------------------------------------------------------------------------------------
-> Question 023: Shallow Copy vs Deep Copy;;

Shallow copy does the task of creating new objects storing references of
original elements. This does not undergo recursion to create copies of nested
objects. It just copies the reference details of nested objects.

Deep copy creates an independent and new copy of an object and even copies all
the nested objects of the original element recursively.


-------------------------------------------------------------------------------------
-> Question 022: Global Interpreter Lock;;

Yes, there are tools like PyChecker and Pylint which are used as static
analysis and linting tools respectively. PyChecker helps find bugs in python
source code files and raises alerts for code issues and their complexity.
Pylint checks for the module’s coding standards and supports different
plugins to enable custom features to meet this requirement.


-------------------------------------------------------------------------------------
-> Question 022: Global Interpreter Lock;;

GIL stands for Global Interpreter Lock. This is a mutex used for limiting
access to python objects and aids in effective thread synchronization by
avoiding deadlocks. GIL helps in achieving multitasking (and not parallel
computing). The following diagram represents how GIL works.


Based on the above diagram, there are three threads. First Thread acquires the
GIL first and starts the I/O execution. When the I/O operations are done,
thread 1 releases the acquired GIL which is then taken up by the second
thread. The process repeats and the GIL are used by different threads
alternatively until the threads have completed their execution. The threads
not having the GIL lock goes into the waiting state and resumes execution
only when it acquires the lock.





-------------------------------------------------------------------------------------
-> Question 021: Lambda function in Python;;

Lambda functions are generally inline, anonymous functions represented by a
single expression. They are used for creating function objects during
runtime. They can accept any number of parameters. They are usually used
where functions are required only for a short period. They can be used as:

mul_func = lambda x,y : x*y
print(mul_func(6, 4))
# Output: 24

-------------------------------------------------------------------------------------
-> Question 020: Module vs Packages in Python;;

The module is a single python file. A module can import other modules
(other python files) as objects. Whereas, a package is the folder/directory
where different sub-packages and the modules reside.

A python module is created by saving a file with the extension of .py. This
file will have classes and functions that are reusable in the code as well as
across modules.

A python package is created by following the below steps:

Create a directory and give a valid name that represents its operation. Place
modules of one kind in this directory. Create __init__.py file in this
directory. This lets python know the directory we created is a package. The
contents of this package can be imported across different modules in other
packages to reuse the functionality.


-------------------------------------------------------------------------------------
-> Question 019: Inheritance in Python;;

Inheritance gives the power to a class to access all attributes and methods of
another class. It aids in code reusability and helps the developer to
maintain applications without redundant code. The class inheriting from
another class is a child class or also called a derived class. The class from
which a child class derives the members are called parent class or
superclass.

Python supports different kinds of inheritance, they are:

# Single Inheritance: Child class derives members of one parent class.

# Parent class
class ParentClass:
    def par_func(self):
         print("I am parent class function")

# Child class
class ChildClass(ParentClass):
    def child_func(self):
         print("I am child class function")

# Driver code
obj1 = ChildClass()
obj1.par_func()
obj1.child_func()


# Multi-level Inheritance: The members of the parent class, A, are inherited
  by child class which is then inherited by another child class, B. The
  features of the base class and the derived class are further inherited into
  the new derived class, C. Here, A is the grandfather class of class C.

# Parent class
class A:
   def __init__(self, a_name):
       self.a_name = a_name
   
# Intermediate class
class B(A):
   def __init__(self, b_name, a_name):
       self.b_name = b_name
       # invoke constructor of class A
       A.__init__(self, a_name)

# Child class
class C(B):
   def __init__(self,c_name, b_name, a_name):
       self.c_name = c_name
       # invoke constructor of class B
       B.__init__(self, b_name, a_name)
       
   def display_names(self):
       print("A name : ", self.a_name)
       print("B name : ", self.b_name)
       print("C name : ", self.c_name)

#  Driver code
obj1 = C('child', 'intermediate', 'parent')
print(obj1.a_name)
obj1.display_names()
 

# Multiple Inheritance: This is achieved when one child class derives members
  from more than one parent class. All features of parent classes are
  inherited in the child class.

# Parent class1
class Parent1:
   def parent1_func(self):
       print("Hi I am first Parent")

# Parent class2
class Parent2:
   def parent2_func(self):
       print("Hi I am second Parent")

# Child class
class Child(Parent1, Parent2):
   def child_func(self):
       self.parent1_func()
       self.parent2_func()

# Driver's code
obj1 = Child()
obj1.child_func()


# Hierarchical Inheritance: When a parent class is derived by more than one
  child class, it is called hierarchical inheritance.

# Base class
class A:
     def a_func(self):
         print("I am from the parent class.")

# 1st Derived class
class B(A):
     def b_func(self):
         print("I am from the first child.")

# 2nd Derived class
class C(A):
     def c_func(self):
         print("I am from the second child.")
 
# Driver's code
obj1 = B()
obj2 = C()
obj1.a_func()
obj1.b_func()    #child 1 method
obj2.a_func()
obj2.c_func()    #child 2 method


-------------------------------------------------------------------------------------
-> Question 018: Access Specifiers used in python;;

Python does not make use of access specifiers specifically like private,
public, protected, etc. However, it does not derive this from any variables.
It has the concept of imitating the behaviour of variables by making use of a
single (protected) or double underscore (private) as prefixed to the variable
names. By default, the variables without prefixed underscores are public.

Example:

# to demonstrate access specifiers
class InterviewbitEmployee:
   
    # protected members
    _emp_name = None
    _age = None
    
    # private members
    __branch = None
    
    # constructor
    def __init__(self, emp_name, age, branch): 
         self._emp_name = emp_name
         self._age = age
         self.__branch = branch
    
    #public member
    def display():
        print(self._emp_name +" "+self._age+" "+self.__branch)


-------------------------------------------------------------------------------------
-> Question 017: Access Parent Class using Child class;;

Following are the ways using which you can access parent class members within
a child class:

By using Parent class name: You can use the name of the parent class to access
the attributes as shown in the example below:

# Example Class;
class Parent(object):  
   # Constructor
   def __init__(self, name):
       self.name = name    
 
class Child(Parent): 
   # Constructor
   def __init__(self, name, age):
       Parent.name = name
       self.age = age
 
   def display(self):
       print(Parent.name, self.age)
 

# Driver Code
obj = Child("Interviewbit", 6)
obj.display()


By using super(): The parent class members can be accessed in child class
using the super keyword.


class Parent(object):
   # Constructor
   def __init__(self, name):
       self.name = name    
 
class Child(Parent):
   # Constructor
   def __init__(self, name, age):         
       ''' 
       In Python 3.x, we can also use super().__init__(name)
       ''' 
       super(Child, self).__init__(name)
       self.age = age
 
   def display(self):
      # Note that Parent.name cant be used 
      # here since super() is used in the constructor
      print(self.name, self.age)
  
# Driver Code
obj = Child("Interviewbit", 6)
obj.display()



-------------------------------------------------------------------------------------
-> Question 016: Python Pickling vs UnPickling;;


Python library offers a feature - serialization out of the box. Serializing an
object refers to transforming it into a format that can be stored, so as to
be able to deserialize it, later on, to obtain the original object. Here, the
pickle module comes into play.

Pickling:

Pickling is the name of the serialization process in Python. Any object in
Python can be serialized into a byte stream and dumped as a file in the
memory. The process of pickling is compact but pickle objects can be
compressed further. Moreover, pickle keeps track of the objects it has
serialized and the serialization is portable across versions. The function
used for the above process is pickle.dump().

Unpickling:

Unpickling is the complete inverse of pickling. It deserializes the byte
stream to recreate the objects stored in the file and loads the object to
memory. The function used for the above process is pickle.load(). Note:
Python has another, more primitive, serialization module called marshall,
which exists primarily to support .pyc files in Python and differs
significantly from the pickle.


-------------------------------------------------------------------------------------
-> Question 014: Class Composition in python;;




-------------------------------------------------------------------------------------
-> Question 013: @classmethod vs @stacticmethod;;

@classmethod 

The @classmethod decorator is a built-in function decorator that is an
expression that gets evaluated after your function is defined. The result of
that evaluation shadows your function definition. A class method receives the
class as an implicit first argument, just like an instance method receives
the instance.

Syntax Python Class Method: 

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.

- A class method is a method that is bound to the class and not the object of
  the class.
- They have the access to the state of the class as it takes a class parameter
that points to the class and not the object instance.
- It can modify a class state that would apply across all the instances of the
class. For example, it can modify a class variable that will be applicable to
all the instances.

@staticmethod 

A static method does not receive an implicit first argument. A static method
is also a method that is bound to the class and not the object of the class.
This method can’t access or modify the class state. It is present in a class
because it makes sense for the method to be present in class.

Syntax Python Static Method: 

class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.

# When to use the class or static method ?
- We generally use the class method to create factory methods. Factory methods
  return class objects ( similar to a constructor ) for different use cases.
- We generally use static methods to create utility functions.

for eg,
# Python program to demonstrate
# use of class method and static method.
from datetime import date
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))

#Output:
21
25
True

-------------------------------------------------------------------------------------
-> Question 012: Magic Method __str__() vs __repr__();;

In Python, the built-in str() and repr() functions both produce a textual
representation of an object.

for eg,

import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))

# Output:
2021-10-14 10:15:31.405463          # output: __str__
datetime.datetime(2021, 10, 14, 10, 15, 31, 405463)     # output: __repr__

The difference between str() and repr() is:-
- The str() function returns a user-friendly description of an object.
- The repr() method returns a developer-friendly string representation of an object.

Working str() and repr() under the hood:-
- When you call str() on an object, it calls the special method __str__ of
the object.
- And when you call repr() on an object, it calls the special method __repr__ 
of the object.
- Also, when you call print() on an object, it calls __str__ method of the 
object. If __str__ is not implemented, the __repr__ is called as a fallback.

for eg, 

# Case 1: Without str() and repr();

class Fruit:
    def __init__(self, name):
        self.name = name

banana = Fruit("Banana")
print(banana)           

# output:
<__main__.Fruit object at 0x7f0ece0e8d00>

# Case 2: With str() and repr();

class Fruit:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'I am a {self.name}'
    
    def __repr__(self):
        return f'Fruit("{self.name}")'

banana = Fruit("Banana")
print(banana)       # output: I am a Banana

-------------------------------------------------------------------------------------
-> Question 011: Set Variable LowerBound and UpperBound;;

This methods helps to set the upper and lower bound of a bound for fallback
prevention.

-> FIRST APPROACH

for eg,
>>> from sys import maxsize

>>> minValue = -maxsize
>>> maxValue = maxsize
>>> print(minValue, maxValue)

-> SECOND APPROACH 
It acts as an unbounded upper value for comparison. This is
useful for finding lowest values for something. for example, calculating path
route costs when traversing trees.

e.g. Finding the "cheapest" path in a list of options:

>>> lowest_path_cost = float('inf')
>>> # pretend that these were calculated using some worthwhile algorithm
>>> path_costs = [1, 100, 2000000000000, 50]
>>> for path in path_costs:
...   if path < lowest_path_cost:
...     lowest_path_cost = path
...
>>> lowest_path_cost
1

if you didn't have float('Inf') available to you, what value would you use for
the initial lowest_path_cost? Would 9999999 be enough -- float('Inf') removes
this guesswork.

-------------------------------------------------------------------------------------
-> Question 010: Create a Generator Class;;

You're almost there, writing an Iterator class (I show a Generator at the end
of the answer), but __next__ gets called every time you call the object with
next, returning a generator object. Instead, to make your code work with the
least changes, and the fewest lines of code, use __iter__, which makes your
class instantiate an iterable (which isn't technically a generator):

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a+self.b
When we pass an iterable to iter(), it gives us an iterator:

>>> f = iter(Fib())
>>> for i in range(3):
...     print(next(f))
...
0
1
1

To make the class itself an iterator, it does require a __next__:

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1        
    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a+self.b
        return return_value
    def __iter__(self):
        return self

And now, since iter just returns the instance itself, we don't need to call
it:

>>> f = Fib()
>>> for i in range(3):
...     print(next(f))
...
0
1
1

-> Why is the value self.a not getting printed at the first place?

Here's your original code with my comments:

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
        
    def __next__(self):
        yield self.a          # yield makes .__next__() return a generator!
        self.a, self.b = self.b, self.a+self.b

f = Fib()

for i in range(3):
    print(next(f))
    
So every time you called next(f) you got the generator object that __next__
returns:

<generator object __next__ at 0x000000000A3E4F68>
<generator object __next__ at 0x000000000A3E4F68>
<generator object __next__ at 0x000000000A3E4F68>


-------------------------------------------------------------------------------------
-> Question 009: Iterators Vs Iterables Vs Generators in python;;

-> Iterators:-
An object capable of returning its members one at a time. Examples of
iterables include all sequence types (such as list, str, and tuple) and some
non-sequence types like dict, file objects, and objects of any classes you
define with an __iter__() method or with a __getitem__() method that
implements Sequence semantics.

Iterables can be used in a for loop and in many other places where a sequence
is needed (zip(), map(), …). When an iterable object is passed as an argument
to the built-in function iter(), it returns an iterator for the object. This
iterator is good for one pass over the set of values. When using iterables, it
is usually not necessary to call iter() or deal with iterator objects
yourself. The for statement does that automatically for you, creating a
temporary unnamed variable to hold the iterator for the duration of the loop.
See also iterator, sequence, and generator.


-> Iterables:-
An object representing a stream of data. Repeated calls to the iterator’s
__next__() method (or passing it to the built-in function next()) return
successive items in the stream. When no more data are available a
StopIteration exception is raised instead. At this point, the iterator object
is exhausted and any further calls to its __next__() method just raise
StopIteration again. Iterators are required to have an __iter__() method that
returns the iterator object itself so every iterator is also iterable and may
be used in most places where other iterables are accepted. One notable
exception is code which attempts multiple iteration passes. A container object
(such as a list) produces a fresh new iterator each time you pass it to the
iter() function or use it in a for loop. Attempting this with an iterator will
just return the same exhausted iterator object used in the previous iteration
pass, making it appear like an empty container.


-> Generator:-
A function which returns a generator iterator. It looks like a normal function
except that it contains yield expressions for producing a series of values
usable in a for-loop or that can be retrieved one at a time with the next()
function.

Usually refers to a generator function, but may refer to a generator iterator
in some contexts. In cases where the intended meaning isn’t clear, using the
full terms avoids ambiguity.


-> Generator Iterators:-
An object created by a generator function.

Each yield temporarily suspends processing, remembering the location execution
state (including local variables and pending try-statements). When the
generator iterator resumes, it picks-up where it left-off (in contrast to
functions which start fresh on every invocation).


-------------------------------------------------------------------------------------
-> Question 008: Iterators in python;;

The below is class which implements `__next__`as if it was a function using
the `yield` keyword:

class FirstHundredGenerator(object):
    def __init__(self):
        self.number = 0

    # Iterators are those which have __next__(self) function;;
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()     ## used to stop iteration;;

gen = FirstHundredGenerator()
next(gen)  # 0
next(gen)  # 1

Notice how the object, with its property, remembers what the value of
`self.number` is at all points in time.

This object is called in Python a generator because every time the next number
is available not because it’s in a sequence, but because it is generated from
its current state (in this case, by adding 1 to `self.number`).

All objects that have this `__next__` method are called iterators. All
generators are iterators, but not the other way round.

For example, you could have an iterator on which you can call `next()`, but
that doesn’t generate its values. Instead, it could take them from a list or
from a database.

*Important*: iterators are objects which have a `__next__` method.

Here’s an example of an iterator which is not a generator:

for eg,
  class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0
    
    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()

As you can see it’s returning numbers that are not being generated; instead
they’re being returned from a list.

If we run this code though, we will get an error:


sum(FirstHundredGenerator())  # comment this line out to run the rest of the file.

or 

for i in FirstHundredGenerator():
    print(i)


And that’s because in Python, an `iterator` and an `iterable` are different
things. You can iterate over an `iterable`. The iterator is used to get the
next value (either from a sequence or generated values).

You can iterate over iterables, not over iterators.
  
-------------------------------------------------------------------------------------
-> Question 007: Generator in Python;;

A generator in Python is a function that remembers the state it’s in, in
between executions.

Let’s explain with an example. Imagine you wanted to build a list of 100
numbers, like this one:

for eg,
  def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
      nums.append(num)
      i += 1
    return nums

We could use list comprehension for this and the `range()` function, but for
now let’s assume that this is a cool way of doing it. We construct a list,
fill it with the first 100 numbers, and then return them.

We now have 100 numbers in a list. The entire list is in your computer’s RAM
memory, taking up an admittedly small amount of space.

If we wanted 10,000,000 numbers, the list would be substantially bigger. As
you grow the number, the amount of memory taken up by the list also grows.

A generator is used to circumvent this problem. Instead of having a list, the
first time you run the function you would get the first number (`0`). The
second time you run the function you’d get `1`. Then `2`, and so on.

You have to run the function every time you want a new number, that’s why it’s
called a “generator”. It generates numbers (or indeed strings, or anything
else you want to generate).

for eg,
  def hundred_numbers():
    num = 0
    while num < 100:
      yield num
      num += 1

The `yield` keyword is very much like a `return`, in that it gives the value
back to the caller and returns execution control to them (show this with
example run). However, the next time you run the function, execution continues
from the very next line inside the function, instead of from the top.

We could re-write the function as a list comprehension:

for eg,
  hunderd_numbers = [n for n in range(100)]

Or indeed as a generator comprehension. This is essentially the same thing,
including the `yield` statement.

hundred_numbers = (n for n in range(100))
print(next(hundred_numbers))
print(next(hundred_numbers))

print(list(hundred_numbers))

""" 
Notice that when we do the code snippet above, `next()` runs the function
once up until the `yield` (which would give you the first value). The
following `next()` runs it again, which gives you the second value. Then,
turning it into a list continues and builds a list from the remaining values
(that’s only 98 values left).

A few sections ago I printed out `range(10)` and it was a strange `range(0,
10)` thing. That’s a generator object! 
"""

-------------------------------------------------------------------------------------
-> Question 006: Type Hinting in Python;;

It is used to validate the data type of the incoming argument of a function or
returning variable  from the function; 

  For eg,
  from typing import List, Dict, Tuple, Type        ## Import statement;

  def sample(x: int) -> List[Dict[key, bool]:
    res = []
    for i in range(x):
      if(i%2 == 0)
        res.append({i:True})
      else:
        res.append({i:False})

    return res            ## Output: List[Dict[int, bool]]


## Generic Types

The fundamental building blocks defined above allow to construct new types in
a generic manner. For example, Tuple can take a concrete type float and make a
concrete type Vector = Tuple[float, ...], or it can take another type UserID
and make another concrete type Registry = Tuple[UserID, ...]. Such semantics
is known as generic type constructor, it is similar to semantics of functions,
but a function takes a value and returns a value, while generic type
constructor takes a type and “returns” a type.

It is common when a particular class or a function behaves in such a type
generic manner. Consider two examples:

Container classes, such as list or dict, typically contain only values of a
particular type. Therefore, a user might want to type annotate them as such:
users = [] # type: List[UserID] users.append(UserID(42)) # OK
users.append('Some guy') # Should be rejected by the type checker

examples = {} # type: Dict[str, Any]
examples['first example'] = object() # OK
examples[2] = None                   # rejected by the type checker

The following function can take two arguments of type int and return an int,
or take two arguments of type float and return a float, etc.: 

def add(x, y):
  return x + y

add(1, 2) == 3
add('1', '2') == '12'
add(2.7, 3.5) == 6.2

To allow type annotations in situations from the first example, built-in
containers and container abstract base classes are extended with type
parameters, so that they behave as generic type constructors. Classes, that
behave as generic type constructors are called generic types. Example:

from typing import Iterable

class Task:
    ...

def work(todo_list: Iterable[Task]) -> None:
    ...

Here Iterable is a generic type that takes a concrete type Task and returns a
concrete type Iterable[Task].

Functions that behave in the type generic manner (as in second example) are
called generic functions. Type annotations of generic functions are allowed by
type variables. Their semantics with respect to generic types is somewhat
similar to semantics of parameters in functions. But one does not assign
concrete types to type variables, it is the task of a static type checker to
find their possible values and warn the user if it cannot find. Example:

def take_first(seq: Sequence[T]) -> T: # a generic function
    return seq[0]

accumulator = 0 # type: int

accumulator += take_first([1, 2, 3])   # Safe, T deduced to be int
accumulator += take_first((2.7, 3.5))  # Unsafe

Type variables are used extensively in type annotations, also internal
machinery of the type inference in type checkers is typically build on type
variables. Therefore, let us consider them in detail.

-------------------------------------------------------------------------------------

-> Question 005: Copy in Python;

In Python, the assignment statement (= operator) does not copy objects.
Instead, it creates a binding between the existing object and the target
variable name. To create copies of an object in Python, we need to use the
copy module. Moreover, there are two ways of creating copies for the given
object using the copy module -

Shallow Copy is a bit-wise copy of an object. The copied object created has an
exact copy of the values in the original object. If either of the values is a
reference to other objects, just the reference addresses for the same are
copied. 

Deep Copy copies all values recursively from source to target object,
i.e. it even duplicates the objects referenced by the source object.

from copy import copy, deepcopy
list_1 = [1, 2, [3, 5], 4]
## shallow copy
list_2 = copy(list_1) 
list_2[3] = 7
list_2[2].append(6)
list_2    # output => [1, 2, [3, 5, 6], 7]
list_1    # output => [1, 2, [3, 5, 6], 4]
## deep copy
list_3 = deepcopy(list_1)
list_3[3] = 8
list_3[2].append(7)
list_3    # output => [1, 2, [3, 5, 6, 7], 8]
list_1    # output => [1, 2, [3, 5, 6], 4]

-------------------------------------------------------------------------------------
-> Question 004: Python arrays;

Arrays in python can only contain elements of same data types i.e., data type
of array should be homogeneous. It is a thin wrapper around C language arrays
and consumes far less memory than lists. Lists in python can contain elements
of different data types i.e., data type of lists can be heterogeneous. It has
the disadvantage of consuming large memory.

import array

a = array.array('i', [1, 2, 3])
for i in a:
    print(i, end=' ')    #OUTPUT: 1 2 3

a = array.array('i', [1, 2, 'string'])   

#OUTPUT: TypeError: an integer is required (got type str)

a = [1, 2, 'string']

for i in a:
   print(i, end=' ')    #OUTPUT: 1 2 string

-------------------------------------------------------------------------------------
-> Question 003: LAMBDA;

Lambda is an anonymous function in Python, that can accept any number of
arguments, but can only have a single expression. It is generally used in
situations requiring an anonymous function for a short time period. Lambda
functions can be used in either of the two ways:

Assigning lambda functions to a variable:
mul = lambda a, b : a * b
print(mul(2, 5))    # output => 10
Wrapping lambda functions inside another function:
def myWrapper(n):
 return lambda a : a * n
mulFive = myWrapper(5)
print(mulFive(2))    # output => 10

-------------------------------------------------------------------------------------
-> Question 002: Comprehensions;

Python comprehensions, like decorators, are syntactic sugar constructs that
help build altered and filtered lists, dictionaries, or sets from a given
list, dictionary, or set. Using comprehensions saves a lot of time and code
that might be considerably more verbose (containing more lines of code). Let's
check out some examples, where comprehensions can be truly beneficial:

Performing mathematical operations on the entire list
my_list = [2, 3, 5, 7, 11]
squared_list = [x**2 for x in my_list]    # list comprehension
# output => [4 , 9 , 25 , 49 , 121]
squared_dict = {x:x**2 for x in my_list}    # dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}
Performing conditional filtering operations on the entire list
my_list = [2, 3, 5, 7, 11]
squared_list = [x**2 for x in my_list if x%2 != 0]    # list comprehension
# output => [9 , 25 , 49 , 121]
squared_dict = {x:x**2 for x in my_list if x%2 != 0}    # dict comprehension
# output => {11: 121, 3: 9 , 5: 25 , 7: 49}

Combining multiple lists into one Comprehensions allow for multiple iterators
and hence, can be used to combine multiple lists into one. 

a = [1, 2, 3]
b = [7, 8, 9]
[(x + y) for (x,y) in zip(a,b)]  # parallel iterators
# output => [8, 10, 12]
[(x,y) for x in a for y in b]    # nested iterators
# output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)] 

Flattening a multi-dimensional list A similar approach of nested iterators (as
above) can be applied to flatten a multi-dimensional list or work upon its
inner elements. 

my_list = [[10,20,30],[40,50,60],[70,80,90]]
flattened = [x for temp in my_list for x in temp]
# output => [10, 20, 30, 40, 50, 60, 70, 80, 90]

Note: List comprehensions have the same effect as the map method in other
languages. They follow the mathematical set builder notation rather than map
and filter functions in Python.


-------------------------------------------------------------------------------------
-> Question 001: Decorators in python;; 

Decorators in Python are essentially functions that add functionality to an
existing function in Python without changing the structure of the function
itself. They are represented the @decorator_name in Python and are called in a
bottom-up fashion. For example:

# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper():
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper
# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper
@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'
hello()   # output => [ 'hello' , 'world' ]

The beauty of the decorators lies in the fact that besides adding
functionality to the output of the method, they can even accept arguments for
functions and can further modify those arguments before passing it to the
function itself. The inner nested function, i.e. 'wrapper' function, plays a
significant role here. It is implemented to enforce encapsulation and thus,
keep itself hidden from the global scope.

# decorator function to capitalize names
def names_decorator(function):
   def wrapper(arg1, arg2):
       arg1 = arg1.capitalize()
       arg2 = arg2.capitalize()
       string_hello = function(arg1, arg2)
       return string_hello
   return wrapper
@names_decorator
def say_hello(name1, name2):
   return 'Hello ' + name1 + '! Hello ' + name2 + '!'
say_hello('sara', 'ansh')   # output => 'Hello Sara! Hello Ansh!'


-------------------------------------------------------------------------------------