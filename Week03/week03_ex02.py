# This script loops over range 1-40 and checks the divisibility of the numbers
# by 5 and 7. There are two solutions: with a 'for' loop and a 'while' loop.

print("Solution with a 'for' loop:")
for x in range(1,41):
    if x == 13:
        continue
    if x % 5 == 0 and x % 7 == 0:
        print(f"{x} is divided by 5 and 7")
    elif x % 5 == 0:
        print(f"{x} is divided by 5")
    elif x % 7 == 0:
        print(f"{x} is divided by 7")
    else:
        print(f"{x} is not important")

print("\n" + "Solution with a 'while' loop:")

x = 1
while x < 41:
    if x == 13:
        x += 1
        continue
    if x % 5 == 0 and x % 7 == 0:
        print(f"{x} is divided by 5 and 7")
    elif x % 5 == 0:
        print(f"{x} is divided by 5")
    elif x % 7 == 0:
        print(f"{x} is divided by 7")
    else:
        print(f"{x} is not important")
    x += 1