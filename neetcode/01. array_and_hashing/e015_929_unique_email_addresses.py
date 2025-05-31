'''
-------------------------------------------------------------------------------------
-> Problem Title: 929. Unique Email Addresses
-> Problem Status: Completed
-> Problem Attempted: 22/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/unique-email-addresses/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        _stdin:
            arg1: list[str]
        _stdout: int
        """
        return self._ansv1(emails)
       
    def _ansv1(self, emails: List[str]):
        """
        _run: accepted (brute-force)
        _code: tc: o(n^2), sc: o(n), rt: 3 ms
        _choke:
        _brief:
        - approach follows exactly what the question says ...
        - local_name: replace() for replacing the dot character and trimming index 
        from start to plus character if any observed
        - domain_name: have to do nothing at all.
        - final combined mail should be add to the mail set for return unqiue mail
        """
        mails = set()
        for email in emails:
            ln, dn = email.split("@")
            # c1 : removal dot operator
            ln = ln.replace(".", "")
            # c2: ignore chars after plus sign;;
            ln = ln[0:ln.index("+")] if "+" in ln else ln
            # final email
            mail = f"{ln}@{dn}"
            mails.add(mail)

        return len(mails)
    

##---Main Execution;;
def main(res=None):
    try:
        data = []
        obj = Solution()
        res = None
        print(f"Result: {res}") if res else print("Empty!")

    except(Exception) as e:
        print(f"Exception Traced : {e}")

    else:
        print("Program Completed : Success")

    finally:
        print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
