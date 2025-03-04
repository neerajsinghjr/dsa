````
-------------------------------------------------------------------------------------
-> Title: Python Diary
-> Author: @neeraj-singh-jr
-> Status: Ongoing...
-> Created: 03/09/2022
-> Updated: 02/03/2025
-> Summary: Notes indices are as follows (*** pending)
-------------------------------------------------------------------------------------
-> Q099 : Closures (Function Encapsulation and Memory Retention);;
-> Q098 : Closures & Decorators (Delayed Execution and Function References);;
-> Q097 : Python Reference Counting & Memory Management;;
-> ***Q096 : Multithreading using Future Module;;
-> ***Q095 : Usages of MultiProcessing Vs Asyncio;;
-> ***Q094 : Inspect module in python;;
-> Q094 : Inspect module in python;;
-> Q093 : Dataclass Schema Creation with Decorator;;
-> Q092 : Dataclass Decorator in Python;;
-> Q091 : Variable Type Hinting in Python;;
-> Q090 : Python Round Division;;
-> Q089 : Scopes in Python Language;;
-> Q088 : What are Mixin in Python;;
-> Q087 : Memoization Concept with Python Decorator;;
-> Q086 : Reduce function in python;;
-> Q085 : Multiprocessing (CPU Task) Vs Asyncio(IO Task);; 
-> Q084 : Asyncio Module in Python;;
-> Q083 : Method Resolution Order in Python;;
-> Q082 : UDP Socket Programming in Pthon
-> Q081 : Multiprocessing Lock And Pool;;
-> Q080 : SortedContainers in Python;;
-> Q079 : Enum in Python;;
-> Q078 : Python Multithreading;;
-> Q077 : Python Crontab Job function;;
-> Q076 : Python Celery function;;
-> Q075 : Python rsplit function;;
-> Q074 : Python Unittest Mock Library;;
-> Q073 : Python urllib method urljoin();;
-> Q072 : Python class inherits from objects;;
-> Q071 : Multitreading Vs Multiprocessing;;
-> Q070 : Different usage when add list to set or set to set;;
-> Q069 : Time Delta (timedelta) in python;;
-> Q068 : Relative Delta (relativedelta)in Python;;
-> Q067 : Sort and Reverse Dictionary by value;;
-> Q066 : Iterators Workflow in Python;;
-> Q065 : Bitwise Operators;;
-> Q064 : Magic Method __call__ in Python;;
-> Q063 : Class Decorator in Python;;
-> Q062 : Generators Workflow in Python;;
-> Q061 : First Class Function in Python;;
-> Q060 : Operator Overloading in Python;;
-> Q059 : Inheritance in Python;;
-> Q058 : Class and Objects Python;;
-> Q057 : Decorator in Python;;
-> Q056 : Date and Time (datetime) Module;;
-> Q055 : Deque in collection module;;
-> Q054 : Name Tuples (namedtuple) in collections module;;
-> Q053 : Ordered Dictionary;;
-> Q052 : Difference list vs [];;
-> Q051 : Collection Module;;
-> Q050 : Exception Handling;;
-> Q049 : List or Variable Destructuring;;
-> Q048 : String Helpers Methods;;
-> Q047 : Dictionary and Operation;;
-> Q046 : Set and Operation;;
-> Q045 : List and Operations;;
-> Q044 : Padding Number using F-String;;
-> Q043 : Join() vs Format() in Python;;
-> Q042 : Python Conventions;;
-> Q041 : Python Operator Precedance;;
-> Q040 : Hashing vs Encryption;;
-> Q039 : What is C3 Linearization in Multiple Inheritance;;
-> Q038 : Multiple Inheritance in Python vs Java;;
-> Q037 : Method Overloading and Operator Overloading;;
-> Q036 : Switch alternative in python;;
-> *** Q035 : ???;;
-> Q034 : Python OOPS Basic Architecture;;
-> Q033 : ABCMeta, AbstractClass, abstractmethod in ABC package;;
-> Q032: Positional Argument(args) & Named Argument(kwargs);;
-> Q031 : Finding and Installing Packages;;
-> Q030 : Default Dict in Python;;
-> Q029 : GropuBy in Itertools;;
-> Q028 : Builtins Error and Exception;;
-> Q027 : Mutable and Immutable data types;;
-> Q026 : Explicit string type at definition of literals;;
-> Q025 : Python first class objects;;
-> Q024 : Python main() function;;
-> Q023 : Shallow Copy vs Deep Copy;;
-> Q022 : Global Interpreter Lock;;
-> Q021 : Lambda function in Python;;
-> Q020 : Module vs Packages in Python;;
-> Q019 : Inheritance in Python;;
-> Q018 : Access Specifiers used in python;;
-> Q017 : Access Parent Class using Child class;;
-> Q016 : Python Pickling vs UnPickling;;
-> Q015 : Class Compositon Vs Inheritance;;
-> Q014 : Duck Typing in Python;;
-> Q013 : @classmethod() vs @staticmethod();;
-> Q012 : Magic Method __str__() vs __repr__();;
-> Q011 : Set Variable LowerBound and UpperBound;;
-> Q010 : Create a Iterator Class using Generator;;
-> Q009 : Iterators Vs Iterables Vs Generators in python;;
-> Q008 : What are Iterators in python;;
-> Q007 : What are Generators in python;;
-> Q006 : Type Hinting;;
-> Q005 : Copy in python;;
-> Q004 : Python arrays;;
-> Q003 : LAMBDA in python;;
-> Q002 : Comprehension in python;;
-> Q001 : Decorators in python;;
-------------------------------------------------------------------------------------
````

### PYTHON NOTES : BEGINNING 

-------------------------------------------------------------------------------------
### Q99 : Closures (Function Encapsulation and Memory Retention);;

Closures in Python are a way to retain access to variables from an enclosing
function even after that function has finished executing. 

---
for eg, go through the code problem
```python
def create_adder(x):  
    def adder(y):  
        return x + y  
    return adder  # Returning the inner function reference
```

Here’s what happens step by step:

1. **Calling `create_adder(10)`**  
   - `x = 10`
   - The function `adder(y)` is **defined but not executed yet**.
   - `adder` is returned as a function reference.

2. **Assigning it to a variable:**
   ```python
   add_10 = create_adder(10)
   ```
   - Now, `add_10` holds a reference to the `adder(y)` function.
   - `adder(y)` still remembers that `x = 10` **even though `create_adder` has
     finished executing**.

3. **Calling `add_10(5)`:**
   ```python
   print(add_10(5))  # Output: 15
   ```
   - `adder(y)` executes with `y = 5`.
   - Since `adder(y)` remembers `x = 10`, it computes `10 + 5 = 15`.

#### Why does this happen?

- Python keeps `x` in memory because `adder(y)` **closes over** the `x`
  variable.  
- This is called a **closure**: the function `adder` **remembers the
  environment in which it was created**.

#### Relation to Decorators  

Yes! This is exactly how decorators work. In decorators, an inner function
retains access to the function it wraps, just like `adder` retains access to
`x`.


-------------------------------------------------------------------------------------
### Q98 : Closures & Decorators (Delayed Execution and Function References);;

---

#### **CLOSURE POINT OF VIEW #1 : FROM FUNCTION PERSPECTIVE;;**


#### **Understanding `adder()` vs `adder` in `create_adder` Function**

Let's break it down step by step:


**1. Function Definition**

```python
def create_adder(x):  
    def adder(y):  
        return x + y  
    return adder 
```

- `create_adder(x)`: This function **returns** another function (`adder`).
- `adder(y)`: This function takes `y` as input and returns `x + y`.

---

**2. `adder` vs `adder()`**

| Expression | Meaning |
|------------|---------|
| `adder` | **Refers to the function itself** (without calling it). It is a function object. |
| `adder()` | **Calls the function**, executing its code and returning a result. |

---

### **3. Example Usage**
```python
add5 = create_adder(5)  # create_adder returns the `adder` function where x=5
print(add5)             # <function create_adder.<locals>.adder at 0x...>
print(add5(10))         # 5 + 10 = 15
```
- `add5` is now a function that **remembers `x=5`**.
- `add5(10)` calls `adder(10)`, which returns `5 + 10 = 15`.


---

#### **FOLLOW UP : if adder is only a method reference not an actual function
       call then how come it is able to give result because adder is never
       called**

#### REFER BELOW FINDINGS ...

**1. Understanding How `adder` Works Without Being Called**

When we define and return `adder` inside `create_adder`, we are **not
calling** `adder` inside `create_adder`. Instead, we are **returning a
reference** to the function.  

**Code Breakdown:**  

```python
def create_adder(x):  
    def adder(y):  # Inner function (closure)
        return x + y  
    return adder  # Returns a reference to `adder`, NOT calling it
```

- `create_adder(5)` **returns** `adder`, meaning `adder` is now a function
  waiting to be executed.
- `adder` remembers the value of `x` (closure).
- **Only when we call `adder(y)`, the function actually runs.**


**2. Function Reference vs. Function Execution**

Let's see this in action:  

```python
add5 = create_adder(5)  # Returns a reference to `adder`
print(add5)  # <function create_adder.<locals>.adder at 0x...> (Function reference)
print(add5(10))  # Calls adder(10), executes it → Output: 15
```

- `create_adder(5)` does **not** execute `adder` but **returns a reference**
  to it.
- When we later call `add5(10)`, it actually executes `adder(10)`.


**3. Why Does `adder` Work Even When Not Called Inside `create_adder`?**

This is because of **closures in Python**.  

- `adder(y)` is a **nested function** inside `create_adder(x)`.  
- Even after `create_adder` finishes execution, `adder` **remembers** the
  value of `x` (5 in our case).  
- This behavior is due to **closures**, which allow inner functions
  to "remember" variables from their enclosing scope.


**4. Proof That `adder` Is Not Called Immediately**

Let's modify the code to include a print statement:

```python
def create_adder(x):  
    print(f"create_adder called with x={x}")  # Debug print
    
    def adder(y):  
        print(f"adder called with y={y}")  # Debug print
        return x + y  
    
    return adder  # Only returns a reference to the function

add5 = create_adder(5)  
print("Function returned:", add5)  # Just a reference, not executing

result = add5(10)  # Now calling the function
print("Result:", result)

# OUTPUT:
# create_adder called with x=5
# Function returned: <function create_adder.<locals>.adder at 0x...>
# adder called with y=10
# Result: 15

```

---

#### CLOSURE POINT OF VIEW #2 : FROM DECORATOR PERSPECTIVE;;

Yes! The concept here is very similar to **function decorators**. Let’s break
it down and relate it to decorators for better understanding.  


**1. How Is `create_adder` Similar to a Decorator?**

Both `create_adder` and a decorator **return a function reference**, which is
executed later.

for example:  

```python
def convertStrToList(func):
    print(f">>>>>>> func: ", func)

    def wrapper(*args, **kwargs):
        print("*args: ", args)
        print("**kwargs: ", kwargs)
        return func(*args, **kwargs)  # Calling the original function

    return wrapper  # Returns function reference, NOT calling it immediately

@convertStrToList
def show():
    return "word of the day is madness"

print(show())  # Only now `wrapper` runs
```

**Similarities with `create_adder`:**  

- Both return a function reference instead of executing immediately.
- Execution happens only when we explicitly call the returned function (`show()` 
  or `add5(10)`).  
- Closure is used to remember external variables (`x` in `create_adder`,
  `func` in decorator).


### **2. Converting `create_adder` to a Decorator**

Let’s rewrite `create_adder` as a decorator for better comparison:

```python
def add_x(x):
    def decorator(func):
        def wrapper(y):
            return func(x, y)  # Pass `x` from outer function
        return wrapper  # Return function reference
    return decorator  # Return decorator

@add_x(5)  # Equivalent to create_adder(5)
def add_numbers(a, b):
    return a + b

print(add_numbers(10))  # Output: 15
```

- `add_x(5)` returns `decorator` (similar to `create_adder(5)` returning `adder`).  
- `decorator` modifies `add_numbers`, just like `create_adder` modifies `adder`.  
- Execution happens only when `add_numbers(10)` is called  


-------------------------------------------------------------------------------------
### Q097 : Python Reference Counting & Memory Management;;

Python uses **automatic memory management**, primarily through **reference
counting** and **garbage collection**. 

---

#### **1. Reference Counting**

Python objects are managed through a **reference count**, which tracks how
many references point to an object.

#### **How It Works**

Each object in Python has an internal counter that increases when a reference
is made and decreases when a reference is deleted.

#### **Example:**

```python
import sys

x = [1, 2, 3]  # List object is created
print(sys.getrefcount(x))  
# Output: 2 (one from x, one from getrefcount argument)

y = x  # Another reference to the same object
print(sys.getrefcount(x))  
# Output: 3 (x, y, and getrefcount reference)

del x  # Deleting x reduces reference count
print(sys.getrefcount(y))  
# Output: 2 (y and getrefcount reference)
```

- When `x = [1, 2, 3]`, Python creates the list object and assigns
  a **reference count of 1**.
- When `y = x`, the count **increases to 2**.
- When `del x` is executed, the count **decreases to 1**.
- Once all references are removed, the object is deleted from memory.

---

### **2. Garbage Collection (GC)**

Python has a **garbage collector (GC)** that automatically deallocates memory
when reference cycles are detected.

#### **Reference Cycle Problem**

Reference counting alone **fails** when objects reference each other, forming
a cycle:


```python
import gc

class A:
    def __init__(self):
        self.ref = None

a = A()
b = A()

a.ref = b  # a → b
b.ref = a  # b → a (circular reference)

del a, b  # Objects are not freed due to the cycle

print(gc.collect())  # Force garbage collection
```

Here, both objects reference each other, so their reference count never
reaches zero. The **garbage collector** detects and removes them.

### **Manually Controlling GC**

```python
import gc
gc.disable()  # Disable automatic garbage collection
gc.collect()  # Force garbage collection
gc.enable()  # Enable it again
```

---

#### **3. Memory Optimization Techniques**

- **Use `weakref` module** for **weak references** that don’t increase
    reference counts.
- **Manually remove references** (`del obj`).
- **Use generators** instead of storing large lists in memory.


-------------------------------------------------------------------------------------
### ***Q096 : Multithreading using Future Module;;



-------------------------------------------------------------------------------------
### ***Q095 : Usages of MultiProcessing Vs Asyncio;;



-------------------------------------------------------------------------------------
### ***Q094 : Inspect module in python;;



-------------------------------------------------------------------------------------
### Q093 : Dataclass Schema Creation with Decorator;;

> Refer : basic_py/03.advance/P007_Oops_Dataclass.py

#### Scenario: Creating a Dataclass based Schema for API Requests/Response

Suppose you're working with a User Management API where:

- Request: Create a user (POST /user)
    - Fields: name, email, age, phone_number
- Response: Get user details (GET /user/{id})
    - Fields: id, name, email, created_at

````python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import json

# Step 1: Implementation for Dataclasses 

@dataclass
class CreateUserRequest:
    """
    Schema for Create User API request.
    """
    name: str
    email: str
    age: Optional[int] = None  # Optional field
    phone_number: Optional[str] = None


@dataclass
class UserResponse:
    """
    Schema for User Details API response.
    """
    id: int
    name: str
    email: str
    created_at: datetime


# Step 2: Serialize/Deserialize API Data Using the Schemas

# Example: Simulate API Request Payload
request_payload = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "phone_number": "123-456-7890",
}

# Convert JSON to Dataclass Object
create_user_request = CreateUserRequest(**request_payload)
print(create_user_request)
# Output: CreateUserRequest(
    name='John Doe', email='john.doe@example.com', 
    age=30, phone_number='123-456-7890'
)

# Example: Simulate API Response Payload
response_payload = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "created_at": "2024-01-26T12:34:56",
}

# Deserialize API response to Dataclass Object
response_payload["created_at"] = datetime.fromisoformat(response_payload["created_at"])
user_response = UserResponse(**response_payload)
print(user_response)
# Output: UserResponse(
    id=1, name='John Doe', email='john.doe@example.com', 
    created_at=datetime.datetime(2024, 1, 26, 12, 34, 56)
)

# Step 3 : Validate or Enforce Data Constraints

@dataclass
class CreateUserRequest:
    name: str
    email: str
    age: Optional[int] = None
    phone_number: Optional[str] = None

    def __post_init__(self):
        if self.age is not None and self.age <= 0:
            raise ValueError("Age must be greater than 0")
        if "@" not in self.email:
            raise ValueError("Invalid email address")


# Step 4. Nested Dataclasses for Complex Schemas
@dataclass
class Address:
    street: str
    city: str
    zip_code: str


@dataclass
class CreateUserRequest:
    name: str
    email: str
    age: Optional[int] = None
    address: Address


# Example: Nested JSON Data
nested_request_payload = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "address": {
        "street": "123 Elm St",
        "city": "Springfield",
        "zip_code": "12345",
    },
}

# Deserialize Nested JSON to Dataclass
address = Address(**nested_request_payload["address"])
create_user_request = CreateUserRequest(**nested_request_payload, address=address)
# or create_user_request = CreateUserRequest(**nested_request_payload) 

print(create_user_request)
# Output: CreateUserRequest(
    name='John Doe', email='john.doe@example.com', 
    age=30, address=Address(
        street='123 Elm St', 
        city='Springfield', 
        zip_code='12345'
    )
)

# Convert Dataclass to JSON
request_json = json.dumps(asdict(create_user_request))
print(request_json)
# Output: 
{
    "name": "John Doe", "email": "john.doe@example.com", 
    "age": 30, "address": {
        "street": "123 Elm St", 
        "city": "Springfield", 
        "zip_code": "12345"
    }
}
````


-------------------------------------------------------------------------------------
### Q092 : Dataclass Decorator in Python;;

- Dataclasses is a decorator from the dataclasses module that simplifies the
  creation of classes by automatically generating special methods
  like __init__, __repr__, __eq__, etc., based on class attributes


#### Dataclasses Basic Usage 

```python
# Example : Basic example for dataclasses in Python;;

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

person1 = Person(name="John", age=30, email="john@example.com")
person2 = Person(name="Doe", age=25, email="doe@example.com")

# Auto-generated methods in action
print(person1)  # Person(name='John', age=30, email='john@example.com')
print(person1 == person2)  # False
```

**NOTE:** 
- Here, __init__, __repr__, and __eq__ are auto-generated.
- The attributes name, age, and email are automatically included in these
  methods.


#### Dataclasses Advances Usages 

> Default Values

- You can provide default values for fields.

```python
# Example 1: Default values with value 100;;

@dataclass
class Book:
    title: str
    author: str
    pages: int = 100


book = Book(title="Python 101", author="John Doe")
print(book)  # Book(title='Python 101', author='John Doe', pages=100)
```

> Default Factory

- For mutable types like lists, use field(default_factory=...)

```python
# Example 2: Usages of field 

from dataclasses import dataclass, field
from typing import List

@dataclass
class ShoppingCart:
    items: List[str] = field(default_factory=list)


cart = ShoppingCart()
cart.items.append("Apple")
print(cart)  # ShoppingCart(items=['Apple'])
```

> Custom Methods 

- Adding custom functions in dataclasses

````python
# Example 3: Adding functions

@dataclass
class Rectangle:
    length: float
    width: float

    def area(self) -> float:
        return self.length * self.width


rect = Rectangle(length=5.0, width=3.0)
print(rect.area())  # 15.0
````

> Post-Initialization (__post_init__)

- If you need custom logic after object creation, use `__post_init__`.

```python
# Example 4: Post-initialization method 

@dataclass
class Product:
    name: str
    price: float
    discounted_price: float = 0.0

    def __post_init__(self):
        self.discounted_price = self.price * 0.9  # Apply 10% discount


product = Product(name="Laptop", price=1000)
print(product.discounted_price)  # 900.0
```

> Frozen Dataclass

- If you want the dataclass to be immutable, set `frozen=True`

```python
# Example 5: Frozen Dataclass for attribute

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int


point = ImmutablePoint(1, 2)
# point.x = 3  # This will raise a FrozenInstanceError
```

> Excluding Fields from Comparison/Representation

- Use field() to exclude fields from being included in certain operations.

```python
# Example 6: field() can be used to mask parameter using repr 

@dataclass
class User:
    username: str
    password: str = field(repr=False)  # Excludes from `__repr__`


user = User(username="admin", password="secret")
print(user)  # User(username='admin')
```

> Inheritance with dataclass

- you can inherit `dataclass` like a normal class

```python
# Example : Dataclass Inheritance 

@dataclass
class Vehicle:
    make: str
    model: str


@dataclass
class Car(Vehicle):
    seats: str

car = Car(make="Toyota", model="Corolla", seats=5)
print(car)  # Car(make='Toyota', model='Corolla', seats=5)
```

#### When to Use dataclass
- For simple classes with attributes and no significant custom logic.
- When you want boilerplate code like __init__, __repr__, or __eq__ to be
  auto-generated.
- For immutable objects (use frozen=True).
- When managing complex data structures like nested configurations.


-------------------------------------------------------------------------------------
### Q091 : Variable Type Hinting in Python;;

- Type Hinting allows you to get the details of the variable used in the piece
  of code.

- These "type hints" are a special syntax that allow declaring the type of a
  variable

for eg,
````python
Ex1: Without Declaring any type hinting

# Here we dont know what type of value we can expect in fname, lname.
# It create a lack of readability inside the code 
def get_full_name(fname, lname): 
    return fname + " " + lname
   
if __name__ == "__main__":
    fname = "Neeraj" # here we know fname should be string
    lname = "Singh"  # here we know lname should be string
    
    print(get_full_name("john", "doe"))


Ex2: With Declaring type

def get_full_name(fname: str, lname: str): 
    return fname + " " + lname
 
if __name__ == "__main__":    
    print(get_full_name("john", "doe"))
````

#### Declaring Types

The main place to declare type hints. As function parameters.

1) int
2) float
3) bool
4) byte 
5) str

for eg,
```python
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e
```

#### Generic types with type parameters

- There are some data structures that can contain other values, like dict, 
list, set and tuple. And the internal values can have their own type too.

- These types that have internal types are called `generic types`. And 
it's possible to declare them, even with their internal types.

- To declare those types and the internal types, you can use the standard 
Python module `typing`. It exists specifically to support these type hints.

for eg,
```python
from typing import List


# Example 1: List Datatype
def process_items(items: List[str]):
    for item in items:
        print(item)
        
       
# Example 2: Tuple and Set Datatype
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

```

**DICT**

- To define a dict, you pass 2 type parameters, separated by commas.

- The first type parameter is for the keys of the dict.

- The second type parameter is for the values of the dict:

for eg,
````python
from typing import Dict


def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
````

**UNION**

- Variable can be any of several types, for example, an int or a str

- In Python 3.6 and above (including Python 3.10) you can use the Union 
type from typing and put inside the square brackets the possible types 
to accept.

- In Python 3.10 there's also a new syntax where you can put the possible 
types separated by a vertical bar (|).

for eg,
```python
from typing import Union


def process_item(item: Union[int, str]):
    print(item)
```

**Possibly NONE Value**

- You can declare that a value could have a type, like str, but that it 
could also be None.

- In Python 3.6 and above (including Python 3.10) you can declare it by 
importing and using Optional from the typing module.

- Using `Optional[str]` instead of just str will let the editor help you 
detecting the errors where you could be assuming that a value is always a 
`str`, when it could actually be `None` too.

- `Optional[Something]` is actually a shortcut for `Union[Something, None]`, 
they are equivalent.

for eg,
```python
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```

**Union or Optional**

- For Python3.10 version below. It would be better to use `Union[str, None]` 
instead of `Optional[str] = None`

- Both are equivalent and underneath they are the same, but I would recommend 
Union instead of Optional because the word "optional" would seem to imply that 
the value is optional, and it actually means "it can be None", even if it's not 
optional and is still required

- I think `Union[SomeType, None]` is more explicit about what it means.

for eg,
```python
from typing import Optional


def say_hi(name: Optional[str]):
    print(f"Hey {name}!") 
    
# The parameter name is defined as Optional[str], but it is not optional, 
# you cannot call the function without the parameter:
   
say_hi()  # Oh, no, this throws an error!

# The name parameter is still required (not optional) because it doesn't 
# have a default value. Still, name accepts None as the value:

say_hi(name=None)  # This works, None is valid
```

NOTE: 
From Python 3.10 you won't have to worry about that, as you will be able to 
simply use | to define unions of types

```python
def say_hi(name: str | None):
    print(f"Hey {name}!")
```

**Classes as types (Generic Type)**

for eg,
```python
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
```


-------------------------------------------------------------------------------------
### Q090 : Python Round Division;;

- `print(6//132)` will output 0, because it performs integer division between
  6 and 132, resulting in 0 with no remainder

- `print(6//-132)` will output -1, because it performs integer division
  between 6 and -132, resulting in -1 with no remainder.

- `print(int(6/-132))` use for accurate result or straight zero. 

> Conclusion:

In Python, integer division always rounds towards negative infinity, meaning
the result is rounded to the nearest integer that is less than or equal to
the true quotient. 

Therefore, -1 is the result of dividing 6 by -132.


-------------------------------------------------------------------------------------
### Q089 : Scopes in Python Language;;

Every object in Python functions within a scope. A scope is a block of code
where an object in Python remains relevant. Namespaces uniquely identify all
the objects inside a program. 

However, these namespaces also have a scope defined for them where you could
use their objects without any prefix. A few examples of scope created during
code execution in Python are as follows:

#### LOCAL Scope

A local scope refers to the local objects available in the current function.

for eg,
````python
def my_function():
    local_variable = 10
    print(local_variable)

my_function()
# This will print 10 because `local_variable` is defined 
# in the local scope of the function.
````

#### GLOBAL Scope:-

A global scope refers to the objects available throughout the code execution
since their inception.

for eg,
````python
global_variable = 20

def another_function():
    print(global_variable)

another_function()
# This will print 20 because `global_variable` is defined 
# in the global scope.
````

#### MODULE-LEVEL Scope
A module-level scope refers to the global objects of the current module accessible 
in the program.

for eg,
````python
# module_example.py
module_variable = 30

def some_function():
    print(module_variable)

# In another file or interactive session
import module_example

module_example.some_function()
# This will print 30 because `module_variable` is defined 
# at the module level.
````

#### BUILT-IN Scope

An outermost scope refers to all the built-in names callable in the program.
The objects in this scope are searched last to find the name referenced.

for eg,
````python
built_in_function = len("example")

def yet_another_function():
    print(len)  # This refers to the built-in len function.

yet_another_function()
# This will print the information about the built-in len function.

````

In this line, the len function is a built-in function in Python, and it is used to 
determine the length of a sequence (such as a string, list, or tuple). 

Here's how it works:
- The `len("example")` calculates the length of the string "example", which is 7.
- The result (7) is then assigned to the variable built_in_function.

Now, built_in_function holds the value 7, representing the length of the string 
"example". You can use the built_in_function variable later in your code.

Built-in functions like len are part of Python's standard library, and they are 
always available for use without the need for explicit import statements. 

These functions provide fundamental operations that can be applied to various 
types of objects in Python. Some other examples of built-in functions include 
print(), type(), sum(), and max().


-------------------------------------------------------------------------------------
### Q088 : What are Mixin in Python;;

In Python, mixins are classes that provide functionality to be inherited by
other classes. They are often used to add common or reusable behavior to
multiple classes without requiring multiple inheritance. Mixins typically
contain methods or attributes that can be shared across different classes.

for eg,
````python
# Define a mixin class for logging functionality
class LogMixin:
    def log_info(self, message):
        print(f"INFO: {message}")

    def log_error(self, message):
        print(f"ERROR: {message}")

# Define a class that uses the LogMixin
class MyClass(LogMixin):
    def do_something(self):
        # Call the log_info method from the LogMixin
        self.log_info("Doing something...")

        # Call the log_error method from the LogMixin
        self.log_error("Oops! Something went wrong.")

# Create an instance of MyClass and call its methods
obj = MyClass()
obj.do_something()
````

> Note

Mixins in Python often utilize multiple inheritance to provide reusable
behavior to multiple classes. 

````python
# Define a mixin class for logging functionality
class LogMixin:
    def log_info(self, message):
        print(f"INFO: {message}")

    def log_error(self, message):
        print(f"ERROR: {message}")

# Define a Utitlity Class for some Productive work;;
class Utils:
       
    def do_utility_stuff(self):
        print("doing something productive here")

# Define a class that uses the LogMixin
class MyClass(LogMixin, Utils):
    def do_something(self):
        # Call the log_info method from the LogMixin
        self.do_utility_stuff()
        self.log_info("Doing something...")

        # Call the log_error method from the LogMixin
        self.log_error("Oops! Something went wrong.")

# Create an instance of MyClass and call its methods
obj = MyClass()
obj.do_something()
````

However, the distinction is that mixins are typically designed to be used with
single inheritance, meaning that they are intended to be added to classes
that inherit from only one base class. This helps avoid the complexities and
ambiguity that can arise from multiple inheritance.


-------------------------------------------------------------------------------------
### Q087 : Memoization Concept with Python Decorator;;

A recursion is a technique where a function calls itself repeatedly till the base 
case condition is met.

Eg 1 : Calculation of Fibonacci series without memoization
````python
def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)

if __name__ == "__main__":
    print("Factorial Response : ", fact(5))
````

Eg2 : Calculation of Fibonacci series with memoization;;
````python
count = 0
memory = {}

def cache(func):
    def reading_cache(num):
        if num not in memory:
            memory[num] = func(num)
        return memory[num]
    return reading_cache

@cache
def fact(num):
    global count
    count += 1
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)

if __name__ == "__main__":
    print("Factorial Response: ", fact(10))
    print("Factorial Run-Count: ", count)
    # without memoization : fact: 120, count: 15
    # with memomization : fact: 120, count: 10
````

Explanation:-

- We have defined `cache` function to store the intermediate result in the variable 
called memory.
- The second method `fact` is the function to calculate the factorial. It is wrapped 
by the decorator `cache`. The fact method has access to the memory variables as result. 
The wrapped function is equivalent as `fact = cache(fact)`.
- When `fact(5)` is called, the recursive call begins in addition to the
  storage of the intermediate results. Every time a calculation needs to be
  done, it is checked if the result is available in the `memory`. If the
  value is available in the `memory` it is used, the value is calculated and
  stored in the `memory`.
- We can use this technique in the tree-based problems.


-------------------------------------------------------------------------------------
### Q086 : Reduce function in python;;

In Python, `reduce()` is a built-in function that applies a given function to the 
elements of an iterable, reducing them to a single value.

#### Syntax for reduce() is as follows:
> functools.reduce(function, iterable[, initializer])

#### Details:
- The function argument is a function that takes two arguments and returns a single 
value. 
- The first argument is the accumulated value, and the second argument is the 
current value from the iterable.
- The iterable argument is the sequence of values to be reduced.
- The optional initializer argument is used to provide an initial value for the 
accumulated result. If no initializer is specified, the first element of the iterable 
is used as the initial value.

for eg,
````python
from functools import reduce
from time import time
from random import randint

class Txn:
    @property
    def amount(self):
        return round(time())

orders = [Txn(), Txn(), Txn(), Txn()]

# Case 1
txn_amounts = map(lambda order: order.amount, orders)
print("txn_amounts: ", sum(txn_amounts))
# Output:
# txn_amounts:  6832652060

# Case 2
total_amounts = reduce(lambda amt1, amt2: amt1 + amt2, 
                        map(lambda order: order.amount, orders))
print("total_amounts: ", total_amounts)
# output:
# total_amounts:  6832652060

# Case 3:
nums = [21, 30, 34, 44, 47, 60 ,71]

def add(a, b):
    r = a + b
    print(f"a: {a}, b: {b}, r: {r}")
    return r
    
ans = reduce(add, nums)
print("ans: ", ans)
# Output :
# a: 21, b: 30, r: 51
# a: 51, b: 34, r: 85
# a: 85, b: 44, r: 129
# a: 129, b: 47, r: 176
# a: 176, b: 60, r: 236
# a: 236, b: 71, r: 307
# ans:  307
````


-------------------------------------------------------------------------------------
### Q085 : Multiprocessing (CPU Task) Vs Asyncio(IO Task);;

(Refer Example : dsa/basic-py/P038_Asyncio.py)

(Refer Study : https://realpython.com/async-io-python/)

`Multiprocessing` and `Asyncio` are both approaches to concurrent programming

#### Multiprocessing (CPU Core Task):
- Nature of Tasks:
    1. Multiprocessing is suitable for CPU-bound tasks, which are tasks that 
       require significant computation or processing power.
    2. It involves running separate processes in parallel, each with its own 
       interpreter and memory space. so its bypasses the Global Interpreter Lock
- Concurrency Model:
    1. Achieves parallelism by executing tasks concurrently in separate processes.
- Use Cases:
    1. Intensive mathematical computations, simulations, data processing, and other
       tasks that heavily utilize the CPU.

for eg,
````python
from multiprocessing import Process

def square_numbers(numbers):
    for number in numbers:
        print('Square:', number * number)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    process = Process(target=square_numbers, args=(numbers,))
    process.start()
    process.join()

````

#### Asyncio (IO Task):

- Nature of Tasks:
    1. Asyncio is suitable for I/O-bound tasks, which are tasks that spend a 
       significant amount of time waiting for external resources such as 
       (e.g., network, file I/O).
    2. It achieves concurrency by efficiently switching between tasks during I/O 
       operations without blocking.
- Concurrency Model:
    1. Achieves concurrency by using an event loop to switch between tasks 
       when one is waiting for I/O.
- Use Cases:
    1. Web servers, network communication, web scraping, and other tasks where 
       waiting for external resources is a significant part of the workload.

For eg,
````python
import asyncio

async def print_numbers():
    for i in range(5):
        print('Number:', i)
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(print_numbers())
````

#### Conclusion
- Use `multiprocessing` for CPU-bound tasks that require parallel execution.
- Use `asyncio` for I/O-bound tasks where concurrency can be achieved by 
  efficiently switching between tasks during I/O operations.
- In practice, both approaches can be combined for scenarios where a mix of
  CPU-bound and I/O-bound tasks need to be handled efficiently in a single
  application.
- Multiprocessing works by creating separate processes (each with its own
  Interpreter and Global Interpreter Lock (GIL)
- Asyncio uses a single-threaded, single-process event loop to handle Python
  interpreter), so it bypasses the Global Interpreter Lock (GIL).
- Asyncio uses a single-threaded, single-process event loop to handle
  asynchronous I/O tasks without blocking.


-------------------------------------------------------------------------------------
### Q084 : Asyncio Module in Python;;

(Refer Example : dsa/basic-py/P038_Asyncio.py)

(Refer Study : https://realpython.com/async-io-python/)


#### Asynchronous Topics:
- `Threading` is a concurrent execution model whereby multiple threads take
  turns executing tasks. One process can contain multiple threads.
- `Coroutines` are computer program components that allow execution to be
  suspended and resumed, generalizing subroutines for cooperative multitasking.
- `Concurrency` is a slightly broader term than parallelism. It suggests that
  multiple tasks have the ability to run in an overlapping manner. (There’s a
  saying that concurrency does not imply parallelism.)


#### AsyncioIO:
- `Async IO` is not multithreading, nor is it multiprocessing. 
- `Async IO` is a single-threaded, single-process design: it uses cooperative
  multitasking, async IO gives a feeling of concurrency despite using a
  single thread in a single process. Coroutines (a central feature of async
  IO) can be scheduled concurrently, but they are not inherently concurrent.
- Asynchronous routines are able to “pause” while waiting on their ultimate
  result and let other routines run in the meantime.
- Asynchronous code, through the mechanism above, facilitates concurrent
  execution. To put it differently, asynchronous code gives the look and feel
  of concurrency.
- At the heart of async IO are coroutines. A coroutine is a specialized
  version of a Python generator function. A coroutine is a function that can
  suspend its execution before reaching return, and it can indirectly pass
  control to another coroutine for some time.


#### AsyncIO Usecase: 
- asyncio is better for IO-bound tasks. 
- asyncio is a library used for writing concurrent code using async/await
  syntax. It's useful when you have I/O-bound tasks (network requests, file
  operations, database queries) that would otherwise block execution.

- Unlike multithreading or multiprocessing, asyncio runs everything in a
  single thread using an event loop.
- While a CPU-bound task is characterized by the computer’s cores continually
  working hard from start to finish, an IO-bound job is dominated by a lot of
  waiting on input/output to complete.

#### Asyncio : Getting Hands Dirty

> 1. Understanding asyncio

- `asyncio` is a library used for writing concurrent code using async/await
  syntax. It's useful when you have I/O-bound tasks (network requests, file
  operations, database queries) that would otherwise block execution.

- Unlike multithreading or multiprocessing, asyncio runs everything in a
  single thread using an event loop.


> 2. Basic Syntax 

**(a) Define Async Basic Function:-**

````python
import asyncio 

async def main():
    print("Hello")
    asyncio.await(3)
    print("World")

asyncio.run(main())
````

**(b) Creating multiple independent tasks:-** 

````python
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(10)
    print("Task 1 completed")
    return (True, "All OK")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")
    return (True, "All OK")

async def main():
    result = await asyncio.gather(task1(), task2())  # Run both tasks concurrently
    print(f"result: ", result)

asyncio.run(main())

# output:
# Task 1 started
# Task 2 started
# Task 2 completed
# Task 1 completed
# result:  [(True, 'All OK'), (True, 'All OK')]

````

**(c) Event Loop and Tasks:-**

- The event loop runs async tasks and manages scheduling.
- asyncio.create_task() schedules tasks to run in the background.
- asyncio.gather() runs multiple coroutines concurrently.

````python
import asyncio

async def task(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} completed")

async def main():
    t1 = asyncio.create_task(task("Task A", 2))
    t2 = asyncio.create_task(task("Task B", 3))

    t1_resp = await t1  # Wait for Task A to finish
    t2_resp = await t2  # Wait for Task B to finish
    print(f"t1_resp: {t1_resp}, t2_resp: {t2_resp}")

    # or run task together using gather function;;
    # resp = await asyncio.gather(t1, t2)
    # print(f"resp: {resp}") 

asyncio.run(main())

````

**(d) Using async with HTTP Requests**

Use aiohttp instead of requests for non-blocking HTTP calls.

````python
import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://www.example.com"
    content = await fetch_url(url)
    print(content[:100])  # Print first 100 chars

asyncio.run(main())

````

**(e) Using async with Databases**

- If you're working with a database like PostgreSQL, use asyncpg

````python
import asyncpg
import asyncio

async def fetch_data():
    conn = await asyncpg.connect("postgresql://user:password@localhost/dbname")
    rows = await conn.fetch("SELECT * FROM users")
    await conn.close()
    return rows

async def main():
    data = await fetch_data()
    print(data)

asyncio.run(main())

````

**(f) When to Use asyncio?**

- When handling multiple I/O-bound operations (API calls, DB queries, file I/O).
- When building web servers (e.g., FastAPI, Sanic).
- When writing web scrapers that make multiple requests at once.

**(g) When not to use asyncio**

- When working with CPU-bound tasks (Use multiprocessing instead).
- When you need thread safety (Use threading module instead).

**(h) Debugging asyncio Code**


To enable debugging mode, run

````python
asyncio.run(main(), debug=True)

````

Or set environment variable:

````python
PYTHONASYNCIODEBUG=1 python script.py

````

**(i) Common Mistakes**

Calling `async` function without `await`

````python
import asyncio

async def foo():
    print("Hello")
    return 42

result = foo()  # ❌ This returns a coroutine, not a result

print(result)
# output 
# <coroutine object expl.<locals>.foo at 0x73b48b39eff0>


# FIX : USE await before calling async function;;
result = await foo()  # ✅ Now it executes the function

````

#### Asyncio :: Exmaple;;

In this we used two different methods which are asyncio methods which we later
attach to asyncio task using create_task, so as they are individual task we
would expect individual result at the end. That's why we are using gather() 
method to combined and push the method to process and later after execution 
asyncio return us with the result. 

We crafted one entry point main() which is also a asyncio method. 

```python
import asyncio
from random import choice

from selenium.webdriver.common.devtools.v113.debugger import resume

rt_flag = choice([True, False])

async def task1():
    result = []
    for i in range(2):
        waiting_time = 10
        wlcm_msg = "Task 1 | Loading Next Stage ..." if i != 0 else "Task 1 | Loading ..."
        print(wlcm_msg)
        await asyncio.sleep(waiting_time)
        t1_rslt = input(f"Executing Task(1): Iteration({i}): Enter Input: ")
        result.append((rt_flag, t1_rslt))
    return result

async def task2():
    result = []
    for i in range(1):
        waiting_time = 3
        wlcm_msg = "Task 2 | Loading Next Stage ..." if i != 0 else "Task 2 | Loading ..."
        print(wlcm_msg)
        await asyncio.sleep(waiting_time)
        t2_rslt = input(f"Executing Task(2): Iteration({i}): Enter Input: ")
        result.append((rt_flag, t2_rslt))
    return result

async def main():
    # Create tasks
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    # Wait for both tasks to complete
    result = await asyncio.gather(t1, t2)
    print("result: ", result)

# Run the event loop
asyncio.run(main())

# output :
[//]: # (Task 1 | Loading ...)
[//]: # (Task 2 | Loading ...)
[//]: # (Executing Task&#40;2&#41;: Iteration&#40;0&#41;: Enter Input: 1)
[//]: # (Executing Task&#40;1&#41;: Iteration&#40;0&#41;: Enter Input: 3)
[//]: # (Task 1 | Loading Next Stage ...)
[//]: # (Executing Task&#40;1&#41;: Iteration&#40;1&#41;: Enter Input: 10)
[//]: # (result:  [[&#40;False, '3'&#41;, &#40;False, '10'&#41;], [&#40;False, '1'&#41;]])
```


-------------------------------------------------------------------------------------
### Q083 : Method Resolution Order in Python;;

(refer source code: python-expl/cls-composiiton/with-inheritance/v3)

`Method Resolution Order(MRO)` signifies the way in which a programming language
resolves a method or attribute. 

Python Support Multiple Inheritance in which a single child class can derive
from mulitple parent class. 
 
MRO or Method Resolution Order defines the order in which the base classes are
searched when executing a method. 

First, the method or attribute is searched within a class and then it follows
the order we specified while inheriting. This order is also called Linearization 
of a class and set of rules are called MRO(Method Resolution Order). 

While inheriting from another class, the interpreter needs a way to resolve
the methods that are being called via an instance. Thus we need the method
resolution order. For Example 

> Python Syntax: TemporarySecretary.__mro__

for eg,
````python
class Employee:
    def __init__(self, eid, name):
        self.id = eid
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self,  eid, name, salary):
        super().__init__(eid, name)
        self.salary = salary

    def calculate_payroll(self):
        return self.salary


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"Secretary: {self.name}, handled billing for {hours} hours")


class TemporarySecretary(Secretary):
    """
    final resolution:- MRO Method Resolution Order
    MRO for class TemporarySecretary(Secretary):
        <class 'TemporarySecretary'>,
        <class 'Secretary'>,
        <class 'SalaryEmployee'>,
        <class 'Employee'>,
        <class 'object'>
    )
    """
    def __init__(self, eid, name, hour, rate):
        # Need to control the constructor calling as well;;
        HourlyEmployee.__init__(self, eid, name, hour, rate)

    def calculate_payroll(self):
        # Needs to override this function as well;;
        return HourlyEmployee.calculate_payroll(self)


if __name__ == "__main__":
    shreya = TemporarySecretary(1005, "Janvi", 100, 70)
````


-------------------------------------------------------------------------------------
### Q082 : UDP Socket Programming in Python;;

#### USER DATAGRAM PROTOCOL:
-  UDP is the abbreviation of User Datagram Protocol. UDP makes use of
   Internet Protocol of the TCP/IP suit. In communications using UDP, a
   client program sends a message packet to a destination server wherein the
   destination server also runs on UDP.

#### Properties of UDP:
-  The UDP does not provide guaranteed delivery of message packets. If for
   some issue in a network if a packet is lost it could be lost forever.
-  Since there is no guarantee of assured delivery of messages, UDP is
   considered an unreliable protocol.
-  The underlying mechanisms that implement UDP involve no connection-based
   communication. There is no streaming of data between a UDP server or and
   an UDP Client.
-  An UDP client can send "n" number of distinct packets to an UDP server and
   it could also receive "n" number of distinct packets as replies from the
   UDP server.
-  Since UDP is connectionless protocol the overhead involved in UDP is less
   compared to a connection based protocol like TCP.

For eg,
````python
#--------------------- CLIENT.py --------------------#

import socket


def run_udp_server():
    # udp client constants;;
    local_ip = '127.0.0.1'
    local_port = 2001
    buffer_size = 1024
    server_ip = ("127.0.0.1", 2002)

    # create udp socket;;
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # bind address with ip;;
    udp_client_socket.bind((local_ip, local_port))

    print("UDP Client is running ...")

    # listen to the port;;
    while(True):
        # convert ascii text to byte datagram;;
        message = input("Client Saying : ")
        enc_message = str.encode(message)

        # client will send message;;
        udp_client_socket.sendto(enc_message, server_ip)

        # message received;;
        raw_message = udp_client_socket.recvfrom(buffer_size)
        message  = raw_message[0]
        print(f"Server reply: ", message.decode())

        # terminate operation;;
        flag = input("Continue (Y or N): ")

        # terminate proce
        if flag.lower() == ['y', 'yes', 'n', 'no']:
            print("Server Terminated by client !")
            break


if __name__ == "__main__":
    print("Starting UDP Server...")
    run_udp_server()
    print("Terminating UDP Server...")


#--------------------- SERVER.py --------------------#

import socket


def run_udp_server():
    # udp client constants;;
    local_ip = '127.0.0.1'
    local_port = 2002
    buffer_size = 1024

    # create udp socket;;
    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # bind address with ip;;
    udp_server_socket.bind((local_ip, local_port))

    print("UDP Server is running ....")

    # listen to the port;;
    while(True):
        # message received;;
        raw_message = udp_server_socket.recvfrom(buffer_size)
        message, client_ip = raw_message
        print(f"Client saying: ", message.decode())

        # convert ascii to byte datagram;;
        message = input("Server Reply: ")
        enc_message = str.encode(message)

        # client will send message;;
        udp_server_socket.sendto(enc_message, client_ip)


if __name__ == "__main__":
    print("Starting UDP Server...")
    run_udp_server()
    print("Terminating UDP Server...")
````


-------------------------------------------------------------------------------------
### Q081 : Multiprocessing Lock And Pool

#### Multiprocessing Pool

-  Multiprocesing Pool object which offers a convenient means of parallelizing
   the execution of a function across multiple input values, distributing the
   input data across processes(data parallelism).

-  for eg, (ref P056 file)

````python
from multiprocessing import Pool
from time import time

def func(x):
   sum = 0
   for x in range(1000):
      sum += x
   return sum

if __name__ == "__main__":
   p1 = Pool()
   result = p1.map(func, range(lc))
````

#### Multiprocessing Lock

-  The most commonly used mechanism for ensuring mutual exclusion is a mutual
   exclusion lock or mutex, or simply lock. A mutex is a special type of
   object that has support in the underlying hardware. The basic idea is that
   each critical section is protected by a lock.

-  for eg, (refer basic-py -> P055 file)

````python
# Basic Snippet
# create a lock
lock = multiprocessing.Lock()
# acquire the lock
lock.acquire()
# ...
# release the lock
lock.release()
````


-------------------------------------------------------------------------------------
### Q080 : SortedContainers in Python;;

- `Sorted Containers` is an Apache2 licensed sorted collections library, written
in pure-Python, and fast as C-extensions.

- Installation: `$ pip install sortedcontainers`

- Features:
  1) Pure-Python
  2) Fully documented
  3) Benchmark comparison (alternatives, runtimes, load-factors
  4) Performance (often faster than C implementations)
  5) Compatible API (nearly identical to popular blist and rbtree modules)
  6) Feature-rich (e.g. get the five largest keys in a sorted dict: d.iloc[-5:])
  7) Pragmatic design (e.g. SortedSet is a Python set with a SortedList index)

- Types Of Containers
  1) SortedList : It is used to add list in sorted containers.
  2) SortedDict : It is used to add dict in sorted containers.
  3) SortedSet : It is used to add set in sorted containers.

#### SortedList :-

-> Methods : add(), discard(), update(), clear()

-> Description :

1) add(value) : A function that takes one element as parameter and inserts it
into the list by maintaining sorted order. 
- Runtime Complexity: `O(log(n))`

2) discard(value) : Remove value from sorted list if it is a member. If value
is not a member, do nothing. 
- Runtime complexity: `O(log(n))`.

3) update(value) : A function that takes an iterable as input and updates the
SortedList adding all the values from the iterable.
- Runtime complexity: `O(k*log(n))`.

4) clear() : Remove all values from sorted list. 
- Runtime complexity: `O(n)`.

For eg, 
````python
from sortedcontainers import SortedList, SortedDict, SortedSet

sl = SortedList()                                                                                

# Add methods;;
sl.add(110)                                                                                      
sl.add(10)                                                                                       
sl.add(1)                                                                                        
print(sl) # 1,10, 110

# Update Methods
s2 = SortedList()
s2.update(sl)

# OUTPUT : 
# Traceback Error, because
# you can't add sortedlist directly to any already sortedcontainer.

Error: TypeError: '<' not supported between instances of 'list' and 'int'

# Update without error
element = [10,100, 80, 90]
s3 = SortedList()
s3.update(element)

# Output: It will work;;
````                                                                                                  

###--- SortedSet :-

-> Methods : add(value), discard(value), clear()

-> Description :

1) add(value) : A function that takes one element as parameter and inserts it
into the set by maintaining sorted order. 
- Runtime Complexity: O(log(n))

2) discard(value): Remove value from sorted set if it is a member. If value is
not a member, do nothing. 
- Runtime complexity: O(log(n))

3) clear(): Remove all values from sorted set. 
- Runtime complexity: O(n)

for eg, 
````python
sorted_set = SortedSet([1, 1, 2, 3, 4])
for i in range(5, 0, -1):
    sorted_set.add(i)
  
print(sorted_set)
# Output: SortedSet([1, 2, 3, 4, 5]
````

###--- SortedDict :-

-> Sorted dict is a sorted mutable mapping in which keys are maintained in
   sorted order.

-> Sorted dict inherits from dict to store items and maintains a sorted list
   of keys. 

-> Sorted dict keys must be hashable and comparable.

-> Description :

1) setdefault(key, default = None) : Return value for item identified by key
in sorted dict. If key is in the sorted dict then return its value. If key is
not in the sorted dict then insert key with value default and return
default. 
- Runtime Complexity: O(log(n))

2) clear(): Remove all values from sorted dict. 
- Runtime complexity: O(n)

3) get(key, default): Return the value for key if key is in the dictionary, else default.
- Runtime Complexity: O(1)

-> for eg,
````python
from sortedcontainers import SortedDict 

sd = SortedDict()                                                                            
sd['d'] = 3                                                                                  
sd['a'] = 2                                                                                  
sd['c'] = 1000

print(sd)
# Output: SortedDict({'a':2, 'c':1000, 'd':3})

sd.setdefault('c', 20)
# Output: SortedDict({'a':2, 'c':20, 'd':3})

sd.get('c')
# Output: 20
````


-------------------------------------------------------------------------------------
### Q079 : Enum in Python;;

`Enumerations` in Python are implemented by using the module named “enum“.

`Enumerations` are created using classes. Enums have names and values associated
with them.

Properties of enum:
1) Enums can be displayed as string or repr. 
2) Enums can be checked for their types using type(). 
3) The “name” keyword is used to display the name of the enum member.

for eg,
````python
from enum import Enum

class Season(Enum):
   spring = 1
   winter = 2
   autumn = 3
   summer_x = 4
   summer_y = 4

print("key:", Season.spring)  # key: Season.spring
print("key: ", Season['summer_x'])  # key:  Season.summer_x
print("value: ", Season['summer_y'].value)   # value:  4
print("type: ", type(Season.spring))   # type:  <enum 'Season'>
print("repr: ", repr(Season.spring))   # repr:  <Season.spring: 1>

season_list = list(Season)
print("list in season: ", season_list) 
# OUTPUT: 
list in season:  [
   <Season.spring: 1>, 
   <Season.winter: 2>, 
   <Season.autumn: 3>, 
   <Season.summer_x: 4>
]

print("Season Obj: ", Season) # Season Obj:  <enum 'Season'>

print("access key based on values : ", Season(4).name)
# OUTPUT: 
# access key based on values :  summer_x

print("list in Season : ", (Season))
# OUTPUT:
# list in Season :  <enum 'Season'>

# Looping Season Values;;
for season in Season:
   print(season.name, "<->", season.value)

# Output
spring <-> 1
winter <-> 2
autumn <-> 3
summer_x <-> 4
````


-------------------------------------------------------------------------------------
### Q078 : Python Multithreading;;

#### Multithreading in Python 

-  `Multithreading`, in its simplest form, is an approach for carrying out many
   threads of operation simultaneously. Each thread operates independently
   from the others and has the capacity to run unique sections of the
   software program simultaneously.

#### Why Python Lack Support For Multithreading 

-  Python's lack of multithreading instruction is due to the Global
   Interpreter Lock (GIL). The GIL is a mechanism that guarantees only one
   thread can execute Python bytecode at a time.

-  Even though numerous threads can exist in a Python process, they are
   incapable of executing Python code concurrently. This is because the GIL
   restricts the interpreter to a single thread, which prevents other threads
   from executing Python code.

-  The Global Interpreter Lock exists because Python adopts a reference-counting 
   memory management model, which deletes objects when their reference count 
   reaches zero.

-  The GIL guarantees that the reference count is accurate, even when multiple
   threads are simultaneously accessing the same object. If the GIL were not
   in place, there would be race conditions whereby two threads may attempt
   to modify the reference count of the same object concurrently, resulting
   in memory corruption.

-  Python used to be designed to be a high-level, user-friendly, and readable
   language. Python lacks many intricate and low-level elements seen in other
   programming languages as a result. 

-  Although it is a powerful tool, multithreading is now not required for all
   Python applications. The single-threaded Python paradigm typically serves
   the meaning well.


-------------------------------------------------------------------------------------
### Q077 : Python Crontab Job function;;

-  CronTab is the linux library which is used to run the any script in as a
   background job.

-  Cronjob alaway run as per the UTC time slot, you make sure to verify your
   utc time before setting any job. 

-  You can use, `$`: date linux command to check machine local utc time slot.

-  Syntax for Configuration of crontab is here 

````
(~ you can also use * for arg1 to arg5 only)

(Time Format is 24 hr format)

arg1: minute (m), 
arg2: hour (h), 
arg3: day of month (dom), 
arg4: month (mon),
arg5: day of week (dow) or use '*' in these fields (for 'any').
arg6: your command which need to run.
````

- Consider there is a dummy file named, test.py

````
23 7 * * * 
source /home/ec2-user/.virtualenvs/api/bin/activate; 
cd /home/ec2-user/api; 
python -m scripts.test >> ~/temp/log

Here, the commands is in the sequence like 
cmd1 : Activating the virtual env for python
cmd2 : Traverse to the project director
cmd3 : Run the python script file, test.py
cmd4 : Logs redirection for verification.
````

`NOTE` : All the commands must be separated with semicolon and order is
important. Otherwise flow will break. Keep this in mind.


-------------------------------------------------------------------------------------
### Q076 : Python Celery function;;

#### USAGE 1 : Definations;;

> Celery :: Basics;

Celery is an open-source Python library which is used to run the tasks
asynchronously. It is a task queue that holds the tasks and distributes them
to the workers in a proper manner. Celery introduces the various
message brokers such as RabbitMQ and Redis.

The main advantage of Celery is that our application can continue to respond
to client requests. So the end-users don't have to wait unnecessarily.

> Celery :: Architecture;

Celery interacts via messages, normally broker works as a mediate between
clients and workers. The inward working of the Celery affirms as Producer and
Consumer pattern. Celery has the three chief elements at the high level.

`Producers` - Producers are 'web nodes' that manages the web requests. When the
application is processing, tasks are assigned to the Celery means forced into
the task queue.

`Consumer` - Consumers are the 'worker nodes' that monitors the queue head, the
workers take the tasks and perform it. Workers can perform various tasks as
well; hence they can also behave as producers.

`Queue` - It is basically a message broker which acts as a bridge between
producer and consumer. It essentially passes messages between web application
and the Celery workers. Celery has wide support for RabbitMQ and Redis, also
helps Zookeeper, Amazon SQS but with confined abilities.

#### Features;

- Open-source Library
- Straight Forward Installation 
- Scheduling
- Broker Support
- Integration with Web Frameworks
- Fast
- Works-flow

#### USAGE 2 : Installation;

- Install using pip :- `$ pip install celery`

- Celery Configuration :-
  - CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
  - CELERY_ACCEPT_CONTENT = ['application/json']
  - CELERY_TASK_SERIALIZER = 'json'
  - CELERY_RESULT_SERIALIZER = 'json'
  - CELERY_TIMEZONE = 'Asia/Kolkata' 

#### About BROKER :

Brokers are separate services that enable applications, systems, and services
to communicate and share information. We assign tasks to workers via a
message queue. A message queue is a first-in, first-out data structure which
means the message is stored at first place will be executed first


-------------------------------------------------------------------------------------
### Q075 : Python rsplit function;;

The `rsplit()` method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split () method.

> SYNTAX : string.rsplit(separator, maxsplit)

- separator :  Optional. Act as Delimiter with default is whitespace.
- maxsplit  :  Optional. Specifies how many splits to do. Default -1.
for eg, maxsplit is 2, output will contain 3 index [ind_0, ind_1, ind_2]

#### USAGE : rsplit()

for eg,
````python
txt = "app.worker.transaction.transact_via_bse"

x = txt.rsplit(".")
print("x : ", x)    # x :  ['app', 'worker', 'transaction', 'transact_via_bse']

y = txt.split(".")
print("y : ", y)    # y :  ['app', 'worker', 'transaction', 'transact_via_bse']

a = txt.rsplit(".", 1)
print("a : ", a)    # a :  ['app.worker.transaction', 'transact_via_bse']

b = txt.rsplit(".", 2)
print("b : ", b)    # b :  ['app.worker', 'transaction', 'transact_via_bse']
````


-------------------------------------------------------------------------------------
### Q074 : Python Unittest Mock Library;

#### Refer : root/basic-python/advance/P001_Unittest_mock_library.py; 

#### Refer : https://realpython.com/python-mock-library/#lazy-attributes-and-methods

####  USAGE 1: Definations;;

A mock object substitutes and imitates a real object within a testing
environment. It is a versatile and powerful tool for improving the quality of
your tests.

One reason to use Python mock objects is to control your code’s behavior
during testing.

For example, if your code makes HTTP requests to external services, then your
tests execute predictably only so far as the services are behaving as you
expected. Sometimes, a temporary change in the behavior of these external
services can cause intermittent failures within your test suite.

Because of this, it would be better for you to test your code in a controlled
environment. Replacing the actual request with a mock object would allow you
to simulate external service outages and successful responses in a
predictable way.

#### USAGE 2: Installation;;

Installation :- `$ pip install mock`

`unittest.mock` provides a class called Mock which you will use to imitate
real objects in your codebase

The library also provides a function, called `patch()`, which replaces the real
objects in your code with Mock instances. You can use `patch()` as either a
decorator or a context manager, giving you control over the scope in which
the object will be mocked. Once the designated scope exits, `patch()` will
clean up your code by replacing the mocked objects with their original
counterparts.

Finally, `unittest.mock` provides solutions for some of the issues inherent in
mocking objects.

#### USAGE 3: Directly using Mock Object;

`unittest.mock` offers a base class for mocking objects called Mock. The use
cases for Mock are practically limitless because Mock is so flexible.

for eg,
````python
from unittest.mock import Mock

mock = Mock()   # <Mock id='4561344720'>
````

Now, you are able to substitute an object in your code with your new Mock. You
can do this by passing it as an argument to a function or by redefining
another object:

````python
# Pass mock as an argument to do_something()
do_something(mock)

# Patch the json library
json = mock
````

When you substitute an object in your code, the Mock must look like the real
object it is replacing. Otherwise, your code will not be able to use the Mock
in place of the original object.

#### USAGE 4: Lazy Attributes and Methods

A Mock must simulate any object that it replaces. To achieve such flexibility,
it creates its attributes when you access them:

for eg,
````python
mock.some_attribute
<Mock name='mock.some_attribute' id='4394778696'>

mock.do_something()
<Mock name='mock.do_something()' id='4394778920'>

# Since Mock can create arbitrary attributes on the fly, 
# it is suitable to replace any object.

json = Mock()
json.dumps()
<Mock name='mock.dumps()' id='4392249776'>
````

#### USAGE 5: mocking with patch

for eg, 
````python
@patch('app.service.branch.requests.post')
def test_create_non_customer_campaign_through_admin(mock_request_post, client, db):
    params = {
        "is_customer": False,
        "name": "Indus OS campaign",
        "description": "Co-branded standee campaign",
        "campaign_code": "indusos",
        "start_time": "2099-07-04",
        "end_time": "3099-07-04",
        "payable_in": "coupon",
        "trigger_event": "first_transaction"
    }
    payload = {
        "action": "create_campaign",
        "params": params
    }
    response = {
        'ok' : True,
        'status_code' : 202,
        'json.return_value' : {
            'url' : f"https://app-bse.sqrrl.in/campaign/{params.get('campaign_code', 'testing')}"
        }
    }
    mock_request_post.return_value = Mock(name="mock response", **response)
    res = initiate_admin_action(client, payload)
    assert res.status_code < 300
````


-------------------------------------------------------------------------------------
### Q073 : Python urllib method urljoin();;

The best way (for me) to think of this is the first argument, base is like the
page you are on in your browser. The second argument url is the href of an
anchor on that page. The result is the final url to which you will be
directed should you click.

urljoin('some', 'thing')           # 'thing'

This one makes sense given my description. Though one would hope base includes
a scheme and domain.

urljoin('http://some', 'thing')     # 'http://some/thing'

If you are on a `vhost` some, and there is an anchor like <a href='thing'>Foo</a>, 
then the link will take you to `http://some/thing`
````
urljoin('http://some/more', 'thing')    # Output: 'http://some/thing'
````

We are on `some/more` here, so a relative link of thing will take us to
`/some/thing`

````python
urljoin('http://some/more/', 'thing') 

# just a tad / after 'more'
'http://some/more/thing'
````

Here, we aren't on `some/more`, we are on `some/more/` which is different. Now,
our relative link will take us to some/more/thing

````python
urljoin('http://some/more/', '/thing')
'http://some/thing'

urljoin('http://some/parent_dir_1/parent_dir_2/', '/child_dir_1')
# Output :: 'http://some/child_dir_1'

# here, /child_dir_1 is considered as new independent root directory;

urljoin('http://some/parent_dir_1/parent_dir_2/', 'child_dir_1')
# Output :: 'http://some/parent_dir_1/parent_dir_2/child_dir_1'

here, child_dir_1 is acting as sub directory of parent_dir_2;

urljoin('http://some/parent_dir_1/parent_dir_2', 'child_dir_1')
# Output :: 'http://some/parent_dir_1/child_dir_1'
````

Here, notice the parent_dir_2 is the sub-directory of the parent_dir_1
then when using accessing child_dir_1. It will replace the parent_dir_2 
completely and replace it with child_dir_1. 
Here "parent_dir_2" and "child_dir_2" is considered as a sub-directory 
of "parent_dir_1" folder.

And lastly. 

If on some/more/ and the href is to /thing, you will be linked to some/thing.


-------------------------------------------------------------------------------------
### Q072 : Python class inherits from objects;;

> PYTHON 2.X : Usage as per Parent object class; 

In Python 2.x (from 2.2 onwards) there's two styles of defining classes
depending on the presence or absence of object as a base-class

1) Classic Style Classes : They don't have object as a base class.

for eg, 
````python
# Example 1
class ClassicSpam:      # no base class
	pass

print(ClassicSpam.__bases__()) 	
# Result : 
AttributeError: 'builtin_function_or_method' object has no attribute '__bases__'
````

2) NEW Style : They have directly or indirectly, object as a base class.

for eg, 
````python
# Example 1
Class NewStyleClass_v1(object):
	pass

print(NewStyleClass_v1.__base__)	# Result : (<type 'object'>)

# Example 2 
Class NewStyleClass_v2(int):
	pass

print(NewStyleClass_v2.__base__)		# Result : (<type 'int'>)
````

> PYTHON 3.X : Usage as per Parent Object Class;

In Python 3, things are simplified. Only new-style classes exist (referred to
plainly as classes) so, the only difference in adding object is requiring you
to type in 8 more characters.

for eg,
````python
# Example 1;
class ClassicSpam:
    pass

It is completely equivalent to this,

# Example 2;
class NewSpam(object):
     pass

# Example 3;
class Spam():
    pass

# All have object in their __bases__ object.
[object in cls.__bases__ for cls in {Spam, NewSpam, ClassicSpam}]
[True, True, True]
````

#### Advantage of Python Object Class

Without a doubt, when writing a class you'll always want to go for new-style
classes. The perks of doing so are numerous, to list some of them:

Support for descriptors. Specifically, the following constructs are made
possible with descriptors:

- `classmethod`: A method that receives the class as an implicit argument
  instead of the instance. 

- `staticmethod`: A method that does not receive the implicit argument self as
  a first argument. properties with property: Create functions for managing
  the getting, setting and deleting of an attribute.

- `__slots__`: Saves memory consumptions of a class and also results in faster
  attribute access. Of course, it does impose limitations. The __new__ static
  method: lets you customize how new class instances are created.

- `Method resolution order` (MRO): in what order the base classes of a class
  will be searched when trying to resolve which method to call.

Related to MRO, super calls. Also see, super() considered super.

If you don't inherit from object, forget these. A more exhaustive description
of the previous bullet points along with other perks of "new" style classes
can be found here.

One of the downsides of new-style classes is that the class itself is more
memory demanding. Unless you're creating many class objects, though, I doubt
this would be an issue and it's a negative sinking in a sea of positives.


-------------------------------------------------------------------------------------
### Q071 : Multitreading Vs Multiprocessing

NOTE : Here address memory is referred to those memory where a program store
variable, argument, control statement etc.

#### Multithreading:

- Multithreading is when a lot of threads of a single process is working
  simultaneously.

- Multiple thread shares the same memory address and heap memory.

- Multiple thread do have their own code and task and their different stack
  memory

- Multiple thread can access global variable simultaneously and that can cause
  a conflict. Becuase any thread can access it and change the value which may
  cause inaccurate result.

- Threads are light weight.

#### Multiprocessing:-

- Multiprocessing is when a lot of multiple process are executing
  simultaneously.

- Multiprocess have different memory address but they can communicate with
  other process using the File, Shared Memory, Message Pipe.

- Process are heavy weighted

- Running Multiprocess is good because one process error doesnt induce error
  flow in another process.


-------------------------------------------------------------------------------------
### Q070 : Different usages when add list to set or set to set;

Mention below, different usage of add or updating list or set to the main set

for eg, 
````python
a = set()

#--- CASE 1: WHEN ADDING LIST TO SET A;

a.add([12, 0])
a.add([13, 1])
a.add([14, 2])

print(a)	# Traceback: TypeError: unhashable type: 'list'

NOTE: Throw Error Saying, 
because set not able to hashed the independent list alone 

NOTE : Countermeasure EXPL

a.add(0)
a.add(1)
a.add(2)

print(a)

# NOTE: WORKS FINE;
{0, 1, 2}

#--- CASE 2 : WHEN UPDATING THE SAME LIST TO A;

a.update([12, 0])
a.update([13, 1])
a.update([14, 2])

print(a)

# NOTE : Notice the list not stored as given 
{0, 1, 2, 12, 13, 14}

#--- CASE 3 : WHEN ADD THE SAME DATA AS TUPLE INSTEAD OF LIST;

a.add((12,0))
a.add((13,1))
a.add((14,2))

print(a)

# NOTE : Notice result format;
{(12, 0), (14, 2), (13, 1)}

#--- CASE 4 : WHEN UPDATE THE SAME LIST DATA AS TUPLE;
pdate((13,1))
a.update((14,2))
a.update((12,0))
a.update((13,1))
a.update((14,2))

print(a)

# NOTE : Notice result format;
{0, 1, 2, 12, 13, 14}
````

#### Difference in Python Set Method Add() Vs Update();;

> **Python Set :: Add()**

- The add method is used to add a `single element` to a set.
- If the element is already present in the set, the set remains unchanged.
- The syntax is `set.add(element)`

for eg,
````pythonpython
# Case 1: Adding list directly;;
a = set()
data = [1,2]
a.add(data) # Traceback: list not hashable;;

# Case 2: Adding hashed data;;
a = set()
data = (1,2)
a.add(data) # {(1,2)}

data = {'a': 1, 'b': 2}
a.add(data) # Traceback: dictionary not hashable;;

# Case 3: Add not hashed data using iteration;;
a = set()
data = [1,2]
a.add(data[0])  # {1}
````

> Python Set :: Update();;

- The update method is used to add `multiple elements` (iterable) to a set.
- It takes an iterable as an argument and adds its elements to the set.
- If any elements in the iterable are already present in the set, they are ignored.
- The syntax is `set.update(iterable)`.

for eg,
````python
# Case 1: Update list directly;;
a = set()
data = [1,2]
a.update(data) # {1,2}

# Case 2: Updating Hashable;;
a = set()
data = (1,2)
a.update(data)  # {1, 2}

data = {'a': 1, 'b':2}
a.update(data)  # {1, 2,'a','b'}

# Case 3: Adding Single Value
a = set()
data = (1,2)
a.update(data[0])   # {1}
````


-------------------------------------------------------------------------------------
### Q069 : Time Delta (timedelta) in python;;

A timedelta represents a duration which is the difference between two dates,
time, or datetime instances, to the microsecond resolution.

The Timedelta class available in Python’s datetime module. Use the timedelta
to add or subtract weeks, days, hours, minutes, seconds, microseconds, and
milliseconds from a given date and time.

#### TIMEDELTA :: ATTRIBUTE

- timedelta.days :: Returns days from timedelta
- timedelta.microseconds :: Returns microseconds from timedelta
- timedelta.seconds :: Returns seconds from timedelta                 
- timedelta.max :: Returns the maximum positive timedelta value,
                   it will be datetime.timedelta(999999999, 86399, 999999)  
- timedelta.min :: Returns the most negative timedelta value and its value
                   is datetime.timedelta(-999999999)
- timedelta.resolution :: Return the smallest possible difference between
                          two nonequal timedelta objects is 1 microsecond.         
- timedelta.total_seconds() :: Returns total seconds in the duration                    


#### USAGE 1: Basic Imports
for eg,
````python
from datetime import timedelta
from datetime import datetime                                     
                                                               
# Given datetime                                                  
current_date = datetime.now()                                     
x_date_time = datetime(                                           
year=2020, month=3, day=21, hour=12, minute=30                  
)

# Difference between two dates, Get timedelta
timedelta = current_date - x_date_time                            
                                                               
print(timedelta)                                                  
print(type(timedelta))                                            
                                                               
# output:                                                         
# 469 days, 20:39:07.830124                                         
# <class 'datetime.timedelta'>                                      
````

#### USAGE 2: Calculate Future Datetime
for eg,
````python
from datetime import datetime, timedelta                          
                                                               
current_date = datetime.now()                                     
print('Given Date:', current_date)                                
                                                               
# add 4 weeks in given date                                       
new_date = current_date + timedelta(weeks=4)                      
print('Future Date:', new_date)                                   
                                                               
# OUTPUT                                                          
# Given Date: 2021-07-04 05:41:46.328154                            
# Future Date: 2021-08-01 05:41:46.328154
````

#### USAGE 3: Features
for eg,
````python
from datetime import datetime                                            
                                                                      
d1 = datetime(year=2020, month=3, day=21, hour=12, minute=30)            
d2 = datetime(year=2021, month=1, day=12, hour=18, minute=15)            
                                                                      
# Get timedelta by subtracting two dates                                 
td = d2 - d1                                                             
                                                                      
# access timedelta attributes                                            
print("Days:", td.days)   # Days: 297                                    
print("Microseconds:", td.microseconds) # Microseconds: 0                
print("seconds:", td.seconds) # seconds: 20700                           
print("Max:", td.max) # Max: 999999999 days, 23:59:59.999999             
print("Min:", td.min)  # Min: -999999999 days, 0:00:00                   
print("Resolution:", td.resolution) # Resolution: 0:00:00.000001                               
print("Total Seconds:", td.total_seconds() # Total Seconds: 25681500.0                       
````


-------------------------------------------------------------------------------------
### Q068 : Relative Delta (relativedelta)in Python;;

Relative delta is a python library used to calculate the date relatively from
a given expected date.

It falls under the `dateutil.realtivedelta` package library.

####  USAGE 1: Params of relativedelta;;
for eg,
````python
from dateutil.relativedelta import relativedelta                             
                                                                             
dt=relativedelta(                                                               
    year=2021,
    month=1,
    day=1,
    hour=23,
    minute=56,
    second=57,
    microsecond=324534         
)                     
                                                         
print(dt)                                                                       
print(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.microsecond)       
                                                                              
# outputs                                                                       
# relativedelta(
#     year=2021, 
#     month=1, 
#     day=1, 
#     hour=23, 
#     minute=56, 
#     second=57, 
#     microsecond=324534 
# )                                                                              
# 2021 1 1 23 56 57 324534        
````

#### USAGE 2: Difference day vs days;;

- `day` : reset the day counter to 1 of that month.
- `days` : adds day relatively for the given today date.

for eg,

````python
from dateutil.relativedelta import relativedelta                                
from datetime import date                                                       
                                                                             
dt=date.today()  # today is 2019-09-23                                          
                                                                             
# Adding one day to today                                                       
print(dt + relativedelta(days=1))  # 2019-09-24                                 
                                                                             
# 1st day of the month                                                          
print(dt + relativedelta(day=1))  # 2019-09-01                                  
````

#### USAGE 3: Difference months vs month;;

- `month` : reset the month counter to the 1 of the year i.e, january.
- `months` : add month relatively to the given today date.

for eg,
````python
from dateutil.relativedelta import relativedelta                                
from datetime import date                                                       
                                                                             
dt=date.today()  # today is 2019-09-23                                          
                                                                             
# Adding one month to today                                                     
print(dt + relativedelta(month=1))  # 2019-01-23                                
                                                                             
# 1st month of the year                                                         
print(dt + relativedelta(months=1))  # 2019-10-23                               
````

#### USAGE 4: Difference years vs year;;

- `year` : reset the year counter to the 0001 of the year.
- `years` : add year relatively to the given today date.

for eg,
````python
from dateutil.relativedelta import relativedelta                                
from datetime import date                                                       
                                                                             
dt=date.today()  # today is 2019-09-23                                          
                                                                             
# Adding one month to today                                                     
print(dt + relativedelta(year=1))  # 0001-10-24                                 
                                                                             
# 1st month of the year                                                         
print(dt + relativedelta(years=1))  # 2020-01-24                                
````

#### USAGE 5: Age Calculation using RealtiveDelta;;

for eg,
````python
from dateutil.relativedelta import relativedelta                                
from datetime import date                                                       
                                                                             
dob = date(1997,1,5)    # date of birth;                                        
today = date.today()    # 28/12/2022                                            
                                                                             
cur_date = relativedelta(today, dob)                                            
print(cur_date)         # relativedelta(years=+25, months=+11, days=+23)        
print(cur_date.years)   # 25                                                    
````

#### USAGE 6: RelativeDelta adding sequence;;

for eg,
````python
from dateutil.relativedelta import relativedelta                                                  
from dateutil.rrule import MO, TU, WE, TH, FR, SA, SU
from datetime import date

dt=date.today()  # today is 2019-09-22                                          
                                                                             
# 2nd Monday from today                                                         
print(dt + relativedelta(weekday=MO(2)))  # 2019-09-30

print(dt + relativedelta(weekday=MO(2)))  # 2019-09-30                          
                                                                             
# 2nd Monday of present Month                                                   
print(dt + relativedelta(day=1,weekday=MO(2)))  # 2019-09-09
                                                                                                        
# Next Sunday from TODAYS                                                       
print(dt + relativedelta(weekday=SU(+1)))  # 2019-09-22                    
                                                                             
# As today is sunday there is no difference with SU(+1) or SU(-1)               
print(dt + relativedelta(weekday=SU(-1)))  # 2019-09-22                         
                                                                             
# previous 2nd Tuesday                                                          
print(dt + relativedelta(weekday=TU(-2)))   # 2019-09-10                        
````


-------------------------------------------------------------------------------------
### Q067 : Sort and Reverse Dictionary by value;;

Dictionary can be directory sorted using the sorted pre-defined function
in the python library.

for eg,
````python
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Sorting the dictionary using the key;;
sort_by_key = dict(sorted(x.items(), key=lambda item:item[0]))

# Sort dictionary by using the value;
sort_by_value = dict(sorted(x.items(), key=lambda item: item[1]))

# Sort the dictionary by value in decreasing order;;
reverse_sort_by_value = dict(sorted(x.items(), reverse=True, key=lambda item: item[1])

print("sort_by_key:", sort_by_key)        # {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
print("sort_by_value:", sort_by_value)    # {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
print(reverse_sort_by_value)              # {4: 3, 3: 4, 2: 1, 1: 2, 0: 0}
````


-------------------------------------------------------------------------------------
### Q066 : Iterators Workflow in Python;;

Iterators are objects that allow us to compute and fetch one value at a time
from a sequence. They help us save memory and computation by not calculating
the results for the entire sequence, but only for the next one.

We can convert any sequence such as list, tuple, dict, and set into an
iterative object using iter(). 

To fetch the next value we can use the next() function as shown below.

#### USAGE 1 : ITERATOR BASIC;;
````python
def example1():
    cartoons = ['Tom and Jerry', 'Shin Chan', 'Doraemon', 'Ninja Hatodi', 'Hage Maru']

    cartoon = iter(cartoons)
    
    print("Generator Object :", cartoon)
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))
    print("next cartoon :", next(cartoon))

if __name__ == "__main__":
    example1()

# OUTPUT:-
# Generator Object : <list_iterator object at 0x7f0897500bb0>
# next cartoon : Tom and Jerry
# next cartoon : Shin Chan
# next cartoon : Doraemon
# next cartoon : Ninja Hatodi
# next cartoon : Hage Maru
````

#### USAGE 2: ITERATOR VS GENERATORS;;

> **ITERATORS**

- Iterators use classes.
- Iterators use the `__next__` and `__iter__` methods.
- Iterators maintain state within instance attributes.
- No methods are paused. State is maintained within instance.
- Can be created using `iter()`.

> **GENERATORS**

- Generators use function.
- Generator use `yield` keyword for pause exeuction and `next()` methods.
- Generator maintain state within the local function variable.
- Functions are paused and their state is maintained within Python.
- Can be created using function().


#### USAGE 3: CREATE A ITERATOR;;

To create an iterator we have to add the `__iter__` and `__next__` methods in
our class. `__iter__` is used to initialize the iterator object and
`__next__` is used to return the next value from the iterator.

To create an iterator instance we have to call the iter() function on the
object of the class.

for eg,
````python
class IDGenerator:

    def __init__(self, ECODE):
        self.id = 0
        self.ECODE = ECODE

    def __iter__(self):
        return self                 # return the self instance of the object;

    def __next__(self):
        self.id += 1
        return f"{self.ECODE}{self.id:03d}"


def example2():
    idObject = IDGenerator('EAC')       # IdGenerator Object;;
    iterObject = iter(idObject)         # Iterator Object;;

    print("GENERATING EMPLOYEE CODE ...")
    for _ in range(5):
        print("ID: ", next(iterObject))


if __name__ == "__main__":
  example2()


# OUTPUT:-
# GENERATING EMPLOYEE CODE ...
# ID:  EAC001
# ID:  EAC002
# ID:  EAC003
# ID:  EAC004
# ID:  EAC005
````

#### USAGE 4: EXAMPLES OF ITERATORS;;

Many functions within Python 3 return an Iterator instead of a list by
default. This is in order to help conserve memory and avoid unnecessary
computation.

For example `the map()`, `filter()` and `range()` functions should ideally
return a sequence. Instead the return value is an iterable. 

To consume its values we have to pass it to the `list()` function or iterate
over it.

for eg, 
````python
# Example 1: range() iterator;;

print(range(5))         # result is an iterator
print(list(range(5)))   # convert iterator to a list

# OUTPUT:
# range(0, 5)
# [0, 1, 2, 3, 4]

# Example 2: map() iterator;;

inputs = [56, 23, 67, 23, 75, 23]
result = map(lambda x: x // 2, inputs)

print("Result : ", result) # <-- returns an iterator

for r in result: # <-- iterates through the results
  print(r, end="\t")

# OUTPUT:-
# Result :  <map object at 0x7ffff781df10>
# 28  11  33  11  37  11

# Example 3: filter() method iterator;;

nums = range(10)
result = filter(lambda x: x & 1, nums)
print("Result type : ", result)
print(list(result))

# OUTPUT:-
# Result type :  <filter object at 0x7ffff781df40>
# [1, 3, 5, 7, 9]
````

#### USAGE 5: MODIFYING ITERATOR WITH ITERTOOLS;;

> **ITERTOOLS :: BASICS**

Python comes with a dedicated inbuilt module to help us work with iterables.
The itertools module in Python consists of a set of functions that allow us
to augment iterables in a way that can ease our work.

To use the function from itertools we have to import it.

for eg,

````python
import itertools
print(itertools)

# OUTPUT:-
# <module 'itertools' (built-in)>
````

> **ITERTOOLS :: ZIP LONGEST** 

The `zip_longest()` function in itertools, extends the `zip()` functions
functionality.

Consider two lists A and B which are not equal in length. A has a length 
of 4 while B has a length of 6.

Given `zip(A, B)`, the `zip()` function ends after the 4th iteration as A has
only 4 values. The `zip_longest()` function on the other hand continues the
iteration until B ends. It fills the empty values missing from A with a fill
value.

for eg,
````python
from itertools import zip_longest

A = ["Aaron", "Clive", "Thomas", "Victor"]
B = ["Sharon", "Rossette", "Emily", "Alice", "Karen", "Shirley"]

for boy, girl in zip(A, B): # <-- ends after the 4th iteration
  print(f"{boy} is paired with {girl}")

# OUTPUT:
# Aaron is paired with Sharon
# Clive is paired with Rossette
# Thomas is paired with Emily
# Victor is paired with Alice

# Set 'Nobody' for fillvalue key for missing values;;
iterator = zip_longest(A, B, fillvalue="Nobody") 

for boy, girl in iterator: # <-- ends after the 6th iteration
  print(f"{boy} is paired with {girl}")

# OUTPUT:
# Aaron is paired with Sharon
# Clive is paired with Rossette
# Thomas is paired with Emily
# Victor is paired with Alice
# Nobody is paired with Karen
# Nobody is paired with Shirley
````

> **ITERTOOLS :: CYCLE**

The `cycle()` function loops through the values of a list infinitely. That is,
once it finishes iterating through all the values from a list, it begins
iterating again from the start of the list.

for eg,
````python
from itertools import cycle

colours = ['Red', 'Pink' , 'Blue']

iterObj = cycle(colours)

for i in range(100):
  print(next(iterObj))

# OUTPUT:
# Red
# Blue
# Pink
# Red
# Blue
# ... TILL 100
````

> **ITERTOOLS :: CHAIN**

The `chain` method in Python is used to combine multiple iterable arguments 
into a single iterable. It takes multiple iterables as arguments and returns 
an iterator that produces items from the first iterable until it is exhausted, 
then it continues to the next iterable, and so on.

for eg,
````python
from itertools import chain

# Example iterables
iterable1 = [1, 2, 3]
iterable2 = ['a', 'b', 'c']
iterable3 = (10, 20, 30)

# Using itertools.chain to combine the iterables
combined_iterable = chain(iterable1, iterable2, iterable3)

# Iterating over the combined iterable
for item in combined_iterable:
    print(item, end="->") 

# OUTPUT:
# 1->2->3->a->b->c->10->20->30
````

> **ITERTOOLS :: COMPRESS**

The `compress()` method helps us pick out elements from an iterable based on 
the values of another iterable.

For example, say we have a list of students `["John", "Vishnu", "Kabir"]` and
a list of results containing a boolean indicating if the student has passed
the test `[True, False, True]`. Now, using `compress()` we can select all the
students from the student list who have passed i.e where the boolean is
True.

for eg,
````python
from itertools import compress

students = ["John", "Vishnu", "Kabir", "Shreya", "Rose"]
results = [True, False, True, True, False]

filtered = compress(students, results)

print(list(filtered))
# OUTPUT: ['John', 'Kabir', 'Shreya']

# or,
filtered_students = [s for s, r in zip(students, results) if r]

print(filtered_students)  
# Output: ['John', 'Kabir', 'Shreya']
````

> **ITERTOOLS :: GROUPBY**

The `groupby()` function does exactly what its name says. Using groupby() 
we can group values of an iterable together based on a certain condition.

***THE ONE QUIRK OF THIS FUNCTION IS THAT IT EXPECTS THE ITERABLE TO BE IN 
SORTED ORDER***

Hence, we need to sort our lists before we use them.

for eg,
````python
from itertools import groupby

students = ["John", "Jishnu", "Vishnu", "Kabir", 
            "Vinod", "Shreya", "Vikas", "Rose"]
students.sort() # <-- sort list
groups = groupby(students, lambda x: x[1])

for group, values in groups:
  print(group, " --- ", list(values))

# OUTPUT: 
# i  ---  ['Jishnu']
# o  ---  ['John']
# a  ---  ['Kabir']
# o  ---  ['Rose']
# h  ---  ['Shreya']
# i  ---  ['Vikas', 'Vinod', 'Vishnu']
````

> **ITERTOOLS :: STARMAP**

The `starmap()` is similar to the map() function where we can iteratively pass
values from a list as an argument to a function. 

**NOTE : The difference between them is that `starmap()` supports passing
multiple arguments to a function.**

We can use `starmap()` in cases where we want to call a function iteratively
for every set of arguments in a list. `starmap()` passes each argument set to
the function and returns the results as an iterable.

for eg,
````python
from itertools import starmap

params= [(2,4), (5,6), (7,8)]

def areaRectangle(length, breadth):
  return length * breadth

res = starmap(areaRectangle, params)

for param, result in zip(params, res):
  print(f"{param} => {result}")

# OUTPUT: -
(2, 4) => 8
(5, 6) => 30
(7, 8) => 56

# ReWriting above code with map function;;

params= [(2,4), (5,6), (7,8)]

def areaRectangle(length, breadth):
  return length * breadth

res = map(areaRectangle, params)

for param, result in zip(params, res):
  print(f"{param} => {result}")

# OUTPUT:
# Traceback (most recent call last): ERROR!
# File "<string>", line 11, in <module>
# TypeError: <lambda>() missing 1 required positional argument: 'y'
````


-------------------------------------------------------------------------------------
### Q065 : Bitwise Operators;;

#### USAGE 1 : BITWISE BASIC;;

All data within a system is represented by bits. A bit is a unit of the binary 
number system, which comprises only two numbers 1 and 0.

A collection of bits make up Integers, Floats, Strings, and other Datatypes.

For example, the following are samples of how natural numbers are represented
in bit.

````
------------------------------
|   BITS      |    VALUES    |
------------------------------
| 0000 0001   |       1      |
| 0000 0010   |       2      |
| 0000 0011   |       3      |
| 0000 0100   |       4      |
| 0000 0101   |       5      |
------------------------------
````

`bin()` : `bin()` is a binary function in python can be used to quickyl view 
the binary representation of the number.

for eg,
````python
print(bin(5))   # 0b101
print(bin(6))   # 0b110
print(bin(15))  # 0b1111
````

#### OPERATOR 1 : BITWISE AND OPERATOR;;

The `AND` operator is represented by an `& (ampersand)` symbol in Python. It
compares two bits and returns 1 if and only if both the operands are 1. If
either one of the operands is 0, then the operator will return a 0.

Illustration 1 :
````
print(5, "\t = ", bin(5))
print(4, "\t = ", bin(4))
print(5 & 4, "\t = ", bin(5 & 4))

# OUTPUT:
5  =  0b101
4  =  0b100
5 & 4  =  0b100

# Code Explanation
5 :  0000 00101
4 :  0000 00100

# RESULT :
5 & 4 => 0000 00100  => 4
````

for eg,
````python
# EXAMPLE 1: CHECK FOR EVEN AND ODD IN BINARY OPERATOR;;
# Find if a number is even or odd using & operator;;

nums = [45, 21, 34, 64]

for num in nums:
  if(num & 1) : # <-- add condition here
    print(f"{num} is odd")
  else:
    print(f"{num} is even")

# OUTPUT:
45 is odd
21 is odd
34 is even
64 is even
````

#### OPERATOR 2 : BITWISE OR OPERATOR;;

The `OR Operator` is represented by a `| pipe character` in Python. The result
of an or operator is 1 if one of the operands is 1.

````
Illustration 2 :

print(10, "\t = ", bin(10))
print(1, "\t = ", bin(1))
print(5, "\t = ", bin(5))
print(10 | 5, "\t = ", bin(10 | 5))

# OUTPUT:
10   =  0000 1010
1    =  0000 0001
5    =  0000 0101
15 | 5  =  0000 1111
````

for eg,
````python
# EXAMPLE 2 : 
# Check if a number is even or odd. If it is odd, you should ignore it. 
# If it is even, increment the number by 1 to 
# make it odd.

# Modify an even number by adding 1 and making it odd
nums = [45, 21, 34, 64, 4, 97, 24]

for num in nums:
  res = num | 1
  print(f"res is now ", {res})

# OUTPUT:
# 45 is now 45
# 21 is now 21
# 34 is now 35
# 64 is now 65
# 4 is now 5
# 97 is now 97
# 24 is now 25

# EXPLANATION:
# We are adding 1 to only even value and making then odd number
# So, for illustration
# 14 : 0000 1110 
# 1 : 0000 0001
# then, OR Operation...
# 14 OR 1 => 0000 1110 OR 0000 0001 => 0000 1111 (~15)
````

#### OPERATOR 3 : XOR BITWISE OPERATION;;

The `XOR operator` is represented by the `^ (hat)` character in Python. The
XOR operator outputs a 1 only if both the input bits are different. If both
input bits are the same, the result is 0.

Illustration 3 :-
````python
print(10, "\t = ", bin(10))
print(12, "\t = ", bin(12))
print(10 ^ 12, "\t = ", bin(10 ^ 12))

# OUTPUT: 
# 10 : 0000 1010
# 12 : 0000 1100
# 10 XOR 12 => 0000 1010 XOR 0000 1100 => 0000 0110
````

for eg,
````python
# Illustration : Version 1 
def example3_v1():
    nums = [
        34, 3, 64, 33, 22, 574, 74, 6, 3, 2, 574, 
        43, 33, 789, 6, 64, 43, 22, 789, 34, 2
    ]

    i, result = 0, 0
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        status = nums[i] ^ nums[j]
        # Status : 0 means number is duplicate;
        if(status == 0):
          break
      # status not 0 means loop iterated success and unique number is found;
      if(status != 0):
        result = nums[i]
        break

    print(f"Result : {result}")

# Illustration : Version 2 
def example3_v2():
    nums = [
        34, 3, 64, 33, 22, 574, 74, 6, 3, 2, 574, 
        43, 33, 789, 6, 64, 43, 22, 789, 34, 2
    ]

    result = 0
    for num in nums:
        print("Current num :", num)
        result ^= num
        print(f"current result:", result)

    print("Result :", result)
````

#### OPERATOR 4 : NOT BITWISE OPERATION;;

The `NOT operation` is simple and easy to grasp. The purpose of the NOT operator
is to just invert the existing bits. i.e if the input is 0 the output is 1
and vice versa. The NOT operator is represented by the ~(tilde) sign in
Python.

The NOT operator is a unary operator in Python, which means, that it only
takes in one operand as the input

like,

````python
print(10, "\t = ", bin(10))   # 10 =  0b1010
print(~10, "\t = ", bin(~10)) # -11 = -0b1011
print(bin(~10 & 0xf))         # 0b101
````

#### OPERATOR 5: LEFT AND RIGHT SHIFT;;

`Left shift and Right shift operators` : These two operators either move the
bits to the left or right based on the value specified by the second operand.
The left and right shift operators are represented by the << and >> operators
respectively.

```
print(8, "\t =", bin(8))                # 8 = 0b1000
print(8 << 1, "\t =", bin(8 << 1))      # 16 = 0b10000

In our example, we right shift bit of integer 8 by 1 bit.

print(8, "\t =", bin(8))                # 8 = 0b1000
print(8 >> 2, "\t =", bin(8 >> 2))      # 2 = 0b10
```

for eg,
```
# Given below is a number n. Your task is to find the number 
# of 1's in the number. Do this using the >> and & operators.

num = 355
result = 0
print(bin(num))
while(num):
  result += (num & 1)
  num = num >> 1

print(result)

# OUTPUT :
0b101100011
5
```

-------------------------------------------------------------------------------------
### Q064 : Magic Method __call__ in Python;;

Python has a set of built-in methods and `__call__` is one of them. 

The `__call__` method enables Python programmers to write classes where the
instances behave like functions and can be called like a function. When the
instance is called as a function. 

If this method is defined,
>    `x(arg1, arg2, ...)` is a shorthand for `x.__call__(arg1, arg2, ...)`.

Syntax:
>    `object()` is shorthand for `object.__call__`

#### EXAMPLE 1:

for eg,
````python
class Example:
    def __init__(self):
        print("Instance Created")
      
    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")
  
# Instance created
e = Example()
  
# __call__ method will be called
e()     # e.__call__() i.e, Call object like a function;

# OUTPUT :
# Instance Created
# Instance is called via special method
````

#### EXAMPLE 2: 

for eg,
````python
class Product:
    def __init__(self):
        print("Instance Created")
  
    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)
  
# Instance created
ans = Product()
  
# __call__ method will be called
ans(10, 20)   # Calling like a function with argument;

# OUTPUT:
Instance Created
200
````

#### EXAMPLE 3:

for eg,
````python
class Student:

  _record = {}

  def __init__(self, name):
    self._record['name'] = name
    print(f"NEW STUDENT CREATED : {name}")

  def __call__(self, *args, **kwargs):
    flag = False
    if (args):
      flag = True
      self._record['extra'] = args

    if(kwargs):
      flag = True
      for key,value in kwargs.items(): 
        self._record[key] = value

    if(flag):
      print(f"PROFILE UPDATED")


  def showDetails(self):
    print(f"Student Profile : {self._record['name']}")
    for k,v in self._record.items():
      if not(k == 'name'):
        print(f"{k} : {v}")

# OUTPUT : 
# NEW STUDENT CREATED : Neeraj Singh
# PROFILE UPDATED
# Student Profile : Neeraj Singh
# extra : ('Crickets', 'Volleyball', 'Badminton')
# school : DUCS Sr. Sec. School
# std : XII
# teacher : Shristi Sharma
# Subjects : ('Physics', 'Chemisty', 'Computer Cpp', 'Maths', 'English')
````

-------------------------------------------------------------------------------------
#### Q063 : Class Decorator in Python;;

We can also use decorators to modify the methods of a class. As a class can
also be passed as an argument to a function, we can access and modify it as
required.

---

#### USAGE 1: IMPLEMENTING DECORATOR FUNCTION ON REGULAR CLASS;;

Here, in this example decorator are implemented using the regular function
like we are using earlied but the decorator are implementing on the class
variable.

for eg,
````python
def printUppercase(_class):
    # Problem: Here we are overwriting the old show method in which we
    # are also calling another decorator.
    # Solution is to preserve the show method original call and then
    # return the original method call before the wrapper ends;;
    print(" Calling printUppercase(): _class: ", _class)

    # Main Wrapper Starts Here
    def wrapper(self):
        res = self.word.upper()
        print(f"before: {self.word}, after: {res}")
        self.word = res
        return self.word

    # _class.show =  wrapper
    # here, we are overriding the memory reference of show method
    # from the class to the wrapper function of the decorator.
    # So that we can modify or extends the functional requirement
    # of that function.

    _class.show = wrapper  # Overriding old show function with wrapper

    return _class

def printUppercase_v2(_class):
    # Solution for previous version fix;;
    print(" Calling printUppercase_v2(): _class: ", _class)

    _original_show = _class.show

    # Main Wrapper Starts Here
    def wrapper(self):
        res = self.word.upper()
        print(f"before: {self.word}, after: {res}")
        self.word = res
        return _original_show(self)

    # _class.show =  wrapper
    # here, we are overriding the memory reference of show method
    # from the class to the wrapper function of the decorator.
    # So that we can modify or extends the functional requirement
    # of that function.

    _class.show = wrapper  # Overriding old show function with wrapper

    return _class

def convertStrToList(func):
    print(f" Calling convertStrToList(): func: ", func)

    def wrapper(*args, **kwargs):
        print(f"*args: {args}, kwargs: {kwargs}", )
        res = func(*args, **kwargs)
        res_list = res and res.split(" ")
        print(f" response: convertStrToList: {res_list}")
        return res_list

    return wrapper

# @printUppercase_v2  # bug fixed;;
@printUppercase   # observed bug;;
class Dictionary:

    def __init__(self):
        self.word = f"word of the day is --->maddness<---"

    @convertStrToList
    def show(self):
        print(f"from in-built memory: {self.word}")
        return self.word

print("__executing_main__")
obj = Dictionary()
print(f"__finished_main__: ", obj.show())

# original logs;;
# Calling convertStrToList(): func:  <function expl.<locals>.Dictionary.show at 0x7330f59c0c10>
# Calling printUppercase(): _class:  <class '__main__.expl.<locals>.Dictionary'>
# __executing_main__
# before: word of the day is --->maddness<---, after: WORD OF THE DAY IS --->MADDNESS<---
# __finished_main__:  WORD OF THE DAY IS --->MADDNESS<---

# v2 logs;;
# Calling convertStrToList(): func:  <function expl.<locals>.Dictionary.show at 0x7ee1a78c0c10>
# Calling printUppercase_v2(): _class:  <class '__main__.expl.<locals>.Dictionary'>
# __executing_main__
# before: word of the day is --->maddness<---, after: WORD OF THE DAY IS --->MADDNESS<---
# *args: (<__main__.expl.<locals>.Dictionary object at 0x7ee1a786f280>,), kwargs: {}
# from in-built memory: WORD OF THE DAY IS --->MADDNESS<---
# response: convertStrToList: ['WORD', 'OF', 'THE', 'DAY', 'IS', '--->MADDNESS<---']
# __finished_main__:  ['WORD', 'OF', 'THE', 'DAY', 'IS', '--->MADDNESS<---']

````

---

#### USAGE 2: IMPLEMENTING DECORATOR CLASS ON REGULAR FUNCTION;;

We can also use a class as a decorator in Python. The function will be
received as an argument to `__init__` and the function arguments will be 
passed to `__call__`.

for eg,
```python
# In the example below we define StoreResults which stores the results
# of every call to add().

class StoreResults:
    """
    @classname
    Here, you've defined the class as a decorator on a regular function.
    In class, you have to received the function name inside the __init__
    method using any keyword.
    Like this,
        def __init__(self, function): ...

    and the given functional arguments from external function (~add())
    will be received by the __call__() magic methods.
    """
    def __init__(self, func):
        self.func = func            # <-- accepts function as arguments;
        self.result = []            # <-- lists to store result;

    def __call__(self, *args, **kwargs):
        print("LOG: args:", args)            # debugger 1
        print("LOG: kwargs:", kwargs)        # debugger 2
        res = self.func(*args, **kwargs)
        self.result.append(res)
        return self.result


@StoreResults
def add(a,b, y,z): 
  return a+b 


if __name__ == "__main__":
  print(add(10, 10, y=10, z=20))
  print(add(11, 11, y=22, z=33))


# OUTPUT :
# LOG : args: (10, 10)
# kwargs: {'y': 10, 'z': 20}
# [20]

# LOG : args: (11, 11)
# LOG : kwargs: {'y': 22, 'z': 33}
# [20, 22]

# or, @return res ... instead of self.result from place INDEX-01;
# 20      
# 20, 22 
```

---

#### EXAMPLE 3 : PASSING ARGUMENT ON CLASS DECORATOR;;

To accept arguments to our class-based decorator, we would have to make subtle
changes because of the following issues.
1) The `__init__` method will now receive the decorator argument and not the function.
2) The function will be passed as the first argument to `__call__`. 
3) The function arguments will be received in a nested function.

for eg, 
````python
# In this case we are expanding the abbreviation of the given message;
# Given Abbreviation inside the system;

abbr = {
  "ttyl": "Talk to you later",
  "omg": "Oh my God!",
  "gtg": "got to go"
}

class Abbreviation:

    # Catch here is that, one layer added for top abstraction for 
    # receiving the class decorator argument;
    # __init__() : It will receive the argument from the decorator
    # calling.
    # dargs : decorator arguments received;

    def __init__(self, decorator_args): 
        self.dargs = decorator_args


    def __call__(self, func):   # here, func : name of the external function;

        # Nested Wrapper for main functionality;
        # args : refers to external argument of function;
        
        def wrapper(args):   
            
            # string, *_ = args             # Doesn't effect the code ;
            # print("string : ", string)    # Doesn't effect the code ;
            # print("undescore : ", _)      # Doesn't effect the code ;

            for key,value in self.dargs.items():
                if(key in args):
                    args = args.replace(key,value)

            return func(args)

        return wrapper


@Abbreviation(abbr)
def message(msg):
    print(msg)


if __name__ == "__main__":
  message("omg that's so funny. Anyways I gtg. ttyl okay.")
````

---

#### Decorator Difference in Usage 2 & Usage 3;;

The key difference is that the **current code uses an extra `__init__`
argument (`decorator_args`)** to accept parameters when applying the class as
a decorator.

---

#### **1. Your Previous Code (`StoreResults`)**

- **Why No Extra Function?**

  - `StoreResults` is used **directly** as a decorator without any parameters.
  - It only needed to store the function reference (`func`) and maintain the
    result list.

```python
@StoreResults
def add(a, b, y, z):
    return a + b
```

- **Flow:**

  1. The function `add` is passed directly to `StoreResults.__init__`.
  2. `__call__` executes the function and stores results.
  3. There’s no additional input required at the time of decoration.

---

## **2. Your Current Code (`Abbreviation`)**

- **Why the Extra Function?**

  - Here, **the decorator itself** takes an argument (`abbr`), which is a dictionary.
  - This **adds another layer of abstraction**:
    - `__init__`: Receives the dictionary when the decorator is used.
    - `__call__`: Receives the function and applies the abbreviation logic.

```python
@Abbreviation(abbr)  # <-- Passing arguments
def message(msg):
    print(msg)
```

- **Flow:**

  1. `@Abbreviation(abbr)` is executed **first**, calling
  `Abbreviation.__init__()`, which stores the abbreviation dictionary.

  2. The `__call__()` method then wraps the `message()` function with a
  `wrapper` function.
  
  3. When `message()` is called, `wrapper()` runs first, replacing
  abbreviations in `msg`.

---

## **Key Difference: When Do We Need an Extra Function?**

**Simple decorator without arguments** (`StoreResults`) : The function is
  passed directly to `__init__`, and `__call__` handles everything.


**Decorator with arguments** (`Abbreviation`) : An extra `__init__` is needed
  to accept the decorator argument (the abbreviation dictionary).

---

## **General Rule**

- **If your decorator doesn’t take parameters**, you can directly store the
    function inside `__init__()`.
- **If your decorator needs parameters**, you need an extra layer
    (`__init__`) to store those parameters **before** wrapping the function.


-------------------------------------------------------------------------------------
### Q062 : Generators Workflow in Python;;

Generators are basically stateful functions. They can be paused and resumed at
specific points.

Consider ordering fries, biryani, and ice cream at a restaurant. You could ask
the waiter to get all the items in one go itself. However, it would be
difficult to consume all of them in one sitting. Instead, you ask the waiter
to get the first dish i.e fries, and once you are through with it, you could
ask them to get the next one i.e, biryani followed by ice cream.

Generators take a similar approach. A function is paused after it yields a
value and resumes when it is explicitly asked.

> Example Illustration in P0043 inside the BasicPython/01.basic/...

for eg, 
````python
###---- Example 1 : Basic Example for Generator object;;
def orderFood():
    yield 'Red Wine'
    yield 'Fish and Rice'
    yield 'Ice Cream'

def example1():
    serving = orderFood()
    print("__main__ :", serving)
    print("Starters : ", next(serving))
    print("Main Course: ", next(serving))
    print("Desserts :", next(serving))

# OUTPUT:
# __main__ : <generator object orderFood at 0x7f431e4f2a50>
# Starters :  Red Wine
# Main Course:  Fish and Rice
# Desserts : Ice Cream


###---Example 2: Fibonacci Series using the Generator Object;;
def fibo(a=0, b=1, limit=10):
    a = 0
    yield(a)
    b = 1
    yield(b)
    for _ in range(limit):
        c = a+b 
        yield(c)
        a,b = b,c

def example2():
    a,b,limit = 0,1,10
    fib = fibo(a,b,limit)        
    print("Generator Initiated ")
    print("Object __main__ :", fib)
    for k in range(limit):
        print(next(fib), end="")
        if not(k == limit-1):
            print("->", end="")
    print('\nGenrator Terminated !')

# OUTPUT:
# Generator Initiated 
# Object __main__ : <generator object fibo at 0x7fc5238c2a50>
# 0->1->1->2->3->5->8->13->21->34
# Genrator Terminated !


###--- Example 3: Calculate first N prime number default limit 10;;
def checkPrimeNumber(num):
    for x in range(2, num//2):
        if(num % x == 0):
            return False
    return True

def primeGenerator(count):
    i = 2           # number 0 and 1 are not prime number;
    cur_count = 0
    while(i and cur_count<=count):
        if(checkPrimeNumber(i)):
            yield(i)
            cur_count += 1
        i += 1

def example3():
    count = 10
    nextPrimeNumber = primeGenerator(count)
    print("Generator Initialized...")
    print("Object __main__ : ", nextPrimeNumber)
    for _ in range(count):
        print("Next Prime Number : ", next(nextPrimeNumber))
    print("\nGenerator Terminated !")

# OUTPUT :
# Generator Initialized...
# Object __main__ :  <generator object primeGenerator at 0x7f50800fea50>
# Next Prime Number :  2
# Next Prime Number :  3
# Next Prime Number :  4
# Next Prime Number :  5
# Next Prime Number :  7
# Next Prime Number :  11
# Next Prime Number :  13
# Next Prime Number :  17
# Next Prime Number :  19
# Next Prime Number :  23
# Generator Terminated !
````

#### USAGE 2 : PASSING ARGUMENT TO GENERATOR;; 

For eg,
````python
names = ["ferrari", "john", "barbie", "cottonwood", "shirley"]
labels = ["car", "boy", "toy", "tree", "girl"]

def combine(data_a, data_b):
  for a, b in zip(data_a, data_b):
    yield f"{a.capitalize()} is a {b}"    # Pause
    
cogen = combine(names, labels) # pass arguments to combine

for value in cogen: # for loop will iterate until end of data
  print(value)

# OUTPUT :
# Ferrari is a car
# John is a boy
# Barbie is a toy
# Cottonwood is a tree
# Shirley is a girl
````


-------------------------------------------------------------------------------------
### Q061 : First Class Function in Python;;

#### DEFINATION OF FIRST CLASS FUNCTION;;

`First class functions`: If a function can be assigned to a variable or passed
as object/variable to other function, that function is called as `first class
function`.

Languages like - `Python`, `Javascript` and `C(pointers)` support first class
functions.

`First class objects` in a language are handled uniformly throughout. They 
may be stored in data structures, passed as arguments, or used in control
structures. A programming language is said to support first-class functions
if it treats functions as first-class objects. Python supports the concept of
First Class functions.

for eg, 
````python
def square(x):
  return x*x

def cube(x):
  return x*x*x

def show(x, func):
  return func(x)

print(show(5, square))    # 25
print(show(5, cube))      # 125
````

#### PROPERTIES OF FIRST CLASS FUNCTIONS:
1) You can store the function in a variable. 
2) You can pass the function as a parameter to another function. 
3) You can return the function from a function. 
4) You can store them in data structures such as hash tables, lists, 

#### Property 1 : Storing function in variable

Functions are objects: Python functions are first class objects. In the
example below, we are assigning function to a variable. This assignment
doesn’t call the function. It takes the function object referenced by shout
and creates a second name pointing to it, yell.

for eg,
````python
def show(message):
  return message.upper()

print(show("Hello World"))      # HELLO WORLD
yell = show
print(yell("Now i'm shouting..."))       # NOW I'M SHOUTING...
````

#### Property 2 : Functions can be passed as arguments to other functions:

Because functions are objects we can pass them as arguments to other
functions. Functions that can accept other functions as arguments are also
called higher-order functions. In the example below, we have created a
function greet which takes a function as an argument.

for eg,
````python
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
    
def whisper(text):
    return text.lower()
    
def greet(func):
    #storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print greeting     

greet(shout)
greet(whisper)
````

#### Property 3 : Functions can return another function

Because functions are objects we can return a function from another function.
In the below example, the create_adder function returns adder function.

for eg,
````python
#Python program to illustrate functions
#Functions can return another function    
def create_adder(x):  
    def adder(y):  
        return x+y  
    return adder 
      
add_15 = create_adder(15)
print(add_15(10))
````


-------------------------------------------------------------------------------------
#### Q060 : Operator Overloading in Python;;

`Operator Overloading` : The + operator is used to add two numbers or
concatenate two strings together. Using Operator Overloading we can also
modify it to perform some operations on our newly created objects.

To overload the + operator, we have to overwrite the internal `__add__` 
method of the operand's class.

for eg,
````python
class House:
  def __init__(self):
    self.rooms = []

  def __add__(self, room): # <-- operator overloading done here
    self.rooms.append(room)
    return house

  def __repr__(self): # <-- For display purposes. Can be ignored
    room_names = [str(room) for room in self.rooms]
    room_str = ', '.join(room_names)
    return f"House[rooms: [{room_str}]]"


class Room:
  def __init__(self, room_owner):
    self.owner = room_owner

  def __repr__(self):
    return f"{self.owner}'s room"


house = House()
judys_room = Room("Judy")
house = house + judys_room # <-- add a room to house using overloaded + operator
print(house)

arthurs_room = Room("Arthur")
house = house + arthurs_room # <-- add another room to house
print(house)


# OUTPUT :
# House[rooms: [Judy's room]]
# House[rooms: [Judy's room, Arthur's room]]
````

#### Overloading other mathematical operators;;

- Addition (c1 + c2): `c1.__add__(c2)`
- Subtraction (c1 - c2): `c1.__sub__(c2)`
- Multiplication (c1 * c2): `c1.__mul__(c2)`
- Power (c1 ** c2): `c1.__pow__(c2)`
- Division (c1/c2): `c1.__truediv__(c2)`
- Floor Division (c1//c2): `c1.__floordiv__(c2)`
- Remainder(c1 % c2) : `c1.__mod__(c2)`
- Bitwise Left Shift(c1 << c2) : `c1.__lshift__(c2)`
- Bitwise Right Shift(c1 >> c2) : `c1.__rshift__(c2)`
- Bitwise AND	(c1 & c2) : `c1.__and__(c2)`
- Bitwise OR (c1 | c2) : `c1.__or__(c2)`
- Bitwise XOR (c1 ^ c2) : `c1.__xor__(c2)`
- Bitwise NOT (~c1) : `c1.__invert__()`


-------------------------------------------------------------------------------------
### Q059 : Inheritance in Python;;

#### EXAMPLE 1: BASIC INHERITANCE;

`Inheritance` : Python supports inheriting data and methods from other
classes. This can help us to avoid rewriting common functionalities across
multiple classes.

#### Inheritance of Class

````py
class Phone: # <-- Parent class
  """
  Contains all functionalities and data of a Phone
  """

  def call(self, number):
    print(f"Calling {number}")


class IPhone(Phone): # <-- Inherits Phone class
  """
  Contains all functionalities and data of a Phone and IPhone
  """
  def __init__(self):
    self.ios_version = "12.5.6"

  def get_ios_version(self):
    print(f"iOS Version {self.ios_version}")


class AndroidPhone(Phone): # <-- Inherits Phone class
  """
  Contains all functionalities and data of a Phone and Android Phone
  """
  def open_playstore(self):
    print("Opening Play Store")


print("Calling iPhone methods")
iphone = IPhone()
iphone.call("999999999") # <-- Called from parent (Phone) class
iphone.get_ios_version() # <-- Called from child (IPhone) class

print("Calling Android methods")
android_phone = AndroidPhone()
android_phone.call("999999999") # <-- Called from parent (Phone) class
android_phone.open_playstore()  # <-- Called from child (AndroidPhone) class

# OUTPUT:
# Calling iPhone methods
# Calling 999999999
# iOS Version 12.5.6

# Calling Android methods
# Calling 999999999
# Opening Play Store
````

#### EXAMPLE 2 : METHOD OVERRIDING;;

`Method Overriding` : Inheritance allows us to overwrite the methods and data
from the parent class. We could add new functionality in the child class for
the same method.

for eg,
````py
class Phone:
  """
  Parent Class
  """
  def send_email(self, email_id):
    print(f"Sending an email to {email_id} via Email")

class IPhone(Phone):
  """
  Child Class
  """
  def send_email(self, email_id): # <-- Child class with same method name and args as parent class
    print(f"Sending an email to {email_id} via Apple Mail")

print("Calling Phone methods")
phone = Phone()
phone.send_email("abc@gmail.com") # <-- Called from Parent class

print()

print("Calling iPhone methods")
iphone = IPhone()
iphone.send_email("abc@gmail.com") # <-- Overwritten method called from Child class

# OUTPUT:
# Calling Phone methods
# Sending an email to abc@gmail.com via Email

# Calling iPhone methods
# Sending an email to abc@gmail.com via Apple Mail
````

#### EXAMPLE 3: SUPER FUNCTION

`SUPER()` method helps us to call the function of parent method from 
before overriding that function in the derived class.

`super()` refers to a temporary instance of the parent class.

for eg, 
````py
class Phone:
  """
  Parent Class
  """
  def power_up(self):
    print("Powering up Phone.")


class IPhone(Phone):
  """
  Child Class
  """
  def power_up(self):
    super().power_up() # <-- Calls Phone.power_up()
    print("Showing apple logo")


print("Calling iPhone methods")
iphone = IPhone()
iphone.power_up()

# OUTPUT:
# Calling iPhone methods
# Powering up Phone.
# Showing apple logo
````

#### EXAMPLE 4: MULTIPLE INHERITANCE

`Multiple Inheritance` can inherit attributes and methods from more than 
two class at the same time.

for eg,

````py
class Phone:
  """
  Contains all functionalities and data of a Phone
  """
  def start(self):
    print(f"Opening Caller")


class Camera:
  """
  Contains all functionalities and data of a Camera
  """
  def start(self):
    print(f"Opening Camera")


class IPhone(Phone, Camera):
  def __init__(self):
    print("Switching on iPhone")


iphone = IPhone()
iphone.start() # <-- Calls from Phone class

# OUTPUT:
# witching on iPhone
# Opening Caller
````

-------------------------------------------------------------------------------------
### Q058 : Class and Objects Python;;

A class is a blueprint for an item. For example, if Dog is a class then a
Labrador is an object or instance of that class

The `__init__` method is automatically called by Python internally when we
create an instance/object of the class

The self variable within our class represents the instance of the class.

#### Basic Class Example;;

````py
class Dog: # <-- Define Dog class
  
  noOfObjects = 1       # <-- Class ATTRIBUTES;

  def __init__(self, name, breed):
    self.name = name # <-- ATTRIBUTE : Dog has a name
    self.breed = breed # <-- ATTRIBUTE : Dog belongs to a breed
    Dog.noOfObjects += 1

  # METHOD 1
  def bark(self): # <-- Dog can bark
    print("Woof")

  # METHOD 2
  def wag_tail(self): # <-- Dog can wag tail
    print("Wagging tail..")  

chester = Dog(name="Chester", breed="dalmatian")

chester.bark()
chester.wag_tail()

print(f"The dog name is {chester.name}") 
print(f"The dog name is {chester.breed}")

# OUTPUT:
# Woof
# Wagging tail..
# The dog name is Chester
# The dog name is dalmati
````

#### Example of class attributes;;

````py
class Employee:

  # Create class attribute count
  id = 0

  def __init__(self, name):
    self.name = name
    Employee.id += 1
    self.id = Employee.id

employee = Employee("Annie")
print(f"{employee.name}'s Employee ID: ", employee.id)

employee = Employee("Jonas")
print(f"{employee.name}'s Employee ID: ", employee.id)

# OUTPUT :
# Annie's Employee ID:  1
# Jonas's Employee ID:  2

# for eg, // Find the class name from a object;
  
class Dog:
  def __init__(self, name):
    self.name = name


chester = Dog("Chester")
print(chester.__class__.__name__)

# OUTPUT 
# Dog
````


-------------------------------------------------------------------------------------
### Q057 : Decorator in Python;; 

*(Refer Q063 : Class Decorator in Python)*

Sometimes we might want to run some code at the beginning and at end of a
function. 

While effective, we would have to wrap any function/code we want to measure
with time.time() statements. 

We can avoid such repetition using decorators and implement the same in a much
cleaner way.

for eg, 

#### EXAMPLE WITHOUT DECORATOR;;
````py
import time

def hello_world():
  print("Hello World")

if __name__ == "__main__":
    start = time.time()
    hello_world()
    end = time.time()
    print(f"Time taken : {end - start} seconds")
````

Decorators are basically functions. They help us run code before and after
other functions. Ideally, you can think of them as wrappers for other
functions.

#### EXAMPLE 1: DECORATOR EXAMPLES;;

For eg, 
````py
# BASIC EXAMPLE 1
import time

def hello_world():
  print("Hello World")

def measure_time(another_function):     # <-- Decorator function
  start = time.time()
  result = another_function()           # <-- Original function called
  end = time.time()
  print(f"Execution Time : {end - start} seconds")
  return result                         # <-- Result of original function returned

measure_time(hello_world)

# BASIC EXAMPLE 2
# Create function encrypt to encrypt the string returned from send_message
# Store the result in message

def encrypt(func):
  res = func()
  return [ord(char) for char in res]

def send_message():
  return "Tango, Charlie, Alpha"

message = encrypt(send_message)

print(message)
# OUTPUT :
[84, 97, 110, 103, 111, 44, 32, 67, 104, 97, 114, 
108, 105, 101, 44, 32, 65, 108, 112, 104, 97]
````

#### EXAMPLE 2: DECORATOR AS ANNOTATION;

Python provides a cleaner and shorter way to represent decorators by using the
`@ symbol`.

for eg,
````py
# Annotations;
def measure_time(another_function):
  start = time.time()
  result = another_function()
  end = time.time()
  print(f"Time Measured : {end - start} seconds")
  return result

@measure_time           # <-- wraps hello_world in measure_time decorator
def hello_world():
  print("Hello World")

# OUTPUT :
Time Measured : 5.936622619628906e-05 seconds
````

**EXPLANATION : There is an issue inside this approach which is that python
  runs measure_time()(hello_world) without an explicit call or calling
  automatically, which is something we might not want.** 

**REMARK : To avoid such automatic calling scenario, we used the nested function.**

#### EXAMPLE 3: NESTED FUNCTION;

Re-define above method using the nested function !!!

for eg,
````py
from time import time, sleep

def runtime(func):
  def wrapper():
    start = time()
    func()
    end = time()
    print(f"runtime : {end - start} seconds")
  return wrapper  # Return the memory reference of the wrapper method defination;
  
@runtime
def greeting():
  print(f"Loading Task Modules In Memory ...", end=sleep(3))      # 3 Seconds;;
  print("Hello World")
  print(f"Flushing Task Modules From Memory ...", end=sleep(3))   # 3 Seconds;;

greeting()    # MAIN ENTERY POINT;

# OUTPUT : 
# Loading Task Modules In Memory ...
# Hello World
# Flushing Task Modules From Memory ...
# runtime : 6.0056188106536865 seconds
````

**EXPLANATION :  The only change that we have made is that we have added a
  nested function called `wrapper()` and moved the code within it.
  `measure_time()` returns this wrapper function to the caller.
  If we run the code snippet now, you will notice measure_time() is not being
  called implicitly. Instead, we will have to call hello_world(), which will
  internally call the code from wrapper() within the measure_time
  decorator.**

for eg, 
````py
# REDEFINE BASIC EXAMPLE 2 WITH WRAPPER;;
# MESSAGE ENCYRPTION PROBLEM;;

def encrypt(func):
  def wrapper():
    message = func()
    return [ord(c) for c in message]
  return wrapper
  
@encrypt
def send_message():
  return "Tango, Charlie, Alpha"

send_message()
````

#### EXAMPLE 4: DECORATOR WITH ARGUMENT;

An buggy based example for receiving the argument inside the decorator.

For eg,
````py
import time

def measure_time(function):
  
  def wrapper():
    start = time.time()
    result = function() # Nested functions have access to variables from parent function
    end = time.time()
    print(f"Time taken for to execute hello is {end - start} seconds")
    return result

  return wrapper


@measure_time
def hello(name):
  print("Hello", name)

hello("Python")     # Here we've passed the "Python" as the arguments;

# OUTPUT : (Missing Parameter Error Occured)
# Traceback (most recent call last):
#   File "script.py", line 17, in <module>
#     hello("Python")
# TypeError: wrapper() takes 0 positional arguments but 1 was given
````

**CORRECTING THE ABOVE CODE SNIPPET TO ACCEPT ARGUMENT;;**

```py
import time

def measure_time(function):
 
  def wrapper(*args, **kwargs): # <-- accepts arguments
    print(f"args : {args} || kwargs : {kwargs}")
    start = time.time()
    result = function(*args, **kwargs) # <-- Pass arguments to function i.e hello()
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    return result
  
  return wrapper # <-- Notice here just memory reference to the function defination;

@measure_time
def hello(*args, **kwargs):
  print("your v-args:", args)
  print("your kw-args:", kwargs)

hello("Python", "Guido Van Rosseum", xyz=20, abc=30)

# OUTPUT:-
# args : ('Python', 'Guido Van Rosseum') || kwargs : {'xyz': 20, 'abc': 30}
# your v-args: ('Python', 'Guido Van Rosseum')
# your kw-args: {'xyz': 20, 'abc': 30}
# Time taken: 1.4543533325195312e-05 seconds
````

### EXAMPLE 5: MULTIPLE DECORATORS;;

The `measure_time` decorator here measures the time for running the function
twice. That is, it includes the `do_twice` decorator's time within it. 

Try swapping the order of the decorators and see the output.

for eg,

````py
# Ex 1: Demonstration for passing argument;

import time

def measure_time(function):

  '''Measures time for execution'''
  def wrapper(*args, **kwargs):
    start = time.time()
    result = function(*args, **kwargs)
    end = time.time()
    print(f"Time taken to execute print_name is {end - start} seconds")
    return result

  return wrapper


def do_twice(function):
  '''Executes the function twice'''
  def wrapper(*args, **kwargs):
    for _ in range(2):
      function(*args, **kwargs)

  return wrapper


@measure_time # <-- Decorator 1
@do_twice # <-- Decorator 2
def print_name(name):
  print(f"My name is {name}")


print_name("Eleven")

# OUTPUT :
# My name is Eleven
# My name is Eleven
# Time taken to execute print_name is 6.9141387939453125e-06 seconds


# Ex 2: For Passing Argument in Decorator;

"""
SCENARIO : Pavel has been working on strengthning his encryption program. He
has decided that once he converts his characters to numbers using ord() he
will add them by a particular constant to increase their encryption
strength.

Help him modify the decorator to accept an integer strength with the value 3,
which will then be added to the result of every ord(char).
"""


# Modify encrypt decorator to accept argument strength
# Add it to ord(c)

# Intermediate Encryption;
def encrypt_v2(times):
  # Encryption V1: Basic Encryption;
  def encrypt_v1(func): # <-- Accept argument strength
    # Create a nested function
    def wrapper(*args, **kwargs):
      message = func(*args, **kwargs)
      return [ord(c)+times for c in message]  # <-- Add strength to ord(c)
    return wrapper
  return encrypt_v1
  
@encrypt_v2(times=3)
def send_message(message):
  return message

message = send_message("Hello Officers. This is your captain speaking.")

print(message)

# OUTPUT:
# [75, 104, 111, 111, 114, 35, 82, 105, 105, 108, 102, 104, 117, 118, 49, 35,
# 87, 107, 108, 118, 35, 108, 118, 35, 124, 114, 120, 117, 35, 102, 100, 115,
# 119, 100, 108, 113, 35, 118, 115, 104, 100, 110, 108, 113, 106, 49]
````

#### EXAMPLE 6: DECORATOR INSIDE DECORATOR WITH ARGUMENT;;

- General purpose Decorator with Decorator itself accepting arbitary arguments;;
- decorator_kwargs: kwargs are coming from decorator main (@decorator_maker);
- 1st Level Decorator;;

for eg,

````py
def decorator_maker(*args):  
    # Decorator works likes the main;

    def decorator_main(func):
        # Wrapper function arguments come from the main external function
        # (employee_details);
        
        def wrapper(**kwargs):
            print("-----------------------------------")
            print("****|Decorator Maker Arguments|****")
            print("-----------------------------------")
            for key,value in kwargs.items():
                print(f"{key} : {value}")
            print("-----------------------------------")
            for key,value in enumerate(args, start=1):
                print(f"Hobbies {key} : {value}")
            else:
                print("-----------------------------------")
                data = func(**kwargs)
                print(f"data : {data}")

        return wrapper          ## 2nd-level-decorator > return;

    return decorator_main       ## 1st-level-decorator -> return ;

# Now, decortator_main() will receive argument like ordinary function;;
@decorator_maker("Crickets", "Badminton", "Football", "Volleyball")
def student_details(**kwargs):
    return kwargs

student_details(
  "firstname" : "Neeraj",
  "middlename" : "Singh",
  "lastname" : "Junior",
  "std" : "XII"
)

# OUTPUT : 
# -----------------------------------
# ****|Decorator Maker Arguments|****
# -----------------------------------
# firstname : Neeraj
# middlename : Singh
# lastname : Junior
# std : XII
# -----------------------------------
# Hobbies 1 : Crickets
# Hobbies 2 : Badminton
# Hobbies 3 : Football
# Hobbies 4 : Volleyball
# -----------------------------------
# data : {
#   'firstname': 'Neeraj', 
#   'middlename': 'Singh', 
#   'lastname': 'Junior', 
#   'std': 'XII'
# }
````

-------------------------------------------------------------------------------------
### Q056 : Date and Time (datetime) Module;;

Python provides specialized modules for working with dates and times. One of
the most popular modules for the same is the datetime module.

SYNTAX :

````py
from datetime import datetime
today = datetime.now()
print(today)               # 2022-11-21 20:01:00.791002

# or, alternatively we can used the datetime object like this also,
xmas = datetime(year=2022, month=12, day=25)
print(f"This year Christmas day comes on a {xmas:%A}")
````

#### EXAMPLE 1: BASIC 

For eg,
```py
from datetime import datetime

today = datetime.now()                          # 2022-11-21 20:01:00.791002  

print(f"The day today is {today.day}")          # The day today is 22
print(f"The month is {today.month}")            # The month is 11
print(f"The year is {today.year}")              # The year is 2022
print(f"The hour is {today.hour}")              # The hour is 1
print(f"The minute is {today.minute}")          # The minute is 36
print(f"The second is {today.second}")          # The second is 4
```

#### EXAMPLE 2: TODAYS DATE;

for eg,
````py
from datetime import datetime

today = datetime.now()

dd = today.day
mm = today.month
yyyy = today.year

print(f"Today : {dd}-{mm}-{yyyy}")              
# OUTPUT : Today : 21-11-2022
````

#### EXAMPLE 3: HUMAN READABLE DATE;

- Human-readable formats of dates :

````
-----------------------------------------------------------
|   Code     |     Description             |   Example    |  
-----------------------------------------------------------
|    %d      |   day of the month          |    08        |
|    %m      |   month of the year         |    12        |
|    %y      |   year in two digits        |    93        |
|    %Y      |   year in four digits       |    1993      |
|    %a      |   abv. name of the day      |    Sun       |
|    %A      |   full name of the day      |    Sunday    |
|    %b      |   abv. name of the month    |    Dec       |
|    %B      |   full name of the month    |    December  |
|    %H      |   hour in 24h format        |    14        |
|    %I      |   hour in 12h format        |    02        |
|    %M      |   minute of the hour        |    30        |
|    %S      |   second of the minute      |    40        |
|    %p      |   AM/PM                     |    PM        |
-----------------------------------------------------------
````

for eg,

```py
from datetime import datetime

today = datetime.now()

print(f"Today   : {today:%d-%m-%y}")            # Today   : 22-11-22
print(f"Today   : {today:%d-%m-%Y}")            # Today   : 22-11-2022
print(f"Time    : {today:%H::%M::%S}")          # Time    : 01::55::57
print(f"AM/PM   : {today:%p}")                  # AM/PM   : AM
print(f"Month   : {today:%b or %B}")            # Month   : Nov or November
print(f"Weekday : {today:%a or %A}")            # Weekday : Tue or Tuesday
```

#### EXAMPLE 4: DIFFERENCE IN TIME;

You can count the required days or months. By simply subtracting it 
from the `datetime.now()` object

for eg,
````py
from datetime import datetime

current_date = datetime.now()
christmas_date = datetime(year=2022, month=12, day=25)
days_left = christmas_date - current_date

print(f"Days left with Time : {days_left}")     # Days left : 32 days, 21:36:31.024657
print(f"Days left only : {days_left}")          # Days left only : 32 days
````

#### EXAMPLE 5: REPLACE VALUE IN DATETIME;;

To replace any value like a year, month, date, hour, etc within the date or
time in the datetime object we can use the replace() method.

for eg,
```py
from datetime import datetime

christmas_day = datetime(year=2022, month=12, day=25)

# can use year, month, day, hour, minute, microsecond
next_christmas = christmas_day.replace(year=2023)

time_since = next_christmas - christmas_day

print(f"Days left for X-Mas : {time_since.days}")   # Days left for X-Mas : 365
```

#### EXAMPLE 6: TIMEDELTA IN PYTHON;

Sometimes we might want to add or subtract a number of days to/from our date.
For this, we use the timedelta() function.

The timedelta object adds or removes weeks, days, and time. For example, we
could also add an hour to our time.

for eg,
````py
from datetime import timedelta, datetime

print(f"Today: {datetime.now()}") 
# OUTPUT : Today: 2022-11-21 21:34:17.346508

# Adds two days
add_two_days = timedelta(days=+2)
print(f"Two days later: {datetime.now() + add_two_days}")
# OUTPUT : Two days later: 2022-11-23 21:34:17.346525

# Adds 1 week
add_one_week = timedelta(weeks=+1)
print(f"One week later: {datetime.now() + add_one_week}")
# OUTPUT : One week later: 2022-11-28 21:34:17.346531

# Subracts 1 day
subtract_one_day = timedelta(days=-1)
print(f"Yesterday: {datetime.now() + subtract_one_day}")
# OUTPUT : Yesterday: 2022-11-20 21:54:19.012421

next_two_year = timedelta(days=365*2)
print(f"next year : {datetime.now() + next_two_year}")
# next year : 2024-11-20 21:54:19.012424
````


-------------------------------------------------------------------------------------
### Q055 : Deque in collection module;;

A deque is a combination of a stack and a queue data structure. It basically
implements the First In First Out (Queue) and First In Last Out
(Stack) policies internally.

It is similar to a list wherein we can add and remove elements. However, a
deque is much faster when adding or removing elements compared to a list. At
the same time, it is slower when accessing elements, as you can only access
the ends of the queue.

SYNTAX :
````py
from collections import deque

que = deque([1,2,3,4,5])
print(que)
````

#### EXAMPLE 1
```py
from collections import deque

nums = [x for x in range(6)]
print(nums)                         # [0, 1, 2, 3, 4, 5]
que = deque(nums)
print(que)                          # deque([0, 1, 2, 3, 4, 5])
que.append(6)
print(que)                          # deque([0, 1, 2, 3, 4, 5, 6])
print(que.pop())                    # 6
print(que)                          # deque([0, 1, 2, 3, 4, 5])
print(que.popleft())                # 0
print(que)                          # deque([1, 2, 3, 4, 5])
que.appendleft(10)
print(que)                          # deque([10, 1, 2, 3, 4, 5])
```


-------------------------------------------------------------------------------------
### Q054 : Name Tuples (namedtuple) in collections module;;

A named tuple is a variant of a tuple whose values can be accessed by a given
attribute instead of indices.

SYNTAX : 

````py
variable_name = namedtuple("tuple_name", ['attribute_1', 'attribute_2'])
````

USE CASE :

- Struct-like objects without needing a full class.
- Readable and self-documenting code.
- Lightweight data storage (similar to objects but immutable like tuples).


#### EXAMPLE 1,

````py
from collections import namedtuple

# Sake of Simplicity, community define the variable-name 
# and name-of-tuple of value same like below,
Employee = namedtuple('Employee', ['firstname', 'lastname', 'ecode'])

# then access, can be easy
e1 = Employee('Neeraj', 'Singh', 'BH10319')

print(e1.firstname)         # Neeraj
print(e1.lastname)          # Singh
print(e1.ecode)             # BH10319

# Alternatively, namedtuple can be defined like this,

e = namedtuple('Employee', ['firstname', 'lastname', 'ecode'])
e1 = e('Neeraj', 'Singh', 'BH10319')
print(e1.firstname)       # Neeraj
````

#### EXAMPLE 2

````py
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'place'])
person = Person("Jonathan", 34, "Goa, India")

print(f"{person.name} is {person.age} years old coming from {person.place}.")
````

#### EXAMPLE 3

````py
from collections import namedtuple

# Create a list of named tuples of planets with the given csv data

csv_data = """Jupiter, 69911\nSaturn, 58232 km\nUranus, 25362 km\nNeptune,
24622 km\nEarth, 6371 km\nVenus, 6052 km\nMars, 3390 km\nMercury, 2440 km"""

# Instantiate named tuple of planet with name and radius

Planet = namedtuple('Planet', ['name','radius'])
planet_list = []

for line in csv_data.split('\n'):
  name, radius = line.split(', ')
  # Create instance of planet tuple
  planet_tuple = Planet(name, radius)
  planet_list.append(planet_tuple)
  
for planet in planet_list:
  print(f"The radius of {planet.name} is {planet.radius}")

# OUTPUT :-
# The radius of Jupiter is 69911
# The radius of Saturn is 58232 km
# The radius of Uranus is 25362 km
# The radius of Neptune is 24622 km
# The radius of Earth is 6371 km
# The radius of Venus is 6052 km
# The radius of Mars is 3390 km
# The radius of Mercury is 2440 km
````


-------------------------------------------------------------------------------------
#### Q052 : Difference list() vs [];

- The [] is just returned the location of the stored objects.
- The list() convert the old object to the new object as list.

for eg,
````py
a = (1,2,3)         
b = (4,5,6)
c = [a] + [b]
print(c)    # [(1, 2, 3), (4, 5, 6)]
c = list(a) + list(b)
print(c)    [3 1, 2, 3, 4, 5, 6]
````


-------------------------------------------------------------------------------------
### Q051 : Collection Module;;

Python provides a number of utilities and storage methods that can help 
us store our data in the most effective way. Many of these utilities are
available in the collections module.

For a `defaultdict` the default value is usually not really a value, it a
factory: a method that generates a new value.

SYNTAX : 
```py
from collections import defaultdict

dictionary = defaultdict(list)     
# here, list is a factory object or iterable objects only.
# Other options are int, float, str, dict, tuple, set etc.
```

#### ILLUSTRATION EXAMPLE  OF DEFAULT DICT;;
for eg,
```py
from collections import defaultdict

string = '''Peter Piper picked a peck of pickled peppers
A peck of pickled peppers Peter Piper picked
If Peter Piper picked a peck of pickled peppers
Where’s the peck of pickled peppers Peter Piper picked?'''

# We initialize defaultdict here and pass list to it.
# This by default assigns an empty list an any new key.
# Other options are int, float, str, dict, tuple, set etc.

position_mapping = defaultdict(list)
words = string.split()

for position, word in enumerate(words, start=1):
    position_mapping[word].append(position)

print(position_mapping)

# OUTPUT:
# defaultdict(
#   <class 'list'>, 
#   {
#     'Peter': [1, 14, 18, 32], 
#     'Piper': [2, 15, 19, 33], 
#     'picked': [3, 16, 20], 
#     'a': [4, 21], 
#     'peck': [5, 10, 22, 28], 
#     'of': [6, 11, 23, 29], 
#     'pickled': [7, 12, 24, 30], 
#     'peppers': [8, 13, 25, 31], 
#     'A': [9], 
#     'If': [17], 
#     'Where’s': [26], 
#     'the': [27], 
#     'picked?': [34]
#   }
# )
```

#### EXAMPLE 1: COUNTER IMPORTS;;

for eg,
````py
import collections

print(collections)
<module 'collections' from '/usr/lib/python3.8/collections/__init__.py'>

dir(collections)

# OUTPUT:
# ['ChainMap', 'Counter', 'Mapping', 'MutableMapping', 'OrderedDict', 'UserDict',
# 'UserList', 'UserString', '_Link', '_OrderedDictItemsView', '_OrderedDictKeysView',
# '_OrderedDictValuesView', '__all__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__getattr__', '__loader__', '__name__', '__package__', '__path__',
# '__spec__', '_chain', '_collections_abc', '_count_elements', '_eq', '_heapq',
# '_iskeyword', '_itemgetter', '_proxy', '_recursive_repr', '_repeat', '_starmap',
# '_sys', '_tuplegetter', 'abc', 'defaultdict', 'deque', 'namedtuple']
````

#### EXAMPLE 2: COUNTER MODULE;;
for eg,
````py
from collections import Counter

string = "hello"
c = Counter(string)
print(c) # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
````

#### EXAMPLE 3: MOST COMMON MODULE;;

- `most_common(n=None)` method of `collections.Counter` instance --

List the n most common elements and their counts from the most common 
to the least. If n is None, then list all element counts.

```py
Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]
```

for eg,
```py
from collections import Counter

string = '''Peter Piper picked a peck of pickled peppers
A peck of pickled peppers Peter Piper picked
If Peter Piper picked a peck of pickled peppers
Where’s the peck of pickled peppers Peter Piper picked?'''

c = Counter(string.split())
print(c.most_common(3))

# OUTPUT:
# [('Peter', 4), ('Piper', 4), ('peck', 4)]
```

#### EXAMPLE 4: DEFAULT DICTIONARY

The collections module also provides a variant of a dictionary called Default
Dictionary. A default dictionary pre initializes the values in a dictionary
to a certain type.

for eg,
````py
string = '''Peter Piper picked a peck of pickled peppers
A peck of pickled peppers Peter Piper picked
If Peter Piper picked a peck of pickled peppers
Where’s the peck of pickled peppers Peter Piper picked?'''

# CASE 1: Without default dict when non-existing key insertion;
position_mapping = {}       # normal dictionary;
words = string.split()

for position, word in enumerate(words, start=1):
  if word in position_mapping:
    position_mapping[word].append(position)
  else:
    position_mapping[word] = [position]

print(position_mapping)

# OUTPUT:
# {'Peter': [1, 14, 18, 32], 'Piper': [2, 15, 19, 33], 'picked': [3, 16, 20], 
# 'a': [4, 21], 'peck': [5, 10, 22, 28], 'of': [6, 11, 23, 29], 
# 'pickled': [7, 12, 24, 30], 'peppers': [8, 13, 25, 31], 'A': [9], 'If': [17], 
# 'Where’s': [26], 'the': [27], 'picked?': [34]}


# CASE 2: With default dict implementation; 
# Other options are int, float, str, dict, tuple, set etc.
position_mapping = defaultdict(list()) 
words = string.split()

for pos, word in enumerate(words, start=1):
    position_mapping[word].append(pos)

print(position_mapping)

# OUTPUT : 
# defaultdict(<class 'list'>, {
#         'Peter': [1, 14, 18, 32], 'Piper': [2, 15, 19, 33], 'picked': [3, 16,
#         20], 'a': [4, 21], 'peck': [5, 10, 22, 28], 'of': [6, 11, 23,
#         29], 'pickled': [7, 12, 24, 30], 'peppers': [8, 13, 25, 31], 'A':[9], 'If':
#         [17], 'Where’s': [26], 'the': [27], 'picked?': [34]
#     }
# )
````

#### EXAMPLE 5: ORDERED DICTIONARY;;

An Ordered Dictionary is a variant of a dictionary that maintains the order of
the elements in the way they were added. 

For eg,
````py
from collections import OrderedDict

data = OrderedDict()
items = [
    "cheese", "yoghurt", "tomatoes", 
    "yoghurt", "onions", "milk", 
    "milk", "cheese"
]

for item in items:
  if not(item in data):
    data[item] = 1
    continue
  data[item] += 1

print(data)

# OUTPUT:
OrderedDict(
    [ ('cheese', 2), ('yoghurt', 2), ('tomatoes', 1), ('onions', 1), ('milk', 2) ]
)
````


-------------------------------------------------------------------------------------
### Q050 : Exception Handling;;

- Exceptions are errors thrown by Python when we try to do something which we
are not allowed to or is not possible to

- The Exception class is imported by default when Python starts. We can use it
to create an Exception object with a custom message and any other details we
need. Like, 

- The Exception object takes in a variable number of arguments. So we can pass
it any number and types of data related to the error we face.

> SYNTAX:
```py
raise Exception("Failure detected.", {"data": [1, 2, 3]})
```

for eg, 
````py
# Raising Exception Example;;
age = 999
if not 1 <= age <= 100:
  raise Exception("Invalid age value provided.")  # Exception is raised;;
````

#### USAGE 1 : BASIC TRY AND CATCH;;

for eg,  
````py
# EXAMPLE 1 : KEY NOT FOUND EXCEPTION;;

countries_and_capitals = {"India": "Delhi"}
print(countries_and_capitals["England"])

# OUTPUT:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'England'

# NOTE: Execption can be handled using the exception handling.
try:
    country = countries_list[i]
    print(f"The capital of {country} is {countries_and_capitals[country]}")

except KeyError:  
    print(f"--- Key {countries_list[i]} does not exist ---")

except IndexError:
    print(f"--- Index {i} is not present in countries_list ---")


# EXAMPLE 2 : VERBOSE MESSAGE;;

try:
  40 / 0
except ZeroDivisionError as e:
  print(e)

# OUTPUT:-
# division by zero
````

#### USAGE 2 : TRY-EXCEPT-ELSE BLOCK;;

The `Else block` in a try/except statement is executed when none of the except
blocks are executed i.e no error is thrown.

for eg,
````py
countries_and_capitals = {
  "India": "Delhi",
  "United Kingdom": "London",
  "Thailand": "Bangkok",
  "Russia": "Moscow",
}

countries_list = ["India", "Russia", "China", "Thailand"]

try:
  country = countries_list[0]
  capital = countries_and_capitals[country]
  print(f"The capital of {country} is {capital}")

except KeyError:
  print("Key was not found in dictionary")

except IndexError:
  print("Index does not exist in List")

else: # <--- Else Block
  print("No Error Occurred")

# OUTPUT :- 
# The capital of India is Delhi
# No Error Occurred
````

#### USAGE 3 : FINALLY BLOCK;;

The `finally block` in a try-except statement, contains code that will be 
run irrespective of if there was an error or not i.e It will always be run.

for eg,
````py
countries_and_capitals = {
  "India": "Delhi",
  "United Kingdom": "London",
  "Thailand": "Bangkok",
  "Russia": "Moscow",
}

countries_list = ["India", "Russia", "China", "Thailand"]

try:
  country = countries_list[4]
  capital = countries_and_capitals[country]
  print(f"The capital of {country} is {capital}")

except KeyError:
  print("Key was not found in dictionary")

except IndexError:
  print("Index does not exist in List")

else:
  print("No Error Occured")

finally:
  print("Runs irrespective of occurrence of error.")

# OUTPUT:-
# Index does not exist in List
# Runs irrespective of occurrence of error.
````

#### USAGE 4 : CREATE CUSTOM EXCEPTION;;

While we can use the Exception class to create and raise new errors but it is
not the recommended method. The Exception class does not distinguish between
different types of errors. It is a broad and generic class that classifies
all exceptions the same way.

To help exception handlers (try-except block) distinguish between errors, we
create a child exception class.

for eg,
````py
age = 999

class InvalidAgeException(Exception): # <-- inherit from Exception

  # Constructor Method;
  def __init__(self, age, message=None):
    self.age = age
    self.message = message

  # Custom Formatting Method;
  def __str__(self):
    return f"{self.age} should be in range 1 - 100"


# EXAMPLE 1 : WITHOUT TRY AND CATCH BLOCK;
if not(1 <= age <= 100):
  raise InvalidAgeException(age, "Invalid Age Provided")

# OUTPUT: EXCEPTION WILL OCCURRED LIKE THIS,
# Traceback (most recent call last):
#   File "script.py", line 12, in <module>
#     raise InvalidAgeException(age, "Invalid age value provided.")
# __main__.InvalidAgeException: 999 is not in the range of 1 - 100


#--- EXAMPLE 2: WITH TRY AND CATCH ERROR BLOCK;;
try:
  if not(1 <= age <= 100):
    raise InvalidAgeException(age, "Invalid age value provided")

except InvalidAgeException: # <-- Handler for age related errors 
  print("Please enter a valid age in the input")

except Exception:
  print("Some error occurred")

# OUTPUT:
# Please enter a valid age in the input
````

#### USAGE 5: RE-RAISING EXCEPTION IN PYTHON;;

Python also allows us to re-raise a handled exception. 

for example, we might want to first capture an error that occurs in our
try-except block and store its details in some file. Then we would want to
continue to raise that exception so that it can be handled at a higher
level.

for eg, 
````py
# ILLUSTRATION OF RE-RAISING EXCEPTION;;

age = 999       # Given, age

def errorLogging(e):
  print("Store Log here...")

class InvalidAgeException(Exception):
  pass

if__name__ == "__main__":
  try:
    if not(1<= age <= 100):
      raise InvalidAgeException("Exception : Invalid Age Found !!!")

  except InvalidAgeException as err:
    # Here, Storing the log to the file;
    errorLogging(err)

    # then again raising the error;
    raise(err)

  except Exception as e:
    print("Exception Traced Here : ", e)

  finally:
    print("Finally Block Executed !")

# OUTPUT:-
# Traceback (most recent call last):
#   File "script.py", line 15, in <module>
#     raise e# <-- re raise the exception
#   File "script.py", line 12, in <module>
#     raise InvalidAgeException("Invalid age value provided.")
# __main__.InvalidAgeException: Invalid age value provided.
````

#### USAGE 6: REAL LIFE SCENARIO;; 

````py
#------------------------------ TASK --------------------------------------------#
# Mr.Sharma wants you to design a login screen where the user has 3 attempts to  
# login into his website.
# 
# Given below is a code snippet that authenticates a user using their email and
# password. If the password does not match, a WrongPasswordError is raised.
# 
# Your task is to capture this exception and reduce the number of login attempts
# by 1. Re-raise the exception once this is done.
#--------------------------------------------------------------------------------#
# Handle WrongPasswordError and reduce attempts. 
# Re raise the exception once done.
#--------------------------------------------------------------------------------#

# SOLUTION HERE...

attempts = 2
email, password = "username@gmail.com", "pasword"

class WrongPasswordError(Exception):
  pass

try:

  try:
    if not (email == "username@gmail.com" and password == "password"):
      raise WrongPasswordError()

  except WrongPasswordError as err:
    # Attempts Calculate, here
    attempts -= 1
    raise(err)

except:
  print(f"Please try again. You have {attempts} left")

# OUTPUT:
# Please try again. You have 1 left
````


-------------------------------------------------------------------------------------
### Q049 : List or Variable Destructuring;;

#### USAGE 1: BASIC DESTRUCTING;
For eg,
```py
animal, bird, insect = "Dog", "Eagle", "Ant"
print(animal, bird, insect)
Dog Eagle Ant
```

#### USAGE 2: TUPLE;
for eg,
````py
animals = ('dog', 'cat', 'elephant')
print(type(animals))   # <class 'tuple'>

a1, a2, a3 = animals
print(a1,'~', a2, '~', a3)  # dog ~ cat ~ elephant
print(animals)  # ('dog', 'cat', 'elephant')
````

#### USAGE 3: VARIABLE ARGUMENT;
for eg,
````py
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
a, b, c, *var = numbers

print(a,b,c) # 1 2 3
print(type(var))    # <class 'list'>
print(var)  # [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(type(numbers))    # <class 'tuple'>
````

#### USAGE 4: DICTIONARY DESTRUCTING;
for eg,
````py
countries_and_capitals = {
...   "USA": "Washington D.C",
...   "India": "New Delhi",
...   "China": "Beijing",
...   "England": "London"
... }

for country, capital in countries_and_capitals.items():
...   print(f"The capital of {country} is {capital}")
...

# OUTPUT:
# The capital of USA is Washington D.C
# The capital of India is New Delhi
# The capital of China is Beijing
# The capital of England is London
````

#### USAGE 5: ENUMERATE FUNCTION;
for eg,
````py
names = ["Ricky", "Justin", "Bob"]

for index, name in enumerate(names):
...   print(f"The value at index {index} is {name}")
... 
The value at index 0 is Ricky
The value at index 1 is Justin
The value at index 2 is Bob
````

#### USAGE 6: NEGATIVE NUMBER;
for eg,
````py
colors = ["red", "pink", "white", "yellow", "grey", "blue"]
print(f"The last element in the list is {colors[-1]}")
# The last element in the list is blue

print(f"The second last element in the list is {colors[-2]}")
# The second last element in the list is grey

print(f"The third last element in the list is {colors[-3]}")
# The third last element in the list is yellow


# Traverse in Reverse order using for loop;;
nums = (1,2,2,3,0,5,5,6,6,76,7,7)

for i in range(len(a)-1, -1, -1):
    print(num[i], end=" ")  # 7 ,7 ,76 ,6 ,6 ,5 ,5 ,0 ,3 ,2 ,2 ,1
  
````

#### USAGE 7: SLICING
for eg,
````py
colors = ["red", "pink", "white", "yellow", "grey", "blue"]
print(colors[0:4])
# ['red', 'pink', 'white', 'yellow']

print(colors[3: 6])
# ['yellow', 'grey', 'blue']

print(colors[4:])
# ['grey', 'blue']

print(colors[:4])
# ['red', 'pink', 'white', 'yellow']
````

#### USAGE 8: MAP
for eg,
````py
names = ["Neeraj", "Mathews", "Jack"]
unames = map(lambda x: x + f"(@{x})", names)

print(unames)   # <map object at 0x7f7241dce430>
print(list(unames))     # ['Neeraj(@Neeraj)', 'Mathews(@Mathews)', 'Jack(@Jack)']
````

#### USAGE 9: LIST COMPREHENSION

List comprehension is an inline for loop, which can be used to quickly iterate
over and process elements of a list.

SYNTAX :
```
[
    (return value) for value in list if (condition)
]
```

for eg,
````py
# Example 1:
names = ["Tom", "Bob", None, "Shirley", None, "Kajal"]
filtered_names = [f"Mr.{name}" for name in names if name is not None]

print(filtered_names)

# OUTPUT:
# ['Mr.Tom', 'Mr.Bob', 'Mr.Shirley', 'Mr.Kajal']
````


-------------------------------------------------------------------------------------
### Q048 : String Helpers Methods;;

#### PYTHON METHOD :: Join() 

Just like separating words into a list using a .split(), we can also join a
list of strings into a sentence using .join().

```py
# Example 1
characters = ["Gangadhar", "Geetha", "Kilvish", "Dr.Jackal"]
print(', '.join(characters))

# OUTPUT :
# Gangadhar, Geetha, Kilvish, Dr.Jackal

# Example 2: 
characters = ["Gangadhar", "Geetha", "Kilvish", "Dr.Jackal"]
print(f"The main characters in Shaktimaan were {', '.join(characters)}")

# OUTPUT :
# The main characters in Shaktimaan were Gangadhar, Geetha, Kilvish, Dr.Jackal
```

#### PYTHON USEFULL STRING METHOD;;

Convert lowercase and uppercase of letter.

for eg, 
````py
# // lowercase 
text = "PUT YOUR HANDS IN THE AIR."
print(text.lower())     # put your hands in the air.

# // upper
text = "put your hands in the air."
print(text.upper())     # PUT YOUR HANDS IN THE AIR.

# // capitalize()
text = "i am the king"
print(text.capitalize())    # I am the king

# // remove extra spaces from string
text = " x "
print(text, f"len: {len(text)}") # x, len: 3

text = text.strip()
print(text, f"len: {len(text)}") # x, len: 1

# // find index of character in word
txt_idx = "The dishes served are Mutton, Soup, Salad".find("Soup")
print(f"The Index of Soup is {txt_idx}")

# // count the appearance of particular letter;
txt = "The dishes served are Mutton, Soup, Salad".find("Soup")
txt_count = txt.count("e") # Returns 0 if the text is not found
print(f"The Count of letter 'e' is {txt_count}")

# // Replace a word;
txt = "The dishes served are Mutton, Soup, Pulav, Chicken, Salad"
txt_count = text.replace("Soup", "Curry")
print(txt_count)

# OUTPUT :
# The dishes served are Mutton, Curry, Pulav, Chicken, Salad

# // Check is string is digit;
print("4532".isdigit()) # check for digit;
print("4efef".isalpha()) # check for alphabet;
print("45.32".isalnum()) # check for alpha-numeric;
print("45.32".isnumeric()) # check for fractions, superscripts, and Unicode numbers.;

# // Select Subset of string;
movie="Spiderman: No Way Home"

# Output:
print(f"The first character is {movie[0]}")
# The first character is S

print(f"The last character is {movie[-1]}") # gets the last character
# The last character is e

print(f"The length of the string is {len(movie)}")
# The length of the string is 22

print(movie[::-1])                                  # emoH yaW oN :namredipS
print(movie[-1])                                    # e
print(movie[-2])                                    # m
print(movie[-7:-2])                                 # ay Ho
print(movie[0:len(movie)-4])                        # Spiderman: No Way 
````


-------------------------------------------------------------------------------------
### Q047 : Dictionary and Operation;;

#### DICT :

Python provides an in-built way of storing key-value pairs. These are called
Dictionaries and can be declared using dict() or {}.

#### OPERATION :
```py
# // Initialization;
fruits_and_colors = {
   "grapes": "green",
   "apple": "red",
   "banana": "yellow",
   "orange": "orange"
}

print(fruits_and_colors)
# {'grapes': 'green', 'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

print(fruits_and_colors['apple'])
# red

# // or 
for k,v  in fruits_and_colors.items():
 print(f"{k} are {v} in colours")

# OUTPUT:
# grapes are green in colours
# apple are red in colours
# banana are yellow in colours
# orange are orange in colours

# // Setting Default Values;
print(fruits_and_colors.get('mango', 'NOT FOUND'))  # NOT FOUND

# // Inserting Values;
fruits_and_colors['sapodilla'] = "brown"
print(fruits_and_colors)
# OUTPUT:
# {
#     'grapes': 'green', 
#     'apple': 'red', 
#     'banana': 'yellow', 
#     'orange': 'orange', 
#     'sapodilla': 'brown'
# }

# // Delete Values from Dictionary;

## METHOD 1: Delete using del keyword;
## To delete a key-value pair from the dictionary we can use the del keyword.

print(fruits_and_colors)

# OUTPUT:
# {
#     'grapes': 'green', 'apple': 'red', 
#     'banana': 'yellow', 'orange': 'orange', 
#     'sapodilla': 'brown'
# }

del fruits_and_colors['apple']  

print(fruits_and_colors)
# OUTPUT:
# {
#     'grapes': 'green', 
#     'banana': 'yellow', 
#     'orange': 'orange', 
#     'sapodilla': 'brown'
# }

## METHOD 2: Delete using pop keyword;
## Pop can also used for deleting element as well. 
## Difference here is pop returned the delte value. 

print(fruits_and_colors)

# OUTPUT:
# {
#     'grapes': 'green', 'banana': 'yellow', 
#     'sapodilla': 'brown'
# }

fruit = fruits_and_colors.pop('sapodilla')

print(fruits_and_colors)
# OUTPUT:
# {'grapes': 'green', 'banana': 'yellow'}

# // Merge Dictionary using updated() method:
states = {'delhi', 'goa'}
states_2 = {'uttrakhand', 'uttar pradesh'}
states.update(states_2)

print(f"type: {type(states)}, states: {states}")
# OUTPUT:
# type: <_class 'set'>
# {
#     'uttrakhand', 
#     'delhi', 'uttar pradesh', 'goa'
# }
```

-------------------------------------------------------------------------------------
### Q046 : Set and Operation;;

#### SET :- 
- It is unqiue collection of number. It can include the numbers, string, list,
  tuple, dictionary.
- Set can be defined using the helper method set() or similary can be defined
  using the brackets {}. But remember the brackets can't be initialized
  empty. 

**NOTE : EMPTY BRACKETS {} IS CONSIDERED AS DICTIONARY NOT SET;**

#### OPERATIONS :
````py
# Initialization;
a = {1,2,3,4,5}
b = {1,3,5,7,9}

# Intersection; 
print(a.intersection(b))
# {1, 3, 5}

# or 
print(a & b)
# {1, 3, 5}

# Union;
print(a.union(b))
# {1, 2, 3, 4, 5, 7, 9}
print(a|b)
# {1, 2, 3, 4, 5, 7, 9}

# Difference;
print(a.difference(b))
# {2, 4}
print(b.difference(a))
# {9, 7}
# or
print(a-b)
# {2, 4}
print(b-a)
# {9, 7}

# issubset()
a = {1,2,3}
b = {1,2,3,4,5,6,7,8,9,10}
print(a.issubset(b))
# True
````

-------------------------------------------------------------------------------------
### Q045 : List and Operations;;

#### LIST;;
- `List`: It is a heterogeneous collection of items 
  - numbers
  - string
  - child list
  - child tuple 
  - dictionary 

#### TUPLE;;

- `Tuples` are similar to Lists except that they cannot be modified. We cannot
  add or remove elements from a tuple once declared.
- Tuples are `read-only` and can only be accessed or searched for elements.
- We can declare a tuple using the () brackets.

#### OPERATION : -
````py
# // Initialization;
fruits = ['animal', 'grapes','guawa', 'banana','mango', 'orange']
print(fruits)
# ['animal', 'grapes', 'guawa', 'banana', 'mango', 'orange']

# // remove operation;
fruits.remove('banana')
print(fruits)
# ['animal', 'grapes', 'guawa', 'mango', 'orange']

# // pop operation default;
fruits.pop()    # 'orange'
print(fruits)
# ['grapes', 'guawa', 'mango']

# // pop operation index provided;
fruits.pop(0)
'animal'
print(fruits)
['grapes', 'guawa', 'mango', 'orange']

# // append operation;
fruits.append('oranges')
print(fruits)
['grapes', 'guawa', 'mango', 'oranges']

# // Accessing list;
for fruit in fruits:
    print(fruit)
    
# OUTPUT 
# grapes
# guawa
# mango
# oranges

# // len of list;
print(len(fruits))  # 6

# // Search a List
print('banana' in fruits) # False
print('guawa' in fruits)
# True


# Remove, pop simultaneously;;
fruits = ['animal', 'grapes','guawa', 'banana','mango', 'orange']

print(fruits, "--->", fruits.remove("animal"))
print(fruits, "--->", fruits.pop())
print(fruits, "--->", fruits.pop(0))
print(fruits)

# OUTPUT:
# ['grapes', 'guawa', 'banana', 'mango', 'orange'] ---> None
# ['grapes', 'guawa', 'banana', 'mango'] ---> orange
# ['guawa', 'banana', 'mango'] ---> grapes
# ['guawa', 'banana', 'mango']

# NOTE: Observe, Even though in every print statement we are first printing the
# fruits and then doing the operation like, remove/pop/pop(index). 
# But in the output, python kinda doing the operation(remove/pop) first, then
# updating the memory reference of the object, then printing the snapshot of
# the memory location. 

````


-------------------------------------------------------------------------------------
### Q044 : Padding Number using F-String;

Sometimes we would like to print our numbers with a fixed length. For example,
printing military time. i.e, 0900 hours, we can use the inbuilt string
formating syntax to print numbers in a fixed length.

In the example below, basically padding or inserting zero to the left of the 
number, if the number has less than 4 digits.

> Syntax: **`number = f"{x:0yz}"`**
 
where, 
- x is the initial number. For eg 9
- y is the number of times you want to add the padding. For eg, 5
- z is the data type. For eg, `d for digit`, `f for float value`.
- for eg, number = `f"{9:05d}` will result `00009`
- for eg, number = `f"{9:05f}"` will result `9.0000`


#### **Understanding `:05d` vs `:05f` Formatting in Python**

- `:05d` → Integer formatting (`d`) with zero-padding (`0`) and a minimum width of `5`.
- `:05f` → Floating-point formatting (`f`) with six decimal places by default.

---

#### **Case 1: `:05d` (Integer Formatting)**

```py
print(f"digit: result: {9:05d}")       # 00009
print(f"digit: result: {99:05d}")      # 00099
print(f"digit: result: {999:05d}")     # 00999
print(f"digit: result: {9999:05d}")    # 09999
print(f"digit: result: {99999:05d}")   # 99999
```

**Breakdown:**
- **`0` (Zero-padding)** → Adds leading zeros to fill the width.
- **`5` (Minimum Width)** → Ensures the number takes at least 5 characters.
- **`d` (Integer format)** → Ensures the value is treated as an integer.


**Note:** If the number **exceeds** the given width (`5`), it prints
  as-is **without truncation**.

```py
print(f"digit: result: {9999999:05d}")   # 9999999
```

---

#### **Case 2: `:05f` (Floating-Point Formatting)**

```python
print(f"float: result: {9:05f}")     # 9.000000
print(f"float: result: {99:05f}")    # 99.000000
print(f"float: result: {999:05f}")   # 999.000000
print(f"float: result: {9999:05f}")  # 9999.000000
print(f"float: result: {99999:05f}") # 99999.000000
```

**Breakdown:**
- `0` (Zero-padding) is ignored for floats.
- `5` (Minimum Width) is ignored when width is smaller than the default float format.
- `f` (Fixed-point notation)** → Ensures **six decimal places** (`.000000`).


**Key Observation:**
Unlike integers, the `0` and `5` **do not** force zero-padding before the
decimal. Instead, floats are printed with **6 decimal places** by default.

---

#### **Case 3: `:05f` (Floats with decimal values)**

```python
print(f"float: result: {0.9:05f}")    # 0.900000
print(f"float: result: {0.99:05f}")   # 0.990000
print(f"float: result: {999:05f}")    # 999.000000
print(f"float: result: {9999:05f}")   # 9999.000000
print(f"float: result: {99999:05f}")  # 99999.000000
```

**Breakdown:**

- `0.9` and `0.99` are small, so **they do not get zero-padded before the decimal.
- The default behavior ensures **six decimal places.**
- Larger numbers behave similarly to integers.

**Key Takeaways:**
- The `0` padding does not affect floating-point values before the decimal.
- Floats always show 6 decimal places unless specified differently
  (`.2f`, `.3f`, etc.).

---

## **Final Summary**

- `:05d` : Integers : Zero-pads the number to at least 5 characters.
- `:05f` : Floats   : Shows 6 decimal places, but `0` and `5` are ignored
  before the decimal.


-------------------------------------------------------------------------------------
### Q043 : Join() vs Format() in Python;

#### PYTHON FORMAT :: format()

The `format()` method is a powerful tool that allows developers to create
formatted strings by embedding variables and values into placeholders within
a template string.
   
for eg, 
````py
###--- Example 0:
fname, mname, lname = "Neeraj", "Singh", "Junior"
v = "f : {0}, m: {1}, l: {2}".format(fname, mname, lname)
print(v)
# f : Neeraj, m: Singh, l: Junior

###--- Example 1:
v = "f : {2}, m: {1}, l: {0}".format(fname, mname, lname)
print(v)
# f : Junior, m: Singh, l: Neeraj

###--- Example 2:
v = "f : {f}, m: {m}, l: {l}".format(fname, mname, lname)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# KeyError: 'f'

###--- Example 3:
v = "f : {f}, m: {m}, l: {l}".format(f=fname, m=mname, l=lname)
print(v)
# f : Neeraj, m: Singh, l: Junior
````

#### PYTHON JOIN :: join()

The `join()` method takes all items in an iterable and joins them into one
string. A string must be specified as the separator.

for eg,
````py
###--- Example 1:
numList = ['1', '2', '3', '4']
print(','.join(numList))    
# OUTPUT: '1,2,3,4'

###--- Example 2:
''.join(['A', 'B', 'C'])
# OUTPUT: 'ABC'

''.join({'A': 0, 'B': 0, 'C': 0}) # note that dicts are unordered
# OUTPUT: 'ACB'

'-'.join(['A', 'B', 'C'])  # '-' string is the seprator
# OUTPUT: 'A-B-C' 

###--- EXAMPLE 3: PRINT DATA IN TABLE FORMAT;
headers = ["Name" ,"Age","Phone","City"]
data = [
  ['Tom', '25', '9838572948', 'Kochi'],
  ['Bob', '29', '8273885932', 'Delhi'],
  ['Rob', '45', '9273285631', 'Miami'],
]

print("-----------------------------------------------------")
print("\t|\t".join(headers))
print("-----------------------------------------------------")
for record in data:
  print("\t|\t".join(record))
print("-----------------------------------------------------")

# OUTPUT:
"""
-------------------------------------------------------------
Name    |   Age |   Phone   |   City
-------------------------------------------------------------
Tom |   25  |   9838572948  |   Kochi
Bob |   29  |   8273885932  |   Delhi
Rob |   45  |   9273285631  |   Miami
-------------------------------------------------------------
"""
````


-------------------------------------------------------------------------------------
### Q042 : Python Conventions;

#### Variable Naming Conventions;

- Tip #1: Variable names should only contain alpha numeric characters.

for eg,
````py
H3LL0_W0RLD = "Hello World" # valid variable name
$uper$t@r = "superstar" # not a valid variable
````

- Tip #2: Variables names cannot start with a number.

for eg,
````py
oceans_12 = "movie" # valid variable name
13_reasons_why = "series" # not a valid variable
````

- Tip #3: Variable names are case sensitive.

for eg,
````py
ANIMAL = "cow" # valid variable name
ANiMaL = "pig" # valid variable name
AnIMal = "crocodile" # valid variable name

print(ANIMAL)   # cow
print(ANiMaL)   # pig
print(AnIMal)   # crocodile
````

- Tip #4: Python variables are generally declared in snake case

for eg,
````py
no_of_animals = 13      # recommended
noOfAnimals = 13        # not recommended
````


-------------------------------------------------------------------------------------
-> Q041 : Python Operator Precedance;;

#### Operator Precedance :
````
 ------------------------------
|    Operators   Priority      |
|        ()          1         |
|        **          2         |
|    *, /, //, %     3         |
|        +, -        4         |
 ------------------------------
````

#### PRIORITIES :-
```
() : It has the highest priority.
** : Exponent will be executed second after the brackets.
*, /, //, % : They all the same priority.
+, - : They have the same priority.
```


-------------------------------------------------------------------------------------
### Q040 : Encryption vs Hashing

#### ENCYRPTION:
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
        modified in transit, it would not be able to be re-encrypted with the
        private key

        Asymmetric Encryption Algorithms:

            1) Elliptic Curve Digital Signature Algorithm (ECDSA)
            2) Rivest-Shamir-Adleman (RSA)
            3) Diffie-Hellman
            4) Pretty Good Privacy (PGP)

    b) Symmetric Encryption : 
        
        Symmetric encryption uses the same key for both encryption and
        decryption. This type of encryption uses less processing power and is
        faster, but is less secure as only one key is used

        Symmetric Encryption Algorithms:

            1) Advanced Encryption Standard (AES)
            2) Blowfish
            3) Twofish
            4) Rivest Cipher (RC4)
            5) Data Encryption Standard (DES)

#### HASHING:

- Hashing, on the other hand, is one-way, meaning the plaintext is scrambled
  into a unique digest, through the use of a salt, that cannot be decrypted.

-  Hashing Algorithms:

    1) Message Digest Algorithm (MD5)
    2) Secure Hashing Algorithm (SHA-1, SHA-2, SHA-3)
    3) WHIRLPOOL
    4) TIGER
    5) Cyclical Reduction Check (CRC32)

#### HASHING USE CASES:

1) One of the uses for hashing is to compare large amounts of data. Hash
values are much easier to compare than large chunks of data, as they are more
concise.

2) Hashing is also used for mapping data, as finding values using hashes is
quick, and good hashes do not overlap.

3) Hashes are used in digital signatures and to create random strings to avoid
duplication of data in databases too.

4) hashing is extremely infeasible to reverse, hashing algorithms are used on
passwords. This makes the password shorter and undiscoverable by attackers.

#### ENCRYPTION USE CASES:

1) Encryption tends to be used for encrypting data that is in transit. Data
being transmitted is data that needs to be read by the recipient only, thus
it must be sent so that an attacker cannot read it.

2) Encryption hides the data from anyone taking it in the middle of transit,
and allows only the decryption key owner to read the data

3) Encryption would be used over hashing is for storing and retrieving data in
databases, authentication methods, and other cases where data must be hidden
at rest, but retrieved later.


-------------------------------------------------------------------------------------
### Q039: What is C3 Linearization in Multiple Inheritance;;

*(Refer Q083 : Method Resolution Order in Python)*

The `C3 Linearization`, often referred to as `C3 superclass linearization`, is
an algorithm used in the context of multiple inheritance to determine the
order in which base classes are considered during method resolution.

The C3 Linearization algorithm is used in languages like Python to address the
`diamond problem` and provide a clear order for method lookup.

In this example, class D inherits from both B and C, both of which inherit
from A. 

The `diamond problem` occurs because there are multiple paths to reach class A
through the inheritance hierarchy.

for eg,
````py
class A:
    def foo(self):
        print("A")

class B(A):
    def foo(self):
        print("B")

class C(A):
    def foo(self):
        print("C")

class D(B, C):
    pass

d = D()
d.test()    # B
C.test(d)   # C
A.test(d)   # A

print(D.__mro__)

# Output (MRO define the order of linearization) 
# (<class '__main__.D'>, <class '__main__.B'>, 
# <class '__main__.C'>, <class '__main__.A'>, 
# <class 'object'>)
````    

#### C3 Linearization:

1. Start with the Class:
- Begin with the class itself (D in this case).

2. Consider the Parent Classes:
- Consider the parent classes in the order they are listed in the class
  definition(B and C). 
- Check their parents in a similar way, maintaining the order.

3. Merge Lists:
- Merge the lists of parent classes, ensuring that the order is preserved, and
  duplicates are removed.
- Keep track of the original order of classes from each list. 
 
4. Check Consistency:
- Ensure that the resulting linearization is consistent and respects the order of 
inheritance.

#### Applying C3 Linearization:

For class D in the given example:

1. Start with D.
2. Consider parents B and C.
3. Merge lists: D, B(A), C(A).
4. Resulting linearization: D, B, C, A. (Refer MRO in the example)

So, the C3 Linearization for class D is D, B, C, A. This order ensures that method 
resolution follows a consistent path, and in case of a method conflict, the method 
from the first class in the linearization is chosen.

#### Method Resolution:
Now, when calling the foo method on an instance of D
````
d_instance = D()
d_instance.foo()
````

The output will be "B" because B comes before C in the C3 linearization order.

This example demonstrates how C3 Linearization helps in establishing a clear and 
predictable order for method resolution in the presence of multiple inheritance.


-------------------------------------------------------------------------------------
### Q038: Multiple Inheritance in Python vs Java;;

*(Refer Q039: What is C3 Linearization in Multiple Inheritance)*

Multiple inheritance in Python and Java is approached differently, and the
design choices in each language contribute to the perceived safety or
challenges of multiple inheritance.

#### PYTHON :

1) C3 Linearization (C3 superclass linearization):
- Python uses the C3 linearization algorithm to determine the order in which
  base classes are considered during method resolution.
- This algorithm ensures a consistent and predictable order for method lookup
  in the presence of multiple inheritance.
- It prevents the `diamond problem`, where ambiguity could arise from the use
  of shared base classes.

2. Mixin Pattern:
- Python encourages the use of mixins, which are small, focused classes that
  provide a specific set of behaviors.
- Mixins can be combined using multiple inheritance to create composite
  classes with a combination of behaviors.

3. Super() Function:
- Python's `super()` function provides a way to call methods from the parent
  class in a cooperative manner.
- It allows for a clear and predictable delegation of method calls in the
  inheritance hierarchy.

#### JAVA :

In Java, multiple inheritance is not supported with classes, but it is
supported with interfaces. However, challenges can arise, and the reasons
include:

1) Diamond Problem:

- Java interfaces support multiple inheritance, but when a class implements
  multiple interfaces with conflicting methods, it can lead to the `diamond
  problem`.
- The diamond problem occurs when a class inherits from two classes that have
  a common ancestor, resulting in ambiguity.

2) Lack of C3 Linearization:

- Unlike Python, Java does not use a C3 linearization algorithm, which means
  that the order of method resolution may not be as predictable.
- This can lead to challenges when dealing with complex inheritance hierarchies.

3) Interface Default Methods:

- Java 8 introduced default methods in interfaces, allowing the inclusion of
  method implementations in interfaces.
- While this provides a form of multiple inheritance, it can also lead to the
  diamond problem and method ambiguity.


-------------------------------------------------------------------------------------
### Q037: Method Overloading and Operator Overloading;;

#### METHOD OVERLOADING;;

Method overloading in Python is achieved by defining multiple methods in the
same class with the same name but different signatures.

for eg,
````py
class MyClass:
    
    def add_sum(self, x, y):
        return x + y
    
    def add_sum(self, x, y, c=0):
        return x + y + c
    

# Creating an instance
obj = MyClass()

# Calling the method with one or two arguments
result1 = obj.add_sum(5, 3)
result2 = obj.add_sum(5, 2, 5)

print(result1)  # Output: 8
print(result2)  # Output: 12
````

#### OPERATOR OVERLOADING;;

- Operator overloading allows you to define how operators behave for objects 
of a class. 
- This is achieved by defining special methods in the class that start and end 
with double underscores (__). 
- For example, to overload the + operator, you can define the __add__ method.

for eg,
````py
class test:
    
    def __init__(self, a, b):
        self.a, self.b = a,b
    
    def __sub__(self, other):
        left = self.a + self.b
        right = other.a + other.b
        return abs(left - right)
    
    def __add__(self, other):
        left = self.a + self.b
        right = other.a + other.b
        return left + right
    
    def __truediv__(self, other):
        left = self.a + self.b
        right = other.a + other.b
        return left/right
    
    def __mul__(self, other):
        left = self.a + self.b
        right = other.a + other.b
        return left*right
    
    def __mod__(self, other):
        left = self.a + self.b
        right = other.a + other.b
        return left%right
        

obj1 = test(5,5)
obj2 = test(4,4)

print("__add__:", obj1+obj2)    # __add__: 18
print("__sub__:", obj1-obj2)    # __sub__: 2
print("__truediv__:", obj1/obj2) # __truediv__: 1.25
print("__mul__:", obj1*obj2) # __mul__: 80
print("__mod__:", obj1%obj2) # __mod__: 2
````

**NOTE: Python In-Build function name W.R.T Operators.**

- Addition (c1 + c2): `c1.__add__(c2)`
- Subtraction (c1 - c2): `c1.__sub__(c2)`
- Multiplication (c1 * c2): `c1.__mul__(c2)`
- Power (c1 ** c2): `c1.__pow__(c2)`
- Division (c1/c2): `c1.__truediv__(c2)`
- Floor Division (c1//c2): `c1.__floordiv__(c2)`
- Remainder(c1 % c2) : `c1.__mod__(c2)`
- Bitwise Left Shift(c1 << c2) : `c1.__lshift__(c2)`
- Bitwise Right Shift(c1 >> c2) : `c1.__rshift__(c2)`
- Bitwise AND	(c1 & c2) : `c1.__and__(c2)`
- Bitwise OR (c1 | c2) : `c1.__or__(c2)`
- Bitwise XOR (c1 ^ c2) : `c1.__xor__(c2)`
- Bitwise NOT (~c1) : `c1.__invert__()`


-------------------------------------------------------------------------------------
### Q036: Switch alternative in python;;

#### Case 1: Switch case using if-else;
````py
def switch(value):
	if(value == 1):	
        return value*10
	elif(value == 2): 
        return value*20
	elif(value == 3): 
        return value*30
	else: 
        return value

print(switch(value=3))	# switch function in python
````

#### Case 2: Switch using dict;
````py
switch = {
	1: lambda: 1*10,
	2: lambda: 2*20,
	3: lambda: 3*30,
}

print(switch.get(1, 1)) # 10
print(switch.get(2, 2)) # 40
````


-------------------------------------------------------------------------------------
### *** Q035 : ???;;



-------------------------------------------------------------------------------------
### Q034 : Python OOPS Basic Architecture;;

#### OOPS : Basic Oops Vs Procedural Programming:

- Object-oriented programming (OOP) is a method of structuring a program by
bundling related properties and behaviors into individual objects

- Procedural Programming, which structures a program like a recipe in that it
provides a set of steps, in the form of functions and code blocks, that flow
sequentially in order to complete a task.

#### OOPS : Python OOPs Basic

- Classes are used to create user-defined data structures. 

- Classes define functions called methods, which identify the behaviors and
  actions that an object created from the class can perform with its data.

for eg,
````py
class Dog:
    
    def __init__(self, name, color, hair):
        self.name = name
        self.color = color
        self.hair = hair

    def bark(self):
        print(f"{self.name}... Bow Bow !!!")

    def __repr__(self):
        return f"Meet My Dog: {self.name}"


if __name__ == "__main__":
    milly = Dog("Milly", "White", "Silky") # <__main__.Dog object at 0x0004ccc90>
    print("Dog: ", milly)
    milly.bark()
````

#### OOPS : Inheritance in Python

- Inheritance is the process by which one class takes on the attributes and
  methods of another. 

- Newly formed classes are called `child classes`, and the classes that child
  classes are derived from are called `parent classes`.

- Child classes can override or extend the attributes and methods of parent
  classes

for eg,
````py
class Pet:
    def __init__(self, name, color, hair):
        self.name = name
        self.hair = hair
        self.color = color

    def bark(self):
        print(f"{self.name}... Aww Aww!!!")


class Dog(Pet):
    
    def __init__(self, name, color, hair, type):
        super().__init__(name, color, hair)
        self.type = type

    def bark(self):
        print(f"{self.name}... Bow Bow !!!")

    def __repr__(self):
        return f"Meet My Dog: {self.name}"


class Cat(Pet):
    
    def __init__(self, name, color, hair, type):
        super()__init__(name, color, hair)
        self.type = type

    def bark(self):
        print(f"{self.name}... Meow Meow !!!")

    def __repr__(self):
        return f"Meet My Cat: {self.name}"

if __name__ == "__main__":

    snobell = Dog("Snobell", "White", "Curly", "CAT") # <__main__.Dog object at 0x0004ccc99>
    milly = Dog("Milly", "White", "Silky", "DOG") # <__main__.Dog object at 0x0004ccc90>

    print("Hello, ", milly)     # Hello, Meet My Dog: Milly
    print("Hello,", snobell)    # Hello, Met My Cat: Snobell

    milly.bark()    # Milly... Bow Bow
    snobell.bark()  # Snobell... Meow Meow

    print(f"Is Milly is a Dog ? ... {isinstance(milly, Dog)}")
    print(f"Is Snobell is a Cat ? ... {isinstance(snobell, Cat)}")
````

-------------------------------------------------------------------------------------
### Q033: ABCMeta, AbstractClass, abstractmethod in ABC package;;

#### BASIC USAGE OF ABSTRACT CLASS:

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
````py
class Fruit:
    def check_ripeness(self):
        raise NotImplementedError("method not implemented!")

class Apple(Fruit):
    pass

a = Apple()
a.check_ripeness() # raises NotImplementedError
````

#### ABSTRACT CLASS PACKAGE :

Abstract base classes (ABCs) enforce what derived classes implement particular
methods from the base class.

To understand how this works and why we should use it, let's take a look at an
example that Van Rossum would enjoy. 

Let's say we have a Base class "MontyPython" with two methods (joke & punchline) 
that must be implemented by all derived classes.

for eg,
````py
class MontyPython:
    def joke(self):
        raise NotImplementedError()

    def punchline(self):
        raise NotImplementedError()

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"
        
# When we instantiate an object and call it's two methods, 
# we'll get an error (as expected) with the punchline() method.

sketch = ArgumentClinic()
sketch.joke()   # Hahahahahah 
sketch.punchline()  # NotImplementatoin Error Raised;;
````
However, this still allows us to instantiate an object of the ArgumentClinic 
class without getting an error. In fact we don't get an error until we look 
for the punchline().

This is avoided by using the Abstract Base Class (ABC) module. 

Let's see how this works with the same example:

for eg,
````py
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


# This time when we try to instantiate an object from the 
# incomplete class, we immediately get a TypeError!

c = ArgumentClinic()

# OUTPUT:
# TypeError: "Can't instantiate abstract class ArgumentClinic 
# with abstract methods punchline"
````

In this case, it's easy to complete the class to avoid any TypeErrors:

for eg,
````py
class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"

    def punchline(self):
        return "Send in the constable!"
````


-------------------------------------------------------------------------------------
### Q032: Positional Argument(args) & Named Argument(kwargs);;

- `args`  : `RECEIVED TUPLE`
- `kargs` : `RECIEVED DICTIONARY`

#### NAMED ARGUMENT OR KEYWORD ARGUMENT (kwargs)

**Usage 1:**

The names args and kwargs are used by convention, they are not a part of the
language specification. Thus, these are equivalent:

for eg, They both are same...
````py
# Example 1
def func(*args, **kwargs):
	print(args)
	print(kwargs)

# Example 2
def func(*a, **b):
	print(a)
	print(b)
````

**Usage 2:**

You may not have more than one args or more than one kwargs parameters
(however they are not required)

````py
def func(*args1, *args2): #  example 1
	# File "<stdin>", line 1
	# def test(*args1, *args2):
	
	# SyntaxError: invalid syntax


def test(**kwargs1, **kwargs2):	# example 2
	# File "<stdin>", line 1
	# def test(**kwargs1, **kwargs2):
	
	# SyntaxError: invalid syntax
````

**Usage 3:** 

If any positional argument follow `*args`, they are keyword-only arguments
that can only be passed by name. A single star may be used instead of `*args`
to force values to be keyword arguments without providing a variadic
parameter list. Keyword-only parameter lists are only available in Pytohn3

````py
# Example 1
def func(a, b, *args, x, y):	
	print(a, b, args, x, y)
	
func(1, 2, 3, 4, 5, 6)
# Output: Error, Missing param x,y

def func(a,b, *args, x, y):
	print(a, b, var, b, y)
	
func(1,2,3,4,6,x=8,y=9) # Work fine
````

**Usage 4:** 

Keyword argument should be at last of the function defination.

````py
def func(**kwargs, *args): 
    pass
    
func()
# Output:
# SyntaxError: arguments cannot follow var-keyword argument
````

**Usage 5:**

Keyword arguments (also known as named arguments) are arguments that need to
be named specifically while calling the function. They don't require to be in
any order like positional arguments.

We can define keyword arguments by adding a * as the first argument to a
function. In the snippet below, we define two keyword arguments width and
length, for the area() function.

for eg,
````py
# Example 1 
def area(*, width, length):
  return width * length

if __name__ == "__main__":
    # Keyworded Argument accepted only;
    result = area(length=10, width=6)    # named argument i.e length=2, width=3
    print(f"The area of the rectangle is {result}")

# Example 2 : without keyword argument in above example will result error;
def area(*, width, length):
  return width * length

result = area(2, 3)     # missing named argument i.e 2,3

# OUTPUT:
# # Will throw an error, like this 
# Traceback (most recent call last):
#   File "script.py", line 4, in <module>
#     result = area(2, 3) # Will throw an error
# TypeError: area() takes 0 positional arguments but 2 were given
````

Usage 6:

We can use variable argument`(*args)` and keyword argument`(**kwargs)` 
together in a function.

for eg, 
````py
# kwargs is a variable keyword argument
def area(*args, shape="rectangle", **kwargs):  
    print(args)
    print(shape)
    print(kwargs)

area(8,9,10,height=6, width=8, breadth=4, shape='cuboid')

# Output : 
# (8, 9, 10)
# cuboid
# {'height': 6, 'width': 8, 'breadth': 4}
````

#### POSITIONAL ARGUMENT : VARIABLE ARGUMENT (args);;

Positional argument uses tuple for sending and receiving the value

when you are using `*args` for sending param value to a func() param then
argument gonna unpack while calling the method and the func() received
individual argument.

for eg,
```py
def func(x,y):
	print(x,y)
	
a = [1,2]
func(*a)		# x = 1, y = 2 unpack a into two variables;

a.append(3)
func(*a)		# error func() expects two agrument but 3 were given;
```

**kwargs using in function**

Work approach is same as in the args but kwargs received `key:value` pair
instead of `tuple as in args`;

for eg,
````py
def func(x,y):
	print(f"x: {x} // y:{y}")

x = {'a': 10, 'b': 20}
func(**x)
````

**Note that the length of the starred argument need to be equal to the 
number of the function's arguments.**

A common python idiom is to use the unpacking operator * with the zip 
function to reverse its effects


-------------------------------------------------------------------------------------
### Q031: Finding and Installing Packages;

For indirect calling for the pip module if the pip module is not defined as 
inside the environment variable;

**NOTE: for directly using pip, you need to defined it inside the environment
  variable like you have done while install python;**

- Search (Obsolete) : 
```sh
$ pip search <query>
```

- Install & Uninstall : 
```sh
$ pip install <query>
```

- Un-install Package : 
```sh
$ pip uniinstall <query>
```

- Install Specific Version : 
```sh
$ pip install [package_name]==x.x.x
```

- Minimum Version Of Package : 
```sh
$ pip install '[package_name]>=x.x.x'
``` 

- List Outdated Package : 
```sh
$ pip list --outdated
``` 

- Upgrade Installed Package : 
```sh
$ pip install --upgrade <package>
```

- Upgrade Pip Module : 
```sh
$ pip install -U pip
```

- Force Reinstall :
```sh
$ pip install --force-reinstall --no-deps -v package_name
```

    1) `--no-deps` : Ignore Dependency
    2) `-v` : Verbosity
    3) `--force-resintall` : Install in every scenario


-------------------------------------------------------------------------------------
### Q030: Deafult Dict in Python;;

A `defaultdict` is a dictionary with a default value for keys, so that keys
for which no value has been explicitly defined can be accessed without
errors. Defaultdict is especially useful when the values in the dictionary
are collections (lists, dicts, etc) in the sense that it does not need to be
initialized every time when a new key is used.

**NOTE: A defaultdict will never raise a KeyError. Any key that does not exist
  gets the default value returned.**

for eg,
````py
from collections import defaultdict

data = defaultdict(int)
nums = [1,2,3,4,4,3,3,1,2,3,4,5,6]
for num in nums:
    data[num] += 1

print(data)     # defaultdict(<class 'int'>, {1: 2, 2: 2, 3: 4, 4: 3, 5: 1, 6: 1})
````


-------------------------------------------------------------------------------------

### Q029 : GroupBy in Itertools;;

*(Refer Example: Basic-Py/P050_Iterator_GroupBy.py)*

Python’s Itertool is a module that provides various functions that work on
iterators to produce complex iterators. This module works as a fast,
memory-efficient tool that is used either by themselves or in combination
to form iterator algebra.

The time complexity of groupby() in Python (from itertools.groupby) depends on
whether the input is sorted or unsorted:

1) **Best Case (Sorted Input) → O(n)**

If the input is already sorted by the key function, groupby() runs in linear
time, iterating through the sequence once and grouping adjacent elements.

2) **Worst Case (Unsorted Input) → O(n log n)**

If the input is unsorted, you often need to sort the data before using groupby(), 
which takes `O(nxlog n)` (Timsort). 

After sorting, groupby() takes `O(n)`, making the total...
`O(nlogn) + O(n) = O(nlogn)`

For eg,
```py
from itertools import groupby

records = [
    ['5000', '1234567890'],
    ['5000', '1234567890'],
    ['6000', '1234567890'],
    ['6000', '1234567890'],
    ['8000', '1234567890'],
]

print("Example 1...")
for key, group in groupby(records):
    print(key,':', list(group))

# Example 1...
# ['5000', '1234567890'] : [['5000', '1234567890'], ['5000', '1234567890']]
# ['6000', '1234567890'] : [['6000', '1234567890'], ['6000', '1234567890']]
# ['8000', '1234567890'] : [['8000', '1234567890']]

print("Example 2...")
for key, group in groupby(records, lambda x: x[0]):
    print(key,':', list(group))

# Example 2...
# 5000 : [['5000', '1234567890'], ['5000', '1234567890']]
# 6000 : [['6000', '1234567890'], ['6000', '1234567890']]
# 8000 : [['8000', '1234567890']]

print("Example 3...")
for key, group in groupby(records, lambda x:x[1]):
    print(key,':', list(group))

# Example 3:
# 1234567890 -> [
#     ['5000', '1234567890'], 
#     ['5000', '1234567890'], 
#     ['6000', '1234567890'], 
#     ['6000', '1234567890'], 
#     ['8000', '1234567890']
# ]
```


-------------------------------------------------------------------------------------
### Q028: Builtins Error and Exception;;

Built in modules contains extra functionalities.For example to get square 
root of a number we need to include math module.

for eg,
````py
import math
math.sqrt(16) # 4.0
````

To know all the functions in a module we can assign the functions list to a
variable, and then print the variable.

````py
import math

dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh','asin', 
'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign','cos', 
'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 
'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 
'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 
'modf', 'pi', 'pow']

dir(__builtins__)
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
````


-------------------------------------------------------------------------------------
### Q027: Mutable and Immutable data types;;

#### Immutable:
- numbers 
- complex
- string
- bytes
- tuple
- frozenset

#### Mutable
- list
- set
- dict
- bytearray


-------------------------------------------------------------------------------------
### Q026: Explicit string type at definition of literals;;

With one letter labels just in front of the quotes you can tell what type of
string you want to define.

- `b'foo bar'` : bytes in Python 3, str in Python 2.
- `u'foo bar'` : str in Python 3, unicode in Python 2.
- `"foo bar"`  : regular string all string in python 3 are unicode.
- `r'foo bar'` : raw string literal, where backslashes \ are treated as
  literal characters and not as escape characters. 

for eg,
````py
normal = 'foo\nbar'         # foo 
                            # bar                            
escaped = 'foo\\nbar'       # foo\nbar
raw = r'foo\nbar'           # foo\nbar

````

-------------------------------------------------------------------------------------
### Q025: Python first class objects;;

It means there are no restrictions on the object's use. It's the same as any
other object.

A first class object is an entity that can be dynamically created, destroyed,
passed to a function, returned as a value, and have all the rights as other
variables in the programming language have.

#### Depending on the language, this can imply

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
### Q024: Python main() function;;

In the world of programming languages, the `main` is considered as an entry
point of execution for a program. 

But in python, it is known that the interpreter serially interprets the file
line-by-line. This means that python does not provide main() function
explicitly. But this doesn't mean that we cannot simulate the execution of
main. 

This can be done by defining user-defined main() function and by using the
`__name__` property of python file. This `__name__` variable is a special
built-in variable that points to the name of the current module. 

This can be done as shown below:

for eg,
````py
def main():
   print("Hi Interviewbit!")

if __name__=="__main__":
   main()
````


-------------------------------------------------------------------------------------
### Q023: Shallow Copy vs Deep Copy;;

`Shallow copy` does the task of creating new objects storing references of
original elements. This does not undergo recursion to create copies of nested
objects. It just copies the reference details of nested objects.

`Deep copy` creates an independent and new copy of an object and even copies 
all the nested objects of the original element recursively.


-------------------------------------------------------------------------------------
### Q022: Global Interpreter Lock;;

- `GIL` stands for `Global Interpreter Lock`. This is a mutex used for limiting
access to python objects and aids in effective thread synchronization by
avoiding deadlocks. 

- GIL helps in achieving multitasking (and not parallel computing).

Thread Work Synchronization, Suppose there are 3 threads, so their execution
should be like this, 

`First Thread`: First Thread acquires the GIL first and starts the I/O
execution. When the I/O operations are done, thread 1 releases the acquired
GIL Lock.

`Second Thread`: After Thread 1 release GIL Lock, which is then taken up by
the second thread. The process repeats and the GIL are used by different
threads alternatively until the threads have completed their execution. 

**The threads not having the GIL lock goes into the waiting state and resumes
  execution only when it acquires the lock**


-------------------------------------------------------------------------------------
### Q021: Lambda function in Python;;

`LAMBDA` functions are generally inline, anonymous functions represented by a
single expression. They are used for creating function objects during
runtime. They can accept any number of parameters. They are usually used
where functions are required only for a short period. They can be used as:

They are defined by using lambda instead of def, and return the result of the
one line of code without requiring the return statement

for eg,
```py
square = lambda x: x * x

print(square(3))
print(square(4))

# OUTPUT : 
# 9
# 16
```

The code above defines a Lambda function that takes in an input x and returns
its square. The LAMBDA is then assigned to variable square that can be called
in a similar way to a normal function.

#### USAGE 2: MAP FUNCTION
Lambda functions are generally useful when using functions like map().  The map() 
function takes in a list and returns its modified version based on some
criteria. This criterion is passed to it as a function.

for eg,
```py
radius = [1,2,3,4,5]
areas = map(lambda x: 3.14*x*x, radius)
print(f"areas : {list(areas)}")
```

#### USAGE 3: FILTER FUNCTION
Filter function is used to  of the sequence 

for eg,
```py
numbers = (1,2,3,4,5,6,7,8,9,10)
data = filter(lambda x: x % 2 == 0, numbers)

print(list(data))

# Output:
[2, 4, 6, 8, 10]
```


-------------------------------------------------------------------------------------
### Q020: Module vs Packages in Python;;

- The module is a single python file. A module can import other modules
  (other python files) as objects. 
- Whereas, a package is the folder/directory where different sub-packages and
  the modules reside.

#### Module

A python module is created by saving a file with the extension of `.py`. This
file will have classes and functions that are reusable in the code as well as
across modules.

#### Package

A python package is created by following the below steps

- Create a directory and give a valid name that represents its operation. 
- Place modules of one kind in this directory. 
- Create `__init__.py` file in this directory. 
- This lets python know the directory we created is a package. 
- The contents of this package can be imported across different modules in
  other packages to reuse the functionality.


-------------------------------------------------------------------------------------
### Q019: Inheritance in Python;;

- Inheritance gives the power to a class to access all attributes and methods
  of another class. 
- It aids in code reusability and helps the developer to maintain applications
  without redundant code. 
- The class inheriting from another class is a `child class` or also called a
  `derived class`. 
- The class from which a child class derives the members are called `parent class` 
  or `superclass`.

Python supports different kinds of inheritance, they are:

#### Single Inheritance: 
Child class derives members of one parent class.

for eg,
````py
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
````

#### Multi-level Inheritance:

The members of the parent class(A), are inherited by child class (B) which is
again inherited by another child class (C). 

Here, A is the grandfather class of class C.

for eg,
```py
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
``` 

#### Multiple Inheritance: 

This is achieved when one child class derives members from more than one
parent class. All features of parent classes are inherited in the child
class.

for eg,
````py
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
````

#### Hierarchical Inheritance: 

When a parent class is derived by more than one child class.

for eg,
````py
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
````


-------------------------------------------------------------------------------------
### Q018: Access Specifiers used in python;;

- Python does not make use of access specifiers specifically like private,
public, protected, etc. However, it does not derive this from any variables.

- It has the concept of imitating the behaviour of variables by making use of a
  - Single underscore (protected) 
  - Double underscore (private) as prefixed to the variable names
  - Variables without prefixed underscores are public for python.

For eg,
```py
# Demonstrate access specifiers
class InterviewbitEmployee:
    # private members
    __branch = None
   
    # protected members
    _emp_name = None
    
    # constructor
    def __init__(self, emp_name, branch): 
         self._emp_name = emp_name
         self.__branch = branch
    
    #public member
    def display():
        print(self._emp_name + " " + self.__branch)


ie = InterviewbitEmployee("Neeraj", "DELHI")

print(ie._emp_name) # Protected Variable
# OUTPUT: Neeraj

print(ie.__branch) # Private Variable
# OUTPUT: 
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 26, in <module>
# AttributeError: 'InterviewbitEmployee' object has no attribute '__branch
```


-------------------------------------------------------------------------------------
### Q017: Access Parent Class using Child class;;

Following are the ways using which you can access parent class members within
a child class:

**By using Parent class name:**

You can use the name of the parent class to access the attributes as shown in
the example below:

````py
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
````

**By using super():** 

The parent class members can be accessed in child class using the super
keyword.

```py
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
```

-------------------------------------------------------------------------------------
### Q016: Python Pickling vs UnPickling;;

Python library offers a feature - serialization out of the box. 

Serializing an object refers to transforming it into a format that can be
stored, so as to be able to deserialize it, later on, to obtain the original
object. 

Here, the pickle module comes into play.

#### Pickling:

- Pickling is the process of converting a Python object into a byte stream.
- The pickle module is used for pickling.
- The `pickle.dump()` method is used to `serialize an object` into a file-like
  object.

for eg,
````py
import pickle

data = {'name': 'John', 'age': 30, 'city': 'New York'}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
````

#### Unpickling:

- Unpickling is the process of converting a byte stream back into a Python object.
- The pickle module is used for unpickling.
- The `pickle.load()` method is used to `deserialize an object` from a file-like
  object.

for eg,
````py
import pickle

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
````

#### Usages Pickling and Unpickling:

**Object Persistence:**
- Pickling: It allows you to save Python objects (such as dictionaries, lists,
  or custom objects) to a file or another storage medium in a serialized
  format.
- Unpickling: It enables you to later read and reconstruct the original Python
  objects from the serialized data.

**Data Storage and Retrieval:**
- Pickling: Useful for storing data persistently in a compact, serialized
  format.
- Unpickling: Allows retrieving the original data from the stored serialized
  format.

**Data Transmission:**
- Pickling: Facilitates the transmission of Python objects between different
  processes or systems.
- Unpickling: Enables the reconstruction of Python objects on the receiving
  end.

**Caching:**
- Pickling: Objects can be pickled and stored in a cache for faster retrieval
  in future computations.
- Unpickling: Retrieves the cached objects when needed.

**Cross-Version Compatibility:**
- Pickling: Can be used to store data in a version-independent format,
  ensuring compatibility between different versions of the same application
  or library.
- Unpickling: Allows reading and using the data across different versions.

**Remote Procedure Calls (RPC) and Distributed Systems:**
- Pickling: Objects can be pickled and sent over a network to remote systems.
- Unpickling: Enables the remote system to reconstruct the original objects.

**Memoization:**
- Pickling: Can be used in memoization techniques to cache and reuse the
  results of expensive function calls.

**Testing:**
- Pickling: Allows creating and storing test data in a serialized format for
  later use in unit tests or integration tests.
- Unpickling: Retrieves the test data for verification during testing.


-------------------------------------------------------------------------------------
### Q015: Class Composition Vs Class Inheritance;;

*(Refer: https://realpython.com/inheritance-composition-python)*

#### Inheritance:

-  Inheritance models what is called an `is a` relationship. This means that
   when you have a Derived class that inherits from a Base class, you created
   a relationship where Derived is a specialized version of Base.

-  Inheritance is represented using the Unified Modeling Language or UML in
   the following way:

-  `Base Class <--- Extends --- Derived Class`

#### Liskov Substitution Principle: 

Suppose, you have base class of type Animal and there is a class Horse derived
from it. So you can say that Horse is a type of Animal. 

Horse inherits interface and implementation of class Animal and Horse class
object can be used to replace the Animal Class object from the code.

This is known as **Liskov Substitution Principle**. 

The Principle states that "in a computer program, If S is a subtype of T, then
objects of type T may be replaced with object of type S without altering any
of the desired properties of the program."

#### Class Composition:

-> Composition model what is called an `has a` relationship. It enables
   creating complex types by combining objects of other types. This means
   that a class Composite can contain an object of another class Component.
   This relationship means that a Composite has a Component.

-> Class composition directly inject the class depency into the composite
   class. so because of this style class composition have loose coupling.

-> UML representation of the following, 

-> Composite Class (1) ---> Component Class

Here,

-  A number represent number of the component class. In our case it is 1,
   which means the composite class have components.
-  The * Symbols indicates that the composite class can contains a variable
   number of component services.
-  A range 1..4 indicates that the composite class can contain a range of
   component instance. The range is indicated with the minimum and maximum
   number of numbers of instances. for eg, if there is minimum instance is of
   1 and maximum doesn't have any limit than it can be show with *, 1..*


-------------------------------------------------------------------------------------
### Q014: Duck Typing in Python;;

`Duck Typing` is a type system used in dynamic languages. 

For example, Python, Perl, Ruby, PHP, Javascript, etc. where the `type` or
`class of an object` is less important than the method it defines. 

Using Duck Typing, we do not check types at all. Instead, we check for the
presence of a given method or attribute.

The name Duck Typing comes from the phrase:

**If it looks like a duck and quacks like a duck, it’s a duck**

for eg,
```py
class Bird:
    def fly(self):
        print("fly with wings")
  
class Airplane:
    def fly(self):
        print("fly with fuel")
  
class Fish:
    def swim(self):
        print("fish swim in sea")

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    try:
        obj.fly()
    except Exception as e:
        print(f"{obj.__class__.__name__} can't fly")

# RESULT:
# fly with wings
# fly with fuel
# Fish can't fly
```


-------------------------------------------------------------------------------------
### Q013: @classmethod vs @stacticmethod;;

#### @classmethod 

The `@classmethod` decorator is a built-in function decorator that is an
expression that gets evaluated after your function is defined. 

The result of that evaluation shadows your function definition. A class 
method receives the class as an implicit first argument, just like an 
instance method receives the instance.

Syntax Python Class Method:

````py
class C(object):

    @classmethod
    def fun(cls, arg1, arg2, ...):
       ...
       
````

`fun`: function that needs to be converted into a class method returns: a
class method for function.

- A class method is a method that is bound to the class and not the object of
  the class.
- They have the access to the state of the class as it takes a class parameter
  that points to the class and not the object instance.
- It can modify a class state that would apply across all the instances of the
  class. 
- For example, it can modify a class variable that will be applicable to all
  the instances.


#### @staticmethod 

A static method does not receive an implicit first argument. A static method
is also a method that is bound to the class and not the object of the class.

This method can’t access or modify the class state. It is present in a class
because it makes sense for the method to be present in class.

Syntax Python Static Method: 

```py
class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...

# returns: a static method for function fun.
```

#### When to use the class or static method ?

- We generally use the `@classmethod` to `create factory methods`. The Factory
  methods return class objects (similar to a construct or) for different use
  cases.
- We generally use `@staticmethods` to `create utility functions`.

for eg,
````py
# Python program to demonstrate use of 
# class method and static method.
from datetime import date
from time import time
 
class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
 
    @classmethod
    def is_adult(cls, user_id):
        # factory method to valid user age > 18;;
        # suppose fetching dob from database;;
        user = cls.objects.filter(user_id).get()
        if now - user.dob < 18:
            return Fale
        return True
     
    @staticmethod
    def generate_username(uid, prefix='UID'):
        # utility method for generating username;;
        return f"C{uid}{int(time())}"


person1 = Person('mayank', '1997-01-05')

print(f"{person1.name} is adult"person1.is_ad)
print(f"{person1.name}'s' Username: {person1.generate_username(uid=1)}")

# Output:
# mayank is adult : True
# mayank's' Username: C11705143685
````


-------------------------------------------------------------------------------------
### Q012: Magic Method __str__() vs __repr__();;

In Python, the built-in str() and repr() functions both produce a textual
representation of an object.

for eg,
````py
import datetime

today = datetime.datetime.now()

print(str(today))
print(repr(today))

# Output:
# 2021-10-14 10:15:31.405463    # output: __str__
# datetime.datetime(2021, 10, 14, 10, 15, 31, 405463)     # output: __repr__
````

#### Difference between str() and repr() is:

- The `str()` function returns a user-friendly description of an object.
- The `repr()` method returns a developer-friendly string representation of an
  object.

#### Working str() and repr() under the hood:

- When you call `str()` on an object, it calls the special method `__str__` of
  the object.
- when you call `repr()` on an object, it calls the special method `__repr__`
  of the object.
- Also, when you call `print()` on an object, it calls `__str__` method of the
  object. If `__str__` is not implemented, the `__repr__` is called as a fallback.

for eg,
````py
# Case 1: Without str() and repr();
class Fruit:
    def __init__(self, name):
        self.name = name

banana = Fruit("Banana")
print(banana)

# OUTPUT : <__main__.Fruit object at 0x7f0ece0e8d00>

# Case 2: With str() and repr();
class Fruit:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'I am a {self.name}'
    
    def __repr__(self):
        return f'Fruit("{self.name}")'

banana = Fruit("Banana")
print(banana)

# OUTPUT : I am a Banana
````


-------------------------------------------------------------------------------------
### Q011: Set Variable LowerBound and UpperBound;;

This methods helps to set the upper and lower bound of a bound for fallback
prevention.

#### FIRST APPROACH

In this, we use sys module to find the maxsize limit for a system.

for eg,
```py
from sys import maxsize

minValue = -maxsize
maxValue = maxsize

print(minValue, maxValue)

# OUTPUT:
# -9223372036854775807 9223372036854775807
```

#### SECOND APPROACH 

It acts as an unbounded upper value for comparison. This is useful for finding
lowest values for something. 

for eg, Finding the "cheapest" path in a list of options:
````py
lowest_path_cost = float('inf')

# pretend that these were calculated using some worthwhile algorithm
path_costs = [1, 100, 2000000000000, 50]

for path in path_costs:
    if path < lowest_path_cost:
     lowest_path_cost = path

print(lowest_path_cost) # 1
````


-------------------------------------------------------------------------------------
### Q010: Create a Iterator Class using Generator;;

**NOTE : Generator is a type of Iterator in itself**

- An iterator is an object representing a stream of data and can be iterated
  one element at a time.
- It must implement two methods: `__iter__()` and `__next__()`.
- The `__iter__()` method returns the iterator object itself, and the
  `__next__()` method returns the next element in the sequence.
- When there are no more elements to return, the __next__() method should
  raise the `StopIteration` exception.

for eg,
```py
class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a+self.b

# When we pass an iterable to iter(), 
# It gives us an iterator

f = iter(Fib())
for i in range(3):
    print("i: ", next(f))

# Output 
# i: 0
# i: 1
# i: 1
```

**NOTE: To make the class itself an iterator, it does require a `__next__`.**

```py
class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
       
    # __iter__ will generate iterable
    def __iter__(self):
        return self
     
    # __next__ will generate sequence;;        
    def __next__(self):
        return  self.a   # Observe, return used not yield
        self.a, self.b = self.b, self.a + self.b


# since iter just returns the instance itself
# we don't need to call it.

f = Fib()
for i in range(3):
    print("i: ", next(f))

# Output
# i: 0
# i: 1
# i: 1
```

From above example observed one thing in `__next__()` function we don't use
`yield` keyword but instead we directly return the value because `yield` will
return generator object.

````py
# Check the same above code with yield implementation instead return;;

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
        
    def __next__(self):
        yield self.a          # yield makes .__next__() return a generator!
        self.a, self.b = self.b, self.a+self.b

f = Fib()
for i in range(3):
    print(next(f))
    
# So every time you called next(f) you got the generator 
# object that __next__ returns

# <generator object __next__ at 0x000000000A3E4F68>
# <generator object __next__ at 0x000000000A3E4F68>
# <generator object __next__ at 0x000000000A3E4F68>
````

-------------------------------------------------------------------------------------
### Q009: Iterators Vs Iterables Vs Generators in python;;

#### Iterators:
- An iterator is an object representing a stream of data and can be iterated
  one element at a time.
- It must implement two methods: `__iter__()` and `__next__()`.
- The `__iter__()` method returns the iterator object itself, and the
  `__next__()` method returns the next element in the sequence.
- When there are no more elements to return, the `__next__()` method should
  raise the `StopIteration` exception.

for eg,
```py
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_iterator = MyIterator([1, 2, 3, 4, 5])

for item in my_iterator:
    print(item)
```

#### Iterables:
- An iterable is any object in Python capable of returning its elements one at
  a time.
- Examples of iterables include lists, tuples, strings, dictionaries, sets,
  and more.
- You can iterate over the elements of an iterable using a loop or by using
  functions like iter() and next().

for eg,
```py
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
```

#### Generator:

- A generator is a special type of iterator defined using a function with the
  `yield` keyword.
- It allows you to iterate over a potentially large sequence of data without
  storing the entire sequence in memory.
- The state of the generator is maintained between successive calls to the
  `yield` statement.

for eg,
```py
def my_generator(data):
    for item in data:
        yield item

my_gen = my_generator([1, 2, 3, 4, 5])

for item in my_gen:
    print(item)
```

#### Generator Iterators:

- An object created by a generator function.
- Each yield temporarily suspends processing, remembering the location 
execution state (including local variables and pending try-statements).
- When the generator iterator resumes, it picks-up where it left-off
(in contrast to functions which start fresh on every invocation).

for eg,
```
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

# We use next function as Generator to fetch the next sequence each time;;
gen = FirstHundredGenerator()
print(next(gen))  # 0
print(next(gen))  # 1
```

#### Iterators Vs Generators:

**Iterators**
- Iterators use classes.             
- Iterators use the __next__ and __iter__ methods.          
- Iterators maintain state within instance attributes.
- No methods are paused. State is maintained within Instance.
- Can be created using iter()       

**Generator**
- Generators use functions.
- Generators use the `yield` keyword and next methods.                    
- Generators store state in local function variables.
- Functions are paused and their state is maintained within Python.
- Can be created using function().


-------------------------------------------------------------------------------------
### Q008: What are Iterators in python;;

An iterator is an object representing a stream of data and can be iterated 
one element at a time.

It must implement two methods: `__iter__()` and `__next__()`.

The `__iter__()` method returns the iterator object.

The `__next__()` method returns the next element in the sequence.

```py
class FirstHundredGenerator(object):
    def __init__(self):
        self.number = 0
    
    # Iter(): return the iterator object;;
    def __iter__(self):
        return self
        
    # Next() will return the sequence of object;;
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()     ## used to stop iteration;;

# Usage 1: It is a generator as well;;
gen = FirstHundredGenerator()
print(next(gen))  # 0
print(next(gen))  # 1

# Usage 2: It is an iterator as well;;
for i in FirstHundredGenerator():
    print(f"i: {i}")

# Output: 
# i : 0
# i : 1 
# ... so on
```


**NOTE**: Below Code Snippet can also be used as Iterator.

- We are only using the `__next__()` for making the sequence.
- Below code won't be able to act act as an iterator because we are not 
using the `__iter__()`

````py
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

# We use next function as Generator to fetch the next sequence each time;;
gen = FirstHundredGenerator()
print(next(gen))  # 0
print(next(gen))  # 1

# If you tried the for loop here then it will throw you an error,
# saying it's not an iterator;;
for i in FirstHundredGenerator():
    print(i)    # Error: FirstHundredGenerator() not itertable.
    
````
Notice how the object, with its property, remembers what the value of
`self.number` is at all points in time.

This object is called in Python Generator because every time the next number
is available not because it’s in a sequence, but because it is generated from
its current state (in this case, by adding 1 to `self.number`).

All objects that have this `__next__` method are called iterators. All
generators are iterators, but not the other way round.

For example, you could have an iterator on which you can call `next()`, but
that doesn’t generate its values. Instead, it could take them from a list or
from a database.

*Important: iterators are objects which have a `__next__` method.*

Here’s an example of an iterator which is not a generator:

for eg,
````py
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

# As you can see it’s returning numbers that are not being generated; 
# Instead they’re being returned from a list.

# If we run this code though, we will get an error:
sum(FirstHundredGenerator())  # comment this line out to run the rest of the file.

or, 
for i in FirstHundredGenerator():
    print(i)
````

And that’s because in Python, an `iterator` and an `iterable` are different
things. You can iterate over an `iterable`. The iterator is used to get the
next value (either from a sequence or generated values).

You can iterate over iterables, not over iterators.
  

-------------------------------------------------------------------------------------
### Q007: What are Generator in Python;;

A generator in Python is a function that remembers the state it’s in, in
between executions.

Let’s explain with an example. Imagine you wanted to build a list of 100
numbers, like this one:

for eg,
````py
def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
      nums.append(num)
      i += 1
    return nums
````

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
````py
def hundred_numbers():
    num = 0
    while num < 100:
      yield num
      num += 1
````

The `yield` keyword is very much like a `return`, in that it gives the value
back to the caller and returns execution control to them (show this with
example run). However, the next time you run the function, execution continues
from the very next line inside the function, instead of from the top.

We could re-write the function as a list comprehension:

for eg,
```py
hunderd_numbers = [n for n in range(100)]
```

Or indeed as a generator comprehension. This is essentially the same thing,
including the `yield` statement.

````py
def hundred_numbers():
    num = 0
    while num < 100:
      yield num
      num += 1

print(next(hundred_numbers())) # 0
print(next(hundred_numbers())) # 1
print(list(hundred_numbers())) # [0,1,2,3,4,5,...,99]
````
 
Notice that when we do the code snippet above, `next()` runs the function once
up until the `yield` (which would give you the first value). 

The following `next()` runs it again, which gives you the second value. Then,
turning it into a list continues and builds a list from the remaining values
(that’s only 98 values left).


-------------------------------------------------------------------------------------
### Q006: Type Hinting in Python;;

It is used to validate the data type of the incoming argument of a function or
returning variable  from the function; 

for eg,
````py
from typing import List, Dict, Tuple, Type

def sample(x: int) -> List[Dict[key, bool]]:
    res = []
    for i in range(x):
        if(i%2 == 0)
            res.append({i:True})
        else:
            res.append({i:False})

    return res            ## Output: List[Dict[int, bool]]
   
print("Answer: ", sample(4))
````

### Generic Types

The fundamental building blocks defined above allow to construct new types in
a generic manner. 

For example, Tuple can take a concrete type float and make a concrete type
`Vector = Tuple[float, ...]`

or, it can take another type UserID and make another concrete type 
`Registry = Tuple[UserID, ...]` 

Such semantics is known as generic type constructor, it is similar to
semantics of functions, but a function takes a value and returns a value,
while generic type constructor takes a type and “returns” a type.

It is common when a particular class or a function behaves in such a type
generic manner. Consider two examples:

Container classes, such as list or dict, typically contain only values of a
particular type. Therefore, a user might want to type annotate them as such:

````py
users = [] # type: List[UserID] 
users.append(UserID(42)) # OK
users.append('Some guy') # Should be rejected by the type checker

examples = {} # type: Dict[str, Any]
examples['first example'] = object() # OK
examples[2] = None  # rejected by the type checker
````

The following function can take two arguments of type int and return an int,
or take two arguments of type float and return a float, etc.

````py
def add(x, y):
  return x + y

add(1, 2) == 3
add('1', '2') == '12'
add(2.7, 3.5) == 6.2
````

To allow type annotations in situations from the first example, built-in
containers and container abstract base classes are extended with type
parameters, so that they behave as generic type constructors. 

Classes, that behave as generic type constructors are called generic types.

Example:

````py
from typing import Iterable

class Task:
    ...

def work(todo_list: Iterable[Task]) -> None:
    ...
````

Here Iterable is a generic type that takes a concrete type Task and returns a
concrete type `Iterable[Task]`.

Functions that behave in the type generic manner (as in second example) are
called generic functions. Type annotations of generic functions are allowed by
type variables. Their semantics with respect to generic types is somewhat
similar to semantics of parameters in functions. But one does not assign
concrete types to type variables, it is the task of a static type checker to
find their possible values and warn the user if it cannot find. Example:

````py
def take_first(seq: Sequence[T]) -> T: # a generic function
    return seq[0]
    
accumulator = 0                        # type: int
accumulator += take_first([1, 2, 3])   # Safe, T deduced to be int
accumulator += take_first((2.7, 3.5))  # Unsafe
````

Type variables are used extensively in type annotations, also internal
machinery of the type inference in type checkers is typically build on type
variables.


-------------------------------------------------------------------------------------
### Q005: Copy in Python;

In Python, the assignment statement (= operator) does not copy objects.
Instead, it creates a binding between the existing object and the target
variable name. To create copies of an object in Python, we need to use the
copy module. 

There are two ways of creating copies for the given object 

Shallow Copy is a bit-wise copy of an object. The copied object created has an
exact copy of the values in the original object. If either of the values is a
reference to other objects, just the reference addresses for the same are
copied. 

Deep Copy copies all values recursively from source to target object,
i.e. it even duplicates the objects referenced by the source object.

```py
from copy import copy, deepcopy
list_1 = [1, 2, [3, 5], 4]

# Shallow Copy : ShallowCopy only copy the parent reference 
list_2 = copy(list_1)
list_2[3] = 7
list_2[2].append(6)
print(list_2)  # output => [1, 2, [3, 5, 6], 7]
print(list_1)  # output => [1, 2, [3, 5, 6], 4], i.e. child [3,5,6] are same both list list_2 & list_1

## deep copy
list_3 = deepcopy(list_1)
list_3[3] = 7
list_3[2].append(6)
print(list_3)  # output => [1, 2, [3, 5, 6, 7], 8]
print(list_1)  # output => [1, 2, [3, 5, 6], 4] i.e, here parent & child both independent;;
```

-------------------------------------------------------------------------------------
### Q004: Python arrays;

- `Arrays` in python can only contain elements of same data types i.e., data type
of array should be homogeneous. 
- It is a thin wrapper around C language arrays and consumes far less memory than 
lists. Lists in python can contain elements of different data types i.e., data type 
of lists can be heterogeneous. It has the disadvantage of consuming large memory.

> Syntax: arr = array(Parameter, [Initialize Values])

for eg,
```py
import array

a = array.array('i', [1, 2, 3])
for i in a:
    print(i, end=' ')    #OUTPUT: 1 2 3
a = array.array('i', [1, 2, 'string'])   

#OUTPUT: TypeError: an integer is required (got type str)

a = [1, 2, 'string']

for i in a:
   print(i, end=' ')    #OUTPUT: 1 2 string
```

#### Array Parameters Details:
- c : character of size 1 byte
- u : unicode character of size 2 bytes
- w : unicode character of size 4 bytes

- b : signed integer of 1 byte
- B : unsigned integer of 1 byte
- h : signed integer of 2 bytes
- H : unsigned integer of 2 bytes
- i : signed integer of 2 bytes
- I : unsigned integer of 2 bytes
- l : signed integer of 4 bytes
- L : unsigned integer of 4 bytes

- f : floating point of 4 bytes
- d : floating point of 8 bytes


for eg,
````py
# // Array CRUD
from array import *

arr = array(i, [1,2,3])

# // append values to array
arr.append(4)
print(arr)  # [1,2,3,4]

# // print array
for i in arr:
    print(i)

# // insert values at array
arr.insert(4,99)

# // extends from list
c = [11,12,13]
arr.extends(c)
print(arr)

# // more helpers...
arr.fromlist(opts=[11,22,33])
arr.count(3)
arr.tostring()              # convert to string
arr.tolist()                # convert to list
````


-------------------------------------------------------------------------------------
### Q003: LAMBDA;;

Lambda is an anonymous function in Python, that can accept any number of
arguments, but can only have a single expression. It is generally used in
situations requiring an anonymous function for a short time period. 

Lambda functions can be used in either of the two ways:

```py
# Useage 1 : Assigning lambda functions to a variable;;
mul = lambda a, b : a * b

print(mul(2, 5))    # output => 10
```

````py
# Usage 2 : Wrapping lambda functions inside another function;;
def myWrapper(n):
    return lambda a : a * n

mulFive = myWrapper(5)
print(mulFive(2))    # output => 10
````

-------------------------------------------------------------------------------------
### Q002: Comprehensions;

Python comprehensions, like decorators, are syntactic sugar constructs that
help build altered and filtered lists, dictionaries, or sets from a given
list, dictionary, or set. Using comprehensions saves a lot of time and code
that might be considerably more verbose (containing more lines of code). Let's
check out some examples, where comprehensions can be truly beneficial:

Performing mathematical operations on the entire list

````py
my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list]    # list comprehension
# output => [4 , 9 , 25 , 49 , 121]

squared_dict = {x:x**2 for x in my_list}    # dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}
````

Performing conditional filtering operations on the entire list

````py
my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list if x % 2 != 0]    # list comprehension
# output => [9 , 25 , 49 , 121]

squared_dict = {x:x**2 for x in my_list if x % 2 != 0}    # dict comprehension
# output => {11: 121, 3: 9 , 5: 25 , 7: 49}
````

Combining multiple lists into one Comprehensions allow for multiple iterators
and hence, can be used to combine multiple lists into one. 

````py
a, b  = [1, 2, 3], [7, 8, 9]

[(x + y) for (x,y) in zip(a,b)]  # parallel iterators
# output => [8, 10, 12]

[(x,y) for x in a for y in b]    # nested iterators
# output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)] 
````

Flattening a multi-dimensional list A similar approach of nested iterators (as
above) can be applied to flatten a multi-dimensional list or work upon its
inner elements. 

or, running multiple loop in a single comprehension

````py
my_list = [[10,20,30],[40,50,60],[70,80,90]]

flattened = [x for temp in my_list for x in temp]
# output => [10, 20, 30, 40, 50, 60, 70, 80, 90]
````

**NOTE: List comprehensions have the same effect as the map method in other
  languages. They follow the mathematical set builder notation rather than
  map and filter functions in Python.**


-------------------------------------------------------------------------------------
### Q001: Decorators in python;; 

Decorators in Python are essentially functions that add functionality to an
existing function in Python without changing the structure of the function
itself. They are represented the @decorator_name in Python and are called in a
bottom-up fashion. For example:

for eg,
```py
# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper(*args, **kwargs):
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper

# decorator function to split words
def splitter_decorator(function):
   def wrapper(*args, **kwargs):
       func = function()
       string_split = func.split()
       return string_split
   return wrapper

@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'

hello()   # output => [ 'hello' , 'world' ]
```

The beauty of the decorators lies in the fact that besides adding 
functionality to the output of the method, they can even accept arguments for
functions and can further modify those arguments before passing it to the
function itself. 

The inner nested function, i.e. 'wrapper' function, plays a significant role
here. It is implemented to enforce encapsulation and thus, keep itself hidden
from the global scope.

```py
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
```

-------------------------------------------------------------------------------------