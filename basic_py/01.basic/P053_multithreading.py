from time import sleep, time
from threading import Thread

#------------------ Example 1 & 2 ------------#

def square(args):
	for a in args:
		sleep(0.2)
		print("Square: ", a*a)

def cube(args):
	for a in args:
		sleep(0.2)
		print("cube: ", a*a*a)


#------------------- Exampl 3 ------------------#
store = []

def quadratic(args):
	global store
	for a in args:
		store.append(a*4)

	print("result from function : ", store)


def example1(args):
	square(args)
	cube(args)


def example2(args):
	#--- Example 2: Multhithreading
	# Thread creation;;
	t1 = Thread(target=square, args=(args,))
	t2 = Thread(target=cube, args=(args,))
	
	# Start the thread;;
	t1.start() 
	t2.start()
	
	# Join to the main thread, if you remove this so even the end line
	# calculating time can work before square and cube function;
	t1.join()
	t2.join()

def example3(args):
	t1 = Thread(target=quadratic, args=(args,))
	t1.start()
	t1.join()

	# This will contains the result from the quadratic function call
	# becuase thread use the same memory address unlink process;
	print("result from main: ", store)


if __name__ == "__main__":
	a = time()
	args = [2,5,6,7,9,10]
	#--- Example 1: Simple Example
	# example1(args)
	# Run: 2.04 seconds

	#--- Example2 : Multithreading
	# example2(args)

	#--- Example3 : Mutithreading with global variable;;
	example3(args)

	# Run: 1.20 seconds
	b = time()
	print("time: ", b-a)

