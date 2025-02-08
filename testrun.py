'''
-------------------------------------------------------------------------------------
-> Title: Testrun
-> Attempted: 04-02-2025
-> Description:
-------------------------------------------------------------------------------------

Exploratory testrun file for python;;

-------------------------------------------------------------------------------------
'''
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
from distutils.util import strtobool


DEBUG = True
count = 0
memory = {}


def expl():
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