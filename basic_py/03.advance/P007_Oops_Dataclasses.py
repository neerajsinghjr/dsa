'''
-------------------------------------------------------------------------------------
-> Title: Oop Dataclasses
-> Attempted: 26-01-2025
-> Description:
-------------------------------------------------------------------------------------

Dataclass explorations !!!

-------------------------------------------------------------------------------------
'''

from dataclasses import dataclass, asdict
from datetime import datetime
from importlib import find_loader
from time import time
import json

def expl_test():
    """
    Testing Default in Dataclasses;;
    """
    @dataclass
    class Product:
        name: str
        price: int = 100

    p1 = Product(name="Pillow", price=50)
    p2 = Product(name="Coca Cola")
    print(f"Product 1: {p1}")
    print(f"Product 2: {p2}")


def expl_test_v2():
    """
    Api Request/Response Payload Schema generation using the datclasses payload;;

    Input:
        Request:
        {
            id: 1,
        }

    Return:
        Response:
        {
            "name": "neeru",
            "phone": "7897897890",
            "gender": "m",
            "address" : {
                "state": "delhi",
                "city": "delhi",
                "pincode": "200101"
            }
        }
    """
    @dataclass
    class UserRequest:
        id: int

    @dataclass
    class Address:
        state: str
        city: str
        pincode: str

    @dataclass
    class UserResponse:
        name: str
        phone: str
        gender: str
        address: Address

    req = {"id": 1}

    user_req = UserRequest(**req)
    print(f"user_req: ", user_req)

    # assume record fetch from database;;
    record = {
        "name": "neeru",
        "phone": "7897897890",
        "gender": "m",
        "address" : {
            "state": "delhi",
            "city": "delhi",
            "pincode": "200101"
        }
    }

    user_addr = Address(**record.pop("address"))
    user_resp = UserResponse(**record, address=user_addr)
    print("user_req: ", user_resp)

    final_response = json.dumps(asdict(user_resp)   )
    # final_response = json.dumps(user_resp.__dict__)   # this wont work;;
    print(f"Final Json Response: ", final_response)

    return final_response


def expl_test_v1():
    """
    Basic Exploration with respect to dataclasses in Python;;
    """

    @dataclass
    class Student:
        name: str
        grade: str
        age: int


    class Person:
        fname: str
        mname: str
        lname: str
        fullname: str

    # runner for expl_test_v1;;
    s1 = Student(name="Neeru", age=16, grade="A")
    print("s1: obj:", s1)
    print(f"s1: dict : {s1.__dict__}")
    print(f"s1: dict : {s1.__dict__.keys()}")


##---Main Execution;;
def main():
    expl_test()

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")