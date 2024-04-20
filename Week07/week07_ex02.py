# This script creates infinite iterators:
# iter1: returning 0, 1, 0, 1, 0, 1, ...,
# iter2: returning randomly 0 or 1,
# iter3: returning 0, 1, 0, -1, 0, 1, 0, -1, ...

import itertools
import random

iter1 = itertools.cycle([0, 1])


# made differently, I didn't know how to do it using itertools
def random_generator():
    while True:
        yield random.randint(0, 1)


iter2 = random_generator()

iter3 = itertools.cycle([0, 1, 0, -1])

# check if the iterators work:

for x in range(10):
    # print(f"First iterator: {next(iter1)}")
    # print(f"Second iterator: {next(iter2)}")
    print(f"Third iterator: {next(iter3)}")
