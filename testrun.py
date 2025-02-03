import sys
import inspect
from distutils.util import strtobool
from datetime import datetime
from functools import reduce


DEBUG = True
count = 0
memory = {}


def expl():
    # def msum():
    #     print(f"a: {a}, b: {b}, c: {c}")
    #     return a+b+c

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
    expl()
