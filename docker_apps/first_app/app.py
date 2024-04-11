import os
import traceback
from time import time
from csv import writer


def save(user_id, user_name):
	file = f'user_log/file_{user_id}'
	header = ['user_id', 'name']
	mode = 'a' if os.path.exists(file) else 'w'
	
	try:
		data = [user_id, user_name]
		with open(file, mode) as fileobj:
			csv_obj = writer(fileobj)
			if mode == 'w':
				csv_obj.writerow(header)
			csv_obj.writerow(data)
	except:
		print("Error Occured: ", traceback.format_exc())


def main():
	print("Hi, Welcome")
	user_id = f"user_{round(time())}"
	user_name = input("Your Name: ")
	save(user_id, user_name)


if __name__ == "__main__":
	main()
