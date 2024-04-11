from multiprocessing import Pool, Value, Lock, Process
from ctypes import c_int
from time import sleep


#------------------ EXAMPLE 1 : WITHOUT LOCK ------------------------# 

def deposit(balance):
	# Add 100rs from Balance
	for i in range(10):
		sleep(0.2)
		balance.value += 1


def withdraw(balance):
	# Deduct 100rs from balance
	for i in range(10):
		sleep(0.2)
		balance.value -= 1


def example1(balance):
	# Create Process
	p1 = Process(target=deposit, args=(balance,))
	p2 = Process(target=withdraw, args=(balance,))
	# Start Process;;
	p1.start()
	p2.start()
	# Join to main Process;;
	p1.join()
	p2.join()
	print("Current Balance v1 : ", balance.value)
	# OUTPUT: 
	# Current Balance v1: 203 (WRONG)


#------------------ EXAMPLE 2 : WITH LOCK ------------------------# 

def deposit_v2(balance,lock):
	# Add 100rs from Balance
	for i in range(10):
		sleep(0.2)
		lock.acquire()
		# Critical Section Locked
		balance.value += 1
		lock.release()


def withdraw_v2(balance,lock):
	# Deduct 100rs from balance
	for i in range(10):
		sleep(0.2)
		lock.acquire()
		# Critical Section Locked
		balance.value -= 1
		lock.release()


def example2(balance, lock):
	# Create Process
	p1 = Process(target=deposit_v2, args=(balance,lock))
	p2 = Process(target=withdraw_v2, args=(balance,lock))
	# Start Process;;
	p1.start()
	p2.start()
	# Join to main Process;;
	p1.join()
	p2.join()
	print("Current Balance v2 : ", balance.value)
	# OUTPUT: 
	# Current Balance v1: 200


#--------------------- MAIN EXECUTION -------------------# 

if __name__ == "__main__":
	bal = Value('i', 200)

	# Example 1: Without Lock
	example1(bal)

	# Example 2: With Lock 
	bal2 = Value('i', 200)	
	lock = Lock()
	example2(bal2, lock)

	print("Run Successfully")