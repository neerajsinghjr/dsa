print("-----------------------------------CODE BEGINS ---------------------------------------")

from enum import Enum



try:

	a = 1001

	def check():
		Mind, Online, Mindmajix = range(3)
		print(Mind)
		print(Online)
		print(Mindmajix)
		print(10 * "aevil ")


	def startPattern(r):
		if not r:
			return(False, "'r' should be integer")

		for x in range(r):
			print(' '*(r-x-1)+'*'*(2*x+1))	


	def hi(name=None):
		if not name:
			print("Hi there...")
		else:
			print("Hi,",name)


	def functionV1():
		b = []
		print("type: ", (type(b) == tuple))
		print("instance: ", isinstance(b, list))
		print("try : {a}")



except Exception as e:
	print(f"Exception Traced: {e}")


finally:
	print("finally...")


#--- Main Execution ---#
def main():
	# functionV1()
	# hi(name="Amisha")
	# startPattern(r=1)
	# check()
	# isAnagram("jjj lsldf sjdknfjsd", "sdfsdf sdfsd")


if __name__ == "__main__":
	main()


print("-----------------------------------CODE ENDS -----------------------------------------")