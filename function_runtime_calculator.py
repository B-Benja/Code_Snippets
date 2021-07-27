# using a decorator function to calculate the runtime of any function
# comparing the fast_function runtime with the slow_function runtime

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def time_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}")
    return time_function


@speed_calc_decorator
def fast_function():
    # just an example function
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    # just an example function
    for i in range(100000000):
        i * i


slow_function()
fast_function()