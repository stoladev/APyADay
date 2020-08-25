"""
Extension of understanding threading in Python.
"""

import concurrent.futures
import time

start = time.perf_counter()


def sleep_a_bit(seconds):
    """
    Sleeps for x amount of seconds.

    With submit, it is submitting the functions once at a time.
    We can use a map method to run our function over a list of values.
    """

    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping after {seconds} seconds."


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]

    # MAP METHOD
    results = executor.map(sleep_a_bit, seconds)

    for result in results:
        print(result)

    # SUBMIT METHOD
    # results = [executor.submit(sleep_a_bit, second) for second in seconds]
    # for future in concurrent.futures.as_completed(results):
    #     print(future.result())

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")

