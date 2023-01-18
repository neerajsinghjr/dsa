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

import pytest

import pytest

import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_retry(self):
        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        # Set the side effect of .get()
        requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            print("@start : request -> get call : ", requests.get.call_count)
            get_holidays()
            # Code will never reached on line : 48 if exception occured;
            print("@Timeout Error: request -> get : ", requests.get.call_count)
            
        # Now retry, expecting a successful response
        assert get_holidays()['12/25'] == 'Christmas'
        # Finally, assert .get() was called twice
        print("@Success: request -> get call : ", requests.get.call_count)
        assert requests.get.call_count == 2

if __name__ == '__main__':
    unittest.main()