from multiprocessing import Pool
from time import time

def func(x):
	sum = 0
	for x in range(1000):
		sum += x
	return sum


if __name__ == "__main__":
	lc = 1000000

	s = time()
	# Task 1 : Executing task with pool
	p1 = Pool()
	result = p1.map(func, range(lc))
	m1 = time()
	print(f"Time With Pool with default processes: {p1._processes} : ", m1-s)
	# OUTPUT : 
	# Time With Pool with default processes: 8 :  7.886874675750732

	# Task 2 : Executing Task 1 when specify process count
	pc = 3
	p2 = Pool(processes=pc)
	result = p1.map(func, range(lc))	
	m2 = time()
	print(f"Time With Pool with manual processes: {pc} : ", m2-m1 )
	# OUTPUT : 
	# Time With Pool with manual processes: 3 :  8.409621477127075

	# Task 3 : Executing same task without pool
	result = []
	for i in range(lc):
		result.append(func(i))
	e = time()
	print("Time Without multiprocessing pool: ",  e-m2 )
	# OUTPUT : 
	# Time Without multiprocessing pool:  28.447165489196777
