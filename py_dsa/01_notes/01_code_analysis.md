````
-------------------------------------------------------------------------------------
-> Title : Code Analysis
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 04/11/2023
-> Updated : 24/11/2024
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q003 : Data Immutability Concept;;
-> Q002 : BigO Wrap Up Highlights;;
-> Q001 : Operation Pop, Insertion, Append;;
-------------------------------------------------------------------------------------
````

### CODE ANALYSIS NOTES : BEGINNING 

-------------------------------------------------------------------------------------
#### Q003 : Data Immutability Concept;;

Mutability is a concept in which we can change the values present inside any
variable without changing its memory location and similarly Immutability
doesnt allow the changing of the variable.

There are multiple types of data types

**IMMUTABLE**

1) Integer
2) String
3) Decimal 
4) Bool 
5) Tuple (Python Specific)

**MUTABLE**
1) class 
2) dictionary (Python Specific)
3) list (Python Specific)
4) deque

**Example to show Mutability & Immutability Concept ...**

````
- eg1, Integer Illustration
a = 10
print(id(a))	# 140218953167208

a = 0
print(id(a))	# 140218953166888
````

**NOTE: Integer are immutbable that's new memory location assigned as soon as 
we overwrite the variable.***

````
- eg2, String Illustration
c = 'neeraj'
print(id(c))	# 140218943997360

c = 'singh'
print(id(c))	# 140218941933680
````

**NOTE: Similary with string case as well** 

````
- eg3, Dictionary Illustration

# dictionary with key "a";;

dict1 = {"a": 1}
print("dict:",id(dict1))		# 140218944304384
print("a:", id(dict1["a"]))		# 140218953166920

# dictionary with key "b";;

dict1["b"] = 2
print("dict:", id(dict1))		# 140218944304384
print("b:", id(dict1['b']))		# 140218953166952

# new dictionary with dict2

dict2 = dict1
dict2['a'] = 10
print("dict1:", id(dict1))		# 140077584004672
print("dict2:", id(dict2))		# 140077584004672
print("dict1:", dict1)			# {'a': 10, 'b': 2}
print("dict2:", dict2)			# {'a': 10, 'b': 2}
````

**NOTE: Here you can see that dict memory location is same when you add the 
new key value inside the dictionary and same will show in delete as well.**


-------------------------------------------------------------------------------------
#### Q002 : BigO Wrap Up Highlights;;

- BigO(n!) : Highlight Factorial but Horrible algorithms.

- BigO(n^2) : Highlights because of loop with loop.

- BigO(n) : Highlights Linearity or Proportional.

- BigO(logn) : Highlight Divide and Conquer

- BigO(1) : Highlights Constants 


-------------------------------------------------------------------------------------
#### Q001 : Operation Pop, Insertion, Append;;

#### POP OPERATION;;

If you pop operation removing element from the end of the list then the time
complexity would be o(1) because it only take one operation to remove
anything from the end.

````
eg, a = [1,2,3,4]
a.pop() # 4, Needs o(1)
````

But, If you are popping element which is present inside the index of 0th then
the algorithm of that data structure will try to reshuffle its indexing
again. 

````
eg, a = [1,2,3,4]
a.pop(0) # rest [2,3,4] needs to be rearrange itself in proper order of a list;;
````

Reshuffling the index will take O(n) operation to rearrange.

#### INSERTION OPERATION;;

Insertion operation is take O(1), if you are inserting at the end. 
 
````
eg,
a = [0]
a.insert(len(a), 1)	# o(1) only for insertion;;
````

But will take o(n), if it's inserting new values at kth index then all the
kth + 1 indexes needs to rearrange itself again

````
eg,
a = [0,1]
a.insert(1, 2) # o(k) or o(n) in worst case scenario;;
````

#### APPEND OPERATION;;

Append will take only o(1) operation time, because it always insert at the end 
of the list.

````
eg,
a = [0,1,2,3]
a.append(4)	# o(1)
````


--------------------------------------------------------------------------------------