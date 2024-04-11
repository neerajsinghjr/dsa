from time import sleep, time
from multiprocessing import Process, Array, Value, Queue


#------------------- Exampl 1 & 2 ------------------#
def square(args):
	for a in args:
		sleep(5)
		print("Square: ", a*a)

def cube(args):
	for a in args:
		sleep(5)
		print("cube: ", a*a*a)


def example1(args):
	#--- Example 1: MultiProcessing Both the below process are running
	# simultaneously together
	
	# Process Creation;;
	p1 = Process(target=square, args=(args,))
	p2 = Process(target=cube, args=(args,))
	
	# Start the Process;;
	p1.start() 
	p2.start()
	
	# Join to the main Process, if you remove this so even the end line
	# calculating time can work before square and cube function;
	p1.join()
	p2.join()



#------------------- Exampl 2 ------------------#
store = []

def quadratic(args):
	global store
	for a in args:
		store.append(a*4)

	# This result will not empty because every process have their own memory
	# address that's why the store variabe empty (ref quadratic method)
	print("result from function : ", store)


def example2(args):
	p3 = Process(target=quadratic, args=(args,))
	p3.start()
	p3.join()

	# This result will be empty because every process have their own memory
	# address that's why the store variabe empty (ref quadratic method)
	print("result from main: ", store)

#------------------- Exampl 3 ------------------#

def quadratic_v2(args, result):
	for i,k in enumerate(args):
		result[i] = k*k

	print("result from function: ", result[:])
	

def example3(args):
	result = Array('i', 6)
	# Result in multiprocessing array case:-
	# result from function:  [4, 25, 36, 49, 81, 100]
	# result from main :  [4, 25, 36, 49, 81, 100]

	# result = [0]*6
	# Result in normal argument:-
	# result from function:  [4, 25, 36, 49, 81, 100]
	# result from main :  [0, 0, 0, 0, 0, 0]

	# single variable sharing purposes;
	# val = Value('new_value', 50.9)

	p1 = Process(target=quadratic_v2, args=(args, result))
	p1.start()
	p1.join()

	print("result from main : ", result[:])
	# print("result from main (~value) : ", val.value)


#------------------- Exampl 4 ------------------#
def quadratic_v4(args, que):
	for i in args:
		que.put(i*i)

	# print("from function ...")
	# while not que.empty():
	# 	print(que.get())


def example4(args):
	que = Queue()
	p1 = Process(target=quadratic_v4, args=(args, que))
	p1.start()
	p1.join()

	print("from main ...")
	while not que.empty():
		print(que.get())


#------------------- MAIN EXECUTION ------------------#

if __name__ == "__main__":
	# NOTE : Here address memory is referred to those memory where a program store
	# variable, argument, control statement etc.

	a = time()
	args = [2,5,6,7,9,10]

	#--- Example 1: Without Multiprocess implementation
	# example1(args)

	#--- Example 2: Showing different memory address usages in multiprocess
	# example2(args)

	#--- Example 3: How to use shared data between multiprocess using array and value
	# example3(args)
	
	#--- Example 4: How to use shared data between multiprocess using QUEUE (Shared Memory)
	"""
	Multiprocessing Queue 
		- lives inside the shared memory on global.
		- Used to shared data between process.
	Normal Queue
		- live inside in-process memory.
		- Used to shared data between queue
	"""
	example4(args)

	# Run: 1.20 seconds
	b = time()
	print("time: ", b-a)
	print("Run Successfully...")
