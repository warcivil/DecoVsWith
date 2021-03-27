#
# and why 'with' faster 'decorator'?
#

import time
import random
class A:
    def __init__(self):
        self.final = 0
    def __enter__(self):
        self.time_now = time.time()
        return self
    def __exit__(self, ex_type, ex_val, ex_tb):
        print(f"time_now with = {time.time()-self.time_now}")
    def calls(self):
        random.randint(1000, 1000005) / random.randint(1000, 1000000)
        
with A() as oops:
    for i in range(1000):
        oops.calls()


def timer(func):
    def wrapper(a):
        time_now = time.time()
        for _ in range(1000):
            func(a)
        print(f"time now deco = {time.time()-time_now}")
    return wrapper

@timer
def f(a=1):
    return random.randint(1000, 1000005) / random.randint(1000, 1000000)

f(2)
