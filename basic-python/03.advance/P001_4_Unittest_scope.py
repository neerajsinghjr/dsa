'''
-------------------------------------------------------------------------------------
-> Title: Pytest Exception
-> Attempted: 
-> Description: 
-------------------------------------------------------------------------------------

Unittest Mock library is used to mock object in the actual library

Ref : https://realpython.com/python-mock-library/

-------------------------------------------------------------------------------------
'''


# Example 1: my_calender within scope;

import resources
from unittest.mock import patch


# Example 1: with scope
with patch('my_calender.is_weekday'):
	resources.my_calendar.is_weekday()
	