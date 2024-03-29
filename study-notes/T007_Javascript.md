````
-------------------------------------------------------------------------------------
-  Title : Javascript Notes
-  Author: @neeraj-singh-jr
-  Status : Ongoing...
-  Created : 12/02/2023
-  Updated : 02/08/2024
-  Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-  Q006 : Array - Javascript
-  Q005 : Object - Javascript
-  Q004 : Undefined and null - Javscript;;
-  Q003 : Number - Javascript;;
-  Q002 : String - Javascript;;
-  Q001 : Variable - Javascript;;
-------------------------------------------------------------------------------------
````

#### Javascript NOTES : BEGINNING 

-------------------------------------------------------------------------------------
### Q006 : Array - Javascript
   
#### Array Basic :-

-  An array is used to store multiple values together.
-  An array is built by a pair of square brackets, with values placed inside
   it separated by commas.
-  for eg,

````
const fruits = ["Apple", "Orange", "Banana"];
console.log(fruits); // ["Apple", "Orange", "Banana"]
````

#### Homogenenous Array :-

-  Array are of the same data type, i.e., string, the array is known as a
   homogeneous array.
-  for eg,
````
const fruits = ["Apple", "Orange", "Banana"];
console.log(fruits); 
// ["Apple", "Orange", "Banana"]
````

#### Heterogeneous Array :-

-  The elements of the array measurements are of different data types. Such an
   array is known as a heterogeneous array.
-  for eg,
````
const measurements = [12, "34cm", 567.89];
console.log(measurements);    
// [12, "34cm", 567.89]
````

#### Reading an Array :-

-  Each element of an array has a number associated with it starting from 0
   and is known as the index of that element.
-  for eg,
````
const names = ["Oliver", "Adam", "Eve"];
console.log(names[0]);  // Oliver

//--- Addng item to array :-

names[3] = "May"
console.log(names[3]);  // May

//--- Adding item to faraway index :-

names[7] = "Neeraj"
console.log(names)   // ["Oliver", "Adam", "Eve", "May", undefined, undefined, undefined, "Neeraj"]

//--- Updating Array Element :-

names[0] = "Jency"
console.log(name[0]) // Jency
````

#### Array Length :-

-  We can use .length to get the number of elements in an array, also known as
   the length of the array.
-  for eg,
````
const fruits = ["Apple", "Banana"];
console.log(fruits.length);   // ~2
````


-------------------------------------------------------------------------------------
### Q005 : Object - Javascript

#### Javascript Object :-

-  Object are used to store complex datatype together in a single entity. For
   an instance, String and Number can hold string and number individually but
   there may be an instance when you need to bundle both together in a single
   entity, then object instance is used.
-  for eg,
````
const car = {
  model: 2011,
  fuelType: "diesel",
  fullName : "Hyundai Verna"
};

console.log(car.model);    // 2011
console.log(car['fullName']);    // Hyundai Verma
````

#### Access Javascript object :-

- There are two ways in which we can access javascript object.

````
//--- CASE 1 : Accessing using Bracket Notation;;

for eg,
const car = {
  model: 2011,
  fuelType: "diesel",
  fullName : "Hyundai Verna"
};

console.log(car['model']);    // 2011
console.log(car['fullName']);    // Hyundai Verma

//--- CASE 2 : Accessing using Dot Notation;;

for eg,
const car = {
  model: 2011,
  fuelType: "diesel",
  fullName : "Hyundai Verna"
};

console.log(car.model);    // 2011
console.log(car.fullName);    // Hyundai Verma
````

#### Different Object Usages :-

-  There are specific conventions for defining key and value syntax of an
   object.

-  for eg,
````
const profile = {
   first name : "Neeraj",  // Incorrect: Unexpected Variable;
   middle_name : "Singh",     // Correct
   last-name : "Junior"    // Incorrect: Unexpected Token '-';
}

console.log(profile)

// Countermeasure of above Syntax Error 

-  for eg,
const profile = {
   "first name" : "Neeraj",  
   "middle_name" : "Singh",  
   "last-name" : "Junior"  
}

NOTE: Object keys which are stored in double quotes can't be accessed using
the dot notation. It can only be accessed using the bracket notation.

console.log(profile."first name")   // Error: Not Accessible
consolg.log(profile["first name"])  // Success

-  for eg, 

const subjectWithCode = {
   101 : "Physics",
   102 : "English",
   103 : "Chemistry",
   104 : "Computer with cpp"
}

// Can't be access using Dot Notation;
console.log(subjectWithCode.101)

// Can be accessed using Bracket Notation;
console.log(subjectWithCode[101])
````

#### Add Property to Existing Object :-

//--- Add using Dot Notation :-
for eg,

````
const person = {
   name : "Adam Jensen",
   age : 26,
   isAdmin : true
};

person.profession = "Software Engineer"
console.log(person)  

# OUTPUT:-
{
  name: 'Adam Jensen',
  age: 26,
  isAdmin: true,
  profession: 'Software Engineer'
}
````

//--- Add using Bracket Notation :-

for eg,
````
const subjects = {
  101: "Physics",
  102: "Biology",
  103: "Chemistry"
};

subjects[104] = "Computer";

// Same as subjects[200] = "Mathematics"
subjects[100 * 2] = "Mathematics"; 

console.log(subjects);

# OUTPUT:- 
{
  '101': 'Physics',
  '102': 'Biology',
  '103': 'Chemistry',
  '104': 'Computer',
  '200': 'Mathematics'
}
````

#### Get Object Keys - Object.keys() :-

-  We can get all the keys of an object using Object.keys(). 
-  It returns the keys as an array of strings.
-  Object.keys() function return list of all keys in an object.
-  for eg,
````
const subjects = {
  101: "Physics",
  102: "Biology",
  103: "Chemistry"
};

console.log(Object.keys(subjects))

// OUTPUT :
[ '101', '102', '103']
````

#### Get Object Values - Object.values() :-

-  We can get all the values of an object using Object.values(). 
-  It returns the values as an array of different types.
-  Object.values() return the value in a list.
-  for eg,
````
const subjects = {
  101: "Physics",
  102: "Biology",
  103: "Chemistry"
};

console.log(Object.keys(subjects))

// OUTPUT :
[ 'Physics', 'Biology', 'Chemistry']
````

#### Get Object Keys and Values - Object.entires() :-

-  We can get all the key-value pairs of an object using Object.entries(). It
   returns the key-value pairs as an array of array
-  Object.entries(person) returns an array in which all the elements are also
   arrays. In other words, Object.entries(person) returns an array with many
   arrays nested in it.
-  Each nested array contains the key and the value of a property of 'subjects',
   in that same order. The keys will be strings.
-  for eg,
````
const subjects = {
  101: ["Physics","P2"],
  102: "Biology",
  103: "Chemistry"
};

// { '101': [ 'Physics', 'P2' ], '102': 'Biology', '103': 'Chemistry' }
console.log(subjects);

// [ '101', '102', '103' ]
console.log(Object.keys(subjects))

// [ [ 'Physics', 'P2' ], 'Biology', 'Chemistry' ]
console.log(Object.values(subjects))

// [ [ '101', [ 'Physics', 'P2' ] ], [ '102', 'Biology' ], [ '103', 'Chemistry' ] ]
console.log(Object.entries(subjects))
````

#### Object Shorthand :-

-  Generally, we define object like this,
-  for eg,
````
const model = 2011;
const fuelType = "diesel";

const car = {
  model: model,      // Here, model is a variable;
  fuelType: fuelType,   // Here, fuelType is a variable;
};

console.log(car);
````
 
- Here, we can use object shorthand
-  for eg,
````
const model = 2011;
const fuelType = "diesel";

const car = {
  model,
  fuelType,
};

console.log(car);
````

#### Object Naming Conventions :-

-  The name of the variable to which an object is assigned should give a clear
   description of what the object holds.
-  The name user itself gives the idea that the value is an object that
   contains information on a user. Suffixing user with Object or Data is
   redundant
-  for instance, an object that contains information on a user should not be
   given names such as object, data, info or any other name that does not
   describe the content of the object
-  for eg,
````
// This is a bad name
const object = { name: "Sam", age: 32 };
console.log(object);

// This is a good name
const user = { name: "Oliver", age: 23 };
console.log(user);
````
-  The name of object properties, i.e., the keys of objects should also follow
   the naming conventions of a variable.
-  for eg,

````
// These are bad key names
const user = {
  "first-name": "Sam",  // Name is not in camel case
  "last name": "Smith",    // Name is not in camel case
  number: 32, // Name does not give good description of value
};
console.log(user);

// These are good key names
const member = {
  firstName: "Oliver",
  lastName: "Smith",
  age: 23,
};
console.log(member);
````


-------------------------------------------------------------------------------------
### Q004 : Undefined and null - Javscript;;

#### Undefined Datatype :-

-  A variable declared using let, whose value hasn't been assigned yet, has
   undefined as its default value.

NOTE : A variable declared using 'const' should always have a value assigned to
it. It won't get automatically assigned with undefined if no value is given
during declaration.
for eg,
````
const age
console.log(age)

// SyntaxError: Missing initializer in const declaration
````

#### Null Datatype :-

The 'null' is a data type in JavaScript. It is used to denote the value of
nothing in a variable.

for eg,
````
const name = null;
console.log(name);      // output: null
````

#### Undefined vs Null :-

-  typeof of a variable assigned with undefined keyword, is always undefined.
-  typeof of a variable assigned with null, is always object.
-  Equality of undefined with null, is always true.

for eg,
````
let name1 = undefined
let name2 = null 

console.log(typeof name1)     // undefined
console.log(typeof name2)     // object
console.log(name1 == name2)   // true
console.log(name1 === name2)  // false
````


-------------------------------------------------------------------------------------
### Q003 : Number - Javascript;;

#### Store Number :-

-  Number can be positive, negative, fraction.
-  for eg,
````
const num1 = 1290
const num2 = -1290
const num3 = 12.90

console.log(f`num1: ${num1} || num2 : ${num2} || num3: ${num3}`)

# Output :-
num1: 1290 || num2 : -1290 || num3: 12.9
````

#### NaN (Not a Number) :-

-  NaN stands for Not a Number
-  Arithmetic operation on a value that is not a number, we get NaN as the result.

-  for eg, check for NaN existence ...

````
const personID = "123abc";
const quotient = personID / 2;

console.log(quotient)
console.log(isNaN(quotient))

# Output:-
NaN
true
````

#### Uniary Operator :-

-  Operator (++), (--) is used to increment the value of a number by 1.
-  for eg,
````
var number = 10
console.log(number)  # 10

number++
console.log(number)  # 11

number++
console.log(number)  # 12
````

#### Remainder (%) :-

-  We can use % to get the remainder. It returns the remainder after the
   division of the value on the left of % by the value on the right of %.
-  for eg,
````
console.log(5 % 3);

# Output : 2
````

-----------------------------------------------------------------------------------
### Q002 : String - Javascript;;

#### Create String :-

for eg,
````
const fullName = "Sam Smith";
console.log(fullName);              # Sam Smith

const book = "The Newest Dragon Stories";
console.log(book);                  # The Newest Dragon Stories

const someRandomSentence = "You can be a great programmer!";
console.log(someRandomSentence);    # You can be a great programmer!
````

#### Joining Strings :-

We can join the string using add '+' operator.

for eg,
````
let firstname = "Neeraj"
let middleName = "Singh"
let lastName = "Junior"

console.log(firstName + middleName + lastName)  # Neeraj Singh Junior
````

#### Template Strings :-

-  Backticks should be used to create a string only when there is a need to
   escape double quotes in the string.
-  for eg,
````
console.log(`Hello, I am a "software developer".`);

# Output :-
Hello, I am a "software developer".
````

-  Backtick is also used to create multi-line strings for formatting.
-  for eg,

````
const itemList = `Fruits:
  Apple
  Mango
  Banana
  Orange
`;

console.log(itemList)

# Output :-
Fruits:
  Apple
  Mango
  Banana
  Orange
````

-  Inserting values from variables into template strings using the ${} 
   notation is called string interpolation.
-  for eg,

````
const firstName = "Sam";
const lastName = "Smith";

// We don't need to do: firstName + " " + lastName, anymore.
const fullName = `${firstName} ${lastName}`;

console.log(fullName);

# Output:-
Sam Smith
````

-------------------------------------------------------------------------------------
### Q001 : Variable - Javascript;;

#### Console Log:-

In js, console.log() to make it visible on a special screen called console.

for eg,
````
console.log("I love ice cream");
````

#### Data Types :-

Different programming languages work with different sets of data types.
JavaScript also has a set of data types it can work with.

//--- Variables :-

-  Variable like `const length = 120`, stores the value 120 in a variable named length.
-  Once the variable is created, we can use the variable name, 'length' in the
   entire code

for eg,
````
const length = 120;

console.log("Length in centimeters:");
console.log(length);

console.log("Length in kilometers:");
console.log(length / 100000);
````

//--- const and let keywords :-

-  const: It used to declare a variable whose value is not intended to be
   changed at all, once it is declared.
-  let : It is used to declared variable whose value can be changed anywhere
   in the code.

NOTE : we can create variables without using the const and the let keyword.

````
for eg,
count = 20
console.log(count) // This will work;;
````

but, this is considered as bad practice.

//--- typeof :-

-  typeof keyword is used to return the type of instance.

for eg,
````
count = 20
console.log(typeof count)              # number 
console.log(typeof "Hello World")      # string
````

//--- Naming Variable :-

-  Variable are always case sensitive in javascript .
-  Javascript uses the camel case conventions for naming variable in javascript.

# Rule of Naming variable are ...
1) Name can be start with lowercase or uppercase.
2) Underscore is allowed for naming variable.
3) Digits can be used for naming variable, but digit can't be placed at the start.
4) A reserved keyword cannot be used as a variable name. 

NOTE : Always name a variable precisely as per the code logic. Variable hold the 
responsibility to make code readable for other developer as well.

//--- Changing Data Type :-

for eg,
````
let lengthOfBox = 120;
console.log(lengthOfBox);                       # 120 

lengthOfBox = "120cm";
console.log(lengthOfBox);                       # 120cm

console.log("Length of box in meters");         # Length of box in meters 
console.log(lengthOfBox * 100);                 # NaN
````

//--- Boolean Variable :-

-  The values true and false are known as Boolean values.
for eg,
````
isAdmin = true
console.log(isAdmin)    # true
````

//--- Expression :-

-  An expression is a piece of code that evaluates to something. It contains
   at least one operator and one operand.

-  The assignment operator = requires two operands, a left-hand operand and a
   right-hand operand.

for eg,
````
console.log(23 + 45);

const length = 1000;
console.log(length / 100);

console.log(typeof ["Apple", "Banana"]);
````

# Key Points :-

1) `23 + 45` is an expression. + is the operator. 23 and 45 are operands.

2) `length = 1000` is an expression. = is the operator. length and 1000 are
operands.

3) `length / 100` is an expression. / is the operator. length and 100 are
operands.

4) `typeof ["Apple", "Banana"]` is an expression. typeof is the operator.
["Apple", "Banana"] is the operand

The operators +, -, *, and / are called arithmetic operators and are used to
perform arithmetic operations on numbers.

//--- Checking equality

We can use the === operator to check if two values are equal.

for eg,
````
console.log(9 === 9);   # true

console.log(9 == "9");  # true 

console.log(9 === "9"); # false
````


-------------------------------------------------------------------------------------