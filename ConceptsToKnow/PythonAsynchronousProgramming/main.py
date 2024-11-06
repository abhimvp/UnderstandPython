import asyncio

# another way to use async await keywords


async def foo(text):
    print(text)
    # pausing the execution of function for 3 seconds
    await asyncio.sleep(3)  # returns a co-routine and used await to run it
    print("done")
    return text


async def foo_runNext(text):
    print(text)
    # pausing the execution of function for 3 seconds
    await asyncio.sleep(1)  # returns a co-routine and used await to run it
    print("done_runNext")


# co-routine example - put async before function definition
async def get_data():
    print("Start")
    await asyncio.sleep(1)
    # await foo("abhi")
    task = asyncio.create_task(foo_runNext("abhi_next"))  # creates a task object
    # basically the above one starts running and doesn't wait for foo("abhi") to complete & allow other code to run
    await asyncio.sleep(
        5
    )  # waits for 5 second - runs the above foo_run immediately as there is delay in this step
    # await task  # waits for foo_runNext("abhi_next") to complete & then allow other code to run
    print("End")


# when you run the above function , it will return a coroutine object ,
# you need to run the coroutine object using await to run the function
# to use the await keyword it must be inside of a asynchrous function

# we need to create a async event-loop to run the async programs
asyncio.run(get_data())  # created an event loop and added the coroutine object
# to the events loop and ran it
