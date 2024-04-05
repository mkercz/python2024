# This script contains a function random_walk that creates an infinite
# generator for a 1D random walker. The generator is then executed with a
# starting position x = 0 and the resulting position after 100 steps is printed.

import random
import itertools


def random_walk(position):
    while True:
        step = random.choice([-1, 1])
        position += step
        yield position


result = next(itertools.islice(random_walk(0), 100, None)) # islice(iterable,
# start, stop)

print("The position after 100 iterations is {}".format(result))
