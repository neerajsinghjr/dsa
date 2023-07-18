from time import sleep, time
from multiprocessing import Process


def square(args):
	for a in args:
		sleep(5)
		print("Square: ", a*a)

def cube(args):
	for a in args:
		sleep(5)
		print("cube: ", a*a*a)


if __name__ == "__main__":
	a = time()
	args = [2,5,6,7,9,10]

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

	# Run: 1.20 seconds
	b = time()
	print("time: ", b-a)
	print("Runned Successfully...")
