````
-------------------------------------------------------------------------------------
-> Title : Linked List
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 04/11/2023
-> Updated : 04/11/2023
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q003 : Steps before Linked List Problems;;
-> Q002 : Linked List Operation;;
-> Q001 : Linked List Getting Started;;
-------------------------------------------------------------------------------------
````

#### LINKED LISt NOTES : BEGINNING 

-------------------------------------------------------------------------------------
#### Q003 : Steps before Linked List Problems;;

**Remember these key points before attempting Linked List problem**

1) Always note how many number of element is there in the problem.

CASE 1: if min element is 0, then add a check
````
for eg,
# Code Snippet;
if not self.head:
    # do some operation or fallback;;
else:
    # main case scenario is there
````

2) INSERT OPERATION: Before inserting in existing list, make sure to check if 



-------------------------------------------------------------------------------------
-> Q002 : Linked List Operation;;

**Insertion Operation**
- Insertion at 0th Index : O(1)
- Insertion at Kth Index : O(k)
- Insertion at Nth Index : O(n)

**Removing Operation**
- Remove from 0th Index : O(1)
- Remove from Kth Index : O(k)
- Remove from Nth Index	: O(n)

**Travering Operation**
- Traversing Element : O(n)

**Lookup By Index** : 
- Time Complexity : O(n)

**NOTE: Even though, you got the index, but you've to traverse full list.**

**Lookup By Value**
- Time Complexity : O(n)

**NOTE: Similary from previous case, if you got the value. You've to iterate 
it throughly.**


-------------------------------------------------------------------------------------
#### Q001 : Linked List Getting Started;;

- Linked List are non-contiguous data structure which store the value inside 
block and every block contains the pointer to the next block.

- Linked List is user-defined derived data-type which store the value in 
functional or object oriented notation.

- Linked List HEAD points to the first node of the list and TAIL points to the 
end node of the list.

- Linked List looks like this in python,

````	
HEAD : {
		"data": 1,
		"next": {
				"data": 2,
				"next": {
						"data": 3,
						"next": {					TAIL NODE 
								"data": 4,
								"next": None
						}
				}		
		}
}

# traversing through nodes
print(HEAD['next']['next']['next']['value'])	# Value 4 or tail node 
````

-------------------------------------------------------------------------------------