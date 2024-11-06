import asyncio


async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {"data": 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())  # A coroutine wrapped in a Future.
    # if a coroutine you defined returns a value , this creates a future
    # future is like a promise in javascript - placeholder for a value that will exist in the future
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    # without await , we will see followiing thing when we run this code
    # python tasks.py
    # <Task pending name='Task-2' coro=<fetch_data() running at C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\ConceptsToKnow\PythonAsynchronousProgramming\tasks.py:3>>
    # start fetching
    # 0
    # here we haven't await task-2 yet
    print(value)
    await task2  # wait for task2 to complete


# $ python tasks.py
# start fetching
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# done fetching
# {'data': 1}
# 8
# 9

# we started task1
# we started task2
# then we see await statement `value=await task1` - this tells our program
# hey we gotta wait for the task1 to finish running before we move any further down
# so we start task1 and we see delay in task1 for 2 seconds
# as soon as this task is delayed , this other task2 part of our event loop , then is allowed to start running
# so it starts running , it delays for 0.25 seconds and checks if it can give back execution to other tasks
# it looks at other tasks they're still delayed and it keeps running
# we can see it only print's done fetching of task1 at time 8 as delay of 2 seconds is done and gives the executionn back to the function task1


asyncio.run(main())
