'''
Problem Description:
Reverse stack using recursion
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

# Reverse a Stack;
def reverseStack(stack) :
	if not stack:
		return stack
	
	size = len(stack)
	return reverse(stack,size)


def reverse(stack,size):
	# base condition;
	if(len(stack) == 0):
		return				# return main call;
	
	# hypothesis;
	lastItem = stack.pop()
	reverse(stack,len(stack))
	
	# induction;
	insert(stack,lastItem)
	
	return stack
	
	
def insert(stack,lastItem, popped=None):
	if(len(stack) == 0):
		stack.append(llastItem)
		return
	
	temp = stack.pop()
	insert(stack,lastItem,temp)
	stack.append(temp)
	return stack


# taking input
def takeInput() :

	n = int(input().strip())
	if(n == 0) :
		 return list(), n

	stack = list(map(int,stdin.readline().strip().split(" ")))
	return stack, n


def printStack(stack) :

	while(len(stack) > 0) :

		print(stack.pop(),end = " ")


# main
stack, n = takeInput()
reverseStack(stack)
printStack(stack)