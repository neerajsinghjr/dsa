import asyncio

async def task1():
    for i in range(5):
        print(f'Task 1 - Step {i}')
        await asyncio.sleep(1)

async def task2():
    for i in range(5):
        print(f'Task 2 - Step {i}')
        await asyncio.sleep(1)

async def main():
    # Create tasks
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    # Wait for both tasks to complete
    await asyncio.gather(t1, t2)

# Run the event loop
asyncio.run(main())