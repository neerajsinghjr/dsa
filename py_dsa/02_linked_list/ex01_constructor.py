'''
-------------------------------------------------------------------------------------
-> Problem Title: Constructor Exercise
-> Problem Status: Ongoing...
-> Problem Attempted: 04/11/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
        
# class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################


my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
"""
-------------------------------------------------------------------------------------
'''

from time import time

class Node:
	"""
	Node class will only create a node with a pointer pointing to null value;
	"""
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	"""
	Linked List class will used to create a list of non-contiguous blocks of
	nodes with one node points to another using the pointer.
	"""

	def __init__(self, value):
		# Initialize the linked list
		node = Node(value)
		self.head = node


##---Main Execution;;
def main():
	ll = LinkedList(4)
	print(ll.head.value)


if __name__ == '__main__':
	print("#------------ Code Start --------------#")
	startTime = time()
	main()
	endTime = time()
	print("Run Time:",endTime-startTime,"ms")
	print("#------------ Code Stop ----------------#")
