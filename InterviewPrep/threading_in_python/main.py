"""Small Code Example Using threading"""
# This example will start two threads. Each thread will perform a simple (but somewhat slow)
# counting task.
# We'll see that even though we start two threads, the total time taken
# isn't halved on a multi-core machine,
# illustrating the GIL's effect for CPU-bound work.

import threading
import time


# A simple function that simulates some CPU work (counting)
def count_intensively(name, count_to):
    """A simple function that simulates some CPU work (counting)"""
    print(f"Thread {name}: Starting to count.")
    counter = 0
    for i in range(count_to):
        counter += 1  # Just doing some work
    print(f"Thread {name}: Finished counting to {count_to}.")


# --- Main part of the script ---
if __name__ == "__main__":
    COUNT_TARGET = 25_000_000  # A large number to make it take some time

    start_time = time.time()

    # Create two thread objects
    # target= specifies the function the thread should run
    # args= is a tuple of arguments to pass to that function
    thread1 = threading.Thread(target=count_intensively, args=("A", COUNT_TARGET))
    thread2 = threading.Thread(target=count_intensively, args=("B", COUNT_TARGET))

    print("Main: Starting threads...")
    # Start the threads - they become ready to run
    thread1.start()
    thread2.start()

    print("Main: Waiting for threads to finish...")
    # Wait for thread1 to complete its execution
    thread1.join()
    # Wait for thread2 to complete its execution
    thread2.join()

    end_time = time.time()
    print(f"Main: All threads finished.")
    print(f"Total execution time: {end_time - start_time:.4f} seconds")
