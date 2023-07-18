from time import sleep, time
from threading import Thread


def square(args):
	for a in args:
		sleep(0.2)
		print("Square: ", a*a)

def cube(args):
	for a in args:
		sleep(0.2)
		print("cube: ", a*a*a)


if __name__ == "__main__":
	a = time()
	args = [2,5,6,7,9,10]
	#--- Example 1: Simple Example
	# square(args)
	# cube(args)
	# # Run: 2.04 seconds

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

	# Run: 1.20 seconds
	b = time()
	print("time: ", b-a)

