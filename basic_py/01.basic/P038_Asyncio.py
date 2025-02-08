import asyncio
from random import choice

rt_flag = choice([True, False])

async def task1():
    result = []
    for i in range(2):
        waiting_time = 10
        wlcm_msg = "Task 1 | Loading Next Stage ..." if i != 0 else "Task 1 | Loading ..."
        print(wlcm_msg)
        await asyncio.sleep(waiting_time)
        t1_rslt = input(f"Executing Task(1): Iteration({i}): Enter Input: ")
        result.append((rt_flag, t1_rslt))
    return result

async def task2():
    result = []
    for i in range(1):
        waiting_time = 3
        wlcm_msg = "Task 2 | Loading Next Stage ..." if i != 0 else "Task 2 | Loading ..."
        print(wlcm_msg)
        await asyncio.sleep(waiting_time)
        t2_rslt = input(f"Executing Task(2): Iteration({i}): Enter Input: ")
        result.append((rt_flag, t2_rslt))
    return result

async def main():
    # Create tasks
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    # Wait for both tasks to complete
    result = await asyncio.gather(t1, t2)
    print("result: ", result)

# Run the event loop
asyncio.run(main())

# output :
# Task 1 | Loading Next Stage ...
# Executing Task(2): Iteration(4): Enter Input: 1234
# Executing Task(1): Iteration(3): Enter Input: 1001
# Task 1 | Loading Next Stage ...
# Executing Task(1): Iteration(4): Enter Input: 19
# result:  [[(False, '10'), (False, '12'), (False, '123')]