"""
A process is an instance of program (e.g. Jupyter notebook, Python
interpreter). Processes spawn threads (sub-processes) to handle subtasks like
reading keystrokes, loading HTML pages, saving files. Threads live inside
processes and share the same memory space.

When you open Word, you create a process. When you start typing, the process
spawns threads: one to read keystrokes, another to display text, one to
autosave your file, and yet another to highlight spelling mistakes. By spawning
multiple threads, Microsoft takes advantage of idle CPU time (waiting for
keystrokes or files to load) and makes you more productive.

Process
- Created by the operating system to run programs
- Processes can have multiple threads
- Two processes can execute code simultaneously in the same python program
- Processes have more overhead than threads
- Sharing information between processes is slower than sharing between threads
- Processes do not share memory space.
- Processes pickle data structures like arrays which requires IO time.

Thread
- Threads are like mini-processes that live inside a process
- They share memory space and efficiently read and write to the same variables
- Two threads shouldn't execute code simultaneously in the same python program

When to use threads vs processes?
- Processes speed up Python operations that are CPU intensive because they
benefit from multiple cores and avoid the GIL.
- Threads are best for IO tasks or tasks involving external systems because
threads can combine their work more efficiently. Processes need to pickle
their results to combine them which takes time.
- Threads provide no benefit in python for CPU intensive tasks because of GIL.
- For certain operations like Dot Product, Numpy works around Python’s GIL
and executes code in parallel.
"""

# Example (using threading, OLD method of doing this. Pools (below) are better
import time
import threading

start = time.perf_counter()


def do_something(seconds):
    """
    Sleeps for x seconds, printing before and after.
    """
    print(f"Sleeping for {seconds} second(s).")
    time.sleep(seconds)
    print("Done sleeping.")


threads = []

for _ in range(5):
    thread = threading.Thread(target=do_something, args=[1.5])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")

