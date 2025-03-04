'''
-------------------------------------------------------------------------------------
-> Title: Testrun
-> Attempted: 04-02-2025
-> Description:
-------------------------------------------------------------------------------------

Exploratory testrun file for python;;

-------------------------------------------------------------------------------------
'''
import gc
import sys
import asyncio
import inspect
import multiprocessing
from asyncio import gather
from random import randint
from time import time, sleep
from functools import reduce
from datetime import datetime
from multiprocessing import Process
from collections import namedtuple
# from distutils.util import strtobool

DEBUG = True
count = 0
memory = {}


def expl():
    from copy import copy, deepcopy
    list_1 = [1, 2, [3, 5], 4]

    # Shallow Copy : ShallowCopy only copy the parent reference
    list_2 = copy(list_1)
    list_2[3] = 7
    list_2[2].append(6)
    print(list_2)  # output => [1, 2, [3, 5, 6], 7]
    print(list_1)  # output => [1, 2, [3, 5, 6], 4], ie. child [3,5,6] are same both list list_2 & list_1

    ## deep copy
    list_3 = deepcopy(list_1)
    list_3[3] = 7
    list_3[2].append(6)
    print(list_3)  # output => [1, 2, [3, 5, 6, 7], 8]
    print(list_1)  # output => [1, 2, [3, 5, 6], 4] i.e, here parent & child both independent;;

def expl_v27():
    # generator vs iterator;;
    def hundred_numbers():
        num = 0
        while num < 100:
            yield num
            num += 1

    print(next(hundred_numbers()))  # 0
    print(next(hundred_numbers()))  # 1
    print(list(hundred_numbers()))  # 2


def expl_v26():
    # exploring generator <-> iterator;;

    # ----------- Example 1 ------------- #
    class Fib:
        def __init__(self):
            self.a, self.b = 0, 1

        def __iter__(self):
            while True:
                yield self.a
                self.a, self.b = self.b, self.a + self.b

    # When we pass an iterable to iter(), It gives us an iterator
    f = iter(Fib())
    for i in range(3):
        print("i: ", next(f))

    # ----------- Example 2 ------------- #
    class FibV2:
        def __init__(self):
            self.a, self.b = 0, 1

        # __iter__ will generate iterable
        def __iter__(self):
            return self

        # __next__ will generate sequence;;
        def __next__(self):
            return self.a  # Observe, return used not yield
            self.a, self.b = self.b, self.a + self.b

    # since iter just returns the instance itself, we don't need to call it.
    f = FibV2()
    for i in range(3):
        print("i_v2: ", next(f))


def expl_v25():
    # exploring minvalue and maxvalue in python code;;
    from sys import maxsize

    minValue = -maxsize
    maxValue = maxsize

    print(minValue, maxValue)


def expl_v24():
    # C3 Superclass Linearization in Python to handle multiple inheritance
    # or, To determine the parent class when child class is derived from
    # more than one base class;;
    # This follows below approach;;
    # step 1: Start with child class (D in our case)
    # Step 2: Follow up gather all the parent class (B, C, E)
    # Step 3: Merge all the parent class together and make sure you preserve the derived order
    # Step

    class A:
        def foo(self):
            print("A")

    class A2:
        def foo(self):
            print("A2")

    class B(A):
        def foo(self):
            print("B")

    class C(A):
        def foo(self):
            print("C")

    class E(A, A2):
        def foo(self):
            print("E")

    class D(B, C, E):
        pass

    obj_d = D()
    obj_d.foo() # B
    print(D.__mro__)
    # (
    #     <class '__main__.expl.<locals>.D'>,
    #     <class '__main__.expl.<locals>.B'>,
    #     < class '__main__.expl.<locals>.C' >,
    #     < class '__main__.expl.<locals>.E' >,
    #     < class '__main__.expl.<locals>.A' >,
    #     < class '__main__.expl.<locals>.A2' >,
    #     < class 'object' >
    # )


def expl_v23():
    # exploring f-string padding;;

    print(f"digit: result: {9:05d}")       # 00009
    print(f"digit: result: {99:05d}")      # 00099
    print(f"digit: result: {999:05d}")     # 00999
    print(f"digit: result: {9999:05d}")    # 09999
    print(f"digit: result: {99999:05d}")   # 99999
    print(f"digit: result: {9999999:05d}")   # 99999

    print(f"float: result: {9:05f}")        # 9.000000
    print(f"float: result: {99:05f}")       # 9.000000
    print(f"float: result: {999:05f}")      # 99.000000
    print(f"float: result: {9999:05f}")     # 9999.000000
    print(f"float: result: {99999:05f}")    # 99999.000000

    print(f"float: result: {0.9:05f}")      # 0.900000
    print(f"float: result: {0.99:05f}")     # 0.990000
    print(f"float: result: {0.999:05f}")    # 0.999000
    print(f"float: result: {0.9999:05f}")   # 0.999900
    print(f"float: result: {0.99999:05f}")  # 0.999990


def expl_v22():
    # Exploring Re-Raise Error Exception;;
    age = 999  # Given, age

    def errorLogging(e):
        print("Log Snapshot Captured ...")

    class InvalidAgeException(Exception):
        pass

    try:
        if not (1 <= age <= 100):
            print("Code before raising the custom exception ...")
            raise InvalidAgeException("Exception : Invalid Age Found !!!")

    except InvalidAgeException as err:
        # Here, Storing the log to the file;
        errorLogging(err)

        # then again raising the error;
        raise err   # alternative writing, raise(err)

    except Exception as e:
        print("Exception Traced Here : ", e)

    finally:
        print("Finally Block Executed !")


def expl_v21():
    # Exploring namedtuple collections;;
    Person = namedtuple("Person", ["f_name", "m_name", "l_name", "s_Id"])
    p1 = Person("Neeraj", "Singh", "Junior", "1001")

    print(f"FirstName: {p1.f_name}")
    print(f"MidName: {p1.m_name}")
    print(f"LastName: {p1.l_name}")
    print(f"SocialId: {p1.m_name}")


def expl_v20():
    # exploring decorators in python only;;
    # --- EAMPLE 1 --- #
    def runtime(func):
        def wrapper(*args, **kwargs):
            print(f"Received Parameter: args: {args}, kwargs: {kwargs}")
            st = time()
            resp = func(*args, *kwargs)
            et = time()
            print("Finished __runtime__: ", et-st)

        return wrapper

    @runtime
    def hello_word(user="Default"):
        print(f"Loading Task Modules In Memory ...", end=sleep(3))      # 3 Seconds;;
        print("Hello World")
        print(f"Flushing Task Modules From Memory ...", end=sleep(3))   # 3 Seconds;;

    hello_word(user="Neeraj")

    # --- EXAMPLE 2 --- #
    def measure_time(function):
        def wrapper(*args, **kwargs):  # <-- accepts arguments
            print(f"args : {args} || kwargs : {kwargs}")
            start = time()
            result = function(*args, **kwargs)  # <-- Pass arguments to function i.e hello()
            end = time()
            print(f"Time taken: {end - start} seconds")
            return result

        return wrapper  # <-- Notice here just memory reference to the function defination;

    @measure_time
    def hello(*args, **kwargs):
        print("your v-args:", args)
        print("your kw-args:", kwargs)

    hello("Python", "Guido Van Rosseum", xyz=20, abc=30)


def expl_v19():
    # Exploring class decorator over the function;;
    class StoreResults:
        """
        @classname
        Here, you've defined the class as a decorator on a regular function.
        In class, you have to received the function name inside the __init__
        method using any keyword.
        Like this,
            def __init__(self, function): ...

        and the given functional arguments from external function (~add())
        will be received by the __call__() magic methods.
        """
        def __init__(self):
            self.result = []            # <-- lists to store result;

        def __call__(self, func):

            def wrapper(*args, **kwargs):
                print("LOG: args:", args)            # debugger 1
                print("LOG: kwargs:", kwargs)        # debugger 2
                res = func(*args, **kwargs)
                self.result.append(res)
                return self.result

            return wrapper


    @StoreResults
    def add(a,b, y,z):
      return a+b


    if __name__ == "__main__":
      print(add(10, 10, y=10, z=20))
      print(add(11, 11, y=22, z=33))


def expl_v18():
    # exploring normal decorator function over the class;;

    def printUppercase(_class):
        # Problem: Here we are overwriting the old show method in which we
        # are also calling another decorator.
        # Solution is to preserve the show method original call and then
        # return the original method call before the wrapper ends;;
        print(" Calling printUppercase(): _class: ", _class)

        # Main Wrapper Starts Here
        def wrapper(self):
            res = self.word.upper()
            print(f"before: {self.word}, after: {res}")
            self.word = res
            return self.word

        # _class.show =  wrapper
        # here, we are overriding the memory reference of show method
        # from the class to the wrapper function of the decorator.
        # So that we can modify or extends the functional requirement
        # of that function.

        _class.show = wrapper  # Overriding old show function with wrapper

        return _class

    def printUppercase_v2(_class):
        # Solution for previous version fix;;
        print(" Calling printUppercase_v2(): _class: ", _class)

        _original_show = _class.show

        # Main Wrapper Starts Here
        def wrapper(self):
            res = self.word.upper()
            print(f"before: {self.word}, after: {res}")
            self.word = res
            return _original_show(self)

        # _class.show =  wrapper
        # here, we are overriding the memory reference of show method
        # from the class to the wrapper function of the decorator.
        # So that we can modify or extends the functional requirement
        # of that function.

        _class.show = wrapper  # Overriding old show function with wrapper

        return _class

    def convertStrToList(func):
        print(f" Calling convertStrToList(): func: ", func)

        def wrapper(*args, **kwargs):
            print(f"*args: {args}, kwargs: {kwargs}", )
            res = func(*args, **kwargs)
            res_list = res and res.split(" ")
            print(f" response: convertStrToList: {res_list}")
            return res_list

        return wrapper

    # @printUppercase_v2  # bug fixed;;
    @printUppercase   # observed bug;;
    class Dictionary:

        def __init__(self):
            self.word = f"word of the day is --->maddness<---"

        @convertStrToList
        def show(self):
            print(f"from in-built memory: {self.word}")
            return self.word

    print("__executing_main__")
    obj = Dictionary()
    print(f"__finished_main__: ", obj.show())

    # original logs;;
    # Calling convertStrToList(): func:  <function expl.<locals>.Dictionary.show at 0x7330f59c0c10>
    # Calling printUppercase(): _class:  <class '__main__.expl.<locals>.Dictionary'>
    # __executing_main__
    # before: word of the day is --->maddness<---, after: WORD OF THE DAY IS --->MADDNESS<---
    # __finished_main__:  WORD OF THE DAY IS --->MADDNESS<---

    # v2 logs;;
    # Calling convertStrToList(): func:  <function expl.<locals>.Dictionary.show at 0x7ee1a78c0c10>
    # Calling printUppercase_v2(): _class:  <class '__main__.expl.<locals>.Dictionary'>
    # __executing_main__
    # before: word of the day is --->maddness<---, after: WORD OF THE DAY IS --->MADDNESS<---
    # *args: (<__main__.expl.<locals>.Dictionary object at 0x7ee1a786f280>,), kwargs: {}
    # from in-built memory: WORD OF THE DAY IS --->MADDNESS<---
    # response: convertStrToList: ['WORD', 'OF', 'THE', 'DAY', 'IS', '--->MADDNESS<---']
    # __finished_main__:  ['WORD', 'OF', 'THE', 'DAY', 'IS', '--->MADDNESS<---']


def expl_v17():
    # # epxloring bit operator;;
    # nums = [4, 10, 46, 20, 34, 64, 4, 97, 24]
    #
    # for num in nums:
    #     res = num | 1
    #     print(f"res is now ", {res})

    # XOR Code;;
    nums = [
        34, 3, 64, 33, 22, 574, 74, 6, 3, 2, 574,
        43, 33, 789, 6, 64, 43, 22, 789, 34, 2
    ]

    i, result = 0, 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(f"nums[i]: {nums[i]}, b({bin(nums[i])}), "
                  f"nums[j]: {nums[j]}, b({bin(nums[j])})")
            status = nums[i] ^ nums[j]
            print("status: ", status)
            # Status : 0 means number is duplicate;
            # if (status == 0):
                # break
        # status not 0 means loop iterated success and unique number is found;
        # if (status != 0):
        #     result = nums[i]
        #     break

        print(f"Result : {result}")


def expl_v16():
    # ----------- chain ------------- #
    from itertools import chain

    # Example iterables
    iterable1 = [1, 2, 3]
    iterable2 = ['a', 'b', 'c']
    iterable3 = (10, 20, 30)

    # Using itertools.chain to combine the iterables
    combined_iterable = chain(iterable1, iterable2, iterable3)

    # Iterating over the combined iterable
    for item in combined_iterable:
        print(item, end="->")

    print()

    # ----------- compress ------------- #
    from itertools import compress

    students = ["John", "Vishnu", "Kabir", "Shreya", "Rose"]
    results = [True, False, True, True, False]

    # test 1:
    # filtered = compress(students, results)

    filtered = compress(results, students)
    print(list(filtered))


def expl_v15():
    from itertools import zip_longest

    # ---------- ERRORED BUG ----------- #
    class IterCls:

        def __init__(self):
            self.id = 0

        def __iter__(self):
            return self.id  # Mistake : __iter__ return an iterable object not an integer;;

        def __next__(self):
            self.id += 1
            return self.id

    # test = IterCls()
    # print(f"test: ", next(test.id)) # Mistake, needed an integer not an attribute;;
    # print(f"test: ", next(test.id)) # Mistake, needed an integer not an attribute;;

    # ---------- /ERRORED BUG ----------- #

    # ---------- FIXED CODE ------------- #
    class IterCls:

        def __init__(self):
            self.id = 0

        def __iter__(self):
            return self

        def __next__(self):
            self.id += 1
            return self.id

    test = IterCls()
    print(f"test: ", next(test))
    print(f"test: ", next(test))
    print(f"test: ", next(test))


def expl_v14():
    # Exploring: rsplit() is right split with
    # rsplit(delimiter, maxsplit)

    txt = "app.worker.transaction.transact_via_bse"

    x = txt.rsplit(".")
    print("x : ", x)  # x :  ['app', 'worker', 'transaction', 'transact_via_bse']

    y = txt.split(".")
    print("y : ", y)  # y :  ['app', 'worker', 'transaction', 'transact_via_bse']

    a = txt.rsplit(".", 1)
    print("a : ", a)  # a :  ['app.worker.transaction', 'transact_via_bse']

    b = txt.rsplit(".", 2)
    print("b : ", b)  # b :  ['app.worker.transaction', 'transact_via_bse']


def expl_v13():
    # Exploring: Garbage Collector;;
    class A:
        def __init__(self):
            self.ref = None

    a = A()
    b = A()

    a.ref = b  # a → b
    b.ref = a  # b → a (circular reference)

    print("ref.a: ", sys.getrefcount(a))
    print("ref.b: ", sys.getrefcount(b))

    del a, b  # Objects are not freed due to the cycle

    print(gc.collect())  # Force garbage collection


def expl_v12():
    # Exploring: Enums Classes in Python;
    from enum import Enum

    class Transaction(Enum):
        SUCCESS = 1
        PENDING = 2
        FAILURE = 3

    print(f"Transaction : {Transaction.SUCCESS}")
    print(f"Transaction : {Transaction.SUCCESS.value}")
    print(f"Transaction : {Transaction['SUCCESS']}")
    print(f"Transaction : {type(Transaction['SUCCESS'])}")
    print(f"Transaction : {repr(Transaction['SUCCESS'])}")


def expl_v11():
    # Exploring multiprocessing pool;;
    def square(iter, sum=0):
        print(f"Process Iteration: ", iter)
        for i in range(10**3):
            sum += i
        return (True, {f"iter_{iter}": "success", "sum": sum})

    # Main Multiprocessing mapping with Pool;;
    with multiprocessing.Pool as pool:
        result = pool.map(square, range(3))
        print(result)


def expl_v10():
    # calling async without await;;
    async def foo():
        print("Hello")
        return 42

    result = foo()  # ❌ This returns a coroutine, not a result
    print(result)


def expl_v9():
    # checking asyncio multi-task independency - trying different way;;
    async def task(name, seconds):
        print(f"{name} started")
        await asyncio.sleep(seconds)
        print(f"{name} completed")
        return (True, "Success")

    async def main():
        t1 = asyncio.create_task(task("Task A", 2))
        t2 = asyncio.create_task(task("Task B", 3))

        t1_resp = await t1  # Wait for Task A to finish
        t2_resp = await t2  # Wait for Task B to finish
        print(f"t1_resp: {t1_resp}, t2_resp: {t2_resp}")

        # or run task together using gather function;;
        # resp = await asyncio.gather(t1, t2)
        # print(f"resp: {resp}")

    asyncio.run(main())


def expl_v8():
    # checking asyncio multi-task independency;;
    async def task1():
        print("Task 1 started")
        await asyncio.sleep(10)
        print("Task 1 completed")
        return (True, "All OK")

    async def task2():
        print("Task 2 started")
        await asyncio.sleep(1)
        print("Task 2 completed")
        return (True, "All OK")

    async def main():
        t1 = asyncio.create_task(task1())
        t2 = asyncio.create_task(task2())
        result = await asyncio.gather(t1, t2)
        # above two line can be combined into one using below synatax;;
        # result = await asyncio.gather(task1(), task2())  # Run both tasks concurrently
        print(f"result: ", result)

    asyncio.run(main())


def expl_v7():
    # Multiprocessing exploration;;
    # def get_square(num):
    #     time_to_sleep = randint(1, 100)
    #     print(f"Processing going to sleep for {time_to_sleep} sec")
    #     print(f"Before returning ")
    #     return
    #
    # def square_list(nums):
    #     return [get_square(num) for num in nums]
    #
    # nums = [randint(1,100) for i in range(10)]
    # process = Process(square_list, args=(nums))
    # process.start()
    # process.join()


    def funA():
        for i in range(10**7):
            print(f"fun(A): {i}")
            sleep(3)
            print(f"func(A): Wait completed for iteration: {i}")

    def funB():
        for i in range(10**7):
            print(f"fun(B): {i}")
            sleep(3)
            print(f"func(B) : Wait completed for iteration: {i}")

    with multiprocessing.Pool() as pool:
        x = [1,2,3]
        r1 = pool.map(funA, x)
        r2 = pool.map(funB, x)

    print(f"Result: {r1}")
    print(f"Result: {r2}")


def expl_v6():
    # reduce combines everything into one;;
    # reduce(function, iterable[...])

    def test(a, b):
        a_s, b_s = sum(a), sum(b)
        r = a_s + b_s
        print(f"a: {a}, b: {b}, r: {r}")
        return r

    nums = [[i, i+1, i+2] for i in range(10)]
    print(f"nums: {nums}")

    x = reduce(test, nums)
    # x = reduce(lambda acc, triplet: msum(acc[0], acc[1], acc[2]) + msum(*triplet), nums)
    # x2= reduce(msum, map(lambda x: x+100, nums))
    # x3 = reduce(msum, map(lambda x: x+100, nums))

    print(f"x: {x}")


def expl_v5():
    # memomization in expl()
    def cache(func):
        def reading_cache(num):
            if num not in memory:
                memory[num] = func(num)
            return memory[num]

        # print(">>>>>>>>>>>>. func: ", func)
        # print(">>>>>>>>>>>> inspect.signature(func): ",inspect.signature(func))
        print(">>>>>>>>>>>> inspect.getsource(func): ",inspect.getsource(func))
        # print(">>>>>>>>>>>> inspect.getfullargspec(func): ",inspect.getfullargspec(func))
        # print(">>>>>>>>>>>> inspect.getdoc(func): ",inspect.getdoc(func))
        # print(">>>>>>>>>>>> inspect.getmembers(func): ",inspect.getmembers(func))
        # print(">>>>>>>>>>>> inspect.ismethod(func): ",inspect.ismethod(func))
        # print(">>>>>>>>>>>> inspect.isfunction(func): ",inspect.isfunction(func))
        # cur_frame = inspect.currentframe()
        # print(">>>>>>>>>>>> inspect.currentframe(): ", cur_frame)
        # print(">>>>>>>>>>>> inspect.getargvalues(func): ",inspect.getargvalues(func))
        # print(">>>>>>>>>>>> inspect.ismodule(func): ",inspect.ismodule(func))
        # print(">>>>>>>>>>>> inspect.isgeneratorfunction(func): ",inspect.isgeneratorfunction(func))

        return reading_cache

    @cache
    def fibo(num):
        global count
        count += 1
        if num <= 1:
            return 1
        return num * fibo(num-1)

    x1 = fibo(10)
    print(f"x1: {fibo(5)}, count: {count}")

    # without memoization : x1: 120, count: 15
    # with memomization : x1: 120, count: 10

    # --- INSPECT LIBRARY ENHANCEMENTS --- #
    # def a(n1, n2):
    #     print(f" >>>> inspect.getsource: {inspect.getsource(a)}")
    #     return n1+n2
    #
    # b = a(10, 20)
    # print(f"b result: ", b)


def expl_v4():
    # exploring datatime fromisoformat()
    dt = "2024-01-26T12:34:56"
    dt_result = datetime.fromisoformat(dt)
    print(f"dt_result: {dt_result}, dt_result_type: {type(dt_result)}, len: {len(dt)}")


def expl_v3():
    ##--------------------------------------------------------------
    # sys.argv
    ##--------------------------------------------------------------
    def lognow():
        print(f"DEBUG: {DEBUG}")

    options = sys.argv
    opt_len = len(options)
    print(">>>>> options: ", options, opt_len)
    if '-d' in options and opt_len == 4:
        DEBUG = strtobool(options[2])
    print(">>>>> options: ", options)
    lognow()
    print("Task Completed")


def expl_v2():

    # Anagram Problem
    def ans_v1(str1, str2):
        result = 0
        s1_map = {}
        s2_map = {}
        # hashmap for str1
        for s1 in str1:
            s1_map[s1] = s1_map[s1]+1 if s1 in s1_map else 1
        # hashmap for str2
        for s2 in str2:
            s2_map[s2] = s2_map[s2]+1 if s2 in s2_map else 1
        # counting the char
        print("s1", s1_map)
        print("s2", s2_map)
        for s, count in s1_map.items():
            if s in s2_map and s2_map[s] != s1_map[s]:
                result += abs(s2_map[s] - s1_map[s])
                print(f"for[{s}]::if::result: ", result)

            if not(s in s2_map):
                print(f"if::2:: s:{s} :: count: {s1_map[s]}")
                result += s1_map[s]

        for s, count in s2_map.items():
            if not(s in s1_map):
                print(f"if::2:: s2_s:{s} :: s2_count: {s2_map[s]}")
                result += s2_map[s]

        if len(s2_map) != len(s1_map):
            print("if::result: ", result)
            result += abs(len(s2_map) - len(s1_map))

        return result

    # --- main ---
    count  = 0
    tc = [('except', 'accept'), ('buy', 'bye')]
    for t1, t2, in tc:
        result = ans_v1(t1, t2)
        print(f"TC[{tc[count]}] : {result}")
        count += 1


def expl_v1():
    # Longest substring with k distinct problem
    def getLengthofLongestSubstring(ch, k):
        n = len(ch)
        i, j = 0, 0
        result = 0
        char_map = {}
        while(j < n):
            if len(char_map) <= k:
                char_map[ch[j]] = char_map[ch[j]] + 1 \
                    if ch[j] in char_map else 1
                result = max(result, sum(char_map.values()))
                j += 1
            else:
                while(len(char_map) > k):
                    if char_map[ch[i]] > 0:
                        char_map[ch[i]] -= 1
                    else:
                        char_map.pop(ch[i])
                    i += 1
        return result

    #--- main ---#
    tc = [('abcbc', 2), ('abcc', 1), ('abcba', 6), ('acbdab', 3)]
    for tc1, tc2 in tc:
        x = getLengthofLongestSubstring(tc1, tc2)
        print(f"for tc1: {tc1}, result: {tc2}")


if __name__ == "__main__":
    print("#------------ Code Start --------------#")
    startTime = time()
    expl()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")