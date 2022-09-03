def first(x): print(x)


def even(x): return(x%2 == 0)


def inc(x): return x+1


def dec(x): return x-1


def operate(func,x):
	res = func(x)
	return res


def smartFilter(func):
		def wrapper():
			print("filtering...")
			return func(flag)	

		return wrapper


@smartFilter
def number(flag=True):
	if(flag):
		return [x for x in range(100) if(x%2 ==0)]
	else:
		return [x for x in range(100) if(x%2 != 0)]
	

def smartCheck(func):
	def wrapper(a,b):
		if(b == 0): 
			return 

		return func(a,b)
	return wrapper


@smartCheck
def divide(a,b):
	return a/b


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


def warmGreeting(func):
	def wrapper(u1,u2):
		return (f"Hi {u1.title()}, I'm {u2.title()}. Nice To Meet You !")

	return wrapper


@warmGreeting
def greet(u1,u2):
	return (f"Hi {u1}, I'm {u2}. Nice To Meet You !")


def main():
	# Greeting Decorator;;;
	res = greet('anshul','sachin')
	print(f"res: {res}")

	### Percent and Start Decorator;;;
	printer("Learning Python Decorator")

	### Divide Decorator;;;
	# number(12,13)

	### Filter Decorator;;;
	"""
	res = filter(number,False)
	print(res()) 

	is equivalent to 

	@filter
	def number():
		// code to do something;

	"""
	# res = filter(number,False)
	# print(res())


	### Higher order function 2 ;;;
	# res1,res2 = operate(inc,3), operate(dec,10)
	# print(f"res1::res2 => {res1}::{res2}")

	### mapping function;;;
	# nums = [x for x in range(100)]
	# # even = map(even, nums)
	# even = filter(even, nums)
	# for e in even:
	# 	print(e)


	### Higher order function;;;
	# first("hello,")
	# second = first
	# second("hello")






if __name__ == "__main__":
	main()