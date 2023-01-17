'''
-------------------------------------------------------------------------------------
-> Title: Unittest Oops
-> Attempted:
-> Description: 
-------------------------------------------------------------------------------------

Unittest Mock library is used to mock object in the actual library

Ref : https://realpython.com/python-mock-library/

-------------------------------------------------------------------------------------
'''

import main
import unittest
from unittest.mock import patch

@patch('main.get_fact')
def test_len_fact(self):
	mock_get_fact = main.get_fact()
	mock_get_fact.return_value = "Cat Lover!!!"
	print(">>>>>>>>>>>>>>>>> mock_get_fact : ", mock_get_fact)
	print(">>>>>>>>>>>>>>>>> mock_get_fact -> return_value : ", mock_get_fact.return_value)
	abc = main.len_fact()
	print(">>>>>>>>>>>>>>>>>>>>>>> abc : ", abc)
	assert abc > 0


# class TestCase(unittest.TestCase):
# 	@patch(get_fact)
# 	def test_len_fact(self, mock_get_fact):
# 		mock_get_fact.return_value = "Cat Lover!!!"
# 		assert len_fact() > 0


# if __name__ == "__main__":
# 	unittest.main()
