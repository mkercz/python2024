# This script creates infinite generators for even numbers, odd numbers and
# powers of k. The generators are then used in examples, with breaks after 20.

def iter_even():
    x = 0
    while True:
        yield x
        x += 2


def iter_odd():
    x = 1
    while True:
        yield x
        x += 2


def iter_power(k):
    x = 1
    while True:
        yield x
        x = x * k


print("Even numbers:")
for i in iter_even():
    print(i)
    if i > 20:
        break

print("Odd numbers:")
for i in iter_odd():
    print(i)
    if i > 20:
        break

print("Powers of k:")
for i in iter_power(3):
    print(i)
    if i > 20:
        break
