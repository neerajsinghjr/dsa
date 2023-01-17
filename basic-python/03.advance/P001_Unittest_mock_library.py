'''
-------------------------------------------------------------------------------------
-> Title: Unittest Mock Library
-> Attempted:
-> Description: 
-------------------------------------------------------------------------------------

Unittest Mock library\ is used to mock object in the actual library

Ref : https://realpython.com/python-mock-library/

-------------------------------------------------------------------------------------
'''


import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
dt = Mock()     # Here, dt mocking datetime object;

def test_is_weekday():
    today = dt.today()  # today :  2019-01-01 00:00:00
    # Python's datetime library treats Monday as 0 and Sunday as 6
    cur_day = today.weekday()   # cur_day = 1

    return (0 <= cur_day < 5)   # True;

# Mock .today() to return Tuesday
print("@before: ", dt.today.return_value)  # @before: <Mock name='mock.today()' id='139762336560464'>
dt.today.return_value = tuesday     # tuesday :  2019-01-01 00:00:00
print("@after: ", dt.today.return_value) # @after tuesday :  2019-01-01 00:00:00

# Test Tuesday is a weekday
assert test_is_weekday() != 6   # 

# Mock .today() to return Saturday
dt.today.return_value = saturday

# Test Saturday is not a weekday
assert not test_is_weekday()