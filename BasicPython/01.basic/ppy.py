# decorator accepts a functions return a wrapper;
def decorator(abc, "Sdfsdf"):
	# wrapper can take argument directly from decorator;
	# Explcit : External function argument 
	# Decorator maker :
	def wrapper(xyz):
		return abc(xyz).upper()
	return wrapper


@decorator
def func(name):
	return "hello " + name

print(func("Neeraj", "url"))

